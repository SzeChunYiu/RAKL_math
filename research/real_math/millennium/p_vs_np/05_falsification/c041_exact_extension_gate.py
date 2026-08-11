"""Bounded exact mathematical gate for a complement extension.

The mathematical content checked here is finite: cylinder relevance, the
C038 lifted-dual transfer condition, and the exact residual augmentation LP.
The surrounding Python execution and tests are assurance only.  A surviving
finite instance does not prove a uniform rule, a divergent recurrence, an
asymptotic lower bound, novelty, or any P-versus-NP statement.

This module deliberately contains no native C041 rule and does not select one.
It evaluates only an explicitly supplied finite parent/child extension.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
from typing import Iterable, Mapping


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import full_cover_oracle as oracle  # noqa: E402


Edge = tuple[int, int]
Antichain = tuple[int, ...]
PairMask = tuple[int, int]

MAX_CHILD_COMPLEMENT_EDGES = 5


def _q(value: Fraction | int) -> dict[str, int]:
    """Serialize one exact rational; serialization itself is assurance only."""
    fraction = Fraction(value)
    return {
        "numerator": fraction.numerator,
        "denominator": fraction.denominator,
    }


def _full_union_pairs(universe_size: int) -> tuple[PairMask, ...]:
    """Enumerate the C034a-complete unordered full-union pair class."""
    full = (1 << universe_size) - 1
    return tuple(
        (e_set, h_set)
        for e_set in range(1 << universe_size)
        for h_set in range(e_set + 1, 1 << universe_size)
        if (e_set | h_set) == full and not oracle._is_comparable(e_set, h_set)
    )


def _validate_antichain(minimals: Antichain, universe_size: int) -> bool:
    if not minimals or tuple(sorted(set(minimals))) != minimals:
        return False
    if any(mask <= 0 or mask >= 1 << universe_size for mask in minimals):
        return False
    return all(
        not oracle._is_comparable(left, right)
        for index, left in enumerate(minimals)
        for right in minimals[index + 1 :]
    )


def _lift_mask(mask: int, old_edges: list[Edge], child_index: Mapping[Edge, int]) -> int:
    return sum(
        1 << child_index[edge]
        for bit, edge in enumerate(old_edges)
        if mask & (1 << bit)
    )


def _relevance_witnesses(
    child_side: int,
    child_complement: set[Edge],
    minimals: Antichain,
) -> list[dict[str, object]]:
    _, row_masks, column_masks, graph_edges = oracle._graph_masks(
        child_side, child_complement
    )
    witnesses: list[dict[str, object]] = []
    for row_vertex, column_vertex in graph_edges:
        row_mask = row_masks[row_vertex]
        column_mask = column_masks[column_vertex]
        if not row_mask or not column_mask:
            continue
        if oracle._filter_contains(minimals, row_mask) and oracle._filter_contains(
            minimals, column_mask
        ):
            witnesses.append(
                {
                    "graph_edge": [row_vertex, column_vertex],
                    "row_mask": row_mask,
                    "column_mask": column_mask,
                }
            )
    return witnesses


def _pair_load(
    pair: PairMask,
    weighted_filters: Iterable[tuple[Antichain, Fraction]],
) -> Fraction:
    return sum(
        (
            weight
            for minimals, weight in weighted_filters
            if oracle.pair_covers_semifilter(minimals, *pair)
        ),
        Fraction(),
    )


def _minimal_neighborhood_columns(
    filters: tuple[Antichain, ...], pairs: tuple[PairMask, ...]
) -> tuple[tuple[Antichain, int], ...]:
    """Keep one representative of each undominated pair-neighborhood.

    If one filter is covered by a subset of the pairs covering another, mass
    on the former weakly dominates equal mass on the latter.  Removing the
    latter therefore preserves the residual packing optimum.
    """
    representative: dict[int, Antichain] = {}
    for minimals in filters:
        signature = sum(
            1 << pair_index
            for pair_index, pair in enumerate(pairs)
            if oracle.pair_covers_semifilter(minimals, *pair)
        )
        if signature == 0:
            raise ArithmeticError("a relevant semi-filter has no legal covering pair")
        representative.setdefault(signature, minimals)

    retained: list[tuple[Antichain, int]] = []
    for signature in sorted(representative, key=lambda value: (value.bit_count(), value)):
        if any((kept_signature & signature) == kept_signature for _, kept_signature in retained):
            continue
        retained.append((representative[signature], signature))
    return tuple(retained)


def _exact_residual_lp(
    filters: tuple[Antichain, ...],
    pairs: tuple[PairMask, ...],
    capacities: tuple[Fraction, ...],
) -> dict[str, object]:
    """Solve the residual packing LP with an exact rational simplex.

    The mathematical certificate is a matching feasible packing ``z`` and
    covering dual ``x``.  The simplex mechanics are assurance only.
    """
    if any(capacity < 0 for capacity in capacities):
        raise ArithmeticError("negative residual capacity")
    if not filters:
        return {
            "exact_optimum": _q(0),
            "primal_total": _q(0),
            "dual_total": _q(0),
            "primal_feasible": True,
            "dual_feasible": True,
            "augmentation_support": [],
            "cover_certificate_support": [],
            "complete_child_filter_count": 0,
            "undominated_filter_count": 0,
        }

    columns = _minimal_neighborhood_columns(filters, pairs)
    variable_count = len(columns)
    constraint_count = len(pairs)
    total_columns = variable_count + constraint_count

    tableau: list[list[Fraction]] = []
    for row_index, capacity in enumerate(capacities):
        row = [
            Fraction((signature >> row_index) & 1)
            for _, signature in columns
        ]
        row.extend(
            Fraction(int(column_index == row_index))
            for column_index in range(constraint_count)
        )
        row.append(capacity)
        tableau.append(row)
    tableau.append(
        [Fraction(-1)] * variable_count
        + [Fraction()] * constraint_count
        + [Fraction()]
    )
    basis = [variable_count + index for index in range(constraint_count)]

    while True:
        entering_candidates = [
            column
            for column in range(total_columns)
            if column not in basis and tableau[-1][column] < 0
        ]
        if not entering_candidates:
            break
        entering = min(entering_candidates)
        leaving_candidates: list[tuple[Fraction, int, int]] = []
        for row_index in range(constraint_count):
            coefficient = tableau[row_index][entering]
            if coefficient > 0:
                leaving_candidates.append(
                    (
                        tableau[row_index][-1] / coefficient,
                        basis[row_index],
                        row_index,
                    )
                )
        if not leaving_candidates:
            raise ArithmeticError("residual LP is unexpectedly unbounded")
        _, _, leaving_row = min(leaving_candidates)

        pivot = tableau[leaving_row][entering]
        tableau[leaving_row] = [value / pivot for value in tableau[leaving_row]]
        for row_index in range(constraint_count + 1):
            if row_index == leaving_row:
                continue
            multiple = tableau[row_index][entering]
            if multiple:
                tableau[row_index] = [
                    value - multiple * pivot_value
                    for value, pivot_value in zip(
                        tableau[row_index], tableau[leaving_row], strict=True
                    )
                ]
        basis[leaving_row] = entering

    primal = [Fraction()] * variable_count
    for row_index, basic_variable in enumerate(basis):
        if basic_variable < variable_count:
            primal[basic_variable] = tableau[row_index][-1]
    dual = [tableau[-1][variable_count + index] for index in range(constraint_count)]

    if any(value < 0 for value in primal) or any(value < 0 for value in dual):
        raise ArithmeticError("exact simplex returned a negative certificate coordinate")

    for row_index, capacity in enumerate(capacities):
        load = sum(
            (
                primal[column_index]
                for column_index, (_, signature) in enumerate(columns)
                if (signature >> row_index) & 1
            ),
            Fraction(),
        )
        if load > capacity:
            raise ArithmeticError("rational residual packing certificate is infeasible")
    for minimals in filters:
        cover = sum(
            (
                dual[pair_index]
                for pair_index, pair in enumerate(pairs)
                if oracle.pair_covers_semifilter(minimals, *pair)
            ),
            Fraction(),
        )
        if cover < 1:
            raise ArithmeticError("rational residual covering certificate is infeasible")

    primal_total = sum(primal, Fraction())
    dual_total = sum(
        (capacity * weight for capacity, weight in zip(capacities, dual, strict=True)),
        Fraction(),
    )
    if primal_total != dual_total or primal_total != tableau[-1][-1]:
        raise ArithmeticError("matching rational certificates do not have equal totals")

    return {
        "exact_optimum": _q(primal_total),
        "primal_total": _q(primal_total),
        "dual_total": _q(dual_total),
        "primal_feasible": True,
        "dual_feasible": True,
        "augmentation_support": [
            {"minimal_masks": list(columns[index][0]), "weight": _q(weight)}
            for index, weight in enumerate(primal)
            if weight
        ],
        "cover_certificate_support": [
            {
                "e_mask": pairs[index][0],
                "h_mask": pairs[index][1],
                "weight": _q(weight),
            }
            for index, weight in enumerate(dual)
            if weight
        ],
        "complete_child_filter_count": len(filters),
        "undominated_filter_count": variable_count,
    }


def _base_receipt() -> dict[str, object]:
    return {
        "status": None,
        "mathematical_outcome": None,
        "mathematical_claim": None,
        "parent_dual_total": None,
        "maximum_parent_pair_load": None,
        "maximum_lifted_pair_load": None,
        "child_certificate_total": None,
        "summary": None,
        "cylinder_lifts": [],
        "lost_lifts": [],
        "lifted_pair_loads": [],
        "residual_augmentation": None,
        "authority": {
            "mathematical_content": None,
            "assurance_only": "implementation, serialization, and tests",
            "grants_uniform_rule_authority": False,
            "grants_asymptotic_authority": False,
            "grants_novelty_authority": False,
            "grants_p_vs_np_authority": False,
            "mathematical_saturation_credit": False,
        },
    }


def evaluate_extension_gate(
    *,
    parent_side: int,
    child_side: int,
    parent_complement: set[Edge],
    child_complement: set[Edge],
    parent_dual: Mapping[Antichain, Fraction],
    max_child_complement_edges: int = MAX_CHILD_COMPLEMENT_EDGES,
) -> dict[str, object]:
    """Evaluate one supplied finite extension without constructing a rule."""
    receipt = _base_receipt()
    effective_bound = min(max_child_complement_edges, MAX_CHILD_COMPLEMENT_EDGES)

    if len(child_complement) > effective_bound:
        receipt.update(
            {
                "status": "CANNOT_CHECK",
                "mathematical_outcome": "CANNOT_CHECK_BOUND_EXCEEDED",
                "bound": {
                    "maximum": effective_bound,
                    "observed": len(child_complement),
                },
            }
        )
        return receipt

    if (
        parent_side < 2
        or child_side < parent_side
        or not parent_complement
        or not parent_complement < child_complement
        or any(not (0 <= u < parent_side and 0 <= v < parent_side) for u, v in parent_complement)
        or any(not (0 <= u < child_side and 0 <= v < child_side) for u, v in child_complement)
        or len(parent_complement) == parent_side * parent_side
        or len(child_complement) == child_side * child_side
    ):
        receipt.update(
            {
                "status": "CANNOT_CHECK",
                "mathematical_outcome": "CANNOT_CHECK_INVALID_EXTENSION",
            }
        )
        return receipt

    parent_edges = sorted(parent_complement)
    child_edges = sorted(child_complement)
    parent_filters = set(oracle._relevant_semifilters(parent_side, parent_complement))
    parent_pairs = _full_union_pairs(len(parent_edges))
    weighted_parent: list[tuple[Antichain, Fraction]] = []
    invalid_parent = False
    for minimals, raw_weight in parent_dual.items():
        weight = Fraction(raw_weight)
        if (
            not _validate_antichain(minimals, len(parent_edges))
            or minimals not in parent_filters
            or weight <= 0
        ):
            invalid_parent = True
            break
        weighted_parent.append((minimals, weight))
    if not weighted_parent:
        invalid_parent = True

    parent_loads = (
        [_pair_load(pair, weighted_parent) for pair in parent_pairs]
        if not invalid_parent
        else []
    )
    maximum_parent_load = max(parent_loads, default=Fraction())
    receipt["parent_dual_total"] = _q(
        sum((weight for _, weight in weighted_parent), Fraction())
    )
    receipt["maximum_parent_pair_load"] = _q(maximum_parent_load)
    if invalid_parent or maximum_parent_load > 1:
        receipt.update(
            {
                "status": "CANNOT_CHECK",
                "mathematical_outcome": "CANNOT_CHECK_INVALID_PARENT_DUAL",
            }
        )
        return receipt

    child_index = {edge: bit for bit, edge in enumerate(child_edges)}
    lifted: list[tuple[Antichain, Fraction]] = []
    lift_rows: list[dict[str, object]] = []
    lost_rows: list[dict[str, object]] = []
    for minimals, weight in weighted_parent:
        child_minimals = tuple(
            sorted(_lift_mask(mask, parent_edges, child_index) for mask in minimals)
        )
        witnesses = _relevance_witnesses(
            child_side, child_complement, child_minimals
        )
        row = {
            "parent_minimal_masks": list(minimals),
            "child_minimal_masks": list(child_minimals),
            "weight": _q(weight),
            "relevant": bool(witnesses),
            "relevance_witnesses": witnesses,
        }
        lift_rows.append(row)
        if witnesses:
            lifted.append((child_minimals, weight))
        else:
            lost_rows.append(
                {
                    "parent_minimal_masks": list(minimals),
                    "child_minimal_masks": list(child_minimals),
                    "weight": _q(weight),
                }
            )

    receipt["cylinder_lifts"] = lift_rows
    receipt["lost_lifts"] = lost_rows
    receipt["summary"] = {
        "positive_parent_support": len(weighted_parent),
        "relevant_cylinder_lifts": len(lifted),
        "irrelevant_cylinder_lifts": len(lost_rows),
    }
    if lost_rows:
        receipt.update(
            {
                "status": "FAIL",
                "mathematical_outcome": "FAIL_RELEVANCE",
            }
        )
        receipt["authority"]["mathematical_content"] = (
            "exact finite counterexample to supported cylinder relevance"
        )
        return receipt

    child_pairs = _full_union_pairs(len(child_edges))
    lifted_loads = tuple(_pair_load(pair, lifted) for pair in child_pairs)
    maximum_lifted_load = max(lifted_loads, default=Fraction())
    receipt["maximum_lifted_pair_load"] = _q(maximum_lifted_load)
    receipt["lifted_pair_loads"] = [
        {
            "e_mask": pair[0],
            "h_mask": pair[1],
            "load": _q(load),
            "residual_capacity": _q(Fraction(1) - load),
        }
        for pair, load in zip(child_pairs, lifted_loads, strict=True)
    ]
    if maximum_lifted_load > 1:
        receipt.update(
            {
                "status": "FAIL",
                "mathematical_outcome": "FAIL_LIFTED_FEASIBILITY_PREMISE",
                "mathematical_claim": (
                    "A lifted-load violation contradicts the C038 transfer premises; "
                    "it is not an independent extension phenomenon."
                ),
            }
        )
        receipt["authority"]["mathematical_content"] = (
            "exact falsification of a claimed C038 transfer premise"
        )
        return receipt

    child_filters = oracle._relevant_semifilters(child_side, child_complement)
    capacities = tuple(Fraction(1) - load for load in lifted_loads)
    try:
        residual = _exact_residual_lp(child_filters, child_pairs, capacities)
    except ArithmeticError as error:
        receipt.update(
            {
                "status": "CANNOT_CHECK",
                "mathematical_outcome": "CANNOT_CHECK_EXACT_CERTIFICATE_FAILURE",
                "assurance_error": str(error),
            }
        )
        return receipt

    receipt["residual_augmentation"] = residual
    delta = Fraction(
        residual["exact_optimum"]["numerator"],
        residual["exact_optimum"]["denominator"],
    )
    parent_total = sum((weight for _, weight in weighted_parent), Fraction())
    receipt["child_certificate_total"] = _q(parent_total + delta)
    if delta == 0:
        receipt.update(
            {
                "status": "FAIL",
                "mathematical_outcome": "FAIL_ZERO_AUGMENTATION",
                "mathematical_claim": (
                    "The supported cylinder remains dual-feasible, but the exact "
                    "residual augmentation optimum is zero for this finite extension."
                ),
            }
        )
        receipt["authority"]["mathematical_content"] = (
            "exact finite zero-augmentation certificate"
        )
        return receipt

    receipt.update(
        {
            "status": "PASS",
            "mathematical_outcome": "FINITE_GATE_SURVIVES",
            "mathematical_claim": (
                "This finite extension admits the recorded positive exact residual "
                "dual augmentation; no uniform or asymptotic conclusion follows."
            ),
        }
    )
    receipt["authority"]["mathematical_content"] = (
        "exact finite positive residual-augmentation certificate"
    )
    return receipt
