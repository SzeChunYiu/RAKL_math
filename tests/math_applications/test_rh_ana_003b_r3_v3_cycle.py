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


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _hash_without(payload: dict, *keys: str) -> str:
    item = copy.deepcopy(payload)
    for key in keys:
        item.pop(key, None)
    raw = json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _event_hash(event: dict) -> str:
    return _hash_without(event, "artifact_hash")


def test_rh_ana_003b_context_memory_cycle_and_authority() -> None:
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
    assert memory["routing_effect"]["changed_action"] is True
    assert len(memory["retrieved"]["query_misses"]) == 2

    episode = cycle["task_episode"]
    assert episode["episode_id"] == "EP-RH-ANA-003b-ROOT-COUPLING-20260811-R3"
    assert episode["shadow"] is True
    assert episode["admitted"] is False
    assert cycle["diagnosis"]["diagnosis_id"] != cycle["obstruction"]["obstruction_id"]
    assert cycle["lesson"]["lesson_id"] != cycle["obstruction"]["obstruction_id"]
    assert {item["category"] for item in cycle["typed_negative_history"]} == {
        "representation",
        "gluing",
    }
    assert set(cycle["saturation"]) == SEVEN_AXES
    assert cycle["artifact_hash"] == _hash_without(cycle, "artifact_hash", "hash_scope")
    assert cycle["RAKL_METHOD_CASE_STUDY"]["novelty_class"]["class"] == "compositional"


def test_rh_ana_003b_traces_are_hash_chained_and_post_fibre() -> None:
    pre = _load("09_trace/RH_ANA_003b_PRE_CANDIDATE_TRACE_20260811_R3.json")
    result = _load("09_trace/RH_ANA_003b_RESULT_TRACE_20260811_R3.json")

    previous = pre["parent_event_hash"]
    for event in pre["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _event_hash(event)
        previous = event["artifact_hash"]
    assert pre["final_event_hash"] == previous
    assert pre["entries"][-1]["event_type"] == "PRE_CANDIDATE_GATE_FROZEN"

    assert result["parent_event_hash"] == pre["final_event_hash"]
    previous = result["parent_event_hash"]
    for event in result["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _event_hash(event)
        previous = event["artifact_hash"]
    assert result["final_event_hash"] == previous
    assert [event["event_type"] for event in result["entries"]] == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]


def test_rh_ana_003b_route_pruning_and_successor_are_scoped() -> None:
    parent = (BASE / "02_problem_dag/RH_ANA_003b.yaml").read_text(encoding="utf-8")
    child = (BASE / "02_problem_dag/RH_ANA_003c.yaml").read_text(encoding="utf-8")
    result = (BASE / "01_frontier/RH_ANA_003b_ROOT_COUPLING_FALSIFIER_20260811_R3.md").read_text(encoding="utf-8")

    assert "status: PARTIAL_SUCCESS_ROUTE_PRUNING" in parent
    assert "successor_atom: RH-ANA-003c" in parent
    assert "status: CONTEXT_REQUIRED" in child
    assert "root_authority: NONE" in child
    assert "\\Longleftrightarrow" in result
    assert "root authority none" in result
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in result


def test_rh_ana_003b_metrics_keep_measurement_and_root_authority_separate() -> None:
    metrics = _load("09_trace/RH_ANA_003b_RAKL_CYCLE_METRICS_20260811_R3.json")[
        "RAKL_CYCLE_METRICS"
    ]
    context = _load("01_frontier/RH_ANA_003b_CONTEXT_FIBER_20260811_R3.json")

    assert metrics["active_atom"] == "RH-ANA-003b"
    assert metrics["atom_fibre_snapshot_hash"] == context["fibre_snapshot_hash"]
    assert set(metrics["retained_semantic_novelty_counts"]) == SEVEN_AXES
    assert metrics["retained_semantic_novelty_counts"]["OPERATOR"] == 0
    assert metrics["retained_semantic_novelty_counts"]["META_METHOD"] == 0
    assert metrics["outcome"] == "PARTIAL_SUCCESS_ROUTE_PRUNING"
    assert metrics["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_status"]["independent_mathematical_reviews"] == 0
    assert metrics["rakl_changed_action"] is True
    assert metrics["raw_repository_growth_counted_as_learning"] is False
    assert metrics["authority"] == "MEASUREMENT_ONLY_PROPOSAL_SHADOW"
