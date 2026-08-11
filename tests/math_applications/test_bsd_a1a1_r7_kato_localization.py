from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"


def _json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_r7_fibre_episode_and_source_scope_are_bound() -> None:
    fibre = _json(BSD / "01_frontier/BSD_A1a1_R7_KATO_LOCALIZATION_CONTEXT_FIBRE_20260811.json")
    episode = _json(BSD / "07_memory/BSD_A1a1_R7_CURRENT_V3_TASK_EPISODE_SHADOW_20260811.taskepisode")
    source = _json(BSD / "00_sources/BSD_A1a1_R7_KATO_LOCALIZATION_SOURCE_RECEIPT_20260811.json")

    assert fibre["atom_id"] == "BSD-A1a1-THETA-ORDER-COMPARISON"
    assert fibre["packet_hash"] == "sha256:788ae31fb787de32f0ab9b4a6e715c0a3092db5332e562dd1481ca29ed324375"
    assert episode["fibre_snapshot_hash"] == fibre["packet_hash"]
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert source["source_family_completeness"] == "BOUNDED_CURRENT_PRIMARY_SOURCE_AUDIT_NOT_LITERATURE_COMPLETE"
    result = source["derived_scope_result"]
    assert "Selmer dimension two" in result["statement"]
    assert "transverse" in result["statement"]
    assert any("No impossibility theorem" in x for x in result["not_claimed"])


def test_r7_episode_diagnosis_failure_obstruction_remain_distinct() -> None:
    diagnosis = _json(BSD / "07_memory/BSD_A1a1_R7_DIAGNOSIS_SHADOW_20260811.json")
    failure = _json(BSD / "07_memory/BSD_A1a1_R7_ANALYTIC_TO_TRANSVERSE_LOCALIZATION_FAILURE_SHADOW_20260811.json")
    obstruction = _json(BSD / "07_memory/BSD_A1a1_R7_TRANSVERSE_LOCALIZATION_OBSTRUCTION_SHADOW_20260811.json")

    assert diagnosis["artifact_type"] == "DIAGNOSIS_PROPOSAL_SHADOW"
    assert failure["artifact_type"] == "FAILURE_EXPERIENCE_PROPOSAL_SHADOW"
    assert obstruction["artifact_type"] == "OBSTRUCTION_PROPOSAL_SHADOW"
    assert failure["retained_as_learning"] is False
    assert obstruction["retained_novelty_OBSTRUCTION"] == 0
    assert obstruction["promotion_status"] == "PROPOSAL_SHADOW_ONLY"
    assert diagnosis["local_mathematical_failure"] is False
    assert diagnosis["local_to_global_gluing_failure"] is True


def test_r7_metrics_have_exact_seven_axis_receipt_and_no_authority_promotion() -> None:
    metrics = _json(BSD / "07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R7.json")
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["framework"]["exact_current_main_sha_at_metrics_sample"] == "a2db16d56d03d16c4e7b9dc8684263d8661b89fc"
    assert metrics["framework"]["method_specs_blob_sha"] == "6342f2692b3fd85de3f274f9c6548c9736225691"
    assert metrics["application"]["base_sha"] == "55f1b786396f0f29ee4edd7e80b0b0023b34e90f"
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


def test_r7_trace_continues_r6_hash_chain() -> None:
    trace = _json(BSD / "09_trace/BSD_A1a1_R7_RESULT_TRACE_DELTA_20260811.json")
    assert trace["base_last_event_id"] == "BSD-A1a1-E22-R6-REVIEW"
    assert trace["base_last_event_hash"] == "sha256:73ff85eea8d7585b2974617c0ca5cdc7e60a0ecdfa6cf319d94b449acac9575b"
    previous = trace["base_last_event_hash"]
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        assert entry["artifact_hash"].startswith("sha256:")
        previous = entry["artifact_hash"]
    assert trace["authority"] == "PUBLIC_DECISION_TRACE_DELTA_NO_ROOT_AUTHORITY"


def test_r7_case_study_and_route_diagnostic_preserve_root_boundary() -> None:
    case = (BSD / "07_memory/RAKL_METHOD_CASE_STUDY_BSD_A1a1_KATO_LOCALIZATION_20260811_R7.md").read_text(encoding="utf-8")
    route = (BSD / "02_problem_dag/BSD_A1a1_R7_KATO_LOCALIZATION_ROUTE_DIAGNOSTIC_20260811.yaml").read_text(encoding="utf-8")
    assert "route re-entry/cycle edge" in case
    assert "state_fingerprint_v2" in case
    assert "ROOT_STATE_OPEN_NO_SOLUTION_CERTIFICATE" in route
    assert "BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE" in route
