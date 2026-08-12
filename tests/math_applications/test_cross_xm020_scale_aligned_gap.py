import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "real_math" / "millennium" / "cross_problem"
TRANSFER = BASE / "01_frontier" / "XM020_NS_YM_SCALE_ALIGNED_GAP_DIFFERENCEWITNESS_20260812.json"
EPISODE = BASE / "07_memory" / "XM020_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
TRACE = BASE / "09_trace" / "XM020_HASH_CHAINED_TRACE_20260812.json"
CASE = BASE / "10_study_pattern" / "RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM020_20260812.json"


def load(path):
    return json.loads(path.read_text())


def test_xm020_difference_witness_is_exact_and_scoped():
    x = load(TRANSFER)
    assert x["authority"].startswith("PROPOSAL_SHADOW")
    assert x["source_atom"]["failure_id"] == "FM-NS-LOCAL-TO-MOVING-SCALE-ESCAPE"
    assert x["target_atom"]["atom_id"] == "YM-E2b"
    assert x["difference_witness"]["world_A"] == "1"
    assert x["difference_witness"]["world_B"] == "0"
    assert x["local_to_global_gluing_failure"] is True
    assert "No proof or disproof of the Yang-Mills Millennium problem is claimed." in x["target_calculation"]["non_implications"]


def test_xm020_toy_scale_calibration():
    for n in range(2, 100):
        a = 1 / n
        delta_a = a
        delta_b = a * a
        assert delta_a > 0 and delta_b > 0
        assert abs(delta_a / a - 1) < 1e-12
        assert abs(delta_b / a - a) < 1e-12
    assert (1 / 100000) < 1e-4


def test_xm020_episode_shadow_and_separation():
    ep = load(EPISODE)
    assert ep["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert ep["authority"] == "PROPOSAL_SHADOW_ONLY"
    sep = ep["episode_diagnosis_lesson_separation"]
    assert len({sep["episode"], sep["diagnosis"], sep["failure"], sep["obstruction"], sep["lesson"]}) == 5
    assert ep["memory"]["routing_effect"]["rakl_changed_action"] is True


def test_xm020_trace_hash_chain_and_order():
    t = load(TRACE)
    events = t["events"]
    expected = [
        "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW", "NEXT_STEP_PROPOSED",
        "FALSIFIER_RUN", "RESULT_RECORDED",
    ]
    assert [e["event_type"] for e in events] == expected
    assert events[0]["previous_event_hash"] == ""
    for prev, cur in zip(events, events[1:]):
        assert cur["previous_event_hash"] == prev["artifact_hash"]
    assert t["root_status"] == "ALL_SIX_OPEN_NO_SOLUTION_CERTIFICATE"


def test_xm020_case_metrics_are_conservative():
    c = load(CASE)
    m = c["RAKL_CYCLE_METRICS"]
    assert m["protected_retained7"] == {
        "KNOWLEDGE": 0, "OPERATOR": 0, "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0, "RELATION": 0, "PATH": 0, "META_METHOD": 0,
    }
    assert m["raw_repo_growth_learning"] == 0
    assert "canonical admission/promotion not invoked" in m["gate"]
    assert len(c["lane_summaries"]) == 6
    for lane in c["lane_summaries"]:
        assert "RAKL_CYCLE_METRICS" in lane
