from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CROSS = ROOT / "research/real_math/millennium/cross_problem"
YM = ROOT / "research/real_math/millennium/yang_mills"
RESULT = CROSS / "07_memory/XM024_HODGE_YM_FAMILYWISE_UNIFORMITY_20260812.json"
CASE = CROSS / "10_case_study/XM024_RAKL_METHOD_CASE_STUDY_20260812.json"
CASE_DRIFT = CROSS / "10_case_study/XM024_RAKL_METHOD_CASE_STUDY_DRIFT_DELTA_20260812.json"
METRICS = CROSS / "10_case_study/XM024_RAKL_CYCLE_METRICS_20260812.json"
METRICS_DRIFT = CROSS / "10_case_study/XM024_RAKL_CYCLE_METRICS_DRIFT_CORRECTION_20260812.json"
DAG = YM / "02_problem_dag/YM_S1a2j_XM024_FAMILYWISE_UNIFORMITY_DAG_DELTA_20260812.json"

AXES = {
    "KNOWLEDGE",
    "OPERATOR",
    "EXPERIENCE_PATTERN",
    "OBSTRUCTION",
    "RELATION",
    "PATH",
    "META_METHOD",
}


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_xm024_hostile_family_is_pointwise_contracting_but_not_uniform() -> None:
    # L_k = diag(2, 1+1/k).  The inverse norm in Euclidean coordinates is
    # max(1/2, k/(k+1)) = k/(k+1).  Every coordinate is a strict
    # contraction, but the supremum over k is 1.
    for k in (1, 2, 3, 10, 100, 10_000):
        q_k = max(Fraction(1, 2), Fraction(k, k + 1))
        assert q_k < 1
        assert Fraction(k + 1, k) > 1  # conorm m(L_k)=1+1/k

    # Exact epsilon witness for sup_k q_k = 1: for every integer m>1,
    # q_m = m/(m+1) > 1 - 1/m.
    for m in (2, 3, 5, 11, 101, 1009):
        assert Fraction(m, m + 1) > 1 - Fraction(1, m)


def test_xm024_result_keeps_transfer_scope_and_roots_open() -> None:
    data = _load(RESULT)
    assert data["authority"] == "PROPOSAL_SHADOW_ONLY_NO_THEOREM_NO_ROOT_AUTHORITY"
    assert data["chronology"]["hypothesis_generation_credit"] == "RETROSPECTIVE_ONLY"
    assert data["difference_witness"]["source_atom"] == "H4d1c-C009"
    assert data["difference_witness"]["target_atom"] == "YM-S1a2j/R22"
    assert "sup_k ||L_k^-1|| = 1" in data["verification"]["family_fact"]
    assert "No claim that Wilson's actual L_k realize this hostile family." in data["verification"]["nonclaims"]
    assert set(data["root_status"].values()) == {"OPEN_NO_SOLUTION_CERTIFICATE"}


def test_xm024_dag_refines_uniformity_without_closing_downstream() -> None:
    dag = _load(DAG)
    assert dag["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    child_ids = {item["atom_id"] for item in dag["refined_children"]}
    assert child_ids == {"YM-S1a2j-u1", "YM-S1a2j-u2"}
    assert "GAUGE_TO_OS_PHYSICAL_RECONSTRUCTION" in dag["unchanged_downstream"]
    assert "CONTINUUM_LIMIT_AND_PHYSICAL_MASS_GAP_NORMALIZATION" in dag["unchanged_downstream"]


def test_xm024_metrology_has_all_axes_and_no_protected_novelty() -> None:
    metrics = _load(METRICS)
    shadow = metrics["retained_semantic_novelty_proposal_shadow"]
    protected = metrics["retained_semantic_novelty_protected"]
    assert AXES <= set(shadow)
    assert AXES <= set(protected)
    assert {axis: protected[axis] for axis in AXES} == {axis: 0 for axis in AXES}
    assert metrics["memory"]["retrieved_count"] == 6
    assert metrics["memory"]["selected_count"] == 4
    assert metrics["memory"]["rejected_or_deferred_count"] == 2
    assert metrics["gate_provenance_ci"]["independent_mathematical_reviews"] == "0/3"
    assert metrics["state_fingerprints"]["raw_repository_growth_counts_as_learning"] is False


def test_cross_lane_case_study_covers_all_six_and_separates_observation_from_lesson() -> None:
    case = _load(CASE)
    lanes = case["lanes"]
    assert set(lanes) == {
        "p_vs_np",
        "riemann_hypothesis",
        "navier_stokes",
        "yang_mills",
        "hodge",
        "birch_swinnerton_dyer",
    }
    assert case["cross_lane_synthesis"]["recurring_process_pathology"] == "CONSUMER_SCOPE_UNIFORMITY_LOSS"
    assert case["cross_lane_synthesis"]["reusable_lesson_status"].startswith("PROPOSAL_ONLY")
    assert case["cross_lane_synthesis"]["framework_hypothesis"]["target"].startswith("RAKL issue #459")


def test_current_main_drift_is_append_only_and_updates_rh_bsd_metrology() -> None:
    drift = _load(CASE_DRIFT)
    correction = _load(METRICS_DRIFT)
    assert drift["preserves_original_snapshot"].endswith("XM024_RAKL_METHOD_CASE_STUDY_20260812.json")
    assert "riemann_hypothesis" in drift["lane_updates"]
    assert "birch_swinnerton_dyer" in drift["lane_updates"]
    assert drift["lane_updates"]["riemann_hypothesis"]["outcome"].startswith("PASS_SAME_CONTEXT_HAND_PROOF")
    assert drift["lane_updates"]["birch_swinnerton_dyer"]["novelty_seven_axes"]["PATH"] == 1
    agg = correction["corrections"]["cross_lane_retained_novelty_lower_bound"]
    assert {axis: agg[axis] for axis in AXES} == {
        "KNOWLEDGE": 5,
        "OPERATOR": 1,
        "EXPERIENCE_PATTERN": 2,
        "OBSTRUCTION": 3,
        "RELATION": 4,
        "PATH": 4,
        "META_METHOD": 0,
    }
    protected = correction["unchanged_xm024_retained_novelty_protected"]
    assert {axis: protected[axis] for axis in AXES} == {axis: 0 for axis in AXES}
    assert correction["raw_repository_growth_learning_credit"] == 0
