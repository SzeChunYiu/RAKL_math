from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"
OLD_FAILURE = (
    BASE
    / "07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_STALE_EVIDENCE_POINTER_20260811.json"
)
LIVE_FAILURE = BASE / "07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_20260811.json"
OLD_MEMORY = (
    BASE
    / "07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_HASH_REPAIRED_20260811.json"
)
LIVE_MEMORY = BASE / "07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_20260811.json"
OLD_TRACE = (
    BASE
    / "09_trace/YM-S1A1_PRE_CANDIDATE_TRACE_MEMORY_HASH_INVALID_20260811.json"
)
LIVE_TRACE = BASE / "09_trace/YM-S1A1_PRE_CANDIDATE_TRACE_20260811.json"
PRE_REVIEW_TRACE = (
    BASE
    / "09_trace/YM-S1A1_PRE_CANDIDATE_TRACE_REVIEW_BINDING_INVALID_20260811.json"
)
OLD_REVIEW = (
    BASE
    / "08_reviews/YM-S1A1_PRE_CANDIDATE_REVIEW_ROLE_COMBINED_20260811.md"
)
LIVE_REVIEW = BASE / "08_reviews/YM-S1A1_PRE_CANDIDATE_REVIEW_20260811.md"
RECEIPT = BASE / "08_reviews/YM-S1A1_PACKET_BINDING_REPAIR_RECEIPT_20260811.json"
SCHEMA = ROOT / "schemas/packet-binding-repair-receipt.schema.json"


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


def _audit_live_review_binding(review_bytes: bytes, trace: dict) -> None:
    review_hash = "sha256:" + hashlib.sha256(review_bytes).hexdigest()
    review_event = next(
        item for item in trace["entries"] if item["event_id"] == "YM-S1A1-E005"
    )
    if review_hash not in review_event["evidence_pointers"]:
        raise ValueError("live_review_hash_not_bound")
    if review_hash not in review_event["outputs"]:
        raise ValueError("live_review_output_hash_not_bound")


def test_yms1a1_packet_binding_repair_preserves_and_supersedes() -> None:
    old_failure = json.loads(OLD_FAILURE.read_text(encoding="utf-8"))
    live_failure = json.loads(LIVE_FAILURE.read_text(encoding="utf-8"))
    old_memory = json.loads(OLD_MEMORY.read_text(encoding="utf-8"))
    live_memory = json.loads(LIVE_MEMORY.read_text(encoding="utf-8"))
    old_trace = json.loads(OLD_TRACE.read_text(encoding="utf-8"))
    pre_review_trace = json.loads(PRE_REVIEW_TRACE.read_text(encoding="utf-8"))
    live_trace = json.loads(LIVE_TRACE.read_text(encoding="utf-8"))
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
    assert receipt["application_repository"]["base_commit"] == receipt["chronology"][
        "base_repair_commit"
    ]
    _git(
        "merge-base",
        "--is-ancestor",
        receipt["application_repository"]["base_commit"],
        "HEAD",
    )
    pin = json.loads((ROOT / "config/rakl-framework-pin.json").read_text())
    assert receipt["framework_pin"]["commit"] == pin["commit"]
    assert receipt["framework_pin"]["commit"] == _git(
        "rev-parse", "HEAD:framework/RAKL"
    )

    stale_pointer = "tests/test_yang_mills_yms1a_source_visibility.py"
    live_pointer = (
        "tests/math_applications/test_yang_mills_yms1a_source_visibility.py"
    )
    assert stale_pointer in old_failure["experiences"][0]["evidence_pointers"]
    assert live_pointer in live_failure["experiences"][0]["evidence_pointers"]
    assert (ROOT / live_pointer).is_file()

    old_memory_for_hash = copy.deepcopy(old_memory)
    old_memory_for_hash["artifact_hash"] = ""
    assert old_memory["artifact_hash"] == _canonical_hash(old_memory_for_hash)
    assert live_memory["failure_lattice_snapshot_hash"] == _canonical_hash(
        live_failure
    )
    live_memory_for_hash = copy.deepcopy(live_memory)
    live_memory_for_hash["artifact_hash"] = ""
    assert live_memory["artifact_hash"] == _canonical_hash(live_memory_for_hash)

    old_memory_event = next(
        item for item in old_trace["entries"] if item["event_id"] == "YM-S1A1-E006"
    )
    live_memory_event = next(
        item for item in live_trace["entries"] if item["event_id"] == "YM-S1A1-E006"
    )
    assert "sha256:9e8e0176a607b4ac63d1231d4b936f9751a0b3e77d1b50bc353eafde98b53279" in (
        old_memory_event["evidence_pointers"] + old_memory_event["outputs"]
    )
    assert live_memory["artifact_hash"] in (
        live_memory_event["evidence_pointers"] + live_memory_event["outputs"]
    )
    assert old_trace["trace_id"] != live_trace["trace_id"]
    assert all(item["event_type"] != "CANDIDATE_PROPOSED" for item in live_trace["entries"])
    _audit_live_review_binding(LIVE_REVIEW.read_bytes(), live_trace)
    try:
        _audit_live_review_binding(LIVE_REVIEW.read_bytes() + b"\nplanted mutation", live_trace)
    except ValueError as exc:
        assert str(exc) == "live_review_hash_not_bound"
    else:
        raise AssertionError("planted review mutation must fail closed")

    expected_files = {
        "old_failure": OLD_FAILURE,
        "live_failure": LIVE_FAILURE,
        "old_memory": OLD_MEMORY,
        "live_memory": LIVE_MEMORY,
        "old_trace": OLD_TRACE,
        "pre_review_trace": PRE_REVIEW_TRACE,
        "live_trace": LIVE_TRACE,
        "old_review": OLD_REVIEW,
        "live_review": LIVE_REVIEW,
    }
    assert set(receipt["artifacts"]) == set(expected_files)
    for key, path in expected_files.items():
        assert receipt["artifacts"][key] == {
            "path": str(path.relative_to(ROOT)),
            "file_sha256": _file_hash(path),
        }

    assert receipt["observed_failures"] == [
        "STALE_EVIDENCE_POINTER",
        "FAIL_DEPENDENCY_BINDING",
        "FAIL_REVIEW_BINDING",
    ]
    assert receipt["lineage"]["supersedes_trace_id"] == old_trace["trace_id"]
    assert receipt["lineage"]["repaired_trace_id"] == live_trace["trace_id"]
    assert receipt["lineage"]["old_memory_hash"] == old_memory["artifact_hash"]
    assert receipt["lineage"]["live_memory_hash"] == live_memory["artifact_hash"]
    assert receipt["lineage"]["pre_review_trace_id"] == pre_review_trace["trace_id"]
    assert receipt["lineage"]["old_review_file_sha256"] == _file_hash(OLD_REVIEW)
    assert receipt["lineage"]["live_review_file_sha256"] == _file_hash(LIVE_REVIEW)
    assert "NO_MATHEMATICAL_RESULT" in receipt["authority"]

    receipt_for_hash = copy.deepcopy(receipt)
    receipt_for_hash["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(receipt_for_hash)
