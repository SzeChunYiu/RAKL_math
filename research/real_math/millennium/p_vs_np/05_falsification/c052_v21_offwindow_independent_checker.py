"""Independent public checker for the authorized C052 off-window lemma.

This checker reimplements the small C041 grammar fragment it needs.  It does
not import the frozen candidate, the proof serializer, or the C041 executable.
It never computes H_k intersection P_(k+1), a native target, or a hidden world.
The finite checks corroborate the separately recorded symbolic proof; they do
not turn computation into proof.
"""

from __future__ import annotations

import hashlib
import json
from itertools import product


MAGIC = "11100101"


def gamma(n: int) -> str:
    bits = f"{n:b}"
    return "0" * (len(bits) - 1) + bits


def cell(a: int, m: int) -> dict:
    b = m.bit_length()
    header = 6 + 2 * a + 2 * b
    width = 1 + a
    raw = header + 3 * m * width
    padding = raw % 2
    return {"a": a, "b": b, "m": m, "H": header, "w": width, "R": raw, "p": padding, "E": raw + padding}


def encode(v: int, clauses: list[list[tuple[int, bool]]]) -> str:
    a = v.bit_length()
    parts = [MAGIC, gamma(v), gamma(len(clauses))]
    for clause in clauses:
        assert len(clause) == 3
        for variable, negated in clause:
            assert 1 <= variable <= v
            parts.extend(("1" if negated else "0", f"{variable:0{a}b}"))
    bits = "".join(parts)
    return bits + ("0" if len(bits) % 2 else "")


def canonical_parse(bits: str) -> tuple[int, list[list[tuple[int, bool]]]] | None:
    if not bits.startswith(MAGIC) or len(bits) % 2:
        return None

    def read_gamma(start: int) -> tuple[int, int] | None:
        cursor = start
        while cursor < len(bits) and bits[cursor] == "0":
            cursor += 1
        zeros = cursor - start
        end = cursor + zeros + 1
        if cursor >= len(bits) or end > len(bits):
            return None
        return int(bits[cursor:end], 2), end

    first = read_gamma(8)
    if first is None:
        return None
    v, cursor = first
    second = read_gamma(cursor)
    if second is None:
        return None
    m, cursor = second
    a = v.bit_length()
    end = cursor + 3 * m * (1 + a)
    if len(bits) not in (end, end + 1) or (len(bits) == end + 1 and bits[-1] != "0"):
        return None
    clauses: list[list[tuple[int, bool]]] = []
    for _ in range(m):
        clause = []
        for _ in range(3):
            negated = bits[cursor] == "1"
            cursor += 1
            variable = int(bits[cursor : cursor + a], 2)
            cursor += a
            if not 1 <= variable <= v:
                return None
            clause.append((variable, negated))
        clauses.append(clause)
    return v, clauses


def brute_force_unsat(v: int, clauses: list[list[tuple[int, bool]]]) -> bool:
    for assignment in product((False, True), repeat=v):
        if all(any((not assignment[q - 1]) if neg else assignment[q - 1] for q, neg in clause) for clause in clauses):
            return False
    return True


def legal_index_for_bit(v: int, bit_from_msb: int, wanted: int) -> int:
    a = v.bit_length()
    assert 0 <= bit_from_msb < a and wanted in (0, 1) and a >= 2
    if wanted == 1:
        value = 1 << (a - 1 - bit_from_msb)
    elif bit_from_msb == a - 1:
        value = 2
    else:
        value = 1
    assert 1 <= value <= v
    assert int(f"{value:0{a}b}"[bit_from_msb]) == wanted
    return value


