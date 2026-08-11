from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CROSS = ROOT / "research/real_math/millennium/cross_problem"
FRONTIER = CROSS / "01_frontier/XM014_BSD_PNP_PARAMETER_BINDING_20260812.json"
EPISODE = CROSS / "07_memory/XM014_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
DIAGNOSIS = CROSS / "07_memory/XM014_DIAGNOSIS_FAILURE_REUSE_SHADOW_20260812.json"
TRACE = CROSS / "09_trace/XM014_HASH_CHAINED_TRACE_20260812.json"
METRICS = CROSS / "10_study_pattern/RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM014_20260812.json"


def _load(path: Path) -> dict:
    return json.loads(path.read_text())


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def test_xm014_task_episode_is_content_bound_shadow_only() -> None:
    episode = _load(EPISODE)
    payload = {key: value for key, value in episode.items() if key != "artifact_hash"}
    assert hashlib.sha256(_canonical(payload)).hexdigest() == episode["artifact_hash"]
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"


def test_xm014_transfer_has_required_difference_witness_and_suppresses_duplicate() -> None:
    frontier = _load(FRONTIER)
    transfer = frontier["transfer"]
    assert transfer["common_abstraction"]
    assert transfer["enabling_assumptions"]
    assert transfer["disanalogies"]
    assert transfer["predicted_principle"] == "SOURCE_PARAMETER_SEMANTIC_BINDING_BEFORE_TARGET_INSTANTIATION"
    assert transfer["cheapest_falsifier"]
    assert transfer["difference_witness"]["nontransfer"]
    assert frontier["falsifier_result"]["status"] == "FALSIFIER_SUCCEEDED_AGAINST_NOVELTY_CLAIM"


def test_xm014_episode_diagnosis_lesson_remain_distinct() -> None:
    diagnosis = _load(DIAGNOSIS)
    assert diagnosis["episode_id"] != diagnosis["diagnosis_id"]
    assert diagnosis["reusable_obstruction_created"] is False
    assert diagnosis["new_lesson_created"] is False
    assert diagnosis["new_tool_created"] is False
    assert diagnosis["new_motif_created"] is False
    assert "MOTIF-ROOT-CRITICAL-COORDINATE-BEFORE-SCORE" in diagnosis["reused_ids"]
    assert diagnosis["framework_improvement_hypothesis"]["issue_opened"] is False


def test_xm014_hash_chain_is_valid() -> None:
    trace = _load(TRACE)
    previous = "0" * 64
    for event in trace["events"]:
        assert event["prev_hash"] == previous
        expected = hashlib.sha256(_canonical({"prev_hash": previous, "payload": event["payload"]})).hexdigest()
        assert event["event_hash"] == expected
        previous = expected
    assert trace["tail_hash"] == f"sha256:{previous}"


def test_xm014_metrics_preserve_zeroes_and_no_authority_promotion() -> None:
    packet = _load(METRICS)
    metrics = packet["RAKL_CYCLE_METRICS"]
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert metrics["gate_provenance_ci_status"]["authority_promotion"] == "NOT_INVOKED"
    assert metrics["gate_provenance_ci_status"]["root_status"] == "OPEN_ALL_SIX_NO_SOLUTION_CERTIFICATE"
    assert packet["RAKL_METHOD_CASE_STUDY"]["outcome"] == "PARTIAL_SUCCESS_SUCCESSFUL_REUSE_DUPLICATE_PATTERN_SUPPRESSION_TARGET_ALREADY_NORMALIZED"
