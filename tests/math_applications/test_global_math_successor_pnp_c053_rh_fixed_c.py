from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_BSD_R15_SUCCESSOR_20260812.json"
NEW = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_PNP_C053_RH_FIXED_C_SUCCESSOR_20260812.json"
PNP_LESSON = ROOT / (
    "research/real_math/millennium/p_vs_np/07_memory/"
    "O9d12a2a1b_C053_K32_CLEAN_PHASE_MATHEMATICAL_LESSON_20260812.json"
)
PNP_RESULT = ROOT / (
    "research/real_math/millennium/p_vs_np/09_trace/"
    "O9d12a2a1b_C053_K32_CLEAN_PHASE_RESULT_RECEIPT_20260812.json"
)
RH_LESSON = ROOT / (
    "research/real_math/millennium/riemann_hypothesis/07_memory/"
    "RH_ANA_003k_JY_C001_POST_ACTIVATION_MATHEMATICAL_LESSON_20260812T175100Z.json"
)
RH_RESULT = ROOT / (
    "research/real_math/millennium/riemann_hypothesis/05_oracles/"
    "RH_ANA_003k_JY_C001_POST_ACTIVATION_RESULT_20260812T175100Z.json"
)
BASE = "daac28a17909a69a42fd816989710a03c651989b"
PNP_ITEM = "MATH-PNP-C053-K32-EXACT-CANONICAL-UNSAT-COMPATIBILITY"
RH_ITEM = "MATH-RH-ANA003K-JY-C001-FIXED-C-FLOOR-INCOMPATIBILITY"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()


def artifact_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(semantic(payload)).hexdigest()


def items(value: dict) -> dict[str, dict]:
    return {
        item["item_id"]: item
        for lane in value["lanes"]
        for item in lane["credited_items"]
    }


def lanes(value: dict) -> dict[str, dict]:
    return {lane["lane_id"]: lane for lane in value["lanes"]}


def test_exactly_two_new_deduplicated_units_preserve_all_prior_units() -> None:
    old, new = load(OLD), load(NEW)
    before, after = items(old), items(new)
    assert set(after) - set(before) == {PNP_ITEM, RH_ITEM}
    assert len(before) == 50 and len(after) == len(set(after)) == 52
    for item_id, value in before.items():
        assert semantic(after[item_id]) == semantic(value), item_id
    assert new["base_repository_sha"] == BASE
    assert new["authority_universe"]["repository_sha"] == BASE
    assert new["authority_universe"]["pending_or_open_pr_material_counted"] is False
    assert new["totals"]["mathematical_credit_units"] == 52
    assert new["totals"]["mathematical_credit_units_by_lane"]["p_vs_np"] == 18
    assert new["totals"]["mathematical_credit_units_by_lane"]["riemann_hypothesis"] == 9
    assert new["totals"]["mathematical_credit_units_by_type"]["PROOF_OR_LEMMA"] == 19
    assert (
        new["totals"]["mathematical_credit_units_by_type"]
        ["EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE"]
        == 18
    )


def test_c053_unit_is_the_exact_8_5_witness_with_hand_resolution() -> None:
    ledger, lesson, result = load(NEW), load(PNP_LESSON), load(PNP_RESULT)
    item = items(ledger)[PNP_ITEM]
    assert item["credit_type"] == "EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE"
    assert item["credit_units"] == 1 and item["mathematical_credit"] is True
    for fragment in (
        "(parent v,current v+)=(8,5)",
        "33-bit label",
        "canonical current prefix",
        "NOT x5",
        "x5",
        "empty clause",
    ):
        assert fragment in item["exact_claim"]
    assert item["seven_field_math_lesson"] == lesson["seven_field_mathematical_lesson"]
    assert item["source_bindings"] == {
        "lesson_artifact_hash": lesson["artifact_hash"],
        "result_artifact_hash": result["artifact_hash"],
        "result_branch": result["result_branch"],
    }
    assert all((ROOT / path).is_file() for path in item["evidence_pointers"])
    boundary = " ".join(item["non_implications"]).lower()
    assert "no cover" in boundary and "p versus np root" in boundary
    assert "same-context" in boundary and "independent" in boundary


def test_rh_unit_is_fixed_c_ratio_lemma_with_certificate_only_scope() -> None:
    ledger, lesson, result = load(NEW), load(RH_LESSON), load(RH_RESULT)
    item = items(ledger)[RH_ITEM]
    assert item["credit_type"] == "PROOF_OR_LEMMA"
    assert item["credit_units"] == 1 and item["mathematical_credit"] is True
    for fragment in (
        "For every fixed real C>0",
        "O_C(log^2(n)/n^(1/3))",
        "rho_C(n)->0",
        "current sufficient certificate",
    ):
        assert fragment in item["exact_claim"]
    assert item["seven_field_math_lesson"] == lesson["seven_field_math_lesson"]
    assert item["source_bindings"] == {
        "lesson_artifact_hash": lesson["artifact_hash"],
        "result_artifact_hash": result["artifact_hash"],
        "result_status": result["status"],
        "hand_proof_artifact_hash": result["hand_proof"]["artifact_hash"],
    }
    assert all((ROOT / path).is_file() for path in item["evidence_pointers"])
    boundary = " ".join(item["non_implications"]).lower()
    for phrase in ("actual natural-order remainder", "li", "riemann hypothesis"):
        assert phrase in boundary
    assert "same-context" in boundary and "independent" in boundary


def test_prior_root_states_and_nonindependence_boundary_are_preserved() -> None:
    old, new = load(OLD), load(NEW)
    assert {
        lane_id: lane["root_status"] for lane_id, lane in lanes(new).items()
    } == {
        lane_id: lane["root_status"] for lane_id, lane in lanes(old).items()
    }
    assert lanes(new)["p_vs_np"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert (
        lanes(new)["riemann_hypothesis"]["root_status"]
        == "OPEN_NO_SOLUTION_CERTIFICATE"
    )
    assert new["claim_boundary"]["any_application_root_newly_solved"] is False
    assert new["claim_boundary"]["independent_review_credit"] == 0
    assert new["bounded_disposition"]["pnp_c053"]["root_state"] == "OPEN"
    assert new["bounded_disposition"]["rh_ana003k_fixed_c"]["root_state"] == "OPEN"


def test_operational_assurance_receives_zero_mathematical_credit() -> None:
    ledger = load(NEW)
    for item_id in (PNP_ITEM, RH_ITEM):
        boundary = " ".join(items(ledger)[item_id]["non_implications"]).lower()
        for term in ("git", "ci", "schemas", "hashes", "chronology"):
            assert term in boundary
    assert ledger["bounded_disposition"]["zero_credit"] == {
        "git_ci_schema_hash_chronology_credit_units": 0,
        "same_context_review_independent_credit_units": 0,
    }
    assert semantic(ledger["excluded_provenance"]) == semantic(load(OLD)["excluded_provenance"])


def test_successor_lineage_and_content_hash_are_exact() -> None:
    old, new = load(OLD), load(NEW)
    lineage = new["successor_lineage"]
    assert lineage["predecessor_artifact_hash"] == old["artifact_hash"]
    assert lineage["predecessor_raw_sha256"] == hashlib.sha256(OLD.read_bytes()).hexdigest()
    assert lineage["predecessor_path"] == OLD.relative_to(ROOT).as_posix()
    assert new["artifact_hash"] == artifact_hash(new)
