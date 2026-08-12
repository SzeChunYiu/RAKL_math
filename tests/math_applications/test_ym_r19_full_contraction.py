"""Assurance-only hostile controls for YM-S1a2h R19.

These tests check elementary implications used in the source audit. They are not
mathematical proof, independent review, or Yang-Mills/root authority.
"""


def full_forward_lipschitz(op_norm: float, c_radius: float, kappa: float, a_radius: float) -> float:
    return max(op_norm + c_radius, kappa + a_radius)


def test_relevant_expansion_blocks_displayed_full_forward_contraction() -> None:
    lambda_rel = 1.1
    full_op_norm = lambda_rel  # cheapest case: full norm equals restriction lower bound
    lip = full_forward_lipschitz(full_op_norm, 0.0, 0.25, 0.0)
    assert lip >= lambda_rel > 1.0


def test_smaller_nonlinear_radius_cannot_remove_linear_expansion() -> None:
    lambda_rel = 1.0001
    for radius_correction in (0.0, 1e-12, 1e-8, 1e-4):
        lip = full_forward_lipschitz(lambda_rel, radius_correction, 0.1, 0.0)
        assert lip > 1.0


def test_irrelevant_contraction_does_not_imply_full_state_contraction() -> None:
    lambda_rel = 1.2
    kappa = 0.2
    lip = full_forward_lipschitz(lambda_rel, 0.0, kappa, 0.0)
    assert kappa < 1.0
    assert lip > 1.0
