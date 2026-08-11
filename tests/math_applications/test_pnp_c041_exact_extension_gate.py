"""Assurance-only checks for the finite mathematical certificates.

Passing these tests grants no mathematical, uniform-rule, or asymptotic
authority; the mathematical content is carried only by the checked witnesses.
"""

from __future__ import annotations

from fractions import Fraction
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
GATE_PATH = (
    ROOT
    / "research"
    / "real_math"
    / "millennium"
    / "p_vs_np"
    / "05_falsification"
    / "c041_exact_extension_gate.py"
)


def _load_gate():
    spec = importlib.util.spec_from_file_location("c041_exact_extension_gate", GATE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _q(numerator: int, denominator: int = 1) -> dict[str, int]:
    return {"numerator": numerator, "denominator": denominator}


def test_c037_world_fails_exactly_at_cylinder_relevance() -> None:
    gate = _load_gate()
    parent = {(0, 0), (2, 1), (1, 2), (2, 2)}
    child = parent | {(1, 1)}
    parent_dual = {
        (1, 4): Fraction(1, 2),
        (1, 6, 10): Fraction(1, 2),
        (2, 4): Fraction(1, 2),
    }

    receipt = gate.evaluate_extension_gate(
        parent_side=3,
        child_side=3,
        parent_complement=parent,
        child_complement=child,
        parent_dual=parent_dual,
    )

    assert receipt["status"] == "FAIL"
    assert receipt["mathematical_outcome"] == "FAIL_RELEVANCE"
    assert receipt["parent_dual_total"] == _q(3, 2)
    assert receipt["summary"] == {
        "positive_parent_support": 3,
        "relevant_cylinder_lifts": 2,
        "irrelevant_cylinder_lifts": 1,
    }
    assert receipt["lost_lifts"] == [
        {
            "parent_minimal_masks": [2, 4],
            "child_minimal_masks": [4, 8],
            "weight": _q(1, 2),
        }
    ]
    assert receipt["residual_augmentation"] is None
    assert receipt["authority"]["mathematical_content"] == (
        "exact finite counterexample to supported cylinder relevance"
    )
    assert receipt["authority"]["grants_uniform_rule_authority"] is False


def test_relevance_preserved_world_has_exact_zero_augmentation_certificate() -> None:
    gate = _load_gate()
    a = (0, 0)
    b = (1, 1)
    c = (0, 1)

    receipt = gate.evaluate_extension_gate(
        parent_side=2,
        child_side=2,
        parent_complement={a, b},
        child_complement={a, b, c},
        parent_dual={(1, 2): Fraction(1)},
    )

    assert receipt["status"] == "FAIL"
    assert receipt["mathematical_outcome"] == "FAIL_ZERO_AUGMENTATION"
    assert receipt["summary"]["irrelevant_cylinder_lifts"] == 0
    assert receipt["maximum_lifted_pair_load"] == _q(1)
    residual = receipt["residual_augmentation"]
    assert residual["exact_optimum"] == _q(0)
    assert residual["primal_total"] == residual["dual_total"] == _q(0)
    assert residual["primal_feasible"] is True
    assert residual["dual_feasible"] is True
    assert receipt["child_certificate_total"] == _q(1)
    assert receipt["mathematical_claim"] == (
        "The supported cylinder remains dual-feasible, but the exact residual "
        "augmentation optimum is zero for this finite extension."
    )


def test_bound_exceeded_world_is_cannot_check_not_mathematical_failure() -> None:
    gate = _load_gate()
    parent = {(0, 0), (1, 1)}
    child = {
        (u, v)
        for u in range(3)
        for v in range(3)
        if (u, v) != (1, 0)
    }

    receipt = gate.evaluate_extension_gate(
        parent_side=2,
        child_side=3,
        parent_complement=parent,
        child_complement=child,
        parent_dual={(1, 2): Fraction(1)},
    )

    assert len(child) == 8
    assert gate.MAX_CHILD_COMPLEMENT_EDGES == 5
    assert receipt["status"] == "CANNOT_CHECK"
    assert receipt["mathematical_outcome"] == "CANNOT_CHECK_BOUND_EXCEEDED"
    assert receipt["bound"] == {"maximum": 5, "observed": 8}
    assert receipt["mathematical_claim"] is None
    assert receipt["residual_augmentation"] is None
    assert receipt["authority"]["mathematical_saturation_credit"] is False


def test_caller_cannot_weaken_the_frozen_five_edge_bound() -> None:
    gate = _load_gate()
    parent = {(0, 0), (1, 1)}
    child = {
        (u, v)
        for u in range(3)
        for v in range(3)
        if (u, v) != (1, 0)
    }

    receipt = gate.evaluate_extension_gate(
        parent_side=2,
        child_side=3,
        parent_complement=parent,
        child_complement=child,
        parent_dual={(1, 2): Fraction(1)},
        max_child_complement_edges=8,
    )

    assert receipt["mathematical_outcome"] == "CANNOT_CHECK_BOUND_EXCEEDED"
    assert receipt["bound"] == {"maximum": 5, "observed": 8}


def test_parent_dual_is_checked_exactly_before_child_evaluation() -> None:
    gate = _load_gate()

    receipt = gate.evaluate_extension_gate(
        parent_side=2,
        child_side=2,
        parent_complement={(0, 0), (1, 1)},
        child_complement={(0, 0), (0, 1), (1, 1)},
        parent_dual={(1, 2): Fraction(3, 2)},
    )

    assert receipt["status"] == "CANNOT_CHECK"
    assert receipt["mathematical_outcome"] == "CANNOT_CHECK_INVALID_PARENT_DUAL"
    assert receipt["maximum_parent_pair_load"] == _q(3, 2)
    assert receipt["mathematical_claim"] is None
