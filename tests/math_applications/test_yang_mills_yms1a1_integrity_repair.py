from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"
INVALID = (
    BASE
    / "07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_HASH_INVALID_20260811.json"
)
REPAIRED = (
    BASE
    / "07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_HASH_REPAIRED_20260811.json"
)
RECEIPT = BASE / "08_reviews/YM-S1A1_MEMORY_HASH_REPAIR_RECEIPT_20260811.json"
SCHEMA = ROOT / "schemas/artifact-integrity-repair-receipt.schema.json"
FRAMEWORK_PIN_SYNC = ROOT / "receipts/framework-pin-sync-bd1a276-20260811.json"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _git(*arguments: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def _audit_exact_provenance(receipt: dict) -> None:
    subject = receipt["subject"]
    source_spec = f'{subject["source_commit"]}:{subject["source_path"]}'
    if _git("rev-parse", source_spec) != subject["source_git_blob"]:
        raise ValueError("source_commit_path_blob_mismatch")
    if _git("hash-object", str(INVALID)) != subject["source_git_blob"]:
        raise ValueError("invalid_copy_not_equal_to_source_blob")
    if not receipt["repair"]["original_preserved"]:
        raise ValueError("original_not_preserved")
    if _git(
        "merge-base",
        "--is-ancestor",
        receipt["application_repository"]["base_commit"],
        "HEAD",
    ):
        raise ValueError("base_commit_not_ancestor")


def test_yms1a1_memory_hash_repair_preserves_the_failed_identity() -> None:
    invalid = json.loads(INVALID.read_text(encoding="utf-8"))
    repaired = json.loads(REPAIRED.read_text(encoding="utf-8"))
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
    _audit_exact_provenance(receipt)

    assert receipt["subject"]["source_path"] == str(
        INVALID.relative_to(ROOT)
    ).replace("_HASH_INVALID", "")
    assert receipt["repair"]["invalid_path"] == str(INVALID.relative_to(ROOT))
    assert receipt["repair"]["repaired_path"] == str(REPAIRED.relative_to(ROOT))
    pin = json.loads((ROOT / "config/rakl-framework-pin.json").read_text())
    pin_sync = json.loads(FRAMEWORK_PIN_SYNC.read_text(encoding="utf-8"))
    assert receipt["framework_pin"]["commit"] == pin_sync["previous_framework_commit"]
    assert pin_sync["current_framework_commit"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert pin["commit"] == _git("rev-parse", "HEAD:framework/RAKL")
    assert pin_sync["semantic_authority_compatibility"][
        "historical_artifacts_keep_recorded_framework_commits"
    ] is True

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


def test_yms1a1_memory_hash_repair_provenance_fails_closed() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    missing_source = copy.deepcopy(receipt)
    missing_source["subject"]["source_path"] += ".missing"
    try:
        _audit_exact_provenance(missing_source)
    except (subprocess.CalledProcessError, ValueError):
        pass
    else:
        raise AssertionError("missing historical source must fail closed")

    forged_blob = copy.deepcopy(receipt)
    forged_blob["subject"]["source_git_blob"] = "0" * 40
    try:
        _audit_exact_provenance(forged_blob)
    except ValueError as exc:
        assert str(exc) == "source_commit_path_blob_mismatch"
    else:
        raise AssertionError("forged source blob must fail closed")
