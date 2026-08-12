from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HODGE = ROOT / "research/real_math/millennium/hodge/deformation"
FIBRE = HODGE / "01_frontier/H4d1c_C009_FROZEN_FIBRE_20260812.json"
EPISODE = HODGE / "07_memory/H4d1c_C009_TASK_EPISODE_SHADOW_20260812.jsonl"
DIAGNOSIS = HODGE / "07_memory/H4d1c_C009_DIAGNOSIS_20260812.json"
OBSTRUCTION = HODGE / "07_memory/H4d1c_C009_OBSTRUCTION_20260812.json"
FAILURE = HODGE / "07_memory/H4d1c_C009_PROCESS_FAILURE_20260812.json"
TRACE = HODGE / "09_trace/H4d1c_C009_HASH_CHAIN_TRACE_20260812.json"
METRICS = HODGE / "09_trace/H4d1c_C009_RAKL_CYCLE_METRICS_20260812.json"
ROUTE = HODGE / "03_routes/H4d1c_C009_RELATIVE_HILBERT_SMOOTHNESS_CERTIFICATE_20260812.md"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_c009_stays_shadow_and_root_open() -> None:
    fibre = _load(FIBRE)
    episode = json.loads(EPISODE.read_text(encoding="utf-8"))
    metrics = _load(METRICS)
    assert fibre["application"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert metrics["gates"]["root_promotion"] == "BLOCKED_OPEN_ROOT"
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
    }


def test_c009_types_relative_smoothness_not_tangent_or_fibre_proxy() -> None:
    route = ROUTE.read_text(encoding="utf-8")
    diagnosis = _load(DIAGNOSIS)
    assert "relative Hilbert morphism" in route
    assert "Smoothness of the fixed-fibre Hilbert scheme" in route
    assert "Bare `H^1(N)=0` slogan" in route
    assert "RELATIVE-NOT-FIBREWISE" in diagnosis["diagnosis_id"]


def test_c009_residual_and_gluing_are_separate() -> None:
    obstruction = _load(OBSTRUCTION)
    metrics = _load(METRICS)
    assert obstruction["obstruction_id"] == "O-H4D1C-RELATIVE-HILBERT-SMOOTHNESS-OR-COUPLED-DOMINANCE"
    assert obstruction["local_vs_gluing"] == "LOCAL_MATHEMATICAL_OBSTRUCTION"
    assert "MONODROMY_BEYOND_LOCAL_MARKING" in obstruction["separate_gluing_obstructions"]
    assert metrics["saturation"]["hodge_seven_axes"]["BRANCH_REACHABILITY"].startswith("REOPENED")


def test_c009_trace_is_hash_chained_and_chronology_failure_is_retained() -> None:
    trace = _load(TRACE)
    events = trace["events"]
    assert len(events) >= 12
    for previous, current in zip(events, events[1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    assert trace["terminal_event_hash"] == events[-1]["artifact_hash"]
    failure = _load(FAILURE)
    assert failure["failure_id"] == "F-H4D1C-C009-PREFREEZE-HYPOTHESIS-EXPOSURE"
    assert "F-H4D1C-C008-PREFREEZE-HYPOTHESIS-EXPOSURE" in failure["repeat_link"]
