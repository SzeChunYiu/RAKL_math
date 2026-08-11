"""Exact rational replay of the finite C037 counterexample reported externally.

The external ledger arrived without its named certificates or verifier receipts.
This script therefore reconstructs only the tiny C037 instance against the
repository's pre-existing full-semi-filter oracle.  Matching feasible primal
and dual certificates establish the two finite LP optima exactly.  They do not
prove an asymptotic result, novelty, or any P-versus-NP claim.
"""

from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import full_cover_oracle as oracle  # noqa: E402


PARENT = {(0, 0), (2, 1), (1, 2), (2, 2)}
CHILD = PARENT | {(1, 1)}


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def _full_union_pairs(m: int) -> tuple[tuple[int, int], ...]:
    full = (1 << m) - 1
    return tuple(
        (e_set, h_set)
        for e_set in range(1 << m)
        for h_set in range(e_set + 1, 1 << m)
        if (e_set | h_set) == full and not oracle._is_comparable(e_set, h_set)
    )


def _subset(mask: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    return [list(edge) for bit, edge in enumerate(edges) if mask & (1 << bit)]


def _certificate_instance(
    *,
    instance_id: str,
    complement: set[tuple[int, int]],
    primal: dict[tuple[int, int], Fraction],
    dual: dict[tuple[int, ...], Fraction],
) -> dict:
    edges = sorted(complement)
    filters = oracle._relevant_semifilters(3, complement)
    pairs = _full_union_pairs(len(edges))

    primal_loads = [
        sum(weight for pair, weight in primal.items() if oracle.pair_covers_semifilter(filt, *pair))
        for filt in filters
    ]
    dual_loads = [
        sum(weight for filt, weight in dual.items() if oracle.pair_covers_semifilter(filt, *pair))
        for pair in pairs
    ]
    primal_total = sum(primal.values(), Fraction())
    dual_total = sum(dual.values(), Fraction())
    if min(primal_loads) < 1 or max(dual_loads) > 1 or primal_total != dual_total:
        raise AssertionError("embedded exact certificates do not establish matching feasible bounds")

    return {
        "instance_id": instance_id,
        "ambient_bipartition": "3x3",
        "complement_edges": [list(edge) for edge in edges],
        "complement_edge_count": len(edges),
        "relevant_semifilter_count": len(filters),
        "full_union_pair_count": len(pairs),
        "primal_support": [
            {
                "e_mask": e_set,
                "h_mask": h_set,
                "e_edges": _subset(e_set, edges),
                "h_edges": _subset(h_set, edges),
                "weight": str(weight),
            }
            for (e_set, h_set), weight in sorted(primal.items())
        ],
        "dual_support": [
            {
                "minimal_masks": list(minimals),
                "minimal_edge_sets": [_subset(mask, edges) for mask in minimals],
                "weight": str(weight),
            }
            for minimals, weight in sorted(dual.items())
        ],
        "minimum_primal_coverage": str(min(primal_loads)),
        "maximum_dual_rule_load": str(max(dual_loads)),
        "primal_total": str(primal_total),
        "dual_total": str(dual_total),
        "exact_optimum": str(primal_total),
        "primal_feasible": True,
        "dual_feasible": True,
    }


def build_receipt() -> dict:
    parent = _certificate_instance(
        instance_id="C037-PARENT-U",
        complement=PARENT,
        primal={(3, 12): Fraction(1, 2), (5, 10): Fraction(1, 2), (9, 14): Fraction(1, 2)},
        dual={(1, 4): Fraction(1, 2), (1, 6, 10): Fraction(1, 2), (2, 4): Fraction(1, 2)},
    )
    child = _certificate_instance(
        instance_id="C037-CHILD-U-PRIME",
        complement=CHILD,
        primal={(1, 30): Fraction(1)},
        dual={(1, 14, 22, 24): Fraction(1)},
    )
    receipt = {
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C037-EXTERNAL-LEDGER-EXACT-REPLAY-20260811",
        "recorded_at": "2026-08-11T13:50:00Z",
        "method": "complete full-union rule enumeration plus exact rational primal-dual certificate checking",
        "oracle_path": "research/real_math/millennium/p_vs_np/05_falsification/full_cover_oracle.py",
        "oracle_git_blob_sha": "2a516b166fe2c01e0f478a73aa60e4b8bb48b6b3",
        "oracle_sha256": "sha256:70a933ff970b2412f8019ff204748b3c7948a6d9d914c62b85c90f2eb609b75d",
        "instances": [parent, child],
        "strict_drop": "1/2",
        "authority_contract": {
            "finite_computational_replay_only": True,
            "grants_asymptotic_authority": False,
            "grants_p_vs_np_root_authority": False,
            "grants_novelty_authority": False,
            "grants_review_independence": False,
        },
        "artifact_hash": "",
    }
    receipt["artifact_hash"] = _canonical_hash(receipt)
    return receipt


def main() -> None:
    print(json.dumps(build_receipt(), indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
