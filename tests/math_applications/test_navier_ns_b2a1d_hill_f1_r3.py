from __future__ import annotations

import json
import math
from pathlib import Path

from rakl.experience_substrate import (
    EpisodeOutcome,
    EpisodeStorageAdmission,
    InventoryAdmissionVerdict,
    TaskEpisode,
    resolve_inventory_admission,
    validate_episode,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"


def _load(rel: str):
    return json.loads((BASE / rel).read_text())


def test_b2a1d_shadow_episode_is_content_valid_and_noncanonical() -> None:
    raw = _load("07_memory/NS-B2a1d_TASK_EPISODE_R3_20260812.json")
    episode = TaskEpisode(
        episode_id=raw["episode_id"], task_id=raw["task_id"], atom_id=raw["atom_id"],
        context_hash=raw["context_hash"], problem_signature=tuple(raw["problem_signature"]),
        fibre_snapshot_hash=raw["fibre_snapshot_hash"], operator_ids=tuple(raw["operator_ids"]),
        action_trace=tuple(raw["action_trace"]), observation_ids=tuple(raw["observation_ids"]),
        verification_ids=tuple(raw["verification_ids"]), outcome=EpisodeOutcome(raw["outcome"]),
        residual_signature=tuple(raw["residual_signature"]), evidence_pointers=tuple(raw["evidence_pointers"]),
        artifact_hash=raw["artifact_hash"], timestamp=raw["timestamp"], cost=raw["cost"],
        storage_admission=EpisodeStorageAdmission(raw["storage_admission"]),
    )
    assert validate_episode(episode) == ()
    report = resolve_inventory_admission(episode)
    assert report.verdict is InventoryAdmissionVerdict.PROPOSAL_SHADOW_STORED
    assert report.retained_for_search is True
    assert report.counts_toward_canonical_inventory is False


def test_b2a1d_hill_velocity_matches_across_unit_sphere() -> None:
    # Choi's explicit stream function gives these physical velocity components.
    W = 2 / 15
    for r in (0.0, 0.2, 0.7, 1.0):
        z = math.sqrt(max(0.0, 1 - r * r))
        vr_inside = 1.5 * W * r * z
        vz_inside = 0.5 * W * (5 - 6 * r * r - 3 * z * z)
        vr_outside = 1.5 * W * r * z
        vz_outside = 0.5 * W * (2 * z * z - r * r)
        assert math.isclose(vr_inside, vr_outside, rel_tol=0.0, abs_tol=1e-14)
        assert math.isclose(vz_inside, vz_outside, rel_tol=0.0, abs_tol=1e-14)


def test_b2a1d_far_field_and_centered_escape_exponents_are_integrable() -> None:
    # |V|=O(r^-3): L2 and L3 tails converge; |grad V|=O(r^-4): L2 tail converges.
    assert 2 - 3 * 2 < -1
    assert 2 - 3 * 3 < -1
    assert 2 - 4 * 2 < -1
    # At tau=-A^2, distance is O(A^2), hence velocity O(A^-6).
    # L^p(B(A)) is O(A^(3/p-6)); p=3 and p=6 both decay.
    assert 3 / 3 - 6 < 0
    assert 3 / 6 - 6 < 0


def test_b2a1d_metrology_does_not_count_candidate_lesson_as_learning() -> None:
    metrics = _load("10_case_study/NS-B2a1d_RAKL_CYCLE_METRICS_R3_20260812.json")
    counts = metrics["retained_semantic_novelty_counts"]
    assert counts["OPERATOR"] == 0
    assert counts["EXPERIENCE_PATTERN"] == 0
    assert counts["META_METHOD"] == 0
    assert metrics["raw_repository_growth_counts_as_learning"] is False
    assert metrics["gate_provenance_ci"]["root_authority"] == "NONE"
    assert metrics["gate_provenance_ci"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
