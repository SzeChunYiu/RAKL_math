from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/birch_swinnerton_dyer/09_trace/bsd_r16_cassels_tate_result_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("bsd_r16_result", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_bsd_r16_result_documents_match_fixture_and_schemas() -> None:
    module = _module()
    docs = module.build_documents(ROOT)
    for key, relative in module.PATHS.items():
        assert json.loads((ROOT / relative).read_text()) == docs[key]
    schema_pairs = (
        ("failure", "failure-experience-lattice.schema.json"),
        ("transformation_memory", "obstruction-transformation-memory.schema.json"),
        ("shortcut", "obstruction-transformation-review.schema.json"),
        ("trace", "math-research-trace.schema.json"),
    )
    for key, schema_name in schema_pairs:
        schema = json.loads((ROOT / "framework/RAKL/schemas" / schema_name).read_text())
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(docs[key])


def test_bsd_r16_result_is_mathematical_and_scoped() -> None:
    docs = _module().build_documents(ROOT)
    source, lesson, failure = docs["source"], docs["lesson"], docs["failure"]
    assert source["classified_branch"] == "PAIRING_DESCENDS_ONLY_TO_QUOTIENT_NO_DIVISIBLE_CORANK_CONTROL"
    countermodel = source["exact_group_countermodel"]
    assert countermodel["maximal_divisible_subgroup"] == "M_div=M"
    assert countermodel["quotient"] == "M_nd=M/M_div=0"
    assert "r=1" in countermodel["checks"][-1]
    required = {
        "attempted_mathematical_implication", "exact_mathematical_result_or_failure",
        "supported_and_competing_mathematical_causes", "scope", "mathematical_falsifier",
        "repair_or_next_discriminator", "proof_or_source_evidence",
    }
    assert required <= set(lesson)
    assert lesson["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert failure["experiences"][0]["diagnosis_status"] == "VERIFIED_IMPOSSIBILITY"
    assert "countermodel is logical" in failure["experiences"][0]["scope_conditions"][2]
    assert "reuse remains allowed" in failure["experiences"][0]["scope_conditions"][3]
    assert docs["dag"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_bsd_r16_source_binding_and_trace_chronology_are_exact() -> None:
    module = _module()
    docs = module.build_documents(ROOT)
    source = docs["source"]["source"]
    assert source["arxiv_id"] == "math/9911267v1"
    assert source["pdf_sha256"] == "a7f6b91f8dbc38d8c061fc8aa2c2848a1ed503cb0dbe91c5bd1a6f6ef9dff804"
    assert source["pdf_bytes"] == 399391
    entries = docs["trace"]["entries"]
    assert [entry["event_type"] for entry in entries[-4:]] == ["FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"]
    previous = ""
    for entry in entries:
        assert entry["previous_event_hash"] == previous
        payload = dict(entry)
        declared = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert declared == module.canonical_hash(payload)
        previous = declared
