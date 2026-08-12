"""Build the result-blind C053 k32 clean-phase evaluation authorization.

This checkpoint binds the already-merged candidate/evaluator/falsifier identities.
It does not construct a word, decode a formula, materialize a hostile world, or
select a result branch.  Subsequent evaluation work is allowed only after this
authorization is committed as its own public-history checkpoint.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C053_K32_CLEAN_PHASE_COMPATIBILITY_IDENTITY_20260812.json"
EVALUATOR = PNP / "05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATOR_IDENTITY_20260812.json"
FALSIFIER = PNP / "05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_FALSIFIER_IDENTITY_20260812.json"
FREEZE_RECEIPT = PNP / "09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_CANDIDATE_FREEZE_RECEIPT_20260812.json"
OUTPUT = PNP / "09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATION_AUTHORIZATION_20260812.json"

APPLICATION_BASE_SHA = "04d8ca7af5c007d3d5f93dd9f47b411a07e95822"
CANDIDATE_MERGE_SHA = "461393f748af13ae9500f368aefbefc0da90f715"
CANDIDATE_MERGED_AT = "2026-08-12T17:19:32Z"
FROZEN_AT = "2026-08-12T17:35:00Z"
CANDIDATE_ID = "PNP-C053-K32-CLEAN-PHASE-FULL-WORD-COMPATIBILITY-v1"
EVALUATOR_ID = "PNP-C053-K32-CLEAN-PHASE-SOURCE-BOUND-EVALUATOR-v1"
FALSIFIER_ID = "PNP-C053-K32-CLEAN-PHASE-FALSIFIER-v1"

BINDINGS = {
    "candidate": {
        "path": str(CANDIDATE.relative_to(ROOT)),
        "artifact_hash": "sha256:81f173681f6178507eef8e32b71857fccb8308c87dd6be588e0aeba172dd87fb",
        "raw_sha256": "sha256:78f4f33b0c9b73f9df6bcca661ec2cac3eac917866c02bcafd4aa5b5652e278f",
        "git_blob": "d384ab91ea2e22c6f9a3c9a8357a386917266399",
    },
    "evaluator": {
        "path": str(EVALUATOR.relative_to(ROOT)),
        "artifact_hash": "sha256:c227e468481a6347940ffb68a369fcc0f54ea584e0f51ad31eae4cca5ffaf3d1",
        "raw_sha256": "sha256:df6a58632f296525014c702eafc332a77a7ab8dd10e3d08599f20e438a5bf076",
        "git_blob": "d846db29e1b37484354a17ffcf58d477ad8946cf",
    },
    "falsifier": {
        "path": str(FALSIFIER.relative_to(ROOT)),
        "artifact_hash": "sha256:4b90366ef589154a4401250ff557738e945a4115081209b3c42c473d8c29f0fe",
        "raw_sha256": "sha256:3edec6ab1e60260cbc9e462454941533879ce0f61c88bad1768608d75f30cebe",
        "git_blob": "c122a3a9dc04948f537ac6c967dff1897b2bb744",
    },
    "freeze_receipt": {
        "path": str(FREEZE_RECEIPT.relative_to(ROOT)),
        "artifact_hash": "sha256:0dbdb2ed3d0d387790474e980e292453d0911553895fbbb6cfdd283247ada9a0",
        "raw_sha256": "sha256:71bdab0d7aedbf68a0cb82ad7198733e599c94964f165fcb096afec36fa2e8e2",
        "git_blob": "8d678dd9562703d10888bddbb462bc9a91384e72",
    },
}


def digest(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def seal(document: dict) -> dict:
    core = dict(document)
    core.pop("artifact_hash", None)
    core["artifact_hash"] = digest(
        json.dumps(core, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    )
    return core


def build() -> dict:
    documents = {
        "candidate": json.loads(CANDIDATE.read_text(encoding="utf-8")),
        "evaluator": json.loads(EVALUATOR.read_text(encoding="utf-8")),
        "falsifier": json.loads(FALSIFIER.read_text(encoding="utf-8")),
        "freeze_receipt": json.loads(FREEZE_RECEIPT.read_text(encoding="utf-8")),
    }
    paths = {
        "candidate": CANDIDATE,
        "evaluator": EVALUATOR,
        "falsifier": FALSIFIER,
        "freeze_receipt": FREEZE_RECEIPT,
    }
    for key, document in documents.items():
        binding = BINDINGS[key]
        if digest(paths[key].read_bytes()) != binding["raw_sha256"]:
            raise RuntimeError(f"{key} raw bytes moved")
        if document["artifact_hash"] != binding["artifact_hash"]:
            raise RuntimeError(f"{key} artifact hash moved")
    candidate = documents["candidate"]
    evaluator = documents["evaluator"]
    falsifier = documents["falsifier"]
    if candidate["candidate_id"] != CANDIDATE_ID:
        raise RuntimeError("candidate identity mismatch")
    if evaluator["evaluator_id"] != EVALUATOR_ID or falsifier["falsifier_id"] != FALSIFIER_ID:
        raise RuntimeError("evaluator/falsifier identity mismatch")
    if evaluator["candidate_artifact_hash"] != candidate["artifact_hash"]:
        raise RuntimeError("evaluator is not bound to candidate")
    if falsifier["evaluator_artifact_hash"] != evaluator["artifact_hash"]:
        raise RuntimeError("falsifier is not bound to evaluator")

    return seal({
        "schema_version": "1.0.0",
        "authorization_id": "PNP-C053-K32-CLEAN-PHASE-EVALUATION-AUTHORIZATION-20260812",
        "atom_id": "O9d12a2a1b-C053-K32-CLEAN-PHASE-COMPATIBILITY",
        "candidate_id": CANDIDATE_ID,
        "evaluator_id": EVALUATOR_ID,
        "falsifier_id": FALSIFIER_ID,
        "application_base_sha": APPLICATION_BASE_SHA,
        "candidate_merge_sha": CANDIDATE_MERGE_SHA,
        "framework_pin": "d21592b0ff8da988deabb923fd549891ff8ad9f0",
        "frozen_at_utc": FROZEN_AT,
        "exact_identity_bindings": BINDINGS,
        "chronology": {
            "candidate_freeze_public_merged_at_utc": CANDIDATE_MERGED_AT,
            "authorization_frozen_after_candidate_merge": True,
            "implementation_exists_in_authorization_checkpoint": False,
            "validation_world_materialized_in_authorization_checkpoint": False,
            "formula_or_certificate_materialized_in_authorization_checkpoint": False,
            "SAT_UNSAT_or_label_comparison_executed_in_authorization_checkpoint": False,
            "result_or_branch_recorded_in_authorization_checkpoint": False,
            "implementation_and_execution_may_begin_only_after_this_authorization_is_committed_as_a_separate_checkpoint": True,
        },
        "authorized_scope_after_checkpoint": {
            "hand_mathematics_first": [
                "write both field-boundary tables and all 33 coordinate equalities",
                "derive a complete W1-W7 positive witness or W1-W6,W8 universal negative proof without computation",
                "treat every computational decode, equality check, SAT check, and enumeration as corroboration only",
            ],
            "implementation": [
                "implement a source-verifying exact three-branch frontend bound to the frozen identities",
                "implement a separately rederived checker that does not import caller-supplied canonicality, UNSAT, equality, or completeness authority",
                "preserve CANNOT_CHECK for every malformed, incomplete, source-mismatched, partial, ambiguous, or conflicting packet",
            ],
            "public_validation_worlds_in_order": [world["world_id"] for world in falsifier["future_worlds"]],
            "actual_32_pair_evaluation": "only after the hand certificate is explicit and every public hostile/conformance/integration world passes",
            "actual_result_branches": list(candidate["allowed_branches"]),
            "result_receipt": "record the exact hand certificate, source-bound corroboration, independent checker result, branch, residuals, seven-field mathematical lesson, and zero root authority",
        },
        "fail_closed_stop_rules": {
            "any_public_validation_world_fails": "STOP_CANNOT_CHECK_NO_ACTUAL_C053_EVALUATION",
            "candidate_evaluator_or_falsifier_source_binding_mismatch": "CANNOT_CHECK",
            "positive_branch_missing_any_W1_through_W7_obligation": "CANNOT_CHECK",
            "negative_branch_missing_universal_W8_coverage": "CANNOT_CHECK",
            "syntax_survival_partial_equality_or_satisfiable_parent": "CANNOT_CHECK",
            "candidate_and_independent_checker_disagree": "CANNOT_CHECK_AND_PRESERVE_DISAGREEMENT",
        },
        "forbidden": [
            "implementation, world materialization, exact computation, or result recording before the separate authorization checkpoint",
            "changing candidate, evaluator, falsifier, source, pair-set, or branch identities after outcome access",
            "using computation as the proof or same-context checking as independent peer review",
            "expanding beyond the exact 32 frozen parameter pairs",
            "cover, circuit, novelty, P-versus-NP, Millennium-root, or mathematical-saturation promotion",
        ],
        "public_only_boundary": {
            "target_k": 32,
            "parameter_pair_count": 32,
            "hidden_worlds_allowed": False,
            "native_parametric_expansion_allowed": False,
            "all_validation_inputs_and_receipts_must_be_public": True,
        },
        "result_state": "UNEVALUATED",
        "credit": {
            "mathematical_result": 0,
            "mathematical_saturation": 0,
            "Git_CI_schema_hash_chronology": 0,
            "independent_review": 0,
        },
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def write() -> dict:
    document = build()
    OUTPUT.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return document


if __name__ == "__main__":
    write()
