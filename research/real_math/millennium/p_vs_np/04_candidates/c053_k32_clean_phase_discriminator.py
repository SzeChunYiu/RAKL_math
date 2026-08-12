"""Authorized C053 exact 32-pair clean-phase discriminator.

The mathematical authority is the explicit three-clause resolution proof in
the positive certificate.  Encoding, decoding, 33-bit comparison, and the
256-row truth table are exact corroboration only.
"""

from __future__ import annotations

import hashlib
import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
MAGIC = "11100101"
BRANCHES = (
    "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS",
    "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF",
    "CANNOT_CHECK",
)
POSITIVE = tuple(f"W{i}" for i in range(1, 8))
NEGATIVE = tuple([*(f"W{i}" for i in range(1, 7)), "W8"])
FROZEN = {
    "candidate": ("04_candidates/O9d12a2a1b_C053_K32_CLEAN_PHASE_COMPATIBILITY_IDENTITY_20260812.json", "78f4f33b0c9b73f9df6bcca661ec2cac3eac917866c02bcafd4aa5b5652e278f"),
    "evaluator": ("05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATOR_IDENTITY_20260812.json", "df6a58632f296525014c702eafc332a77a7ab8dd10e3d08599f20e438a5bf076"),
    "falsifier": ("05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_FALSIFIER_IDENTITY_20260812.json", "3edec6ab1e60260cbc9e462454941533879ce0f61c88bad1768608d75f30cebe"),
    "freeze_receipt": ("09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_CANDIDATE_FREEZE_RECEIPT_20260812.json", "71bdab0d7aedbf68a0cb82ad7198733e599c94964f165fcb096afec36fa2e8e2"),
    "authorization": ("09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATION_AUTHORIZATION_20260812.json", "75681baecee68576b32d14e1681916ebce675e88ada62ae791f45b0ed56ea935"),
    "c041": ("04_candidates/C041_fx_sat_one_sided.py", "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"),
}


def sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sources_hold(overrides: dict[str, bytes] | None = None) -> bool:
    supplied = overrides or {}
    return all(
        sha(supplied.get(name, (PNP / path).read_bytes())) == expected
        for name, (path, expected) in FROZEN.items()
    )


def gamma(value: int) -> str:
    bits = f"{value:b}"
    return "0" * (len(bits) - 1) + bits


def token(variable: int, negated: bool, width: int) -> str:
    return ("1" if negated else "0") + f"{variable:0{width - 1}b}"


def encode(v: int, clauses: tuple[tuple[tuple[int, bool], ...], ...]) -> str:
    result = MAGIC + gamma(v) + gamma(len(clauses)) + "".join(
        token(variable, negated, 1 + v.bit_length())
        for clause in clauses for variable, negated in clause
    )
    return result + ("0" if len(result) % 2 else "")


def parse_canonical(bits: str) -> dict | None:
    if len(bits) % 2 or not bits.startswith(MAGIC):
        return None
    cursor = len(MAGIC)

    def read_gamma(start: int) -> tuple[int, int] | None:
        zeros = 0
        while start + zeros < len(bits) and bits[start + zeros] == "0":
            zeros += 1
        lead = start + zeros
        end = lead + zeros + 1
        if lead >= len(bits) or end > len(bits):
            return None
        return int(bits[lead:end], 2), end

    first = read_gamma(cursor)
    if first is None:
        return None
    v, cursor = first
    second = read_gamma(cursor)
    if second is None:
        return None
    m, cursor = second
    width = 1 + v.bit_length()
    raw_end = cursor + 3 * m * width
    if len(bits) not in {raw_end, raw_end + 1} or (len(bits) == raw_end + 1 and bits[-1] != "0"):
        return None
    literals = []
    for _ in range(3 * m):
        block = bits[cursor:cursor + width]
        variable = int(block[1:], 2)
        if not 1 <= variable <= v:
            return None
        literals.append((variable, block[0] == "1"))
        cursor += width
    return {"v": v, "m": m, "width": width, "literals": tuple(literals), "raw_end": raw_end}


def clause_holds(clause: tuple[tuple[int, bool], ...], assignment: tuple[bool, ...]) -> bool:
    return any((not assignment[q - 1]) if negated else assignment[q - 1] for q, negated in clause)


