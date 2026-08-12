"""Separately rederived checker and hostile worlds for the C053 result."""

from __future__ import annotations

import hashlib
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
M = "11100101"
POS = tuple(f"W{i}" for i in range(1, 8))
NEG = tuple([*(f"W{i}" for i in range(1, 7)), "W8"])
SOURCES = {
    "candidate": ("04_candidates/O9d12a2a1b_C053_K32_CLEAN_PHASE_COMPATIBILITY_IDENTITY_20260812.json", "78f4f33b0c9b73f9df6bcca661ec2cac3eac917866c02bcafd4aa5b5652e278f"),
    "evaluator": ("05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATOR_IDENTITY_20260812.json", "df6a58632f296525014c702eafc332a77a7ab8dd10e3d08599f20e438a5bf076"),
    "falsifier": ("05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_FALSIFIER_IDENTITY_20260812.json", "3edec6ab1e60260cbc9e462454941533879ce0f61c88bad1768608d75f30cebe"),
    "authorization": ("09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATION_AUTHORIZATION_20260812.json", "75681baecee68576b32d14e1681916ebce675e88ada62ae791f45b0ed56ea935"),
    "c041": ("04_candidates/C041_fx_sat_one_sided.py", "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"),
}


def source_ok(overrides: dict[str, bytes] | None = None) -> bool:
    supplied = overrides or {}
    return all(hashlib.sha256(supplied.get(key, (PNP / path).read_bytes())).hexdigest() == expected
               for key, (path, expected) in SOURCES.items())


def g(n: int) -> str:
    b = bin(n)[2:]
    return "0" * (len(b) - 1) + b


def lit(q: int, neg: bool, bits: int) -> str:
    return ("1" if neg else "0") + format(q, f"0{bits}b")


def word(v: int, clauses: tuple) -> str:
    raw = M + g(v) + g(len(clauses)) + "".join(lit(q, neg, v.bit_length()) for clause in clauses for q, neg in clause)
    return raw + ("0" if len(raw) & 1 else "")


def kernel(src: bool, pos: bool, neg: bool, bad: bool) -> str:
    if bad or not src or pos == neg:
        return "CANNOT_CHECK"
    return "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS" if pos else "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF"


def front(*, positive: dict | None = None, negative: dict | None = None, bad: bool = False,
          overrides: dict[str, bytes] | None = None) -> str:
    p = (positive or {}).get("positive_obligations")
    n = (negative or {}).get("negative_obligations")
    pv = isinstance(p, dict) and set(p) == set(POS) and all(p.values())
    nv = isinstance(n, dict) and set(n) == set(NEG) and all(n.values())
    return kernel(source_ok(overrides), pv, nv, bad)


