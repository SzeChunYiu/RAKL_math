from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_YM_R20_HODGE_C007_BSD_R12_SUCCESSOR_20260812.json"
NEW_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_NS_R6_SUCCESSOR_20260812.json"
LATEST_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_YM_R20_HODGE_C007_SUCCESSOR_20260812.json"
BASE = "d65014c9a4dfa251ed9453addb3ac87815ab949a"
FRAMEWORK = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
NEW_ITEM = "MATH-NS-B1A3B1A2A-R6-ANCIENT-SMOOTHING-TO-FIXED-TIME-CAPACITY"
PREDECESSOR_RAW_SHA256 = "fc5b37b6ff6709b8ee4757525d127c92bd80649b2f30709c908ba2ced40213bf"
PREDECESSOR_GIT_BLOB = "ebcf1d6e7c744770fa36cd6347fb444eaee79e6e"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def canonical_hash(document: dict) -> str:
    payload = copy.deepcopy(document)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def semantic_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def items(document: dict) -> dict[str, dict]:
    return {
        item["item_id"]: item
        for lane in document["lanes"]
        for item in lane["credited_items"]
    }


def test_ns_r6_successor_binds_exact_merged_main_and_predecessor() -> None:
    old, new = load(OLD_LEDGER), load(NEW_LEDGER)
    assert new["base_repository_sha"] == BASE
    assert new["authority_universe"] == {
        "kind": "MERGED_ORIGIN_MAIN_ONLY",
        "pending_or_open_pr_material_counted": False,
        "repository_sha": BASE,
        "rule": (
            "Only content reachable from exact frozen origin/main "
            f"{BASE} is eligible. Git/merge/CI status supplies assurance only "
            "and zero mathematical credit."
        ),
    }
    lineage = new["successor_lineage"]
    assert lineage["predecessor_artifact_hash"] == old["artifact_hash"]
    assert lineage["predecessor_raw_sha256"] == PREDECESSOR_RAW_SHA256
    assert hashlib.sha256(OLD_LEDGER.read_bytes()).hexdigest() == PREDECESSOR_RAW_SHA256
    assert lineage["predecessor_git_blob"] == PREDECESSOR_GIT_BLOB
    assert lineage["predecessor_path"] == OLD_LEDGER.relative_to(ROOT).as_posix()
    assert new["artifact_hash"] == canonical_hash(new)


def test_exactly_one_unit_is_added_and_every_predecessor_unit_is_byte_semantic() -> None:
    old, new = load(OLD_LEDGER), load(NEW_LEDGER)
    old_items, new_items = items(old), items(new)
    assert set(new_items) - set(old_items) == {NEW_ITEM}
    assert set(old_items) <= set(new_items)
    for item_id, old_item in old_items.items():
        assert semantic_bytes(new_items[item_id]) == semantic_bytes(old_item), item_id
    assert len(new_items) == len(set(new_items)) == 47
    assert new["totals"]["mathematical_credit_units"] == 47
    assert new["totals"]["mathematical_credit_units_by_lane"] == {
        "p_vs_np": 16,
        "riemann_hypothesis": 7,
        "navier_stokes": 11,
        "yang_mills": 5,
        "hodge_conjecture": 5,
        "birch_swinnerton_dyer": 3,
        "poincare_conjecture": 0,
    }
    assert new["totals"]["mathematical_credit_units_by_type"] == {
        "BROKEN_MATHEMATICAL_ASSUMPTION": 7,
        "EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE": 17,
        "MATHEMATICAL_FALSIFIER": 1,
        "PROOF_OR_LEMMA": 15,
        "TRANSFER_CONDITION": 7,
    }


def test_ns_r6_item_is_one_scoped_proof_with_packet_witness_zero_credit() -> None:
    ledger = load(NEW_LEDGER)
    item = items(ledger)[NEW_ITEM]
    assert item["authority"] == "SOURCE_BOUND_SCOPED_PROOF"
    assert item["credit_type"] == "PROOF_OR_LEMMA"
    assert item["credit_units"] == 1
    assert item["mathematical_credit"] is True
    assert item["attached_representation_witness_credit_units"] == 0
    for text in (
        "||nabla^k partial_t^l u||_infinity <= C_{k,l} M^(k+2l+1)",
        "8 I R/(lambda^2 delta)",
        "16 I K R lambda^(-3)",
        "K=0",
    ):
        assert text in item["exact_claim"]
    assert item["scope"]
    assert all((ROOT / pointer).is_file() for pointer in item["evidence_pointers"])
    boundary = " ".join(item["non_implications"]).lower()
    assert "unbounded radius" in boundary
    assert "representation-only packet witness" in boundary
    assert "zero separate mathematical credit" in boundary
    for term in ("git", "ci", "tests", "schemas", "hashes", "chronology", "telemetry"):
        assert term in boundary


