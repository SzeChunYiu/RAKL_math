import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"
PRE = BSD / "01_frontier/BSD_A1a1_R12_PRE_CANDIDATE_PACKET_20260812.json"
RESULT = BSD / "00_sources/BSD_A1a1_R12_PINFINITY_VP_BINDING_RESULT_20260812.json"
TRACE = BSD / "09_trace/BSD_A1a1_R12_PRE_CANDIDATE_TRACE_20260812.json"


def load(path):
    return json.loads(path.read_text())


def test_r12_stays_proposal_shadow_and_root_open():
    pre, result = load(PRE), load(RESULT)
    assert pre["authority"] == "PROPOSAL_SHADOW_PRE_CANDIDATE_ONLY"
    assert result["authority"] == "PROPOSAL_SHADOW_SOURCE_BOUND"
    assert result["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert result["root_promotion"] == "FORBIDDEN_NO_ROOT_CERTIFICATE"


def test_r12_closes_only_coefficient_coordinate_residual():
    result = load(RESULT)
    ep = result["task_episode_shadow"]
    assert "PINFINITY_SELMER_TO_VP_SELMER_EXACT_COORDINATE_BINDING_OPEN" in ep["residual_before"]
    assert "PINFINITY_SELMER_TO_VP_SELMER_EXACT_COORDINATE_BINDING_OPEN" not in ep["residual_after"]
    assert "SELMER_VP_DIMENSION_LOWER_BOUND_TO_EXACT_DIMENSION2_UPPER_BOUND" in ep["residual_after"]
    assert "TRANSVERSE_P_LOCALIZATION_NONZERO" in ep["residual_after"]
    assert result["exact_result"]["novelty_claim"].startswith("NO_NEW_MATHEMATICS_CLAIM")


def test_r12_semantic_shortcut_is_search_not_lift():
    pre = load(PRE)
    review = pre["obstruction_transformation_review"]
    assert review["SEARCH"]["status"] == "VIABLE_MATCH"
    assert review["selected_route"] == "SEARCH"
    assert review["LIFT"]["status"] == "BLOCKED_NOT_NEEDED"
    assert len(pre["research_memory_review"]["rejected_ids"]) >= 2


def test_r12_trace_is_hash_chained_at_gate_boundary():
    trace = load(TRACE)
    assert trace["frozen_before_candidate"] is True
    entries = trace["entries"]
    assert [e["event_type"] for e in entries] == [
        "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW", "NEXT_STEP_PROPOSED",
    ]
    for prior, current in zip(entries, entries[1:]):
        assert current["previous_event_hash"] == prior["artifact_hash"]
    result = load(RESULT)
    assert result["trace_continuation"][0]["previous_event_hash"] == trace["last_event_hash"]


def test_r12_all_seven_novelty_axes_explicit():
    novelty = load(RESULT)["saturation"]["retained_semantic_novelty"]
    assert novelty == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
