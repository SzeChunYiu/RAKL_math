import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research/real_math/millennium/yang_mills/00_sources/YM-S1c1a2_K_COORDINATE_NORMAL_FORM_AUDIT_20260812_R10.md"
FIBRE = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1c1a2_FIBRE_RECEIPT_20260812_R10.json"
CASE = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1c1a2_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260812_R10.json"


def test_additive_forcing_has_nonzero_slaved_g2_graph():
    # Scalar hostile control for K_{k+1}=q K_k + c g_k^2.
    q = 0.5
    c = 3.0
    a = c / (1.0 - q)
    assert a == 6.0
    # K=A g^2 cancels the order-g^2 forcing only after subtracting the graph.
    assert abs(q * a + c - a) < 1e-12


def test_slaved_piece_can_shift_cubic_beta_coefficient_without_cancellation():
    beta = 11.0
    mixed = 2.0
    q = 0.5
    forcing = 3.0
    a = forcing / (1.0 - q)
    effective_beta = beta - mixed * a
    # The source-shaped O(g K) term is O(g^3) on K=A g^2.
    assert effective_beta != beta


def test_source_audit_keeps_local_and_gluing_failures_separate():
    text = SOURCE.read_text()
    assert "additive `O(g^2)` forcing" in text
    assert "no new `O(g^3)` term" in text
    assert "local mathematical/source-representation failure" in text
    assert "local-to-global gluing failure" in text
    assert "PROPOSAL_SHADOW_ONLY" in text


def test_fibre_is_frozen_before_repair_candidate_authority():
    text = FIBRE.read_text()
    assert "PROPOSAL_SHADOW_ONLY_ROOT_AUTHORITY_NONE" in text
    assert "The repair candidate itself is not authorized until this receipt is committed" in text
    assert "YM-S1c1a2a-IRRELEVANT-COORDINATE-FORCING-NORMAL-FORM-CONSISTENCY" in text


def test_r10_metrics_preserve_shadow_authority_and_zero_protected_novelty():
    packet = json.loads(CASE.read_text())
    assert packet["authority"] == "PROPOSAL_SHADOW_MEASUREMENT_ONLY_ROOT_AUTHORITY_NONE"
    metrics = packet["RAKL_CYCLE_METRICS"]
    assert metrics["gate_provenance_ci"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["independent_mathematical_reviews"] == "0/3"
    assert all(v == 0 for v in metrics["protected_retained_semantic_novelty"].values())
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 1,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["residual_after"] == "RES-YM-S1c1a2b-SLAVING-NORMAL-FORM-PLUS-MARGINAL-CANCELLATION-AND-SAME-OS-KERNEL-TRANSPORT"
    assert packet["episode_diagnosis_obstruction_lesson"]["lesson_status"] == "NO_LESSON_MINTED"
