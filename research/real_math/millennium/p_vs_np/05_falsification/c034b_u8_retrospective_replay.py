"""Pure-Python exact retrospective replay for the externally reported U8 LP.

The target value was exposed before this checker and its certificates existed.
This module therefore grants only bounded exact-computation authority for the
explicitly reconstructed finite evaluator.  It grants no strict RAKL discovery,
proof, novelty, review-independence, asymptotic, or P-versus-NP authority.
"""

from __future__ import annotations

import copy
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path


U8 = ((0, 0), (1, 2), (1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (3, 4))
DENOMINATOR = 24

# A regenerated exact certificate.  It need not equal the missing reported
# 21/24-support certificate: this one has 17 primal and 20 dual support items.
PRIMAL = (
    (7, 248, 5), (14, 241, 5), (15, 244, 3), (15, 248, 1),
    (25, 230, 4), (25, 238, 2), (27, 228, 5), (27, 244, 2),
    (30, 225, 3), (30, 227, 2), (41, 222, 4), (71, 184, 4),
    (102, 153, 1), (103, 250, 2), (110, 145, 2), (110, 153, 1),
    (154, 229, 3),
)
DUAL = (
    ((1, 10), 6), ((1, 68), 3), ((1, 144), 3), ((6, 144), 2),
    ((24, 68), 3), ((224, 1), 5), ((224, 10), 5),
    ((4, 32, 64, 147), 1), ((16, 32, 128), 3), ((2, 8, 16), 3),
    ((2, 4, 8), 2), ((1, 6, 12), 2), ((1, 18, 24), 3),
    ((4, 32, 64), 2), ((4, 48, 64, 128), 1), ((16, 64, 128), 1),
    ((1, 38, 44, 52, 68, 132), 1),
    ((2, 12, 49, 52, 56, 84, 112, 144), 1),
    ((8, 18, 37, 38, 52, 68, 148, 164), 1),
    ((4, 80, 144, 235), 1),
)


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def _is_comparable(left: int, right: int) -> bool:
    return left & right == left or left & right == right


def _contains(minimals: tuple[int, ...], subset: int) -> bool:
    return any(minimal & subset == minimal for minimal in minimals)


def _covers(minimals: tuple[int, ...], pair: tuple[int, int]) -> bool:
    left, right = pair
    return (
        _contains(minimals, left)
        and _contains(minimals, right)
        and not _contains(minimals, left & right)
    )


def _generator_pairs(
    ambient: dict[str, int], complement_edges: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, int], ...]:
    left_size = ambient["left_size"]
    right_size = ambient["right_size"]
    index = {edge: bit for bit, edge in enumerate(complement_edges)}
    row_masks = tuple(
        sum(1 << index[edge] for edge in complement_edges if edge[0] == row)
        for row in range(left_size)
    )
    column_masks = tuple(
        sum(1 << index[edge] for edge in complement_edges if edge[1] == column)
        for column in range(right_size)
    )
    complement = set(complement_edges)
    return tuple(
        sorted(
            {
                (row_masks[row], column_masks[column])
                for row in range(left_size)
                for column in range(right_size)
                if (row, column) not in complement
                and row_masks[row]
                and column_masks[column]
            }
        )
    )


def _full_union_pairs(edge_count: int) -> tuple[tuple[int, int], ...]:
    full = (1 << edge_count) - 1
    return tuple(
        (left, right)
        for left in range(1 << edge_count)
        for right in range(left + 1, 1 << edge_count)
        if left | right == full and not _is_comparable(left, right)
    )


