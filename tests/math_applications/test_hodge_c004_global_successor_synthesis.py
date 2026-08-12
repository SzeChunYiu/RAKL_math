from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_POINCARE_C001_SUCCESSOR_20260812.json"
NEW_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_HODGE_C004_SUCCESSOR_20260812.json"
OLD_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_POINCARE_C001_SUCCESSOR_20260812.json"
NEW_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_HODGE_C004_SUCCESSOR_20260812.json"
MERGED_HODGE_SHA = "e51a8c3722546b6ead3f0dcc48bb2262aadb68c0"


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


def test_hodge_successor_preserves_exact_merged_predecessors() -> None:
    old_ledger, new_ledger = _load(OLD_LEDGER), _load(NEW_LEDGER)
    old_atlas, new_atlas = _load(OLD_ATLAS), _load(NEW_ATLAS)
    assert new_ledger["successor_lineage"]["predecessor_raw_sha256"] == hashlib.sha256(OLD_LEDGER.read_bytes()).hexdigest()
    assert new_ledger["successor_lineage"]["predecessor_artifact_hash"] == old_ledger["artifact_hash"]
    assert new_atlas["successor_lineage"]["predecessor_raw_sha256"] == hashlib.sha256(OLD_ATLAS.read_bytes()).hexdigest()
    assert new_atlas["successor_lineage"]["predecessor_artifact_hash"] == old_atlas["artifact_hash"]
    assert new_ledger["authority_universe"]["repository_sha"] == MERGED_HODGE_SHA
    assert new_atlas["authority_universe"]["repository_sha"] == MERGED_HODGE_SHA
    assert new_ledger["artifact_hash"] == _canonical_hash(new_ledger)
    assert new_atlas["artifact_hash"] == _canonical_hash(new_atlas)


def test_exactly_one_scoped_counterexample_transfer_unit_is_added() -> None:
    old, new = _load(OLD_LEDGER), _load(NEW_LEDGER)
    old_items, new_items = _items(old), _items(new)
    assert set(new_items) - set(old_items) == {"MATH-HODGE-C004-PROJECTION-KERNEL-NONIMPLICATION"}
    assert set(old_items) <= set(new_items)
    item = new_items["MATH-HODGE-C004-PROJECTION-KERNEL-NONIMPLICATION"]
    assert item["credit_type"] == "EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE"
    assert item["credit_units"] == 1
    assert "p(A)=p(B)=<v1>" in item["exact_claim"]
    assert "B/A -> H/p(A)" in item["exact_claim"]
    assert new["totals"]["mathematical_credit_units"] == old["totals"]["mathematical_credit_units"] + 1 == 39
    assert new["totals"]["mathematical_credit_units_by_lane"]["hodge_conjecture"] == 3
    assert new["totals"]["mathematical_credit_units_by_type"]["EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE"] == 15
    assert all((ROOT / path).is_file() for path in item["evidence_pointers"])


def test_assurance_and_unproved_hodge_claims_receive_zero_credit() -> None:
    item = _items(_load(NEW_LEDGER))["MATH-HODGE-C004-PROJECTION-KERNEL-NONIMPLICATION"]
    boundary = " ".join(item["non_implications"]).lower()
    for term in ("software tests", "ci", "schemas", "hashes", "chronology", "repository growth"):
        assert term in boundary
    for term in ("actual total-witness incidence", "higher-order", "root result"):
        assert term in boundary
    ledger = _load(NEW_LEDGER)
    assert ledger["claim_boundary"]["framework_promotion_implied"] is False
    assert ledger["claim_boundary"]["independent_review_credit"] == 0


def test_atlas_adds_distinct_projection_failure_and_preserves_representation_warning() -> None:
    old, new = _load(OLD_ATLAS), _load(NEW_ATLAS)
    old_by_id = {item["id"]: item for item in old["failure_mechanisms"]}
    new_by_id = {item["id"]: item for item in new["failure_mechanisms"]}
    assert set(new_by_id) - set(old_by_id) == {"FM-HODGE-SOURCE-ENLARGEMENT-NOT-PROJECTION-GAIN"}
    assert all(new_by_id[key] == value for key, value in old_by_id.items())
    assert new_by_id["FM-HODGE-REPRESENTATION-EQUIVALENCE-NOT-REDUCTION"] == old_by_id["FM-HODGE-REPRESENTATION-EQUIVALENCE-NOT-REDUCTION"]
    item = new_by_id["FM-HODGE-SOURCE-ENLARGEMENT-NOT-PROJECTION-GAIN"]
    assert "B/A -> H/p(A)" in item["falsifier"]
    assert "p(B)=H" in item["falsifier"]
    assert "signed rational" in item["repair"]
    assert item["related_failure"]["id"] == "FM-HODGE-REPRESENTATION-EQUIVALENCE-NOT-REDUCTION"
    assert "mathematical consumer map" in item["proposal_only_rakl_lesson"]
    assert "framework promotion" in item["proposal_only_rakl_lesson"]
    assert all((ROOT / path).is_file() for path in item["evidence"])
