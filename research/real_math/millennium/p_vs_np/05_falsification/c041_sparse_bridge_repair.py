"""Sparse-support verifier/decider for the unchanged frozen C041 language."""

from __future__ import annotations

import importlib.util
from itertools import product
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
CANDIDATE_PATH = HERE.parent / "04_candidates/C041_fx_sat_one_sided.py"
SPEC = importlib.util.spec_from_file_location("c041_fx_sat_bridge_base", CANDIDATE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen C041 decoder")
candidate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = candidate
SPEC.loader.exec_module(candidate)


Formula3CNF = candidate.Formula3CNF


def occurring_variables(formula: Formula3CNF) -> tuple[int, ...]:
    return tuple(
        sorted({variable for clause in formula.clauses for variable, _ in clause})
    )


def sparse_assignment_satisfies(
    formula: Formula3CNF, assignment: tuple[bool, ...]
) -> bool:
    support = occurring_variables(formula)
    if len(assignment) != len(support):
        return False
    values = dict(zip(support, assignment, strict=True))
    return all(
        any(
            (not values[variable]) if negated else values[variable]
            for variable, negated in clause
        )
        for clause in formula.clauses
    )


def sparse_is_satisfiable(formula: Formula3CNF) -> bool:
    support_size = len(occurring_variables(formula))
    return any(
        sparse_assignment_satisfies(formula, assignment)
        for assignment in product((False, True), repeat=support_size)
    )


def graph_edge_has_sparse_np_witness(
    level: int,
    row: int,
    column: int,
    assignment: tuple[bool, ...] | None = None,
) -> bool:
    if level < candidate.SEED_LEVEL:
        return False
    side = 1 << level
    if not (0 <= row < side and 0 <= column < side):
        return False
    if level == candidate.SEED_LEVEL:
        return (row, column) not in candidate.SEED_COMPLEMENT
    half = side >> 1
    if row < half and column < half:
        return graph_edge_has_sparse_np_witness(
            level - 1, row, column, assignment
        )
    if row < half <= column:
        formula = candidate.decode_formula(
            candidate.cross_word(level - 1, row, column - half)
        )
        return assignment is not None and sparse_assignment_satisfies(
            formula, assignment
        )
    return True


def complement_contains_sparse(level: int, row: int, column: int) -> bool:
    """Same U-level predicate, decided over occurring variables only."""
    if level < candidate.SEED_LEVEL:
        raise ValueError("the family starts at level 2")
    side = 1 << level
    if not (0 <= row < side and 0 <= column < side):
        raise ValueError("vertex label lies outside the square domain")
    if level == candidate.SEED_LEVEL:
        return (row, column) in candidate.SEED_COMPLEMENT
    half = side >> 1
    if row < half and column < half:
        return complement_contains_sparse(level - 1, row, column)
    if row < half <= column:
        formula = candidate.decode_formula(
            candidate.cross_word(level - 1, row, column - half)
        )
        return not sparse_is_satisfiable(formula)
    return False
