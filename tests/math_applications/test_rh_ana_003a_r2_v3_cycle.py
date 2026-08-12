from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import json
from math import comb
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


def test_rh_ana_003a_context_memory_and_cycle_hashes() -> None:
    context = _load("01_frontier/RH_ANA_003a_CONTEXT_FIBER_20260811_R2.json")
    memory = _load("07_memory/RH_ANA_003a_RESEARCH_MEMORY_REVIEW_20260811_R2.json")
    cycle = _load("07_memory/RH_ANA_003a_CYCLE_MEMORY_AND_EPISODE_20260811_R2.json")

    assert context["root_contract"]["status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert context["proposal_authority"] == "SHADOW_ONLY"
    assert context["fibre_snapshot_hash"] == _hash_without(
        context, "fibre_snapshot_hash", "hash_scope"
    )
    assert memory["context_hash"] == context["fibre_snapshot_hash"]
    assert memory["artifact_hash"] == _hash_without(memory, "artifact_hash", "hash_scope")
    assert memory["routing_effect"]["changed_action"] is True

    episode = cycle["task_episode"]
    assert episode["episode_id"] == "EP-RH-ANA-003a-MAGNITUDE-TRANSPORT-20260811-R2"
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
    assert "RAKL_METHOD_CASE_STUDY" in cycle


def test_rh_ana_003a_traces_are_hash_chained() -> None:
    pre = _load("09_trace/RH_ANA_003a_PRE_CANDIDATE_TRACE_20260811_R2.json")
    result = _load("09_trace/RH_ANA_003a_RESULT_TRACE_20260811_R2.json")

    previous = pre["parent_event_hash"]
    for event in pre["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _event_hash(event)
        previous = event["artifact_hash"]
    assert pre["final_event_hash"] == previous
    assert pre["entries"][-1]["event_type"] == "NEXT_STEP_PROPOSED"

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


def test_signed_geometric_calibration_exactly_exposes_majorant_loss() -> None:
    # Calibration only: the proof recorded in the research artifact is the binomial theorem.
    for n in range(1, 21):
        signed = sum(Fraction(comb(n, m) * ((-1) ** m), 3**m) for m in range(1, n + 1))
        absolute = sum(Fraction(comb(n, m), 3**m) for m in range(1, n + 1))
        assert signed == Fraction(2, 3) ** n - 1
        assert absolute == Fraction(4, 3) ** n - 1
        assert -1 < signed < 0
        assert absolute > 0


def test_rh_ana_003a_metrics_keep_root_open() -> None:
    metrics = _load("09_trace/RH_ANA_003a_RAKL_CYCLE_METRICS_20260811_R2.json")[
        "RAKL_CYCLE_METRICS"
    ]
    context = _load("01_frontier/RH_ANA_003a_CONTEXT_FIBER_20260811_R2.json")

    assert metrics["active_atom"] == "RH-ANA-003a"
    assert metrics["atom_fibre_snapshot_hash"] == context["fibre_snapshot_hash"]
    assert set(metrics["retained_semantic_novelty_counts"]) == SEVEN_AXES
    assert metrics["retained_semantic_novelty_counts"]["OPERATOR"] == 0
    assert metrics["retained_semantic_novelty_counts"]["META_METHOD"] == 0
    assert metrics["outcome"] == "PARTIAL_SUCCESS_ROUTE_PRUNING"
    assert metrics["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["rakl_changed_action"] is True
    assert metrics["raw_repository_growth_counted_as_learning"] is False
