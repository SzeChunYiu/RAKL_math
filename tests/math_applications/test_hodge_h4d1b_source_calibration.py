from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _sha256_object(payload: dict) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def test_h4d1b_context_is_hash_bound_and_source_scoped() -> None:
    context = _load("01_frontier/H4d1b_CONTEXT_FIBER_20260811.json")
    assert context["atom_id"] == "H4d1b"
    assert context["first_candidate_at"] is None
    expected = context["packet_hash"]
    unhashed = dict(context)
    unhashed["packet_hash"] = ""
    assert _sha256_object(unhashed) == expected
    assert "https://arxiv.org/abs/2104.14845" in context["source_anchors"]
    joined = " ".join(context["explicit_disanalogies"]).lower()
    assert "arbitrary rational cycle" in joined
    assert "semiregular" in joined
    assert "higher" in joined


def test_h4d1b_memory_retrieves_parent_failures_without_minting_tool() -> None:
    review = _load("07_memory/H4d1b_RESEARCH_MEMORY_REVIEW_20260811.json")
    assert review["tool_query_status"] == "NO_RELEVANT_MATCH"
    assert review["selected_tool_ids"] == []
    assert set(review["relevant_failure_ids"]) == {
        "F-H4D1A-SAME-DETECTOR-BRANCH-NOGO",
        "F-H4D1-DETECTOR-KERNEL-GAP",
    }
    expected = review["artifact_hash"]
    unhashed = dict(review)
    unhashed["artifact_hash"] = ""
    assert _sha256_object(unhashed) == expected


def test_h4d1b_precalibration_trace_is_hash_chained_and_candidate_free() -> None:
    trace = _load("09_trace/H4d1b_PRE_SOURCE_CALIBRATION_TRACE_20260811.json")
    entries = trace["entries"]
    assert [entry["event_type"] for entry in entries] == [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert all(entry["event_type"] != "CANDIDATE_PROPOSED" for entry in entries)
    previous = ""
    for entry in entries:
        assert entry["previous_event_hash"] == previous
        expected = entry["artifact_hash"]
        unhashed = dict(entry)
        unhashed["artifact_hash"] = ""
        assert _sha256_object(unhashed) == expected
        previous = expected


def test_h4d1b_result_continues_exact_trace_and_preserves_boundaries() -> None:
    pre = _load("09_trace/H4d1b_PRE_SOURCE_CALIBRATION_TRACE_20260811.json")
    continuation = _load("09_trace/H4d1b_SOURCE_CALIBRATION_TRACE_CONTINUATION_20260811.json")
    assert continuation["entries"][0]["previous_event_hash"] == pre["entries"][-1]["artifact_hash"]
    assert [entry["event_type"] for entry in continuation["entries"]] == [
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]
    route = (BASE / "03_routes/H4d1b_KLOOSTERMAN_TANGENT_LIFT_CALIBRATION_20260811.md").read_text(encoding="utf-8")
    assert "KLOOSTERMAN_SOURCE_FIRST_ORDER_DIRECT_LIFT = PASS" in route
    assert "does **not** show that direct branch annihilation is weaker than full semiregularity" in route
    assert "not a proof of the rational Hodge conjecture" in route
    assert "H4d1c" in route and "H4d1b-HO" in route


def test_h4d1b_metrics_quantify_all_seven_axes_and_fail_closed() -> None:
    metrics = _load("10_case_study/H4d1b_RAKL_CYCLE_METRICS_20260811.json")
    assert metrics["framework"]["current_main_sha"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert metrics["framework"]["application_framework_pin_sha"] == metrics["framework"]["current_main_sha"]
    assert metrics["outcome"]["category"] == "SOURCE_BOUND_METHOD_CALIBRATION"
    assert metrics["outcome"]["new_mathematics_claim"] is False
    assert metrics["gates"]["independent_review"] is False
    assert metrics["gates"]["root_authority"] == "NONE"
    assert metrics["rakl_action_attribution"]["causal_claim"] == "CANNOT_MEASURE"
    assert set(metrics["retained_semantic_novelty"]) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
