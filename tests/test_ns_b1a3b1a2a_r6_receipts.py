import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def load_json(rel):
    return json.loads((NS / rel).read_text())


def test_r6_pre_candidate_freeze_and_root_fail_closed():
    p = load_json("03_context/NS-B1a3b1a2a_R6_PRE_CANDIDATE_PACKET_20260812.json")
    assert p["authority"] == "PROPOSAL_SHADOW_PRE_CANDIDATE"
    assert p["framework_source_of_truth"]["main_sha_read_before_math"] == "8274f51b3c56145b4300435cea0d401c47313756"
    assert p["framework_source_of_truth"]["method_version"] == "3.0.0"
    assert p["rakl_math_base"] == "3871283cfe5040801b174e25b045e05ee0228cc2"
    assert p["root_contract"]["status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert p["root_contract"]["independent_review_credit"] == "0/3"
    assert p["obstruction_transformation_review"]["selected_route"] == "SEARCH"
    assert p["candidate_generation_allowed"] is True
    trace = p["research_trace"]
    assert [e["event"] for e in trace] == [
        "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW", "NEXT_STEP_PROPOSED",
    ]
    for left, right in zip(trace, trace[1:]):
        assert right["previous_event_hash"] == left["artifact_hash"]


def test_r6_episode_diagnosis_obstruction_lesson_are_distinct():
    ep = load_json("07_memory/NS-B1a3b1a2a_R6_TASK_EPISODE_SHADOW_20260812.json")
    ex = load_json("07_memory/NS-B1a3b1a2a_R6_EXPERIENCE_DELTA_20260812.json")
    assert ep["episode_id"] == "E-NS-B1a3b1a2a-R6-20260812"
    ids = {
        ep["episode_id"],
        ex["diagnosis"]["id"],
        ex["failure"]["id"],
        ex["obstruction"]["id"],
        ex["lesson"]["id"],
        ex["motif"]["id"],
        ex["new_tool"]["id"],
    }
    assert len(ids) == 7
    assert ep["outcome"] == "ANCIENT_LOCAL_SMOOTHING_BOUND__GLOBAL_LORENTZ_GLUE_OPEN_QUANTIFIED_LINEAR_CAPACITY"
    assert ep["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_r6_mathematical_scope_and_scaling_receipt():
    text = (NS / "04_candidates/NS-B1a3b1a2a_R6_ANCIENT_SMOOTHING_LINEAR_PACKET_CAPACITY_20260812.md").read_text()
    assert "M^(k+2l+1)" in text
    assert "||omega||_infinity <= C M^2" in text
    assert "||partial_t omega||_infinity <= C M^4" in text
    assert "C I M^4 R lambda^(-3)" in text
    assert "Hard DifferenceWitness" in text
    assert "not asserted to solve Navier–Stokes" in text
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in text


def test_r6_trace_continuation_is_hash_chained_to_pre_candidate_tip():
    p = load_json("03_context/NS-B1a3b1a2a_R6_PRE_CANDIDATE_PACKET_20260812.json")
    lines = (NS / "09_trace/NS-B1a3b1a2a_R6_TRACE_CONTINUATION_20260812.jsonl").read_text().splitlines()
    trace = [json.loads(line) for line in lines if line.strip()]
    assert trace[0]["previous_event_hash"] == p["research_trace"][-1]["artifact_hash"]
    for left, right in zip(trace, trace[1:]):
        assert right["previous_event_hash"] == left["artifact_hash"]
    assert trace[-1]["event"] == "SATURATION_UPDATED"


def test_r6_framework_drift_is_fail_closed_not_backfilled():
    f = load_json("07_memory/NS-B1a3b1a2a_R6_PROCESS_DRIFT_FAILURE_20260812.json")
    c = load_json("10_case_study/NS-B1a3b1a2a_R6_RAKL_METHOD_CASE_STUDY_20260812.json")
    assert f["id"] == "F-NS-B1a3b1a2a-R6-PROCESS-MIDRUN-FRAMEWORK-SUBJECT-GATE-DRIFT"
    assert f["observation"]["framework_sha_read_before_mathematics"] != f["observation"]["framework_sha_observed_at_closeout"]
    assert "No strict latest-current-main" in f["authority_effect"]
    assert c["midrun_framework_drift"]["protected_surface_changed"] is True
    assert c["saturation_axes"]["raw_repository_growth_counted_as_learning"] is False
