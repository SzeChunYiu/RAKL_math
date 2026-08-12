"""Build the result-blind C045 candidate/evaluator freeze documents.

This fixture contains specification data and hashing only.  It does not import
or execute the frozen evaluator, any decoder, or any target-data producer.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ATOM = "O9d12a2a1b-C045"
CANDIDATE_ID = "C045-U17-INCIDENCE-CLASSIFICATION-PLAN-v1"
APPLICATION_BASE_SHA = "4653b516349d158279a8792aa503c209ed0cecab"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
PRE_GATE_GIT_BLOB = "d89d70c745abe03060cb0a916cbe375ae1c65f1b"
PRE_GATE_CANONICAL_SHA256 = "sha256:bad15fef7e3914dc54a85d6e306dfb553242a3b1ecbe83a8f28a64827634c118"
PRE_TRACE_LAST_EVENT_HASH = "sha256:83cb11b84072c529c9e617e448dfefaa693f04e6a6bd4ba9f737bc4aae0a3de9"
DECODER_GIT_BLOB = "fcc4814dd618da96ef9bb8144a4783a0a6e886e1"
DECODER_RAW_SHA256 = "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"
SPARSE_GIT_BLOB = "f81c4b20af57528432e1077810528be02450c7c3"
SPARSE_RAW_SHA256 = "a151014f45b0fd6ac7a0235b01b0f6fd8de8b7b2d1d816dca3e8dd4e6dd32e3b"
EVALUATOR_RAW_SHA256 = "692973741158f8123c0c4f19a306d9bc45a9ff9ba86e574199e5962b345e3211"

PNP = "research/real_math/millennium/p_vs_np"
PRE_GATE_PATH = f"{PNP}/09_trace/O9d12a2a1b_C045_LATEST_RAKL_GATE_RECEIPT_20260812.json"
PRE_TRACE_PATH = f"{PNP}/09_trace/O9d12a2a1b_C045_PRE_CANDIDATE_TRACE_20260812.json"
DECODER_PATH = f"{PNP}/04_candidates/C041_fx_sat_one_sided.py"
SPARSE_PATH = f"{PNP}/05_falsification/c041_sparse_bridge_repair.py"
CANDIDATE_PATH = (
    f"{PNP}/04_candidates/"
    "O9d12a2a1b_C045_U17_INCIDENCE_CLASSIFICATION_PLAN_FREEZE_20260812.json"
)
EVALUATOR_PATH = f"{PNP}/05_falsification/c045_u17_incidence_classification_evaluator.py"
EVALUATOR_MANIFEST_PATH = (
    f"{PNP}/05_falsification/"
    "O9d12a2a1b_C045_U17_INCIDENCE_EVALUATOR_FREEZE_20260812.json"
)
TRACE_PATH = f"{PNP}/09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_TRACE_20260812.json"
RECEIPT_PATH = f"{PNP}/09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_RECEIPT_20260812.json"

REGISTERED_BRANCHES = [
    "NO_NEW_SEMANTIC_CELL",
    "NO_CROSS_COMPONENT_COUPLING",
    "CROSS_COMPONENT_COUPLING_WITNESS",
    "OLD_TYPE_COLLISION_OR_SPLIT",
    "CANNOT_CHECK",
]
BRANCH_PRECEDENCE = [
    "CANNOT_CHECK_ON_IDENTITY_OR_COMPLETENESS_FAILURE",
    "OLD_TYPE_COLLISION_OR_SPLIT",
    "NO_NEW_SEMANTIC_CELL",
    "CROSS_COMPONENT_COUPLING_WITNESS",
    "NO_CROSS_COMPONENT_COUPLING",
]


def _hash(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _with_artifact_hash(payload: dict) -> dict:
    document = dict(payload)
    document["artifact_hash"] = ""
    document["artifact_hash"] = _hash(document)
    return document


def _source_identity() -> dict:
    return {
        "application_base_commit": APPLICATION_BASE_SHA,
        "framework_commit": FRAMEWORK_SHA,
        "pre_candidate_gate": {
            "path": PRE_GATE_PATH,
            "git_blob": PRE_GATE_GIT_BLOB,
            "canonical_sha256": PRE_GATE_CANONICAL_SHA256,
        },
        "decoder": {
            "path": DECODER_PATH,
            "git_blob": DECODER_GIT_BLOB,
            "raw_sha256": DECODER_RAW_SHA256,
            "use_boundary": "IDENTITY_ONLY_NOT_IMPORTED_OR_EXECUTED_IN_THIS_FREEZE",
        },
        "sparse_semantics": {
            "path": SPARSE_PATH,
            "git_blob": SPARSE_GIT_BLOB,
            "raw_sha256": SPARSE_RAW_SHA256,
            "use_boundary": "IDENTITY_ONLY_NOT_IMPORTED_OR_EXECUTED_IN_THIS_FREEZE",
        },
    }


def _analytic_obligations() -> list[dict]:
    return [
        {
            "obligation_id": "C045-A1",
            "requirement": "Verify exact application-base, framework, decoder, sparse-semantics, and pre-candidate-gate identities before any target access.",
            "failure_branch": "CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-A2",
            "requirement": "Derive the complete U16-to-U17 source syntax and canonical cross-band residual cases analytically from the frozen source definition, without learning them from outputs.",
            "failure_branch": "CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-A3",
            "requirement": "Prove that the analytic residual cases are mutually exclusive and cover every source-defined canonical case; keep the fallback branch separate.",
            "failure_branch": "CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-A4",
            "requirement": "Freeze the branch predicates, precedence, evidence schema, and falsifiers before later evaluator or decoder execution.",
            "failure_branch": "CANNOT_CHECK",
        },
    ]


def _exhaustive_obligations() -> list[dict]:
    return [
        {
            "obligation_id": "C045-E1",
            "requirement": "Later, enumerate the complete frozen source domain for the immediate extension and prove coverage rather than sample it.",
            "failure_branch": "CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-E2",
            "requirement": "Later, prove every emitted relation belongs to exactly one frozen analytic case and that no source case or relation is omitted or duplicated.",
            "failure_branch": "CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-E3",
            "requirement": "Later, recompute every row and column neighbourhood from the full accumulated old-plus-new history on both sides.",
            "failure_branch": "CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-E4",
            "requirement": "Later, certify the twin partitions biconditionally and classify every inherited-type collision or split before component attribution.",
            "failure_branch": "OLD_TYPE_COLLISION_OR_SPLIT_OR_CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-E5",
            "requirement": "Later, certify the exact quotient-complement support extensionally from the full-history twin classes.",
            "failure_branch": "CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-E6",
            "requirement": "Later, map every eligible quotient endpoint to inherited component provenance and test every new support incidence for cross-component coupling.",
            "failure_branch": "CANNOT_CHECK",
        },
        {
            "obligation_id": "C045-E7",
            "requirement": "Later, discharge exactly one registered branch under the frozen precedence and attach a complete proof or exhaustive certificate pointer.",
            "failure_branch": "CANNOT_CHECK",
        },
    ]


def _branch_definitions() -> list[dict]:
    return [
        {
            "branch": "CANNOT_CHECK",
            "precedence_rank": 1,
            "predicate": "Any source-identity, analytic coverage, exhaustive coverage, full-history twin, provenance, or evidence obligation is incomplete or inconsistent.",
            "required_evidence": ["bounded reason codes for every failed obligation"],
            "non_implications": ["not evidence for or against coupling", "not permission to change the evaluator"],
        },
        {
            "branch": "OLD_TYPE_COLLISION_OR_SPLIT",
            "precedence_rank": 2,
            "predicate": "Complete full-history recomputation proves an inherited twin class splits or a previously distinct old/new endpoint type collides, so inherited component attribution is not stable.",
            "required_evidence": ["explicit proof/certificate pointer for the collision or split", "complete twin-partition certificate"],
            "non_implications": ["does not establish cross-component coupling", "does not establish cover growth"],
        },
        {
            "branch": "NO_NEW_SEMANTIC_CELL",
            "precedence_rank": 3,
            "predicate": "After stable full-history twins are certified, the complete immediate-extension relation adds no semantic quotient-support cell.",
            "required_evidence": ["exhaustive no-new-cell certificate", "complete source-domain coverage certificate"],
            "non_implications": ["does not prove future stagnation", "does not determine a cover value"],
        },
        {
            "branch": "CROSS_COMPONENT_COUPLING_WITNESS",
            "precedence_rank": 4,
            "predicate": "With stable inherited provenance and at least one new semantic cell, a certified new support incidence has endpoints in distinct inherited active components.",
            "required_evidence": ["one checkable witness pointer", "complete provenance and quotient-support certificates"],
            "non_implications": ["retires only the separable transfer precondition", "does not prove a cover lower bound"],
        },
        {
            "branch": "NO_CROSS_COMPONENT_COUPLING",
            "precedence_rank": 5,
            "predicate": "With stable inherited provenance and at least one new semantic cell, exhaustive exact support classification proves every new incidence stays within one inherited component.",
            "required_evidence": ["exhaustive no-coupling certificate", "complete provenance and quotient-support certificates"],
            "non_implications": ["does not prove a transferred upper bound until local preconditions are checked", "does not determine a cover value"],
        },
    ]


def _falsifiers() -> list[dict]:
    return [
        {"falsifier_id": "C045-F1", "condition": "Any bound source identity differs from the frozen identity.", "effect": "CANNOT_CHECK"},
        {"falsifier_id": "C045-F2", "condition": "The analytic source-case partition is incomplete or overlapping.", "effect": "CANNOT_CHECK"},
        {"falsifier_id": "C045-F3", "condition": "Target relations are sampled or inferred rather than exhaustively certified.", "effect": "CANNOT_CHECK"},
        {"falsifier_id": "C045-F4", "condition": "Any old-band relation is omitted from full-history neighbourhood recomputation.", "effect": "CANNOT_CHECK"},
        {"falsifier_id": "C045-F5", "condition": "An old type collision or split is left unclassified before component attribution.", "effect": "CANNOT_CHECK"},
        {"falsifier_id": "C045-F6", "condition": "One certified new support incidence joins distinct inherited components.", "effect": "FALSIFIES_NO_CROSS_COMPONENT_COUPLING"},
        {"falsifier_id": "C045-F7", "condition": "A coupling claim lacks a checkable witness pointer and complete provenance certificate.", "effect": "CANNOT_CHECK"},
        {"falsifier_id": "C045-F8", "condition": "A no-new-cell or no-coupling claim lacks an exhaustive completeness certificate.", "effect": "CANNOT_CHECK"},
        {"falsifier_id": "C045-F9", "condition": "Target output is accessed before this candidate, evaluator, and receipt are frozen.", "effect": "MARK_RETROSPECTIVE_AND_MOVE_STRICT_ASSURANCE_TO_A_NEW_UNTOUCHED_TARGET"},
    ]


def candidate_document() -> dict:
    return _with_artifact_hash(
        {
            "schema_version": "1.0.0",
            "candidate_id": CANDIDATE_ID,
            "atom_id": ATOM,
            "candidate_kind": "TYPED_PLAN_ONLY_NO_TARGET_OUTPUT",
            "frozen_at": "2026-08-12T01:18:28Z",
            "target_extension": "U16_TO_U17_IMMEDIATE_SOURCE_EXTENSION",
            "qoi": "EXACT_FULL_HISTORY_QUOTIENT_COMPONENT_INCIDENCE",
            "source_identity": _source_identity(),
            "registered_branches": REGISTERED_BRANCHES,
            "branch_precedence": BRANCH_PRECEDENCE,
            "branch_definitions": _branch_definitions(),
            "analytic_obligations": _analytic_obligations(),
            "exhaustive_obligations": _exhaustive_obligations(),
            "falsifiers": _falsifiers(),
            "evidence_contract": {
                "obligation_records": "exactly C045-A1..A4 and C045-E1..E7, each discharged with a nonempty evidence pointer",
                "branch_observations": [
                    "old_type_collision_or_split",
                    "new_semantic_cell_exists",
                    "cross_component_coupling_exists",
                ],
                "positive_branch_evidence": "proof/certificate pointer required under the frozen branch definition",
                "raw_target_data_in_freeze_packet": False,
            },
            "target_access": {
                "decoder_imported_or_executed": False,
                "evaluator_imported_or_executed": False,
                "target_enumerated": False,
                "target_output_accessed": False,
                "outcome_branch_selected": False,
            },
            "authority": {
                "licensed_action_exercised": "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY",
                "generic_runtime_candidate_paths_non_authoritative": True,
                "target_evaluator_execution_authorized": False,
                "grants_incidence_outcome": False,
                "grants_cover_or_lower_bound_conclusion": False,
                "grants_circuit_lower_bound": False,
                "grants_p_vs_np_authority": False,
                "mathematical_saturation_credit": False,
                "mathematical_result_credit": False,
            },
        }
    )


def evaluator_manifest_document(candidate: dict) -> dict:
    return _with_artifact_hash(
        {
            "schema_version": "1.0.0",
            "manifest_id": "PNP-C045-U17-INCIDENCE-EVALUATOR-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "frozen_at": "2026-08-12T01:18:29Z",
            "status": "FROZEN_FOR_LATER_POST_FREEZE_EXECUTION_NOT_RUN",
            "candidate_binding": {
                "path": CANDIDATE_PATH,
                "artifact_hash": candidate["artifact_hash"],
                "canonical_sha256": _hash(candidate),
            },
            "evaluator": {
                "path": EVALUATOR_PATH,
                "raw_sha256": EVALUATOR_RAW_SHA256,
                "classification_contract": "certificate-only five-branch classifier; produces no target relation",
            },
            "source_identity": _source_identity(),
            "required_analytic_obligation_ids": [f"C045-A{i}" for i in range(1, 5)],
            "required_exhaustive_obligation_ids": [f"C045-E{i}" for i in range(1, 8)],
            "registered_branches": REGISTERED_BRANCHES,
            "branch_precedence": BRANCH_PRECEDENCE,
            "later_execution_gate": {
                "post_freeze_authorization_required": True,
                "authorization_must_postdate_freeze": True,
                "authorization_must_bind_evaluator_raw_sha256": True,
                "authorization_must_bind_freeze_receipt": True,
                "current_task_execution_authorized": False,
            },
            "target_access": {
                "decoder_imported_or_executed": False,
                "evaluator_imported_or_executed": False,
                "target_enumerated": False,
                "target_output_accessed": False,
                "outcome_branch_selected": False,
            },
            "authority": {
                "evaluator_freeze_only": True,
                "generic_runtime_candidate_paths_non_authoritative": True,
                "grants_incidence_outcome": False,
                "grants_cover_or_lower_bound_conclusion": False,
                "mathematical_saturation_credit": False,
                "mathematical_result_credit": False,
            },
        }
    )


def trace_document(candidate: dict, manifest: dict) -> dict:
    pre_trace_path = Path(__file__).with_name(
        "O9d12a2a1b_C045_PRE_CANDIDATE_TRACE_20260812.json"
    )
    pre_trace = json.loads(pre_trace_path.read_text(encoding="utf-8"))
    if pre_trace["entries"][-1]["artifact_hash"] != PRE_TRACE_LAST_EVENT_HASH:
        raise ValueError("pre-candidate trace head does not match the frozen gate")
    payload = {
        "event_id": "O9d12a2a1b-C045-E09",
        "atom_id": ATOM,
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": "2026-08-12T01:18:30Z",
        "state_summary": "The merged result-blind pre-candidate gate licenses one typed incidence-classification plan. The plan and inert evaluator are frozen without importing or executing target-capable code and without observing an outcome.",
        "action_summary": "Freeze the branch-complete C045 plan and exact later evaluator identity only.",
        "evidence_pointers": [PRE_GATE_PATH, CANDIDATE_PATH, EVALUATOR_MANIFEST_PATH, EVALUATOR_PATH],
        "alternatives_considered": [
            "execute the target immediately",
            "run a cover or lower-bound search",
            "freeze only prose without evaluator identity",
            "freeze one typed certificate classifier and defer execution",
        ],
        "decision_rationale": "The pre-candidate receipt licenses only a plan freeze. Exact evaluator and source identities plus complete obligations make the later discriminator reproducible while preserving target blindness.",
        "outputs": [
            CANDIDATE_ID,
            "PLAN_ONLY",
            "TARGET_OUTCOME_UNOBSERVED",
            "ZERO_MATHEMATICAL_RESULT_CREDIT",
            f"candidate_artifact_hash:{candidate['artifact_hash']}",
            f"evaluator_manifest_artifact_hash:{manifest['artifact_hash']}",
            f"evaluator_raw_sha256:{EVALUATOR_RAW_SHA256}",
        ],
        "uncertainties": [
            "the target incidence branch is unobserved",
            "same-context review is not independent peer review",
        ],
        "residuals": [
            "later analytic/exhaustive certificate production remains pending",
            "no cover conclusion is licensed",
            "root remains OPEN",
        ],
        "next_steps": [
            "in a separate post-freeze task, authorize and run the exact evaluator only after verifying this receipt",
            "record the applicable falsifier and result trace events only after authorized target access",
        ],
        "previous_event_hash": PRE_TRACE_LAST_EVENT_HASH,
    }
    event = dict(payload)
    event["artifact_hash"] = _hash(payload)
    return {
        "trace_id": "PNP-O9d12a2a1b-C045-CANDIDATE-FREEZE-TRACE-20260812",
        "entries": [*pre_trace["entries"], event],
    }


def receipt_document(candidate: dict, manifest: dict, trace: dict) -> dict:
    full_document_integrity = {
        "algorithm": "SHA-256",
        "json_canonicalization": "JSON_SORT_KEYS_COMPACT_UTF8",
        "json_inputs": {
            "pre_candidate_gate": {
                "path": PRE_GATE_PATH,
                "canonical_sha256": PRE_GATE_CANONICAL_SHA256,
                "git_blob": PRE_GATE_GIT_BLOB,
            },
            "candidate": {"path": CANDIDATE_PATH, "canonical_sha256": _hash(candidate)},
            "evaluator_manifest": {"path": EVALUATOR_MANIFEST_PATH, "canonical_sha256": _hash(manifest)},
            "trace": {"path": TRACE_PATH, "canonical_sha256": _hash(trace)},
        },
        "byte_inputs": {
            "evaluator_source": {"path": EVALUATOR_PATH, "raw_sha256": EVALUATOR_RAW_SHA256},
            "decoder_source": {"path": DECODER_PATH, "raw_sha256": DECODER_RAW_SHA256, "git_blob": DECODER_GIT_BLOB},
            "sparse_semantics_source": {"path": SPARSE_PATH, "raw_sha256": SPARSE_RAW_SHA256, "git_blob": SPARSE_GIT_BLOB},
        },
        "self_binding_excluded": RECEIPT_PATH,
    }
    return _with_artifact_hash(
        {
            "schema_version": "1.0.0",
            "receipt_id": "PNP-C045-U17-INCIDENCE-CANDIDATE-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "frozen_at": "2026-08-12T01:18:31Z",
            "application_base_commit": APPLICATION_BASE_SHA,
            "framework_commit": FRAMEWORK_SHA,
            "full_document_integrity": full_document_integrity,
            "full_document_integrity_hash": _hash(full_document_integrity),
            "chronology": {
                "pre_candidate_gate_precedes_candidate": True,
                "candidate_precedes_any_target_access": True,
                "evaluator_frozen_before_any_later_execution": True,
                "decoder_imported_or_executed": False,
                "evaluator_imported_or_executed": False,
                "target_enumerated": False,
                "target_output_accessed": False,
                "outcome_branch_selected": False,
            },
            "application_authority": {
                "generic_runtime_candidate_paths_non_authoritative": True,
                "licensed_actions": ["FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"],
                "candidate_construction_authorized": False,
                "target_evaluator_execution_authorized": False,
                "cover_or_lower_bound_conclusion_authorized": False,
            },
            "credit": {
                "mathematical_saturation_credit": False,
                "mathematical_result_credit": False,
                "strict_discovery_result_credit": False,
            },
            "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
            "later_execution": {
                "status": "NOT_AUTHORIZED_IN_THIS_TASK",
                "requires_separate_post_freeze_authorization": True,
                "requires_this_receipt_and_exact_evaluator_hash": True,
                "may_only_classify_the_registered_incidence_branches": True,
            },
        }
    )


def build_documents() -> dict[str, dict]:
    candidate = candidate_document()
    manifest = evaluator_manifest_document(candidate)
    trace = trace_document(candidate, manifest)
    receipt = receipt_document(candidate, manifest, trace)
    return {
        "candidate": candidate,
        "evaluator_manifest": manifest,
        "trace": trace,
        "receipt": receipt,
    }
