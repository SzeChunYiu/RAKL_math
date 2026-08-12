from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_POINCARE_C001_SUCCESSOR_20260812.json"
ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_POINCARE_C001_SUCCESSOR_20260812.json"
SYNTHESIS = ROOT / "research/real_math/millennium/cross_problem/poincare_transfer/10_case_study/POINCARE_SUCCESS_TRANSFER_SYNTHESIS_20260812.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(document: dict) -> str:
    payload = copy.deepcopy(document)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def test_c001_gets_exactly_one_candidate_specific_math_credit() -> None:
    ledger = load(LEDGER)
    assert ledger["artifact_hash"] == canonical_hash(ledger)
    lanes = {row["lane_id"]: row for row in ledger["lanes"]}
    credits = [row for row in lanes["navier_stokes"]["credited_items"] if row["item_id"].startswith("MATH-XM-PC-NS-C001-")]
    assert len(credits) == 1
    credit = credits[0]
    assert credit["credit_type"] == "PROOF_OR_LEMMA"
    assert credit["credit_units"] == 1
    assert "twelve ordered resonant contributions" in credit["exact_claim"]
    assert "candidate-specific" in " ".join(credit["non_implications"]).lower()
    assert ledger["totals"]["mathematical_credit_units"] == 38
    assert ledger["totals"]["mathematical_credit_units_by_lane"]["navier_stokes"] == 9


def test_poincare_is_solved_externally_without_new_application_solution_credit() -> None:
    ledger = load(LEDGER)
    lane = next(row for row in ledger["lanes"] if row["lane_id"] == "poincare_conjecture")
    assert lane["status"] == "SOLVED_EXTERNALLY_SOURCE_SUCCESS_CASE"
    assert lane["root_status"] == "SOLVED_EXTERNALLY_NO_ACTIVE_APPLICATION_CLAIM"
    assert lane["credited_items"] == []
    assert ledger["claim_boundary"]["any_application_root_newly_solved"] is False


def test_atlas_records_bounded_candidate_failure_not_universal_no_transfer() -> None:
    atlas = load(ATLAS)
    assert atlas["artifact_hash"] == canonical_hash(atlas)
    assert len(atlas["success_transfer_failures"]) == 1
    failure = atlas["success_transfer_failures"][0]
    assert failure["cause_status"] == "VERIFIED_SCOPED"
    assert "universal enstrophy monotonicity remains unresolved" in failure["failure_scope"]
    assert "No Perelman" in failure["non_transfer"]
    assert atlas["self_rakl_feedback"]["poincare_success_transfer_fresh_assurance"].startswith("Required")


def test_synthesis_preserves_composite_chain_and_proposal_only_improvement() -> None:
    synthesis = load(SYNTHESIS)
    assert synthesis["artifact_hash"] == canonical_hash(synthesis)
    assert synthesis["source_boundary"]["status"] == "SOLVED_EXTERNALLY"
    assert len(synthesis["source_success_chain"]) == 5
    assert all(row["enabling_assumptions"] for row in synthesis["source_success_chain"])
    verdict = synthesis["transfer_verdict"]
    assert verdict["target_candidate_counterexample"] == "FALSIFIED_BY_EXACT_CANCELLATION"
    assert verdict["universal_enstrophy_monotonicity"] == "UNRESOLVED"
    assert verdict["perelman_machinery_transfer"] == "NOT_ESTABLISHED"
    improvement = synthesis["proposal_only_rakl_improvement"]
    assert improvement["current_authority"] == "APPLICATION_FEEDBACK_PROPOSAL_ONLY_NOT_PROMOTED"
    assert improvement["fresh_assurance_required"] is True
    assert improvement["non_guarantees"]
