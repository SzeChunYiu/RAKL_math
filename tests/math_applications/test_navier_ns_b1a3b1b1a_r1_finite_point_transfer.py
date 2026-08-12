import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"


def _canonical_hash(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def test_context_root_and_frozen_transfer_contract():
    data = json.loads((BASE / "01_frontier/NS-B1a3b1b1a_CONTEXT_FIBER_R1_20260812.json").read_text())
    assert data["atom_id"] == "NS-B1a3b1b1a"
    assert data["control_issue"] == "RAKL_math#180"
    assert data["root_contract"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert data["root_contract"]["root_authority"] == "NONE"
    assert "lambda^{-1/2}" in data["problem_signature"]["target"]
    assert data["authority"] == "PROPOSAL_SHADOW_ONLY"


def test_pre_candidate_trace_hash_chain_and_required_order():
    trace = json.loads((BASE / "09_trace/NS-B1a3b1b1a_PRE_CANDIDATE_TRACE_R1_20260812.json").read_text())
    required = [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert [e["event_type"] for e in trace["events"]] == required
    prev = None
    for event in trace["events"]:
        stored = event["artifact_hash"]
        body = dict(event)
        del body["artifact_hash"]
        assert stored == "sha256:" + _canonical_hash(body)
        assert event["previous_event_hash"] == prev
        prev = stored
    assert trace["terminal_pre_action_hash"] == prev


def test_result_trace_continues_frozen_pre_action_chain():
    pre = json.loads((BASE / "09_trace/NS-B1a3b1b1a_PRE_CANDIDATE_TRACE_R1_20260812.json").read_text())
    lines = [json.loads(x) for x in (BASE / "09_trace/NS-B1a3b1b1a_RESULT_TRACE_CONTINUATION_R1_20260812.jsonl").read_text().splitlines() if x.strip()]
    assert lines[0]["previous_event_hash"] == pre["terminal_pre_action_hash"]
    prev = pre["terminal_pre_action_hash"]
    for event in lines:
        stored = event["artifact_hash"]
        body = dict(event)
        del body["artifact_hash"]
        assert stored == "sha256:" + _canonical_hash(body)
        assert event["previous_event_hash"] == prev
        prev = stored
    assert lines[-1]["event_type"] == "NEXT_STEP_PROPOSED"


def test_episode_is_content_bound_shadow_only():
    path = BASE / "07_memory/NS-B1a3b1b1a_TASK_EPISODE_R1_20260812.json"
    episode = json.loads(path.read_text())
    stored = episode["artifact_hash"]
    body = dict(episode)
    del body["artifact_hash"]
    assert stored == _canonical_hash(body)
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert episode["outcome"] == "PARTIAL_SUCCESS_SCOPED_TRANSFER_ROUTE_PRUNING"
    assert episode["independent_review_credit"] == "0/3"


def test_local_failure_is_separate_from_gluing_residuals():
    result = (BASE / "04_candidates/NS-B1a3b1b1a_C001_R1_FINITE_POINT_TRANSFER_RESULT_20260812.md").read_text()
    assert "F-NS-B1a3b1b1a-CARDINALITY-NOT-CRITICAL-RADIUS" in result
    assert "G-NS-B1a3b1b1a-TERMINAL-TO-PRETERMINAL-MORPHOLOGY" in result
    assert "G-NS-B1a3b1b1a-FAR-FIELD-GLOBAL-SUPERLEVEL-COVER" in result
    assert "G-NS-B1a3b1b1a-VELOCITY-TO-VORTICITY-CONSUMER-STATE" in result
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in result
    assert "Type II remains untouched" in result


def test_memory_records_selected_rejected_and_action_change():
    memory = json.loads((BASE / "07_memory/NS-B1a3b1b1a_RESEARCH_MEMORY_REVIEW_R1_20260812.json").read_text())
    assert memory["success_memory"]["selected_ids"]
    assert memory["success_memory"]["rejected_ids"]
    assert memory["failure_memory"]["selected_ids"]
    assert memory["failure_memory"]["rejected_ids"]
    assert memory["pre_memory_preference"] != memory["post_memory_preference"]
    assert memory["cross_millennium_query"]["queried"] is False


def test_problem_dag_does_not_promote_root():
    text = (BASE / "02_problem_dag/NS_B1a3b1b1a_C001_R1_DELTA_20260812.yaml").read_text()
    assert "status: OPEN_NO_SOLUTION_CERTIFICATE" in text
    assert "authority: NONE" in text
    assert "direct_Barker_terminal_point_count_to_Grujic_critical_finite_center_morphology" in text
    assert "Type_II_untouched" in text
