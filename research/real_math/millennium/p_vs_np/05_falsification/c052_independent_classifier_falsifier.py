"""Independent hostile falsifier for the frozen C052 classifier identity.

The arithmetic, phase, indexing, and quantifier audit are repeated here from
the public grammar.  No candidate module or candidate-produced certificate is
used as an input to the recomputation.
"""

from __future__ import annotations


MAGIC = "11100101"
FALSIFIER_ID = "PNP-C052-INDEPENDENT-HOSTILE-SUPPORTED-CELL-FALSIFIER-v1"


def _positive_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _raw_length(a: int, m: int) -> int:
    return 6 + 2 * a + 2 * m.bit_length() + 3 * m * (1 + a)


def _header_length(a: int, m: int) -> int:
    return 6 + 2 * a + 2 * m.bit_length()


def _support(cell: object) -> tuple[str | None, dict | None]:
    if not isinstance(cell, dict):
        return "input is not a mapping", None
    required = (
        "k", "a", "b", "m", "v_range", "parent_padding",
        "a_plus", "b_plus", "m_plus", "v_plus_range", "current_padding",
        "literal_index_quantifier", "literal_sign_quantifier",
    )
    missing = [key for key in required if key not in cell]
    if missing:
        return f"missing fields {missing}", None
    for key in ("k", "a", "b", "m", "a_plus", "b_plus", "m_plus"):
        if not _positive_integer(cell[key]):
            return f"invalid positive integer {key}", None
    if cell["b"] != cell["m"].bit_length() or cell["b_plus"] != cell["m_plus"].bit_length():
        return "bit-length coordinate mismatch", None
    v_range = [1 << (cell["a"] - 1), (1 << cell["a"]) - 1]
    v_plus_range = [1 << (cell["a_plus"] - 1), (1 << cell["a_plus"]) - 1]
    if cell["v_range"] != v_range or cell["v_plus_range"] != v_plus_range:
        return "incomplete variable-count cell", None
    if cell["literal_index_quantifier"] != "ALL_LEGAL_1_TO_V" or cell["literal_sign_quantifier"] != "BOTH":
        return "incomplete literal quantifier coverage", None
    parent_raw = _raw_length(cell["a"], cell["m"])
    current_raw = _raw_length(cell["a_plus"], cell["m_plus"])
    if cell["parent_padding"] != parent_raw % 2:
        return "parent padding mismatch", None
    if cell["current_padding"] != current_raw % 2:
        return "current padding mismatch", None
    if parent_raw + parent_raw % 2 != 2 * cell["k"]:
        return "parent support mismatch", None
    if current_raw + current_raw % 2 != 2 * (cell["k"] + 1):
        return "current support mismatch", None
    return None, {
        "parent_raw": parent_raw,
        "parent_padding": parent_raw % 2,
        "current_raw": current_raw,
        "current_padding": current_raw % 2,
        "v_range": v_range,
        "v_plus_range": v_plus_range,
    }


def _possible_bits(a: int, phase: int) -> tuple[set[int], dict]:
    v_values = list(range(1 << (a - 1), 1 << a))
    if phase == 0:
        return {0, 1}, {
            "kind": "sign",
            "v_values": v_values,
            "indices": sum(v_values),
            "signs": [0, 1],
            "complete": True,
        }
    offset = phase - 1
    values: set[int] = set()
    per_v: dict[str, list[int]] = {}
    for v in v_values:
        indices = list(range(1, v + 1))
        per_v[str(v)] = indices
        for index in indices:
            values.add(int(format(index, f"0{a}b")[offset]))
    return values, {
        "kind": "variable_index_bit",
        "offset": offset,
        "v_values": v_values,
        "legal_indices_by_v": per_v,
        "both_signs_for_every_index": True,
        "complete": True,
    }


