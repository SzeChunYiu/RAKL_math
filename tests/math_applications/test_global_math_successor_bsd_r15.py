from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_RH_C002_SUCCESSOR_20260812.json"
NEW_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_BSD_R15_SUCCESSOR_20260812.json"
OLD_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_YM_R20_HODGE_C007_SUCCESSOR_20260812.json"
NEW_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_BSD_R15_SUCCESSOR_20260812.json"
LESSON = ROOT / "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a2_R15_SCOPED_MATHEMATICAL_LESSON_20260812.json"
BASE = "f3275302b2198bbd15d551d57adce85c5762c013"
ITEM = "MATH-BSD-R15-KUMMER-SHA-CORANK-DECOMPOSITION"
SPECIALIZATION = "SP-BSD-R15-UNCONTROLLED-QUOTIENT-CORANK"
PARENT = "FM-BSD-ARITHMETIC-PREMISE-REIMPORT"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(semantic(payload)).hexdigest()


def items(value: dict) -> dict[str, dict]:
    return {item["item_id"]: item for lane in value["lanes"] for item in lane["credited_items"]}


def test_exactly_one_new_deduplicated_bsd_proof_unit() -> None:
    old, new = load(OLD_LEDGER), load(NEW_LEDGER)
    before, after = items(old), items(new)
    assert set(after) - set(before) == {ITEM}
    assert len(before) == 49 and len(after) == len(set(after)) == 50
    for item_id, value in before.items():
        assert semantic(after[item_id]) == semantic(value), item_id
    assert new["base_repository_sha"] == BASE
    assert new["authority_universe"]["repository_sha"] == BASE
    assert new["totals"]["mathematical_credit_units"] == 50
    assert new["totals"]["mathematical_credit_units_by_lane"]["birch_swinnerton_dyer"] == 4
    assert new["totals"]["mathematical_credit_units_by_type"]["PROOF_OR_LEMMA"] == 18


def test_bsd_unit_is_mathematical_and_preserves_seven_fields() -> None:
    ledger, lesson = load(NEW_LEDGER), load(LESSON)
    item = items(ledger)[ITEM]
    assert item["credit_type"] == "PROOF_OR_LEMMA"
    assert item["credit_units"] == 1 and item["mathematical_credit"] is True
    assert "corank_Zp Sel" in item["exact_claim"]
    assert "rank_Z E(Q)" in item["exact_claim"]
    assert "corank_Zp Sha" in item["exact_claim"]
    fields = item["seven_field_math_lesson"]
    assert fields["attempted_implication"] == lesson["attempted_implication"]
    assert fields["exact_result_or_failure"] == lesson["exact_result_or_failure"]
    assert fields["supported_and_competing_causes"] == lesson["supported_and_competing_causes"]
    assert fields["scope"] == lesson["scope"]
    assert fields["mathematical_falsifier"] == lesson["mathematical_falsifier"]
    assert fields["mathematical_repair_or_next_discriminator"] == lesson["mathematical_repair_or_next_discriminator"]
    assert fields["proof_or_source_evidence"] == lesson["proof_or_source_evidence"]
    assert all((ROOT / path).is_file() for path in item["evidence_pointers"])


def test_r15_is_distinct_from_r9_and_r12_but_not_a_new_failure_cause() -> None:
    ledger = load(NEW_LEDGER)
    item = items(ledger)[ITEM]
    dedup = item["deduplication"]
    assert "R9 gives only" in dedup["new_relative_to_bsd_r9"]
    assert "R12 equates" in dedup["new_relative_to_bsd_r12"]
    disposition = ledger["bounded_disposition"]
    assert disposition["bsd_r15"]["credit_units"] == 1
    assert disposition["bsd_r15"]["new_global_failure_cause_units"] == 0
    assert disposition["failure_atlas"]["added_cause_ids"] == []
    assert disposition["failure_atlas"]["specialization_id"] == SPECIALIZATION
    assert disposition["failure_atlas"]["parent_cause_id"] == PARENT


def test_atlas_preserves_all_12_causes_and_adds_only_typed_specialization() -> None:
    old, new = load(OLD_ATLAS), load(NEW_ATLAS)
    assert len(old["failure_mechanisms"]) == len(new["failure_mechanisms"]) == 12
    assert semantic(old["failure_mechanisms"]) == semantic(new["failure_mechanisms"])
    assert semantic(old["cross_problem_equivalence_classes"]) == semantic(new["cross_problem_equivalence_classes"])
    assert new["authority_universe"]["framework_sha"] == old["authority_universe"]["framework_sha"]
    assert new["bounded_disposition"]["new_distinct_failure_mechanism_ids"] == []
    assert new["bounded_disposition"]["added_specialization_ids"] == [SPECIALIZATION]
    specialization = new["failure_mechanism_specializations"]
    assert len(specialization) == 1
    specialization = specialization[0]
    assert specialization["specialization_id"] == SPECIALIZATION
    assert specialization["parent_cause_id"] == PARENT
    assert specialization["equivalence_class"] == "CROSS-REPRESENTATION-RELOCATION"
    assert specialization["new_global_failure_cause_credit_units"] == 0
    assert "Sha(E/Q)[p^infinity]" in specialization["mechanism_mapping"]["relocated_or_reimported_obligation"]


def test_specialization_is_a_complete_mathematical_cause_record() -> None:
    specialization = load(NEW_ATLAS)["failure_mechanism_specializations"][0]
    for field in (
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_discriminator",
        "proof_or_source_evidence",
    ):
        assert specialization[field]
    assert specialization["classification"] == "VERIFIED_EXACT_SEQUENCE_SPECIALIZATION_NOT_NEW_CAUSE"
    assert "exact Kummer-Selmer corank identity" in specialization["supported_and_competing_causes"]["supported"]
    assert "No actual elliptic curve" in specialization["nonclaim"]


def test_root_and_operational_credit_boundaries_remain_closed() -> None:
    ledger, atlas = load(NEW_LEDGER), load(NEW_ATLAS)
    lane = next(lane for lane in ledger["lanes"] if lane["lane_id"] == "birch_swinnerton_dyer")
    assert lane["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    item = items(ledger)[ITEM]
    boundary = " ".join(item["non_implications"]).lower()
    for term in ("git", "ci", "schemas", "hashes", "chronology", "telemetry", "same-context"):
        assert term in boundary
    assert atlas["credit_contract"]["software_assurance_credit_units"] == 0
    assert atlas["credit_contract"]["atlas_synthesis_creates_new_mathematical_credit"] is False


def test_successors_are_content_bound() -> None:
    for path in (NEW_LEDGER, NEW_ATLAS):
        value = load(path)
        assert value["artifact_hash"] == artifact_hash(value)
