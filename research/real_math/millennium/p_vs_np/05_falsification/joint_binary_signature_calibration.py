#!/usr/bin/env python3
"""Exact finite gate for C025's normalized G_NEQ binary-signature model.

This executable checks a local representation.  It does not prove a result about
P versus NP, and finite enumeration is not used as theorem authority.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
from functools import lru_cache
import json
from pathlib import Path
from typing import Iterable, Iterator, Sequence


DEFAULT_N_VALUES = (2, 3, 4, 5, 8, 9, 16, 17)
EXHAUSTIVE_N_MAX = 4


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def required_bits(n_labels: int) -> int:
    """Return ceil(log2(n_labels)) exactly for n_labels >= 2."""
    if n_labels < 2:
        raise ValueError("n_labels must be at least 2")
    return (n_labels - 1).bit_length()


def iter_cut_families(n_labels: int, n_bits: int) -> Iterator[tuple[int, ...]]:
    """Enumerate ordered normalized cut families as bit masks."""
    if n_labels < 2:
        raise ValueError("n_labels must be at least 2")
    if n_bits < 0:
        raise ValueError("n_bits must be nonnegative")
    yield from itertools.product(range(1 << n_labels), repeat=n_bits)


def joint_signatures(n_labels: int, cuts: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    """Return the shared binary signature of each diagonal generator trace."""
    if n_labels < 2:
        raise ValueError("n_labels must be at least 2")
    limit = 1 << n_labels
    if any(cut < 0 or cut >= limit for cut in cuts):
        raise ValueError("cut mask lies outside the registered label universe")
    return tuple(
        tuple((cut >> label) & 1 for cut in cuts) for label in range(n_labels)
    )


def directly_separated(cuts: Sequence[int], left: int, right: int) -> bool:
    """Check whether one normalized complementary cut separates two labels."""
    if left == right:
        return False
    return any(((cut >> left) & 1) != ((cut >> right) & 1) for cut in cuts)


def is_covering_family(n_labels: int, cuts: Sequence[int]) -> bool:
    """Check every ordered unequal G_NEQ obligation in the normalized model."""
    signatures = joint_signatures(n_labels, cuts)
    return len(set(signatures)) == n_labels


@lru_cache(maxsize=None)
def all_semifilters(n_labels: int) -> tuple[int, ...]:
    """Enumerate semi-filters as bitsets over subsets; only for tiny worlds."""
    if n_labels < 2 or n_labels > EXHAUSTIVE_N_MAX:
        raise ValueError("full semi-filter enumeration is restricted to 2<=N<=4")
    subset_count = 1 << n_labels
    out: list[int] = []
    # Bit position X records membership of subset X in the family.
    for family in range(1, 1 << subset_count):
        if family & 1:  # the empty subset is prohibited
            continue
        upward = True
        for subset in range(subset_count):
            if not ((family >> subset) & 1):
                continue
            for superset in range(subset_count):
                if subset & ~superset == 0 and not ((family >> superset) & 1):
                    upward = False
                    break
            if not upward:
                break
        if upward:
            out.append(family)
    return tuple(out)


def _member(semifilter: int, subset: int) -> bool:
    return bool((semifilter >> subset) & 1)


def _cut_covers_semifilter(n_labels: int, cut: int, semifilter: int) -> bool:
    complement = ((1 << n_labels) - 1) ^ cut
    # The normalized sides are disjoint, and empty is absent by construction.
    return _member(semifilter, cut) and _member(semifilter, complement)


def direct_full_semifilter_family_cover(n_labels: int, cuts: Sequence[int]) -> bool:
    """Apply the source preservation definition to every small-world semi-filter."""
    for left in range(n_labels):
        for right in range(n_labels):
            if left == right:
                continue
            left_singleton = 1 << left
            right_singleton = 1 << right
            for semifilter in all_semifilters(n_labels):
                if not (
                    _member(semifilter, left_singleton)
                    and _member(semifilter, right_singleton)
                ):
                    continue
                if not any(
                    _cut_covers_semifilter(n_labels, cut, semifilter) for cut in cuts
                ):
                    return False
    return True


def _full_semifilter_equivalence_result(n_labels: int) -> dict[str, object]:
    checked = 0
    mismatches = 0
    for n_bits in range(required_bits(n_labels) + 1):
        for cuts in iter_cut_families(n_labels, n_bits):
            checked += 1
            signature_verdict = is_covering_family(n_labels, cuts)
            direct_verdict = direct_full_semifilter_family_cover(n_labels, cuts)
            if signature_verdict != direct_verdict:
                mismatches += 1
    return {
        "N": n_labels,
        "semifilter_count": len(all_semifilters(n_labels)),
        "ordered_cut_families_checked": checked,
        "direct_vs_signature_mismatches": mismatches,
        "equivalence_pass": mismatches == 0,
    }


def canonical_binary_cuts(n_labels: int) -> tuple[int, ...]:
    """Construct the usual injective binary label code as normalized cuts."""
    bits = required_bits(n_labels)
    cuts = []
    for bit in range(bits):
        mask = 0
        for label in range(n_labels):
            if (label >> bit) & 1:
                mask |= 1 << label
        cuts.append(mask)
    return tuple(cuts)


def exhaustive_minimum_bits(n_labels: int) -> int:
    """Counterexample-first exact search, intended only for small N."""
    upper = required_bits(n_labels)
    for n_bits in range(upper + 1):
        if any(is_covering_family(n_labels, cuts) for cuts in iter_cut_families(n_labels, n_bits)):
            return n_bits
    raise AssertionError("canonical upper bound was not found")


def _case_result(n_labels: int) -> dict[str, object]:
    bits = required_bits(n_labels)
    cuts = canonical_binary_cuts(n_labels)
    signatures = joint_signatures(n_labels, cuts)
    separated = sum(
        directly_separated(cuts, left, right)
        for left in range(n_labels)
        for right in range(n_labels)
        if left != right
    )
    total = n_labels * (n_labels - 1)
    low_order_bits = bits - 1
    low_order_capacity = 1 << low_order_bits
    return {
        "N": n_labels,
        "required_bits": bits,
        "capacity_at_required_bits": 1 << bits,
        "constructive_cut_masks": list(cuts),
        "constructive_distinct_signature_count": len(set(signatures)),
        "unequal_ordered_pairs_total": total,
        "unequal_ordered_pairs_separated": separated,
        "calibration_pass": len(set(signatures)) == n_labels and separated == total,
        "low_order_bits": low_order_bits,
        "low_order_capacity": low_order_capacity,
        "low_order_collision_forced": low_order_capacity < n_labels,
    }


def build_receipt(
    *, preregistration_path: Path, evaluated_at: str, n_values: Iterable[int] = DEFAULT_N_VALUES
) -> dict[str, object]:
    preregistration_path = preregistration_path.resolve()
    executable_path = Path(__file__).resolve()
    prereg = json.loads(preregistration_path.read_text(encoding="utf-8"))
    if prereg["candidate_id"] != "C025" or prereg["atom_id"] != "O9d12a2a1a":
        raise ValueError("wrong preregistration identity")
    prereg_payload = copy.deepcopy(prereg)
    prereg_payload["artifact_hash"] = ""
    if prereg["artifact_hash"] != _canonical_hash(prereg_payload):
        raise ValueError("preregistration artifact hash is invalid")
    if evaluated_at <= prereg["frozen_at"]:
        raise ValueError("evaluation must occur after preregistration freeze")

    cases = [_case_result(n_labels) for n_labels in n_values]
    exhaustive = [
        {
            "N": n_labels,
            "exhaustive_minimum_bits": exhaustive_minimum_bits(n_labels),
            "predicted_minimum_bits": required_bits(n_labels),
        }
        for n_labels in range(2, EXHAUSTIVE_N_MAX + 1)
    ]
    full_equivalence = [
        _full_semifilter_equivalence_result(n_labels)
        for n_labels in range(2, EXHAUSTIVE_N_MAX + 1)
    ]
    full_equivalence_pass = all(item["equivalence_pass"] for item in full_equivalence)
    all_calibrations_pass = all(item["calibration_pass"] for item in cases)
    all_low_order_fail = all(item["low_order_collision_forced"] for item in cases)
    exhaustive_matches = all(
        item["exhaustive_minimum_bits"] == item["predicted_minimum_bits"]
        for item in exhaustive
    )
    verdict = (
        "PASS_SCOPED_CALIBRATION_WITH_CAPACITY_NO_GO"
        if all_calibrations_pass and all_low_order_fail and exhaustive_matches and full_equivalence_pass
        else "FAIL_FROZEN_C025_PREDICTION"
    )
    receipt: dict[str, object] = {
        "schema_version": "1.0.0",
        "receipt_id": "C025-JOINT-SIGNATURE-CALIBRATION-20260811",
        "candidate_id": "C025",
        "atom_id": "O9d12a2a1a",
        "evaluated_at": evaluated_at,
        "bindings": {
            "preregistration_artifact_hash": prereg["artifact_hash"],
            "preregistration_file_sha256": _file_hash(preregistration_path),
            "executable_file_sha256": _file_hash(executable_path),
            "context_packet_hash": prereg["chronology"]["context_packet_hash"],
            "rakl_math_base_commit": prereg["chronology"]["rakl_math_base_commit"],
            "framework_authority_commit": prereg["chronology"]["framework_authority_commit"],
        },
        "model": {
            "object": "normalized complementary cuts on the diagonal complement of G_NEQ",
            "coverage_equivalence": "unequal pair separated iff its two joint binary signatures differ",
            "capacity_law": "k binary coordinates admit at most 2^k distinct first-order signatures",
        },
        "case_results": cases,
        "exhaustive_counterexample_search": {
            "N_max": EXHAUSTIVE_N_MAX,
            "ordered_cut_families": True,
            "results": exhaustive,
            "matches_frozen_prediction": exhaustive_matches,
            "authority": "EXACT_FINITE_SEARCH_ONLY",
        },
        "full_semifilter_definition_regression": {
            "N_max": EXHAUSTIVE_N_MAX,
            "results": full_equivalence,
            "all_equivalent": full_equivalence_pass,
            "authority": "EXACT_FINITE_SOURCE-DEFINITION_REGRESSION_ONLY",
        },
        "frozen_falsifier_outcomes": [
            {"id": "C025-F1", "outcome": "NOT_TRIGGERED" if exhaustive_matches else "TRIGGERED"},
            {"id": "C025-F2", "outcome": "NOT_TRIGGERED" if all_calibrations_pass else "TRIGGERED"},
            {"id": "C025-F3", "outcome": "NOT_TRIGGERED" if full_equivalence_pass else "TRIGGERED", "evidence": "exhaustive source-definition full-semi-filter/signature equivalence regression N<=4"},
            {"id": "C025-F4", "outcome": "NOT_TRIGGERED", "evidence": "exact cardinality 2^k"},
        ],
        "capacity_falsifier": {
            "observed_result": "FIRST_ORDER_CARDINALITY_ONLY_ARGUMENT_LOGARITHMICALLY_CAPPED",
            "route_effect": "REJECT_AS_SUPERLOG_PRIMARY_ROUTE_WITHIN_FROZEN_SCOPE",
            "residual_signature": [
                "joint integrality recovered on G_NEQ",
                "first-order cardinality-only state capacity saturates at ceil(log2 M)",
                "higher-order semi-filter closure coordinate remains untested",
            ],
            "diagnosis_status": "SUPPORTED_WITHIN_REGISTERED_REPRESENTATION_SCOPE",
        },
        "claim_scope": {
            "normalized_G_NEQ_joint_signatures": "EXACT_LOCAL_CALIBRATION",
            "capacity_only_first_order_argument": "LOGARITHMIC_CEILING",
            "arbitrary_full_cover_targets": "NOT_TESTED",
            "higher_order_closure_signatures": "NOT_TESTED",
            "p_vs_np": "NO_AUTHORITY",
        },
        "verdict": verdict,
        "authority": "EXACT_LOCAL_REPRESENTATION_CALIBRATION / FINITE_ENUMERATION_SUPPORT / COMPUTATION_IS_NOT_PROOF / SAME_CONTEXT_REVIEW_NOT_INDEPENDENT / ROOT_AUTHORITY_NONE",
        "artifact_hash": "",
    }
    receipt["artifact_hash"] = _canonical_hash(receipt)
    return receipt


def write_receipt(*, preregistration_path: Path, output_path: Path, evaluated_at: str) -> None:
    receipt = build_receipt(
        preregistration_path=preregistration_path,
        evaluated_at=evaluated_at,
    )
    output_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preregistration", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--evaluated-at", required=True)
    args = parser.parse_args()
    write_receipt(
        preregistration_path=args.preregistration,
        output_path=args.output,
        evaluated_at=args.evaluated_at,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
