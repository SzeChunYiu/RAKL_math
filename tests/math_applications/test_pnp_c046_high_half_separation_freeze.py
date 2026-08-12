from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c046_high_half_separation_candidate_fixture.py"
VERIFIER = PNP / "09_trace/verify_c046_candidate_freeze_packet.py"
EVALUATOR = PNP / "05_falsification/c046_high_half_separation_evaluator.py"

ARTIFACTS = {
    "candidate": PNP / "04_candidates/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_LEMMA_FREEZE_20260812.json",
    "evaluator_manifest": PNP / "05_falsification/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_EVALUATOR_FREEZE_20260812.json",
    "authorization": PNP / "09_trace/O9d12a2a1b_C046_EVALUATION_AUTHORIZATION_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C046_CANDIDATE_FREEZE_TRACE_20260812.json",
    "receipt": PNP / "09_trace/O9d12a2a1b_C046_CANDIDATE_FREEZE_RECEIPT_20260812.json",
    "feedback": PNP / "10_feedback/C046_INVARIANT_FEASIBILITY_FIRST_APPLICATION_FEEDBACK_PROPOSAL_20260812.json",
}


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_c046_candidate_packet_matches_fixture_and_public_freeze_parent() -> None:
    fixture = _module("pnp_c046_candidate_fixture", FIXTURE)
    expected = fixture.build_documents()
    assert set(expected) == set(ARTIFACTS)
    for name, path in ARTIFACTS.items():
        assert path.is_file(), path
        assert _load(path) == expected[name]
    assert fixture.APPLICATION_BASE_SHA == "ac8c0745be8aed791a446fd55fcf5154cac01962"
    assert fixture.PRE_CANDIDATE_FREEZE_SHA == "538d689390fb60d30cba31863c1b73cc1716036e"
    assert fixture.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"


def test_c046_candidate_is_a_mathematical_partition_lemma_not_a_target_result() -> None:
    candidate = _load(ARTIFACTS["candidate"])
    assert candidate["candidate_id"] == "C046-HIGH-HALF-SEPARATION-LEMMA-v1"
    assert candidate["candidate_kind"] == "MATHEMATICAL_LEMMA_CANDIDATE"
    assert candidate["statement"] == {
        "quantifier": "for every integer n >= 17",
        "old_row_projection": "Rows(U_n) is a subset of [0, 2^(n-1))",
        "canonical_prefix_projection": "every length-2n canonical MAGIC word has n-bit prefix in [2^(n-1), 2^n)",
        "conclusion": "Rows(U_n) is disjoint from the set of canonical MAGIC n-bit prefixes",
        "collision_consequence": "there is no finite canonical UNSAT prefix-row collision level in the frozen one-sided family",
    }
    assert candidate["proof_obligations"] == [
        "BASE_U3_ROW_PROJECTION",
        "INDUCTIVE_SUPPORT_QUADRANT_CONTAINMENT",
        "MAGIC_LEADING_BIT_PREFIX_CONTAINMENT",
        "DISJOINT_HALF_INTERVAL_CONCLUSION",
    ]
    assert candidate["falsifiers"] == [
        "a U3 complement edge has row >= 4",
        "a recursive complement clause creates support with row >= 2^(n-1)",
        "a canonical MAGIC word has leading bit 0",
        "a canonical prefix belongs to both half intervals",
        "the source family, encoding, or coordinate embedding differs from the frozen identities",
    ]
    assert candidate["target_access"] == {
        "decoder_imported_or_executed": False,
        "evaluator_imported_or_executed": False,
        "later_target_enumerated": False,
        "later_target_result_accessed": False,
        "finite_collision_level_selected": False,
    }
    assert candidate["credit_boundary"] == {
        "candidate_mathematical_content": "lemma/construction/assumptions/transfer conditions/falsifiers",
        "assurance_only_zero_credit": [
            "Git/branch/PR chronology",
            "CI/tests",
            "schemas/hashes/serialization",
            "runtime and evaluator wiring",
        ],
        "candidate_freeze_mathematical_saturation_credit": False,
        "candidate_freeze_mathematical_result_credit": False,
    }


