"""Assurance checks for the mathematical sparse-support bridge repair."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
REPAIR_PATH = PNP / "05_falsification/c041_sparse_bridge_repair.py"


def _load():
    spec = importlib.util.spec_from_file_location("c041_sparse_bridge_repair", REPAIR_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_sparse_support_repairs_exponentially_large_declared_universe() -> None:
    repair = _load()
    candidate = repair.candidate
    huge_declared = candidate.Formula3CNF(
        1 << 20,
        (((1, False), (1, False), (1, False)),),
        "SPARSE_COUNTERFAMILY",
    )
    assert repair.occurring_variables(huge_declared) == (1,)
    assert repair.sparse_assignment_satisfies(huge_declared, (True,))
    assert repair.sparse_is_satisfiable(huge_declared)


def test_sparse_semantics_agree_with_full_semantics_on_small_formulas() -> None:
    repair = _load()
    candidate = repair.candidate
    formulas = [candidate.TAUTOLOGY, candidate.CONTRADICTION]
    for formula in formulas:
        assert repair.sparse_is_satisfiable(formula) == candidate.is_satisfiable(
            formula
        )


def test_sparse_graph_verifier_has_correct_sat_reduction_polarity() -> None:
    repair = _load()
    candidate = repair.candidate
    satisfiable = candidate.Formula3CNF(
        1 << 12,
        (((1, False), (1, False), (1, False)),),
        "SPARSE_SAT",
    )
    contradictory = candidate.Formula3CNF(
        1 << 12,
        (
            ((1, False), (1, False), (1, False)),
            ((1, True), (1, True), (1, True)),
        ),
        "SPARSE_UNSAT",
    )
    level, row, column = candidate.sat_reduction(satisfiable)
    assert repair.graph_edge_has_sparse_np_witness(level, row, column, (True,))
    level, row, column = candidate.sat_reduction(contradictory)
    assert not repair.graph_edge_has_sparse_np_witness(level, row, column, (True,))
    assert not repair.graph_edge_has_sparse_np_witness(level, row, column, (False,))


def test_sparse_decider_agrees_with_frozen_rule_on_the_evaluated_transition() -> None:
    repair = _load()
    candidate = repair.candidate
    for row in range(8):
        for column in range(8):
            assert repair.complement_contains_sparse(
                3, row, column
            ) == candidate.complement_contains(3, row, column)
