"""Assurance-only scalar controls for YM-S1a2k R23.

These tests reproduce elementary finite-dimensional witnesses used by the
proposal/shadow source audit. Passing tests carry no theorem/root authority.
"""

from fractions import Fraction


def inf_norm_2x2(a, b, c, d):
    return max(abs(a) + abs(b), abs(c) + abs(d))


def test_similarity_can_destroy_inverse_norm_contraction_without_condition_control():
    # L = diag(2, 3), so ||L^-1||_inf = 1/2.
    l_inv_norm = inf_norm_2x2(Fraction(1, 2), 0, 0, Fraction(1, 3))
    assert l_inv_norm == Fraction(1, 2)

    # J = [[1,M],[0,1]], A = J L J^-1 = [[2,M],[0,3]].
    # Hence A^-1 = [[1/2,-M/6],[0,1/3]].
    m = 4
    a_inv_norm = inf_norm_2x2(
        Fraction(1, 2), Fraction(-m, 6), 0, Fraction(1, 3)
    )
    assert a_inv_norm == Fraction(7, 6)
    assert a_inv_norm > 1


def test_graph_over_irrelevant_data_does_not_imply_unique_irrelevant_data_for_g():
    # Toy stable set M={(g, lambda, K): lambda=0}. For each (g,K), lambda is
    # uniquely tuned, but for fixed g there are many K values. This witnesses
    # the logical gap between a graph over stable/irrelevant data and a
    # one-parameter graph g -> (lambda,K).
    g = Fraction(1, 10)
    stable_points_same_g = [(g, 0, Fraction(k, 10)) for k in (0, 1, 2)]
    assert all(point[0] == g and point[1] == 0 for point in stable_points_same_g)
    assert len({point[2] for point in stable_points_same_g}) == 3
