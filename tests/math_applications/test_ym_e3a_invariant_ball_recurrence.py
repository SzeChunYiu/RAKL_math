from __future__ import annotations


def step(x: float, rho: float, C: float) -> float:
    return rho * x + C * x * x


def test_literal_a10_bound_has_explicit_counterexample() -> None:
    rho = 0.5
    C = 1.0
    r = 2.0
    x = r
    x = step(x, rho, C)
    x = step(x, rho, C)
    claimed_n2 = (rho**2) * r + C * r * r / (1.0 - rho)
    assert x == 27.5
    assert claimed_n2 == 8.5
    assert x > claimed_n2


def test_strict_invariant_ball_gives_geometric_decay() -> None:
    rho = 0.5
    C = 1.0
    r_star = 0.25
    q = rho + C * r_star
    assert q == 0.75 < 1.0

    x0 = r_star
    x = x0
    for n in range(1, 21):
        x = step(x, rho, C)
        assert 0.0 <= x <= r_star
        assert x <= (q**n) * x0 + 1e-15


def test_sufficient_radius_choice_is_strict() -> None:
    for rho, C in [(0.1, 0.5), (0.5, 1.0), (0.9, 7.0)]:
        r_star = (1.0 - rho) / (2.0 * C)
        q = rho + C * r_star
        assert q == (1.0 + rho) / 2.0
        assert q < 1.0