def _separate_primal(
    primal: tuple[tuple[int, int, int], ...],
    generator: tuple[int, int],
    threshold: int,
) -> dict[str, object]:
    """Search every monotone assignment on the certificate-relevant subposet.

    Any full semi-filter restricts to a monotone assignment on these masks, so
    absence of a sub-threshold restricted assignment is a sound exhaustive
    certificate.  Conversely, a sub-threshold assignment is extended by the
    upward closure of its 1-masks and returned as a concrete falsifier.
    """

    masks = tuple(sorted({0, *generator, *(mask for e, h, _ in primal for mask in (e, h, e & h))}))
    position = {mask: index for index, mask in enumerate(masks)}
    size = len(masks)
    supersets = tuple(
        sum(1 << other_index for other_index, other in enumerate(masks) if mask & other == mask)
        for mask in masks
    )
    subsets = tuple(
        sum(1 << other_index for other_index, other in enumerate(masks) if mask & other == other)
        for mask in masks
    )
    rules = tuple(
        (position[left], position[right], position[left & right], weight)
        for left, right, weight in primal
    )
    impacts = [0] * size
    for left, right, intersection, weight in rules:
        impacts[left] += weight
        impacts[right] += weight
        impacts[intersection] += weight

    def assign(ones: int, zeros: int, variable: int, value: int) -> tuple[int, int] | None:
        implied = supersets[variable] if value else subsets[variable]
        if (implied & zeros) if value else (implied & ones):
            return None
        return (ones | implied, zeros) if value else (ones, zeros | implied)

    state = assign(0, 0, position[0], 0)
    assert state is not None
    state = assign(*state, position[generator[0]], 1)
    assert state is not None
    state = assign(*state, position[generator[1]], 1)
    assert state is not None
    explored = 0

    @lru_cache(maxsize=None)
    def visit(ones: int, zeros: int) -> tuple[int, int | None]:
        nonlocal explored
        explored += 1
        forced_cost = sum(
            weight
            for left, right, intersection, weight in rules
            if (ones >> left) & 1 and (ones >> right) & 1 and (zeros >> intersection) & 1
        )
        if forced_cost >= threshold:
            return forced_cost, None
        unknown = ((1 << size) - 1) & ~(ones | zeros)
        if not unknown:
            return forced_cost, ones
        variable = max(
            (
                impacts[index] * 100
                + (supersets[index] & unknown).bit_count()
                + (subsets[index] & unknown).bit_count(),
                index,
            )
            for index in range(size)
            if (unknown >> index) & 1
        )[1]
        best_cost = 10**9
        for value in (0, 1):
            child = assign(ones, zeros, variable, value)
            if child is None:
                continue
            child_cost, witness = visit(*child)
            if child_cost < best_cost:
                best_cost = child_cost
            if child_cost < threshold:
                return child_cost, witness
        return best_cost, None

    lower_bound_or_falsifier_cost, witness_ones = visit(*state)
    witness_minimals: list[int] = []
    if witness_ones is not None:
        one_masks = [mask for index, mask in enumerate(masks) if (witness_ones >> index) & 1]
        witness_minimals = [
            mask
            for mask in one_masks
            if not any(other != mask and other & mask == other for other in one_masks)
        ]
    return {
        "generator_pair": list(generator),
        "certified_floor_or_falsifier_cost": lower_bound_or_falsifier_cost,
        "states_explored": explored,
        "tracked_mask_count": size,
        "subthreshold_witness_minimal_masks": witness_minimals,
    }


def pass_world() -> dict[str, object]:
    ambient = {"left_size": 4, "right_size": 5}
    generators = _generator_pairs(ambient, U8)
    return {
        "ambient_bipartition": ambient,
        "ambient_binding": "MINIMAL_COORDINATE_AMBIENT_4x5; ZERO_STAR_PADDING_IS_EVALUATOR_INVARIANT",
        "complement_edges": [list(edge) for edge in U8],
        "generator_pairs": [list(pair) for pair in generators],
        "primal_scaled_denominator": DENOMINATOR,
        "primal_support": [
            {"e_mask": left, "h_mask": right, "scaled_weight": weight}
            for left, right, weight in PRIMAL
        ],
        "dual_support": [
            {"minimal_masks": list(minimals), "scaled_weight": weight}
            for minimals, weight in DUAL
        ],
    }


