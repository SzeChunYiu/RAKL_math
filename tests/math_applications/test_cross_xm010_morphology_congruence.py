from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/cross_problem"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_xm010_task_episode_is_content_bound_shadow_only() -> None:
    path = BASE / "07_memory/XM010_CURRENT_V3_TASK_EPISODE_SHADOW_20260811_R6.taskepisode"
    episode = _load(path)
    asserted = episode.pop("artifact_hash")
    canonical = json.dumps(episode, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert hashlib.sha256(canonical).hexdigest() == asserted
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"


def test_xm010_disjoint_copy_weak_l32_scaling_is_exact() -> None:
    p = 3.0 / 2.0
    c = 2.0 ** (-2.0 / 3.0)
    assert math.isclose(c * 2.0 ** (1.0 / p), 1.0, rel_tol=0.0, abs_tol=1e-15)


def test_xm010_registered_difference_witness_and_scope() -> None:
    mapping = _load(BASE / "07_memory/XM010_PNP_NS_TRANSFER_MAPPING_20260811_R6.json")
    assert mapping["transfer_verdict"] == (
        "APPLICABLE_AS_REPRESENTATION_FALSIFIER; NO_MATHEMATICAL_THEOREM_TRANSFER"
    )
    assert "2^(-2/3)" in mapping["difference_witness"]["same_projection"]
    assert "one-core Q=true" in mapping["difference_witness"]["different_outcome"]

    proof = (BASE / "04_candidates/XM010_PNP_NS_MORPHOLOGY_CONGRUENCE_FALSIFIER_20260811_R6.md").read_text(
        encoding="utf-8"
    )
    assert "not asserted to solve Navier" in proof
    assert "cannot refute `NSE + finite I -> morphology`" in proof
    assert "|p_+ - p_-| = 2" in proof


def test_xm010_metrics_count_no_shadow_artifact_as_retained_learning() -> None:
    metrics = _load(BASE / "10_study_pattern/RAKL_CYCLE_METRICS_XM010_20260811_R6.json")
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert metrics["raw_repository_growth_counts_as_learning"] is False
    assert metrics["gates_provenance_ci"]["canonical_inventory_admission"] == "NOT_REQUESTED"
    assert metrics["gates_provenance_ci"]["root_promotion"] == "BLOCKED_OPEN_RESIDUALS"
    assert metrics["cross_lane_aggregates"]["latest_comparable_episode_count"] == 6
    assert metrics["cross_lane_aggregates"]["retained_novelty_totals"] == {
        "KNOWLEDGE": 5,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 3,
        "OBSTRUCTION": 4,
        "RELATION": 6,
        "PATH": 4,
        "META_METHOD": 0,
    }


def test_xm010_trace_is_hash_chained() -> None:
    trace = _load(BASE / "09_trace/XM010_HASH_CHAIN_TRACE_20260811_R6.json")
    prev = "0" * 64
    for event in trace["events"]:
        asserted = event["event_hash"]
        payload = {key: value for key, value in event.items() if key != "event_hash"}
        assert payload["prev_hash"] == prev
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        assert hashlib.sha256(canonical).hexdigest() == asserted
        prev = asserted
    assert prev == trace["terminal_hash"]
