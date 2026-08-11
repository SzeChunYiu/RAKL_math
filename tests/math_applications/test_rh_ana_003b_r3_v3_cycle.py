from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"
SEVEN_AXES = {
    "KNOWLEDGE",
    "OPERATOR",
    "EXPERIENCE_PATTERN",
    "OBSTRUCTION",
    "RELATION",
    "PATH",
    "META_METHOD",
}
PARENT_TRACE_HASH = "sha256:a45f41ceeb2fc8d7dd607f4d4cc0637ee6b79aaeef32f6beeebd3e683bb24b20"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _hash_without(payload: dict, *keys: str) -> str:
    item = copy.deepcopy(payload)
    for key in keys:
        item.pop(key, None)
    raw = json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_rh_ana_003b_context_memory_cycle_are_shadow_and_bound() -> None:
    context = _load("01_frontier/RH_ANA_003b_CONTEXT_FIBER_20260811_R3.json")
    memory = _load("07_memory/RH_ANA_003b_RESEARCH_MEMORY_REVIEW_20260811_R3.json")
    cycle = _load("07_memory/RH_ANA_003b_CYCLE_MEMORY_AND_EPISODE_20260811_R3.json")

    assert context["root_contract"]["status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert context["proposal_authority"] == "SHADOW_ONLY"
    assert context["fibre_snapshot_hash"] == _hash_without(
        context, "fibre_snapshot_hash", "hash_scope"
    )
    assert memory["context_hash"] == context["fibre_snapshot_hash"]
    assert memory["artifact_hash"] == _hash_without(memory, "artifact_hash", "hash_scope")
    assert cycle["fibre_snapshot_hash"] == context["fibre_snapshot_hash"]
    assert cycle["artifact_hash"] == _hash_without(cycle, "artifact_hash", "hash_scope")

    episode = cycle["task_episode"]
    assert episode["episode_id"] == "EP-RH-ANA-003b-ROOT-STRENGTH-AUDIT-20260811-R3"
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["admitted"] is False
    assert cycle["problem_novelty_class"] == "UNRESOLVED"
    assert cycle["diagnosis"]["diagnosis_id"] != cycle["obstruction"]["obstruction_id"]
    assert cycle["lesson"]["lesson_id"] != cycle["obstruction"]["obstruction_id"]
    assert {x["category"] for x in cycle["typed_negative_history"]} == {
        "decomposition",
        "gluing",
    }
    assert set(cycle["saturation"]) == SEVEN_AXES
    assert cycle["verification"]["independent_review_count"] == 0
    assert "RAKL_METHOD_CASE_STUDY" in cycle


def test_rh_ana_003b_trace_continues_predecessor_and_is_hash_chained() -> None:
    trace = _load("09_trace/RH_ANA_003b_RESULT_TRACE_20260811_R3.json")
    assert trace["parent_event_hash"] == PARENT_TRACE_HASH
    previous = PARENT_TRACE_HASH
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _hash_without(event, "artifact_hash")
        previous = event["artifact_hash"]
    assert trace["final_event_hash"] == previous
    assert trace["entries"][-1]["event_type"] == "SATURATION_UPDATED"


def test_rh_ana_003b_metrics_keep_root_open_and_count_semantics_only() -> None:
    metrics = _load("09_trace/RH_ANA_003b_RAKL_CYCLE_METRICS_20260811_R3.json")[
        "RAKL_CYCLE_METRICS"
    ]
    assert metrics["active_atom"] == "RH-ANA-003b"
    assert set(metrics["retained_semantic_novelty_counts"]) == SEVEN_AXES
    assert metrics["retained_semantic_novelty_counts"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 1,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["outcome"] == "PARTIAL_SUCCESS_DECOMPOSITION_PRUNING"
    assert metrics["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["raw_repository_growth_counted_as_learning"] is False
    assert metrics["independent_mathematical_reviews"] == 0
    assert metrics["rakl_changed_action"] == (
        "CANNOT_MEASURE: predecessor memory was already materialized in the "
        "automation context before a clean pre-memory counterfactual could be captured."
    )


def test_root_strength_result_is_not_promoted_as_solution() -> None:
    cycle = _load("07_memory/RH_ANA_003b_CYCLE_MEMORY_AND_EPISODE_20260811_R3.json")
    assert cycle["task_episode"]["outcome"] == "PARTIAL_SUCCESS_DECOMPOSITION_PRUNING"
    assert cycle["problem_novelty_class"] == "UNRESOLVED"
    assert cycle["verification"]["computation"] == "none"
