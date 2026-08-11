"""XM015 exact finite certificate regression.

This test verifies the finite n=2->3 child certificate only.  It is
repository assurance/calibration, not a proof of an asymptotic circuit
lower bound, P != NP, or any Yang-Mills statement.
"""
from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ORACLE = (
    ROOT
    / "research"
    / "real_math"
    / "millennium"
    / "p_vs_np"
    / "05_falsification"
    / "full_cover_oracle.py"
)

spec = spec_from_file_location("xm015_full_cover_oracle", ORACLE)
assert spec is not None and spec.loader is not None
oracle = module_from_spec(spec)
spec.loader.exec_module(oracle)

CHILD = {(0, 0), (0, 4), (1, 2), (2, 1), (2, 2)}
PRIMAL_FILTERS = ((4, 8), (2, 8), (2, 4))
DUAL_PAIRS = ((3, 28), (7, 24), (11, 20))
FULL = 31


def _legal_full_union_pairs():
    pairs = []
    for e_set in range(1 << 5):
        for h_set in range(e_set + 1, 1 << 5):
            if (e_set | h_set) != FULL:
                continue
            if oracle._is_comparable(e_set, h_set):
                continue
            pairs.append((e_set, h_set))
    return pairs


def test_xm015_full_reoptimization_certificate():
    relevant = oracle._relevant_semifilters(8, CHILD)
    legal_pairs = _legal_full_union_pairs()

    assert len(relevant) == 787
    assert len(legal_pairs) == 90
    assert all(filt in relevant for filt in PRIMAL_FILTERS)

    # Primal: three relevant filters at weight 1/2; no legal pair covers all
    # three, so every pair load is at most 2*(1/2)=1.
    max_priced_filters_covered = max(
        sum(oracle.pair_covers_semifilter(filt, e_set, h_set) for filt in PRIMAL_FILTERS)
        for e_set, h_set in legal_pairs
    )
    assert max_priced_filters_covered == 2

    # Dual: three full-union pairs at weight 1/2; every relevant semi-filter
    # is covered by at least two, so receives total dual weight at least 1.
    min_dual_pairs_covering_filter = min(
        sum(oracle.pair_covers_semifilter(filt, e_set, h_set) for e_set, h_set in DUAL_PAIRS)
        for filt in relevant
    )
    assert min_dual_pairs_covering_filter == 2

    # Matching feasible primal and dual values are both 3/2.
    assert 3 * 0.5 == 1.5
