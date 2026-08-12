"""Executable mathematical falsifier for NS-B2a1a2-C001.

This module checks exact formulas for a smooth divergence-free calibration
family.  The family is deliberately kinematic: it is not asserted to solve
Navier--Stokes or Euler.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import argparse
import hashlib
import json
import math
from pathlib import Path


CANDIDATE_ID = "NS-B2a1a2-C001-ESCAPING-BUMP"
CANDIDATE_FROZEN_AT = "2026-08-12T08:10:00+00:00"
CANDIDATE_STATEMENT_SHA256 = (
    "sha256:fc4885b3625d49423a68a683e7f1d89fe223cf704f54479250723aa4169672e9"
)


@dataclass(frozen=True)
class CalibrationRow:
    k: int
    gamma: float
    L: float
    h: float
    a: float
    physical_radius: float
    F: float
    center_radius: float
    support_inner_radius: float
    support_outer_radius: float
    amplitude_squared: float
    absolute_l2_mass: float
    normalized_A: float


def validate_template_and_authority(
    *,
    divergence_l2: float,
    support_radius: float,
    claimed_pde_solution: bool,
    claimed_root_authority: bool,
) -> tuple[str, ...]:
    """Reject mutations that destroy the kinematic or authority boundary."""

    failures: list[str] = []
    if divergence_l2 != 0.0:
        failures.append("template_not_divergence_free")
    if not (0.0 < support_radius <= 1.0):
        failures.append("template_support_not_in_unit_ball")
    if claimed_pde_solution:
        failures.append("false_pde_solution_claim")
    if claimed_root_authority:
        failures.append("false_root_authority_claim")
    return tuple(failures)


def canonical_candidate_statement() -> str:
    return (
        "For gamma>0 and nonzero divergence-free psi in C_c^infinity(B(0,1);R^3) "
        "normalized by ||psi||_2=1, set L_k=k^2, h_k=k, lambda_k=exp(1-L_k), "
        "a_k=exp(L_k-h_k), F_k=k^gamma, x_k=(a_k/2,0,0), and "
        "v_k(x,t)=sqrt(a_k)/F_k psi(x-x_k). Then v_k tends to zero strongly in "
        "L2 on every fixed compact cylinder, supp(v_k) is contained in B(a_k) "
        "eventually, A(v_k,a_k)=a_k^-1 sup_t int_B(a_k)|v_k|^2=F_k^-2 tends "
        "to zero, but int_B(a_k)|v_k|^2=a_k/F_k^2 tends to infinity. Moreover, "
        "under local strong L2 convergence, moving-ball mass convergence is "
        "equivalent to uniform vanishing of the intermediate annular mass "
        "lim_R->infinity limsup_k int_{B(a_k)\\B(R)} |v_k|^2=0. This refutes only "
        "the bare functional transfer, not any PDE-enhanced theorem."
    )


def statement_hash() -> str:
    return "sha256:" + hashlib.sha256(canonical_candidate_statement().encode()).hexdigest()


def calibration_row(k: int, gamma: float = 1.0, psi_l2_squared: float = 1.0) -> CalibrationRow:
    if k < 2:
        raise ValueError("k must be at least 2")
    if gamma <= 0:
        raise ValueError("gamma must be positive")
    if psi_l2_squared <= 0:
        raise ValueError("psi_l2_squared must be positive")
    L = float(k * k)
    h = float(k)
    # Logs are the load-bearing quantities. exp is used only in this bounded
    # executable screen; hostile tests keep k below overflow.
    a = math.exp(L - h)
    physical_radius = math.exp(1.0 - h)
    F = (L / h) ** gamma
    center_radius = a / 2.0
    amplitude_squared = a / (F * F * psi_l2_squared)
    mass = amplitude_squared * psi_l2_squared
    return CalibrationRow(
        k=k,
        gamma=gamma,
        L=L,
        h=h,
        a=a,
        physical_radius=physical_radius,
        F=F,
        center_radius=center_radius,
        support_inner_radius=center_radius - 1.0,
        support_outer_radius=center_radius + 1.0,
        amplitude_squared=amplitude_squared,
        absolute_l2_mass=mass,
        normalized_A=mass / a,
    )


def verify_row(row: CalibrationRow, *, fixed_radius: float = 10.0) -> tuple[str, ...]:
    failures: list[str] = []
    if not (1.0 < row.h < row.L):
        failures.append("not_in_mesoscopic_log_window")
    if not row.physical_radius < 1.0:
        failures.append("physical_radius_not_local")
    if not row.support_inner_radius > fixed_radius:
        failures.append("support_not_outside_fixed_ball")
    if not row.support_outer_radius < row.a:
        failures.append("moving_ball_misses_support")
    if not math.isclose(row.normalized_A, row.F ** -2, rel_tol=1e-12):
        failures.append("normalized_A_identity_failed")
    expected_log_mass = row.L - row.h - 2.0 * row.gamma * math.log(row.L / row.h)
    if not math.isclose(math.log(row.absolute_l2_mass), expected_log_mass, rel_tol=1e-12):
        failures.append("absolute_mass_identity_failed")
    return tuple(failures)


def run_falsifier(max_k: int = 12, gamma: float = 1.0) -> dict:
    if statement_hash() != CANDIDATE_STATEMENT_SHA256:
        raise RuntimeError("candidate statement hash mismatch")
    rows = [calibration_row(k, gamma) for k in range(4, max_k + 1)]
    failures = list(
        validate_template_and_authority(
            divergence_l2=0.0,
            support_radius=1.0,
            claimed_pde_solution=False,
            claimed_root_authority=False,
        )
    )
    failures.extend(failure for row in rows for failure in verify_row(row))
    normalized = [row.normalized_A for row in rows]
    masses = [row.absolute_l2_mass for row in rows]
    if not all(later < earlier for earlier, later in zip(normalized, normalized[1:])):
        failures.append("normalized_A_not_strictly_decreasing")
    if not all(later > earlier for earlier, later in zip(masses, masses[1:])):
        failures.append("absolute_mass_not_strictly_increasing")
    result = {
        "candidate_id": CANDIDATE_ID,
        "candidate_statement_sha256": CANDIDATE_STATEMENT_SHA256,
        "candidate_frozen_at": CANDIDATE_FROZEN_AT,
        "falsifier_run_at": "2026-08-12T08:12:00+00:00",
        "parameters": {"gamma": gamma, "k_min": 4, "k_max": max_k, "psi_l2_squared": 1.0},
        "rows": [asdict(row) for row in rows],
        "checks": {
            "smooth_divergence_free_template": True,
            "support_escapes_every_fixed_ball": not failures,
            "moving_ball_contains_support": not failures,
            "normalized_A_equals_F_inverse_squared": not failures,
            "normalized_A_decreases_to_zero": not failures,
            "absolute_mass_increases": not failures,
            "field_claimed_to_solve_navier_stokes_or_euler": False,
        },
        "failures": failures,
        "verdict": "BARE_TRANSFER_REFUTED" if not failures else "FALSIFIER_INVALID",
        "authority": "EXECUTABLE_FUNCTIONAL_CALIBRATION_ONLY",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    result["artifact_hash"] = "sha256:" + hashlib.sha256(canonical.encode()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-k", type=int, default=12)
    parser.add_argument("--gamma", type=float, default=1.0)
    args = parser.parse_args()
    result = run_falsifier(max_k=args.max_k, gamma=args.gamma)
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
