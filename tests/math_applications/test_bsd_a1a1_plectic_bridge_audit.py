from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_plectic_bridge_cycle_stays_shadow_and_root_open() -> None:
    episode = _load(BSD / "07_memory" / "BSD_A1a1_PLECTIC_TASK_EPISODE_SHADOW_20260811_R3.json")
    failure = _load(BSD / "07_memory" / "BSD_A1a1_PLECTIC_FAILURE_SHADOW_20260811_R3.json")
    metrics = _load(BSD / "07_memory" / "BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R3.json")

    assert episode["atom_id"] == "BSD-A1a1-THETA-ORDER-COMPARISON"
    assert episode["authority"] == "PROPOSAL_SHADOW_SEARCH_PRIORITY_ONLY"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["new_authority_objects"] == {
        "lessons_promoted": [],
        "tools_promoted": [],
        "mathematical_candidates": [],
        "root_promotions": [],
    }
    assert failure["diagnosis_status"] == "OBSERVED_ONLY"
    assert failure["authority"] == "OBSERVED_ONLY_SHADOW_NO_BLOCKING_AUTHORITY"
    assert metrics["authority"] == "MEASUREMENT_ONLY_NO_PROMOTION_AUTHORITY"
    assert metrics["gate_provenance_ci"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["mathematical_candidate_generated"] is False
    assert metrics["gate_provenance_ci"]["lesson_or_tool_promoted"] is False


def test_plectic_metrics_do_not_count_raw_growth_as_learning() -> None:
    metrics = _load(BSD / "07_memory" / "BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R3.json")

    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert all(metrics["raw_growth_not_learning"].values())
    assert metrics["framework_learning"]["promoted_new_lesson_count"] == 0
    assert metrics["framework_learning"]["promoted_new_tool_count"] == 0
    assert metrics["framework_learning"]["promoted_new_meta_method_count"] == 0
    assert metrics["rakl_action_counterfactual"]["status"] == "CANNOT_MEASURE"
    assert metrics["state_fingerprints"]["pre"] == "CANNOT_MEASURE"
    assert metrics["state_fingerprints"]["post"] == "CANNOT_MEASURE"


def test_plectic_trace_delta_extends_frozen_a1a1_trace_without_candidate() -> None:
    delta = _load(BSD / "09_trace" / "BSD_A1a1_PLECTIC_RESEARCH_TRACE_DELTA_20260811_R3.json")

    assert delta["base_last_event_id"] == "BSD-A1a1-E07"
    assert delta["base_last_event_hash"] == "sha256:878564f38d9a1b30fc23e70cae1012b07d8edb8e765a58907d1423dbd769c0a8"
    assert [entry["event_type"] for entry in delta["entries"]] == ["RESULT_RECORDED", "REVIEWED"]
    assert delta["entries"][0]["previous_event_hash"] == delta["base_last_event_hash"]
    assert delta["entries"][1]["previous_event_hash"] == delta["entries"][0]["artifact_hash"]
    assert "candidate_status:NONE" in delta["entries"][0]["outputs"]
    assert "candidate_generation:BLOCKED" in delta["entries"][1]["outputs"]


def test_current_framework_and_execution_pin_are_synchronized_prospectively() -> None:
    metrics = _load(BSD / "07_memory" / "BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R3.json")

    expected = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert metrics["framework"]["semantic_git_sha"] == expected
    assert metrics["framework"]["execution_dependency_pin"] == expected
    assert metrics["framework"]["semantic_execution_pin_synchronized"] is True


def test_audit_distinguishes_theorem_level_downstream_arrows_from_missing_first_arrow() -> None:
    audit = (BSD / "01_frontier" / "BSD_A1a1_PLECTIC_BRIDGE_AUDIT_20260811.md").read_text(encoding="utf-8")

    assert "nonzero mock plectic invariant -> p-Selmer rank two" in audit
    assert "complex analytic rank -> plectic-class nonvanishing/significance" in audit
    assert "conjectural" in audit
    assert "No mathematical candidate" in audit
