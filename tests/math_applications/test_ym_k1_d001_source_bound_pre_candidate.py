from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker
from rakl.schema_reference_constraints import check_reference_constraints


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FIXTURE = YM / "09_trace/ym_k1_d001_source_bound_pre_candidate_fixture.py"
SCHEMAS = ROOT / "framework/RAKL/schemas"


def module():
    spec = importlib.util.spec_from_file_location("ym_k1_d001_pre", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_documents_regenerate_from_exact_current_main_and_framework() -> None:
    m = module()
    docs = m.build_documents()
    assert set(docs) == set(m.PATHS)
    assert m.APPLICATION_BASE_SHA == "334c3cf0a405906fe14b07067d6d7f73b6170d4f"
    assert m.FRAMEWORK_SHA == "d21592b0ff8da988deabb923fd549891ff8ad9f0"
    for name, path in m.PATHS.items():
        assert json.loads(path.read_text()) == docs[name], name


def test_primary_source_identity_hashes_and_exact_passage_ranges_are_bound() -> None:
    audit = module().build_documents()["source_audit"]
    source = audit["source_identity"]
    assert source["author"] == "Jonathan J. Wilson"
    assert source["zenodo_version_doi"] == "10.5281/zenodo.19393832"
    assert source["zenodo_concept_doi"] == "10.5281/zenodo.19393831"
    assert source["authority"] == "PRIMARY_AUTHOR_OPEN_ARTIFACT_NOT_INDEPENDENT_PEER_REVIEW"
    files = {row["filename"]: row["sha256"] for row in audit["source_files"]}
    assert files == {
        "4D GZ-Yang-Mills.pdf": "08013e1ce75c8b2be79c62ba61f70e30024b9bb427c465ceab7ee9266236690d",
        "GZYM_submission_final.tex": "ef936e502e84b0cafabc594c9705c16c9c1df29dc95f2a6a679b6b446c526c18",
    }
    passages = {row["passage_id"]: row for row in audit["passage_bindings"]}
    assert passages["WILSON-40.3-K-CONTRACTION"]["pdf_pages"] == [145, 146]
    assert passages["WILSON-40.3-K-CONTRACTION"]["tex_lines"] == [9554, 9571]
    assert passages["WILSON-40.5-GRAPH-DOMAIN-AND-CONSTANT-CHOICE"]["tex_lines"] == [9595, 9662]
    assert passages["WILSON-40.5-FACTOR-TWO-TRANSPORT"]["tex_lines"] == [9665, 9680]
    assert passages["WILSON-A.15-POLYMER-NORM"]["pdf_pages"] == [172]
    assert passages["WILSON-A.15-POLYMER-NORM"]["tex_lines"] == [11481, 11499]


def test_source_exposure_is_superseded_by_two_supported_mathematical_gaps() -> None:
    docs = module().build_documents()
    audit = docs["source_audit"]
    lesson = docs["lesson"]
    assert audit["classification"] == "STRONGER_PREMISE_MISMATCH"
    assert audit["supersession"]["prior_source_exposure_diagnosis"] == "SUPERSEDED_BY_OPEN_PRIMARY_SOURCE"
    assert audit["uniformity_assessment"]["norm_transport"] == "EXPLICIT_K_TO_K_PLUS_1_SCALE_INDEXED_NORM"
    assert audit["uniformity_assessment"]["joint_exact_graph_ball_applicability"] == "NOT_ESTABLISHED"
    gaps = {row["gap_id"]: row for row in audit["supported_gaps"]}
    assert set(gaps) == {"A-DOMAIN-RADIUS-COMPATIBILITY", "B-FACTOR-TWO-FLOW-COMPARISON"}
    assert "4C/(1-rho)>C" in gaps["A-DOMAIN-RADIUS-COMPATIBILITY"]["displayed_same_C_consequence"]
    assert "(1+rho)c_K g_{k+1}^2" in gaps["B-FACTOR-TWO-FLOW-COMPARISON"]["observation"]
    assert lesson["classification"] == "STRONGER_PREMISE_MISMATCH"
    assert "not a refutation" in lesson["exact_mathematical_result_or_failure"].lower()
    assert "mass gap" in lesson["scope"].lower()


def test_cheapest_discriminator_is_staged_and_not_executed_or_reinterpreted() -> None:
    docs = module().build_documents()
    audit = docs["source_audit"]
    next_step = audit["cheapest_future_discriminator"]
    assert next_step["stage_1_test"] == "4*C_force/(1-rho) <= C_dom"
    assert next_step["stage_2_only_if_stage_1_passes"].startswith("On a separately frozen coupling interval")
    assert next_step["not_executed_here"] is True
    assert audit["future_candidate_identity"] is None
    assert audit["candidate_generation_allowed"] is False
    gap_a = audit["supported_gaps"][0]
    assert "does not reinterpret" in gap_a["no_reinterpretation_rule"]
    shortcut = docs["shortcut_review"]
    assert shortcut["selected_mode"] == "CANNOT_CHECK"
    assert shortcut["selected_episode_ids"] == []
    assert shortcut["missing_transformation_specification"] is None


def test_pre_candidate_trace_is_hash_chained_and_contains_no_candidate_event() -> None:
    docs = module().build_documents()
    trace = docs["trace"]
    expected = [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert [entry["event_type"] for entry in trace["entries"]] == expected
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        unsigned = dict(entry)
        actual = unsigned["artifact_hash"]
        unsigned["artifact_hash"] = ""
        assert actual == module()._sha(unsigned)
        previous = actual
    text = json.dumps(trace, sort_keys=True)
    assert "CANDIDATE_PROPOSED" not in text
    assert "FALSIFIER_RUN" not in text
    assert "PROOF_CHECKED" not in text
    assert trace["entries"][-1]["outputs"] == ["NO_SUCCESSOR_CANDIDATE_IDENTITY", "CANDIDATE_GENERATION_BLOCKED"]


def test_seven_field_lesson_is_mathematical_and_software_gets_zero_credit() -> None:
    lesson = module().build_documents()["lesson"]
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
    assert lesson["future_candidate_identity"] is None
    assert lesson["candidate_generation_allowed"] is False
    assert set(lesson["zero_mathematical_credit"]) >= {
        "Git/branch/PR state",
        "CI/tests",
        "schemas/hashes/chronology",
        "telemetry/repository growth",
    }


def test_framework_schemas_and_failure_link_endpoints_close() -> None:
    docs = module().build_documents()
    schema_map = {
        "context": "math-context-fiber.schema.json",
        "memory": "research-memory-review.schema.json",
        "transformation_memory": "obstruction-transformation-memory.schema.json",
        "shortcut_review": "obstruction-transformation-review.schema.json",
        "trace": "math-research-trace.schema.json",
        "failure": "failure-experience-lattice.schema.json",
    }
    for name, schema_name in schema_map.items():
        schema = json.loads((SCHEMAS / schema_name).read_text())
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(docs[name])
        if name == "failure":
            assert check_reference_constraints(docs[name], schema) == ()
    failures = {row["failure_id"] for row in docs["failure"]["experiences"]}
    link = docs["failure"]["links"][0]
    assert link["source_id"] in failures
    assert link["target_id"] in failures
    assert link["relation"] == "SUPERSEDES_DIAGNOSIS"


def test_same_context_review_is_not_mislabeled_independent() -> None:
    review = module().build_documents()["expert_review"]
    assert review["review_independence"] == "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW"
    assert {row["role"] for row in review["roles"]} == {
        "domain_theory_lead",
        "analogy_method_transfer_lead",
        "adversarial_falsification_lead",
        "formal_methods_lead",
        "novelty_research_value_lead",
    }
    assert review["candidate_generation_allowed"] is False
    assert review["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
