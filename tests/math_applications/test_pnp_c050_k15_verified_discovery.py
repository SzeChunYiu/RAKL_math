from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
PRE = BASE / "09_trace/O9d12a2a1b_C050_K15_TARGET_EVAL_PRE_ACTION_20260812.json"
RESULT = BASE / "05_falsification/O9d12a2a1b_C050_K15_RESULT_20260812.json"
EPISODE = BASE / "09_trace/O9d12a2a1b_C050_K15_TASK_EPISODE_20260812.json"
TRACE = BASE / "09_trace/O9d12a2a1b_C050_K15_TRACE_20260812.json"
CASE = BASE / "10_case_study/C050_K15_VERIFIED_DISCOVERY_CYCLE_20260812.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_sha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def test_pre_action_receipt_and_fibre_hashes_are_exact() -> None:
    packet = _load(PRE)
    assert _canonical_sha(packet["pre_action_receipt"]) == packet["pre_action_receipt_sha256"]
    assert _canonical_sha(packet["actual_fibre"]) == packet["actual_fibre_sha256"]
    assert packet["successor_authorization"]["target_result_access_authorized_after_this_freeze"] is True


def test_k15_result_is_scoped_bit3_separation_only() -> None:
    result = _load(RESULT)
    math = result["exact_mathematical_result"]
    assert "H_15 intersection P_16 is empty" in math["lemma"]
    assert any("bit 3 equal to 1" in step for step in math["proof_core"])
    assert any("MAGIC[3]=0" in step for step in math["proof_core"])
    assert "any statement for k>15" in math["does_not_establish"]
    calibration = result["counterexample_first_verification"]["bounded_calibration"]
    assert calibration["authority"] == "CALIBRATION_ONLY_NOT_PROOF"
    assert calibration["intersection_size"] == 0


def test_task_episode_hash_matches_current_v3_content_contract() -> None:
    packet = _load(EPISODE)
    episode = packet["task_episode"]
    content = {key: value for key, value in episode.items() if key != "artifact_hash"}
    assert _canonical_sha(content) == episode["artifact_hash"]
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert packet["inventory_disposition"] == "NESTED_TASK_EPISODE_NOT_TOP_LEVEL_INVENTORY_OBJECT"


def test_trace_chain_is_exact_and_preserves_tooling_negative_history() -> None:
    packet = _load(TRACE)
    prev = packet["initial_prev_hash"]
    for event in packet["events"]:
        assert event["prev_hash"] == prev
        payload = {key: value for key, value in event.items() if key != "event_hash"}
        assert _canonical_sha(payload) == event["event_hash"]
        prev = event["event_hash"]
    assert packet["last_hash"] == prev
    assert packet["negative_history"]["mathematical_effect"] == "NONE"


def test_metrics_keep_protected_novelty_zero_and_root_open() -> None:
    case = _load(CASE)
    metrics = case["RAKL_CYCLE_METRICS"]
    assert metrics["retained_semantic_novelty_protected"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert case["application_subject"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert case["same_context_expert_cell"]["independent_review_credit"] == "0/3"
    assert metrics["rakl_changed_observable_action"].startswith("YES:")
