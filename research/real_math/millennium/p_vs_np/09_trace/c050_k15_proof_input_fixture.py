"""Prospective hand-proof inputs for the public C050 k=15 candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


BASE = "research/real_math/millennium/p_vs_np"
RESULT_BASE_SHA = "02c5fb7764116cf075d8dd5efd7b6fe835275ab9"
PUBLIC_MERGE_SHA = "0b0f1840f99043a57050d625683ba8311fef3f24"
CANDIDATE_BLOB = "cd20d173cebad0357593041d8591766313143269"
CANDIDATE_ID = "C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1"
CANDIDATE_CORE_SHA256 = "sha256:c869e4726c36551b69f10407dd482f30d83f2b2a8129c5364ac2c08eda4c1d43"
CANDIDATE_ARTIFACT_HASH = "sha256:47bf8d99a7c5620b8ab8f2e3fadfb762125df921bed4b65fe2ddb56f4733c5e1"
FROZEN_AT = "2026-08-12T07:02:03Z"
EVALUATOR = f"{BASE}/05_falsification/c050_k15_alignment_proof_checker.py"
EVALUATOR_RAW_SHA256 = "882c2c7eaf16edc050ff4a019b4bbe9a18fc6bc2257479d9da37cb3d8dd2f03a"
PATHS = {
    "certificate": f"{BASE}/04_candidates/O9d12a2a1b_C050_K15_PROOF_CERTIFICATE_FREEZE_20260812.json",
    "authorization": f"{BASE}/09_trace/O9d12a2a1b_C050_K15_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json",
    "chronology": f"{BASE}/09_trace/O9d12a2a1b_C050_K15_PROOF_INPUT_CHRONOLOGY_20260812.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def seal(value: dict) -> dict:
    document = dict(value)
    document["artifact_hash"] = ""
    document["artifact_hash"] = canonical_hash(document)
    return document


def build_documents() -> dict[str, dict]:
    obligations = [
        {
            "obligation_id": "PARENT_LENGTH_30_PARAMETER_EXHAUSTION",
            "status": "PROVED",
            "proof": "Write a=bit_length(v), b=bit_length(m). The raw canonical length is R=6+2a+2b+3m(1+a), and the encoded length is E=R+(R mod 2). UNSAT requires m>=2. For v=1, m=2 gives E=24, m=3 gives R=E=30, and m>=4 gives E>=38. For v>=2, m=2 already gives E>=32, and larger m only increases the length. Hence canonical UNSAT length 30 uniquely forces v=1,m=3 with no padding.",
            "parameters": {"v": 1, "m": 3, "raw_length": 30, "padding": False},
        },
        {
            "obligation_id": "CURRENT_LENGTH_32_PARAMETER_BRANCH_EXHAUSTION",
            "status": "PROVED",
            "proof": "For m=1, R=11+5a, so E=32 exactly when a=4: v=8,...,15, R=31 and one zero pad. For m=2, R=16+8a, so E=32 exactly when a=2: v in {2,3}, R=32 and no pad. For m=3, a=1 gives E=30 while a>=2 gives E>=42. For m>=4 the minimum is R=38 at v=1,m=4. These cases exhaust every positive v,m.",
            "branches": [
                {"v_values": [2, 3], "m": 2, "raw_length": 32, "padding": False},
                {
                    "v_values": list(range(8, 16)),
                    "m": 1,
                    "raw_length": 31,
                    "encoded_length": 32,
                    "padding": True,
                },
            ],
        },
        {
            "obligation_id": "EXACT_CANONICAL_PARENT_PARSE",
            "status": "PROVED",
            "proof": "At v=1,m=3 the header is MAGIC||gamma(1)||gamma(3)=11100101||1||011, of length 12. Each of nine literals is sign||1, so the 18-bit payload gives total length 30 with no padding. The equal split after bit 14 lies three payload bits after the header. Thus the suffix begins at x[15], the variable-code bit of the second literal, and x[17], the variable-code bit of the third literal, is fixed to 1.",
        },
        {
            "obligation_id": "EXACT_CANONICAL_CURRENT_PARSE",
            "status": "PROVED",
            "proof": "By the frozen definition, P_16 contains prefixes only of canonical long-form words; malformed-to-tautology words and the all-zero short contradiction are not members of this prefix language. Each frozen length-32 branch admits canonical words by choosing in-range variable indices. In the unpadded v in {2,3},m=2 branches, the header length is 14 and the 16-bit prefix extends two bits into the payload. In the padded v=8,...,15,m=1 branches, the header itself has length 16. In every branch the prefix starts with the unchanged eight-bit MAGIC word 11100101.",
            "all_frozen_branches_covered": True,
            "noncanonical_and_total_decoder_fallbacks_excluded": True,
        },
        {
            "obligation_id": "EXACT_1C_EQUALS_PREFIX16_BITWISE",
            "status": "PROVED",
            "proof": "For every h=1||c in H_15, h[3]=x[17]=1. For every p in P_16, p begins MAGIC=11100101, so p[3]=MAGIC[3]=0. Hence exact equality h=p is impossible.",
            "separating_coordinate": 3,
            "indexing": "ZERO_BASED",
            "h15_fixed_bit": 1,
            "p16_fixed_bit": 0,
            "conclusion": "H_15 intersection P_16 is empty.",
        },
        {
            "obligation_id": "PARENT_UNSAT_PROOF_INDEPENDENT_OF_SYNTAX",
            "status": "PROVED",
            "proof": "The explicit formula (z OR z OR z) AND (not-z OR not-z OR not-z) AND (z OR z OR z) is UNSAT: the first clause forces z=true while the second forces z=false. This proves H_15 is syntactically and semantically nonvacuous, but the separation itself applies to every canonical UNSAT parent because its fixed bit follows from v=1 syntax.",
        },
        {
            "obligation_id": "SWAPPED_REDUCTION_PRESERVED",
            "status": "PROVED",
            "proof": "No decoder, split, label, relation, or coordinate map changes. For x=r||c, the transposed query remains (2^15+c,r), exactly the C048 endpoint-swapped reduction.",
        },
        {
            "obligation_id": "BOUNDED_SCOPE_ONLY",
            "status": "PROVED",
            "proof": "The argument uses the unique length-30 parent field alignment and proves only H_15 intersection P_16 is empty. It makes no statement for another k, for a changed grammar/split, for cover growth, or for P versus NP.",
        },
    ]
    certificate = seal(
        {
            "schema_version": "1.0.0",
            "certificate_id": "PNP-C050-K15-HAND-PROOF-CERTIFICATE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": CANDIDATE_CORE_SHA256,
            "candidate_artifact_hash": CANDIDATE_ARTIFACT_HASH,
            "frozen_at": FROZEN_AT,
            "proof_kind": "HAND_SYMBOLIC_EXHAUSTIVE_FIELD_CONTRADICTION",
            "obligations": obligations,
            "source_side_nonvacuity_witness": {
                "formula": "(z OR z OR z) AND (not-z OR not-z OR not-z) AND (z OR z OR z)",
                "header": "111001011011",
                "payload": "010101111111010101",
                "word_x": "111001011011010101111111010101",
                "r": "111001011011010",
                "c": "101111111010101",
                "h_1c": "1101111111010101",
                "unsat_proof": "The first clause requires z=true and the second clause requires z=false; therefore no assignment satisfies their conjunction, regardless of the redundant third clause.",
            },
            "scoped_conclusion_if_records_validate": "H_15 intersection P_16 is empty under the exact C041 grammar, equal split, and retained C048 swapped reduction.",
            "falsifiers": [
                "a canonical UNSAT length-30 parent outside v=1,m=3",
                "a canonical length-32 current word outside the two frozen branch families",
                "an H_15 label with zero-based bit 3 equal to 0",
                "a P_16 prefix with zero-based bit 3 equal to 1",
                "one exact common label",
                "a hidden encoding, split, or swapped-reduction change",
            ],
            "scope": [
                "k=15 only",
                "exact C041 canonical long-form grammar and equal split; total-decoder malformed/all-zero fallback branches are outside H_15 and P_16 by definition",
                "all frozen length-32 branches",
                "C048 swapped reduction retained",
                "no other k, cover/lower-bound, novelty, or root result",
            ],
            "authority": {
                "same_context_hand_proof": True,
                "formal": False,
                "independent": False,
                "novelty": False,
                "root": "OPEN",
            },
            "credit": {
                "mathematical": [
                    "length-30 parent parameter forcing",
                    "length-32 branch exhaustion",
                    "fixed bit-3 separation",
                    "explicit UNSAT nonvacuity and bounded scope",
                ],
                "computation_alone": 0,
                "software_process": 0,
                "ci_schema_hash_runtime": 0,
            },
        }
    )
    authorization = seal(
        {
            "schema_version": "1.0.0",
            "authorization_id": "PNP-C050-K15-POST-FREEZE-PROOF-CHECK-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": CANDIDATE_CORE_SHA256,
            "candidate_artifact_hash": CANDIDATE_ARTIFACT_HASH,
            "certificate_artifact_hash": certificate["artifact_hash"],
            "evaluator_path": EVALUATOR,
            "evaluator_raw_sha256": EVALUATOR_RAW_SHA256,
            "proof_check_authorized": True,
            "authorized_operation": "evaluate_certificate(exact_certificate, exact_authorization)",
            "contract_implemented": "the frozen inert evaluator's eight declared future obligations and four allowed result branches",
            "target_decoder_access_authorized": False,
            "formula_enumeration_authorized": False,
            "other_k_access_authorized": False,
            "authorized_result_scope": "H_15 intersection P_16 only",
            "authorization_source": "direct operator instruction after public candidate merge; records operational authorization but does not create independent review or formal-proof authority",
            "authorization_effect": "check exact hand certificate, exhaustive grammar branch identity, and fixed coordinate; no decoder search, novelty, cover, or root authority",
        }
    )
    chronology = seal(
        {
            "schema_version": "1.0.0",
            "chronology_id": "PNP-C050-K15-PROOF-INPUT-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_public_freeze": {
                "merge_commit": PUBLIC_MERGE_SHA,
                "candidate_blob": CANDIDATE_BLOB,
                "merge_is_ancestor_of_result_base": True,
                "result_base_commit": RESULT_BASE_SHA,
            },
            "verified_candidate_identity": {
                "candidate_core_sha256": CANDIDATE_CORE_SHA256,
                "candidate_artifact_hash": CANDIDATE_ARTIFACT_HASH,
            },
            "proof_inputs": [
                {"path": PATHS["certificate"], "artifact_hash": certificate["artifact_hash"]},
                {"path": PATHS["authorization"], "artifact_hash": authorization["artifact_hash"]},
            ],
            "frozen_at": FROZEN_AT,
            "status": "LOCALLY_FROZEN_BEFORE_EVALUATOR_EXECUTION_UNDER_DIRECT_OPERATOR_AUTHORIZATION",
            "target_result_access_before_this_freeze": False,
            "target_access": {
                "decoder_executed": False,
                "proof_checker_executed": False,
                "shared_target_bit_checked_by_runtime": False,
                "result_determined_by_runtime": False,
            },
            "scope": "k=15 and the two frozen length-32 branch families only",
            "credit": {
                "mathematical_result": False,
                "software_assurance": 0,
                "independent_review": False,
            },
        }
    )
    return {
        "certificate": certificate,
        "authorization": authorization,
        "chronology": chronology,
    }


def write_documents(root: Path = Path(".")) -> None:
    for name, document in build_documents().items():
        path = root / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    write_documents()
