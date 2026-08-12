import json
from pathlib import Path

BASE = Path("research/real_math/millennium/navier_stokes")


def test_ns_b1a3a_task_episode_and_metrics_are_proposal_shadow():
    episode = json.loads((BASE / "07_memory/NS-B1a3a_TASK_EPISODE_20260812.json").read_text())
    telemetry = json.loads((BASE / "09_trace/NS-B1a3a_RAKL_V3_CASE_STUDY_AND_CYCLE_METRICS_20260812.json").read_text())
    metrics = telemetry["RAKL_CYCLE_METRICS"]

    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert metrics["gate_status"]["root_authority"] == "NONE"
    assert metrics["gate_status"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["retained_semantic_novelty_counts"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 1,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }


def test_ns_b1a3a_core_tail_residual_is_not_promoted_to_global_l3():
    diagnosis = json.loads((BASE / "07_memory/NS-B1a3a_C001_DIAGNOSIS_20260812.json").read_text())
    assert diagnosis["failure_category"] == "LOCAL_TO_GLOBAL_GLUING"
    assert diagnosis["local_mathematics_status"] == "VERIFIED_SAME_CONTEXT"
    assert diagnosis["gluing_status"] == "OPEN"


def test_ns_b1a3a_trace_chain_is_linked_to_parent():
    trace = json.loads((BASE / "09_trace/NS-B1a3a_RESULT_TRACE_CONTINUATION_20260812.json").read_text())
    assert trace["continues_from"] == "sha256:84a49c402f6329723828bf848452f336b300cb82fa4c35f9618be60edf5001b6"
    events = trace["events"]
    assert events[1]["prev_event_hash"] == events[0]["event_hash"]
    assert events[2]["prev_event_hash"] == events[1]["event_hash"]
    assert trace["final_event_hash"] == events[-1]["event_hash"]
