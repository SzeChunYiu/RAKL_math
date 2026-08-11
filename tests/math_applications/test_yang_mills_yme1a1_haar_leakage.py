from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"


def _matmul(a: tuple[tuple[int, ...], ...], b: tuple[tuple[int, ...], ...]):
    n = len(a)
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def _trace(a: tuple[tuple[int, ...], ...]) -> int:
    return sum(a[i][i] for i in range(len(a)))


def _haar_u_udag_trace_contraction(
    a: tuple[tuple[int, ...], ...],
    b: tuple[tuple[int, ...], ...],
) -> Fraction:
    """Index-expand int Tr(AU) Tr(U†B) dU using first Schur orthogonality."""
    n = len(a)
    total = Fraction(0)
    # Tr(AU)=sum_ij A_ij U_ji
    # Tr(U†B)=sum_lk conj(U_lk) B_lk
    # int U_ji conj(U_lk)dU = delta_jl delta_ik / N.
    for i in range(n):
        for j in range(n):
            for l in range(n):
                for k in range(n):
                    if j == l and i == k:
                        total += Fraction(a[i][j] * b[l][k], n)
    return total


def _canonical_hash(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_exact_local_haar_contraction_generates_concatenated_trace() -> None:
    p = (
        (0, 1, 0),
        (0, 0, 1),
        (1, 0, 0),
    )
    p2 = _matmul(p, p)
    ident = _matmul(p, p2)

    assert _trace(p) == 0
    assert _trace(p2) == 0
    assert _trace(_matmul(p, p)) == 0
    assert _trace(ident) == 3

    contraction_pp = _haar_u_udag_trace_contraction(p, p)
    contraction_pp2 = _haar_u_udag_trace_contraction(p, p2)

    assert contraction_pp == Fraction(_trace(_matmul(p, p)), 3) == 0
    assert contraction_pp2 == Fraction(_trace(ident), 3) == 1

    # Re Tr(U†B) supplies one half of this U-U† contraction.
    assert Fraction(1, 2) * contraction_pp == 0
    assert Fraction(1, 2) * contraction_pp2 == Fraction(1, 2)


def test_center_invariance_kills_two_u_contraction_for_registered_scope() -> None:
    # For a primitive Nth central root z, z^2=1 iff N divides 2.
    # Thus the two-U integral can be nonzero by this channel for N=1,2,
    # while every registered N>=3 candidate has z^2 != 1.
    assert all(2 % n != 0 for n in range(3, 12))


def test_failure_record_and_post_candidate_trace_are_hash_bound_and_scoped() -> None:
    failure_path = (
        BASE / "07_memory/YM_E1a1_C001_FAILURE_EXPERIENCE_DELTA_20260811.json"
    )
    failure_delta = json.loads(failure_path.read_text(encoding="utf-8"))
    failure = failure_delta["experience"]

    assert failure["diagnosis_status"] == "SUPPORTED"
    assert failure["candidate_id"] == "YM-E1a1-C001"
    assert "gauge group SU(N) with N>=3" in failure["scope_conditions"]
    assert failure_delta["links"][0]["relation"] == "SHARES_BROKEN_ASSUMPTION_WITH"

    failure_for_hash = copy.deepcopy(failure)
    digest = failure_for_hash["artifact_hash"]
    failure_for_hash["artifact_hash"] = ""
    assert digest == _canonical_hash(failure_for_hash)

    pre = json.loads(
        (BASE / "09_trace/YM_E1a1_PRE_CANDIDATE_TRACE_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    post = json.loads(
        (BASE / "09_trace/YM_E1a1_POST_CANDIDATE_TRACE_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    expected_previous = pre["entries"][-1]["artifact_hash"]
    assert post["entries"][0]["previous_event_hash"] == expected_previous

    previous = expected_previous
    for event in post["entries"]:
        assert event["previous_event_hash"] == previous
        event_for_hash = copy.deepcopy(event)
        digest = event_for_hash["artifact_hash"]
        event_for_hash["artifact_hash"] = ""
        assert digest == _canonical_hash(event_for_hash)
        previous = digest

    assert [event["event_type"] for event in post["entries"]] == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
        "REVIEWED",
    ]


def test_candidate_document_keeps_balaban_and_root_boundaries_explicit() -> None:
    text = (
        BASE
        / "04_candidates/YM_E1a1_C001_LOCAL_HAAR_CONCATENATION_LEAKAGE_20260811.md"
    ).read_text(encoding="utf-8")
    assert "F'_0(A,B)=\\frac{1}{2N}\\operatorname{Tr}(AB)" in text
    assert "does **not** establish" in text
    assert "Balaban" in text
    assert "mass gap" in text
    assert "SU(2)" in text
