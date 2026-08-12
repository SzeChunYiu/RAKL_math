from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/yang_mills/09_trace/ym_r20k1_c001_source_result_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("ym_r20k1_c001_source_result", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_ym_k1_c001_documents_match_fixture_and_framework_schemas() -> None:
    module = _module()
    docs = module.build_documents(ROOT)
    for key, relative in module.PATHS.items():
        assert json.loads((ROOT / relative).read_text()) == docs[key]
    for key, schema_name in (
        ("failure", "failure-experience-lattice.schema.json"),
        ("trace", "math-research-trace.schema.json"),
    ):
        schema = json.loads((ROOT / "framework/RAKL/schemas" / schema_name).read_text())
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(docs[key])


def test_ym_k1_c001_fails_closed_on_source_scope_but_proves_only_abstract_lemma() -> None:
    docs = _module().build_documents(ROOT)
    source, result = docs["source"], docs["result"]
    assert source["classified_branch"] == "SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT"
    assert source["source_boundary"]["global_source_absence_claim"] is False
    assert source["obligation_results"] == {
        "O1-SOURCE-UNIFORMITY": "NOT_DISCHARGED_BY_ACQUIRED_EVIDENCE",
        "O4-NORM-AND-SCALE-SCOPE": "NOT_DISCHARGED_BY_ACQUIRED_EVIDENCE",
    }
    assert result["classified_branch"] == source["classified_branch"]
    assert result["candidate_truth_status"] == "TARGET_APPLICATION_NOT_ESTABLISHED_NOT_REFUTED"
    assert result["authorized_order_execution"][-1]["result"] == "NOT_IMPORTED_NOT_EXECUTED_AFTER_EARLIER_SOURCE_BRANCH"
    lemma = result["abstract_scalar_proposition"]
    assert lemma["authority"] == "ELEMENTARY_ABSTRACT_PROOF_NOT_FORMALIZED"
    assert lemma["target_application_authority"] == "NONE_WITHOUT_O1_AND_O4"
    assert any("delta_L" in step for step in lemma["existence_neighborhood_proof"])
    assert any("delta_M" in step for step in lemma["existence_neighborhood_proof"])
    assert any("g_{k+1}^2>=g_k^2" in step for step in lemma["conditional_composition_proof"])


def test_ym_k1_c001_retains_seven_field_math_lesson_failure_scope_and_open_root() -> None:
    module = _module()
    docs = module.build_documents(ROOT)
    lesson = docs["lesson"]
    required = {
        "attempted_mathematical_implication",
        "exact_mathematical_result_or_failure",
        "supported_and_competing_mathematical_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_discriminator",
        "proof_or_source_evidence",
    }
    assert required <= set(lesson)
    assert "does not claim the inaccessible source globally lacks" in lesson["scope"]
    experience = docs["failure"]["experiences"][0]
    assert experience["diagnosis_status"] == "SUPPORTED"
    assert "no source-wide absence" in experience["selected_diagnosis"]
    assert docs["dag"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert docs["dag"]["nodes"][0]["status"] == "PROVED_BY_ELEMENTARY_CONTINUITY_AND_INEQUALITY_ARGUMENT"
    assert docs["dag"]["nodes"][2]["status"] == "NOT_ESTABLISHED_NOT_REFUTED"
    entries = docs["trace"]["entries"]
    assert [entry["event_type"] for entry in entries[-4:]] == [
        "PROOF_CHECKED",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
        "REVIEWED",
    ]
    previous = ""
    for entry in entries:
        assert entry["previous_event_hash"] == previous
        payload = dict(entry)
        declared = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert declared == module.canonical_hash(payload)
        previous = declared
