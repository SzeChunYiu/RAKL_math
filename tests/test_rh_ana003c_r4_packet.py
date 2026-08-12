import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"


def _load(rel):
    return json.loads((BASE / rel).read_text(encoding="utf-8"))


def _semantic_hash(obj):
    excluded = {"artifact_hash", "packet_hash", "fibre_snapshot_hash", "self_hash"}

    def strip(value):
        if isinstance(value, dict):
            return {k: strip(v) for k, v in sorted(value.items()) if k not in excluded}
        if isinstance(value, list):
            return [strip(v) for v in value]
        return value

    payload = json.dumps(strip(obj), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def test_rh_ana003c_r4_pre_candidate_chronology_and_hashes():
    fibre = _load("01_frontier/RH_ANA_003c_CONTEXT_FIBER_20260812_R4.json")
    memory = _load("07_memory/RH_ANA_003c_RESEARCH_MEMORY_REVIEW_20260812_R4.json")
    expert = _load("08_reviews/RH_ANA_003c_EXPERT_CELL_PRE_CANDIDATE_20260812_R4.json")
    trace = _load("09_trace/RH_ANA_003c_PRE_CANDIDATE_TRACE_20260812_R4.json")
    candidate = _load("04_candidates/RH_ANA_003c_INDEPENDENT_WINDOW_REORDERABILITY_CANDIDATE_20260812_R4.json")

    assert _semantic_hash(fibre) == fibre["fibre_snapshot_hash"]
    assert _semantic_hash(memory) == memory["artifact_hash"]
    assert _semantic_hash(expert) == expert["artifact_hash"]

    expected_types = [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert [event["event_type"] for event in trace["events"]] == expected_types

    previous = None
    for event in trace["events"]:
        assert event["previous_event_hash"] == previous
        assert _semantic_hash(event) == event["artifact_hash"]
        previous = event["artifact_hash"]
    assert trace["terminal_event_hash"] == previous
    assert _semantic_hash(trace) == trace["artifact_hash"]

    assert candidate["frozen_after_pre_candidate_trace_hash"] == trace["terminal_event_hash"]
    assert _semantic_hash(candidate) == candidate["artifact_hash"]
    assert candidate["authority"] == "PROPOSAL_ONLY"
    assert expert["independent_review_credit"] == 0


def test_rh_ana003c_r4_current_work_and_authority_guards():
    fibre = _load("01_frontier/RH_ANA_003c_CONTEXT_FIBER_20260812_R4.json")
    memory = _load("07_memory/RH_ANA_003c_RESEARCH_MEMORY_REVIEW_20260812_R4.json")
    result = (BASE / "04_candidates/negative_history/RH_ANA_003c_CUTOFF_GLUE_FALSIFIER_20260812_R4.md").read_text(encoding="utf-8")

    assert fibre["root_contract"]["status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert fibre["proposal_authority"] == "SHADOW_ONLY"
    assert 118 in memory["current_work_coverage"]["queried_open_rh_prs"]
    assert 147 in memory["current_work_coverage"]["queried_open_rh_prs"]
    assert memory["counterfactual_action_effect"]["changed"] is True
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in result
    assert "independent mathematical review credit `0`" in result
    assert "does **not** converge absolutely" in result
