import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1c1a1_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260811_R9.json"
SOURCE = ROOT / "research/real_math/millennium/yang_mills/00_sources/YM-S1c1a1_AFIR_VANISHING_ENDPOINT_AUDIT_20260811_R9.md"


def test_additive_summable_defect_does_not_force_vanishing():
    # Exact hostile control for d_{k+1} <= d_k + C epsilon_k.
    c = 7.0
    d = [1.0] * 8
    eps = [0.0] * 7
    assert all(d[k + 1] <= d[k] + c * eps[k] for k in range(7))
    assert sum(eps) == 0.0
    assert d[-1] == 1.0


def test_endpoint_distance_lower_bounds_path_length():
    # A path between fixed metric endpoints at distance 1 cannot have length < 1/2.
    endpoint_distance = 1.0
    claimed_length = 0.5
    assert endpoint_distance > claimed_length
    assert not (endpoint_distance <= claimed_length)


def test_r9_packet_preserves_authority_and_zero_protected_novelty():
    packet = json.loads(CASE.read_text())
    assert packet["authority"] == "PROPOSAL_SHADOW_MEASUREMENT_ONLY_ROOT_AUTHORITY_NONE"
    metrics = packet["RAKL_CYCLE_METRICS"]
    assert metrics["gate_provenance_ci"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["independent_mathematical_reviews"] == "0/3"
    assert all(v == 0 for v in metrics["protected_retained_semantic_novelty"].values())
    assert metrics["residual_after"] == "RES-YM-S1c1a2-ENDPOINT-PRESERVING-VANISHING-AFIR-ANCHOR-OR-STRICT-CONTRACTION-SAME-OS-THEORY"


def test_source_audit_binds_bounded_vs_vanishing_and_endpoint_preservation():
    text = SOURCE.read_text()
    assert "Theorem 10.8 proves bounded discrepancy, not vanishing discrepancy" in text
    assert "Lemma F.10's arbitrary-short-path claim conflicts with endpoint distance" in text
    assert "tail-only modified path" in text
    assert "No Yang–Mills theorem" in text
