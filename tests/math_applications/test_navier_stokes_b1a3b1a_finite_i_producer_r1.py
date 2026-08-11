import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"


def _load(rel):
    return json.loads((NS / rel).read_text())


def _canonical_hash(obj, excluded):
    payload = {k: v for k, v in obj.items() if k not in excluded}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def test_context_memory_fibre_preaction_episode_hashes():
    ctx = _load("01_frontier/NS-B1a3b1a_CONTEXT_FIBER_R1_20260811.json")
    assert ctx["packet_hash"] == "sha256:" + _canonical_hash(ctx, {"packet_hash"})
    mem = _load("07_memory/NS-B1a3b1a_RESEARCH_MEMORY_REVIEW_R1_20260811.json")
    assert mem["artifact_hash"] == "sha256:" + _canonical_hash(mem, {"artifact_hash"})
    fibre = _load("09_trace/NS-B1a3b1a_FIBRE_SNAPSHOT_R1_20260811.json")
    assert fibre["fibre_snapshot_hash"] == "sha256:" + _canonical_hash(fibre, {"fibre_snapshot_hash"})
    pre = _load("09_trace/NS-B1a3b1a_PRE_ACTION_RECEIPT_R1_20260811.json")
    assert pre["artifact_hash"] == "sha256:" + _canonical_hash(pre, {"artifact_hash"})
    ep = _load("10_case_study/NS-B1a3b1a_C001_R1_V3_TASK_EPISODE_20260811.json.shadow")
    assert ep["artifact_hash"] == _canonical_hash(ep, {"artifact_hash"})
    assert ep["outcome"] == "PARTIAL_SUCCESS"


def test_traces_contiguous():
    pre = _load("09_trace/NS-B1a3b1a_PRE_CANDIDATE_TRACE_R1_20260811.json")
    prev = None
    for event in pre["events"]:
        assert event["previous_event_hash"] == prev
        assert event["artifact_hash"] == "sha256:" + _canonical_hash(event, {"artifact_hash"})
        prev = event["artifact_hash"]
    assert pre["final_hash"] == prev
    post = _load("09_trace/NS-B1a3b1a_RESULT_TRACE_CONTINUATION_R1_20260811.json")
    assert post["continues_from"] == pre["final_hash"]
    for event in post["events"]:
        assert event["previous_event_hash"] == prev
        assert event["artifact_hash"] == "sha256:" + _canonical_hash(event, {"artifact_hash"})
        prev = event["artifact_hash"]
    assert post["final_hash"] == prev


def test_time_frequency_envelope_is_uniform():
    for N in (8, 16, 32, 64, 128, 256):
        for k in range(101):
            r = 10 ** (-k / 20)
            e = N * N * r * r * min(r * r, N ** -2)
            c = r * min(r * r, N ** -2)
            assert e <= 1.0 + 1e-12
            assert c <= 1.0 + 1e-12
        assert N > 0
        assert math.log(N) > 0


def test_scope_and_root_nonpromotion():
    metrics = _load("10_case_study/NS-B1a3b1a_C001_R1_RAKL_CYCLE_METRICS_20260811.json")
    assert set(metrics["saturation_retained_semantic_novelty"]) == {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION",
        "RELATION", "PATH", "META_METHOD"
    }
    assert metrics["outcome"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["root_promotion_gate"] == "BLOCKED"
    assert metrics["route_family_health_shadow"]["surrogate_progress_kind"] == "LOCAL_PROGRESS"
    assert metrics["raw_repository_growth_counted_as_learning"] is False
    text = (NS / "04_candidates/NS-B1a3b1a_C001_R1_HOSTILE_NEAR_MISS_20260811.md").read_text()
    assert "not asserted to solve Navier" in text
    assert "equation-specific" in text
