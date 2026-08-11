from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"

CONTEXT = NS / "01_frontier/NS-B1a4_CONTEXT_FIBER_20260812.json"
MEMORY = NS / "07_memory/NS-B1a4_RESEARCH_MEMORY_REVIEW_20260812.json"
DIAGNOSIS = NS / "07_memory/NS-B1a4_C001_FAILURE_DIAGNOSIS_20260812.json"
FAILURE = NS / "07_memory/NS-B1a4_C001_FAILURE_EXPERIENCE_DELTA_20260812.json"
LESSON = NS / "07_memory/NS-B1a4_C001_OBSTRUCTION_LESSON_20260812.json"
PRE_TRACE = NS / "09_trace/NS-B1a4_C001_PRE_VERIFICATION_TRACE_20260812.json"
POST_TRACE = NS / "09_trace/NS-B1a4_C001_TRACE_CONTINUATION_20260812.json"
EPISODE = NS / "09_trace/NS-B1a4_C001_TASK_EPISODE_20260812.json"
RESULT = NS / "01_frontier/NS-B1a4_C001_SIGNED_FLUX_NO_RECROSSING_AUDIT_20260812.md"
METRICS = NS / "10_case_study/NS-B1a4_C001_RAKL_CYCLE_METRICS_20260812.json"
DAG = NS / "02_problem_dag/NS_B1a4_C001_DELTA_20260812.yaml"


def _load(path: Path):
    return json.loads(path.read_text())


def _event_hash(event: dict) -> str:
    payload = dict(event)
    payload.pop("artifact_hash")
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _trace_hash(trace: dict) -> str:
    payload = dict(trace)
    payload.pop("artifact_hash")
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_ns_b1a4_exact_pressure_free_shear_calibration():
    # Analytic proof lives in the research artifact. This is only a deterministic
    # calibration/regression check; computation is not theorem authority.
    eps = 0.73
    k = 1.17
    x2 = -0.31
    t = 0.19
    f = eps * math.exp(k * x2 + k * k * t)

    partial_t = k * k * f
    laplacian = k * k * f
    divergence = 0.0  # f is x1-independent.
    convection = 0.0  # u=(f,0,0), so u.grad u=f*partial_1 u=0.

    assert divergence == 0.0
    assert convection == 0.0
    assert partial_t == laplacian

    # For every fixed ball, the spatial integral is a positive t-independent
    # constant times exp(2*k^2*t), so the derivative is positive.
    energy = math.exp(2.0 * k * k * t)
    energy_derivative = 2.0 * k * k * energy
    assert energy > 0.0
    assert energy_derivative > 0.0


def test_ns_b1a4_hash_chained_trace_and_episode_scope():
    pre = _load(PRE_TRACE)
    prev = None
    for event in pre["events"]:
        assert event["previous_event_hash"] == prev
        assert event["artifact_hash"] == _event_hash(event)
        prev = event["artifact_hash"]
    assert pre["terminal_event_hash"] == prev
    assert pre["artifact_hash"] == _trace_hash(pre)

    post = _load(POST_TRACE)
    assert post["previous_trace_terminal_hash"] == pre["terminal_event_hash"]
    prev = pre["terminal_event_hash"]
    for event in post["events"]:
        assert event["previous_event_hash"] == prev
        assert event["artifact_hash"] == _event_hash(event)
        prev = event["artifact_hash"]
    assert post["terminal_event_hash"] == prev
    assert post["artifact_hash"] == _trace_hash(post)

    episode = _load(EPISODE)
    assert episode["authority"] == "PROPOSAL_SHADOW_EPISODE_ONLY"
    assert episode["outcome"] == "PARTIAL_SUCCESS_ROUTE_PRUNING"
    assert "no strict RAKL candidate-generation credit" in episode["candidate_chronology"]


def test_ns_b1a4_local_failure_is_not_global_gluing_or_root_promotion():
    diagnosis = _load(DIAGNOSIS)
    failure = _load(FAILURE)
    lesson = _load(LESSON)
    result = RESULT.read_text()
    dag = DAG.read_text()

    assert diagnosis["local_math_failure"] is True
    assert diagnosis["local_to_global_gluing_failure"] is False
    assert failure["local_to_global_gluing"] == "NO_NEW_GLUING_FAILURE"
    assert failure["failure_records"][0]["not_a_global_blacklist"] is True
    assert lesson["reusable_obstruction"]["authority"] == "PROPOSAL_ONLY_REUSABLE_OBSTRUCTION"
    assert "not globally finite-energy" in result
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in result
    assert "root_status: OPEN_NO_SOLUTION_CERTIFICATE" in dag


def test_ns_b1a4_memory_and_metrology_are_conservative():
    context = _load(CONTEXT)
    memory = _load(MEMORY)
    metrics = _load(METRICS)

    assert context["packet_hash"].startswith("sha256:")
    assert memory["retrieval_counts"]["failure_ids_selected"] == 3
    assert memory["retrieval_counts"]["failure_ids_rejected"] == 3
    assert memory["retrieval_counts"]["success_tools_consulted"] == 0
    assert "CANNOT_MEASURE" in memory["missed_relevant_experience"]

    novelty = metrics["retained_semantic_novelty_counts"]
    assert set(novelty) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert novelty["OBSTRUCTION"] == 1
    assert novelty["RELATION"] == 1
    assert sum(novelty.values()) == 2
    assert metrics["root_gate"]["status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["candidate_generation_credit"] == 0
