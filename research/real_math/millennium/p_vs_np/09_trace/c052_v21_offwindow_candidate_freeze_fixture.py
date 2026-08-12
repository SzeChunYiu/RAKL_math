"""Serialize the inert C052 v2.1 off-window lemma candidate freeze.

This module contains data construction only.  It does not import the C041
decoder, construct a formula witness, prove the proposed lemma, execute a
falsifier, enumerate a hidden world, or compare an H_k label with P_(k+1).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
PRE_TRACE = BASE / "09_trace/O9d12a2a1b_C052_V21_SUPERSEDING_PRE_CANDIDATE_TRACE_20260812.json"
CONTEXT = BASE / "01_frontier/O9d12a2a1b_C052_V21_SEMANTIC_KERNEL_CONTEXT_20260812.json"
C041_SOURCE = BASE / "04_candidates/C041_fx_sat_one_sided.py"
CANDIDATE = BASE / "04_candidates/O9d12a2a1b_C052_V21_OFFWINDOW_UNSAT_ANCHOR_LEMMA_FREEZE_20260812.json"
FALSIFIER = BASE / "05_falsification/O9d12a2a1b_C052_V21_OFFWINDOW_LEMMA_FALSIFIER_MANIFEST_20260812.json"
RECEIPT = BASE / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_CANDIDATE_FREEZE_RECEIPT_20260812.json"

APPLICATION_BASE_SHA = "ce7e3491c67ae62b387ce77e71cb1bf37acace48"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
PRE_TRACE_BLOB = "b22c284180118a5d363aed6a7b688aceb98f79c0"
CONTEXT_BLOB = "805dbb6b2089930b76fb7b95613c533c5241f82d"
C041_SOURCE_BLOB = "fcc4814dd618da96ef9bb8144a4783a0a6e886e1"
FROZEN_AT = "2026-08-12T13:59:53Z"
ATOM_ID = "O9d12a2a1b-C052-V2.1"
CANDIDATE_ID = "PNP-C052-OFFWINDOW-UNSAT-ANCHOR-MARGINAL-LEMMA-v1"
FALSIFIER_ID = "PNP-C052-OFFWINDOW-UNSAT-ANCHOR-FALSIFIER-MANIFEST-v1"


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def raw_sha(value: object) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def file_raw_sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def seal(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return result


def candidate_document() -> dict:
    return seal({
        "schema_version": "1.0.0",
        "candidate_id": CANDIDATE_ID,
        "atom_id": ATOM_ID,
        "candidate_kind": "INERT_PROSPECTIVE_MATHEMATICAL_LEMMA_SPECIFICATION",
        "status": "FROZEN_NOT_PROVED_NOT_EXECUTED",
        "frozen_at_utc": FROZEN_AT,
        "object": "The exact C041 canonical UNSAT suffix language H_k when h[1..7] is wholly inside the literal payload and at least two clauses can be reserved outside the clauses touched by that window.",
        "qoi": "Whether an off-window contradictory clause pair certifies coordinate-wise marginal variation inside H_k and thereby removes only the local h[0..7] forced-MAGIC obstruction.",
        "definitions": {
            "a": "bit_length(v)",
            "b": "bit_length(m)",
            "header_length_H": "6+2*a+2*b",
            "literal_token_width_w": "1+a",
            "raw_length_R": "H+3*m*w",
            "padding_p": "R mod 2",
            "encoded_length_E": "R+p=2*k",
            "payload_index_interval": "[H,R-1] using zero-based inclusive bit indices before optional padding",
            "window": "h[j]=x[k+j-1] for 1<=j<=7, so the parent window is x[k..k+6]",
            "semantic_language": "H_k={1||c: there exists r such that x=r||c is an exact length-2k canonical C041 encoding of an UNSAT 3CNF}",
            "magic": "11100101",
        },
        "exact_quantified_candidate": {
            "cell_quantifiers": "For every positive integer tuple (k,a,b,m) satisfying b=bit_length(m), a>=2, m>=4, R=H+3*m*(1+a), p=R mod 2, and R+p=2*k",
            "window_premise": "H<=k and k+6<R, equivalently x[k..k+6] lies wholly in the unpadded literal payload",
            "full_a_cell_quantifier": "for every v with 2^(a-1)<=v<=2^a-1",
            "marginal_quantifiers": "for every j in {1,...,7} and every epsilon in {0,1}",
            "existential_conclusion": "there exists an exact canonical UNSAT length-2k parent word x, with h=1||x[k:], such that h[j]=epsilon",
            "anchor_structure": "the clauses touched by x[k..k+6] are left available for the coordinate witness, while two untouched clauses are reserved as opposite repeated-unit clauses on one legal variable",
            "coordinate_corollary": "h[0]=1=MAGIC[0], and both marginal values are proposed for every h[j], 1<=j<=7; therefore no coordinate j in {0,...,7} is universally forced unequal to MAGIC[j] over H_k",
        },
        "touched_clause_bound_candidate": {
            "claim": "The seven consecutive payload bits touch at most two clauses because each clause occupies 3*(1+a)>=9 consecutive payload bits.",
            "reserve_consequence": "Since m>=4, at least two clauses remain untouched and are available for the opposite repeated-unit UNSAT anchor.",
        },
        "marginal_not_independent_caveat": {
            "asserted_meaning": "For each fixed (v,j,epsilon), a possibly different H_k member may witness h[j]=epsilon.",
            "not_asserted": [
                "one common formula realizes arbitrary prescribed values at all seven coordinates",
                "all 2^7 window patterns occur",
                "two witnesses can be chosen to differ only at coordinate j",
                "other bits of the same variable-index token remain fixed while one index bit flips",
            ],
            "reason_for_boundary": "Legal variable indices form {1,...,v}, not an unconstrained Boolean a-cube; coordinate-wise marginal support is the exact quantifier needed for the local forced-coordinate corollary.",
        },
        "adjacent_support_corollary_boundary": {
            "additional_premise": "At least one current C041 support cell has encoded length 2*(k+1).",
            "proposed_local_effect": "The current prefix exposes MAGIC[0..7], while the parent semantic language has no universally unequal coordinate among h[0..7].",
            "non_effect": "This does not construct or prove an element of H_k intersection P_(k+1).",
        },
        "smallest_planned_public_regression": {
            "status": "UNEVALUATED_PLANNED_REGRESSION_IDENTITY_ONLY",
            "selection_rule": "least k among cells satisfying every lemma premise and having nonempty adjacent current support",
            "expected_parent_cell_for_future_proof": {
                "k": 31,
                "a": 2,
                "b": 3,
                "m": 5,
                "v_range": [2, 3],
                "H": 16,
                "w": 3,
                "R": 61,
                "p": 1,
                "E": 62,
                "window_parent_indices": [31, 37],
                "window_payload_offsets": [15, 21],
                "expected_touched_clause_indices_one_based": [2, 3],
            },
            "expected_exhaustive_current_cells_for_future_proof": [
                {"a_plus": 1, "b_plus": 4, "m_plus": 8, "v_plus_range": [1, 1], "R_plus": 64, "p_plus": 0},
                {"a_plus": 4, "b_plus": 2, "m_plus": 3, "v_plus_range": [8, 15], "R_plus": 63, "p_plus": 1},
                {"a_plus": 6, "b_plus": 2, "m_plus": 2, "v_plus_range": [32, 63], "R_plus": 64, "p_plus": 0},
            ],
            "required_current_encoded_length": 64,
            "witness_formulas_or_labels_included": False,
            "arithmetic_or_semantic_evaluation_executed_in_this_round": False,
            "authority": "FROZEN_EXPECTATION_FOR_LATER_PROOF_NOT_A_RESULT",
        },
        "proof_obligations_for_future_authorized_check": [
            "O1_EXACT_C041_HEADER_TOKEN_RAW_AND_PADDED_LENGTH_IDENTITIES",
            "O2_SEVEN_BIT_PAYLOAD_INTERVAL_TOUCHES_AT_MOST_TWO_CLAUSES",
            "O3_M_GE_4_LEAVES_TWO_UNTOUCHED_CLAUSES",
            "O4_OPPOSITE_REPEATED_UNIT_CLAUSES_ARE_CANONICAL_FOR_EVERY_V_IN_FULL_A_CELL",
            "O5_RESERVED_ANCHOR_PAIR_MAKES_THE_WHOLE_FORMULA_UNSAT_INDEPENDENT_OF_TOUCHED_CLAUSES",
            "O6_EVERY_SIGN_PHASE_HAS_BOTH_MARGINAL_VALUES_INSIDE_H_K",
            "O7_EVERY_VARIABLE_INDEX_BIT_HAS_BOTH_LEGAL_MARGINAL_VALUES_FOR_EVERY_FIXED_V_IN_THE_FULL_A_CELL",
            "O8_LITERAL_CONTENT_CHANGES_PRESERVE_HEADER_LENGTH_PADDING_AND_EXACT_H_K_BINDING",
            "O9_H0_EQUALS_MAGIC0_AND_EACH_H1_THROUGH_H7_HAS_A_MAGIC_MATCHING_H_K_MEMBER",
            "O10_K31_PARENT_PREMISES_AND_WINDOW_TO_CLAUSE_BINDING",
            "O11_LENGTH64_CURRENT_SUPPORT_BRANCH_EXHAUSTION",
            "O12_NO_SMALLER_ADJACENT_SUPPORTED_PREMISE_CELL",
            "O13_MARGINAL_QUANTIFIER_IS_NOT_STRENGTHENED_TO_SINGLE_BIT_FLIP_OR_JOINT_PATTERN_COVERAGE",
        ],
        "allowed_future_result_branches": [
            "PROVED_EXACT_QUANTIFIED_SCOPE",
            "REFUTED_BY_EXACT_COUNTEREXAMPLE_OR_BROKEN_OBLIGATION",
            "CANNOT_CHECK",
        ],
        "future_result_firewall": {
            "implementation_present": False,
            "decoder_or_sat_executed": False,
            "formula_witness_constructed": False,
            "k31_regression_executed": False,
            "hidden_world_materialized_or_label_accessed": False,
            "overlap_compared": False,
            "proof_checked": False,
        },
        "source_identity": {
            "application_base_commit": APPLICATION_BASE_SHA,
            "framework_pin": FRAMEWORK_SHA,
            "pre_candidate_trace": {"path": str(PRE_TRACE.relative_to(ROOT)), "git_blob": PRE_TRACE_BLOB, "raw_sha256": file_raw_sha(PRE_TRACE)},
            "context": {"path": str(CONTEXT.relative_to(ROOT)), "git_blob": CONTEXT_BLOB, "raw_sha256": file_raw_sha(CONTEXT)},
            "c041_grammar": {"path": str(C041_SOURCE.relative_to(ROOT)), "git_blob": C041_SOURCE_BLOB, "raw_sha256": file_raw_sha(C041_SOURCE)},
            "pre_candidate_last_event": "O9d12a2a1b-C052-V21-E32",
        },
        "lineage": {
            "superseding_parent_atom": "O9d12a2a1b-C052-V2.1",
            "public_v2_invalid_freeze_preserved": True,
            "v1_semantic_subset_failure_preserved": True,
            "consumed_k20_not_reused_as_hidden_validation": True,
            "candidate_generated_only_after_v21_pre_candidate_packet_merged": True,
        },
        "non_guarantees": [
            "no proof or mathematical result in this freeze",
            "no H_k intersection P_(k+1) witness or impossibility result",
            "no classifier, kernel, adapter, falsifier, or evaluator implementation",
            "no hidden label, theorem novelty, independent review, circuit lower bound, or P-versus-NP authority",
        ],
        "credit": {
            "mathematical_result": 0,
            "mathematical_saturation": 0,
            "software_process": 0,
            "independent_review": 0,
        },
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def falsifier_manifest(candidate: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "falsifier_id": FALSIFIER_ID,
        "candidate_id": CANDIDATE_ID,
        "candidate_artifact_hash": candidate["artifact_hash"],
        "atom_id": ATOM_ID,
        "identity_kind": "INERT_FUTURE_FALSIFIER_MANIFEST",
        "status": "FROZEN_NOT_IMPLEMENTED_NOT_EXECUTED",
        "frozen_at_utc": FROZEN_AT,
        "independence_boundary": {
            "same_context_role_separated_not_independent_peer_review": True,
            "candidate_implementation_import_allowed": False,
            "candidate_proof_certificate_reuse_allowed": False,
            "future_checker_must_rederive_source_identities_and_every_obligation": True,
        },
        "future_inputs": [
            "exact candidate bytes and artifact hash",
            "exact C041 grammar identity",
            "one explicit premise cell or a symbolic universal proof domain",
            "formula-bound H_k membership and UNSAT evidence only after separate authorization",
        ],
        "ordered_future_checks": [
            "validate source identity, full quantifier domain, length equations, and payload-window premise",
            "rederive maximum touched-clause count and untouched-clause reserve",
            "check repeated-unit anchor legality and symbolic UNSAT implication",
            "check sign and every variable-index bit marginal over each fixed v in the full a-cell",
            "check exact canonical bytes, split, h coordinate, and H_k membership for any later witness",
            "check the marginal-not-single-bit-flip boundary is preserved",
            "check k31 minimality and every length64 current support branch without reading overlap labels",
        ],
        "decisive_refuters": [
            "one premise-satisfying cell whose seven-bit window touches three or more clauses",
            "one premise-satisfying cell with fewer than two untouched clauses",
            "one fixed v in an a>=2 cell and one index-bit position lacking either legal marginal among indices 1 through v",
            "one exact C041 grammar rule that rejects the reserved repeated-unit clauses",
            "one satisfying assignment to the claimed opposite-unit anchor conjunction",
            "one literal-content change that alters the registered length or padding inside a fixed cell",
            "one j and epsilon for which complete proof shows no formula-bound H_k witness exists",
            "one smaller adjacent-supported cell satisfying every frozen premise",
            "one omitted length64 current support cell or one listed current cell that fails exact support",
        ],
        "cannot_check_conditions": [
            "source identity mismatch",
            "incomplete a-cell or support-cell quantification",
            "missing canonical or UNSAT evidence",
            "coordinate or padding ambiguity",
            "only ambient syntax variation is shown",
            "candidate is silently strengthened to joint-pattern or single-bit-flip coverage",
        ],
        "allowed_future_outcomes": ["CANDIDATE_SURVIVES_EXACT_SCOPE", "CANDIDATE_REFUTED", "CANNOT_CHECK"],
        "planned_public_regressions": [
            "k31 off-window parent/current support identity after separate proof-check authorization"
        ],
        "hidden_world_policy": {
            "hidden_labels_included": False,
            "hidden_value_materialized": False,
            "consumed_k20_excluded_from_fresh_hidden_validation": True,
        },
        "execution_surface": {
            "implementation_path": None,
            "entrypoint": None,
            "executed": False,
        },
        "credit": {"mathematical_result": 0, "independent_review": 0, "root_authority": 0},
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def candidate_trace_delta(candidate: dict, falsifier: dict) -> dict:
    prior = json.loads(PRE_TRACE.read_text(encoding="utf-8"))
    previous = prior["entries"][-1]
    event = {
        "event_id": "O9d12a2a1b-C052-V21-E33",
        "atom_id": ATOM_ID,
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": FROZEN_AT,
        "chronology_order_index": 33,
        "chronology_basis": "EXACT_MERGED_MAIN_THEN_LOCAL_RESULT_BLIND_CANDIDATE_FREEZE",
        "state_summary": "The v2.1 pre-candidate packet is public on exact main; only an inert off-window marginal-lemma identity and future falsifier manifest are frozen.",
        "action_summary": "Freeze the exact quantified off-window UNSAT-anchor lemma, its marginal-only boundary, and a planned unevaluated k31 regression.",
        "evidence_pointers": [str(CANDIDATE.relative_to(ROOT)), str(FALSIFIER.relative_to(ROOT))],
        "alternatives_considered": [
            "execute constructed witnesses now",
            "freeze a stronger single-bit-flip statement",
            "reuse consumed k20 as hidden validation",
            "freeze the exact marginal lemma and defer every proof/evaluation",
        ],
        "decision_rationale": "The marginal quantifier is sufficient for the local forced-coordinate corollary, while proof, regression, and overlap must remain later separately authorized actions.",
        "outputs": [candidate["artifact_hash"], falsifier["artifact_hash"], "ZERO_MATHEMATICAL_RESULT_CREDIT"],
        "uncertainties": [
            "the lemma has not been proof-checked in this freeze",
            "k31 arithmetic and semantic obligations remain planned",
            "same-context review is not independent peer review",
        ],
        "residuals": [
            "future proof-check authorization required",
            "actual H_k intersection P_(k+1) remains open",
            "P-versus-NP root remains open",
        ],
        "next_steps": [
            "PR and merge this candidate identity after review",
            "freeze a separate proof-check authorization before constructing witnesses or executing the k31 regression",
        ],
        "previous_event_hash": previous["artifact_hash"],
    }
    event["artifact_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(event, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return event


def freeze_receipt(candidate: dict, falsifier: dict) -> dict:
    trace_delta = candidate_trace_delta(candidate, falsifier)
    return seal({
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C052-V21-OFFWINDOW-CANDIDATE-FREEZE-RECEIPT-20260812",
        "atom_id": ATOM_ID,
        "candidate_id": CANDIDATE_ID,
        "frozen_at_utc": FROZEN_AT,
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_pin": FRAMEWORK_SHA,
        "source_identities": {
            "pre_candidate_trace_git_blob": PRE_TRACE_BLOB,
            "pre_candidate_trace_raw_sha256": file_raw_sha(PRE_TRACE),
            "pre_candidate_last_event_id": "O9d12a2a1b-C052-V21-E32",
            "candidate_artifact_hash": candidate["artifact_hash"],
            "candidate_raw_sha256": raw_sha(candidate),
            "falsifier_artifact_hash": falsifier["artifact_hash"],
            "falsifier_raw_sha256": raw_sha(falsifier),
            "candidate_trace_delta_artifact_hash": trace_delta["artifact_hash"],
        },
        "public_trace_delta": trace_delta,
        "chronology": {
            "v21_pre_candidate_packet_merged_before_candidate": True,
            "candidate_identity_frozen": True,
            "falsifier_manifest_frozen": True,
            "implementation_created": False,
            "formula_witness_constructed": False,
            "proof_or_falsifier_executed": False,
            "k31_regression_executed": False,
            "hidden_label_accessed": False,
            "overlap_or_native_result_accessed": False,
        },
        "frozen_scope": [
            "exact quantified marginal off-window lemma identity",
            "marginal-not-single-bit-flip caveat",
            "proof obligations and decisive falsifiers",
            "k31 as an unevaluated planned public regression identity",
        ],
        "authority": {
            "candidate_is_proposal_only": True,
            "mathematical_result_credit": 0,
            "mathematical_saturation_credit": 0,
            "independent_review": False,
            "p_vs_np_authority": False,
            "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
        "next_authorized_action": "PR_REVIEW_MERGE_ONLY_NO_PROOF_OR_EVALUATION",
    })


def build() -> tuple[dict, dict, dict]:
    candidate = candidate_document()
    falsifier = falsifier_manifest(candidate)
    receipt = freeze_receipt(candidate, falsifier)
    return candidate, falsifier, receipt


def write() -> tuple[dict, dict, dict]:
    values = build()
    for path, value in zip((CANDIDATE, FALSIFIER, RECEIPT), values):
        path.write_bytes(canonical_bytes(value))
    return values


if __name__ == "__main__":
    write()
