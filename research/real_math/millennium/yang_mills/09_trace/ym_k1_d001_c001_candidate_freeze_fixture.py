from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any

ROOT = Path(__file__).resolve().parents[5]
YM = ROOT / "research/real_math/millennium/yang_mills"
PARENT_MAIN_SHA = "4c9e987483c06b56e8a060ca58ac3b98e365941f"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
ATOM = "YM-S1a2i-K1-D001"
CANDIDATE_ID = "YM-S1a2i-K1-D001-C001-TWO-STAGE-SOURCE-BRIDGE"
FROZEN_AT = "2026-08-12T15:30:00Z"

CONTEXT = "research/real_math/millennium/yang_mills/01_frontier/YM-S1a2i_K1_D001_CONTEXT_FIBER_20260812.json"
SOURCE = "research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_K1_D001_WILSON_SOURCE_APPLICABILITY_AUDIT_20260812.json"
MEMORY = "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_D001_RESEARCH_MEMORY_REVIEW_20260812.json"
SHORTCUT = "research/real_math/millennium/yang_mills/08_reviews/YM-S1a2i_K1_D001_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json"
PRE_TRACE = "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_PRE_CANDIDATE_TRACE_20260812.json"

PATHS = {
    "candidate": ROOT / "research/real_math/millennium/yang_mills/04_candidates/YM-S1a2i_K1_D001_C001_TWO_STAGE_SOURCE_BRIDGE_FREEZE_20260812.json",
    "falsifier": ROOT / "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_D001_C001_INERT_FALSIFIER_FREEZE_20260812.json",
    "trace": ROOT / "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_C001_CANDIDATE_FREEZE_TRACE_20260812.json",
    "receipt": ROOT / "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_C001_CANDIDATE_FREEZE_RECEIPT_20260812.json",
}


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def _sha(value: Any, *, prefix: bool = True) -> str:
    digest = hashlib.sha256(_canonical(value)).hexdigest()
    return f"sha256:{digest}" if prefix else digest


def _seal(document: dict[str, Any], field: str = "artifact_hash") -> dict[str, Any]:
    value = dict(document)
    value[field] = ""
    value[field] = _sha(value)
    return value


def _input_binding(path: str) -> dict[str, Any]:
    raw = (ROOT / path).read_bytes()
    document = json.loads(raw)
    blob = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", f"{PARENT_MAIN_SHA}:{path}"],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    return {
        "path": path,
        "application_commit": PARENT_MAIN_SHA,
        "git_blob": blob,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_sha256": _sha(document),
        "declared_content_hash": document.get("artifact_hash") or document.get("packet_hash") or "",
    }


def parent_bindings() -> dict[str, Any]:
    return {
        "pr": 401,
        "pr_url": "https://github.com/SzeChunYiu/RAKL_math/pull/401",
        "merge_commit": PARENT_MAIN_SHA,
        "framework_sha": FRAMEWORK_SHA,
        "inputs": {
            "context": _input_binding(CONTEXT),
            "source_audit": _input_binding(SOURCE),
            "memory_review": _input_binding(MEMORY),
            "shortcut_review": _input_binding(SHORTCUT),
            "pre_candidate_trace": _input_binding(PRE_TRACE),
        },
    }


