from fractions import Fraction


def telescoping_lower_bound(delta0, defects):
    return delta0 - sum(defects, start=Fraction(0, 1))


def geometric_total_bound(C, theta):
    assert Fraction(0, 1) <= theta < Fraction(1, 1)
    return C / (Fraction(1, 1) - theta)


def superexp_certificate_term(q, c, b, k):
    """Exact rational analogue q^(floor(c*b^k)) for integer c,b,k.

    This is only a structural calibration of the first-term/tail dependence in
    the displayed source envelope; it is not numerical evidence for Yang-Mills.
    """
    return q ** (c * (b**k))


def test_summability_alone_does_not_force_positive_margin():
    delta0 = Fraction(1, 1)
    defects = [Fraction(3, 5), Fraction(3, 5)]
    assert sum(defects) < float("inf")
    assert telescoping_lower_bound(delta0, defects) == Fraction(-1, 5)


def test_geometric_envelope_requires_relative_constant_certificate():
    delta0 = Fraction(1, 1)
    C = Fraction(1, 1)
    theta = Fraction(1, 2)
    assert geometric_total_bound(C, theta) == Fraction(2, 1)
    assert not geometric_total_bound(C, theta) < delta0


def test_large_block_factor_does_not_change_displayed_k0_certificate():
    q = Fraction(1, 2)
    c = 2
    assert superexp_certificate_term(q, c, 2, 0) == Fraction(1, 4)
    assert superexp_certificate_term(q, c, 100, 0) == Fraction(1, 4)
    assert superexp_certificate_term(q, c, 100, 1) < superexp_certificate_term(q, c, 2, 1)
