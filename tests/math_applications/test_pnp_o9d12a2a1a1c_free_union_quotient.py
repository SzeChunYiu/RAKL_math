"""Finite hostile controls for O9d12a2a1a1c.

These tests calibrate the representation/admission rule only. They are not proof
of Cavalar--Oliveira Theorem 30 or of any asymptotic circuit lower bound.
"""

from itertools import combinations


def union_closure(generators: frozenset[frozenset[int]]) -> frozenset[frozenset[int]]:
    items = tuple(generators)
    out = {frozenset()}
    for r in range(1, len(items) + 1):
        for combo in combinations(items, r):
            merged: set[int] = set()
            for item in combo:
                merged.update(item)
            out.add(frozenset(merged))
    return frozenset(out)


def test_free_union_expansion_changes_presentation_without_changing_free_targets() -> None:
    base = frozenset({frozenset({1}), frozenset({2}), frozenset({3})})
    expanded = union_closure(base)

    assert len(expanded) > len(base)  # a presentation-sensitive score can inflate
    assert frozenset({1, 3}) in expanded  # but this target is union-generated at zero intersections
    assert union_closure(expanded) == expanded  # canonical free-union quotient is idempotent


def test_hostile_score_must_not_treat_generator_count_as_intersection_cost() -> None:
    base = frozenset({frozenset({1}), frozenset({2}), frozenset({3}), frozenset({4})})
    expanded = union_closure(base)

    naive_generator_count_score_before = len(base)
    naive_generator_count_score_after = len(expanded)

    assert naive_generator_count_score_after > naive_generator_count_score_before
    assert union_closure(base) == union_closure(expanded)
    # Therefore raw generator-family size is not invariant under the cost-zero quotient.


def test_control_does_not_claim_intersection_closure_is_free() -> None:
    base = frozenset({frozenset({1, 2}), frozenset({2, 3})})
    expanded = union_closure(base)
    intersection = frozenset({2})

    assert intersection not in expanded
    # The atom normalizes only operations counted as free (unions), not intersections.
