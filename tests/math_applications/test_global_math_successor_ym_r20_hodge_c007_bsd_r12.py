from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_HODGE_C006_SUCCESSOR_20260812.json"
NEW_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_YM_R20_HODGE_C007_BSD_R12_SUCCESSOR_20260812.json"
OLD_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_HODGE_C006_SUCCESSOR_20260812.json"
NEW_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_YM_R20_HODGE_C007_SUCCESSOR_20260812.json"
BASE = "02c5fb7764116cf075d8dd5efd7b6fe835275ab9"
FRAMEWORK = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
NEW_ITEM_IDS = {
    "MATH-YM-R20-SHRINKING-GRAPH-INVARIANCE-AND-RELEVANT-MARGIN",
    "MATH-HODGE-C007-SINGULAR-TANGENT-SURJECTIVITY-NONIMPLICATION",
    "MATH-BSD-R12-PINFINITY-VP-COEFFICIENT-CORANK-DIMENSION-EQUALITY",
}
NEW_CAUSE_IDS = {
    "FM-YM-R20-SHRINKING-DOMAIN-RELEVANT-MARGIN",
    "FM-HODGE-C007-SINGULAR-TANGENT-EXCESS-NONINTEGRABILITY",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(document: dict) -> str:
    payload = copy.deepcopy(document)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def items(document: dict) -> dict[str, dict]:
    return {
        item["item_id"]: item
        for lane in document["lanes"]
        for item in lane["credited_items"]
    }


def causes(document: dict) -> dict[str, dict]:
    return {item["id"]: item for item in document["failure_mechanisms"]}


def test_successors_bind_live_merged_authority_and_preserve_predecessors() -> None:
    old_ledger, new_ledger = load(OLD_LEDGER), load(NEW_LEDGER)
    old_atlas, new_atlas = load(OLD_ATLAS), load(NEW_ATLAS)
    assert new_ledger["base_repository_sha"] == BASE
    assert new_ledger["authority_universe"]["repository_sha"] == BASE
    assert new_atlas["authority_universe"] == {
        "framework_sha": FRAMEWORK,
        "kind": "MERGED_ORIGIN_MAIN_ONLY",
        "repository_sha": BASE,
    }
    for old_path, old, new in (
        (OLD_LEDGER, old_ledger, new_ledger),
        (OLD_ATLAS, old_atlas, new_atlas),
    ):
        lineage = new["successor_lineage"]
        assert lineage["predecessor_artifact_hash"] == old["artifact_hash"]
        assert lineage["predecessor_raw_sha256"] == hashlib.sha256(old_path.read_bytes()).hexdigest()
        assert lineage["predecessor_path"] == old_path.relative_to(ROOT).as_posix()
    assert new_ledger["artifact_hash"] == canonical_hash(new_ledger)
    assert new_atlas["artifact_hash"] == canonical_hash(new_atlas)


def test_exactly_three_deduplicated_math_units_and_expected_totals() -> None:
    old, new = load(OLD_LEDGER), load(NEW_LEDGER)
    old_items, new_items = items(old), items(new)
    assert set(new_items) - set(old_items) == NEW_ITEM_IDS
    assert all(new_items[key] == value for key, value in old_items.items())
    assert len(new_items) == len(set(new_items)) == 46
    assert {key: new_items[key]["credit_type"] for key in NEW_ITEM_IDS} == {
        "MATH-YM-R20-SHRINKING-GRAPH-INVARIANCE-AND-RELEVANT-MARGIN": "BROKEN_MATHEMATICAL_ASSUMPTION",
        "MATH-HODGE-C007-SINGULAR-TANGENT-SURJECTIVITY-NONIMPLICATION": "EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE",
        "MATH-BSD-R12-PINFINITY-VP-COEFFICIENT-CORANK-DIMENSION-EQUALITY": "TRANSFER_CONDITION",
    }
    assert new["totals"]["mathematical_credit_units"] == 46
    assert new["totals"]["mathematical_credit_units_by_lane"] == {
        "p_vs_np": 16,
        "riemann_hypothesis": 7,
        "navier_stokes": 10,
        "yang_mills": 5,
        "hodge_conjecture": 5,
        "birch_swinnerton_dyer": 3,
        "poincare_conjecture": 0,
    }
    assert new["totals"]["mathematical_credit_units_by_type"] == {
        "BROKEN_MATHEMATICAL_ASSUMPTION": 7,
        "EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE": 17,
        "MATHEMATICAL_FALSIFIER": 1,
        "PROOF_OR_LEMMA": 14,
        "TRANSFER_CONDITION": 7,
    }
    assert all(new_items[key]["credit_units"] == 1 for key in NEW_ITEM_IDS)
    assert all((ROOT / pointer).is_file() for key in NEW_ITEM_IDS for pointer in new_items[key]["evidence_pointers"])


def test_math_only_rubric_and_zero_software_credit_boundaries() -> None:
    ledger = load(NEW_LEDGER)
    new_items = items(ledger)
    ym = new_items["MATH-YM-R20-SHRINKING-GRAPH-INVARIANCE-AND-RELEVANT-MARGIN"]
    assert "c g_{k+1}^2<=c g_k^2" in ym["exact_claim"]
    assert "(1-C_2)c_lambda>=C_2(1+c_K)" in ym["exact_claim"]
    hodge = new_items["MATH-HODGE-C007-SINGULAR-TANGENT-SURJECTIVITY-NONIMPLICATION"]
    assert "d pi_0 surjective" in hodge["exact_claim"]
    assert "pi(W)=W is a proper closed subset" in hodge["exact_claim"]
    assert "smooth at some w" in hodge["exact_claim"]
    assert ledger["bounded_disposition"]["hodge_c007"]["attached_certificate_credit_units"] == 0
    bsd = new_items["MATH-BSD-R12-PINFINITY-VP-COEFFICIENT-CORANK-DIMENSION-EQUALITY"]
    for term in ("maximal divisible subgroup", "full Z_p-lattice", "finite quotient", "without assuming Sha finiteness"):
        assert term in bsd["exact_claim"]
    for item in (ym, hodge, bsd):
        boundary = " ".join(item["non_implications"]).lower()
        for term in ("git", "ci", "tests", "schemas", "hashes", "chronology"):
            assert term in boundary
        assert item["scope"]
        assert item["evidence_pointers"]
    excluded = next(x for x in ledger["excluded_provenance"] if x["item_id"] == "EXCLUDED-PNP-C050-K15-FREEZE-WITHOUT-TARGET-RESULT")
    assert excluded["mathematical_credit"] is False and excluded["credit_units"] == 0
    assert "no evaluated target mathematical result" in excluded["reason"].lower()


def test_failure_atlas_adds_exactly_two_distinct_causes_and_no_bsd_cause() -> None:
    old, new = load(OLD_ATLAS), load(NEW_ATLAS)
    old_causes, new_causes = causes(old), causes(new)
    assert set(new_causes) - set(old_causes) == NEW_CAUSE_IDS
    assert all(new_causes[key] == value for key, value in old_causes.items())
    assert len(new_causes) == len(set(new_causes)) == len(old_causes) + 2
    assert not any(key.startswith("FM-BSD-R12") for key in new_causes)
    disposition = load(NEW_LEDGER)["bounded_disposition"]["failure_atlas"]
    assert set(disposition["cause_ids"]) == NEW_CAUSE_IDS
    assert disposition["bsd_r12_failure_cause_added"] is False


def test_new_causes_satisfy_full_math_lesson_rubric() -> None:
    new = causes(load(NEW_ATLAS))
    for cause_id in NEW_CAUSE_IDS:
        cause = new[cause_id]
        for field in (
            "failed_inference",
            "exact_result",
            "supported_causes",
            "competing_causes",
            "scope",
            "falsifier",
            "repair",
            "evidence",
        ):
            assert cause[field], (cause_id, field)
        assert all((ROOT / path).is_file() for path in cause["evidence"])
    ym = new["FM-YM-R20-SHRINKING-DOMAIN-RELEVANT-MARGIN"]
    assert "wrong inequality direction" in ym["supported_causes"][0]["cause"]
    assert any("C_2<1" in row["cause"] for row in ym["supported_causes"])
    hodge = new["FM-HODGE-C007-SINGULAR-TANGENT-EXCESS-NONINTEGRABILITY"]
    assert "excess Zariski tangent directions" in hodge["proximate_cause"]
    assert "smoothness" in hodge["falsifier"] and "properness" in hodge["falsifier"]
