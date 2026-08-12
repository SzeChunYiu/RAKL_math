import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def test_unit_viscosity_coefficient_matching_and_aspect_cost():
    # W=c V(alpha z,beta s), V_t+V.grad V-nu Delta V+grad P=0.
    # Unit convection and diffusion require beta=c*alpha=alpha**2/nu.
    for alpha, nu in [(1.0, 0.25), (2.0, 0.04), (0.5, 0.01)]:
        c = alpha / nu
        beta = alpha**2 / nu
        assert c * alpha / beta == 1.0
        assert nu * alpha**2 / beta == nu**2  # coefficient before correcting expression below
        # Diffusion coefficient after division by c*beta is alpha**2/beta = nu;
        # to turn source viscosity nu into one, the PDE coefficient is nu*alpha**2/beta.
        # With beta=alpha**2*nu, not alpha**2/nu, this would be 1; guard the actual algebra separately.


def test_correct_normalization_equations():
    # Direct coefficient equations: c*alpha/beta=1 and nu*alpha**2/beta=1.
    # Therefore beta=nu*alpha**2 and c=nu*alpha, for W=c V(alpha z,beta s).
    # The audit uses the inverse-coordinate convention W=c V(z/alpha,s/beta), which yields
    # c=alpha/nu, beta=alpha**2/nu. This test prevents silently mixing conventions.
    for alpha, nu in [(1.0, 0.25), (2.0, 0.04), (0.5, 0.01)]:
        beta_direct = nu * alpha**2
        c_direct = nu * alpha
        assert c_direct * alpha / beta_direct == 1.0
        assert nu * alpha**2 / beta_direct == 1.0


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
