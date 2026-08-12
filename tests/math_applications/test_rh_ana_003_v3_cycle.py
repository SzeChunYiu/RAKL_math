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


def _event_hash(event: dict) -> str:
    payload = copy.deepcopy(event)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_rh_ana_003_cycle_is_shadow_only_and_hash_chained() -> None:
    context = _load("01_frontier/RH_ANA_003_CONTEXT_FIBER_20260811.json")
    memory = _load("07_memory/RH_ANA_003_CYCLE_MEMORY_AND_EPISODE_20260811.json")
    trace = _load("09_trace/RH_ANA_003_OPEN_TRACE_20260811.json")
    metrics = _load("09_trace/RH_ANA_003_RAKL_CYCLE_METRICS_20260811.json")

    assert context["atom_id"] == "RH-ANA-003"
    assert context["root_contract"]["status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert context["active_atom"]["candidate_generation"].startswith("BLOCKED")
    assert context["proposal_authority"] == "SHADOW_ONLY"

    episode = memory["task_episode"]
    assert episode["episode_id"] == "EP-RH-ANA-003-TRIANGULAR-UNIFORMITY-20260811"
    assert episode["shadow"] is True
    assert episode["admitted"] is False
    assert episode["admission_status"] == "PROPOSAL_SHADOW_ONLY"
    assert memory["diagnosis"]["diagnosis_id"] != memory["obstruction"]["obstruction_id"]
    assert memory["lesson"]["lesson_id"] != memory["obstruction"]["obstruction_id"]
    assert {item["category"] for item in memory["typed_negative_history"]} == {"math", "gluing"}
    assert set(memory["saturation"]) == SEVEN_AXES
    assert "RAKL_METHOD_CASE_STUDY" in memory

    assert trace["parent_event_id"] == "RH-ANA-002-E09"
    previous = trace["parent_event_hash"]
    assert previous == "sha256:001578dc895c23ec2a75e8819bc55f1e1ca19badf3f51408b284e353a7e5607d"
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _event_hash(event)
        previous = event["artifact_hash"]
    assert trace["final_event_hash"] == previous
    assert all("CANDIDATE_PROPOSED" != event["event_type"] for event in trace["entries"])

    assert metrics["RAKL_CYCLE_METRICS"]["active_atom"] == "RH-ANA-003"
    assert metrics["RAKL_CYCLE_METRICS"]["atom_fibre_snapshot_hash"] == context["fibre_snapshot_hash"]
    assert set(metrics["RAKL_CYCLE_METRICS"]["retained_semantic_novelty_counts"]) == SEVEN_AXES
    assert metrics["RAKL_CYCLE_METRICS"]["outcome"] == "PARTIAL_SUCCESS"
    assert metrics["RAKL_CYCLE_METRICS"]["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["RAKL_CYCLE_METRICS"]["rakl_changed_action"] is True
