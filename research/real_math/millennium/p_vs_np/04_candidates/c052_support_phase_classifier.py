"""Frozen-identity C052 target-blind support/phase classifier.

The classifier is purely syntactic.  It validates one explicit adjacent support
cell, then checks the local eight-coordinate forced-bit obstruction.  It does
not decode formulas, decide satisfiability, compare languages, or select a
native half-length.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
IDENTITY = ROOT / "research/real_math/millennium/p_vs_np/04_candidates/O9d12a2a1b_C052_TARGET_BLIND_CLASSIFIER_IDENTITY_20260812.json"
IDENTITY_RAW_SHA256 = "sha256:d9310cc4b4ff2823cadf0d2004869988b64f5857a7fc9b3ed0a14b9c0bf52e58"
IDENTITY_ID = "PNP-C052-TARGET-BLIND-TOTAL-SUPPORT-PHASE-CLASSIFIER-v1"
MAGIC = "11100101"


def _raw_length(a: int, m: int) -> int:
    return 6 + 2 * a + 2 * m.bit_length() + 3 * m * (1 + a)


def _payload_start(a: int, m: int) -> int:
    return 6 + 2 * a + 2 * m.bit_length()


def _raw_identity_sha() -> str:
    return "sha256:" + hashlib.sha256(IDENTITY.read_bytes()).hexdigest()


def _valid_positive_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _validate(cell: object) -> tuple[str | None, dict | None]:
    if _raw_identity_sha() != IDENTITY_RAW_SHA256:
        return "classifier identity bytes do not match the frozen public identity", None
    if not isinstance(cell, dict):
        return "input is not a complete symbolic support-cell record", None
    required = (
        "k", "a", "b", "m", "v_range", "parent_padding",
        "a_plus", "b_plus", "m_plus", "v_plus_range", "current_padding",
        "literal_index_quantifier", "literal_sign_quantifier",
    )
    missing = [name for name in required if name not in cell]
    if missing:
        return f"missing required fields: {missing}", None
    for name in ("k", "a", "b", "m", "a_plus", "b_plus", "m_plus"):
        if not _valid_positive_integer(cell[name]):
            return f"{name} is not a positive integer", None
    if cell["b"] != cell["m"].bit_length():
        return "b does not equal bit_length(m)", None
    if cell["b_plus"] != cell["m_plus"].bit_length():
        return "b_plus does not equal bit_length(m_plus)", None
    expected_v = [1 << (cell["a"] - 1), (1 << cell["a"]) - 1]
    expected_v_plus = [1 << (cell["a_plus"] - 1), (1 << cell["a_plus"]) - 1]
    if cell["v_range"] != expected_v:
        return "v_range does not cover the complete a-cell", None
    if cell["v_plus_range"] != expected_v_plus:
        return "v_plus_range does not cover the complete a_plus-cell", None
    if cell["literal_index_quantifier"] != "ALL_LEGAL_1_TO_V":
        return "literal-index quantifier is incomplete", None
    if cell["literal_sign_quantifier"] != "BOTH":
        return "literal-sign quantifier is incomplete", None
    parent_raw = _raw_length(cell["a"], cell["m"])
    current_raw = _raw_length(cell["a_plus"], cell["m_plus"])
    parent_padding = parent_raw % 2
    current_padding = current_raw % 2
    if cell["parent_padding"] != parent_padding:
        return "parent_padding was not derived as R mod 2", None
    if cell["current_padding"] != current_padding:
        return "current_padding was not derived as R_plus mod 2", None
    if parent_raw + parent_padding != 2 * cell["k"]:
        return "parent support equality R+padding=2k fails", None
    if current_raw + current_padding != 2 * (cell["k"] + 1):
        return "current support equality R_plus+padding_plus=2(k+1) fails", None
    return None, {
        "parent_raw_length": parent_raw,
        "parent_padding": parent_padding,
        "parent_encoded_length": parent_raw + parent_padding,
        "current_raw_length": current_raw,
        "current_padding": current_padding,
        "current_encoded_length": current_raw + current_padding,
        "v_range": expected_v,
        "v_plus_range": expected_v_plus,
    }


def _phase_values(a: int, phase: int) -> tuple[set[int], dict]:
    v_values = range(1 << (a - 1), 1 << a)
    if phase == 0:
        return {0, 1}, {
            "complete": True,
            "phase_kind": "literal_sign",
            "v_values": list(v_values),
            "legal_index_count": sum(v_values),
            "signs": [0, 1],
        }
    bit_offset = phase - 1
    values: set[int] = set()
    per_v: dict[str, int] = {}
    pairs = 0
    for v in v_values:
        per_v[str(v)] = v
        for index in range(1, v + 1):
            values.add(int(f"{index:0{a}b}"[bit_offset]))
            pairs += 1
    return values, {
        "complete": True,
        "phase_kind": "variable_index_bit",
        "bit_offset_from_most_significant": bit_offset,
        "v_values": list(v_values),
        "legal_indices_per_v": per_v,
        "v_index_pairs": pairs,
        "both_signs_per_index": True,
    }


def _cannot_check(reason: str) -> dict:
    return {
        "identity_id": IDENTITY_ID,
        "branch": "CANNOT_CHECK",
        "certificate": {
            "input_or_support_validation_failure": reason,
            "evidence_pointer_if_available": str(IDENTITY.relative_to(ROOT)),
        },
        "non_guarantees": ["no supported-cell semantic branch was reached"],
    }


def classify(cell: object) -> dict:
    failure, support = _validate(cell)
    if failure is not None or support is None:
        return _cannot_check(failure or "support validation failed")
    assert isinstance(cell, dict)
    a = cell["a"]
    m = cell["m"]
    k = cell["k"]
    payload_start = _payload_start(a, m)
    payload_end = support["parent_raw_length"]
    support_equalities = {
        **support,
        "parent_equation": f"{support['parent_raw_length']}+{support['parent_padding']}=2*{k}",
        "current_equation": f"{support['current_raw_length']}+{support['current_padding']}=2*({k}+1)",
    }
    if k < payload_start or k + 6 >= payload_end:
        return {
            "identity_id": IDENTITY_ID,
            "branch": "UNRESOLVED",
            "certificate": {
                "support_equalities": support_equalities,
                "failed_certificate_obligations": [
                    "h[1] through h[7] are not all inside the parent literal payload, so the frozen local token-phase certificate is inapplicable"
                ],
            },
            "non_guarantees": ["no conflict or escape certificate was validated"],
        }
    phi_c0 = (k - payload_start) % (1 + a)
    coordinates = [{
        "j": 0,
        "source": "h[0]=1 separately prepended",
        "possible_parent_bits": [1],
        "MAGIC_bit": int(MAGIC[0]),
        "universally_forced_unequal": False,
        "quantifier_coverage": {"not_a_parent_token": True},
    }]
    conflicts: list[dict] = []
    for j in range(1, 8):
        phase = (phi_c0 + j - 1) % (1 + a)
        values, audit = _phase_values(a, phase)
        mismatch = len(values) == 1 and next(iter(values)) != int(MAGIC[j])
        coordinate = {
            "j": j,
            "source": f"h[{j}]=x[{k + j - 1}]",
            "token_phase": phase,
            "possible_parent_bits": sorted(values),
            "MAGIC_bit": int(MAGIC[j]),
            "universally_forced_unequal": mismatch,
            "quantifier_coverage": audit,
        }
        coordinates.append(coordinate)
        if mismatch:
            conflicts.append(coordinate)
    if conflicts:
        first = conflicts[0]
        return {
            "identity_id": IDENTITY_ID,
            "branch": "FORCED_CONFLICT",
            "certificate": {
                "support_equalities": support_equalities,
                "phi_c0": phi_c0,
                "indexing": "h[0]=1 is prepended; h[1]=c[0]=x[k]",
                "coordinate_j": first["j"],
                "forced_parent_bit": first["possible_parent_bits"][0],
                "MAGIC_bit": first["MAGIC_bit"],
                "all_v_indices_signs_coverage_proof": first["quantifier_coverage"],
                "coordinates_0_through_7": coordinates,
            },
            "non_guarantees": ["bounded local syntactic conflict only", "not a theorem or P-versus-NP result"],
        }
    return {
        "identity_id": IDENTITY_ID,
        "branch": "ESCAPE_ADMISSIBLE",
        "certificate": {
            "support_equalities": support_equalities,
            "phi_c0": phi_c0,
            "indexing": "h[0]=1 is prepended; h[1]=c[0]=x[k]",
            "coordinates_0_through_7": coordinates,
            "universally_forced_unequal_coordinates": [],
            "no_universal_unequal_bit_proof": "Every payload coordinate audit is complete; none is both universally forced and unequal to its MAGIC coordinate.",
            "not_overlap_disclaimer": True,
        },
        "non_guarantees": [
            "not an intersection witness",
            "not a SAT or UNSAT result",
            "not a theorem or P-versus-NP result",
        ],
    }
