from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"
INVALID = (
    BASE
    / "07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_HASH_INVALID_20260811.json"
)
REPAIRED = BASE / "07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_20260811.json"
RECEIPT = BASE / "08_reviews/YM-S1A1_MEMORY_HASH_REPAIR_RECEIPT_20260811.json"
SCHEMA = ROOT / "schemas/artifact-integrity-repair-receipt.schema.json"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def test_yms1a1_memory_hash_repair_preserves_the_failed_identity() -> None:
    invalid = json.loads(INVALID.read_text(encoding="utf-8"))
    repaired = json.loads(REPAIRED.read_text(encoding="utf-8"))
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)

    invalid_for_hash = copy.deepcopy(invalid)
    invalid_for_hash["artifact_hash"] = ""
    computed = _canonical_hash(invalid_for_hash)
    assert invalid["artifact_hash"] != computed
    assert receipt["observed_result"] == {
        "status": "FAIL_HASH_INTEGRITY",
        "stored_artifact_hash": invalid["artifact_hash"],
        "computed_canonical_hash": computed,
        "invalid_file_sha256": _file_hash(INVALID),
    }

    invalid_semantics = copy.deepcopy(invalid)
    repaired_semantics = copy.deepcopy(repaired)
    invalid_semantics.pop("artifact_hash")
    repaired_semantics.pop("artifact_hash")
    assert repaired_semantics == invalid_semantics

    repaired_for_hash = copy.deepcopy(repaired)
    repaired_for_hash["artifact_hash"] = ""
    assert repaired["artifact_hash"] == _canonical_hash(repaired_for_hash)
    assert receipt["repair"]["original_preserved"] is True
    assert receipt["repair"]["semantic_fields_changed"] == []
    assert receipt["repair"]["identity_fields_changed"] == ["artifact_hash"]
    assert receipt["repair"]["repaired_file_sha256"] == _file_hash(REPAIRED)

    receipt_for_hash = copy.deepcopy(receipt)
    receipt_for_hash["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(receipt_for_hash)
    assert "NO_MATHEMATICAL_RESULT" in receipt["authority"]
    assert "PROPOSAL_ONLY" in receipt["reusable_lesson_candidate"]["status"]