def planted_fail_world() -> dict[str, object]:
    world = pass_world()
    world["primal_support"][0]["scaled_weight"] = 1
    return world


def structural_cannot_check_world() -> dict[str, object]:
    world = pass_world()
    del world["ambient_bipartition"]
    return world


def zero_star_padding_world() -> dict[str, object]:
    """Pad by one left and one right vertex with empty complement stars."""
    world = pass_world()
    world["ambient_bipartition"] = {"left_size": 5, "right_size": 6}
    world["ambient_binding"] = "ZERO_STAR_PADDED_5x6_EXECUTABLE_INVARIANCE_WORLD"
    # The explicit complement is unchanged.  The newly introduced stars are
    # empty and therefore cannot form a relevant generator pair.
    return world


def mutate_primal_weight(world: dict[str, object]) -> dict[str, object]:
    mutated = copy.deepcopy(world)
    mutated["primal_support"][0]["scaled_weight"] -= 1
    return mutated


def mutate_dual_weight(world: dict[str, object]) -> dict[str, object]:
    mutated = copy.deepcopy(world)
    mutated["dual_support"][0]["scaled_weight"] += DENOMINATOR
    return mutated


def drop_generator_pair(world: dict[str, object]) -> dict[str, object]:
    mutated = copy.deepcopy(world)
    mutated["generator_pairs"] = mutated["generator_pairs"][:-1]
    return mutated


