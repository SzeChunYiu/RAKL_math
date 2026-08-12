"""Build the prospective C051 k=19 mathematical candidate freeze."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CONTEXT = PNP / "01_frontier/O9d12a2a1b_C051_MATH_CONTEXT_FIBER_20260812.json"
GATE = PNP / "09_trace/O9d12a2a1b_C051_PRE_CANDIDATE_GATE_RECEIPT_20260812.json"
CORRECTION = PNP / "09_trace/O9d12a2a1b_C051_SUPPORT_CONTAMINATION_CORRECTION_20260812.json"
EVALUATOR = PNP / "05_falsification/c051_k19_alignment_evaluator.py"
OUTPUT = PNP / "04_candidates/O9d12a2a1b_C051_K19_ALIGNMENT_DISCRIMINATOR_FREEZE_20260812.json"


def sha256_bytes(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def seal(document: dict) -> dict:
    core = dict(document)
    core.pop("artifact_hash", None)
    encoded = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["artifact_hash"] = sha256_bytes(encoded)
    return core


def build() -> dict:
    context = json.loads(CONTEXT.read_text(encoding="utf-8"))
    gate = json.loads(GATE.read_text(encoding="utf-8"))
    correction = json.loads(CORRECTION.read_text(encoding="utf-8"))
    if correction["corrected_authority"]["licensed_action"] != "FREEZE_RETROSPECTIVE_K19_DISCRIMINATOR_BEFORE_ANY_SHARED_BIT_OR_UNSAT_EVALUATION":
        raise RuntimeError("C051 correction does not license this retrospective candidate")
    if correction["corrected_authority"]["candidate_generation_allowed_under_original_strict_gate"] is not False:
        raise RuntimeError("C051 correction must fail the original strict gate closed")
    if gate["chronology"]["candidate_identity"] is not None:
        raise RuntimeError("C051 pre-candidate gate already binds a candidate")

    candidate_core = {
        "candidate_id": "C051-K19-TARGET-BLIND-SYNCHRONIZED-DISCRIMINATOR-v1",
        "object": "Exact H_19 intersection P_20 under the frozen C041 canonical grammar, equal split, and C048 swapped reduction",
        "qoi": "EXACT_H19_INTERSECTION_P20_CLASSIFICATION",
        "parent_length_classification": {
            "claim": "The only UNSAT-capable canonical encoded-length-38 parameter regime is v=1,m=4.",
            "proof": [
                "Write a=bit_length(v), b=bit_length(m). Raw length is R=6+2a+2b+3m(1+a), and encoded length is R rounded up to even.",
                "For a=1, R=8+2b+6m is even; m=4 gives R=38, while m<=3 gives at most 30 and m>=5 gives at least 44.",
                "For a=2 and m>=2, m=2 gives R=32 and m>=3 gives at least 41; for a>=3,m>=2 the minimum is 40. One-clause formulas are satisfiable, so these cases exhaust UNSAT-capable parents.",
            ],
            "unsat_capability": "The v=1,m=4 class contains UNSAT formulas, for example one clause forcing z and one forcing not-z, with two arbitrary extra clauses.",
        },
        "current_length_classification": {
            "claim": "The only canonical encoded-length-40 parameter regimes are 4<=v<=7,m=2.",
            "proof": [
                "For a=1, successive relevant raw lengths around 40 are 38 at m=4 and 44 at m=5.",
                "For a=2, m=2 gives 32 and m=3 gives 41, which rounds to 42.",
                "For a=3,m=2, R=40, giving exactly v in {4,5,6,7}; m=1 gives 26 and m>=3 gives at least 52.",
                "For a>=4,m>=2 the minimum is 48; for m=1, R=11+5a gives 31,36,41 at a=4,5,6 and cannot encode to 40.",
            ],
        },
        "discriminator": {
            "procedure": [
                "Enumerate all 2^12 sign assignments of the v=1,m=4 parent literal sequence; retain exactly the formulas false for both z assignments.",
                "For each retained parent, form the exact 20-bit label 1||suffix_19(parent_word).",
                "Enumerate the exhaustive current regimes v in {4,5,6,7},m=2 and every possible first width-3 literal token; later tokens cannot affect prefix_20.",
                "Compare the exact 20-bit strings and emit the first complete witness or an exhaustive scoped impossibility certificate.",
            ],
            "allowed_result_branches": [
                "EXACT_OVERLAP_WITNESS",
                "SCOPED_OVERLAP_IMPOSSIBILITY",
                "CANNOT_CHECK",
            ],
            "positive_certificate": "A canonical length-38 parent word with a two-assignment UNSAT proof, a canonical length-40 current word, and bit-for-bit equality 1||suffix_19=prefix_20.",
            "negative_certificate": "Exhaust all 2^12 parent sign strings and every possible first token in the four current width-class branches, with the length classifications proved above.",
        },
        "difference_witness_vs_c050": {
            "changed_coordinates": [
                "half-length 15 becomes 19",
                "parent class v=1,m=3 becomes v=1,m=4",
                "current classes become v in {4,5,6,7},m=2",
                "the half split moves to a different phase inside the parent payload",
            ],
            "old_falsifier_not_transported": "C050's zero-based bit-3 contradiction was derived from the k=15 field alignment; no coordinate value is copied into k=19.",
            "cheapest_repeat_failure_test": "The frozen exact 20-bit comparison is run before any downstream cover or asymptotic reasoning.",
        },
        "falsifiers": [
            "an omitted encoded-length-38 or encoded-length-40 canonical parameter regime",
            "a retained parent formula satisfiable at z=false or z=true",
            "a positive branch with one unequal label bit or a noncanonical word",
            "a negative branch with one exact canonical overlap witness",
            "any changed encoding, split, transpose interface, or extrapolation beyond k=19",
        ],
        "scope": [
            "k=19 only",
            "exact C041 canonical long-form grammar and equal split",
            "C048 swapped reduction retained",
            "no cover growth, circuit lower bound, novelty, independent review, or P-versus-NP authority",
        ],
    }
    candidate_id_hash = sha256_bytes(
        json.dumps(candidate_core, sort_keys=True, separators=(",", ":")).encode()
    )
    return seal({
        "schema_version": "1.0.0",
        "record_type": "PROSPECTIVE_MATHEMATICAL_CANDIDATE_AND_EVALUATOR_FREEZE",
        "authority": "RETROSPECTIVE_SUPPORT_SELECTION__PROSPECTIVE_SHARED_BIT_AND_UNSAT_DISCRIMINATOR_FREEZE__NO_EVALUATED_RESULT_NO_ROOT_AUTHORITY",
        "atom_id": "O9d12a2a1b-C051",
        "candidate_identity": {
            "candidate_id": candidate_core["candidate_id"],
            "candidate_core_sha256": candidate_id_hash,
        },
        "candidate": candidate_core,
        "source_bindings": {
            "application_base_commit": "f3275302b2198bbd15d551d57adce85c5762c013",
            "application_pinned_framework_commit": "5dc0627f039e8f3e1cdcb7e05cd7603860afc554",
            "pre_candidate_authoritative_framework_commit": "9da0f4d331e9ae61f1309b3a006d7a3c67fa217c",
            "framework_revalidated_current_main_commit": "55c688dc42352c8c254f7d370c66d999b414fc52",
            "framework_intervening_diff_assessment": {
                "verdict": "CURRENT_CHANGED_NO_PROTECTED_C051_GATE_SEMANTIC_CHANGE",
                "math_context_runtime_or_candidate_freeze_files_changed": False,
                "new_relevant_surfaces": [
                    "proposal-only quantifier/scope compatibility witness, not wired into protected math gates",
                    "pre-scratch host hook, not wired into the protected math runtime",
                ],
                "effect": "Candidate materialization remains governed by the already-passed C051 gate; the new proposal-only surfaces add no mandatory precondition to this fixed finite interface atom.",
            },
            "context_packet_hash": context["packet_hash"],
            "pre_candidate_gate_artifact_hash": gate["artifact_hash"],
            "support_contamination_correction_artifact_hash": correction["artifact_hash"],
            "evaluator_path": str(EVALUATOR.relative_to(ROOT)),
            "evaluator_raw_sha256": sha256_bytes(EVALUATOR.read_bytes()),
        },
        "chronology": {
            "frozen_at": "2026-08-12T09:44:24Z",
            "evaluator_executed": False,
            "generic_target_result_accessed": True,
            "k19_support_parameters_preexposed": True,
            "k19_shared_bits_unsat_and_intersection_unaccessed": True,
            "target_state": "K13_QUARANTINED__K19_SUPPORT_PREEXPOSED__K19_SHARED_BITS_UNSAT_INTERSECTION_UNACCESSED",
            "quarantined_families": ["k=13"],
            "result_artifact": None,
        },
        "mathematical_credit_boundary": {
            "credit_now": [],
            "no_credit_now": ["preexposed k19 support selection and repeated length classifications", "candidate existence", "evaluator existence", "tests", "CI", "Git", "hashes", "schemas", "chronology"],
            "future_result_requires_direct_mathematical_certificate": True,
        },
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


if __name__ == "__main__":
    OUTPUT.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
