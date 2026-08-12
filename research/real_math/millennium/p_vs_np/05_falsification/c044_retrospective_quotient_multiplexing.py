"""Retrospective finite corroborator for the C043 Q16 quotient.

The three explicit disjoint pairs are mathematical upper-bound witnesses.
This script checks their finite fibre-separation consequences and records a
canonical-only exhaustive result.  The C044 outcome was exposed before a
strict pre-candidate freeze, so this module cannot create strict RAKL discovery
chronology.  Computation is not proof; the hand generator-separation argument
is recorded separately.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
CANONICAL_PATH = HERE / "canonical_cover_oracle.py"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


canonical = _load("c044_canonical_oracle", CANONICAL_PATH)

EDGE_NAMES = {
    "a": (0, 0),
    "b": (1, 2),
    "c": (2, 1),
    "d": (2, 2),
    "e": (4, 4),
    "f": (5, 5),
    "g": (5, 6),
    "h": (6, 5),
    "i": (7, 5),
    "j": (7, 7),
}
QUOTIENT_COMPLEMENT = set(EDGE_NAMES.values())
OLD_COMPONENT = {EDGE_NAMES[name] for name in "abcde"}
NEW_COMPONENT = {EDGE_NAMES[name] for name in "fghij"}
PAIR_NAMES = (
    (frozenset("abcde"), frozenset("fghij")),
    (frozenset("aefgh"), frozenset("bcdij")),
    (frozenset("abdfg"), frozenset("cehij")),
)
PAIRS = tuple(
    (
        frozenset(EDGE_NAMES[name] for name in e_names),
        frozenset(EDGE_NAMES[name] for name in h_names),
    )
    for e_names, h_names in PAIR_NAMES
)


def fibres() -> tuple[dict[int, frozenset[tuple[int, int]]], dict[int, frozenset[tuple[int, int]]]]:
    rows = {
        u: frozenset(edge for edge in QUOTIENT_COMPLEMENT if edge[0] == u)
        for u in range(8)
    }
    columns = {
        v: frozenset(edge for edge in QUOTIENT_COMPLEMENT if edge[1] == v)
        for v in range(8)
    }
    return rows, columns


def signature(star: frozenset[tuple[int, int]]) -> str:
    result = []
    for e_set, h_set in PAIRS:
        if star <= e_set:
            result.append("E")
        elif star <= h_set:
            result.append("H")
        else:
            result.append("X")
    return "".join(result)


def relevant_graph_edges() -> list[tuple[int, int]]:
    rows, columns = fibres()
    return [
        (u, v)
        for u in range(8)
        for v in range(8)
        if (u, v) not in QUOTIENT_COMPLEMENT and rows[u] and columns[v]
    ]


def separating_pair_indices(u: int, v: int) -> list[int]:
    rows, columns = fibres()
    answer = []
    for index, (e_set, h_set) in enumerate(PAIRS, start=1):
        if (
            (rows[u] <= e_set and columns[v] <= h_set)
            or (rows[u] <= h_set and columns[v] <= e_set)
        ):
            answer.append(index)
    return answer


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def build_receipt() -> dict[str, object]:
    rows, columns = fibres()
    relevant = relevant_graph_edges()
    coverage = [
        {
            "graph_edge": [u, v],
            "separating_pair_indices": separating_pair_indices(u, v),
        }
        for u, v in relevant
    ]
    if any(not row["separating_pair_indices"] for row in coverage):
        raise ArithmeticError("explicit pairs fail generator separation")
    if any(e_set & h_set for e_set, h_set in PAIRS):
        raise ArithmeticError("explicit pair is not disjoint")
    if any((e_set | h_set) != QUOTIENT_COMPLEMENT for e_set, h_set in PAIRS):
        raise ArithmeticError("explicit pair is not a full partition")

    exact_canonical = canonical.exact_canonical_cover_number(8, QUOTIENT_COMPLEMENT)
    receipt: dict[str, object] = {
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C044-RETROSPECTIVE-Q16-MULTIPLEXING-20260812",
        "candidate_id": "C044-RETROSPECTIVE-Q16-MULTIPLEXING-v1",
        "chronology": {
            "strict_pre_candidate_gate_run": False,
            "candidate_evaluator_frozen_before_output": False,
            "result_exposed_before_candidate_freeze": True,
            "strict_rakl_discovery_authority": False,
            "truth_check_may_proceed_retrospectively": True,
        },
        "quotient": {
            "side": 8,
            "ordered_complement": [list(edge) for edge in sorted(QUOTIENT_COMPLEMENT)],
            "complement_edge_count": 10,
            "old_component": [list(edge) for edge in sorted(OLD_COMPONENT)],
            "new_component": [list(edge) for edge in sorted(NEW_COMPONENT)],
            "cross_component_complement_edges": [],
            "empty_fibre_labels": [3],
        },
        "explicit_pairs": [
            {
                "pair_index": index,
                "e_names": sorted(e_names),
                "h_names": sorted(h_names),
                "e_edges": [list(edge) for edge in sorted(e_set)],
                "h_edges": [list(edge) for edge in sorted(h_set)],
                "disjoint": not bool(e_set & h_set),
                "partitions_complement": (e_set | h_set) == QUOTIENT_COMPLEMENT,
            }
            for index, ((e_names, h_names), (e_set, h_set)) in enumerate(
                zip(PAIR_NAMES, PAIRS, strict=True), start=1
            )
        ],
        "fibre_signatures": {
            "rows": [
                {"label": u, "star_names": sorted(name for name, edge in EDGE_NAMES.items() if edge in rows[u]), "signature": signature(rows[u])}
                for u in range(8) if rows[u]
            ],
            "columns": [
                {"label": v, "star_names": sorted(name for name, edge in EDGE_NAMES.items() if edge in columns[v]), "signature": signature(columns[v])}
                for v in range(8) if columns[v]
            ],
        },
        "generator_separation": {
            "relevant_graph_edge_count": len(relevant),
            "coverage": coverage,
            "all_relevant_graph_edges_separated": True,
            "proved_upper_bound": "rho(Q16)<=sigma(Q16)<=3",
            "lifted_upper_bound": "rho(G16)<=rho(Q16)<=3",
        },
        "canonical_exhaustive_support": {
            "canonical_graph_edges": exact_canonical.canonical_edges,
            "distinct_maximal_pair_masks": exact_canonical.distinct_maximal_pair_masks,
            "minimum_pairs": exact_canonical.minimum_pairs,
            "authority": "RETROSPECTIVE_COMPUTATIONAL_CORROBORATION_NOT_PROOF",
        },
        "scope": {
            "proves_explicit_upper_bound_only": True,
            "grants_exact_quotient_value": False,
            "grants_uniform_quotient_bound": False,
            "grants_recurrence": False,
            "grants_circuit_lower_bound": False,
            "grants_p_vs_np_authority": False,
            "computation_is_proof": False,
            "independent_peer_review": False,
        },
        "artifact_hash": "",
    }
    receipt["artifact_hash"] = _canonical_hash(receipt)
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(build_receipt(), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
