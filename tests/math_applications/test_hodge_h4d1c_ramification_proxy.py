from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"


def _load(rel: str):
    return json.loads((BASE / rel).read_text())


def test_c006_ramification_countermodel_and_authority():
    # pi(t)=t^2: derivative at the selected point is zero although the
    # affine ring map Q[u]->Q[t], u|->t^2, has zero kernel.
    assert 2 * 0 == 0
    assert {2 * n for n in range(-3, 4)} != set(range(-3, 4))  # no finite-set surjectivity proxy is used as proof

    episode = _load("07_memory/H4d1c_C006_TASK_EPISODE_SHADOW_20260812.jsonl")
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert "O-H4D1C-GENERIC-NONVERTICALITY-OR-DIRECT-IMAGE-DIMENSION" in episode["residual_signature"]


def test_c006_episode_diagnosis_failure_obstruction_lesson_are_distinct():
    diagnosis = _load("07_memory/H4d1c_C006_DIAGNOSIS_20260812.json")
    failure = _load("07_memory/H4d1c_C006_FAILURE_20260812.json")
    obstruction = _load("07_memory/H4d1c_C006_OBSTRUCTION_20260812.json")
    lesson = _load("07_memory/H4d1c_C006_CANDIDATE_LESSON_20260812.json")
    assert diagnosis["failure_id"] == failure["failure_id"]
    assert obstruction["obstruction_id"] != failure["failure_id"]
    assert lesson["lesson_id"] != obstruction["obstruction_id"]
    assert diagnosis["local_to_global_gluing_failure"] is False
    assert lesson["authority"] == "CANDIDATE"


def test_c006_preaction_gate_order_and_final_trace_chain():
    trace = _load("09_trace/H4d1c_C006_HASH_CHAIN_TRACE_20260812.json")
    expected = [
        "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW", "NEXT_STEP_PROPOSED",
        "CANDIDATE_PROPOSED", "FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED",
    ]
    assert [event["event"] for event in trace["events"]] == expected
    for previous, current in zip(trace["events"], trace["events"][1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    assert trace["terminal_event_hash"] == trace["events"][-1]["artifact_hash"]


def test_c006_shortcut_is_same_domain_search_only():
    review = _load("07_memory/H4d1c_C006_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json")
    assert review["selected_mode"] == "SEARCH"
    assert review["direct_search_status"] == "MATCHES_FOUND"
    assert review["jump_search_status"] == "NOT_RUN"
    assert review["glue_search_status"] == "NOT_RUN"
    assert review["selected_episode_ids"] == ["OT-HODGE-C004-CONSUMER-PROJECTION-ALIGNMENT"]
