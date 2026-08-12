"""Materialize the inert C052 classifier/falsifier identities.

This module is a serializer only.  It deliberately contains no classifier,
decoder, SAT solver, overlap test, support-cell enumerator, or target selector.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CLASSIFIER = PNP / "04_candidates/O9d12a2a1b_C052_TARGET_BLIND_CLASSIFIER_IDENTITY_20260812.json"
FALSIFIER = PNP / "05_falsification/O9d12a2a1b_C052_INDEPENDENT_HOSTILE_FALSIFIER_IDENTITY_20260812.json"
FREEZE = PNP / "09_trace/O9d12a2a1b_C052_CLASSIFIER_FALSIFIER_IDENTITY_FREEZE_20260812.json"
REVALIDATION = PNP / "09_trace/O9d12a2a1b_C052_FRAMEWORK_REVALIDATION_EA607C8_20260812.json"
TRACE = PNP / "09_trace/O9d12a2a1b_C052_CLASSIFIER_IDENTITY_FREEZE_TRACE_20260812.json"
PRE_TRACE = PNP / "09_trace/O9d12a2a1b_C052_PRE_CANDIDATE_TRACE_20260812.json"


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def raw_sha256(value: object) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def seal(value: dict) -> dict:
    core = dict(value)
    core.pop("artifact_hash", None)
    core["artifact_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return core


def classifier_identity() -> dict:
    return {
        "schema_version": "1.0.0",
        "identity_id": "PNP-C052-TARGET-BLIND-TOTAL-SUPPORT-PHASE-CLASSIFIER-v1",
        "atom_id": "O9d12a2a1b-C052",
        "identity_kind": "INERT_DATA_ONLY_CLASSIFIER_SPECIFICATION",
        "status": "FROZEN_NOT_EXECUTED",
        "object": "C041 canonical-code parent/current symbolic support cells at adjacent half-lengths, projected through the unchanged C048 label interface",
        "qoi": "For an explicitly quantified supported cell, determine whether canonical syntax proves a universal unequal coordinate against MAGIC, proves escape admissibility from that local obstruction, remains unresolved, or cannot be checked.",
        "domain": {
            "total_input_contract": "Every input is either a complete symbolic support-cell record or malformed/missing; the classifier must return exactly one declared branch.",
            "parent_variables": ["k", "a", "b", "m", "v", "parent_padding"],
            "current_variables": ["a_plus", "b_plus", "m_plus", "v_plus", "current_padding"],
            "quantifiers": [
                "k,a,b,m,a_plus,b_plus,m_plus are positive integers",
                "2^(a-1) <= v <= 2^a-1 and b=bit_length(m)",
                "2^(a_plus-1) <= v_plus <= 2^a_plus-1 and b_plus=bit_length(m_plus)",
                "every legal literal variable index 1..v and each sign is covered when a parent bit is claimed forced",
                "every legal current literal index 1..v_plus and each sign is covered when a current bit is claimed forced",
            ],
            "derived_equalities": [
                "H(a,b)=6+2a+2b",
                "w(a)=1+a",
                "R(a,b,m)=H(a,b)+3m*w(a)",
                "parent_padding=R(a,b,m) mod 2 and R+parent_padding=2k",
                "current_padding=R(a_plus,b_plus,m_plus) mod 2 and R(a_plus,b_plus,m_plus)+current_padding=2(k+1)",
                "phi_c0=(k-H(a,b)) mod w(a)",
                "h[0]=1 is prepended; c[0]=x[k]=h[1]",
                "for j>=1, h[j]=x[k+j-1] and token phase=(phi_c0+j-1) mod w(a)",
                "for 0<=j<=7, every current word has p[j]=MAGIC[j] with MAGIC=11100101",
            ],
            "forbidden_domain_shortcuts": [
                "replace v by a single representative of its bit-length cell",
                "omit literal indices or signs",
                "choose padding rather than derive it",
                "conflate h[0] with c[0]=h[1]",
                "select or enumerate a new k before identity publication",
            ],
        },
        "total_result_algebra": {
            "ordered_precedence": ["CANNOT_CHECK", "FORCED_CONFLICT", "ESCAPE_ADMISSIBLE", "UNRESOLVED"],
            "branches": {
                "FORCED_CONFLICT": "Support is proved and a certificate gives j in 0..7 and bit q such that every legal parent realization has h[j]=q while q differs from MAGIC[j].",
                "ESCAPE_ADMISSIBLE": "Support is proved and an independently checkable certificate shows that no j in 0..7 is universally forced unequal by this local support/phase obstruction. This is not an overlap witness.",
                "UNRESOLVED": "Support is proved, but neither a universal forced-conflict certificate nor an escape-admissibility certificate is established.",
                "CANNOT_CHECK": "The record, source identity, arithmetic, quantifier coverage, or certificate is missing, malformed, inconsistent, or outside the frozen decidable interface.",
            },
            "exactly_one_branch_required": True,
        },
        "certificate_interfaces": {
            "forced_conflict": ["support_equalities", "coordinate_j", "forced_parent_bit", "MAGIC_bit", "all_v_indices_signs_coverage_proof"],
            "escape_admissible": ["support_equalities", "coordinates_0_through_7", "no_universal_unequal_bit_proof", "not_overlap_disclaimer"],
            "unresolved": ["support_equalities", "failed_certificate_obligations"],
            "cannot_check": ["failed_closed_obligation", "evidence_pointer_if_available"],
        },
        "mandatory_regression_worlds": [
            {
                "world_id": "C050-k15-bounded-regression",
                "expected_branch": "FORCED_CONFLICT",
                "expected_certificate": "h[3]=1 while MAGIC[3]=0",
                "scope": "k=15 only; not an induction premise",
                "source": "research/real_math/millennium/p_vs_np/05_falsification/O9d12a2a1b_C050_K15_PROOF_CHECK_RESULT_20260812.json",
            },
            {
                "world_id": "C051-k19-bounded-regression",
                "expected_branch": "FORCED_CONFLICT",
                "expected_certificate": "h[3]=1 while MAGIC[3]=0",
                "scope": "k=19 retrospective verification only; not an induction premise",
                "source": "research/real_math/millennium/p_vs_np/05_falsification/O9d12a2a1b_C051_K19_PROOF_RESULT_20260812.json",
            },
        ],
        "hostile_world_contract": {
            "world_id": "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1",
            "identity_only_now": True,
            "future_input_requirement": "An independently derived complete support cell and certificate showing no universally forced unequal MAGIC coordinate.",
            "expected_branch_if_certificate_valid": "ESCAPE_ADMISSIBLE",
            "materialization_and_execution_status": "NOT_MATERIALIZED_NOT_EXECUTED",
            "failure_if": "The classifier calls the cell FORCED_CONFLICT, omits it, or calls escape admissibility an overlap witness.",
        },
        "non_guarantees": [
            "no support cell, residue class, forced coordinate, or escape cell is found in this identity freeze",
            "no classifier result, SAT/UNSAT result, decoder result, overlap result, cover bound, circuit lower bound, or P-versus-NP conclusion",
            "no theorem, proof, novelty, independent-review, or mathematical-result credit",
        ],
        "forbidden_capabilities": ["decoder import or execution", "SAT or UNSAT execution", "overlap comparison", "new-k enumeration", "target-k selection"],
    }


def falsifier_identity() -> dict:
    return {
        "schema_version": "1.0.0",
        "identity_id": "PNP-C052-INDEPENDENT-HOSTILE-SUPPORTED-CELL-FALSIFIER-v1",
        "atom_id": "O9d12a2a1b-C052",
        "identity_kind": "INERT_DATA_ONLY_FALSIFIER_SPECIFICATION",
        "status": "FROZEN_NOT_EXECUTED",
        "independence_boundary": {
            "implementation_identity_distinct_from_classifier": True,
            "classifier_import_allowed": False,
            "classifier_certificate_reuse_allowed": False,
            "same_context_review_is_independent_peer_review": False,
            "future_observation_must_recompute_support_phase_and_quantifier_coverage": True,
        },
        "inputs_after_separate_authorization": [
            "frozen classifier bytes and raw SHA-256",
            "complete symbolic support-cell record",
            "claimed classifier branch and certificate",
            "C050 and C051 immutable regression source records",
            "independently generated hostile supported escape-cell witness",
        ],
        "independent_checks": [
            "recompute both adjacent support equations and derived padding",
            "recompute phi_c0 and the h[0] versus c[0]=h[1] index map",
            "audit every v in each bit-length cell and every legal literal index/sign used by a forced-bit claim",
            "verify exactly one of FORCED_CONFLICT, ESCAPE_ADMISSIBLE, UNRESOLVED, CANNOT_CHECK was returned",
            "reproduce C050 k=15 and C051 k=19 only as bounded FORCED_CONFLICT regression worlds",
            "validate the hostile supported escape witness without treating it as an overlap witness",
        ],
        "falsification_conditions": [
            "any omitted support, padding, v, literal-index, literal-sign, or coordinate branch",
            "any h[0] and h[1]=c[0] conflation",
            "a FORCED_CONFLICT claim without universal forced-bit coverage",
            "failure to retain ESCAPE_ADMISSIBLE, UNRESOLVED, or CANNOT_CHECK",
            "finite C050/C051 evidence used as a universal induction premise",
            "an escape-admissible cell described as exact overlap",
            "any decoder, SAT, overlap, selected-target, or new-k result leakage",
        ],
        "hostile_supported_escape_cell": {
            "world_id": "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1",
            "selection_rule_identity": "INDEPENDENT-SYMBOLIC-SUPPORT-SOLVER-WITH-NO-FORCED-MAGIC-CONFLICT-v1",
            "frozen_obligations": ["exact parent/current support", "derived padding", "complete quantifier coverage", "no universally unequal MAGIC coordinate", "no overlap inference"],
            "cell_value_status": "WITHHELD_UNMATERIALIZED_UNTIL_SEPARATE_EXECUTION_AUTHORIZATION",
            "no_new_k_access_in_this_round": True,
        },
        "total_falsifier_outcomes": ["CLASSIFIER_SURVIVES", "CLASSIFIER_FALSIFIED", "UNRESOLVED", "CANNOT_CHECK"],
        "non_guarantees": ["identity separation is not independent peer review", "the falsifier is not executed", "no mathematical result or theorem authority"],
    }


def framework_revalidation() -> dict:
    return seal({
        "schema_version": "framework-subject-revalidation-observation-v1",
        "observation_id": "PNP-C052-FRAMEWORK-REVALIDATION-EA607C8-20260812",
        "atom_id": "O9d12a2a1b-C052",
        "prior_framework_sha": "7d67a18a96499f5df7bf58bc6b1356d1ce1cafbf",
        "observed_current_main_sha": "ea607c8cd8e4fd308ea9a4e024d8c93ff87f5fda",
        "intervening_diff_classification": "19 Paper2/Paper3 manuscript, registration, objective receipt, script, and test files only; no protected mathematical context, memory, trace, quantifier, structural-transport, candidate-freeze, or assurance surface changed",
        "licensed_action": "FREEZE_TARGET_BLIND_CLASSIFIER_AND_DISTINCT_INDEPENDENT_FALSIFIER_IDENTITIES_ONLY",
        "identity_creation_authorized": True,
        "classifier_or_falsifier_execution_authorized": False,
        "new_k_enumeration_or_selection_authorized": False,
        "decoder_sat_overlap_access_authorized": False,
        "grants_scientific_authority": False,
        "mathematical_result_credit": 0,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
        "evidence": [
            "git-ls-remote:SzeChunYiu/RAKL:refs/heads/main:ea607c8cd8e4fd308ea9a4e024d8c93ff87f5fda",
            "git-diff:7d67a18a96499f5df7bf58bc6b1356d1ce1cafbf..ea607c8cd8e4fd308ea9a4e024d8c93ff87f5fda",
        ],
    })


def candidate_trace(classifier: dict, falsifier: dict) -> dict:
    prior = json.loads(PRE_TRACE.read_text(encoding="utf-8"))
    entries = list(prior["entries"])
    previous = entries[-1]["artifact_hash"]
    payload = {
        "event_id": "O9d12a2a1b-C052-E09",
        "atom_id": "O9d12a2a1b-C052",
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": "2026-08-12T12:20:00Z",
        "state_summary": "The target-blind total classifier and a distinct hostile-falsifier identity now exist as inert data specifications. No native support cell, class result, decoder/SAT state, overlap result, theorem, or root result has been accessed.",
        "action_summary": "Freeze the exact symbolic domain, four total classifier branches, bounded C050/C051 regression worlds, and independent hostile supported-escape falsifier identity without execution.",
        "evidence_pointers": [str(CLASSIFIER.relative_to(ROOT)), str(FALSIFIER.relative_to(ROOT)), str(REVALIDATION.relative_to(ROOT))],
        "alternatives_considered": ["blindly enumerate another k", "promote C050/C051 to an induction", "execute while freezing", "freeze distinct target-blind identities only"],
        "decision_rationale": "The public C052 gate licenses identity materialization only. A total four-branch classifier plus an independently recomputing hostile falsifier preserves bounded regressions, escape, unresolved, and fail-closed outcomes without learning a new target result.",
        "outputs": [classifier["identity_id"], raw_sha256(classifier), falsifier["identity_id"], raw_sha256(falsifier), "IDENTITIES_FROZEN_NOT_EXECUTED", "ZERO_MATHEMATICAL_RESULT_CREDIT"],
        "uncertainties": ["whether any nontrivial support class forces a conflict", "whether a native supported escape cell exists", "same-context review is not independent"],
        "residuals": ["classifier and falsifier unexecuted", "hostile cell unmaterialized", "UNSAT and overlap obligations untouched", "root OPEN_NO_SOLUTION_CERTIFICATE"],
        "next_steps": ["publish this exact identity before any evaluation", "obtain separate authorization", "materialize the hostile supported escape world independently", "run regressions and falsifier before native class evaluation"],
        "previous_event_hash": previous,
    }
    payload["artifact_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    entries.append(payload)
    return {"trace_id": "PNP-O9d12a2a1b-C052-CLASSIFIER-IDENTITY-FREEZE-TRACE-20260812", "entries": entries}


def freeze_receipt(classifier: dict, falsifier: dict, revalidation: dict, trace: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C052-CLASSIFIER-FALSIFIER-IDENTITY-FREEZE-20260812",
        "atom_id": "O9d12a2a1b-C052",
        "authority": "IDENTITY_FREEZE_ONLY_NO_EXECUTION_NO_RESULT_NO_MATHEMATICAL_CREDIT",
        "framework_subject": {
            "commit": "ea607c8cd8e4fd308ea9a4e024d8c93ff87f5fda",
            "revalidation_id": revalidation["observation_id"],
            "revalidation_artifact_hash": revalidation["artifact_hash"],
        },
        "research_trace": {"path": str(TRACE.relative_to(ROOT)), "last_event_hash": trace["entries"][-1]["artifact_hash"], "event_type": "CANDIDATE_PROPOSED"},
        "identities": {
            "classifier": {"id": classifier["identity_id"], "path": str(CLASSIFIER.relative_to(ROOT)), "raw_sha256": raw_sha256(classifier)},
            "falsifier": {"id": falsifier["identity_id"], "path": str(FALSIFIER.relative_to(ROOT)), "raw_sha256": raw_sha256(falsifier)},
            "distinct_raw_identities": raw_sha256(classifier) != raw_sha256(falsifier),
        },
        "frozen_result_branches": ["FORCED_CONFLICT", "ESCAPE_ADMISSIBLE", "UNRESOLVED", "CANNOT_CHECK"],
        "mandatory_validation_worlds": ["C050-k15-bounded-regression", "C051-k19-bounded-regression", "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1"],
        "chronology": {"classifier_executed": False, "falsifier_executed": False, "hostile_cell_materialized": False, "new_k_enumerated": False, "target_k_selected": False, "decoder_sat_overlap_accessed": False, "result_accessed": False},
        "mathematical_state": {"candidate_is_a_theorem": False, "mathematical_result_created": False, "lesson_created": False, "root": "OPEN_NO_SOLUTION_CERTIFICATE"},
        "review_boundary": "Same-context role separation and this implementation review are not independent peer review.",
        "credit": {"mathematical_result_units": 0, "software_git_ci_hash_schema_chronology": 0, "same_context_review_independence": 0},
        "next_action": "After public merge and a separate authorization, materialize the independent hostile supported escape cell and run the falsifier/regression worlds before any native parametric class evaluation.",
    })


def build() -> tuple[dict, dict, dict, dict, dict]:
    classifier = classifier_identity()
    falsifier = falsifier_identity()
    revalidation = framework_revalidation()
    trace = candidate_trace(classifier, falsifier)
    return classifier, falsifier, revalidation, trace, freeze_receipt(classifier, falsifier, revalidation, trace)


def write() -> None:
    classifier, falsifier, revalidation, trace, freeze = build()
    for path, value in ((CLASSIFIER, classifier), (FALSIFIER, falsifier), (REVALIDATION, revalidation), (TRACE, trace), (FREEZE, freeze)):
        path.write_bytes(canonical_bytes(value))


if __name__ == "__main__":
    write()
