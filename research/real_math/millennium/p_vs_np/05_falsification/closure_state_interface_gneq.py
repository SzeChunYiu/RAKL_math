#!/usr/bin/env python3
"""Exact finite regression for the O9d12a2a1a1 G_NEQ closure-interface audit.

This module reconstructs the source-defined Theorem 24 propagation rules after
the *C025-only* G_NEQ normalization to complementary partition pairs.

It is assurance code, not proof authority.  The mathematical audit proves the
identity symbolically; enumeration below only attacks transcription mistakes
and searches for a counterexample in small worlds.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from typing import Iterator, Sequence


def subset_contains(mask: int, element: int) -> bool:
    return bool((mask >> element) & 1)


def joint_signature(cuts: Sequence[int], element: int) -> tuple[int, ...]:
    return tuple(int(subset_contains(cut, element)) for cut in cuts)


def base_closure(n: int, left: int, right: int) -> frozenset[int]:
    """The G_NEQ Theorem-24 base state above edge (left,right)."""
    if not (0 <= left < n and 0 <= right < n and left != right):
        raise ValueError("expected an unequal ordered G_NEQ edge")
    return frozenset(
        subset
        for subset in range(1 << n)
        if subset_contains(subset, left) or subset_contains(subset, right)
    )


def first_stage_activation(
    cuts: Sequence[int], left: int, right: int
) -> tuple[bool, ...]:
    """Whether E_i and H_i are both in the source base closure."""
    return tuple(
        subset_contains(cut, left) != subset_contains(cut, right)
        for cut in cuts
    )


def xor_activation(
    cuts: Sequence[int], left: int, right: int
) -> tuple[bool, ...]:
    sigma_left = joint_signature(cuts, left)
    sigma_right = joint_signature(cuts, right)
    return tuple(a != b for a, b in zip(sigma_left, sigma_right))


def source_partition_closure(
    n: int, cuts: Sequence[int], left: int, right: int
) -> frozenset[int]:
    """Run the source G_w closure for H_i = U\\E_i exactly.

    Sets are bit masks on U={d_0,...,d_{n-1}}.  The base case is the upward
    closure of the row/column traces {d_left},{d_right}.  A propagation rule
    adds E_i∩H_i and every superset when both sides are present.
    """
    universe = (1 << n) - 1
    state = set(base_closure(n, left, right))
    changed = True
    while changed:
        changed = False
        for cut in cuts:
            complement = universe ^ cut
            if cut in state and complement in state:
                intersection = cut & complement  # exactly empty for partitions
                for superset in range(1 << n):
                    if intersection & ~superset == 0 and superset not in state:
                        state.add(superset)
                        changed = True
    return frozenset(state)


def iter_cut_families(n: int, k: int) -> Iterator[tuple[int, ...]]:
    yield from itertools.product(range(1 << n), repeat=k)


def audit_small_worlds(n_max: int = 5, k_max: int = 2) -> dict[str, object]:
    families_checked = 0
    edge_states_checked = 0
    same_signature_edge_groups = 0
    raw_base_only_difference_example = None

    for n in range(2, n_max + 1):
        full_state = frozenset(range(1 << n))
        for k in range(k_max + 1):
            for cuts in iter_cut_families(n, k):
                families_checked += 1
                groups: dict[
                    tuple[tuple[int, ...], tuple[int, ...]],
                    list[tuple[int, int, frozenset[int], tuple[bool, ...]]],
                ] = defaultdict(list)

                for left in range(n):
                    for right in range(n):
                        if left == right:
                            continue
                        edge_states_checked += 1
                        sigma_left = joint_signature(cuts, left)
                        sigma_right = joint_signature(cuts, right)
                        direct = first_stage_activation(cuts, left, right)
                        xor = xor_activation(cuts, left, right)
                        if direct != xor:
                            raise AssertionError(
                                ("activation/XOR mismatch", n, cuts, left, right)
                            )

                        closure = source_partition_closure(n, cuts, left, right)
                        predicted = (
                            full_state if any(xor) else base_closure(n, left, right)
                        )
                        if closure != predicted:
                            raise AssertionError(
                                ("terminal closure mismatch", n, cuts, left, right)
                            )
                        if ((0 in closure) != (sigma_left != sigma_right)):
                            raise AssertionError(
                                ("empty-set/signature mismatch", n, cuts, left, right)
                            )

                        groups[(sigma_left, sigma_right)].append(
                            (left, right, base_closure(n, left, right), xor)
                        )

                for signature_pair, states in groups.items():
                    if len(states) < 2:
                        continue
                    same_signature_edge_groups += 1
                    if (
                        raw_base_only_difference_example is None
                        and k >= 1
                        and any(0 < cut < (1 << n) - 1 for cut in cuts)
                    ):
                        for a, b in itertools.combinations(states, 2):
                            if a[2] != b[2] and a[3] == b[3]:
                                raw_base_only_difference_example = {
                                    "N": n,
                                    "cut_masks": list(cuts),
                                    "ordered_signature_pair": [
                                        list(signature_pair[0]),
                                        list(signature_pair[1]),
                                    ],
                                    "edge_a": [a[0], a[1]],
                                    "edge_b": [b[0], b[1]],
                                    "derived_activation": list(a[3]),
                                    "interpretation": (
                                        "base generator identities can differ while "
                                        "partition-derived activation is identical"
                                    ),
                                }
                                break

    return {
        "N_max": n_max,
        "k_max": k_max,
        "partition_families_checked": families_checked,
        "ordered_edge_states_checked": edge_states_checked,
        "same_signature_edge_groups_seen": same_signature_edge_groups,
        "raw_base_only_difference_example": raw_base_only_difference_example,
        "verdict": "NO_DERIVED_DIFFERENCEWITNESS_WITHIN_NORMALIZED_GNEQ",
        "authority": (
            "EXACT_FINITE_REGRESSION_ONLY / COMPUTATION_IS_NOT_PROOF / "
            "ROOT_AUTHORITY_NONE"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=5)
    parser.add_argument("--k-max", type=int, default=2)
    args = parser.parse_args()
    print(json.dumps(audit_small_worlds(args.n_max, args.k_max), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