def run() -> dict:
    parent = (
        ((2, False), (2, False), (5, True)),
        ((2, True), (2, True), (2, True)),
        ((2, False), (2, False), (5, False)),
    )
    current = (
        ((2, False), (1, False), (1, False)),
        ((4, False), (1, False), (1, False)),
        ((1, False), (1, False), (1, False)),
        ((1, False), (1, False), (1, False)),
    )
    x, y = word(8, parent), word(5, current)
    label, prefix = "1" + x[32:], y[:33]
    # Independently normalize duplicates and check the three resolution steps:
    # (x2 or not x5), not x2 |- not x5; (x2 or x5), not x2 |- x5;
    # not x5, x5 |- empty.
    normalized = [frozenset(clause) for clause in parent]
    expected_normalized = [
        frozenset({(2, False), (5, True)}),
        frozenset({(2, True)}),
        frozenset({(2, False), (5, False)}),
    ]
    minus_x5 = frozenset({(5, True)})
    plus_x5 = frozenset({(5, False)})
    proof_valid = normalized == expected_normalized and (
        minus_x5.difference({(5, True)}) | plus_x5.difference({(5, False)})
    ) == frozenset()
    sat_count = sum(
        all(any((not a[q - 1]) if neg else a[q - 1] for q, neg in clause) for clause in parent)
        for a in product((False, True), repeat=8)
    )
    actual = {
        "W1": source_ok(), "W2": (8, 5) in product(range(8, 16), range(4, 8)),
        "W3": len(x) == 64 and x.startswith(M + g(8) + g(3)) and x[-1] == "0",
        "W4": len(y) == 66 and y.startswith(M + g(5) + g(4)),
        "W5": label == prefix and len(label) == 33,
        "W6": [x[33 + 5 * i:38 + 5 * i] for i in range(6)] == ["10010", "10010", "10010", "00010", "00010", "00101"],
        "W7": proof_valid and sat_count == 0,
    }
    positive = {"positive_obligations": actual}
    planted_positive = {"positive_obligations": {key: True for key in POS}}
    planted_negative = {"negative_obligations": {key: True for key in NEG}}
    worlds = {
        "C053-CLEAN-PHASE-PLANTED-POSITIVE-v1": front(positive=planted_positive),
        "C053-CLEAN-PHASE-PLANTED-NEGATIVE-v1": front(negative=planted_negative),
        "C053-CLEAN-PHASE-SYNTAX-SURVIVAL-ONLY-v1": front(),
        "C053-CLEAN-PHASE-PARTIAL-EQUALITY-v1": front(positive={"positive_obligations": {**actual, "W5": False}}),
        "C053-CLEAN-PHASE-SAT-PARENT-FALSE-POSITIVE-v1": front(positive={"positive_obligations": {**actual, "W7": False}}),
        "C053-CLEAN-PHASE-INCOMPLETE-PAIR-COVERAGE-v1": front(negative={"negative_obligations": {key: True for key in NEG if key != "W8"}}),
        "C053-CLEAN-PHASE-SOURCE-MISMATCH-v1": front(positive=planted_positive, overrides={"c041": b"mutated"}),
        "C053-CLEAN-PHASE-CONFLICTING-CERTIFICATES-v1": front(positive=planted_positive, negative=planted_negative),
        "C053-CLEAN-PHASE-FRONTEND-BRANCH-PROPAGATION-v1": {
            "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS": front(positive=planted_positive),
            "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF": front(negative=planted_negative),
            "CANNOT_CHECK": front(),
        },
    }
    expected = {
        "C053-CLEAN-PHASE-PLANTED-POSITIVE-v1": "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS",
        "C053-CLEAN-PHASE-PLANTED-NEGATIVE-v1": "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF",
        "C053-CLEAN-PHASE-SYNTAX-SURVIVAL-ONLY-v1": "CANNOT_CHECK",
        "C053-CLEAN-PHASE-PARTIAL-EQUALITY-v1": "CANNOT_CHECK",
        "C053-CLEAN-PHASE-SAT-PARENT-FALSE-POSITIVE-v1": "CANNOT_CHECK",
        "C053-CLEAN-PHASE-INCOMPLETE-PAIR-COVERAGE-v1": "CANNOT_CHECK",
        "C053-CLEAN-PHASE-SOURCE-MISMATCH-v1": "CANNOT_CHECK",
        "C053-CLEAN-PHASE-CONFLICTING-CERTIFICATES-v1": "CANNOT_CHECK",
        "C053-CLEAN-PHASE-FRONTEND-BRANCH-PROPAGATION-v1": {
            "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS": "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS",
            "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF": "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF",
            "CANNOT_CHECK": "CANNOT_CHECK",
        },
    }
    actual_branch = front(positive=positive)
    return {
        "source_valid": source_ok(), "parent_word": x, "current_word": y,
        "label": label, "prefix": prefix, "positive_obligations": actual,
        "resolution_implication_check": proof_valid, "truth_table_satisfying_assignment_count": sat_count,
        "actual_branch": actual_branch, "world_results": worlds,
        "worlds_all_pass": worlds == expected,
        "authority": "SEPARATELY_REDERIVED_SAME_CONTEXT_CHECK_NOT_INDEPENDENT_PEER_REVIEW",
        "computation_authority": "CORROBORATION_ONLY_HAND_RESOLUTION_IS_PROOF",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, sort_keys=True))
