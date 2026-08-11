"""Frozen cheap structural gate for C041 decoder activation thresholds.

The executable output is finite verification support.  Mathematical authority
comes from the length lower bound, exact formula classification, twin-quotient
proof, and explicit intersection constructions recorded with the receipt.
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
PNP = HERE.parent
CANDIDATE_PATH = PNP / "04_candidates/C041_fx_sat_one_sided.py"
SPARSE_PATH = HERE / "c041_sparse_bridge_repair.py"
ORACLE_PATH = HERE / "full_cover_oracle.py"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


candidate = _load("c042_frozen_candidate", CANDIDATE_PATH)
sparse = _load("c042_sparse_semantics", SPARSE_PATH)
oracle = _load("c042_full_cover_oracle", ORACLE_PATH)


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


def cross_unsat_words(level: int) -> tuple[str, ...]:
    """Enumerate only all-zero plus MAGIC-prefixed words at one small level."""
    length = 2 * level
    if length < 2:
        return ()
    words: set[str] = {"0" * length}
    if length >= len(candidate.MAGIC):
        suffix_length = length - len(candidate.MAGIC)
        for suffix in range(1 << suffix_length):
            word = candidate.MAGIC + f"{suffix:0{suffix_length}b}"
            formula = candidate.decode_formula(word)
            if (
                formula.decoder_branch == "CANONICAL_MAGIC_LONG_FORM"
                and not sparse.sparse_is_satisfiable(formula)
            ):
                words.add(word)
    return tuple(sorted(words))


def word_pair(word: str) -> tuple[int, int]:
    half = len(word) // 2
    return int(word[:half], 2), int(word[half:], 2)


def recursive_complement(level: int) -> set[tuple[int, int]]:
    if level < candidate.SEED_LEVEL:
        raise ValueError("family starts at level 2")
    complement = set(candidate.SEED_COMPLEMENT)
    for parent_level in range(candidate.SEED_LEVEL, level):
        old_side = 1 << parent_level
        complement.update(
            (row, old_side + offset)
            for row, offset in map(word_pair, cross_unsat_words(parent_level))
        )
    return complement


def _types(
    side: int, complement: set[tuple[int, int]], *, rows: bool
) -> tuple[list[dict[str, object]], dict[int, int]]:
    signatures: dict[tuple[int, ...], list[int]] = {}
    adjacency: dict[int, list[int]] = {}
    for row, column in sorted(complement):
        vertex, other = (row, column) if rows else (column, row)
        adjacency.setdefault(vertex, []).append(other)
    for vertex in range(side):
        signature = tuple(adjacency.get(vertex, ()))
        signatures.setdefault(signature, []).append(vertex)
    result: list[dict[str, object]] = []
    type_of: dict[int, int] = {}
    for index, (signature, vertices) in enumerate(
        sorted(signatures.items(), key=lambda item: (item[1][0], item[0]))
    ):
        result.append(
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
    return result, type_of


def quotient_receipt(level: int) -> dict[str, object]:
    side = 1 << level
    complement = recursive_complement(level)
    row_types, row_type_of = _types(side, complement, rows=True)
    column_types, column_type_of = _types(side, complement, rows=False)
    quotient_complement = {
        (row_type_of[row], column_type_of[column]) for row, column in complement
    }
    if len(row_types) != len(column_types):
        raise ArithmeticError("frozen square quotient unexpectedly has unequal side types")
    qside = len(row_types)
    exact = oracle.exact_full_cover_number(qside, quotient_complement)
    return {
        "level": level,
        "side": side,
        "complement_edge_count": len(complement),
        "row_types": row_types,
        "column_types": column_types,
        "row_type_count": len(row_types),
        "column_type_count": len(column_types),
        "explicit_row_rectangle_count": len(row_types),
        "quotient_complement": [list(edge) for edge in sorted(quotient_complement)],
        "quotient_complement_edge_count": len(quotient_complement),
        "quotient_exact_full_cover_number": exact.minimum_pairs,
        "rho_full_upper_bound_by_quotient_lift": exact.minimum_pairs,
        "authority": "C013 twin-quotient lift plus exact bounded quotient cover; no asymptotic conclusion",
    }


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def build_receipt() -> dict[str, object]:
    level_rows: list[dict[str, object]] = []
    for level in range(2, 13):
        words = cross_unsat_words(level)
        canonical = [
            word
            for word in words
            if candidate.decode_formula(word).decoder_branch
            == "CANONICAL_MAGIC_LONG_FORM"
        ]
        level_rows.append(
            {
                "parent_level": level,
                "word_length": 2 * level,
                "all_unsat_words": list(words),
                "canonical_magic_unsat_words": canonical,
                "cross_unsat_pairs": [list(word_pair(word)) for word in words],
            }
        )

    receipt: dict[str, object] = {
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C042-ACTIVATION-QUOTIENT-GATE-20260812",
        "candidate_id": "C042-ACTIVATION-QUOTIENT-GATE-v1",
        "length_formula": "L0(v,m)=8+gamma_len(v)+gamma_len(m)+3m(1+bit_length(v)); L=L0+(L0 mod 2)",
        "frozen_threshold_claims": {
            "magic_prefix_first_parent_level": 4,
            "canonical_syntax_first_parent_level": 8,
            "canonical_unsat_first_parent_level": 12,
            "canonical_unsat_equality_parameters": {"v": 1, "m": 2},
        },
        "levels_2_through_12": level_rows,
        "first_syntax_child": quotient_receipt(9),
        "first_unsat_capable_child": quotient_receipt(13),
        "scope": {
            "proves_only_through_level": 13,
            "grants_uniform_quotient_bound": False,
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
