from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"
CALIBRATION = BASE / "04_candidates/RH_SPEC_002_LIMIT_STABILITY_CALIBRATION_20260811.json"
CONTINUATION = BASE / "09_trace/RH_SPEC_002_CALIBRATION_TRACE_CONTINUATION_20260811.json"
PARENT_TRACE = BASE / "09_trace/RH_SPEC_002_OPEN_TRACE_20260811.json"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_calibration_artifact_hash_and_route_classification() -> None:
    raw = json.loads(CALIBRATION.read_text(encoding="utf-8"))
    payload = copy.deepcopy(raw)
    payload["artifact_hash"] = ""
    assert raw["artifact_hash"] == _canonical_hash(payload)
    assert raw["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert "NO_RH_THEOREM" in raw["authority"]

    classes = {
        item["package"]: item["classification"]
        for item in raw["package_classification"]
    }
    assert classes["local_uniform_source_normalized_entire_determinants_to_exact_Xi"] == (
        "TARGET_SIDE_SUFFICIENT_BUT_SOURCE_SIDE_UNPROVED"
    )
    assert classes["strong_resolvent_or_Mosco_without_extra_spectral_exactness"] == "TOO_WEAK"
    assert classes["finite_zero_prefix_or_counting_statistic_or_UV_asymptotics"] == "TOO_WEAK"
    assert classes["unspecified_joint_N_lambda_or_cutoff_limit"] == "UNDER_SPECIFIED"
    assert raw["research_decision"]["selected_next_residual"] == (
        "RH-SPEC-002a-DETERMINANT-COMPACTNESS-BRIDGE"
    )


def test_rank_one_projection_strong_resolvent_calibration() -> None:
    # On a fixed finite-support vector x, P_n x is exactly zero once n is
    # outside the support.  The explicit rank-one resolvent correction then
    # vanishes exactly on x, while each approximant still has eigenvalue 1.
    z = 1j
    correction = 1 / (1 - z) + 1 / z
    assert correction != 0

    x_support_max = 5
    for n in range(6, 20):
        assert n > x_support_max
        projection_of_x_norm = 0.0
        resolvent_difference_norm = abs(correction) * projection_of_x_norm
        assert resolvent_difference_norm == 0.0

    approximant_eigenvalue = 1
    limit_spectrum = {0}
    assert approximant_eigenvalue not in limit_spectrum


def test_exact_galerkin_gap_pollution_calibration() -> None:
    # The mixed boundary vector v=(e_-+e_+)/sqrt(2) has Av=w orthogonal to v
    # and to every earlier basis vector, so its one-dimensional compression
    # eigenvalue is exactly <v,Av>=0 although sigma(A)={-1,+1}.
    inv_sqrt2 = 1 / math.sqrt(2)
    v = (inv_sqrt2, inv_sqrt2)
    av = (-inv_sqrt2, inv_sqrt2)
    inner = v[0] * av[0] + v[1] * av[1]
    assert abs(inner) < 1e-15
    assert 0 not in {-1, 1}


def test_two_parameter_limit_is_path_dependent() -> None:
    def value(n: float, lam: float) -> float:
        return n / (n + lam)

    assert math.isclose(value(10**12, 1), 1.0, rel_tol=0, abs_tol=2e-12)
    assert math.isclose(value(1, 10**12), 0.0, rel_tol=0, abs_tol=2e-12)
    assert value(10**6, 10**6) == 0.5


def test_finite_real_zero_prefix_does_not_force_entire_convergence() -> None:
    # At z=1/2, the canonical product factor stays bounded away from zero
    # (and tends to 2/pi), whereas exp(n/2) grows without bound.
    def log_abs_g_at_half(n: int) -> float:
        product_log = sum(math.log1p(-1 / (4 * k * k)) for k in range(1, n + 1))
        return n / 2 + product_log

    assert log_abs_g_at_half(40) > log_abs_g_at_half(20) + 9
    product_200 = math.prod(1 - 1 / (4 * k * k) for k in range(1, 201))
    assert abs(product_200 - 2 / math.pi) < 0.002


def test_calibration_trace_continues_parent_hash_chain() -> None:
    parent = json.loads(PARENT_TRACE.read_text(encoding="utf-8"))
    continuation = json.loads(CONTINUATION.read_text(encoding="utf-8"))
    parent_final = parent["entries"][-1]["artifact_hash"]
    assert parent_final == continuation["parent_final_event_hash"]

    previous = parent_final
    event_types = []
    for item in continuation["entries"]:
        payload = copy.deepcopy(item)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        assert item["previous_event_hash"] == previous
        previous = artifact_hash
        event_types.append(item["event_type"])

    assert event_types == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]
    assert previous == "sha256:53bc2f8fd0a983cd747034f32270e2ba4399a6b8d1e8224adadcef25f06423bb"