def candidate_core(bindings: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "candidate_id": CANDIDATE_ID,
        "atom_id": ATOM,
        "candidate_kind": "SOURCE_APPLICABILITY_DISCRIMINATOR_PROTOCOL_NOT_A_PROOF_LEMMA",
        "frozen_at": FROZEN_AT,
        "source_identity": {
            "author": "Jonathan J. Wilson",
            "zenodo_version_doi": "10.5281/zenodo.19393832",
            "zenodo_concept_doi": "10.5281/zenodo.19393831",
            "pdf_filename": "4D GZ-Yang-Mills.pdf",
            "pdf_sha256": "08013e1ce75c8b2be79c62ba61f70e30024b9bb427c465ceab7ee9266236690d",
            "tex_filename": "GZYM_submission_final.tex",
            "tex_sha256": "ef936e502e84b0cafabc594c9705c16c9c1df29dc95f2a6a679b6b446c526c18",
            "authority": "PRIMARY_AUTHOR_OPEN_ARTIFACT_NOT_INDEPENDENT_PEER_REVIEW",
        },
        "parent_packet_binding": bindings,
        "two_stage_discriminator": {
            "stage_order": ["STAGE_A_SOURCE_DOMAIN_COMPATIBILITY", "STAGE_B_EXACT_FLOW_MARGIN"],
            "stage_a": {
                "stage_id": "STAGE_A_SOURCE_DOMAIN_COMPATIBILITY",
                "object": "Determine from the upstream proof of Wilson Lemma 40.3 whether separately justified C_dom,C_force,rho exist with the contraction estimate valid for every ||K_k||_k<=C_dom g_k^2 and forcing coefficient C_force.",
                "required_extractions": [
                    "C_dom with exact proof passage/provenance for the admitted K-ball coefficient",
                    "C_force with exact proof passage/provenance for the g_k^4 forcing coefficient",
                    "rho with exact proof passage/provenance and 0<rho<1",
                ],
                "no_reinterpretation_rule": "The displayed single symbol C may not be split into C_dom and C_force unless the upstream derivation independently justifies both roles and their relation.",
                "chosen_graph_radius": "c_K=4*C_force/(1-rho)",
                "pass_predicate": "all three constants are separately source-derived with exact provenance and c_K<=C_dom",
                "failure_predicate": "the constants are derived but c_K>C_dom, including the literal conflated-C case C_dom=C_force=C because 4C/(1-rho)>C",
                "cannot_check_predicate": "the upstream proof does not expose enough information to derive separately justified C_dom,C_force,rho or their compatibility",
                "next_stage_rule": "Stage B is forbidden unless Stage A passes.",
            },
            "stage_b": {
                "stage_id": "STAGE_B_EXACT_FLOW_MARGIN",
                "entry_condition": "STAGE_A_SOURCE_DOMAIN_COMPATIBILITY=PASS only",
                "source_constants": ["b_0>0", "C_beta>=0", "rho", "C_force", "c_K"],
                "frozen_interval": "0<g<=g_star, where one positive source-faithful g_star and its provenance must be frozen before result access; no value is selected in this freeze round",
                "lower_flow_factor": "L(g)=1-b_0*g^2-C_beta*g^4",
                "required_predicates": [
                    "L(g)>=0 for every 0<g<=g_star",
                    "L(g)^2>=rho+(C_force/c_K)*g^2 for every 0<g<=g_star",
                ],
                "factor_two_rejection_rule": "The pair ||K_{k+1}||<=((1+rho)/2)c_K g_k^2 and g_k^2<=2g_{k+1}^2 yields only (1+rho)c_K g_{k+1}^2 and cannot discharge the exact margin.",
                "pass_predicate": "both exact predicates are proved on the entire frozen interval",
                "failure_predicate": "Stage A passed but one exact Stage B predicate is disproved, or the claimed proof relies only on the rejected factor-two implication",
                "cannot_check_predicate": "Stage A passed but the exact interval-wide predicates cannot be proved or disproved from the authorized evidence",
            },
        },
        "allowed_result_branches": {
            "APPLICABLE_BRIDGE": "Stage A passes and Stage B passes; authority is limited to conditional applicability of the K-coordinate bridge.",
            "STRONGER_PREMISE_MISMATCH_A": "Stage A derives constants but c_K>C_dom; Stage B is not entered.",
            "FLOW_MARGIN_FAIL_B": "Stage A passes, then an exact Stage B predicate fails or the factor-two trap is the only claimed derivation.",
            "CANNOT_CHECK": "Required source derivation or exact interval-wide evidence is insufficient at either stage.",
        },
        "branch_precedence": [
            "If Stage A cannot be checked, return CANNOT_CHECK and do not enter Stage B.",
            "If Stage A is checked and fails, return STRONGER_PREMISE_MISMATCH_A and do not enter Stage B.",
            "If Stage A passes but Stage B cannot be checked, return CANNOT_CHECK.",
            "If Stage A passes and Stage B fails, return FLOW_MARGIN_FAIL_B.",
            "Return APPLICABLE_BRIDGE only when both stages pass.",
        ],
        "quantifier_order": "FIRST derive one source-faithful k-uniform C_dom,C_force,rho packet; THEN decide c_K<=C_dom; ONLY ON PASS freeze one g_star before result access; THEN require both Stage B predicates FOR ALL 0<g<=g_star.",
        "falsifiers": {
            "stage_a": "A source-faithful derivation gives c_K>C_dom; the conflated-C trap is the cheapest planted case.",
            "stage_b": "After Stage A passes, one exact interval predicate fails; the factor-two trap rejects the displayed coarse implication.",
            "authority": "Any conclusion extends beyond the local K-coordinate applicability bridge to lambda, full stable manifold, continuum limit, OS reconstruction or mass gap.",
        },
        "explicit_exclusions": [
            "NO_EVALUATOR_IMPLEMENTATION",
            "NO_SOURCE_PROOF_EXECUTION",
            "NO_HIDDEN_OR_NUMERIC_CONSTANT_VALUES",
            "NO_G_STAR_VALUE_OR_THRESHOLD_SELECTION",
            "NO_FALSIFIER_EXECUTION",
            "NO_RESULT_CLASSIFICATION_IN_THIS_ROUND",
            "NO_REFUTATION_CLAIM",
            "NO_STABLE_MANIFOLD_OR_MASS_GAP_CLAIM",
            "NO_INDEPENDENT_REVIEW_CLAIM",
        ],
        "target_access": {
            "source_proof_accessed_or_executed": False,
            "constants_derived": False,
            "g_star_selected": False,
            "stage_a_evaluated": False,
            "stage_b_evaluated": False,
            "planted_worlds_executed": False,
            "result_accessed": False,
        },
        "authority": {
            "diagnostic_candidate_proposal": True,
            "strict_proof_candidate_authority": False,
            "mathematical_result_credit": False,
            "proof_authority": False,
            "target_truth": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
        "operator_process_note": "The direct operator instruction freezes this diagnostic protocol after PR401. It does not convert the PR401 CANNOT_CHECK shortcut review into theorem or method authority.",
        "future_result_lesson_contract": {
            "current_status": "NO_RESULT_NO_LESSON",
            "required_after_material_result": [
                "attempted_mathematical_implication",
                "exact_mathematical_result_or_failure",
                "supported_and_competing_mathematical_causes",
                "scope",
                "mathematical_falsifier",
                "repair_or_next_discriminator",
                "proof_or_source_evidence",
            ],
            "operational_metadata_zero_math_credit": [
                "Git/branch/PR state",
                "CI/tests",
                "schemas/hashes/chronology",
                "telemetry/repository growth",
            ],
        },
    }


def candidate_document(bindings: dict[str, Any]) -> dict[str, Any]:
    core = candidate_core(bindings)
    identity = {
        "candidate_id": CANDIDATE_ID,
        "canonical_core_sha256": _sha(core),
        "identity_scope": "FULL_CANDIDATE_CORE_BEFORE_IDENTITY_AND_ARTIFACT_HASH",
    }
    return _seal({**core, "candidate_identity": identity})


def planted_worlds() -> list[dict[str, Any]]:
    return [
        {
            "world_id": "WORLD-A-B-PASS-SEPARATE-CONSTANTS-EXACT-MARGIN",
            "world_kind": "PLANTED_PASS_SPECIFICATION_NO_VALUES",
            "structural_payload": ["C_dom,C_force,rho are independently source-derived", "4C_force/(1-rho)<=C_dom", "one g_star is frozen before result access", "both exact L(g) predicates hold on the full interval"],
            "expected_branch": "APPLICABLE_BRIDGE",
            "purpose": "Clean PASS world for the two-stage routing contract; it supplies no target constants.",
        },
        {
            "world_id": "WORLD-A-FAIL-CONFLATED-C-TRAP",
            "world_kind": "PLANTED_FAIL_SPECIFICATION_NO_VALUES",
            "structural_payload": ["the only justified statement uses C_dom=C_force=C", "0<rho<1", "c_K=4C/(1-rho)>C"],
            "expected_branch": "STRONGER_PREMISE_MISMATCH_A",
            "purpose": "Reject post hoc splitting or domain enlargement when the source proof supports only the displayed conflated C.",
        },
        {
            "world_id": "WORLD-B-FAIL-FACTOR-TWO-TRAP",
            "world_kind": "PLANTED_FAIL_SPECIFICATION_NO_VALUES",
            "structural_payload": ["Stage A passes", "the claimed Stage B proof uses only ((1+rho)/2)c_K g_k^2 and g_k^2<=2g_{k+1}^2", "the product coefficient is 1+rho>1"],
            "expected_branch": "FLOW_MARGIN_FAIL_B",
            "purpose": "Reject the coarse factor-two implication as a proof of the exact next-radius margin.",
        },
        {
            "world_id": "WORLD-CANNOT-CHECK-UPSTREAM-CONSTANTS",
            "world_kind": "PLANTED_CANNOT_CHECK_SPECIFICATION_NO_VALUES",
            "structural_payload": ["the upstream proof does not expose separately justified C_dom and C_force", "no authorized derivation supplies their relation"],
            "expected_branch": "CANNOT_CHECK",
            "purpose": "Ensure missing source evidence fails closed rather than inventing constants.",
        },
    ]


def build_documents() -> dict[str, dict[str, Any]]:
    bindings = parent_bindings()
    candidate = candidate_document(bindings)
    declarative_core = {
        "schema_version": "1.0.0",
        "manifest_id": "YM-S1a2i-K1-D001-C001-DECLARATIVE-FALSIFIER-20260812",
        "candidate_id": CANDIDATE_ID,
        "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
        "planted_worlds": planted_worlds(),
        "world_payload_policy": "Structural predicate specifications only; no hidden, symbolic-assigned, or numeric constant values are chosen in this round.",
        "evaluator_identity": None,
        "evaluator_path": None,
        "evaluator_implementation_present": False,
        "current_round_execution_authorized": False,
        "source_proof_execution_authorized": False,
        "result_classification_authorized": False,
        "future_authorization_status": "NOT_CREATED; authorization is a separate post-merge round",
        "mathematical_result_credit": False,
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    }
    falsifier_identity = {
        "manifest_id": declarative_core["manifest_id"],
        "candidate_id": CANDIDATE_ID,
        "canonical_core_sha256": _sha(declarative_core),
        "identity_scope": "FULL_DECLARATIVE_FALSIFIER_CORE_BEFORE_IDENTITY_AND_ARTIFACT_HASH",
    }
    falsifier = _seal({**declarative_core, "falsifier_identity": falsifier_identity, "artifact_hash": ""})
    pre_trace = json.loads((ROOT / PRE_TRACE).read_text())
    entries = list(pre_trace["entries"])
    event = {
        "event_id": "YM-S1a2i-K1-D001-E08",
        "atom_id": ATOM,
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": FROZEN_AT,
        "state_summary": "PR401 is public at exact main and the two-stage source-applicability discriminator plus declarative planted-world identities are now frozen without target evaluation.",
        "action_summary": "Freeze the Stage A domain-compatibility gate, conditional Stage B exact flow margin, four result branches, and declarative trap worlds; do not create authorization or evaluator code.",
        "evidence_pointers": [CONTEXT, SOURCE, str(PATHS["candidate"].relative_to(ROOT)), str(PATHS["falsifier"].relative_to(ROOT))],
        "alternatives_considered": ["execute the Wilson proof now", "choose hidden constants", "create authorization now", "implement an inert evaluator", "freeze declarations only"],
        "decision_rationale": "The diagnostic declaration is the exact cheapest next action from PR401; authorization and evaluator implementation are separate post-merge concerns.",
        "outputs": [CANDIDATE_ID, candidate["candidate_identity"]["canonical_core_sha256"], falsifier_identity["canonical_core_sha256"], "FROZEN_UNEVALUATED", "ZERO_MATHEMATICAL_RESULT_CREDIT"],
        "uncertainties": ["The upstream proof may not separate C_dom and C_force.", "No g_star or exact interval result is available in this round."],
        "residuals": ["Stage A unevaluated", "Stage B gated and unevaluated", "evaluation authorization absent", "root OPEN_NO_SOLUTION_CERTIFICATE"],
        "next_steps": ["merge this exact freeze", "create separate post-merge evaluation authorization", "only then implement/evaluate Stage A before any Stage B action"],
        "artifact_hash": "",
        "previous_event_hash": entries[-1]["artifact_hash"],
    }
    event = _seal(event)
    entries.append(event)
    trace = {"trace_id": "TRACE-YM-S1a2i-K1-D001-C001-FREEZE-20260812", "entries": entries}
    documents: dict[str, dict[str, Any]] = {"candidate": candidate, "falsifier": falsifier, "trace": trace}
    integrity = {
        "json_outputs": {
            name: {"path": str(PATHS[name].relative_to(ROOT)), "canonical_sha256": _sha(document)}
            for name, document in sorted(documents.items())
        },
        "parent_packet": bindings,
    }
    receipt = _seal(
        {
            "schema_version": "1.0.0",
            "receipt_id": "YM-S1a2i-K1-D001-C001-CANDIDATE-FALSIFIER-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "candidate_artifact_hash": candidate["artifact_hash"],
            "falsifier_artifact_hash": falsifier["artifact_hash"],
            "falsifier_core_sha256": falsifier_identity["canonical_core_sha256"],
            "trace_canonical_sha256": _sha(trace),
            "frozen_at": FROZEN_AT,
            "chronology": {
                "application_parent_commit": PARENT_MAIN_SHA,
                "pr401_packet_precedes_candidate": True,
                "candidate_publication_status": "TO_BE_COMMITTED_BEFORE_ANY_EVALUATION",
                "evaluation_authorization_created": False,
                "evaluator_implementation_present": False,
                "source_proof_executed": False,
                "falsifier_executed": False,
                "g_star_selected": False,
                "result_accessed": False,
            },
            "full_document_integrity": integrity,
            "full_document_integrity_hash": _sha(integrity),
            "authority": {
                "candidate_is_diagnostic_proposal": True,
                "target_truth": False,
                "independent_review": False,
                "mathematical_result_credit": False,
                "mathematical_saturation_credit": False,
                "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            },
            "allowed_next_action": "PUBLIC FREEZE ONLY; AUTHORIZATION AND EVALUATOR IMPLEMENTATION REQUIRE A SEPARATE POST-MERGE ROUND.",
            "artifact_hash": "",
        }
    )
    documents["receipt"] = receipt
    return documents


def write_documents() -> None:
    for name, document in build_documents().items():
        path = PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_documents()