def test_c046_evaluator_is_inert_and_authorization_forbids_execution() -> None:
    manifest = _load(ARTIFACTS["evaluator_manifest"])
    authorization = _load(ARTIFACTS["authorization"])
    source = EVALUATOR.read_text(encoding="utf-8")
    assert manifest["status"] == "FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED"
    assert manifest["evaluator"]["raw_sha256"] == hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    assert manifest["mathematical_obligations_only"] is True
    assert manifest["target_result_capability"] is False
    assert "BASE_U3_ROW_PROJECTION" in source
    assert "BASE_U2_ROW_PROJECTION" not in source
    assert authorization == {
        **authorization,
        "current_task_evaluator_execution_authorized": False,
        "later_target_access_authorized": False,
        "finite_target_scan_authorized": False,
        "allowed_next_action": "PUBLICLY_FREEZE_THIS_EXACT_CANDIDATE_AND_EVALUATOR_BEFORE_ANY_LATER_CHECK",
    }
    for forbidden in (
        "C041_fx_sat_one_sided",
        "decode_formula",
        "is_satisfiable",
        "materialize_complement",
        "importlib",
        "subprocess",
    ):
        assert forbidden not in source


def test_c046_trace_appends_candidate_after_pre_candidate_hash_chain() -> None:
    trace = _load(ARTIFACTS["trace"])
    assert len(trace["entries"]) == 9
    assert trace["entries"][-1]["event_type"] == "CANDIDATE_PROPOSED"
    assert trace["entries"][-1]["outputs"][:3] == [
        "C046-HIGH-HALF-SEPARATION-LEMMA-v1",
        "MATHEMATICAL_LEMMA_CANDIDATE",
        "TARGET_RESULT_UNACCESSED",
    ]
    assert trace["entries"][-1]["previous_event_hash"] == trace["entries"][-2]["artifact_hash"]
    text = json.dumps(trace, sort_keys=True)
    assert "RESULT_RECORDED" not in text
    assert "FALSIFIER_RUN" not in text


def test_c046_feedback_is_proposal_only_and_requires_fresh_self_rakl_assurance() -> None:
    feedback = _load(ARTIFACTS["feedback"])
    assert feedback["status"] == "APPLICATION_FEEDBACK_PROPOSAL_ONLY_NOT_PROMOTED"
    assert feedback["trigger"] == "ONLY_IF_THE_C046_HIGH_HALF_SEPARATION_LEMMA_LATER_VALIDATES"
    assert feedback["proposed_method_lesson"] == (
        "Before searching later finite targets for a desired collision or property, first test family-wide feasibility with an invariant or partition lemma."
    )
    assert feedback["authority"] == {
        "theorem_authority": False,
        "framework_evolution_authority": False,
        "method_promotion_authority": False,
        "inventory_mutation_allowed": False,
        "failure_lattice_mutation_allowed": False,
        "fresh_self_rakl_assurance_required_before_framework_change": True,
        "same_context_review_is_independent": False,
    }
    assert feedback["credit"] == {
        "primary_mathematical_lesson_is_the_separation_lemma": True,
        "feedback_transport_mathematical_saturation_credit": False,
        "feedback_transport_mathematical_result_credit": False,
    }


def test_c046_candidate_verifier_passes_and_detects_stale_mutation(tmp_path: Path) -> None:
    verifier = _module("pnp_c046_candidate_verifier", VERIFIER)
    assert verifier.audit_packet(ROOT) == ()
    verifier.verify_packet(ROOT)

    for name, source_path in ARTIFACTS.items():
        target = tmp_path / source_path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source_path.read_bytes())
    target_eval = tmp_path / EVALUATOR.relative_to(ROOT)
    target_eval.parent.mkdir(parents=True, exist_ok=True)
    target_eval.write_bytes(EVALUATOR.read_bytes())
    candidate = _load(tmp_path / ARTIFACTS["candidate"].relative_to(ROOT))
    candidate["statement"]["old_row_projection"] = "HOSTILE_WEAKENING"
    (tmp_path / ARTIFACTS["candidate"].relative_to(ROOT)).write_text(
        json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    assert any("candidate" in error and "digest mismatch" in error for error in verifier.audit_packet(tmp_path))
