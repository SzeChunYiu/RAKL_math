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


def test_context_memory_fibre_and_episode_hashes():
    ctx = _load("01_frontier/NS-B1a3b1_CONTEXT_FIBER_R2_20260811.json")
    assert ctx["packet_hash"] == "sha256:" + _canonical_hash(ctx, {"packet_hash"})

    mem = _load("07_memory/NS-B1a3b1_RESEARCH_MEMORY_REVIEW_R2_20260811.json")
    assert mem["artifact_hash"] == "sha256:" + _canonical_hash(mem, {"artifact_hash"})

    fibre = _load("09_trace/NS-B1a3b1_FIBRE_SNAPSHOT_R2_20260811.json")
    assert fibre["fibre_snapshot_hash"] == "sha256:" + _canonical_hash(fibre, {"fibre_snapshot_hash"})

    ep = _load("10_case_study/NS-B1a3b1_C001_R2_V3_TASK_EPISODE_20260811.json.shadow")
    assert ep["artifact_hash"] == _canonical_hash(ep, {"artifact_hash"})
    assert ep["outcome"] == "PARTIAL_SUCCESS"


def test_hash_chained_traces_are_contiguous():
    pre = _load("09_trace/NS-B1a3b1_PRE_CANDIDATE_TRACE_R2_20260811.json")
    prev = None
    for event in pre["events"]:
        assert event["previous_event_hash"] == prev
        expected = "sha256:" + _canonical_hash(event, {"artifact_hash"})
        assert event["artifact_hash"] == expected
        prev = event["artifact_hash"]
    assert pre["final_hash"] == prev

    post = _load("09_trace/NS-B1a3b1_RESULT_TRACE_CONTINUATION_R2_20260811.json")
    assert post["continues_from"] == pre["final_hash"]
    prev = pre["final_hash"]
    for event in post["events"]:
        assert event["previous_event_hash"] == prev
        expected = "sha256:" + _canonical_hash(event, {"artifact_hash"})
        assert event["artifact_hash"] == expected
        prev = event["artifact_hash"]
    assert post["final_hash"] == prev


def test_log_bmo_zoom_weight_is_nonexpansive_for_zoom_in():
    for r in (1.0, 0.5, 0.1, 1e-6):
        for rho in (0.49, 0.25, 0.01, 1e-8):
            assert 0 < r * rho < 0.5
            ratio = abs(math.log(rho)) / abs(math.log(r * rho))
            assert ratio <= 1.0 + 1e-15


def test_metrics_do_not_promote_root_and_count_all_axes():
    metrics = _load("10_case_study/NS-B1a3b1_C001_R2_RAKL_CYCLE_METRICS_20260811.json")
    novelty = metrics["saturation_retained_semantic_novelty"]
    assert set(novelty) == {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION",
        "RELATION", "PATH", "META_METHOD"
    }
    assert metrics["outcome"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["root_promotion_gate"] == "BLOCKED"
    assert metrics["raw_repository_growth_counted_as_learning"] is False
