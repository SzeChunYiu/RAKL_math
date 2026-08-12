from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"


def load_json(rel: str) -> dict:
    return json.loads((BSD / rel).read_text())


def test_r14_pre_action_was_prospective_and_framework_pinned() -> None:
    pre = load_json("07_memory/BSD_S001c1_R14_PRE_ACTION_RECEIPT_20260812.json")
    assert pre["chronology"] == "FROZEN_BEFORE_R14_PARITY_SOURCE_SEARCH"
    assert pre["framework_sha"] == "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
    assert pre["application_base_sha"] == "451d9506d365f06eb314323523ba123edd3ffb32"
    assert pre["atom_id"] == "BSD-S001c1-KURIHARA-TAYLOR-COMPARISON"
    assert pre["scientific_authority_granted"] is False
    assert pre["root_promotion_granted"] is False
    assert pre["preference_before_memory_gate"] != pre["preference_after_memory_gate"]


def test_r14_source_bound_parity_relation_is_scoped_not_exact() -> None:
    audit = load_json("00_sources/BSD_S001c1_R14_PARITY_COMPARISON_SOURCE_AUDIT_20260812.json")
    lemma = audit["exact_composition"]
    assert lemma["lemma_id"] == "LEM-BSD-R14-KURIHARA-COMPLEX-PARITY"
    assert "modulo 2" in lemma["statement"]
    assert lemma["new_mathematics_claim"] is False
    assert audit["counterexample_first_falsifier"]["hostile_pair"] == [2, 4]
    assert audit["counterexample_first_falsifier"]["result"] == "SURVIVES"
    assert audit["failure_typing"]["local_mathematics"] == "SUCCESS_WITHIN_SCOPED_THEOREM_CELL"
    assert audit["failure_typing"]["gluing"] == "OPEN_MAGNITUDE_COMPARISON_AND_GLOBAL_BSD_GLUE"
    assert audit["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_r14_episode_diagnosis_failure_are_distinct() -> None:
    episode = load_json("07_memory/BSD_S001c1_R14_V3_TASK_EPISODE_SHADOW_20260812.taskepisode")
    diagnosis = load_json("07_memory/BSD_S001c1_R14_DIAGNOSIS_SHADOW_20260812.json")
    failure = load_json("07_memory/BSD_S001c1_R14_FAILURE_SHADOW_20260812.json")
    assert episode["episode_id"] == failure["episode_reference_id"] == diagnosis["episode_reference_id"]
    assert diagnosis["diagnosis_id"] == failure["diagnosis_reference_id"]
    assert diagnosis["new_obstruction_id"] is None
    assert diagnosis["new_lesson_id"] is None
    assert failure["local_mathematics_failed"] is False
    assert failure["local_to_global_gluing_failed"] is True
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_ONLY"


def test_r14_dag_refines_to_magnitude_residual_without_root_promotion() -> None:
    dag = (BSD / "02_problem_dag/open_obligations.yaml").read_text()
    assert "SOURCE_BOUND_PARITY_REFINED_MAGNITUDE_OPEN" in dag
    assert "ord(Kurihara) congruent to ord_{s=1}L(E,s) mod 2" in dag
    assert "No source-bound magnitude bound excludes 4,6,..." in dag
    assert dag.startswith("root: BSD\nauthority: OPEN_NO_SOLUTION_CERTIFICATE")


def test_r14_trace_extends_canonical_s001c1_chain() -> None:
    trace = load_json("09_trace/BSD_S001c1_R14_RESULT_TRACE_DELTA_20260812.json")
    events = trace["events"]
    assert events[0]["previous_event_hash"] == "sha256:67a09967e75a4b56fb4bbf3440b58295b88ce3a419da8285c030a7439344e5ca"
    for previous, current in zip(events, events[1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    assert trace["trace_tail_hash"] == events[-1]["artifact_hash"]


def test_r14_case_study_and_metrics_keep_authority_and_learning_conservative() -> None:
    case = load_json("10_feedback/RAKL_METHOD_CASE_STUDY_BSD_S001c1_R14_20260812.json")
    metrics = load_json("07_memory/BSD_S001c1_R14_RAKL_CYCLE_METRICS_20260812.json")
    assert case["outcome"] == "SCOPED_SOURCE_BOUND_MOD2_COMPLEX_DISCRETE_RELATION; ROOT_OPEN"
    assert case["failure_category"]["gluing"] is True
    assert case["episode_diagnosis_obstruction_lesson_separation"]["new_lesson"] is None
    novelty = metrics["retained_semantic_novelty"]
    assert novelty == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["application"]["raw_repository_growth_is_learning"] is False
    assert metrics["gate_provenance_ci"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["independent_mathematical_review_credit"] == 0
    assert metrics["rakl_action_effect"]["changed_observable_pre_memory_pre_gate_preference"] is True
