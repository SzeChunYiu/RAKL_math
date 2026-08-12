from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c053_k32_clean_phase_candidate_freeze_fixture.py"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C053_K32_CLEAN_PHASE_COMPATIBILITY_IDENTITY_20260812.json"
EVALUATOR = PNP / "05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATOR_IDENTITY_20260812.json"
FALSIFIER = PNP / "05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_FALSIFIER_IDENTITY_20260812.json"
RECEIPT = PNP / "09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_CANDIDATE_FREEZE_RECEIPT_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c053_k32_clean_phase_candidate_freeze", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_documents_match_inert_fixture_and_exact_public_base() -> None:
    expected = module().build()
    observed = tuple(load(path) for path in (CANDIDATE, EVALUATOR, FALSIFIER, RECEIPT))
    assert observed == expected
    candidate, evaluator, falsifier, receipt = observed
    assert candidate["application_base_sha"] == "47fcc8f71f5d4801b3c337d50c3b17bb6b8a648d"
    assert candidate["framework_pin"] == "d21592b0ff8da988deabb923fd549891ff8ad9f0"
    assert evaluator["candidate_artifact_hash"] == candidate["artifact_hash"]
    assert falsifier["evaluator_artifact_hash"] == evaluator["artifact_hash"]
    assert receipt["falsifier_artifact_hash"] == falsifier["artifact_hash"]


def test_exact_small_clean_phase_and_all_32_pairs_are_frozen() -> None:
    candidate = load(CANDIDATE)
    phase = candidate["exact_phase"]
    assert phase["parent"]["a"] == 4 and phase["parent"]["m"] == 3
    assert phase["current"]["a"] == 3 and phase["current"]["m"] == 4
    assert phase["parameter_pair_count"] == 32
    assert phase["parameter_pairs"] == [
        {"parent_v": parent_v, "current_v": current_v}
        for parent_v in range(8, 16)
        for current_v in range(4, 8)
    ]
    assert any("(6,2)->(3,4)" in item for item in candidate["forbidden_scope"])
    assert "global H_32 intersection P_33" in candidate["forbidden_scope"]


def test_full_word_obligations_hand_plan_and_three_branches_are_exact() -> None:
    candidate = load(CANDIDATE)
    obligations = candidate["full_word_compatibility_obligations"]
    assert len(obligations) == 9
    assert any("all 33 equalities" in item for item in obligations)
    assert any("prove Dec(x) UNSAT" in item for item in obligations)
    assert any("all 32 parameter pairs" in item for item in obligations)
    assert len(candidate["hand_proof_plan"]) == 7
    assert candidate["allowed_branches"] == [
        "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS",
        "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF",
        "CANNOT_CHECK",
    ]
    assert candidate["mathematical_lesson"].keys() == {
        "attempted_implication",
        "exact_theorem_or_failure",
        "supported_and_competing_mathematical_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_mathematical_move",
        "proof_and_source_evidence",
    }
    assert candidate["mathematical_learning_credit_policy"]["zero_credit"] == [
        "Git", "CI", "schemas", "hashes", "chronology", "repository activity"
    ]


def test_evaluator_and_falsifier_fail_closed_without_materialization() -> None:
    evaluator = load(EVALUATOR)
    falsifier = load(FALSIFIER)
    worlds = {world["world_id"]: world for world in falsifier["future_worlds"]}
    assert evaluator["implementation"] is None
    assert evaluator["evaluation_authorized"] is False
    assert evaluator["result_accessed"] is False
    assert len(worlds) == 9
    assert all(world["materialized"] is False for world in worlds.values())
    assert worlds["C053-CLEAN-PHASE-SYNTAX-SURVIVAL-ONLY-v1"]["expected_branches"] == ["CANNOT_CHECK"]
    assert worlds["C053-CLEAN-PHASE-SAT-PARENT-FALSE-POSITIVE-v1"]["expected_branches"] == ["CANNOT_CHECK"]
    assert worlds["C053-CLEAN-PHASE-INCOMPLETE-PAIR-COVERAGE-v1"]["expected_branches"] == ["CANNOT_CHECK"]
    assert worlds["C053-CLEAN-PHASE-FRONTEND-BRANCH-PROPAGATION-v1"]["expected_branches"] == load(CANDIDATE)["allowed_branches"]


def test_freeze_accesses_no_result_or_authority_and_extends_trace_tip() -> None:
    receipt = load(RECEIPT)
    firewall = receipt["chronology_firewall"]
    assert firewall["candidate_identity_frozen"] is True
    assert firewall["evaluator_identity_frozen"] is True
    assert firewall["falsifier_identity_frozen"] is True
    assert all(value is False for key, value in firewall.items() if not key.endswith("identity_frozen"))
    assert receipt["next_authorized_action"] == "PR_REVIEW_MERGE_ONLY"
    assert receipt["trace_delta"]["previous_event_hash"] == module().PREVIOUS_EVENT_HASH
    assert receipt["trace_delta"]["event_type"] == "CANDIDATE_PROPOSED"
    assert receipt["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    source = FIXTURE.read_text(encoding="utf-8")
    for forbidden in ("from C041_fx_sat_one_sided", "import C041_fx_sat_one_sided", "decode_formula", "is_satisfiable", "subprocess"):
        assert forbidden not in source