def verify_world(world: dict[str, object]) -> dict[str, object]:
    if "ambient_bipartition" not in world:
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_AMBIENT_BIPARTITION"}
    required = {
        "complement_edges", "generator_pairs", "primal_scaled_denominator",
        "primal_support", "dual_support",
    }
    missing = sorted(required - world.keys())
    if missing:
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_STRUCTURAL_FIELDS", "fields": missing}

    ambient = world["ambient_bipartition"]
    try:
        left_size = ambient["left_size"]
        right_size = ambient["right_size"]
        edges = tuple(sorted(tuple(edge) for edge in world["complement_edges"]))
        if len(edges) != len(set(edges)) or not edges:
            raise ValueError("complement must be a nonempty set")
        if any(not (0 <= left < left_size and 0 <= right < right_size) for left, right in edges):
            raise ValueError("edge outside ambient bipartition")
    except (KeyError, TypeError, ValueError) as exc:
        return {"verdict": "CANNOT_CHECK", "reason": "MALFORMED_FINITE_OBJECT", "detail": str(exc)}

    generators = _generator_pairs(ambient, edges)
    supplied_generators = tuple(tuple(pair) for pair in world["generator_pairs"])
    if supplied_generators != generators:
        return {"verdict": "CANNOT_CHECK", "reason": "GENERATOR_PAIR_SPACE_MISMATCH"}
    full_union_pairs = _full_union_pairs(len(edges))
    pair_set = set(full_union_pairs)
    denominator = world["primal_scaled_denominator"]
    if not isinstance(denominator, int) or denominator <= 0:
        return {"verdict": "CANNOT_CHECK", "reason": "INVALID_CERTIFICATE_DENOMINATOR"}

    primal = tuple(
        (item["e_mask"], item["h_mask"], item["scaled_weight"])
        for item in world["primal_support"]
    )
    if any((left, right) not in pair_set or not isinstance(weight, int) or weight <= 0 for left, right, weight in primal):
        return {"verdict": "FAIL", "falsifier": "ILLEGAL_PRIMAL_SUPPORT"}
    separation = tuple(_separate_primal(primal, generator, denominator) for generator in generators)
    floors = [item["certified_floor_or_falsifier_cost"] for item in separation]
    if min(floors) < denominator:
        witness = min(separation, key=lambda item: item["certified_floor_or_falsifier_cost"])
        return {
            "verdict": "FAIL",
            "falsifier": "PLANTED_PRIMAL_WEIGHT_REDUCTION_DETECTED",
            "minimum_scaled_primal_coverage": min(floors),
            "witness": witness,
        }

    dual = tuple(
        (tuple(item["minimal_masks"]), item["scaled_weight"])
        for item in world["dual_support"]
    )
    for minimals, weight in dual:
        if not minimals or not isinstance(weight, int) or weight <= 0:
            return {"verdict": "FAIL", "falsifier": "MALFORMED_DUAL_SUPPORT"}
        if any(mask <= 0 or mask >= 1 << len(edges) for mask in minimals):
            return {"verdict": "FAIL", "falsifier": "DUAL_MASK_OUT_OF_RANGE"}
        if any(_is_comparable(left, right) for i, left in enumerate(minimals) for right in minimals[i + 1 :]):
            return {"verdict": "FAIL", "falsifier": "DUAL_MINIMALS_NOT_ANTICHAIN"}
        if not any(_contains(minimals, row) and _contains(minimals, column) for row, column in generators):
            return {"verdict": "FAIL", "falsifier": "DUAL_WITNESS_NOT_RELEVANT"}
    dual_loads = [
        sum(weight for minimals, weight in dual if _covers(minimals, pair))
        for pair in full_union_pairs
    ]
    if max(dual_loads, default=0) > denominator:
        return {
            "verdict": "FAIL",
            "falsifier": "DUAL_RULE_OVERLOAD_DETECTED",
            "maximum_scaled_dual_load": max(dual_loads),
        }

    primal_total_scaled = sum(weight for _, _, weight in primal)
    dual_total_scaled = sum(weight for _, weight in dual)
    if primal_total_scaled != dual_total_scaled:
        return {"verdict": "FAIL", "falsifier": "PRIMAL_DUAL_TOTAL_MISMATCH"}
    tight_witnesses = [
        {"minimal_masks": list(minimals), "scaled_coverage": sum(weight for left, right, weight in primal if _covers(minimals, (left, right)))}
        for minimals, _ in dual
    ]
    return {
        "verdict": "PASS",
        "complement_edge_count": len(edges),
        "relevant_generator_pair_count": len(generators),
        "full_union_pair_count": len(full_union_pairs),
        "primal_support_count": len(primal),
        "dual_support_count": len(dual),
        "primal_total": str(Fraction(primal_total_scaled, denominator)),
        "dual_total": str(Fraction(dual_total_scaled, denominator)),
        "minimum_scaled_primal_coverage": min(item["scaled_coverage"] for item in tight_witnesses),
        "maximum_scaled_dual_load": max(dual_loads),
        "generator_separation_lower_bounds": floors,
        "generator_separation": list(separation),
        "tight_dual_witness_coverage": tight_witnesses,
        "primal_feasible": True,
        "dual_feasible": True,
        "matching_totals": True,
        "exact_optimum": str(Fraction(primal_total_scaled, denominator)),
    }