def test_ns_r6_adds_no_global_failure_cause_or_pending_material() -> None:
    ledger = load(NEW_LEDGER)
    disposition = ledger["bounded_disposition"]["ns_r6"]
    assert disposition == {
        "attached_packet_witness_credit_units": 0,
        "classification": "SOURCE_BOUND_SCOPED_PROOF",
        "credit_units": 1,
        "credited_item_id": NEW_ITEM,
        "global_failure_cause_added": False,
        "overlap_disposition": (
            "PR310 ambient packet witness and the pending R7 summation-tail "
            "refinement receive zero R6 credit and are not imported."
        ),
    }
    atlas = ledger["bounded_disposition"]["failure_atlas"]
    assert atlas["action"] == "NO_NEW_DISTINCT_CAUSE"
    assert atlas["added_cause_ids"] == []
    assert atlas["existing_related_cause_id"] == "FM-NS-LOCAL-TO-MOVING-SCALE-ESCAPE"
    assert atlas["unchanged_atlas_path"] == LATEST_ATLAS.relative_to(ROOT).as_posix()
    assert LATEST_ATLAS.is_file()
    assert not (MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_NS_R6_SUCCESSOR_20260812.json").exists()
    assert ledger["authority_universe"]["pending_or_open_pr_material_counted"] is False
    assert ledger["bounded_disposition"]["pnp_c050_k15_evaluated_result"] == {
        "credit_units": 0,
        "evidence_pointer": (
            "research/real_math/millennium/p_vs_np/05_falsification/"
            "O9d12a2a1b_C050_K15_PROOF_CHECK_RESULT_20260812.json"
        ),
        "state": "MERGED_RESULT_PENDING_SEPARATE_SYNTHESIS",
        "reason": (
            "One scoped evaluated C050 k15 mathematical result is reachable "
            "from the frozen main base, but this R6-only successor does not "
            "adjudicate or count it."
        ),
    }


def test_predecessor_nonunit_planes_are_preserved_and_root_stays_open() -> None:
    old, new = load(OLD_LEDGER), load(NEW_LEDGER)
    for field in (
        "claim_boundary",
        "counting_rule",
        "global_artifact_audit",
        "object",
        "quantity_of_interest",
    ):
        assert semantic_bytes(new[field]) == semantic_bytes(old[field]), field
    old_lanes = {lane["lane_id"]: lane for lane in old["lanes"]}
    new_lanes = {lane["lane_id"]: lane for lane in new["lanes"]}
    assert set(old_lanes) == set(new_lanes)
    for lane_id in old_lanes:
        for field in ("display_name", "lane_id", "root_status", "status"):
            assert new_lanes[lane_id][field] == old_lanes[lane_id][field]
    assert new_lanes["navier_stokes"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert new["claim_boundary"]["independent_review_credit"] == 0
    excluded_id = "EXCLUDED-PNP-C050-K15-FREEZE-WITHOUT-TARGET-RESULT"
    old_excluded = {item["item_id"]: item for item in old["excluded_provenance"]}
    new_excluded = {item["item_id"]: item for item in new["excluded_provenance"]}
    assert set(old_excluded) == set(new_excluded)
    for item_id in set(old_excluded) - {excluded_id}:
        assert semantic_bytes(new_excluded[item_id]) == semantic_bytes(old_excluded[item_id])
    corrected = new_excluded[excluded_id]
    assert corrected["credit_units"] == 0
    assert corrected["mathematical_credit"] is False
    assert corrected["reason"] == (
        "The target-blind C050 k15 candidate/evaluator freeze artifacts "
        "preserve chronology and assurance and contain no evaluated target "
        "mathematical result themselves. A later merged evaluated result is "
        "separately marked pending synthesis; the freeze still earns zero "
        "mathematical credit."
    )
    assert new["bounded_disposition"]["pnp_c050_k15_freeze"]["reason"] == (
        "The merged freeze artifacts are target-blind discriminator/candidate "
        "objects and contain no evaluated target mathematical result "
        "themselves; candidate chronology and assurance do not mint mathematics."
    )
