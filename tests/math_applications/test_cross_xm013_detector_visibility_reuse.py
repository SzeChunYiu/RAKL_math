from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "real_math" / "millennium" / "cross_problem"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def test_xm013_task_episode_is_content_bound_shadow_only() -> None:
    episode = _load(BASE / "07_memory" / "XM013_CURRENT_V3_TASK_EPISODE_SHADOW_20260811.taskepisode")
    artifact_hash = episode.pop("artifact_hash")
    assert hashlib.sha256(_canonical_bytes(episode)).hexdigest() == artifact_hash
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["residual_signature"]
    assert episode["evidence_pointers"]


def test_xm013_transfer_reuses_instead_of_minting_duplicate_obstruction() -> None:
    transfer = _load(BASE / "01_frontier" / "XM013_DETECTOR_VISIBILITY_REUSE_20260811.json")
    result = transfer["result"]
    assert result["new_mathematical_claim"] is False
    assert result["new_obstruction_minted"] is False
    assert result["transfer_decision"] == "STRUCTURAL_MOTIF_APPLIES_BUT_TARGET_OBSTRUCTION_ALREADY_STORED"
    assert "F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE" in result["successful_reuse_ids"]
    assert transfer["fibre"]["difference_witness"]["boundary"]
    assert transfer["fibre"]["disanalogies"]


def test_xm013_episode_diagnosis_lesson_remain_distinct_and_unpromoted() -> None:
    memory = _load(BASE / "07_memory" / "XM013_DIAGNOSIS_FAILURE_LESSON_SHADOW_20260811.json")
    assert memory["episode_lineage"] == ["EP-XM013-DETECTOR-VISIBILITY-REUSE-20260811"]
    assert memory["diagnosis"]["diagnosis_id"] == "D-XM013-DETECTOR-VISIBILITY-ALREADY-STORED"
    assert memory["obstruction"]["new_obstruction_id"] is None
    assert memory["obstruction"]["reused_obstruction_id"] == "F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE"
    assert memory["candidate_lesson"]["status"] == "PROPOSAL_SHADOW_CANDIDATE_NOT_PROMOTED"
    assert memory["candidate_lesson"]["learning_credit"] == 0


def test_xm013_metrics_have_seven_axes_and_fail_closed_current_work() -> None:
    packet = _load(BASE / "10_study_pattern" / "RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM013_20260811.json")
    metrics = packet["RAKL_CYCLE_METRICS"]
    axes = {"KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD"}
    assert set(metrics["retained_semantic_novelty"]) == axes
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["current_work_coverage"]["status"] == "CURRENT_WORK_NOT_BOUND"
    assert metrics["current_work_coverage"]["open_issue_count"] == 33
    assert metrics["current_work_coverage"]["open_pr_count"] == 59
    assert metrics["raw_repository_growth_is_learning"] is False
    assert metrics["gate_provenance_ci"]["independent_mathematical_reviews"] == 0
    assert metrics["gate_provenance_ci"]["scientific_authority_promotion"] == "NOT_INVOKED"


def test_xm013_cross_lane_aggregate_excludes_unmeasured_pnp_vector() -> None:
    packet = _load(BASE / "10_study_pattern" / "RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM013_20260811.json")
    aggregate = packet["RAKL_CYCLE_METRICS"]["cross_lane_aggregates"]
    assert aggregate["retained_novelty_lower_bound_explicit_five_lane_vectors"] == {
        "KNOWLEDGE": 3,
        "OPERATOR": 1,
        "EXPERIENCE_PATTERN": 2,
        "OBSTRUCTION": 4,
        "RELATION": 5,
        "PATH": 5,
        "META_METHOD": 0,
    }
    assert aggregate["retained_novelty_lower_bound_plus_XM013"] == {
        "KNOWLEDGE": 3,
        "OPERATOR": 1,
        "EXPERIENCE_PATTERN": 3,
        "OBSTRUCTION": 4,
        "RELATION": 6,
        "PATH": 6,
        "META_METHOD": 0,
    }
    assert any("P_vs_NP" in item for item in aggregate["excluded_from_vector"])
