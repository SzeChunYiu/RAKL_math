"""Frozen finite corroborator for the C043 first residual-language split.

The generated receipt is assurance for explicit finite witnesses.  Mathematical
truth must come from the length, clause, residual-equivalence, band-support and
type-class arguments recorded with the result.  No LP is run.
"""

from __future__ import annotations

import argparse
import copy
from dataclasses import asdict
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PNP = HERE.parent
CANDIDATE_PATH = PNP / "04_candidates/C041_fx_sat_one_sided.py"
SPARSE_PATH = HERE / "c041_sparse_bridge_repair.py"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load frozen module {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


candidate = _load("c043_frozen_decoder", CANDIDATE_PATH)
sparse = _load("c043_sparse_semantics", SPARSE_PATH)


def gamma_length(value: int) -> int:
    if value < 1:
        raise ValueError("positive integer required")
    return 2 * value.bit_length() - 1


def unpadded_length(variable_count: int, clause_count: int) -> int:
    width = variable_count.bit_length()
    return (
        len(candidate.MAGIC)
        + gamma_length(variable_count)
        + gamma_length(clause_count)
        + 3 * clause_count * (1 + width)
    )


def canonical_even_length(variable_count: int, clause_count: int) -> int:
    raw = unpadded_length(variable_count, clause_count)
    return raw + raw % 2


def parameter_pairs_for_length(length: int) -> tuple[tuple[int, int], ...]:
    if length < 1 or length % 2:
        return ()
    pairs: list[tuple[int, int]] = []
    for variable_count in range(1, length + 1):
        for clause_count in range(1, length + 1):
            if canonical_even_length(variable_count, clause_count) == length:
                pairs.append((variable_count, clause_count))
    return tuple(pairs)


def _clause_options(variable_count: int):
    literals = tuple(
        (variable, negated)
        for variable in range(1, variable_count + 1)
        for negated in (False, True)
    )
    return tuple(product(literals, repeat=3))


def canonical_unsat_words(parent_level: int) -> tuple[str, ...]:
    length = 2 * parent_level
    words: set[str] = set()
    for variable_count, clause_count in parameter_pairs_for_length(length):
        # A single nonempty clause is always satisfiable, so avoid irrelevant
        # enumeration while retaining the analytic classification in output.
        if clause_count == 1:
            continue
        clauses = _clause_options(variable_count)
        for ordered_clauses in product(clauses, repeat=clause_count):
            formula = candidate.Formula3CNF(
                variable_count,
                tuple(tuple(clause) for clause in ordered_clauses),
                "CANONICAL_MAGIC_LONG_FORM",
            )
            encoded = candidate.encode_formula(formula)
            if len(encoded) != length:
                raise ArithmeticError("formula enumeration escaped length class")
            if not sparse.sparse_is_satisfiable(formula):
                words.add(encoded)
    return tuple(sorted(words))


def split_word(word: str) -> tuple[int, int]:
    half = len(word) // 2
    return int(word[:half], 2), int(word[half:], 2)


def cross_unsat_pairs(parent_level: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        sorted({(0, 0), *(split_word(word) for word in canonical_unsat_words(parent_level))})
    )


def recursive_complement(level: int) -> set[tuple[int, int]]:
    if level < candidate.SEED_LEVEL:
        raise ValueError("family starts at level 2")
    complement = set(candidate.SEED_COMPLEMENT)
    for parent_level in range(candidate.SEED_LEVEL, level):
        old_side = 1 << parent_level
        complement.update(
            (row, old_side + offset)
            for row, offset in cross_unsat_pairs(parent_level)
        )
    return complement


def _types(
    side: int, complement: set[tuple[int, int]], *, rows: bool
) -> tuple[list[dict[str, object]], dict[int, int]]:
    adjacency: dict[int, list[int]] = {}
    for row, column in sorted(complement):
        vertex, other = (row, column) if rows else (column, row)
        adjacency.setdefault(vertex, []).append(other)
    signatures: dict[tuple[int, ...], list[int]] = {}
    for vertex in range(side):
        signatures.setdefault(tuple(adjacency.get(vertex, ())), []).append(vertex)
    records: list[dict[str, object]] = []
    type_of: dict[int, int] = {}
    for index, (signature, vertices) in enumerate(
        sorted(signatures.items(), key=lambda item: (item[1][0], item[0]))
    ):
        records.append(
            {
                "type_index": index,
                "representative": vertices[0],
                "class_size": len(vertices),
                "vertices": vertices if len(vertices) <= 16 else vertices[:16],
                "vertices_truncated": len(vertices) > 16,
                "complement_neighborhood": list(signature),
            }
        )
        type_of.update({vertex: index for vertex in vertices})
    return records, type_of


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def build_receipt() -> dict[str, object]:
    length_classes = []
    for length in (26, 28, 30):
        parent_level = length // 2
        words = canonical_unsat_words(parent_level)
        length_classes.append(
            {
                "word_length": length,
                "parent_level": parent_level,
                "canonical_parameter_pairs": [
                    list(pair) for pair in parameter_pairs_for_length(length)
                ],
                "canonical_unsat_count": len(words),
                "canonical_unsat_words": list(words),
            }
        )

    words_15 = canonical_unsat_words(15)
    row_residuals: dict[int, list[int]] = {}
    suffix_prefixes: dict[int, list[int]] = {}
    for word in words_15:
        row, suffix = split_word(word)
        row_residuals.setdefault(row, []).append(suffix)
        suffix_prefixes.setdefault(suffix, []).append(row)
    for values in row_residuals.values():
        values.sort()
    for values in suffix_prefixes.values():
        values.sort()

    row_residual_classes: dict[tuple[int, ...], list[int]] = {}
    for row, suffixes in sorted(row_residuals.items()):
        row_residual_classes.setdefault(tuple(suffixes), []).append(row)
    column_neighborhood_classes: dict[tuple[int, ...], list[int]] = {}
    for suffix, rows in sorted(suffix_prefixes.items()):
        column_neighborhood_classes.setdefault(tuple(rows), []).append(suffix)

    complement = recursive_complement(16)
    side = 1 << 16
    row_types, row_type_of = _types(side, complement, rows=True)
    column_types, column_type_of = _types(side, complement, rows=False)
    quotient_complement = sorted(
        {(row_type_of[row], column_type_of[column]) for row, column in complement}
    )

    receipt: dict[str, object] = {
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C043-FIRST-ROW-SPLIT-GATE-20260812",
        "candidate_id": "C043-FIRST-ROW-SPLIT-RESIDUAL-v1",
        "length_formula": "L0(v,m)=8+gamma_len(v)+gamma_len(m)+3m(1+bit_length(v)); L=L0+(L0 mod 2)",
        "length_classes": length_classes,
        "parent_15_new_band": {
            "canonical_unsat_count": len(words_15),
            "active_rows": sorted(row_residuals),
            "row_residuals": [
                {"row": row, "suffixes": suffixes, "size": len(suffixes)}
                for row, suffixes in sorted(row_residuals.items())
            ],
            "row_residual_classes": [
                {"rows": rows, "suffixes": list(suffixes), "size": len(suffixes)}
                for suffixes, rows in sorted(
                    row_residual_classes.items(), key=lambda item: item[1]
                )
            ],
            "distinct_row_residual_count": len(row_residual_classes),
            "suffix_neighborhood_classes": [
                {"rows": list(rows), "suffixes": suffixes, "suffix_count": len(suffixes)}
                for rows, suffixes in sorted(
                    column_neighborhood_classes.items(), key=lambda item: item[0]
                )
            ],
            "distinct_nonempty_column_neighborhood_count": len(
                column_neighborhood_classes
            ),
        },
        "full_accumulated_G16": {
            "level": 16,
            "side": side,
            "complement_edge_count": len(complement),
            "row_types": row_types,
            "column_types": column_types,
            "row_type_count": len(row_types),
            "column_type_count": len(column_types),
            "quotient_complement": [list(edge) for edge in quotient_complement],
            "quotient_complement_edge_count": len(quotient_complement),
            "type_class_rectangle_upper_bound": min(len(row_types), len(column_types)),
            "rho_upper_bound_by_type_classes": min(len(row_types), len(column_types)),
        },
        "scope": {
            "proves_only_through_level": 16,
            "runs_full_cover_LP": False,
            "grants_quotient_cover_optimum": False,
            "grants_uniform_type_growth": False,
            "grants_recurrence": False,
            "grants_circuit_lower_bound": False,
            "grants_p_vs_np_authority": False,
            "computation_is_proof": False,
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
