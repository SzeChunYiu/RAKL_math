import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def test_weak_lorentz_union_exponent_is_two_thirds():
    p = 3 / 2
    assert math.isclose(1 / p, 2 / 3)
    for n in (1, 2, 8, 27):
        # Distribution bound: mu_union <= n*(A/s)^p, hence
        # s*mu_union^(1/p) <= n^(1/p)*A.
        assert math.isclose(n ** (1 / p), n ** (2 / 3))


def test_fixed_multiplicity_log_gain_vanishes():
    n0 = 17
    vals = [(n0 ** (2 / 3)) / math.log(lam) for lam in (1e4, 1e8, 1e16)]
    assert vals[0] > vals[1] > vals[2] > 0


def test_growth_guard_rejects_too_many_centers():
    # If N(lambda)=(log lambda)^2, then N^(2/3)/log lambda
    # grows like (log lambda)^(1/3), so fixed-N absorption logic cannot apply.
    lam1, lam2 = 1e8, 1e16
    q1 = (math.log(lam1) ** 2) ** (2 / 3) / math.log(lam1)
    q2 = (math.log(lam2) ** 2) ** (2 / 3) / math.log(lam2)
    assert q2 > q1


def test_shadow_episode_and_root_nonpromotion():
    episode = json.loads(
        (NS / "10_case_study" / "NS-B1a3b1b1_C001_R1_V3_TASK_EPISODE_20260811.json.shadow").read_text()
    )
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert episode["independent_review_credit"] == "0/3"


def test_context_lift_keeps_producer_residual_open():
    pack = json.loads(
        (NS / "07_memory" / "NS-B1a3b1b1_C001_R1_DERIVED_MEMORY_PACK_20260811.json").read_text()
    )
    assert pack["context_lift_record"]["loss"] == "N0^(2/3)"
    assert "PRODUCER" in pack["obstruction"]["failure_category"]
