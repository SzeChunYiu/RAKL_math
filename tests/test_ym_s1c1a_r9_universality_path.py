"""R9 hostile controls for the YM-S1c1a universality path-length audit.

Proposal/shadow research test only. This validates an inference-form falsifier; it is
not a Yang--Mills proof or counterexample.
"""


def chain_length(xs):
    return sum(abs(b - a) for a, b in zip(xs, xs[1:]))


def test_fine_partition_does_not_shrink_total_endpoint_path_length():
    for n in (1, 2, 10, 100, 1000):
        xs = [j / n for j in range(n + 1)]
        assert abs(chain_length(xs) - 1.0) < 1e-12
        assert chain_length(xs) >= abs(xs[-1] - xs[0])


def test_lipschitz_control_does_not_imply_endpoint_equality():
    # K=[0,1], d=|.|, S(theta)=theta is exactly 1-Lipschitz.
    S = lambda theta: theta
    theta, theta_prime = 0.0, 1.0
    assert abs(S(theta) - S(theta_prime)) <= abs(theta - theta_prime)
    assert S(theta) != S(theta_prime)
