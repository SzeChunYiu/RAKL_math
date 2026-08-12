from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_HODGE_C004_SUCCESSOR_20260812.json"
NEW_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_NS_B2A1B2_SUCCESSOR_20260812.json"
OLD_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_HODGE_C004_SUCCESSOR_20260812.json"
NEW_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_NS_B2A1B2_SUCCESSOR_20260812.json"
MERGED_NS_SHA = "4a1341447e5ef83125adfab7f915855b96245f0a"
ITEM_ID = "MATH-NS-B2A1B2-HILL-FINITE-ENERGY-DENSITY-FALSIFIER"
CAUSE_ID = "FM-NS-FINITE-ENERGY-KERNEL-NONIDENTIFYING-DENSITY"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _items(ledger: dict) -> dict[str, dict]:
    return {item["item_id"]: item for lane in ledger["lanes"] for item in lane["credited_items"]}


def test_ns_successor_preserves_exact_hodge_predecessors() -> None:
    old_ledger, new_ledger = _load(OLD_LEDGER), _load(NEW_LEDGER)
    old_atlas, new_atlas = _load(OLD_ATLAS), _load(NEW_ATLAS)
    assert new_ledger["successor_lineage"]["predecessor_raw_sha256"] == hashlib.sha256(OLD_LEDGER.read_bytes()).hexdigest()
    assert new_ledger["successor_lineage"]["predecessor_artifact_hash"] == old_ledger["artifact_hash"]
    assert new_atlas["successor_lineage"]["predecessor_raw_sha256"] == hashlib.sha256(OLD_ATLAS.read_bytes()).hexdigest()
    assert new_atlas["successor_lineage"]["predecessor_artifact_hash"] == old_atlas["artifact_hash"]
    assert new_ledger["authority_universe"]["repository_sha"] == MERGED_NS_SHA
    assert new_atlas["authority_universe"]["repository_sha"] == MERGED_NS_SHA
    assert new_ledger["artifact_hash"] == _canonical_hash(new_ledger)
    assert new_atlas["artifact_hash"] == _canonical_hash(new_atlas)


def test_exactly_one_deduplicated_hill_mathematical_falsifier_is_added() -> None:
    old, new = _load(OLD_LEDGER), _load(NEW_LEDGER)
    old_items, new_items = _items(old), _items(new)
    assert set(new_items) - set(old_items) == {ITEM_ID}
    assert set(old_items) <= set(new_items)
    assert all(new_items[key] == value for key, value in old_items.items())
    item = new_items[ITEM_ID]
    assert item["credit_type"] == "MATHEMATICAL_FALSIFIER"
    assert item["credit_units"] == 1
    assert "0 <= R^-1 int chi_R|U(t)|^2 <= R^-1||V||_2^2 -> 0" in item["exact_claim"]
    assert "Lambda_chi(t)=0" in item["exact_claim"]
    assert new["totals"]["mathematical_credit_units"] == old["totals"]["mathematical_credit_units"] + 1 == 40
    assert new["totals"]["mathematical_credit_units_by_lane"]["navier_stokes"] == 10
    assert new["totals"]["mathematical_credit_units_by_type"]["MATHEMATICAL_FALSIFIER"] == 1
    assert all((ROOT / path).is_file() for path in item["evidence_pointers"])


def test_zero_software_or_unproved_root_credit() -> None:
    item = _items(_load(NEW_LEDGER))[ITEM_ID]
    boundary = " ".join(item["non_implications"]).lower()
    for term in ("software", "ci", "schemas", "hashes", "chronology", "git", "pr state", "repository growth"):
        assert term in boundary
    for term in ("seregin theorem 3.1", "navier-stokes blow-up extraction", "root result", "independent-review"):
        assert term in boundary
    ledger = _load(NEW_LEDGER)
    assert ledger["claim_boundary"]["framework_promotion_implied"] is False
    assert ledger["claim_boundary"]["independent_review_credit"] == 0


def test_atlas_adds_only_distinct_finite_energy_kernel_cause() -> None:
    old, new = _load(OLD_ATLAS), _load(NEW_ATLAS)
    old_by_id = {item["id"]: item for item in old["failure_mechanisms"]}
    new_by_id = {item["id"]: item for item in new["failure_mechanisms"]}
    assert set(new_by_id) - set(old_by_id) == {CAUSE_ID}
    assert all(new_by_id[key] == value for key, value in old_by_id.items())
    assert new_by_id["FM-HODGE-REPRESENTATION-EQUIVALENCE-NOT-REDUCTION"] == old_by_id["FM-HODGE-REPRESENTATION-EQUIVALENCE-NOT-REDUCTION"]
    assert new_by_id["FM-HODGE-SOURCE-ENLARGEMENT-NOT-PROJECTION-GAIN"] == old_by_id["FM-HODGE-SOURCE-ENLARGEMENT-NOT-PROJECTION-GAIN"]
    item = new_by_id[CAUSE_ID]
    assert item["failed_inference"] == "nonzero/unit-scale F(a)=1 Euler-side state implies Lambda_chi(t)>0"
    assert "0 <= R^-1 int chi_R(x)|U(x,t)|^2 dx <= R^-1||V||_2^2 -> 0" in item["exact_hill_inequality"]
    assert len(item["supported_causes"]) == 2
    assert len(item["competing_causes"]) == 4
    assert "source-valid theorem" in item["falsifier"]
    assert "observable zero set" in item["repair"]
    assert item["related_failure"]["id"] == "FM-NS-LOCAL-TO-MOVING-SCALE-ESCAPE"
    assert "exact kernel" in item["proposal_only_rakl_lesson"]
    assert "framework promotion" in item["proposal_only_rakl_lesson"]
    assert all((ROOT / path).is_file() for path in item["evidence"])
