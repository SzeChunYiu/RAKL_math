import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "real_math" / "millennium" / "cross_problem"
TRANSFER = BASE / "01_frontier" / "XM019_PNP_RH_NEGLIGIBLE_COMPLEMENT_DIFFERENCEWITNESS_20260812.json"
EPISODE = BASE / "07_memory" / "XM019_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
TRACE = BASE / "09_trace" / "XM019_HASH_CHAINED_TRACE_20260812.json"
CASE = BASE / "10_study_pattern" / "RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM019_20260812.json"


def load(path):
    return json.loads(path.read_text())


def test_xm019_transfer_scope_and_difference_witness():
    x = load(TRANSFER)
    assert x["authority"].startswith("PROPOSAL_SHADOW")
    assert x["source_atom"]["lane"] == "P_vs_NP"
    assert x["target_atom"]["atom_id"] == "RH-ANA-003e"
    assert x["difference_witness"]["status"].startswith("NO_DIFFERENCE_WITNESS")
    assert x["outcome"].startswith("PARTIAL_SUCCESS")
    assert "No proof or disproof of RH is claimed." in x["target_calculation"]["non_implications"]


def test_xm019_elementary_growth_congruence_calibration():
    # Finite calibration only; proof authority is the triangle-inequality argument in the transfer artifact.
    for A in (0, 1, 2, 5):
        for n in range(1, 50):
            p = n ** A
            t = 1 / (n + 1)
            s = p + t
            assert abs(s) <= 2 * (n ** A)
            assert abs(p) <= abs(s) + 1


def test_xm019_episode_is_shadow_only():
    ep = load(EPISODE)
    assert ep["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert ep["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert ep["episode_diagnosis_lesson_separation"]["authority"].startswith("ALL_PROPOSAL_SHADOW")


def test_xm019_trace_hash_chain_and_order():
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


def test_xm019_metrics_are_conservative():
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
