from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_NS_R6_SUCCESSOR_20260812.json"
NEW = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_PNP_C050_K15_SUCCESSOR_20260812.json"
ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_YM_R20_HODGE_C007_SUCCESSOR_20260812.json"
BASE = "594a29b310706618e30d61a6f7418ff231477b41"
FRAMEWORK = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
ITEM = "MATH-PNP-C050-K15-FIXED-CODE-MAGIC-SEPARATION"
RAW = "7926aaf6742df7e924e3927c2d33f0751dcef427efd239a51694c082d3f0e37d"
BLOB = "b9e27ac2040879a042cd273ae578f1b5c4c745dd"


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def semantic(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_hash(value: dict) -> str:
    value = copy.deepcopy(value)
    value["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(semantic(value)).hexdigest()


def items(value: dict) -> dict[str, dict]:
    return {item["item_id"]: item for lane in value["lanes"] for item in lane["credited_items"]}


def test_c050_successor_binds_exact_current_main_and_predecessor() -> None:
    old, new = load(OLD), load(NEW)
    assert new["base_repository_sha"] == BASE
    assert new["authority_universe"]["repository_sha"] == BASE
    assert new["authority_universe"]["pending_or_open_pr_material_counted"] is False
    lineage = new["successor_lineage"]
    assert lineage["predecessor_artifact_hash"] == old["artifact_hash"]
    assert lineage["predecessor_raw_sha256"] == RAW == hashlib.sha256(OLD.read_bytes()).hexdigest()
    assert lineage["predecessor_git_blob"] == BLOB
    assert lineage["predecessor_path"] == OLD.relative_to(ROOT).as_posix()
    assert new["artifact_hash"] == artifact_hash(new)


def test_exactly_one_c050_unit_and_all_47_predecessor_units_preserved() -> None:
    old, new = load(OLD), load(NEW)
    before, after = items(old), items(new)
    assert set(after) - set(before) == {ITEM}
    assert len(before) == 47 and len(after) == len(set(after)) == 48
    for item_id, value in before.items():
        assert semantic(after[item_id]) == semantic(value), item_id
    assert new["totals"]["mathematical_credit_units"] == 48
    assert new["totals"]["mathematical_credit_units_by_lane"]["p_vs_np"] == 17
    assert new["totals"]["mathematical_credit_units_by_type"]["PROOF_OR_LEMMA"] == 16


def test_c050_unit_is_scoped_k15_proof_and_k_greater_than_15_remains_open() -> None:
    ledger = load(NEW)
    item = items(ledger)[ITEM]
    assert item["credit_type"] == "PROOF_OR_LEMMA"
    assert item["credit_units"] == 1 and item["mathematical_credit"] is True
    assert item["authority"] == "SAME_CONTEXT_HAND_DERIVATION_RECORD_CHECK_PASS"
    for text in (
        "H_15 intersection P_16 is empty",
        "h[3]=1",
        "p[3]=MAGIC[3]=0",
        "(v,m)=(2,2),(3,2)",
        "(v,m)=(8,1),...,(15,1)",
    ):
        assert text in item["exact_claim"]
    boundary = " ".join(item["non_implications"])
    assert "k>15 remains open" in boundary
    assert "P versus NP" in boundary
    assert all((ROOT / p).is_file() for p in item["evidence_pointers"])


def test_candidate_freeze_stays_zero_and_result_is_synthesized_once() -> None:
    ledger = load(NEW)
    freeze = ledger["bounded_disposition"]["pnp_c050_k15_freeze"]
    assert freeze["credit_units"] == 0
    result = ledger["bounded_disposition"]["pnp_c050_k15_evaluated_result"]
    assert result == {
        "classification": "SCOPED_EXACT_SYMBOLIC_IMPOSSIBILITY_PROOF",
        "credit_units": 1,
        "credited_item_id": ITEM,
        "state": "MERGED_RESULT_SYNTHESIZED_THIS_SUCCESSOR",
        "k_greater_than_15": "OPEN",
    }
    atlas = ledger["bounded_disposition"]["failure_atlas"]
    assert atlas["action"] == "NO_NEW_DISTINCT_CAUSE"
    assert atlas["added_cause_ids"] == []
    assert atlas["existing_specialized_cause_id"] == "FM-PNP-C049-FIRST-ADMISSIBLE-FIELD-ALIGNMENT-CONFLICT"
    assert atlas["unchanged_atlas_path"] == ATLAS.relative_to(ROOT).as_posix()
    assert not (MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_PNP_C050_K15_SUCCESSOR_20260812.json").exists()


def test_software_and_review_have_zero_mathematical_credit() -> None:
    item = items(load(NEW))[ITEM]
    text = " ".join(item["non_implications"]).lower()
    for term in ("git", "ci", "tests", "schemas", "hashes", "chronology", "runtime"):
        assert term in text
    assert "same-context review supplies zero independent-review credit" in text
