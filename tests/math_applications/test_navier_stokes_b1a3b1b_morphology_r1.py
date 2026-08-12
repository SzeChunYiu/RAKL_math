from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def test_weak_l32_two_copy_scaling_is_r_independent():
    # Analytic calibration of lambda*(2 r^3 mu_0(lambda r^2))^(2/3)
    # after s=lambda*r^2. This is not a proof substitute; the proof is in the artifact.
    for r in (1e-1, 1e-2, 1e-3):
        scale_factor = (r ** -2) * ((2 * r**3) ** (2 / 3))
        assert math.isclose(scale_factor, 2 ** (2 / 3), rel_tol=1e-12, abs_tol=1e-12)


def test_one_center_radius_bound_can_be_forced_below_core_separation():
    L = 3.0
    C = 10.0
    r = L / (4 * C * math.sqrt(2))
    allowed_radius = C * math.sqrt(2) * r
    required_radius = L
    assert allowed_radius < required_radius


def test_task_episode_is_shadow_and_root_stays_open():
    episode = json.loads(
        (NS / "10_case_study" / "NS-B1a3b1b_C001_R1_V3_TASK_EPISODE_20260811.json.shadow").read_text()
    )
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["artifact_hash"] == "c93b41ea48d6bc4890245d2fe5cc4ce00b4d3b9e2f4d0343e9d72625c103b280"

    dag = (NS / "02_problem_dag" / "NS_B1a3b1b_C001_R1_DELTA_20260811.yaml").read_text()
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in dag
    assert "ROOT_AUTHORITY" not in dag or "NONE" in dag


def test_local_and_gluing_failures_are_separate():
    failures = json.loads(
        (NS / "07_memory" / "NS-B1a3b1b_C001_R1_FAILURE_EXPERIENCE_20260811.json").read_text()
    )["failures"]
    categories = {item["category"] for item in failures}
    assert "LOCAL_MATHEMATICAL_REPRESENTATION_FAILURE" in categories
    assert "LOCAL_TO_GLOBAL_GLUING_FAILURE" in categories


def test_preaction_binding_hashes_match_frozen_fibre():
    receipt = json.loads(
        (NS / "09_trace" / "NS-B1a3b1b_PRE_ACTION_RECEIPT_R1_20260811.json").read_text()
    )
    fibre = json.loads(
        (NS / "09_trace" / "NS-B1a3b1b_FIBRE_SNAPSHOT_R1_20260811.json").read_text()
    )
    assert receipt["framework_commit"] == "3863b4814e0020e72c8681727357eda1aab7bf2b"
    assert receipt["fibre_snapshot_hash"] == fibre["snapshot_hash"]
    assert receipt["receipt_canonical_sha256"] == "600be22b2b3644cce725a3a4a9811d739cafd2bcf11e1ddab17d89204d06cafb"
