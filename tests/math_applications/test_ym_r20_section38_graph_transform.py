"""Assurance-only controls for YM-S1a2i R20.

These tests calibrate the recorded scalar hostile controls and authority metadata.
They are not mathematical proof, novelty review, or Yang--Mills evidence.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1a2i_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260812_R20.json"


def test_value_remainder_does_not_calibrate_monotonicity() -> None:
    b = 1.0
    eps = 1.0
    g0 = 0.1
    n = (2 * 10_000 + 1) * math.pi / g0

    def r(g: float) -> float:
        return eps * g**5 * math.sin(n * g)

    def derivative(g: float) -> float:
        return 1.0 - 3.0 * b * g**2 + eps * (
            5.0 * g**4 * math.sin(n * g) + n * g**5 * math.cos(n * g)
        )

    # Same pointwise source shape |r(g)| <= eps g^5.
    for g in (1e-6, 0.01, 0.05, g0):
        assert abs(r(g)) <= eps * g**5 + 1e-30

    # Smooth pointwise control alone does not calibrate a uniform monotonicity margin.
    assert derivative(1e-8) > 0.0
    assert derivative(g0) < 0.0


def test_forward_relevant_graph_control_expands_and_misses_smaller_radius() -> None:
    g = 0.1
    b = 1.0
    g_next = g - b * g**3
    a = 2.0
    rho = 0.5
    c_lambda = 3.0

    assert 0.0 < rho < 1.0
    assert 0.0 < g_next < g

    # Sup-norm difference in the relevant graph coordinate is multiplied by a>1.
    graph_difference = 0.25
    assert a * graph_difference > graph_difference

    # A boundary point in the old O(g^2) radius does not land in the smaller O(g_next^2) radius.
    lambda_old = c_lambda * g**2
    lambda_next = a * lambda_old
    assert lambda_next > c_lambda * g_next**2


def test_r20_packet_keeps_protected_authority_zero() -> None:
    data = json.loads(PACKET.read_text())
    metrics = data["RAKL_CYCLE_METRICS"]
    assert data["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert data["TaskEpisode"]["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert set(metrics["protected_retained_semantic_novelty"].values()) == {0}
    assert metrics["gate_status"]["independent_mathematical_reviews"] == "0/3"
    assert metrics["gate_status"]["root_promotion"] == "DENIED_NOT_ATTEMPTED"
