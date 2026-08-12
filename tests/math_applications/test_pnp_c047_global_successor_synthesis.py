from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_20260812.json"
NEW_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_C047_SUCCESSOR_20260812.json"
OLD_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_20260812.json"
NEW_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_C047_SUCCESSOR_20260812.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _hash(document: dict) -> str:
    value = copy.deepcopy(document)
    value["artifact_hash"] = ""
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_c047_successor_ledger_preserves_exact_frozen_predecessor() -> None:
    old = _load(OLD_LEDGER)
    new = _load(NEW_LEDGER)
    lineage = new["successor_lineage"]
    assert hashlib.sha256(OLD_LEDGER.read_bytes()).hexdigest() == "4e3982d171e32d1eb975ca660d2ae3eea8c295db8225e0ed78398c9189ffb8b6"
    assert old["artifact_hash"] == "sha256:8772a805a521bcf5965a0ca3c51a0393e482e58b716b15840ee6217f5f7c4746"
    assert lineage == {
        "predecessor_path": "research/real_math/millennium/cross_problem/07_memory/GLOBAL_MATH_ONLY_SATURATION_LEDGER_20260812.json",
        "predecessor_repository_sha": "944730da118004124bbadd0e45dd06ab02a75b6f",
        "predecessor_git_blob": "d71b2b41acce58dc429d07fb6ee37e9f44fdfe29",
        "predecessor_raw_sha256": "4e3982d171e32d1eb975ca660d2ae3eea8c295db8225e0ed78398c9189ffb8b6",
        "predecessor_artifact_hash": old["artifact_hash"],
        "preservation": "PREDECESSOR_REMAINS_UNCHANGED; THIS DOCUMENT ADDS ONE DEDUPLICATED C047 MATHEMATICAL UNIT",
    }
    assert new["artifact_hash"] == _hash(new)
    assert new["authority_universe"]["repository_sha"] == "70a4c30e88e01f3923ab3efc4311a77c50b05bba"


def test_c047_successor_adds_exactly_one_math_credit() -> None:
    old = _load(OLD_LEDGER)
    new = _load(NEW_LEDGER)
    old_items = {item["item_id"] for lane in old["lanes"] for item in lane["credited_items"]}
    new_items = {item["item_id"] for lane in new["lanes"] for item in lane["credited_items"]}
    assert new_items - old_items == {"MATH-PNP-C047-ORIENTATION-ONLY-HEADER-SEPARATION"}
    assert old_items <= new_items
    assert new["totals"]["mathematical_credit_units"] == old["totals"]["mathematical_credit_units"] + 1 == 37
    assert new["totals"]["mathematical_credit_units_by_lane"]["p_vs_np"] == 15
    assert new["totals"]["mathematical_credit_units_by_type"]["PROOF_OR_LEMMA"] == 12
    item = next(item for lane in new["lanes"] for item in lane["credited_items"] if item["item_id"] in new_items - old_items)
    assert item["credit_type"] == "PROOF_OR_LEMMA"
    assert item["credit_units"] == 1
    assert "1111" in item["exact_claim"] and "1110" in item["exact_claim"]
    assert "literal matrix transpose" in " ".join(item["non_implications"]).lower()
    assert "prefix r placed on the fresh row" in item["scope"]
    assert all((ROOT / pointer).is_file() for pointer in item["evidence_pointers"])


def test_c047_successor_does_not_mint_assurance_or_framework_credit() -> None:
    new = _load(NEW_LEDGER)
    item = next(item for lane in new["lanes"] for item in lane["credited_items"] if item["item_id"] == "MATH-PNP-C047-ORIENTATION-ONLY-HEADER-SEPARATION")
    boundary = " ".join(item["non_implications"]).lower()
    for term in ("git", "ci", "schemas", "hashes", "chronology"):
        assert term in boundary
    assert new["claim_boundary"]["any_root_solved"] is False
    assert new["claim_boundary"]["framework_promotion_implied"] is False


def test_c047_atlas_successor_preserves_predecessor_and_changes_only_pnp_mechanism() -> None:
    old = _load(OLD_ATLAS)
    new = _load(NEW_ATLAS)
    assert hashlib.sha256(OLD_ATLAS.read_bytes()).hexdigest() == "fd21577eda03859848f2173d911ed1d1729c44e0fdc17188cd2ac8fc70b09245"
    assert old["artifact_hash"] == "sha256:e06e3151a201c63c45c960fa4f17c2a04b63a6b49c1271e82c0d3e0147ac3ebb"
    assert new["artifact_hash"] == _hash(new)
    assert new["authority_universe"]["repository_sha"] == "70a4c30e88e01f3923ab3efc4311a77c50b05bba"
    assert new["successor_lineage"]["predecessor_git_blob"] == "976f3b8367c141d4f3f635195a036924aac167c4"
    old_by_id = {item["id"]: item for item in old["failure_mechanisms"]}
    new_by_id = {item["id"]: item for item in new["failure_mechanisms"]}
    assert set(old_by_id) == set(new_by_id)
    pnp = "FM-PNP-C043-C046-SEMANTICS-WITHOUT-INTERACTION"
    assert {key for key in old_by_id if old_by_id[key] != new_by_id[key]} == {pnp}
    for key in ("cross_problem_equivalence_classes", "root_status", "credit_contract", "self_rakl_feedback"):
        assert old[key] == new[key]


def test_c047_atlas_refinement_is_exactly_bounded_not_a_mirrored_family_nogo() -> None:
    atlas = _load(NEW_ATLAS)
    pnp = next(item for item in atlas["failure_mechanisms"] if item["id"] == "FM-PNP-C043-C046-SEMANTICS-WITHOUT-INTERACTION")
    assert pnp["root_cause_status"] == "SUPPORTED_WITHIN_FROZEN_AND_PREFIX_PRESERVING_ORIENTATION_FAMILIES"
    joined_scope = " ".join(pnp["scope"]).lower()
    assert "prefix-preserving new-old mirror" in joined_scope
    assert "literal matrix transpose" in joined_scope
    assert "does not rule out" in joined_scope
    assert "does not establish cover growth" in joined_scope
    assert "1111" in pnp["proximate_cause"] and "1110" in pnp["proximate_cause"]
    assert pnp["source_items"][-1] == "MATH-PNP-C047-ORIENTATION-ONLY-HEADER-SEPARATION"
    assert all((ROOT / pointer).is_file() for pointer in pnp["evidence"])
