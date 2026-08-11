from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"


def _hash_without_artifact(value: dict[str, object]) -> str:
    payload = dict(value)
    payload.pop("artifact_hash", None)
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def test_current_frontier_audit_is_source_bound_and_candidate_free() -> None:
    text = (
        BSD
        / "01_frontier/BSD_A1a1_CURRENT_2026_ANTICYCLOTOMIC_FRONTIER_AUDIT.md"
    ).read_text(encoding="utf-8")
    assert "bd1a2768f0f474ff44ffa25243241f94bfaf6466" in text
    assert "8a608f340d47b4b6ae612275b0595faf6b804432" in text
    assert "arXiv:2608.06879" in text
    assert "arXiv:2603.22483" in text
    assert "CM elliptic curves" in text
    assert "weight at least 4" in text
    assert "NO_MATHEMATICAL_CANDIDATE" in text
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in text


def test_current_frontier_episode_is_shadow_only_and_content_bound() -> None:
    episode = json.loads(
        (
            BSD
            / "07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_SHADOW.json"
        ).read_text(encoding="utf-8")
    )
    assert episode["artifact_type"] == "TASK_EPISODE_SHADOW"
    assert episode["authority"] == "PROPOSAL_SHADOW_SEARCH_PRIORITY_ONLY"
    assert episode["framework_semantic_authority"]["commit"] == (
        "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    )
    assert episode["execution_dependency_pin"]["commit"] == (
        "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
    )
    assert episode["new_authority_objects"] == {
        "lessons_promoted": [],
        "tools_promoted": [],
        "mathematical_candidates": [],
        "root_promotions": [],
    }
    assert episode["artifact_hash"] == _hash_without_artifact(episode)


def test_current_frontier_failure_stays_observed_only() -> None:
    failure = json.loads(
        (
            BSD / "07_memory/BSD_A1a1_CURRENT_2026_FAILURE_SHADOW.json"
        ).read_text(encoding="utf-8")
    )
    assert failure["authority"] == "OBSERVED_ONLY"
    assert failure["allowed_effect"] == "SEARCH_PRIORITY_WARNING_ONLY"
    assert failure["reusable_lesson_status"] == "NOT_PROMOTED"
    assert len(failure["competing_diagnoses"]) >= 3
    assert failure["artifact_hash"] == _hash_without_artifact(failure)


def test_cycle_metrics_quantify_all_seven_axes_and_fail_closed() -> None:
    metrics = json.loads(
        (
            BSD / "07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R2.json"
        ).read_text(encoding="utf-8")
    )
    assert metrics["artifact_type"] == "RAKL_CYCLE_METRICS"
    assert metrics["authority"] == "MEASUREMENT_ONLY_NO_PROMOTION_AUTHORITY"
    assert metrics["framework"]["semantic_git_sha"] == (
        "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    )
    assert metrics["framework"]["method_version"] == "CANNOT_MEASURE"
    assert metrics["application"]["base_sha"] == (
        "8a608f340d47b4b6ae612275b0595faf6b804432"
    )
    assert metrics["fibre_snapshot_hash"] == (
        "sha256:385d587cb9ab74512adc3fed98e00df9a804c37fd327539c2cea449a97b5417d"
    )
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert metrics["state_fingerprints"]["pre"] == "CANNOT_MEASURE"
    assert metrics["state_fingerprints"]["post"] == "CANNOT_MEASURE"
    assert metrics["rakl_action_counterfactual"]["status"] == "CANNOT_MEASURE"
    assert metrics["new_objects"]["lesson_ids"] == []
    assert metrics["new_objects"]["tool_ids"] == []
    assert metrics["new_objects"]["obstruction_ids"] == []
    assert metrics["new_objects"]["motif_ids"] == []
    assert metrics["artifact_hash"] == _hash_without_artifact(metrics)
