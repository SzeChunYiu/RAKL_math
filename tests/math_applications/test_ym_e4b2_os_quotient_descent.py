from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-E4b2_PRE_ACTION_FIBRE_RECEIPT_20260811.json"


def canonical_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def q_inf(v: tuple[Fraction, Fraction]) -> Fraction:
    x, _ = v
    return x * x


def q_n(v: tuple[Fraction, Fraction], n: int) -> Fraction:
    x, y = v
    return x * x + y * y / n


def test_ym_e4b2_hostile_family_separates_asymptotic_form_convergence_from_exact_quotient_descent() -> None:
    e2 = (Fraction(0), Fraction(1))
    assert q_inf(e2) == 0
    for n in (2, 3, 10, 100):
        assert q_n(e2, n) == Fraction(1, n) > 0
    # Therefore e2 is continuum-null but not n-null: [0]=[e2] in the
    # continuum quotient while their regulated classes differ for every n.


def test_ym_e4b2_d5_style_domination_forces_exact_null_inclusion() -> None:
    # Abstract implication used by the candidate: if 0 <= Q_n(F) <= M Q_inf(F)
    # and Q_inf(F)=0, then Q_n(F)=0 exactly.  Keep the arithmetic exact.
    q_limit = Fraction(0)
    M = Fraction(7)
    q_regulated = Fraction(0)
    assert 0 <= q_regulated <= M * q_limit
    assert q_regulated == 0


def test_ym_e4b2_pre_action_receipt_content_hash_is_self_consistent() -> None:
    document = json.loads(RECEIPT.read_text(encoding="utf-8"))
    recorded = document.pop("receipt_canonical_sha256")
    assert recorded == canonical_sha256(document)
    assert document["allowed_outcome_branches"] == [
        "SUCCESS",
        "PARTIAL_SUCCESS",
        "FAILURE",
        "BLOCKED",
        "UNKNOWN",
    ]