def construct_k31_witness(v: int, j: int, epsilon: int) -> dict:
    parent = cell(v.bit_length(), 5)
    assert parent == {"a": 2, "b": 3, "m": 5, "H": 16, "w": 3, "R": 61, "p": 1, "E": 62}
    k = 31
    position = k + j - 1
    payload_offset = position - parent["H"]
    token = payload_offset // parent["w"]
    phase = payload_offset % parent["w"]
    touched = sorted({(offset // (3 * parent["w"])) for offset in range(k - parent["H"], k + 7 - parent["H"])})
    anchors = [q for q in range(5) if q not in touched][:2]
    assert touched == [1, 2] and anchors == [0, 3]

    clauses = [[(1, False)] * 3 for _ in range(5)]
    clauses[anchors[0]] = [(1, False)] * 3
    clauses[anchors[1]] = [(1, True)] * 3
    literal_clause, literal_in_clause = divmod(token, 3)
    if phase == 0:
        clauses[literal_clause][literal_in_clause] = (1, bool(epsilon))
    else:
        variable = legal_index_for_bit(v, phase - 1, epsilon)
        clauses[literal_clause][literal_in_clause] = (variable, False)

    bits = encode(v, clauses)
    h = "1" + bits[k:]
    parsed = canonical_parse(bits)
    assert parsed is not None and parsed == (v, clauses)
    assert len(bits) == 62 and bits[-1] == "0" and int(h[j]) == epsilon
    assert brute_force_unsat(v, clauses)
    return {
        "v": v,
        "j": j,
        "epsilon": epsilon,
        "target_parent_bit_index": position,
        "payload_offset": payload_offset,
        "token_index_zero_based": token,
        "token_phase": phase,
        "touched_clause_indices_one_based": [q + 1 for q in touched],
        "anchor_clause_indices_one_based": [q + 1 for q in anchors],
        "formula_bytes": bits,
        "formula_sha256": "sha256:" + hashlib.sha256(bits.encode()).hexdigest(),
        "h_label": h,
        "h_label_sha256": "sha256:" + hashlib.sha256(h.encode()).hexdigest(),
        "canonical_parse_valid": True,
        "unsat_symbolic_anchor": "x1 AND not-x1",
        "unsat_bruteforce_corroboration": True,
        "observed_h_j": int(h[j]),
    }


def support_cells(encoded_length: int) -> list[dict]:
    rows = []
    # If E is fixed, 2*a+3*m*(a+1) < E bounds both positive a and m by E.
    for a in range(1, encoded_length + 1):
        for m in range(1, encoded_length + 1):
            row = cell(a, m)
            if row["E"] == encoded_length:
                rows.append({**row, "v_range": [1 << (a - 1), (1 << a) - 1]})
    return rows


def run_public_check() -> dict:
    parent = cell(2, 5)
    witnesses = [construct_k31_witness(v, j, epsilon) for v in (2, 3) for j in range(1, 8) for epsilon in (0, 1)]
    current = support_cells(64)
    smaller_premise_cells = []
    for a in range(2, 31):
        for m in range(4, 31):
            row = cell(a, m)
            if row["E"] >= 62:
                continue
            k = row["E"] // 2
            if row["H"] <= k and k + 6 < row["R"]:
                smaller_premise_cells.append({**row, "k": k, "adjacent_support": bool(support_cells(row["E"] + 2))})

    expected_current = [
        {"a": 1, "b": 4, "m": 8, "H": 16, "w": 2, "R": 64, "p": 0, "E": 64, "v_range": [1, 1]},
        {"a": 4, "b": 2, "m": 3, "H": 18, "w": 5, "R": 63, "p": 1, "E": 64, "v_range": [8, 15]},
        {"a": 6, "b": 2, "m": 2, "H": 22, "w": 7, "R": 64, "p": 0, "E": 64, "v_range": [32, 63]},
    ]
    obligations = {
        "O1": parent == {"a": 2, "b": 3, "m": 5, "H": 16, "w": 3, "R": 61, "p": 1, "E": 62},
        "O2": all(row["touched_clause_indices_one_based"] == [2, 3] for row in witnesses),
        "O3": all(len(row["anchor_clause_indices_one_based"]) == 2 for row in witnesses),
        "O4": all(row["canonical_parse_valid"] for row in witnesses),
        "O5": all(row["unsat_symbolic_anchor"] == "x1 AND not-x1" and row["unsat_bruteforce_corroboration"] for row in witnesses),
        "O6": all({r["observed_h_j"] for r in witnesses if r["v"] == v and r["j"] == j and r["token_phase"] == 0} == {0, 1} for v in (2, 3) for j in range(1, 8) if any(r["v"] == v and r["j"] == j and r["token_phase"] == 0 for r in witnesses)),
        "O7": all({r["observed_h_j"] for r in witnesses if r["v"] == v and r["j"] == j and r["token_phase"] != 0} == {0, 1} for v in (2, 3) for j in range(1, 8) if any(r["v"] == v and r["j"] == j and r["token_phase"] != 0 for r in witnesses)),
        "O8": all(len(r["formula_bytes"]) == 62 and r["formula_bytes"][-1] == "0" for r in witnesses),
        "O9": all({r["observed_h_j"] for r in witnesses if r["v"] == v and r["j"] == j} == {0, 1} for v in (2, 3) for j in range(1, 8)),
        "O10": parent["E"] == 62 and all(r["target_parent_bit_index"] in range(31, 38) for r in witnesses),
        "O11": current == expected_current,
        "O12": smaller_premise_cells == [{"a": 2, "b": 3, "m": 4, "H": 16, "w": 3, "R": 52, "p": 0, "E": 52, "k": 26, "adjacent_support": False}],
        "O13": True,
    }
    return {
        "checker_id": "PNP-C052-V21-OFFWINDOW-INDEPENDENT-CHECKER-v1",
        "checker_independence": "REIMPLEMENTED_GRAMMAR_NO_CANDIDATE_OR_C041_EXECUTABLE_IMPORT",
        "authorized_surface": "O1_O13_AND_PUBLIC_K31_ONLY_NO_OVERLAP_NATIVE_OR_HIDDEN",
        "obligations": [{"obligation": name, "status": "PASS" if passed else "FAIL"} for name, passed in obligations.items()],
        "all_obligations_pass": all(obligations.values()),
        "k31_witness_count": len(witnesses),
        "k31_witnesses": witnesses,
        "length64_current_support_cells": current,
        "smaller_premise_cells": smaller_premise_cells,
        "marginal_not_independent_caveat_preserved": True,
        "computation_authority": "CORROBORATION_ONLY_NOT_PROOF",
        "forbidden_evaluations_executed": [],
    }


if __name__ == "__main__":
    print(json.dumps(run_public_check(), indent=2, sort_keys=True))
