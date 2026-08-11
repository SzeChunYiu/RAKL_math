from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def check_self_hash(path: Path) -> dict:
    obj = json.loads(path.read_text())
    claimed = obj.pop("artifact_hash")
    assert claimed.startswith("sha256:")
    assert hashlib.sha256(canonical(obj)).hexdigest() == claimed.split(":", 1)[1]
    return obj


def test_ns_b1a2_context_and_memory_are_content_bound() -> None:
    context = check_self_hash(BASE / "01_frontier/NS-B1a2_CONTEXT_FIBER_20260811.json")
    memory = check_self_hash(BASE / "07_memory/NS-B1a2_RESEARCH_MEMORY_REVIEW_20260811.json")
    assert context["candidate_generation_allowed"] is False
    assert memory["target_context_hash"] == "sha256:" + hashlib.sha256(canonical(context)).hexdigest()
    assert "F-NS-B1a1-C001-SCALE-NEUTRAL-CHARGE" in memory["failure_query"]["relevant_failure_ids"]


def _check_trace(path: Path, expected_previous: str | None = None) -> dict:
    trace = json.loads(path.read_text())
    claimed_trace = trace.pop("trace_hash")
    assert claimed_trace.startswith("sha256:")
    assert hashlib.sha256(canonical(trace)).hexdigest() == claimed_trace.split(":", 1)[1]
    previous = expected_previous
    for event in trace["events"]:
        assert event["previous_event_hash"] == previous
        claimed = event["artifact_hash"]
        unsigned = dict(event)
        unsigned.pop("artifact_hash")
        assert hashlib.sha256(canonical(unsigned)).hexdigest() == claimed.split(":", 1)[1]
        previous = claimed
    assert trace["final_event_hash"] == previous
    return {"trace": trace, "hash": claimed_trace}


def test_ns_b1a2_trace_chronology_is_hash_chained() -> None:
    pre = _check_trace(BASE / "09_trace/NS-B1a2_PRE_CANDIDATE_TRACE_20260811.json")
    assert [e["event_type"] for e in pre["trace"]["events"]] == [
        "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW", "NEXT_STEP_PROPOSED",
    ]
    cont = _check_trace(
        BASE / "09_trace/NS-B1a2_C001_TRACE_CONTINUATION_20260811.json",
        expected_previous=pre["trace"]["final_event_hash"],
    )
    assert cont["trace"]["parent_trace_hash"] == pre["hash"]
    assert all(e["event_type"] != "PROMOTED" for e in cont["trace"]["events"])


def test_ns_b1a2_task_episode_matches_current_v3_content_identity() -> None:
    wrapper = json.loads((BASE / "10_case_study/NS-B1a2_C001_V3_TASK_EPISODE_20260811.json").read_text())
    episode = wrapper["task_episode"]
    claimed = episode["artifact_hash"]
    unsigned = dict(episode)
    unsigned.pop("artifact_hash")
    assert len(claimed) == 64
    assert hashlib.sha256(canonical(unsigned)).hexdigest() == claimed
    assert wrapper["authority"].startswith("PROPOSAL_SHADOW")
    assert episode["outcome"] == "PARTIAL_SUCCESS"


def test_ns_b1a2_cycle_metrics_have_all_seven_novelty_axes() -> None:
    metrics = json.loads((BASE / "10_case_study/NS-B1a2_C001_RAKL_CYCLE_METRICS_20260811.json").read_text())
    assert set(metrics["retained_semantic_novelty"]) == {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION",
        "RELATION", "PATH", "META_METHOD",
    }
    assert metrics["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["authority"] == "PROPOSAL_SHADOW_TELEMETRY"
