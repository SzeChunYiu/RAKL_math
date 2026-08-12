"""Independently materialize the frozen C052 controlled hostile world.

This bounded symbolic solver uses only the published length grammar.  It does
not import the candidate implementation, inspect semantic formula outcomes, or
compare the two languages.  The selected cell is a validator world, not a
native research target.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
AUTHORIZATION = BASE / "09_trace/O9d12a2a1b_C052_EVALUATION_AUTHORIZATION_20260812.json"
OUTPUT = BASE / "05_falsification/O9d12a2a1b_C052_HOSTILE_SUPPORTED_ESCAPE_CELL_20260812.json"
MAGIC = "11100101"
SELECTION_RULE = "INDEPENDENT-SYMBOLIC-SUPPORT-SOLVER-WITH-NO-FORCED-MAGIC-CONFLICT-v1"


def header_length(a: int, b: int) -> int:
    return 6 + 2 * a + 2 * b


def raw_length(a: int, m: int) -> int:
    b = m.bit_length()
    return header_length(a, b) + 3 * m * (1 + a)


def encoded_length(a: int, m: int) -> int:
    raw = raw_length(a, m)
    return raw + raw % 2


def payload_bit_values(a: int, phase: int) -> tuple[set[int], dict]:
    """Audit every v and legal index in an a-cell for one token phase."""
    v_values = range(1 << (a - 1), 1 << a)
    if phase == 0:
        return {0, 1}, {
            "phase_kind": "literal_sign",
            "signs_covered": [0, 1],
            "v_values_covered": list(v_values),
            "legal_index_count": sum(v for v in v_values),
        }
    bit_offset = phase - 1
    observed: set[int] = set()
    pair_count = 0
    per_v_counts: dict[str, int] = {}
    for v in v_values:
        per_v_counts[str(v)] = v
        for index in range(1, v + 1):
            observed.add(int(f"{index:0{a}b}"[bit_offset]))
            pair_count += 1
    return observed, {
        "phase_kind": "variable_index_bit",
        "bit_offset_from_most_significant": bit_offset,
        "v_values_covered": list(v_values),
        "legal_indices_per_v": per_v_counts,
        "v_index_pairs_covered": pair_count,
        "both_literal_signs_covered_per_index": True,
    }


def certificate_for(a: int, m: int, k: int) -> dict | None:
    b = m.bit_length()
    start = k
    payload_start = header_length(a, b)
    payload_end = raw_length(a, m)
    if start < payload_start or start + 6 >= payload_end:
        return None
    phase_c0 = (k - payload_start) % (1 + a)
    coordinates = [{
        "j": 0,
        "source": "separately_prepended_h0",
        "possible_parent_bits": [1],
        "magic_bit": int(MAGIC[0]),
        "universally_forced": True,
        "universally_forced_unequal": False,
        "quantifier_audit": {"not_a_parent_token": True},
    }]
    unequal: list[int] = []
    for j in range(1, 8):
        phase = (phase_c0 + j - 1) % (1 + a)
        values, audit = payload_bit_values(a, phase)
        forced = len(values) == 1
        mismatch = forced and next(iter(values)) != int(MAGIC[j])
        if mismatch:
            unequal.append(j)
        coordinates.append({
            "j": j,
            "source": f"h[{j}]=x[{k + j - 1}]",
            "token_phase": phase,
            "possible_parent_bits": sorted(values),
            "magic_bit": int(MAGIC[j]),
            "universally_forced": forced,
            "universally_forced_unequal": mismatch,
            "quantifier_audit": audit,
        })
    return {
        "phi_c0": phase_c0,
        "h0_indexing": "h[0]=1 is prepended and h[1]=c[0]=x[k]",
        "coordinates_0_through_7": coordinates,
        "all_h1_through_h7_in_literal_payload": True,
        "universally_forced_unequal_coordinates": unequal,
        "all_v_indices_and_both_signs_covered": True,
        "classifier_branch_expected": "ESCAPE_ADMISSIBLE" if not unequal else "FORCED_CONFLICT",
        "not_overlap_witness": not unequal,
    }


def _sealed(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


def materialize() -> dict:
    authorization = json.loads(AUTHORIZATION.read_text(encoding="utf-8"))
    rank = 0
    for k in range(8, 129):
        for a in range(1, 9):
            for m in range(2, 33):
                if encoded_length(a, m) != 2 * k:
                    continue
                certificate = certificate_for(a, m, k)
                if certificate is None or certificate["universally_forced_unequal_coordinates"]:
                    continue
                for a_plus in range(1, 9):
                    for m_plus in range(1, 33):
                        if encoded_length(a_plus, m_plus) != 2 * (k + 1):
                            continue
                        rank += 1
                        parent_raw = raw_length(a, m)
                        current_raw = raw_length(a_plus, m_plus)
                        cell = {
                            "k": k,
                            "a": a,
                            "b": m.bit_length(),
                            "m": m,
                            "v_range": [1 << (a - 1), (1 << a) - 1],
                            "a_plus": a_plus,
                            "b_plus": m_plus.bit_length(),
                            "m_plus": m_plus,
                            "v_plus_range": [1 << (a_plus - 1), (1 << a_plus) - 1],
                        }
                        receipt = _sealed({
                            "schema_version": "1.0.0",
                            "receipt_id": "PNP-C052-HOSTILE-SUPPORTED-ESCAPE-CELL-20260812",
                            "world_id": "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1",
                            "selection_rule_id": SELECTION_RULE,
                            "selection_rank": rank,
                            "authorization": {
                                "path": str(AUTHORIZATION.relative_to(ROOT)),
                                "artifact_hash": authorization["artifact_hash"],
                                "frozen_at_utc": authorization["frozen_at_utc"],
                            },
                            "cell": cell,
                            "support_checks": {
                                "parent_header_length": header_length(a, m.bit_length()),
                                "parent_raw_length": parent_raw,
                                "parent_padding": parent_raw % 2,
                                "parent_encoded_length": parent_raw + parent_raw % 2,
                                "current_header_length": header_length(a_plus, m_plus.bit_length()),
                                "current_raw_length": current_raw,
                                "current_padding": current_raw % 2,
                                "current_encoded_length": current_raw + current_raw % 2,
                                "parent_clause_count_allows_explicit_contradictory_pair": m >= 2,
                            },
                            "certificate": certificate,
                            "raw_pre_review_proposed_lesson": {
                                "status": "ZERO_CREDIT_SUPERSEDED_CERTIFICATE",
                                "attempted_implication": "The local support/phase obstruction might classify every adjacent supported cell as a forced MAGIC conflict, as in C050 and C051.",
                                "exact_result_or_failure": "The lexicographically first authorized controlled hostile cell has exact adjacent support but no universally forced unequal coordinate among h[0] through h[7].",
                                "supported_and_competing_causes": "Supported bounded cause: across the complete a-cell, every payload variable-bit phase occurring here attains both 0 and 1, while sign phases also attain both values. Rejected explanations are missing v values, a representative-only index check, chosen padding, h[0]/h[1] conflation, and an overlap computation.",
                                "scope": "This controlled symbolic cell and the local eight-coordinate forced-bit obstruction only; it is not a native target, language-intersection witness, theorem, or asymptotic result.",
                                "mathematical_falsifier": "A support arithmetic failure, an omitted v/index/sign case, or any j in 0..7 universally fixed to the complement of MAGIC[j] falsifies the escape certificate.",
                                "repair_or_next_discriminator": "Require the frozen classifier to reproduce C050 and C051 conflicts and this escape before any separately authorized native parametric classification.",
                                "proof_and_source_evidence": "Exact affine length equalities and exhaustive finite bit-domain quantifier audit recorded in this receipt; computation is a checked bounded certificate, not proof of language intersection or P versus NP.",
                            },
                            "authority": {
                                "bounded_symbolic_certificate": False,
                                "v1_evaluator_mathematical_credit": 0,
                                "computation_is_proof": False,
                                "same_context_independent_review": False,
                                "native_result": False,
                                "root": "OPEN_NO_SOLUTION_CERTIFICATE",
                            },
                        })
                        receipt["raw_pre_review_artifact_hash"] = receipt.pop("artifact_hash")
                        receipt["semantic_status_after_review"] = "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT"
                        receipt["native_gate_after_review"] = "BLOCKED"
                        receipt["superseding_review"] = "research/real_math/millennium/p_vs_np/08_reviews/O9d12a2a1b_C052_V1_CONTROLLED_SEMANTIC_FALSIFICATION_20260812.json"
                        receipt["raw_certificate_authority"] = "PRESERVED_RAW_V1_OUTPUT_ZERO_MATHEMATICAL_CREDIT"
                        return _sealed(receipt)
    raise RuntimeError("no eligible controlled hostile cell in the frozen bounded domain")


def write() -> dict:
    receipt = materialize()
    OUTPUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return receipt


if __name__ == "__main__":
    write()