def satisfying_assignments(v: int, clauses: tuple[tuple[tuple[int, bool], ...], ...]) -> list[tuple[bool, ...]]:
    return [a for a in product((False, True), repeat=v) if all(clause_holds(c, a) for c in clauses)]


def resolution_proof_holds(clauses: tuple[tuple[tuple[int, bool], ...], ...]) -> bool:
    normalized = [frozenset(clause) for clause in clauses]
    expected = [
        frozenset({(2, False), (5, True)}),
        frozenset({(2, True)}),
        frozenset({(2, False), (5, False)}),
    ]
    if normalized != expected:
        return False
    r1 = frozenset({(5, True)})       # resolve clause 0 with clause 1 on x2
    r2 = frozenset({(5, False)})      # resolve clause 2 with clause 1 on x2
    r3 = r1.difference({(5, True)}) | r2.difference({(5, False)})
    return r3 == frozenset()


def kernel(*, source_valid: bool, positive_valid: bool, negative_valid: bool, malformed: bool) -> str:
    if not source_valid or malformed or positive_valid == negative_valid:
        return "CANNOT_CHECK"
    return BRANCHES[0] if positive_valid else BRANCHES[1]


def frontend(*, positive: dict | None = None, negative: dict | None = None,
             overrides: dict[str, bytes] | None = None, malformed: bool = False) -> dict:
    pos = (positive or {}).get("positive_obligations")
    neg = (negative or {}).get("negative_obligations")
    positive_valid = isinstance(pos, dict) and set(pos) == set(POSITIVE) and all(pos.values())
    negative_valid = isinstance(neg, dict) and set(neg) == set(NEGATIVE) and all(neg.values())
    state = {"source_valid": sources_hold(overrides), "positive_valid": positive_valid,
             "negative_valid": negative_valid, "malformed": malformed}
    return {"kernel_input": state, "branch": kernel(**state)}


def build_hand_witness() -> dict:
    parent_clauses = (
        ((2, False), (2, False), (5, True)),
        ((2, True), (2, True), (2, True)),
        ((2, False), (2, False), (5, False)),
    )
    current_clauses = (
        ((2, False), (1, False), (1, False)),
        ((4, False), (1, False), (1, False)),
        ((1, False), (1, False), (1, False)),
        ((1, False), (1, False), (1, False)),
    )
    x = encode(8, parent_clauses)
    y = encode(5, current_clauses)
    h = "1" + x[32:]
    p = y[:33]
    parent = parse_canonical(x)
    current = parse_canonical(y)
    coordinate_rows = [{"j": j, "h": h[j], "p": p[j], "parent_coordinate": None if j == 0 else 31 + j}
                       for j in range(33)]
    forced_parent_tokens = [x[33 + 5 * i:38 + 5 * i] for i in range(6)]
    obligations = {
        "W1": sources_hold(),
        "W2": (8, 5) in {(v, vp) for v in range(8, 16) for vp in range(4, 8)},
        "W3": parent is not None and parent["v"] == 8 and parent["m"] == 3 and len(x) == 64 and x[-1] == "0",
        "W4": current is not None and current["v"] == 5 and current["m"] == 4 and len(y) == 66,
        "W5": h == p and len(h) == 33 and all(row["h"] == row["p"] for row in coordinate_rows),
        "W6": forced_parent_tokens == ["10010", "10010", "10010", "00010", "00010", "00101"],
        "W7": resolution_proof_holds(parent_clauses),
    }
    return {
        "parent_v": 8, "current_v": 5, "parent_clauses": parent_clauses,
        "current_clauses": current_clauses, "x": x, "y": y, "h": h, "p": p,
        "coordinate_rows": coordinate_rows, "forced_parent_tokens_3_through_8": forced_parent_tokens,
        "parent_parse": parent, "current_parse": current,
        "resolution_proof_valid": resolution_proof_holds(parent_clauses),
        "truth_table_satisfying_assignment_count": len(satisfying_assignments(8, parent_clauses)),
        "positive_obligations": obligations,
    }


def evaluate() -> dict:
    witness = build_hand_witness()
    routed = frontend(positive=witness)
    return {"branch": routed["branch"], "frontend_kernel_input": routed["kernel_input"],
            "witness": witness, "computation_authority": "EXACT_CORROBORATION_ONLY_HAND_RESOLUTION_IS_PROOF"}


if __name__ == "__main__":
    print(json.dumps(evaluate(), indent=2, sort_keys=True))
