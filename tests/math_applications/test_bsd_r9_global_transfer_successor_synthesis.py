from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"
OLD_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_NS_B2A1B2_SUCCESSOR_20260812.json"
NEW_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_BSD_R9_SUCCESSOR_20260812.json"
PRESERVED_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_NS_B2A1B2_SUCCESSOR_20260812.json"
MERGED_R10_BASE_SHA = "51ab50bf7e37b49711ac2eb59013ba0bf34427d0"
ITEM_ID = "MATH-BSD-R9-ZHANG-TECHNICAL-PRIME-SELMER-CORANK-LOWER-BOUND"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def _items(ledger: dict) -> dict[str, dict]:
    return {item["item_id"]: item for lane in ledger["lanes"] for item in lane["credited_items"]}


def test_bsd_r9_successor_preserves_exact_ns_predecessor() -> None:
    old, new = _load(OLD_LEDGER), _load(NEW_LEDGER)
    assert new["successor_lineage"]["predecessor_git_blob"] == _git_blob_sha(OLD_LEDGER.read_bytes())
    assert new["successor_lineage"]["predecessor_raw_sha256"] == hashlib.sha256(OLD_LEDGER.read_bytes()).hexdigest()
    assert new["successor_lineage"]["predecessor_artifact_hash"] == old["artifact_hash"]
    assert new["authority_universe"]["repository_sha"] == MERGED_R10_BASE_SHA
    assert new["base_repository_sha"] == MERGED_R10_BASE_SHA
    assert new["artifact_hash"] == _canonical_hash(new)


def test_exactly_one_deduplicated_zhang_transfer_condition_is_added() -> None:
    old, new = _load(OLD_LEDGER), _load(NEW_LEDGER)
    old_items, new_items = _items(old), _items(new)
    assert set(new_items) - set(old_items) == {ITEM_ID}
    assert set(old_items) <= set(new_items)
    assert all(new_items[key] == value for key, value in old_items.items())
    item = new_items[ITEM_ID]
    assert item["credit_type"] == "TRANSFER_CONDITION"
    assert item["credit_units"] == 1
    assert "p>=5" in item["exact_claim"]
    assert "Theorem 1.4 hypotheses (1)-(4)" in item["exact_claim"]
    assert "ord_{s=1} L(E,s)=2" in item["exact_claim"]
    assert "root number +1" in item["exact_claim"]
    assert "corank_Zp Sel_{p^infinity}(E/Q) >= 2" in item["exact_claim"]
    assert new["totals"]["mathematical_credit_units"] == old["totals"]["mathematical_credit_units"] + 1 == 41
    assert new["totals"]["mathematical_credit_units_by_lane"]["birch_swinnerton_dyer"] == 2
    assert new["totals"]["mathematical_credit_units_by_type"]["TRANSFER_CONDITION"] == 6
    assert all((ROOT / path).is_file() for path in item["evidence_pointers"])


def test_strict_nonclaims_and_r10_zero_credit_are_explicit() -> None:
    new = _load(NEW_LEDGER)
    item = _items(new)[ITEM_ID]
    boundary = " ".join(item["non_implications"]).lower()
    for term in (
        "exact selmer corank two",
        "transverse p-local localization",
        "p-infinity/v_p",
        "rank-two bsd leading-term",
        "every prime",
        "mordell-weil rank two",
        "sha finiteness",
    ):
        assert term in boundary
    disposition = new["bounded_disposition"]
    assert disposition["r9"]["credited_item_id"] == ITEM_ID
    assert disposition["r9"]["credit_units"] == 1
    assert disposition["r10"]["credit_units"] == 0
    assert "source/proof-interface audit" in disposition["r10"]["reason"]
    assert disposition["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert new["claim_boundary"]["independent_review_credit"] == 0


def test_failure_atlas_is_preserved_without_a_new_cause() -> None:
    new, atlas = _load(NEW_LEDGER), _load(PRESERVED_ATLAS)
    atlas_disposition = new["bounded_disposition"]["failure_atlas"]
    assert atlas_disposition["action"] == "UNCHANGED_NO_NEW_CAUSE"
    assert atlas_disposition["preserved_path"] == str(PRESERVED_ATLAS.relative_to(ROOT))
    assert atlas_disposition["preserved_bsd_cause_id"] == "FM-BSD-ARITHMETIC-PREMISE-REIMPORT"
    causes = {item["id"]: item for item in atlas["failure_mechanisms"]}
    cause = causes[atlas_disposition["preserved_bsd_cause_id"]]
    assert "representation change relocates rather than closes" in cause["root_cause"]
    assert not (MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_BSD_R9_SUCCESSOR_20260812.json").exists()
    assert (BSD / "00_sources/BSD_A1a1_R9_ZHANG_LOWER_BOUND_SOURCE_AUDIT_20260812.json").is_file()