def _recompute(cell: object) -> dict:
    failure, support = _support(cell)
    if failure is not None or support is None:
        return {"branch": "CANNOT_CHECK", "reason": failure or "support failure"}
    assert isinstance(cell, dict)
    a, m, k = cell["a"], cell["m"], cell["k"]
    header = _header_length(a, m)
    if k < header or k + 6 >= support["parent_raw"]:
        return {
            "branch": "UNRESOLVED",
            "reason": "eight-coordinate window is not wholly in the literal payload",
            "support": support,
        }
    phi = (k - header) % (1 + a)
    coordinates = [{
        "j": 0,
        "possible_bits": [1],
        "magic_bit": int(MAGIC[0]),
        "unequal": False,
        "coverage": {"h0_separate": True},
    }]
    conflicts: list[dict] = []
    for j in range(1, 8):
        phase = (phi + j - 1) % (1 + a)
        values, coverage = _possible_bits(a, phase)
        unequal = len(values) == 1 and next(iter(values)) != int(MAGIC[j])
        record = {
            "j": j,
            "source_index": k + j - 1,
            "phase": phase,
            "possible_bits": sorted(values),
            "magic_bit": int(MAGIC[j]),
            "unequal": unequal,
            "coverage": coverage,
        }
        coordinates.append(record)
        if unequal:
            conflicts.append(record)
    return {
        "branch": "FORCED_CONFLICT" if conflicts else "ESCAPE_ADMISSIBLE",
        "support": support,
        "phi_c0": phi,
        "indexing": "h[0] separate; h[1]=c[0]=x[k]",
        "coordinates": coordinates,
        "first_conflict": conflicts[0] if conflicts else None,
        "all_v_indices_signs_covered": True,
    }


def _certificate_matches(expected: dict, claimed: dict) -> tuple[bool, str]:
    certificate = claimed.get("certificate")
    if not isinstance(certificate, dict):
        return False, "claimed certificate is absent or malformed"
    branch = expected["branch"]
    if branch == "FORCED_CONFLICT":
        conflict = expected["first_conflict"]
        if certificate.get("coordinate_j") != conflict["j"]:
            return False, "claimed separating coordinate differs from recomputation"
        if certificate.get("forced_parent_bit") != conflict["possible_bits"][0]:
            return False, "claimed forced parent bit differs from recomputation"
        if certificate.get("MAGIC_bit") != conflict["magic_bit"]:
            return False, "claimed MAGIC bit differs from recomputation"
        coverage = certificate.get("all_v_indices_signs_coverage_proof", {})
        if coverage.get("complete") is not True:
            return False, "claimed quantifier coverage is incomplete"
    elif branch == "ESCAPE_ADMISSIBLE":
        if certificate.get("universally_forced_unequal_coordinates") != []:
            return False, "escape certificate reports a forced unequal coordinate"
        if certificate.get("not_overlap_disclaimer") is not True:
            return False, "escape certificate omits its non-intersection disclaimer"
    elif branch == "UNRESOLVED":
        if not certificate.get("failed_certificate_obligations"):
            return False, "unresolved certificate has no failed obligation"
    elif branch == "CANNOT_CHECK":
        if not certificate.get("input_or_support_validation_failure"):
            return False, "cannot-check certificate has no validation failure"
    return True, "claimed certificate agrees with independent recomputation"


def audit(cell: object, claimed: object) -> dict:
    expected = _recompute(cell)
    if not isinstance(claimed, dict):
        return {
            "falsifier_id": FALSIFIER_ID,
            "outcome": "CLASSIFIER_FALSIFIED",
            "expected_branch": expected["branch"],
            "reason": "claimed result is not a mapping",
            "recomputed_support_phase_quantifier_coverage": True,
            "classifier_certificate_reused": False,
        }
    branch_matches = claimed.get("branch") == expected["branch"]
    certificate_matches, reason = _certificate_matches(expected, claimed) if branch_matches else (False, "claimed branch differs from independent recomputation")
    return {
        "falsifier_id": FALSIFIER_ID,
        "outcome": "CLASSIFIER_SURVIVES" if branch_matches and certificate_matches else "CLASSIFIER_FALSIFIED",
        "expected_branch": expected["branch"],
        "claimed_branch": claimed.get("branch"),
        "reason": reason,
        "recomputed_support_phase_quantifier_coverage": True,
        "classifier_certificate_reused": False,
        "independent_recomputation": expected,
    }
