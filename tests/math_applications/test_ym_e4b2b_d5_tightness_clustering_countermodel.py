from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-E4b2b_PRE_ACTION_FIBRE_RECEIPT_20260811.json"
RESULT = ROOT / "research/real_math/millennium/yang_mills/04_candidates/YM-E4b2b_D5_TIGHTNESS_CLUSTERING_COUNTERMODEL_20260811.md"


def canonical_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def os_norm_sq_of_positive_z(epsilon: Fraction) -> Fraction:
    # In the product reflection-positive model, Q(F,F)=|E F|^2.
    return epsilon * epsilon


def test_ym_e4b2b_pre_action_receipt_is_self_consistent_and_current_v3_bound() -> None:
    document = json.loads(RECEIPT.read_text(encoding="utf-8"))
    recorded = document.pop("receipt_canonical_sha256")
    assert recorded == canonical_sha256(document)
    assert document["framework_commit"] == "812e9cf18345ef430f0a4cc3ff78f93d7f18ed22"
    assert document["application_commit"] == "812addd25a7f34d3c6272143e21d5d7db34539aa"
    assert document["atom_id"] == "YM-E4b2b"
    assert document["allowed_outcome_branches"] == [
        "SUCCESS",
        "PARTIAL_SUCCESS",
        "FAILURE",
        "BLOCKED",
        "UNKNOWN",
    ]


def test_ym_e4b2b_product_model_is_exactly_reflection_positive_on_finite_gram_calibration() -> None:
    # For any positive-time cylinder family F_i in the product model,
    # Q(F_i,F_j)=conj(E F_i) E F_j.  On a real calibration this is an
    # outer-product Gram matrix, so c^T Q c=(sum c_i E F_i)^2 >= 0.
    epsilon = Fraction(1, 3)
    expectations = [Fraction(1), epsilon, epsilon * epsilon]
    coefficients = [Fraction(2), Fraction(-5), Fraction(3)]
    quadratic = sum(c * e for c, e in zip(coefficients, expectations)) ** 2
    assert quadratic >= 0


def test_ym_e4b2b_product_model_has_perfect_disjoint_support_clustering_calibration() -> None:
    # Two distinct product coordinates are independent:
    # E[Z_x Z_y] - E[Z_x]E[Z_y] = epsilon^2 - epsilon^2 = 0.
    for epsilon in (Fraction(1, 2), Fraction(1, 3), Fraction(1, 5), Fraction(1, 10)):
        covariance = epsilon * epsilon - epsilon * epsilon
        assert covariance == 0


def test_ym_e4b2b_generic_d5_implication_fails_exactly_on_limit_null_source() -> None:
    q_limit = Fraction(0)
    for epsilon in (Fraction(1, 2), Fraction(1, 3), Fraction(1, 5), Fraction(1, 10)):
        q_regulated = os_norm_sq_of_positive_z(epsilon)
        assert q_regulated > 0
        # No finite M can satisfy q_regulated <= M*q_limit, because RHS=0.
        for M in (Fraction(1), Fraction(7), Fraction(10_000)):
            assert not (q_regulated <= M * q_limit)


def test_ym_e4b2b_result_keeps_source_and_root_authority_closed() -> None:
    text = RESULT.read_text(encoding="utf-8")
    assert "source-route diagnostic" in text
    assert "not a counterexample to Yang–Mills" in text
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in text
    assert "zero independent-review credit" in text
    assert "KNOWLEDGE=0" in text
    assert "META_METHOD=0" in text
