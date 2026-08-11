"""Executable regression for C026's generic source-native closure cascade.

This module checks only the finite set-system construction frozen before outcomes.
It does not prove P != NP, does not establish a graph-specific cascade, and does
not grant novelty or root authority.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable


SetT = frozenset[int]
Pair = tuple[SetT, SetT]


def powerset(universe: SetT) -> tuple[SetT, ...]:
    items = tuple(sorted(universe))
    out: list[SetT] = []
    for r in range(len(items) + 1):
        out.extend(frozenset(c) for c in combinations(items, r))
    return tuple(out)


def upward_closure(seed: Iterable[SetT], universe: SetT) -> set[SetT]:
    all_sets = powerset(universe)
    seed_tuple = tuple(seed)
    return {target for target in all_sets if any(base <= target for base in seed_tuple)}


@dataclass(frozen=True)
class ClosureResult:
    family: frozenset[SetT]
    fired_intersections: tuple[SetT, ...]

    @property
    def contains_empty(self) -> bool:
        return frozenset() in self.family


def least_preservation_closure(
    required_sets: Iterable[SetT],
    pairs: Iterable[Pair],
    universe: SetT,
) -> ClosureResult:
    family = upward_closure(required_sets, universe)
    fired: list[SetT] = []
    pair_tuple = tuple(pairs)
    changed = True
    while changed:
        changed = False
        for left, right in pair_tuple:
            intersection = left & right
            if left in family and right in family and intersection not in family:
                family |= upward_closure((intersection,), universe)
                fired.append(intersection)
                changed = True
    return ClosureResult(frozenset(family), tuple(fired))


@dataclass(frozen=True)
class CascadeInstance:
    m: int
    universe: SetT
    required_traces: tuple[SetT, ...]
    old_pairs: tuple[Pair, ...]
    new_pair: Pair
    chain: tuple[SetT, ...]


def cascade_instance(m: int) -> CascadeInstance:
    if m < 3:
        raise ValueError("m must be at least 3")
    universe = frozenset(range(1, m + 1))
    d = {i: universe - {i} for i in range(1, m + 1)}
    c = {j: universe - set(range(1, j + 1)) for j in range(2, m + 1)}
    old_pairs = tuple((c[j], d[j + 1]) for j in range(2, m))
    return CascadeInstance(
        m=m,
        universe=universe,
        required_traces=tuple(d[i] for i in range(1, m + 1)),
        old_pairs=old_pairs,
        new_pair=(d[1], d[2]),
        chain=tuple(c[j] for j in range(2, m + 1)),
    )


def check_cascade(m: int) -> dict[str, object]:
    instance = cascade_instance(m)
    before = least_preservation_closure(
        instance.required_traces, instance.old_pairs, instance.universe
    )
    after = least_preservation_closure(
        instance.required_traces,
        (instance.new_pair,) + instance.old_pairs,
        instance.universe,
    )
    return {
        "m": m,
        "before_cardinality": len(before.family),
        "after_cardinality": len(after.family),
        "before_contains_empty": before.contains_empty,
        "after_contains_empty": after.contains_empty,
        "before_fired_count": len(before.fired_intersections),
        "after_fired_count": len(after.fired_intersections),
        "expected_chain": [sorted(s) for s in instance.chain],
        "observed_fired_chain": [sorted(s) for s in after.fired_intersections],
        "predictions_pass": (
            len(before.family) == m + 1
            and not before.contains_empty
            and len(before.fired_intersections) == 0
            and after.contains_empty
            and len(after.family) == 2**m
            and after.fired_intersections == instance.chain
        ),
    }


def regression_receipt(min_m: int = 3, max_m: int = 10) -> dict[str, object]:
    rows = [check_cascade(m) for m in range(min_m, max_m + 1)]
    return {
        "candidate_id": "C026",
        "scope": "generic finite source-compatible discrete spaces only",
        "tested_m": list(range(min_m, max_m + 1)),
        "rows": rows,
        "all_predictions_pass": all(bool(row["predictions_pass"]) for row in rows),
        "authority": (
            "FINITE_REGRESSION_ONLY / GENERAL_ARGUMENT_IS_SYMBOLIC / "
            "NO_GRAPH_SPECIFIC_OR_ROOT_AUTHORITY"
        ),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(regression_receipt(), indent=2, sort_keys=True))
