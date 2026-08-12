from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "research/real_math/millennium/p_vs_np/07_memory/C034_C040_MATH_ONLY_LESSON_RECLASSIFICATION_20260812.json"
REQUIRED = {
    "attempted_mathematical_implication",
    "exact_result_or_failure",
    "supported_and_competing_mathematical_causes",
    "scope",
    "mathematical_falsifier",
    "repair_or_next_mathematical_move",
    "proof_or_source_evidence",
}
ZERO_CREDIT_TERMS = ("git", "branch", "commit", "pull-request", "merge", "ci", "schema", "hash", "chronology")


def _load() -> dict:
    value = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def test_reclassification_is_hash_bound_and_root_open() -> None:
    artifact = _load()
    assert artifact["artifact_hash"] == _hash(artifact)
    assert artifact["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert artifact["synthesis"]["root_impact"] == "NONE"
    assert artifact["synthesis"]["framework_promotion_authority"] is False
    assert artifact["synthesis"]["independent_review_authority"] is False


def test_every_credited_unit_is_a_complete_math_lesson() -> None:
    artifact = _load()
    lessons = artifact["mathematical_lessons"]
    assert len(lessons) == 5
    assert sum(item["credit_units"] for item in lessons) == artifact["synthesis"]["unique_scoped_mathematical_credit_units"] == 5
    assert len({item["lesson_id"] for item in lessons}) == 5
    for item in lessons:
        assert item["credit_units"] == 1
        lesson = item["seven_field_mathematical_lesson"]
        assert set(lesson) == REQUIRED
        assert all(isinstance(lesson[field], str) and lesson[field].strip() for field in REQUIRED)


def test_operational_records_are_retained_at_zero_math_credit() -> None:
    artifact = _load()
    operational = artifact["operational_provenance_zero_credit"]
    assert len(operational) == artifact["synthesis"]["operational_items_retained_at_zero_credit"] == 4
    assert all(item["classification"] == "NO_MATHEMATICAL_LESSON" for item in operational)
    assert all(item["credit_units"] == 0 for item in operational)
    joined = " ".join(item["reason"].lower() for item in operational)
    assert any(term in joined for term in ZERO_CREDIT_TERMS)


def test_authority_boundaries_do_not_turn_computation_into_proof() -> None:
    artifact = _load()
    assert artifact["classification_contract"]["computation_is_proof"] is False
    assert artifact["classification_contract"]["same_context_review_is_independent_review"] is False
    u8 = next(item for item in artifact["mathematical_lessons"] if "C034B" in item["lesson_id"])
    c037 = next(item for item in artifact["mathematical_lessons"] if "C037" in item["lesson_id"])
    assert "FINITE" in u8["authority"] and "ASYMPTOTIC" in u8["authority"]
    assert "FINITE" in c037["authority"]
    assert artifact["nonclaims"][-1].endswith("zero mathematical-learning credit.")
