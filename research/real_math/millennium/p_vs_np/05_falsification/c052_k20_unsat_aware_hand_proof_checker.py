"""Exact checker for the retrospective C052 k=20 local-obstruction lemma.

The checker constructs a family of plainly contradictory two-clause formulas
inside the semantic parent set H_20.  It is intentionally independent of the
v1 classifier and its falsifier.  This is a same-context exact checker, not a
formal proof assistant or independent peer review.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
OUTPUT = BASE / "04_candidates/O9d12a2a1b_C052_K20_UNSAT_AWARE_LOCAL_ESCAPE_HAND_PROOF_20260812.json"
MAGIC = "11100101"


def gamma(value: int) -> str:
    bits = f"{value:b}"
    return "0" * (len(bits) - 1) + bits


def contradictory_unit_pair(v: int, r: int, order: str) -> tuple[str, str]:
    if not 4 <= v <= 7 or not 1 <= r <= v:
        raise ValueError("witness lies outside the frozen a=3 cell")
    if order not in {"positive_then_negative", "negative_then_positive"}:
        raise ValueError("unknown clause order")
    positive = [(0, r)] * 3
    negative = [(1, r)] * 3
    tokens = positive + negative if order == "positive_then_negative" else negative + positive
    payload = "".join(str(sign) + f"{index:03b}" for sign, index in tokens)
    word = MAGIC + gamma(v) + gamma(2) + payload
    if len(word) != 40:
        raise AssertionError("the exact parent support length is not 40")
    return word, "1" + word[20:]


def clause_value(clause: list[tuple[int, int]], assignment: tuple[bool, ...]) -> bool:
    return any((not assignment[index - 1]) if sign else assignment[index - 1] for sign, index in clause)


def opposite_unit_pair_is_unsat(v: int, r: int, order: str) -> bool:
    positive = [(0, r)] * 3
    negative = [(1, r)] * 3
    clauses = [positive, negative] if order == "positive_then_negative" else [negative, positive]
    for mask in range(1 << v):
        assignment = tuple(bool(mask & (1 << offset)) for offset in range(v))
        if all(clause_value(clause, assignment) for clause in clauses):
            return False
    return True


def _seal(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


def build_proof() -> dict:
    family: list[dict] = []
    for v in range(4, 8):
        for r in range(1, v + 1):
            for order in ("positive_then_negative", "negative_then_positive"):
                word, h = contradictory_unit_pair(v, r, order)
                if not opposite_unit_pair_is_unsat(v, r, order):
                    raise AssertionError("opposite repeated unit clauses unexpectedly admit an assignment")
                family.append({
                    "witness_id": f"H20-v{v}-r{r}-{'PN' if order == 'positive_then_negative' else 'NP'}",
                    "v": v,
                    "r": r,
                    "m": 2,
                    "clause_order": order,
                    "formula": (
                        f"(x_{r} OR x_{r} OR x_{r}) AND (not x_{r} OR not x_{r} OR not x_{r})"
                        if order == "positive_then_negative"
                        else f"(not x_{r} OR not x_{r} OR not x_{r}) AND (x_{r} OR x_{r} OR x_{r})"
                    ),
                    "unsat_proof": "opposite repeated unit clauses",
                    "truth_table_assignments_checked": 1 << v,
                    "satisfying_assignments": 0,
                    "word": word,
                    "word_length": len(word),
                    "h_label": h,
                    "h_0_through_7": h[:8],
                })
    coordinate_attainment: list[dict] = []
    for j, magic_bit in enumerate(MAGIC):
        values = sorted({int(item["h_label"][j]) for item in family})
        witnesses_by_bit = {
            str(bit): next(item["witness_id"] for item in family if int(item["h_label"][j]) == bit)
            for bit in values
        }
        coordinate_attainment.append({
            "j": j,
            "source": (
                "h[0]=1 separately prepended"
                if j == 0
                else f"h[{j}]=x[{20 + j - 1}]"
            ),
            "attained_bits_in_H20": values,
            "witnesses_by_bit": witnesses_by_bit,
            "magic_bit": int(magic_bit),
            "universally_forced_unequal": len(values) == 1 and values[0] != int(magic_bit),
        })
    if coordinate_attainment[0]["attained_bits_in_H20"] != [1]:
        raise AssertionError("h[0] indexing is wrong")
    if any(item["attained_bits_in_H20"] != [0, 1] for item in coordinate_attainment[1:]):
        raise AssertionError("the UNSAT-preserving family does not vary every payload coordinate")
    return _seal({
        "schema_version": "1.0.0",
        "proof_id": "PNP-C052-K20-UNSAT-AWARE-LOCAL-ESCAPE-HAND-PROOF-20260812",
        "atom_id": "O9d12a2a1b-C052",
        "candidate_lineage": {
            "frozen_v1_identity": "PNP-C052-TARGET-BLIND-TOTAL-SUPPORT-PHASE-CLASSIFIER-v1",
            "v1_semantic_status": "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT",
            "relation": "POST_RESULT_REPAIRED_SCOPED_PROOF_NOT_RETROACTIVE_VALIDATOR_REPAIR",
        },
        "claim": "Within H_20, no coordinate j in 0..7 is universally fixed to a bit unequal to MAGIC[j].",
        "support_derivation": {
            "parent": "H=16, w=4, R=16+3*2*4=40, padding=0, k=20",
            "current": "H_plus=14, w_plus=3, R_plus=14+3*3*3=41, padding_plus=1, E_plus=42=2*(20+1)",
            "suffix_phase": "phi_c0=(20-16) mod 4=0",
            "index_map": "h[0]=1; h[1..4] are token-2 sign/index bits x[20..23]; h[5..7] are token-3 sign/first-two-index bits x[24..26]",
        },
        "hand_derivation": [
            "For every v in {4,5,6,7} and r in {1,...,v}, the two opposite repeated unit clauses are legal canonical 3CNF clauses and their conjunction is UNSAT: one forces x_r=true and the other forces x_r=false.",
            "Both clause orders remain UNSAT. Since h[1] is token-2's sign and h[5] is token-3's sign, reversing the clause order attains both 0 and 1 at each sign coordinate within H_20.",
            "For every v>=4, indices 1=001, 2=010, and 4=100 are legal. They attain both bit values in each of the three width-3 variable-index positions. Repetition inside each unit clause transfers this to token 2 (h[2..4]) and token 3 (h[6..7]).",
            "Thus h[0]=1 matches MAGIC[0], and every h[j] for 1<=j<=7 attains both 0 and 1 among explicit members of H_20. No such coordinate is universally forced unequal to MAGIC.",
        ],
        "unsat_preserving_witness_family": family,
        "coordinate_attainment": coordinate_attainment,
        "exact_result": "The k=20 support cell escapes the local eight-coordinate forced-MAGIC obstruction inside the semantic UNSAT parent set H_20.",
        "chronology": {
            "constructed_after_v1_result_access": True,
            "prospective_v1_validator_credit": False,
            "repairs_v1_authorization_retroactively": False,
            "strict_context_first_discovery_credit": False,
        },
        "authority": "RETROSPECTIVE_SAME_CONTEXT_EXACT_HAND_PROOF_CHECK_NOT_FORMAL_NOT_INDEPENDENT",
        "non_guarantees": [
            "not a repair or pass for the frozen v1 classifier/falsifier",
            "not an H_20 intersection P_21 witness",
            "not a decoder, SAT-oracle, cover, circuit, or P-versus-NP result",
            "not formal proof, novelty assurance, or independent peer review",
        ],
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def write() -> dict:
    proof = build_proof()
    OUTPUT.write_text(json.dumps(proof, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return proof


if __name__ == "__main__":
    write()
