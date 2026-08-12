from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "real_math" / "millennium" / "p_vs_np"


def gamma_len(n: int) -> int:
    return 2 * n.bit_length() - 1


def raw_len(v: int, m: int) -> int:
    return 8 + gamma_len(v) + gamma_len(m) + 3 * m * (v.bit_length() + 1)


def canonical_len(v: int, m: int) -> int:
    n = raw_len(v, m)
    return n + (n % 2)


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def test_k14_length_support_matches_hand_proof_calibration() -> None:
    # This finite regression is calibration only; the cycle packet contains the hand proof.
    at_28 = [(v, m) for v in range(1, 257) for m in range(1, 65) if canonical_len(v, m) == 28]
    at_30 = [(v, m) for v in range(1, 257) for m in range(1, 65) if canonical_len(v, m) == 30]
    assert at_28 == []
    assert at_30 == [(1, 3)]


def test_v2_task_episode_hash_matches_current_v3_contract() -> None:
    path = BASE / "09_trace" / "O9d12a2a1b_C050_K14_TASK_EPISODE_V2_20260812.json"
    container = json.loads(path.read_text())
    assert "episode_id" not in container
    assert container["inventory_disposition"] == "NESTED_TASK_EPISODE_NOT_TOP_LEVEL_INVENTORY_OBJECT"
    episode = container["task_episode"]
    payload = {
        "episode_id": episode["episode_id"],
        "task_id": episode["task_id"],
        "atom_id": episode["atom_id"],
        "context_hash": episode["context_hash"],
        "problem_signature": episode["problem_signature"],
        "fibre_snapshot_hash": episode["fibre_snapshot_hash"],
        "operator_ids": episode["operator_ids"],
        "action_trace": episode["action_trace"],
        "observation_ids": episode["observation_ids"],
        "verification_ids": episode["verification_ids"],
        "outcome": episode["outcome"],
        "residual_signature": episode["residual_signature"],
        "evidence_pointers": episode["evidence_pointers"],
        "timestamp": episode["timestamp"],
        "cost": episode["cost"],
        "storage_admission": episode["storage_admission"],
    }
    assert hashlib.sha256(canonical_bytes(payload)).hexdigest() == episode["artifact_hash"]
    assert episode["artifact_hash"] == "496ba5c27f125f228900d565cf45c9d2fb96b9e58d8fe9dfdaa9ade64832f38a"
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"


def test_v2_trace_is_hash_chained() -> None:
    path = BASE / "09_trace" / "O9d12a2a1b_C050_K14_TRACE_V2_20260812.json"
    trace = json.loads(path.read_text())
    previous = "GENESIS"
    for index, event in enumerate(trace["events"]):
        assert event["index"] == index
        assert event["previous_event_hash"] == previous
        payload = {key: value for key, value in event.items() if key != "event_hash"}
        assert hashlib.sha256(canonical_bytes(payload)).hexdigest() == event["event_hash"]
        previous = event["event_hash"]
    assert trace["last_event_hash"] == previous


def test_correction_preserves_zero_protected_novelty_and_open_root() -> None:
    path = BASE / "10_case_study" / "C050_K14_TELEMETRY_HASH_CORRECTION_20260812.json"
    doc = json.loads(path.read_text())
    metrics = doc["RAKL_CYCLE_METRICS_CORRECTION"]
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert metrics["correction_counts_as_learning"] is False
    assert doc["replacement_task_episode"]["json_pointer"] == "/task_episode"
    assert doc["ci_failure_correction"]["diagnosis"] == "TOOLING_REPOSITORY_INVENTORY_INTEGRATION_FAILURE_NOT_MATHEMATICAL_FAILURE"
    assert doc["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert doc["negative_history_preserved"] is True
