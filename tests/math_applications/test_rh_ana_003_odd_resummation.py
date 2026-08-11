from __future__ import annotations

from fractions import Fraction
from math import comb


def signed_binomial_piece(n: int, q: int) -> Fraction:
    return sum(
        ((-1) ** j) * comb(n, j) * Fraction(1, q**j)
        for j in range(2, n + 1)
    )


def resummed_piece(n: int, q: int) -> Fraction:
    return (Fraction(q - 1, q) ** n) - 1 + Fraction(n, q)


def absolute_value_surrogate(n: int, q: int) -> Fraction:
    return sum(
        comb(n, j) * Fraction(1, q**j)
        for j in range(2, n + 1)
    )


def test_exact_odd_integer_resummation_piecewise() -> None:
    for n in range(1, 15):
        for q in range(1, 32, 2):
            assert signed_binomial_piece(n, q) == resummed_piece(n, q)


def test_each_resummed_piece_is_nonnegative() -> None:
    for n in range(1, 30):
        for q in range(1, 64, 2):
            assert resummed_piece(n, q) >= 0


def test_boundary_sanity() -> None:
    assert resummed_piece(1, 1) == 0
    for q in range(1, 64, 2):
        assert resummed_piece(2, q) == Fraction(1, q * q)


def test_termwise_absolute_values_destroy_exact_cancellation() -> None:
    # This is a methodological regression check, not a theorem about asymptotic
    # sharpness.  It proves the unsigned surrogate is a different quantity and
    # can strictly exceed the exact signed term after cancellation.
    witnessed_strict_loss = False
    for n in range(3, 12):
        for q in range(3, 24, 2):
            signed = signed_binomial_piece(n, q)
            unsigned = absolute_value_surrogate(n, q)
            assert unsigned >= signed
            witnessed_strict_loss |= unsigned > signed
    assert witnessed_strict_loss
