from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_PNP_C050_K15_SUCCESSOR_20260812.json"
NEW = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_RH_C002_SUCCESSOR_20260812.json"
LESSON = ROOT / "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_003_ABEL_001_C002_SCOPED_MATHEMATICAL_LESSON_20260812.json"
BASE = "6fd16ea7363607021c1b0815dd3f27db7e4b3e5f"
ITEM = "MATH-RH-ABEL-C002-FIXED-N-NATURAL-ORDER-NONABSOLUTE"
RAW = "6b3279e91de8e5a6c8b964154abba2e7ff403eb595fdad4de8cbb6b19208baaa"
BLOB = "66a679c442217f27aa4ca2a495710064623aac1a"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_hash(value: dict) -> str:
    value = copy.deepcopy(value)
    value["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(semantic(value)).hexdigest()


def items(value: dict) -> dict[str, dict]:
    return {item["item_id"]: item for lane in value["lanes"] for item in lane["credited_items"]}


def test_successor_binds_exact_main_and_preserves_predecessor() -> None:
    old, new = load(OLD), load(NEW)
    assert new["ledger_id"] == "GLOBAL-MATH-ONLY-SATURATION-LEDGER-RH-C002-SUCCESSOR-20260812"
    assert new["ledger_id"] != old["ledger_id"]
    assert new["as_of_utc"] == "2026-08-12T08:20:00Z"
    assert new["as_of_utc"] > "2026-08-12T08:18:00Z"
    assert new["base_repository_sha"] == BASE
    assert new["authority_universe"]["repository_sha"] == BASE
    assert new["authority_universe"]["pending_or_open_pr_material_counted"] is False
    lineage = new["successor_lineage"]
    assert lineage["predecessor_artifact_hash"] == old["artifact_hash"]
    assert lineage["predecessor_raw_sha256"] == RAW == hashlib.sha256(OLD.read_bytes()).hexdigest()
    assert lineage["predecessor_git_blob"] == BLOB
    assert new["artifact_hash"] == artifact_hash(new)


def test_exactly_one_deduplicated_rh_unit_and_all_48_predecessors_preserved() -> None:
    old, new = load(OLD), load(NEW)
    before, after = items(old), items(new)
    assert set(after) - set(before) == {ITEM}
    assert len(before) == 48 and len(after) == len(set(after)) == 49
    for item_id, value in before.items():
        assert semantic(after[item_id]) == semantic(value), item_id
    assert new["totals"]["mathematical_credit_units"] == 49
    assert new["totals"]["mathematical_credit_units_by_lane"]["riemann_hypothesis"] == 8
    assert new["totals"]["mathematical_credit_units_by_type"]["PROOF_OR_LEMMA"] == 17


def test_rh_c002_unit_preserves_exact_seven_field_lesson_and_scope() -> None:
    ledger, lesson = load(NEW), load(LESSON)
    item = items(ledger)[ITEM]
    assert item["credit_type"] == "PROOF_OR_LEMMA"
    assert item["credit_units"] == 1 and item["mathematical_credit"] is True
    assert item["seven_field_math_lesson"] == lesson["seven_field_math_lesson"]
    for text in ("fixed integer n>=1", "natural-order identity", "m=6k", "including n=1"):
        assert text in item["exact_claim"]
    assert all((ROOT / path).is_file() for path in item["evidence_pointers"])


def test_operational_process_and_label_repair_get_zero_math_credit() -> None:
    ledger = load(NEW)
    item = items(ledger)[ITEM]
    boundary = " ".join(item["non_implications"]).lower()
    for term in ("git", "merges", "ci", "tests", "schemas", "hashes", "serialization", "runtime", "chronology", "telemetry"):
        assert term in boundary
    disposition = ledger["bounded_disposition"]["rh_c002"]
    assert disposition["credit_units"] == 1
    assert disposition["invalid_result_label_credit_units"] == 0
    assert disposition["postmerge_governance_repair_credit_units"] == 0
    assert disposition["effective_frozen_result_branch"] == "PROVED_FIXED_N_NATURAL_ORDER_IDENTITY"
    assert disposition["seven_field_math_lesson_preserved_exactly"] is True
    assert disposition["global_failure_cause_added"] is False


def test_root_remains_open_and_failure_atlas_is_unchanged() -> None:
    ledger = load(NEW)
    lane = next(lane for lane in ledger["lanes"] if lane["lane_id"] == "riemann_hypothesis")
    assert lane["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert ledger["claim_boundary"] == load(OLD)["claim_boundary"]
    assert ledger["bounded_disposition"]["failure_atlas"]["action"] == "NO_NEW_DISTINCT_CAUSE"
    assert ledger["bounded_disposition"]["failure_atlas"]["added_cause_ids"] == []