def build_receipt() -> dict[str, object]:
    passing = pass_world()
    receipt = {
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C034B-U8-RETROSPECTIVE-EXACT-REPLAY-20260811",
        "recorded_at": "2026-08-11T17:35:00Z",
        "framework_pin": "9027cc6beab7e935d714bbdf8e902b89b50caaa8",
        "application_base_commit": "1d248204b35426695419f1a5a477e49cf163d39b",
        "source_binding": {
            "path": "research/real_math/millennium/p_vs_np/00_sources/RAKL_PVSNP_C034_C040_EXTERNAL_LEDGER_20260811.md",
            "source_sha256": "sha256:3db396674e15231f7cda79964d20c252ef99f6cd9058f20aa27173376075429d",
            "claim_id": "C034B-U8-49/24",
            "prior_assessment_path": "research/real_math/millennium/p_vs_np/08_reviews/C034_C040_EXTERNAL_LEDGER_ASSESSMENT_20260811.json",
            "prior_assessment_sha256": "sha256:c64edcf80f2048562182c16a32d5f58416324f3a5c876a430f96902af095cae5",
            "target_exposed_before_replay": True,
            "reported_support_counts_not_reproduced": True,
            "ambient_literal_absent": True,
            "reconstruction_boundary": "The evaluator uses the coordinate-minimal 4x5 ambient. Extra zero-star row/column padding generates no relevant pair and leaves this finite evaluator unchanged. Authority is conditional on that evaluator binding, not on the missing external artifact bundle.",
            "certificate_support_difference": {
                "ledger_reported_primal_support": 21,
                "ledger_reported_dual_support": 24,
                "regenerated_primal_support": 17,
                "regenerated_dual_support": 20,
                "interpretation": "DIFFERENT_MATCHING_CERTIFICATE_REPRESENTATION_NOT_ORIGINAL_CERTIFICATE_RECOVERY",
            },
        },
        "object_qoi_context": {
            "object": "the finite full-semi-filter fractional cover LP induced by the explicit eight-edge complement U8",
            "qoi": "exact optimum of the reconstructed finite LP",
            "context": "minimal 4x5 bipartition; unordered incomparable full-union pair space; relevant upward-closed semi-filters containing a nonempty row-star/column-star generator pair",
            "evidence_boundary": "retrospective exact computation after target exposure",
        },
        "evaluator_contract": {
            "implementation": "research/real_math/millennium/p_vs_np/05_falsification/c034b_u8_retrospective_replay.py",
            "implementation_sha256": "sha256:" + hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "arithmetic": "integer-scaled exact loads with denominator 24",
            "primal_global_check": "exhaustive monotone-assignment search on the certificate-relevant subposet for each of 12 generator pairs",
            "dual_global_check": "exact enumeration of all 3025 unordered incomparable full-union pairs",
            "full_union_reduction_dependency": "C034a ledger argument; desk-checked only, so the replay's strongest unconditional scope is the reconstructed full-union LP",
        },
        "certificate": passing,
        "validation_worlds": {
            "pass": verify_world(passing),
            "planted_fail": verify_world(planted_fail_world()),
            "structural_cannot_check": verify_world(structural_cannot_check_world()),
            "zero_star_padding_invariance": verify_world(zero_star_padding_world()),
        },
        "claim_update": {
            "prior_verdict": "CANNOT_CHECK_MISSING_CERTIFICATE_AND_RECEIPT",
            "new_verdict": "RETROSPECTIVE_EXACT_REPLAY_PASS_RECONSTRUCTED_FULL_UNION_LP_SOURCE_BINDING_CONDITIONAL",
            "original_missing_bundle_verdict": "CANNOT_CHECK_MISSING_CERTIFICATE_AND_RECEIPT",
            "root_status": "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE",
            "reported_external_certificate_status": "STILL_MISSING_NOT_REPRODUCED",
        },
        "review_authority": "SAME_CONTEXT_INTERNAL_ASSURANCE_NOT_INDEPENDENT_PEER_REVIEW",
        "authority_contract": {
            "grants_proof_authority": False,
            "grants_p_vs_np_root_authority": False,
            "grants_theorem_authority": False,
            "grants_asymptotic_authority": False,
            "grants_novelty_authority": False,
            "grants_review_independence": False,
            "grants_strict_rakl_discovery_credit": False,
            "promotes_missing_external_certificate": False,
        },
        "residuals": [
            "recover the original ambient declaration, certificates, verifier receipts, and chronology artifacts",
            "formally or independently assure the C034a reduction before extending equality from the full-union LP to all original rules",
            "obtain isolated external review before any stronger finite-claim promotion",
        ],
        "artifact_hash": "",
    }
    receipt["artifact_hash"] = _canonical_hash(receipt)
    return receipt


def main() -> None:
    print(json.dumps(build_receipt(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
