from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"


def _json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_r8_fibre_episode_and_source_scope_are_bound() -> None:
    fibre = _json(BSD / "01_frontier/BSD_A1a1_R8_BKS_RANK_INDEX_CONTEXT_FIBRE_20260812.json")
    episode = _json(BSD / "07_memory/BSD_A1a1_R8_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode")
    source = _json(BSD / "00_sources/BSD_A1a1_R8_BKS_RANK_INDEX_SOURCE_RECEIPT_20260812.json")

    assert fibre["atom_id"] == "BSD-A1a1-THETA-ORDER-COMPARISON"
    assert fibre["packet_hash"] == "sha256:31e70137e19f33c745dd76608ae2e84bb5d2d2cdb315476ba18eeecda84a97e1"
    assert episode["fibre_snapshot_hash"] == fibre["packet_hash"]
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS_ROUTE_PRUNED_NO_ROOT_CANDIDATE"
    assert source["source_family_completeness"] == "BOUNDED_CURRENT_PRIMARY_SOURCE_AUDIT_NOT_LITERATURE_COMPLETE"
    result = source["derived_scope_result"]
    assert "algebraic-rank-indexed" in result["statement"]
    assert any("No impossibility theorem" in x for x in result["not_claimed"])


def test_r8_episode_diagnosis_failure_obstruction_remain_distinct() -> None:
    diagnosis = _json(BSD / "07_memory/BSD_A1a1_R8_DIAGNOSIS_SHADOW_20260812.json")
    failure = _json(BSD / "07_memory/BSD_A1a1_R8_ANALYTIC_TO_ALGEBRAIC_RANK_INDEX_FAILURE_SHADOW_20260812.json")
    obstruction = _json(BSD / "07_memory/BSD_A1a1_R8_TARGET_INDEXED_DERIVATIVE_OBSTRUCTION_SHADOW_20260812.json")

    assert diagnosis["artifact_type"] == "DIAGNOSIS_PROPOSAL_SHADOW"
    assert failure["artifact_type"] == "FAILURE_EXPERIENCE_PROPOSAL_SHADOW"
    assert obstruction["artifact_type"] == "OBSTRUCTION_PROPOSAL_SHADOW"
    assert failure["retained_as_learning"] is False
    assert obstruction["retained_novelty_OBSTRUCTION"] == 0
    assert obstruction["promotion_status"] == "PROPOSAL_SHADOW_ONLY"
    assert diagnosis["local_mathematical_failure"] is False
    assert diagnosis["local_to_global_gluing_failure"] is True


def test_r8_metrics_have_exact_seven_axis_receipt_and_no_authority_promotion() -> None:
    metrics = _json(BSD / "07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260812_R8.json")
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["framework"]["method_specs_blob_sha"] == "6342f2692b3fd85de3f274f9c6548c9736225691"
    assert metrics["framework"]["v3_facade_blob_sha"] == "280bf143fc8910d5860aaa02fbe3817a6aacfb72"
    assert metrics["application"]["base_sha"] == "a7301f0f0e2cab2750ac6e923efe18b5750b5af6"
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["gates"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gates"]["scientific_authority_promotion"] == "NOT_INVOKED"
    assert metrics["raw_repository_growth_is_learning"] is False


def test_r8_trace_continues_r7_hash_chain() -> None:
    trace = _json(BSD / "09_trace/BSD_A1a1_R8_RESULT_TRACE_DELTA_20260812.json")
    assert trace["base_last_event_id"] == "BSD-A1a1-E26-R7-REVIEW"
    assert trace["base_last_event_hash"] == "sha256:be71bb36fdb30705154c45e1f6873bfb7fd7b401972e66ecf2c701a6ff18cac8"
    previous = trace["base_last_event_hash"]
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        assert entry["artifact_hash"].startswith("sha256:")
        previous = entry["artifact_hash"]
    assert trace["authority"] == "PUBLIC_DECISION_TRACE_DELTA_NO_ROOT_AUTHORITY"


def test_r8_case_study_and_route_diagnostic_preserve_root_boundary() -> None:
    case = (BSD / "07_memory/RAKL_METHOD_CASE_STUDY_BSD_A1a1_BKS_RANK_INDEX_20260812_R8.md").read_text(encoding="utf-8")
    route = (BSD / "02_problem_dag/BSD_A1a1_R8_BKS_RANK_INDEX_ROUTE_DIAGNOSTIC_20260812.yaml").read_text(encoding="utf-8")
    assert "index_provenance" in case
    assert "Experience guided search only" in case
    assert "root_state: OPEN_NO_SOLUTION_CERTIFICATE" in route
    assert "DIRECT_BKS_ANALYTIC_RANK2_SUBSTITUTION_PRUNED" in route
