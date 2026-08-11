from fractions import Fraction
from pathlib import Path


CANDIDATE = Path("research/real_math/millennium/yang_mills/04_candidates/YM-E3a1_INVARIANT_BALL_RECURRENCE_REPAIR_20260811.md")
FAILURE = Path("research/real_math/millennium/yang_mills/03_dual_memory/failures/F_YM_E3A1_MAIN_5P11_N_BOUND_INVALID_20260811.json")
FIBRE = Path("research/real_math/millennium/yang_mills/10_case_study/YM-E3a1_FIBRE_RECEIPT_20260811T1939Z.json")


def test_printed_appendix_closure_condition_is_impossible_for_positive_inputs():
    C = Fraction(3, 2)
    r = Fraction(1, 7)
    assert 2 * C * r + C * r * r > 0


def test_main_equation_5_11_claimed_all_n_bound_has_exact_counterexample():
    rho = Fraction(1, 2)
    n = 4
    lhs = n * rho ** (n - 1)
    rhs = Fraction(1, 1 - rho) * rho ** (n - 1)
    assert lhs == Fraction(1, 2)
    assert rhs == Fraction(1, 4)
    assert lhs > rhs


def test_invariant_ball_contraction_exact_rational_control():
    rho = Fraction(1, 2)
    C = Fraction(1, 1)
    r_star = Fraction(1, 4)
    q = rho + C * r_star
    assert q == Fraction(3, 4) < 1

    x = r_star
    for n in range(12):
        assert x <= q ** n * r_star
        assert x <= r_star
        x = rho * x + C * x * x


def test_threshold_equality_can_have_nondecaying_fixed_point():
    rho = Fraction(1, 2)
    C = Fraction(1, 1)
    r_star = Fraction(1, 2)
    assert C * r_star == 1 - rho
    x = r_star
    for _ in range(8):
        x = rho * x + C * x * x
        assert x == r_star


def test_application_artifacts_preserve_non_escalation_boundary():
    candidate = CANDIDATE.read_text()
    failure = FAILURE.read_text()
    fibre = FIBRE.read_text()
    assert "PROPOSAL_SHADOW_LOCAL_MATHEMATICS_ONLY / ROOT_AUTHORITY_NONE" in candidate
    assert "SOURCE_SPECIFIC_FRD_ENTRY_AND_CONSTANT_BINDING_BLOCKED" in candidate
    assert '"authority": "PROPOSAL_SHADOW_ONLY"' in failure
    assert '"new_protected_obstruction_minted": false' in failure
    assert '"authority": "PROPOSAL_SHADOW_ONLY"' in fibre
    assert "THIS_RECEIPT_BINDS_VERIFICATION_ONLY" in fibre
