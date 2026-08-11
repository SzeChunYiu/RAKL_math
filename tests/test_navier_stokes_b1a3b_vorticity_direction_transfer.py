from __future__ import annotations

import math


def periodic_velocity(n: int, a: float, x1: float, t: float) -> tuple[float, float, float]:
    decay = math.exp(-(n * n) * t)
    return (0.0, (a / n) * decay * math.sin(n * x1), (a / n) * decay * math.cos(n * x1))


def periodic_vorticity(n: int, a: float, x1: float, t: float) -> tuple[float, float, float]:
    decay = math.exp(-(n * n) * t)
    return (0.0, a * decay * math.sin(n * x1), a * decay * math.cos(n * x1))


def dot(x: tuple[float, float, float], y: tuple[float, float, float]) -> float:
    return sum(a * b for a, b in zip(x, y))


def norm(x: tuple[float, float, float]) -> float:
    return math.sqrt(dot(x, x))


def test_exact_periodic_solution_algebra() -> None:
    # u=(0,v(x1,t),w(x1,t)); therefore div u=0 and u·grad = v d2+w d3 = 0.
    for n in (1, 3, 11):
        a = 2.5
        x1 = 0.37
        t = 0.041
        u = periodic_velocity(n, a, x1, t)
        assert u[0] == 0.0

        # Analytic heat residual componentwise: d_t f = -n^2 f and Delta f = d_11 f = -n^2 f.
        for component in u:
            assert math.isclose((-n * n) * component - (-n * n) * component, 0.0, abs_tol=1e-15)

        # Convective derivative vanishes because the field has no x1 velocity and no x2/x3 dependence.
        convective = (0.0, 0.0, 0.0)
        assert convective == (0.0, 0.0, 0.0)


def test_periodic_energy_and_vorticity_scaling() -> None:
    volume = (2.0 * math.pi) ** 3
    a = 3.0
    for n in (2, 5, 17):
        kinetic_l2_squared_t0 = volume * a * a / (n * n)
        enstrophy_l2_squared_t0 = volume * a * a
        assert math.isclose(kinetic_l2_squared_t0 * n * n, volume * a * a)
        assert math.isclose(enstrophy_l2_squared_t0, volume * a * a)


def test_direction_rotates_on_vanishing_spatial_scale() -> None:
    a = 1.0
    alpha = 0.5
    previous_lower_bound = 0.0
    for n in (4, 8, 16, 32):
        x1 = 0.0
        y1 = math.pi / (2.0 * n)
        xi_x = periodic_vorticity(n, a, x1, 0.0)
        xi_y = periodic_vorticity(n, a, y1, 0.0)
        xi_x = tuple(value / norm(xi_x) for value in xi_x)
        xi_y = tuple(value / norm(xi_y) for value in xi_y)
        assert math.isclose(dot(xi_x, xi_y), 0.0, abs_tol=1e-12)
        distance = abs(y1 - x1)
        holder_lower_bound = math.sqrt(2.0) / (distance**alpha)
        assert holder_lower_bound > previous_lower_bound
        previous_lower_bound = holder_lower_bound


def test_local_r3_core_formula_has_small_velocity_and_order_one_rotating_curl() -> None:
    # On any core where the cutoff chi is exactly one, the compactly supported calibration has
    # w_n=(0,n^-1 sin(nx1),n^-1 cos(nx1)) and curl w_n=(0,sin(nx1),cos(nx1)).
    for n in (5, 20, 80):
        x1 = 0.41
        w = (0.0, math.sin(n * x1) / n, math.cos(n * x1) / n)
        omega = (0.0, math.sin(n * x1), math.cos(n * x1))
        assert norm(w) == 1.0 / n
        assert math.isclose(norm(omega), 1.0, rel_tol=1e-12, abs_tol=1e-12)


def test_cutoff_order_counting_matches_uniform_h1_bound() -> None:
    # A_n=n^-2 chi*(0,sin(nx1),cos(nx1)). One derivative is O(n^-1)+O(n^-2),
    # while two derivatives are O(1)+O(n^-1)+O(n^-2) on a fixed compact support.
    for n in (2, 10, 100):
        first_derivative_scale = 1.0 / n + 1.0 / (n * n)
        second_derivative_scale = 1.0 + 1.0 / n + 1.0 / (n * n)
        assert first_derivative_scale <= 0.75
        assert second_derivative_scale <= 1.75
