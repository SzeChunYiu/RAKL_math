import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def test_unit_viscosity_coefficient_matching():
    # Source: V_t + V.grad V - nu Delta V + grad P = 0.
    # Target: W=c V(alpha z,beta s) solves viscosity-one NSE.
    # Cancellation after substituting the source PDE requires
    # beta=c*alpha and beta*nu=alpha**2.
    for alpha, nu in [(1.0, 0.25), (2.0, 0.04), (0.5, 0.01)]:
        c = alpha / nu
        beta = alpha**2 / nu
        assert c * alpha / beta == 1.0
        assert beta * nu / alpha**2 == 1.0


def test_maximal_target_cylinder_and_alpha_invariance():
    # Q_W(r) maps to spatial radius alpha*r and source time depth beta*r**2.
    # The source Q_V(a) permits r=a*sqrt(nu)/alpha.  The induced A/E/D
    # prefactors are independent of alpha at this maximal lawful radius.
    for alpha, nu, a in [(1.0, 0.25, 3.0), (2.0, 0.04, 5.0), (0.5, 0.01, 2.0)]:
        c = alpha / nu
        beta = alpha**2 / nu
        r = a * nu**0.5 / alpha
        assert alpha * r <= a
        assert abs(beta * r**2 - a**2) < 1e-12
        a_prefactor = c**2 * alpha**-3 * (a / r)
        e_prefactor = (c * alpha)**2 * alpha**-3 / beta * (a / r)
        d_prefactor = c**3 * alpha**-3 / beta * (a**2 / r**2)
        assert abs(a_prefactor - nu**-2.5) / nu**-2.5 < 1e-12
        assert abs(e_prefactor - nu**-1.5) / nu**-1.5 < 1e-12
        assert abs(d_prefactor - nu**-3.0) / nu**-3.0 < 1e-12


def test_certificate_exponent_floors():
    # With F<=nu^-1, exponent arithmetic for the derived upper-bound expressions is exact.
    assert -2.5 + 2.0 == -0.5      # A: nu^-5/2 * F^-2
    assert -1.5 + 1.0 == -0.5      # E: nu^-3/2 * F^-1
    assert -3.0 + 2.0 == -1.0      # D: nu^-3 * F^-2
    assert -3.0 + 9.0 / 4.0 == -3.0 / 4.0  # leading C term


def test_shadow_authority_and_root_remain_open():
    episode = json.loads((NS / "07_memory" / "NS-B2a1a2_TASK_EPISODE_R1_20260812.json").read_text())
    delta = json.loads((NS / "02_problem_dag" / "NS_B2A1A2_R1_DELTA_20260812.json").read_text())
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"].endswith("DIRECT_CKN_BRIDGE_ESTIMATE_INSUFFICIENT")
    assert delta["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert delta["root_promotion"] == "NONE"
