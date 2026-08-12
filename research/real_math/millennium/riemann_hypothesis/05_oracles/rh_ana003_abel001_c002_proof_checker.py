#!/usr/bin/env python3
"""Record checker for the frozen C002 hand proof.

This checker verifies exact artifact identity, required proof obligations, and
several exact algebraic/finite hostile checks.  It does not replace a proof
assistant and it creates no independent-review or RH authority.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"
CERTIFICATE = BASE / "04_candidates/RH_ANA_003_ABEL_001_C002_HAND_PROOF_CERTIFICATE_FREEZE_20260812.json"
AUTHORIZATION = BASE / "09_trace/RH_ANA_003_ABEL_001_C002_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json"
PROOF_INPUT = BASE / "04_candidates/RH_ANA_003_ABEL_001_C002_PROOF_INPUT_FREEZE_20260812.json"


def raw_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def laguerre_coefficients(n: int) -> list[Fraction]:
    """Coefficients of L_(n-1)^(1)(u), low degree first."""
    from math import comb, factorial

    return [Fraction((-1) ** j * comb(n, j + 1), factorial(j)) for j in range(n)]


def derivative_difference(coefficients: list[Fraction]) -> list[Fraction]:
    derivative = [Fraction(0)] * len(coefficients)
    for j in range(1, len(coefficients)):
        derivative[j - 1] = j * coefficients[j]
    return [derivative[j] - coefficients[j] for j in range(len(coefficients))]


def finite_abel_check(a: dict[int, Fraction], x: Fraction, y: Fraction) -> bool:
    def b(t: Fraction) -> Fraction:
        return t * t + 2 * t + 1

    def integral_a_bprime(left: Fraction, right: Fraction) -> Fraction:
        # A(t) is constant on each interval between integer jumps.
        total = Fraction(0)
        cuts = [left] + [Fraction(m) for m in range(1, int(right) + 1) if left < m < right] + [right]
        for lo, hi in zip(cuts, cuts[1:]):
            cumulative = sum((value for m, value in a.items() if m <= lo), Fraction(0))
            total += cumulative * (b(hi) - b(lo))
        return total

    def cumulative(t: Fraction) -> Fraction:
        return sum((value for m, value in a.items() if m <= t), Fraction(0))

    lhs = sum((value * b(Fraction(m)) for m, value in a.items() if x < m <= y), Fraction(0))
    rhs = cumulative(y) * b(y) - cumulative(x) * b(x) - integral_a_bprime(x, y)
    return lhs == rhs


def evaluate() -> dict:
    certificate = load(CERTIFICATE)
    authorization = load(AUTHORIZATION)
    proof_input = load(PROOF_INPUT)

    if raw_sha256(PROOF_INPUT) != certificate["proof_input_raw_sha256"]:
        raise ValueError("proof-input identity mismatch")
    if certificate["artifact_hash"] != authorization["certificate_artifact_hash"]:
        raise ValueError("certificate authorization mismatch")
    if authorization["proof_check_authorized"] is not True:
        raise ValueError("proof check not authorized")
    if authorization["requires_public_freeze_commit"] is not True:
        raise ValueError("public-freeze chronology condition missing")

    obligations = certificate["obligations"]
    required = {f"O{i}" for i in range(1, 8)}
    observed = {row["obligation_id"].split("-")[0] for row in obligations}
    if observed != required or any(row["status"] != "PROVED_IN_FROZEN_HAND_CERTIFICATE" for row in obligations):
        raise ValueError("incomplete hand-proof obligation set")

    # Exact coefficient checks across low and moderate n, including hostile n=1.
    coefficient_checks = []
    for n in range(1, 17):
        p = laguerre_coefficients(n)
        q = derivative_difference(p)
        expected = Fraction((-1) ** n, 1)
        from math import factorial
        expected /= factorial(n - 1)
        if q[-1] != expected:
            raise ValueError(f"leading coefficient mismatch at n={n}")
        coefficient_checks.append({"n": n, "degree": n - 1, "leading": str(q[-1])})

    endpoint_worlds = [
        ({1: Fraction(2), 2: Fraction(-3), 4: Fraction(5)}, Fraction(1, 2), Fraction(9, 2)),
        ({1: Fraction(-1), 3: Fraction(7), 5: Fraction(2)}, Fraction(3, 2), Fraction(11, 2)),
    ]
    if not all(finite_abel_check(*world) for world in endpoint_worlds):
        raise ValueError("finite Abel endpoint hostile check failed")

    if any((6 * k) % 2 or (6 * k) % 3 for k in range(1, 101)):
        raise ValueError("6k arithmetic witness check failed")

    if proof_input["status"] != "FROZEN_UNEVALUATED":
        raise ValueError("frozen proof-input state changed")

    return {
        "status": "PASS",
        "verdict": "ALL_O1_O7_SUPPORTED_BY_FROZEN_HAND_PROOF",
        "candidate_id": certificate["candidate_id"],
        "candidate_core_sha256": certificate["candidate_core_sha256"],
        "proof_input_raw_sha256": certificate["proof_input_raw_sha256"],
        "obligations_checked": 7,
        "exact_laguerre_coefficient_worlds": coefficient_checks,
        "finite_abel_hostile_worlds": len(endpoint_worlds),
        "six_k_sample_worlds": 100,
        "authority": "RECORD_AND_EXACT_ALGEBRA_CHECK_ONLY_HAND_PROOF_SUPPLIES_MATHEMATICS",
    }


def main() -> None:
    output = evaluate()
    sys.stdout.write(json.dumps(output, sort_keys=True, separators=(",", ":")) + "\n")


if __name__ == "__main__":
    main()
