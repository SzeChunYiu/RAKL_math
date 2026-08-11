from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TRACE_DIR = ROOT / "research/real_math/millennium/p_vs_np/09_trace"
ORIGINAL = TRACE_DIR / "O9d12a2a1a_PRE_CANDIDATE_TRACE_20260811.json"
REPAIRED = (
    TRACE_DIR
    / "O9d12a2a1a_PRE_CANDIDATE_TRACE_MIGRATION_REPAIRED_20260811.json"
)
RECEIPT = ROOT / "migration/O9d12a2a1a_TRACE_INTEGRITY_REPAIR_RECEIPT_20260811.json"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _event_hash(event: dict) -> str:
    payload = copy.deepcopy(event)
    payload["artifact_hash"] = ""
    return _canonical_hash(payload)


def test_receipt_preserves_the_source_failure_and_is_self_hashing() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    original = json.loads(ORIGINAL.read_text(encoding="utf-8"))

    receipt_for_hash = copy.deepcopy(receipt)
    receipt_for_hash["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(receipt_for_hash)
    assert receipt["source_provenance"]["source_file_sha256"] == _file_hash(ORIGINAL)
    assert receipt["source_provenance"]["migration_byte_preservation"] == (
        "VERIFIED_EQUAL_TO_SOURCE_COMMIT"
    )

    observed = receipt["observed_result"]
    assert observed["status"] == "FAIL_HASH_INTEGRITY"
    assert observed["invalid_event_ids"] == [
        "O9d12a2a1a-E01",
        "O9d12a2a1a-E02",
        "O9d12a2a1a-E03",
        "O9d12a2a1a-E04",
        "O9d12a2a1a-E05",
        "O9d12a2a1a-E06",
    ]
    assert observed["valid_event_ids"] == ["O9d12a2a1a-E07"]
    assert observed["stored_chain_links_valid"] is True

    computed = {item["event_id"]: item for item in observed["event_audit"]}
    previous = ""
    for event in original["entries"]:
        item = computed[event["event_id"]]
        assert item["stored_artifact_hash"] == event["artifact_hash"]
        assert item["computed_canonical_hash"] == _event_hash(event)
        assert item["previous_link_valid"] == (event["previous_event_hash"] == previous)
        previous = event["artifact_hash"]

    assert receipt["diagnosis"]["status"] == "BOUNDED_UNRESOLVED_CAUSE"
    assert receipt["repair"]["original_preserved"] is True
    assert "NO_MATHEMATICAL_CANDIDATE" in receipt["authority"]
    assert "ROOT_AUTHORITY_NONE" in receipt["authority"]


def test_repaired_trace_changes_only_identity_and_hash_chain_fields() -> None:
    original = json.loads(ORIGINAL.read_text(encoding="utf-8"))
    repaired = json.loads(REPAIRED.read_text(encoding="utf-8"))
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    assert receipt["repair"]["repaired_file_sha256"] == _file_hash(REPAIRED)
    assert repaired["trace_id"] == receipt["repair"]["repaired_trace_id"]
    assert repaired["trace_id"] != original["trace_id"]
    assert len(repaired["entries"]) == len(original["entries"])

    previous = ""
    for old_event, new_event in zip(original["entries"], repaired["entries"], strict=True):
        old_semantics = {
            key: value
            for key, value in old_event.items()
            if key not in {"artifact_hash", "previous_event_hash"}
        }
        new_semantics = {
            key: value
            for key, value in new_event.items()
            if key not in {"artifact_hash", "previous_event_hash"}
        }
        assert new_semantics == old_semantics
        assert new_event["previous_event_hash"] == previous
        assert new_event["artifact_hash"] == _event_hash(new_event)
        previous = new_event["artifact_hash"]

    assert all(
        event["event_type"] != "CANDIDATE_PROPOSED" for event in repaired["entries"]
    )
