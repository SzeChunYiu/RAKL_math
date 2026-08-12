from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
EVALUATOR = YM / "05_oracles/ym_k1_d001_c001_two_stage_evaluator.py"
FIXTURE = YM / "09_trace/ym_k1_d001_c001_stage_a_result_fixture.py"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_frozen_planted_worlds_route_exactly() -> None:
    m = load(EVALUATOR, "ym_k1_d001_c001_evaluator")
    worlds = {
        "pass": m.EvaluationWorld(m.StageADerivation.SEPARATE_CONSTANTS, True, True, m.StageBProof.EXACT_INTERVAL_MARGIN),
        "conflated": m.EvaluationWorld(m.StageADerivation.CONFLATED_SOURCE_CONSTANT, False, False, m.StageBProof.NOT_ENTERED),
        "factor_two": m.EvaluationWorld(m.StageADerivation.SEPARATE_CONSTANTS, True, True, m.StageBProof.FACTOR_TWO_ONLY),
        "cannot": m.EvaluationWorld(m.StageADerivation.INSUFFICIENT, None, False, m.StageBProof.NOT_ENTERED),
    }
    assert {key: m.evaluate(world).branch.value for key, world in worlds.items()} == {
        "pass": "APPLICABLE_BRIDGE",
        "conflated": "STRONGER_PREMISE_MISMATCH_A",
        "factor_two": "FLOW_MARGIN_FAIL_B",
        "cannot": "CANNOT_CHECK",
    }


def test_target_stage_a_is_literal_conflated_source_world_and_stage_b_is_closed() -> None:
    f = load(FIXTURE, "ym_k1_d001_c001_stage_a_fixture")
    result = f.build_documents()["result"]
    assert result["classified_branch"] == "STRONGER_PREMISE_MISMATCH_A"
    assert result["stage_a"]["literal_source_binding"] == "C_dom=C_force=C"
    assert result["stage_a"]["symbolic_ratio"] == "c_K/C_dom=4/(1-rho)>4>1"
    assert result["stage_b"]["entered"] is False
    assert result["stage_b"]["g_star_selected"] is False
    assert result["run_type"] == "RETROSPECTIVE_REPRODUCTION_NOT_PROSPECTIVE_DISCOVERY"
    assert result["strict_rakl_discovery_chronology"] is False
    assert result["authority"]["strict_rakl_discovery_authority"] is False


def test_source_passages_preserve_quantifiers_and_competing_causes() -> None:
    f = load(FIXTURE, "ym_k1_d001_c001_stage_a_fixture_passages")
    source = f.build_documents()["source_result"]
    assert source["source_identity"]["tex_sha256"] == "ef936e502e84b0cafabc594c9705c16c9c1df29dc95f2a6a679b6b446c526c18"
    assert source["lemma_40_3_quantifier_audit"]["quantified_statement"] == (
        "exists rho in (0,1), C>0, g_star>0 such that forall admitted k,g_k,K_k, "
        "||KF_k(u_k,K_k)||_(k+1)<=rho||K_k||_k+C g_k^4 on ||K_k||_k<=C g_k^2"
    )
    statuses = {row["diagnosis"]: row["status"] for row in source["competing_mathematical_diagnoses"]}
    assert statuses["NOTATION_OVERLOAD_HIDES_SEPARATE_COMPATIBLE_CONSTANTS"] == "UNSUPPORTED_BY_BOUND_SOURCE"
    assert statuses["ADJUSTABLE_ABSOLUTE_BALL_OR_NORM_RESCALING_REPAIRS_DOMAIN"] == "NOT_MAPPED_TO_LEMMA_40_3_GRAPH_BALL"
    assert statuses["LATER_SOURCE_LEMMA_PROVES_THE_MISSING_COMPARISON"] == "NOT_FOUND_IN_FULL_BOUND_TEX_SEARCH"


def test_seven_field_lesson_is_mathematical_and_operations_get_zero_credit() -> None:
    f = load(FIXTURE, "ym_k1_d001_c001_stage_a_fixture_lesson")
    lesson = f.build_documents()["lesson"]
    required = {
        "attempted_mathematical_implication",
        "exact_mathematical_result_or_failure",
        "supported_and_competing_mathematical_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_discriminator",
        "proof_or_source_evidence",
    }
    assert required <= lesson.keys()
    assert "CI/tests" in lesson["zero_mathematical_credit"]
    assert lesson["framework_method_implication_proposal"]["status"] == "QUARANTINED_PROPOSAL_ONLY"


def test_same_context_review_resolves_mathematical_objections_without_claiming_independence() -> None:
    f = load(FIXTURE, "ym_k1_d001_c001_stage_a_fixture_review")
    review = f.build_documents()["review"]
    assert review["review_independence"] == "SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW"
    assert {row["role"] for row in review["role_reviews"]} == {
        "DOMAIN_THEORY_LEAD",
        "ANALOGY_METHOD_TRANSFER_LEAD",
        "ADVERSARIAL_FALSIFICATION_LEAD",
        "FORMAL_METHODS_LEAD",
        "NOVELTY_RESEARCH_VALUE_LEAD",
    }
    assert review["blocking_concerns"] == []
    assert review["verdict"] == "INTERNALLY_READY_FOR_SCOPED_STAGE_A_RESULT_PR"


def test_generated_receipts_and_hashes_are_exact() -> None:
    f = load(FIXTURE, "ym_k1_d001_c001_stage_a_fixture_hash")
    documents = f.build_documents()
    for key, path in f.OUTPUTS.items():
        observed = json.loads(path.read_text())
        assert observed == documents[key]
        unsigned = dict(observed)
        actual = unsigned["artifact_hash"]
        unsigned["artifact_hash"] = ""
        assert actual == "sha256:" + hashlib.sha256(f.canonical(unsigned)).hexdigest()
