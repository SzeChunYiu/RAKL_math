"""Finite exact hostile calibration for O9d12a2a1a1b.

This enumerates source-defined semi-filters for the G_NEQ complement U on N<=4
points, computes the complete legal-pair cover neighborhood of each semi-filter,
and checks the exact row quotient.  It is a regression/falsifier only; the
mathematical lemmas in the accompanying audit do not depend on enumeration.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations


def subseteq(a: int, b: int) -> bool:
    return (a & ~b) == 0


def antichains_nonempty(n: int):
    """Yield antichains of nonempty subsets of [n], including the empty antichain."""
    subsets = tuple(range(1, 1 << n))
    for choose_mask in range(1 << len(subsets)):
        chosen = tuple(subsets[i] for i in range(len(subsets)) if choose_mask & (1 << i))
        if all(not subseteq(a, b) and not subseteq(b, a) for a, b in combinations(chosen, 2)):
            yield chosen


def upset(minimal_antichain: tuple[int, ...], n: int) -> frozenset[int]:
    return frozenset(
        s for s in range(1 << n)
        if any(subseteq(a, s) for a in minimal_antichain)
    )


def relevant_gneq_semifilters(n: int) -> tuple[frozenset[int], ...]:
    """All semi-filters above at least one unequal G_NEQ edge.

    In the G_NEQ complement, row/column generator traces are singleton diagonal
    points.  Being above an unequal edge is therefore equivalent to containing
    at least two singleton subsets.
    """
    rows = []
    singleton_masks = tuple(1 << i for i in range(n))
    for antichain in antichains_nonempty(n):
        if not antichain:
            continue
        family = upset(antichain, n)
        if sum(singleton in family for singleton in singleton_masks) >= 2:
            rows.append(family)
    return tuple(rows)


def pair_neighborhood(family: frozenset[int], n: int) -> frozenset[tuple[int, int]]:
    """All ordered pair vertices (E,H) that cover this semi-filter."""
    return frozenset(
        (e, h)
        for e in range(1 << n)
        for h in range(1 << n)
        if e in family and h in family and (e & h) not in family
    )


def canonical_family(u: int, v: int, n: int) -> frozenset[int]:
    return upset((1 << u, 1 << v), n)


@dataclass(frozen=True)
class AuditRow:
    n: int
    relevant_rows: int
    quotient_rows: int
    canonical_rows: int
    fixed_edge_rows: int
    singleton_pair_covers_fixed_edge: bool


def audit(n: int) -> AuditRow:
    if not 2 <= n <= 4:
        raise ValueError("exhaustive regression is intentionally bounded to 2 <= N <= 4")
    rows = relevant_gneq_semifilters(n)
    neighborhoods = {pair_neighborhood(family, n) for family in rows}
    canonical = tuple(canonical_family(u, v, n) for u in range(n) for v in range(u + 1, n))
    canonical_neighborhoods = {pair_neighborhood(family, n) for family in canonical}

    fixed_u, fixed_v = 0, 1
    fixed_rows = tuple(
        family for family in rows
        if (1 << fixed_u) in family and (1 << fixed_v) in family
    )
    planted_pair = (1 << fixed_u, 1 << fixed_v)
    covers_all = all(planted_pair in pair_neighborhood(family, n) for family in fixed_rows)

    return AuditRow(
        n=n,
        relevant_rows=len(rows),
        quotient_rows=len(neighborhoods),
        canonical_rows=len(canonical_neighborhoods),
        fixed_edge_rows=len(fixed_rows),
        singleton_pair_covers_fixed_edge=covers_all,
    )


def main() -> None:
    for n in (2, 3, 4):
        row = audit(n)
        print(
            f"N={row.n} relevant={row.relevant_rows} quotient={row.quotient_rows} "
            f"canonical={row.canonical_rows} fixed_edge={row.fixed_edge_rows} "
            f"singleton_pair_covers_all={row.singleton_pair_covers_fixed_edge}"
        )


if __name__ == "__main__":
    main()
