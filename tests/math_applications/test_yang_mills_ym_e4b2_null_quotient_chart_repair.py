from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"
PRE = YM / "01_frontier" / "YM-E4b2_PRE_ACTION_FIBRE_RECEIPT_20260811.json"
CANDIDATE = YM / "04_candidates" / "YM-E4b2_OS_NULL_QUOTIENT_CHART_REPAIR_20260811.md"
METRICS = YM / "10_case_study" / "YM-E4b2_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260811.json"


def test_preaction_precedes_repair_outcome_and_binds_current_cycle() -> None:
    pre = json.loads(PRE.read_text())
    assert pre["schema_version"] == "rakl-math-pre-action-fibre-receipt-shadow-v1"
    assert pre["pre_outcome"] == "UNOBSERVED_AT_RECEIPT_FREEZE"
    assert pre["atom"]["id"] == "YM-E4b2"
    assert pre["framework"]["method_version"] == "3.0.0"
    assert pre["framework"]["main_sha"] == "787c7e00af2a5877ccb715bc807ec14f52974e9c"
    assert pre["application"]["base_sha"] == "dc83b72201cb58844b2bdc76117e4dcb9190211d"
    assert pre["fibre_snapshot_hash"].startswith("sha256:")
    assert len(pre["fibre_snapshot_hash"].removeprefix("sha256:")) == 64


def test_collapsing_null_space_falsifies_raw_quotient_descent() -> None:
    # q0(x,y)=x^2 has e2 as a null vector; q_eps=x^2+eps*y^2 does not.
    e2 = (0.0, 1.0)

    def q0(v: tuple[float, float]) -> float:
        return v[0] ** 2

    def qeps(v: tuple[float, float], eps: float) -> float:
        return v[0] ** 2 + eps * v[1] ** 2

    assert q0(e2) == 0.0
    for eps in (1.0, 0.1, 1e-3, 1e-6):
        assert qeps(e2, eps) > 0.0
        assert abs(qeps(e2, eps) - q0(e2)) == eps
    assert qeps(e2, 1e-9) < qeps(e2, 1e-6)


def test_candidate_scope_and_seven_axis_zero_retention_are_bound() -> None:
    text = CANDIDATE.read_text()
    metrics = json.loads(METRICS.read_text())
    assert "R_sigma(N_0) subseteq N_sigma" in text
    assert "finite-chart" in text
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in text
    novelty = metrics["RAKL_CYCLE_METRICS"]["retained_semantic_novelty"]
    for axis in (
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    ):
        assert novelty[axis] == 0
    assert metrics["RAKL_CYCLE_METRICS"]["outcome"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["RAKL_CYCLE_METRICS"]["gate_provenance_ci"]["independent_mathematical_reviews"] == 0


def test_hash_chain_is_closed_and_non_promoting() -> None:
    metrics = json.loads(METRICS.read_text())
    trace = metrics["hash_chained_trace"]
    assert trace[0]["parent_hash"] is None
    for previous, current in zip(trace, trace[1:]):
        assert current["parent_hash"] == previous["event_hash"]
    assert all(event["event_hash"].startswith("sha256:") for event in trace)
    assert metrics["task_episode"]["authority"] == "PROPOSAL_SHADOW_ONLY"
