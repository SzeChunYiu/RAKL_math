"""Deterministic C047 candidate/evaluator freeze with no target access."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


APPLICATION_BASE_SHA = "ec8a9eb5eeedaaf1d3f497a8688384256a2079e0"
PRE_CANDIDATE_FREEZE_SHA = "d84e3814f1d8f355246f2bddb6982c3a1859fb6c"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
CANDIDATE_ID = "C047-ORIENTATION-ONLY-SEPARATION-LEMMA-v1"
FROZEN_AT = "2026-08-12T03:05:02Z"
BASE = "research/real_math/millennium/p_vs_np"
PATHS = {
    "candidate": f"{BASE}/04_candidates/O9d12a2a1b_C047_ORIENTATION_ONLY_SEPARATION_LEMMA_FREEZE_20260812.json",
    "evaluator_manifest": f"{BASE}/05_falsification/O9d12a2a1b_C047_ORIENTATION_FEASIBILITY_EVALUATOR_FREEZE_20260812.json",
    "authorization": f"{BASE}/09_trace/O9d12a2a1b_C047_EVALUATION_AUTHORIZATION_20260812.json",
    "trace": f"{BASE}/09_trace/O9d12a2a1b_C047_CANDIDATE_FREEZE_TRACE_20260812.json",
    "feedback": f"{BASE}/10_feedback/C047_COARSE_REPAIR_INTERFACE_CONGRUENCE_APPLICATION_FEEDBACK_PROPOSAL_20260812.json",
    "receipt": f"{BASE}/09_trace/O9d12a2a1b_C047_CANDIDATE_FREEZE_RECEIPT_20260812.json",
}
PRE_GATE_PATH = f"{BASE}/09_trace/O9d12a2a1b_C047_PRE_CANDIDATE_GATE_RECEIPT_20260812.json"
PRE_TRACE_PATH = f"{BASE}/09_trace/O9d12a2a1b_C047_PRE_CANDIDATE_TRACE_20260812.json"
EVALUATOR_PATH = f"{BASE}/05_falsification/c047_orientation_feasibility_evaluator.py"
PRE_GATE_BLOB = "0973599f68f24f4e520e2df3b3f5ec27393cffad"
PRE_GATE_RAW_SHA256 = "9749cfb0fbbb2e8d45737b0ceae400ceb9ac5103866d5cb89b85d6a9aa49a273"
PRE_TRACE_BLOB = "4eded4656c8fabf2295e92cdf90135c7a061a59a"
PRE_TRACE_RAW_SHA256 = "b7461b5c0aba86ce0d14d22ee012b5ec6fe773720da16b5857efe2d33209cc3a"
EVALUATOR_RAW_SHA256 = "28040619b04031d33932203d96fdbb49a0da697c8990e096c9b00bf562a21043"


def h(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def seal(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = ""
    result["artifact_hash"] = h(result)
    return result


def build_documents() -> dict[str, dict]:
    candidate = seal({
        "schema_version": "1.0.0",
        "candidate_id": CANDIDATE_ID,
        "atom_id": "O9d12a2a1b-C047",
        "candidate_kind": "MATHEMATICAL_LEMMA_CANDIDATE",
        "frozen_at": FROZEN_AT,
        "family_definition": {
            "seed": "the exact C041 U_2 seed",
            "inherited_block": "embed U_(n-1) unchanged in the old-old quadrant",
            "old_new_option": "for UNSAT Dec(bin_(n-1)(r)||bin_(n-1)(c)), add (r,2^(n-1)+c)",
            "prefix_preserving_new_old_option": "for the same decoded word, add (2^(n-1)+r,c)",
            "variants": ["MIRROR_ONLY", "TWO_SIDED_OLD_NEW_PLUS_PREFIX_MIRROR"],
            "excluded_variants": ["literal matrix transpose with suffix c on the fresh row", "unequal or overlapping split", "coordinate relabelling", "decoder or MAGIC change"],
        },
        "statement": {
            "quantifier": "for every integer n >= 18 and each frozen orientation-only variant",
            "generated_row_classes": [
                "inherited rows in [0,2^(n-1))",
                "the all-zero fresh row with n-bit word 1 followed by n-1 zeroes",
                "canonical fresh rows whose n-bit word begins with 1 followed by MAGIC=11100101",
            ],
            "canonical_current_rows": "every n-bit prefix of a current canonical length-2n word begins with MAGIC=11100101",
            "conclusion": "the complement row projection is disjoint from the set of current canonical MAGIC n-bit prefixes",
            "repair_consequence": "moving or copying only the prefix coordinate into the fresh-row quadrant does not repair the C046 canonical row-collision impossibility",
        },
        "predicted_discriminator": {
            "low_inherited_case": "first bit 0 versus first MAGIC bit 1",
            "all_zero_case": "first two bits 10 versus first two MAGIC bits 11",
            "canonical_mirror_case": "1||MAGIC begins 1111 while MAGIC begins 1110",
        },
        "assumptions": [
            "unchanged total C041 decoder: all-zero contradiction, valid MAGIC canonical form, every other word tautology",
            "unchanged equal prefix/suffix split",
            "prefix coordinate r is placed on the fresh row without relabelling",
            "no complement in the new-new quadrant",
            "n>=18, so predecessor and current prefixes expose the full eight-bit MAGIC header",
        ],
        "transfer_conditions": [
            "the recursive quadrant clauses are exhaustive",
            "orientation changes neither decoded word nor coordinate ordering",
            "the target property is exact row-label collision",
        ],
        "proof_obligations": [
            "DEFINE_ORIENTATION_ONLY_FAMILIES",
            "EXHAUSTIVE_ROW_SUPPORT_TRICHOTOMY",
            "DECODER_BRANCH_TO_FRESH_ROW_FORMS",
            "BINARY_HEADER_DISJOINTNESS",
            "MIRROR_AND_TWO_SIDED_CONCLUSION",
        ],
        "falsifiers": [
            "an orientation-only complement row lies outside the three frozen row classes",
            "a non-tautological nonzero decoded word lacks the MAGIC header",
            "1||MAGIC and MAGIC agree through the first four bits",
            "an inherited old row has n-bit leading bit 1",
            "the claimed family silently places suffix c rather than prefix r on the fresh row",
        ],
        "non_guarantees": [
            "candidate is not yet proved",
            "literal transpose, relabelling, and split-changing repairs remain open",
            "no cover or circuit lower bound",
            "no novelty or P-versus-NP authority",
            "no framework promotion authority",
        ],
        "source_identity": {
            "application_base_commit": APPLICATION_BASE_SHA,
            "pre_candidate_freeze_commit": PRE_CANDIDATE_FREEZE_SHA,
            "framework_commit": FRAMEWORK_SHA,
            "pre_candidate_gate": {"path": PRE_GATE_PATH, "git_blob": PRE_GATE_BLOB, "raw_sha256": PRE_GATE_RAW_SHA256},
        },
        "target_access": {
            "decoder_imported_or_executed": False,
            "evaluator_imported_or_executed": False,
            "later_target_enumerated": False,
            "later_target_result_accessed": False,
            "finite_collision_level_selected": False,
        },
        "credit_boundary": {
            "candidate_mathematical_content": "lemma/construction/assumptions/transfer conditions/falsifiers",
            "assurance_only_zero_credit": ["Git/branch/PR chronology", "CI/tests", "schemas/hashes/serialization", "runtime and evaluator wiring"],
            "candidate_freeze_mathematical_saturation_credit": False,
            "candidate_freeze_mathematical_result_credit": False,
        },
    })
    manifest = seal({
        "schema_version": "1.0.0",
        "manifest_id": "PNP-C047-ORIENTATION-FEASIBILITY-EVALUATOR-FREEZE-20260812",
        "candidate_id": CANDIDATE_ID,
        "frozen_at": FROZEN_AT,
        "status": "FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED",
        "evaluator": {"path": EVALUATOR_PATH, "raw_sha256": EVALUATOR_RAW_SHA256},
        "required_obligations": candidate["proof_obligations"],
        "mathematical_obligations_only": True,
        "target_result_capability": False,
        "later_execution_gate": {"separate_post_freeze_authorization_required": True, "current_task_execution_authorized": False, "target_enumeration_forbidden": True},
        "target_access": candidate["target_access"],
        "authority": {"proof_authority": False, "mathematical_result_credit": False, "p_vs_np_authority": False},
    })
    authorization = seal({
        "schema_version": "1.0.0",
        "authorization_id": "PNP-C047-EVALUATION-AUTHORIZATION-20260812",
        "candidate_id": CANDIDATE_ID,
        "evaluator_raw_sha256": EVALUATOR_RAW_SHA256,
        "current_task_evaluator_execution_authorized": False,
        "later_target_access_authorized": False,
        "finite_target_scan_authorized": False,
        "allowed_next_action": "PUBLICLY_FREEZE_THIS_EXACT_CANDIDATE_AND_EVALUATOR_BEFORE_ANY_PROOF_CHECK",
        "future_proof_check_requires_separate_authorization": True,
        "future_authorization_cannot_change_candidate_or_obligations": True,
        "target_result_state": "TARGET_RESULT_UNACCESSED",
        "mathematical_saturation_credit": False,
        "mathematical_result_credit": False,
    })
    pre = json.loads(Path(PRE_TRACE_PATH).read_text(encoding="utf-8"))
    entries = list(pre["entries"])
    payload = {
        "event_id": "O9d12a2a1b-C047-E09",
        "atom_id": "O9d12a2a1b-C047",
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": FROZEN_AT,
        "state_summary": "All C047 v3 pre-candidate gates passed at the public parent; one orientation-only lemma, inert evaluator, and no-execution authorization are frozen without later-target access.",
        "action_summary": "Freeze exact mirror-only and two-sided orientation-feasibility proof obligations.",
        "evidence_pointers": [PATHS["candidate"], PATHS["evaluator_manifest"], PATHS["authorization"], PRE_GATE_PATH],
        "alternatives_considered": ["enumerate later levels", "include literal transpose", "change encoding or split", "freeze the smallest orientation-only candidate"],
        "decision_rationale": "The public SEARCH route selected coarse-repair then interface congruence; this candidate changes only the quadrant and freezes symbolic row classes before checking them.",
        "outputs": [CANDIDATE_ID, "MATHEMATICAL_LEMMA_CANDIDATE", "TARGET_RESULT_UNACCESSED", candidate["artifact_hash"], manifest["artifact_hash"], authorization["artifact_hash"]],
        "uncertainties": ["candidate truth and novelty are unchecked", "literal transpose and relabelling remain open", "same-context review is not independent"],
        "residuals": ["proof obligations unexecuted", "root OPEN"],
        "next_steps": ["publish exact candidate/evaluator freeze", "only then freeze a separate proof certificate and execution authorization", "do not enumerate later targets"],
        "previous_event_hash": entries[-1]["artifact_hash"],
    }
    payload["artifact_hash"] = h(payload)
    entries.append(payload)
    trace = {"trace_id": "PNP-O9d12a2a1b-C047-CANDIDATE-FREEZE-TRACE-20260812", "entries": entries}
    feedback = seal({
        "schema_version": "1.0.0",
        "feedback_id": "PNP-C047-COARSE-REPAIR-INTERFACE-CONGRUENCE-PROPOSAL-20260812",
        "source_atom_id": "O9d12a2a1b-C047",
        "status": "APPLICATION_FEEDBACK_PROPOSAL_ONLY_NOT_PROMOTED",
        "trigger": "ONLY_IF_THE_C047_ORIENTATION_FEASIBILITY_LEMMA_LATER_VALIDATES",
        "proposed_method_lesson": "After a coarse structural change removes a partition obstruction, test exact interface congruence before treating the repair as viable or enumerating targets.",
        "failure_hypothesis": "Research can mistake occupancy of the correct coarse region for restoration of the exact relation required by the quantity of interest.",
        "validation_obligations": [
            "validate C047 mathematically before using the lesson",
            "freeze a separate Self-RAKL challenger and evaluator before framework change",
            "include negative controls where coarse repair really is sufficient",
            "test fresh tasks with hierarchical coarse/fine obstructions",
        ],
        "authority": {"framework_evolution_authority": False, "method_promotion_authority": False, "fresh_self_rakl_assurance_required": True, "same_context_review_is_independent": False},
        "credit": {"feedback_transport_mathematical_saturation_credit": False, "feedback_transport_mathematical_result_credit": False},
        "evidence_pointers": [PATHS["candidate"], PATHS["trace"], PRE_GATE_PATH],
    })
    documents = {"candidate": candidate, "evaluator_manifest": manifest, "authorization": authorization, "trace": trace, "feedback": feedback}
    integrity = {
        "algorithm": "SHA-256",
        "canonicalization": "JSON_SORT_KEYS_COMPACT_UTF8",
        "json_inputs": {name: {"path": PATHS[name], "canonical_sha256": h(doc)} for name, doc in sorted(documents.items())},
        "byte_inputs": {
            "evaluator_source": {"path": EVALUATOR_PATH, "raw_sha256": EVALUATOR_RAW_SHA256},
            "pre_candidate_gate": {"path": PRE_GATE_PATH, "git_blob": PRE_GATE_BLOB, "raw_sha256": PRE_GATE_RAW_SHA256},
            "pre_candidate_trace": {"path": PRE_TRACE_PATH, "git_blob": PRE_TRACE_BLOB, "raw_sha256": PRE_TRACE_RAW_SHA256},
        },
    }
    receipt = seal({
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C047-ORIENTATION-ONLY-CANDIDATE-FREEZE-20260812",
        "candidate_id": CANDIDATE_ID,
        "frozen_at": FROZEN_AT,
        "chronology": {"pre_candidate_freeze_commit": PRE_CANDIDATE_FREEZE_SHA, "candidate_frozen_after_pre_candidate_gate": True, "candidate_publication_status": "TO_BE_PUBLISHED_BEFORE_ANY_EVALUATION", "target_result_accessed": False, "evaluator_imported_or_executed": False, "finite_target_enumerated": False},
        "full_document_integrity": integrity,
        "full_document_integrity_hash": h(integrity),
        "authority": {"candidate_is_mathematical_proposal": True, "theorem_truth": False, "novelty": False, "independent_review": False, "mathematical_saturation_credit": False, "mathematical_result_credit": False, "p_vs_np_authority": False, "root_status": "OPEN"},
        "allowed_next_action": "PUSH_PUBLIC_FREEZE_THEN_CREATE_SEPARATE_PROOF_CERTIFICATE_AND_AUTHORIZATION",
    })
    documents["receipt"] = receipt
    return documents


if __name__ == "__main__":
    print(json.dumps(build_documents(), indent=2, sort_keys=True))
