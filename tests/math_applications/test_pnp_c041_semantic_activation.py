"""Assurance-only checks for C041 semantic activation.

Passing these finite checks is calibration, not a recurrence, circuit lower bound,
novelty certificate, or P-vs-NP proof.
"""

from __future__ import annotations

import importlib.util
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = (
    ROOT
    / "research"
    / "real_math"
    / "millennium"
    / "p_vs_np"
    / "04_candidates"
    / "C041_fx_sat_one_sided.py"
)

spec = importlib.util.spec_from_file_location("pnp_c041_fx_sat_one_sided", CANDIDATE)
assert spec is not None and spec.loader is not None
c041 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = c041
spec.loader.exec_module(c041)


def _formula(*clauses: tuple[bool, bool, bool]):
    built = []
    for signs in clauses:
        built.append(tuple((1, negated) for negated in signs))
    return c041.Formula3CNF(1, tuple(built), "TEST_CANONICAL")


def test_n8_magic_is_syntactic_only() -> None:
    unsat = []
    for signs in product((False, True), repeat=3):
        formula = _formula(signs)
        encoded = c041.encode_formula(formula)
        assert len(encoded) == 16
        if not c041.is_satisfiable(formula):
            unsat.append(encoded)
        row = int(encoded[:8], 2)
        column = 256 + int(encoded[8:], 2)
        assert not c041.complement_contains(9, row, column)
    assert unsat == []
    assert c041.complement_contains(9, 0, 256)


def test_n12_first_semantic_magic_unsat_geometry() -> None:
    unsat = []
    for first in product((False, True), repeat=3):
        for second in product((False, True), repeat=3):
            formula = _formula(first, second)
            encoded = c041.encode_formula(formula)
            assert len(encoded) == 24
            if not c041.is_satisfiable(formula):
                unsat.append(encoded)

    assert len(unsat) == 2
    assert {word[:12] for word in unsat} == {"111001011010"}
    assert {word[12:] for word in unsat} == {
        "010101111111",
        "111111010101",
    }

    coordinates = {
        (int(word[:12], 2), 4096 + int(word[12:], 2))
        for word in unsat
    }
    assert coordinates == {(3674, 5503), (3674, 8149)}
    for row, column in coordinates:
        assert c041.complement_contains(13, row, column)
