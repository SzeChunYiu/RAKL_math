from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / (
    "research/real_math/millennium/birch_swinnerton_dyer/01_frontier/"
    "BSD-S001c1a_LOCAL_CORRECTION_AND_EXTRA_ZERO_AUDIT_20260811.md"
)


def test_bsd_s001c1a_local_correction_audit_is_fail_closed() -> None:
    text = AUDIT.read_text(encoding="utf-8")
    required = (
        "a151d5612709ea0f95c3ea232630f246f722739a",
        "arXiv:1509.00682",
        "sp(S)",
        "strict Selmer",
        "extra zero",
        "REPRESENTATION_ORDER_HAS_INDEPENDENT_LOCAL_OR_EXTRA_VANISHING",
        "no-uncontrolled-extra-zero",
        "NO_NEW_THEOREM",
        "ROOT_AUTHORITY_NONE",
        "OPEN_NO_SOLUTION_CERTIFICATE",
    )
    for token in required:
        assert token in text

    # Guard the exact authority boundary: the source-backed obstruction may prune
    # a raw representation, but must not be promoted to a universal impossibility
    # or to a BSD solution.
    forbidden = (
        "BSD is proved",
        "ROOT_CERTIFICATE_VALID",
        "universal impossibility theorem",
    )
    for token in forbidden:
        assert token not in text
