from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction


def quartet_contribution(beta: float, gamma: float, n: int) -> float:
    rho = complex(beta, gamma)
    z = 1 - 1 / rho
    return 4.0 - 2.0 * (z**n + z ** (-n)).real


def main() -> None:
    beta = Fraction(1, 4)
    gamma = 100
    modulus_sq = Fraction(1, 1) + (1 - 2 * beta) / (beta * beta + gamma * gamma)

    rho = complex(float(beta), gamma)
    z = 1 - 1 / rho
    radius = abs(z)
    theta = cmath.phase(z)

    witness_n = None
    witness = None
    for n in range(500_000, 600_001):
        cosine = math.cos(n * theta)
        if cosine <= 0.99:
            continue
        value = quartet_contribution(float(beta), gamma, n)
        scale = math.sqrt(n) * math.log(n)
        ratio = abs(value) / scale
        if ratio > 100:
            witness_n = n
            witness = {
                "cos_n_theta": cosine,
                "quartet_contribution": value,
                "sqrt_n_log_n": scale,
                "absolute_ratio": ratio,
            }
            break

    output = {
        "calibration_id": "CAL-RH-ANA-003-DENSITY-RADIAL-OUTLIER",
        "beta": f"{beta.numerator}/{beta.denominator}",
        "gamma": gamma,
        "modulus_squared_exact": f"{modulus_sq.numerator}/{modulus_sq.denominator}",
        "modulus_squared_gt_one": modulus_sq > 1,
        "radius": radius,
        "witness_n": witness_n,
        "witness": witness,
        "authority": "KNOWN_ANSWER_NUMERICAL_CALIBRATION_ONLY",
        "root_authority": "NONE",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
