from __future__ import annotations

import math


def _op_norm_diagonal(entries: tuple[float, ...]) -> float:
    return max(abs(x) for x in entries)


def _conorm_diagonal(entries: tuple[float, ...]) -> float:
    return min(abs(x) for x in entries)


def test_operator_norm_lower_bound_does_not_imply_invertibility() -> None:
    entries = (2.0, 0.0)
    assert _op_norm_diagonal(entries) == 2.0
    assert _conorm_diagonal(entries) == 0.0


def test_operator_norm_lower_bound_does_not_imply_inverse_contraction() -> None:
    entries = (2.0, 0.5)
    assert _op_norm_diagonal(entries) == 2.0
    assert _conorm_diagonal(entries) == 0.5
    inverse_norm = 1.0 / _conorm_diagonal(entries)
    assert inverse_norm == 2.0
    assert inverse_norm > 1.0


def test_diagonal_dominance_conorm_repair_shape() -> None:
    # Elementary scalar version of m(D+M) >= m(D)-||M||.
    diagonal_minimum = 3.0
    correction_norm = 1.5
    lower_bound = diagonal_minimum - correction_norm
    assert lower_bound > 1.0
    assert 1.0 / lower_bound < 1.0
    assert math.isclose(1.0 / lower_bound, 2.0 / 3.0)
