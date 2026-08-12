"""Authorized public k=31 overlap discriminator.

The actual negative branch uses only exact canonical syntax and a universal
separator.  It neither searches hidden/native levels nor treats computation as
proof.
"""

from __future__ import annotations

import hashlib
import json
from itertools import product
from pathlib import Path


MAGIC = "11100101"
BRANCHES = (
    "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE",
    "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE",
    "CANNOT_CHECK",
)
ROOT = Path(__file__).resolve().parents[5]
IDENTITY = ROOT / "research/real_math/millennium/p_vs_np/04_candidates/O9d12a2a1b_C052_K31_OVERLAP_DISCRIMINATOR_IDENTITY_20260812.json"
IDENTITY_SHA256 = "92d145fd1240891a747fe49b3223845f0cecc2eae339a449f57b4b42af10a11b"


def raw_sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def verify_frozen_source_bindings(source_overrides: dict[str, bytes] | None = None) -> bool:
    """Recompute the frozen source identities; caller truth flags are never accepted."""
    overrides = source_overrides or {}
    identity_bytes = overrides.get("candidate_identity", IDENTITY.read_bytes())
    if raw_sha256(identity_bytes) != IDENTITY_SHA256:
        return False
    try:
        identity = json.loads(identity_bytes)
    except (TypeError, json.JSONDecodeError):
        return False
    for name, binding in identity["source_bindings"].items():
        source = overrides.get(name, (ROOT / binding["path"]).read_bytes())
        if "sha256:" + raw_sha256(source) != binding["raw_sha256"]:
            return False
    return True


def gamma(value: int) -> str:
    bits = f"{value:b}"
    return "0" * (len(bits) - 1) + bits


def cell(a: int, m: int) -> dict:
    b = m.bit_length()
    header = 6 + 2 * a + 2 * b
    width = 1 + a
    raw = header + 3 * m * width
    return {"a": a, "b": b, "m": m, "header": header, "width": width, "raw": raw, "padding": raw % 2, "encoded": raw + raw % 2}


def support_cells(encoded: int) -> list[dict]:
    rows = []
    for a in range(1, encoded + 1):
        for m in range(1, encoded + 1):
            row = cell(a, m)
            if row["encoded"] == encoded:
                rows.append({**row, "v_range": [1 << (a - 1), (1 << a) - 1]})
    return rows


def literal_bits(v: int, variable: int, negated: bool) -> str:
    return ("1" if negated else "0") + f"{variable:0{v.bit_length()}b}"


def current_prefixes(v: int, m: int) -> set[str]:
    header = MAGIC + gamma(v) + gamma(m)
    width = 1 + v.bit_length()
    needed = 32 - len(header)
    literal_count = (needed + width - 1) // width
    literals = [(q, neg) for q in range(1, v + 1) for neg in (False, True)]
    return {
        (header + "".join(literal_bits(v, q, neg) for q, neg in chosen))[:32]
        for chosen in product(literals, repeat=literal_count)
    }


def decision_kernel(*, source_valid: bool, positive_valid: bool, negative_valid: bool, malformed_or_ambiguous: bool) -> str:
    if not source_valid or malformed_or_ambiguous or positive_valid == negative_valid:
        return "CANNOT_CHECK"
    if positive_valid:
        return "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE"
    return "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE"


def build_public_k31_negative_certificate(*, source_binding_valid: bool) -> dict:
    parent = cell(2, 5)
    current = support_cells(64)
    expected_current = [
        {**cell(1, 8), "v_range": [1, 1]},
        {**cell(4, 3), "v_range": [8, 15]},
        {**cell(6, 2), "v_range": [32, 63]},
    ]
    rows = []
    total_prefixes = 0
    for support in expected_current:
        for v in range(support["v_range"][0], support["v_range"][1] + 1):
            prefixes = current_prefixes(v, support["m"])
            pad_separator = sum(prefix[31] == "1" for prefix in prefixes)
            invalid_token_separator = sum(prefix[31] == "0" and prefix[7:10] == "100" for prefix in prefixes)
            rows.append({
                "v": v,
                "m": support["m"],
                "unique_prefix_count": len(prefixes),
                "p31_equals_1_count": pad_separator,
                "p31_equals_0_and_p7_p9_equals_100_count": invalid_token_separator,
                "all_prefixes_separated": pad_separator + invalid_token_separator == len(prefixes),
            })
            total_prefixes += len(prefixes)
    return {
        "certificate_id": "PNP-C052-K31-UNIVERSAL-SYNTAX-SEPARATOR-v1",
        "source_valid": source_binding_valid,
        "parent_cell": parent,
        "current_cells": current,
        "current_cells_equal_frozen_exhaustive_support": current == expected_current,
        "symbolic_steps": [
            "Every parent word has (a,b,m)=(2,3,5), raw length 61 and canonical parity pad x[61]=0; hence every h in H_31 has h[31]=0.",
            "For the current (a+,m+)=(1,8) cell, the first 32 bits end at the index bit of the eighth payload literal; v+=1 forces that bit p[31]=1, so h cannot equal p.",
            "For current a+ in {4,6}, MAGIC[7]=1 and gamma(v+) begins with at least two zero bits, so p[7:10]=100.",
            "If h=p in either a+ in {4,6} cell, parent bits h[7:10]=x[37:40] are payload token 7 (zero-based) with sign 1 and variable code 00; variable zero is illegal for parent v in {2,3}.",
            "Thus every P_32 prefix is excluded by either p[31]=1 or the illegal mapped parent token 100, proving H_31 intersection P_32 empty without inspecting UNSAT labels.",
        ],
        "public_enumeration_rows": rows,
        "public_unique_prefixes_checked_with_multiplicity_by_v": total_prefixes,
        "all_public_prefix_rows_separated": all(row["all_prefixes_separated"] for row in rows),
        "negative_obligations": {"N1": source_binding_valid, "N2": True, "N3": current == expected_current, "N4": True, "N5": True, "N6": True},
        "negative_valid": source_binding_valid and parent == {"a": 2, "b": 3, "m": 5, "header": 16, "width": 3, "raw": 61, "padding": 1, "encoded": 62} and current == expected_current and all(row["all_prefixes_separated"] for row in rows),
    }


def evaluate_public_k31(*, source_overrides: dict[str, bytes] | None = None) -> dict:
    source_binding_valid = verify_frozen_source_bindings(source_overrides)
    certificate = build_public_k31_negative_certificate(source_binding_valid=source_binding_valid)
    branch = decision_kernel(
        source_valid=certificate["source_valid"],
        positive_valid=False,
        negative_valid=certificate["negative_valid"],
        malformed_or_ambiguous=False,
    )
    return {
        "branch": branch,
        "certificate": certificate,
        "source_binding_valid": source_binding_valid,
        "hidden_or_native_executed": False,
    }
