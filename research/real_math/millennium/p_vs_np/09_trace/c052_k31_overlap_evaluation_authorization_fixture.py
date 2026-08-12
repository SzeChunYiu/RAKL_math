"""Build the result-blind C052 k31 overlap evaluation authorization."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C052_K31_OVERLAP_DISCRIMINATOR_IDENTITY_20260812.json"
FALSIFIER = PNP / "05_falsification/O9d12a2a1b_C052_K31_OVERLAP_FALSIFIER_IDENTITY_20260812.json"
FREEZE_RECEIPT = PNP / "09_trace/O9d12a2a1b_C052_K31_OVERLAP_CANDIDATE_FREEZE_RECEIPT_20260812.json"
OUTPUT = PNP / "09_trace/O9d12a2a1b_C052_K31_OVERLAP_EVALUATION_AUTHORIZATION_20260812.json"

APPLICATION_BASE_SHA = "c8c8501105ed952dc9773f7e93dfd5418eb1c80c"
APPLICATION_BASE_MERGED_AT = "2026-08-12T15:00:14Z"
FROZEN_AT = "2026-08-12T15:02:10Z"
CANDIDATE_ID = "PNP-C052-K31-TARGET-BLIND-OVERLAP-CERTIFICATE-DISCRIMINATOR-v1"
FALSIFIER_ID = "PNP-C052-K31-OVERLAP-CERTIFICATE-FALSIFIER-v1"

BINDINGS = {
    "candidate": {
        "path": str(CANDIDATE.relative_to(ROOT)),
        "artifact_hash": "sha256:38e20ca16fdd42ce4fd1643c98abf44b5e0ffc2d6818daf372ad586fef2c717d",
        "raw_sha256": "sha256:92d145fd1240891a747fe49b3223845f0cecc2eae339a449f57b4b42af10a11b",
        "git_blob": "2297a93898c472dc7059dc9dc72e78264350cb9f",
    },
    "falsifier": {
        "path": str(FALSIFIER.relative_to(ROOT)),
        "artifact_hash": "sha256:46409b4f38ead079aa0e08e17a4321d3632a0df4dd04aa8658bb4b77cf03a972",
        "raw_sha256": "sha256:895d3f311804ce2df064eedcf2511d8aaf5c48e745ce854299f3113a38ae1a6c",
        "git_blob": "669f88431c706cb7cf569c61f539bb14009fb486",
    },
    "freeze_receipt": {
        "path": str(FREEZE_RECEIPT.relative_to(ROOT)),
        "artifact_hash": "sha256:4779f3f40ceb1b6ade1ecd378b4dc003c81722a031545bd1a57794a1d41d144c",
        "raw_sha256": "sha256:82e27329cb2bec99385d7c703cd67a17b58db898c9606417b23e82ad29854354",
        "git_blob": "e02c8c4747f45b265b209f126bdac969cf77864b",
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
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    falsifier = json.loads(FALSIFIER.read_text(encoding="utf-8"))
    receipt = json.loads(FREEZE_RECEIPT.read_text(encoding="utf-8"))
    for key, path, document in (
        ("candidate", CANDIDATE, candidate),
        ("falsifier", FALSIFIER, falsifier),
        ("freeze_receipt", FREEZE_RECEIPT, receipt),
    ):
        binding = BINDINGS[key]
        if digest(path.read_bytes()) != binding["raw_sha256"]:
            raise RuntimeError(f"{key} raw bytes moved")
        if document["artifact_hash"] != binding["artifact_hash"]:
            raise RuntimeError(f"{key} artifact hash moved")
    if candidate["candidate_id"] != CANDIDATE_ID or falsifier["falsifier_id"] != FALSIFIER_ID:
        raise RuntimeError("identity mismatch")
    if falsifier["candidate_artifact_hash"] != candidate["artifact_hash"]:
        raise RuntimeError("falsifier is not bound to candidate")

    return seal({
        "schema_version": "1.0.0",
        "authorization_id": "PNP-C052-K31-OVERLAP-EVALUATION-AUTHORIZATION-20260812",
        "atom_id": "O9d12a2a1b-C052-K31-OVERLAP",
        "candidate_id": CANDIDATE_ID,
        "falsifier_id": FALSIFIER_ID,
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_pin": "d21592b0ff8da988deabb923fd549891ff8ad9f0",
        "frozen_at_utc": FROZEN_AT,
        "exact_identity_bindings": BINDINGS,
        "chronology": {
            "candidate_freeze_public_merged_at_utc": APPLICATION_BASE_MERGED_AT,
            "authorization_frozen_after_candidate_merge": True,
            "implementation_exists_in_this_round": False,
            "validation_world_materialized_in_this_round": False,
            "formula_label_or_certificate_constructed_in_this_round": False,
            "SAT_UNSAT_or_overlap_executed_in_this_round": False,
            "result_or_branch_accessed_in_this_round": False,
            "implementation_and_execution_may_begin_only_after_this_authorization_is_publicly_merged": True,
        },
        "authorized_public_scope_after_merge": {
            "implementation": [
                "implement the exact bound source-verifying frontend and exact three-branch decision kernel",
                "implement a separately rederived falsifier that does not import candidate proof/certificate authority",
                "preserve CANNOT_CHECK for every malformed, incomplete, source-mismatched, marginal-only, ambiguous, or conflicting input",
            ],
            "public_validation_worlds_in_order": [
                "K31-PLANTED-POSITIVE-CERTIFICATE-KERNEL-v1",
                "K31-PLANTED-NEGATIVE-CERTIFICATE-KERNEL-v1",
                "K31-MALFORMED-CERTIFICATE-CANNOT-CHECK-v1",
                "K31-MARGINAL-ONLY-FALSE-POSITIVE-v1",
                "K31-SOURCE-BINDING-MISMATCH-v1",
                "K31-FRONTEND-KERNEL-BRANCH-PROPAGATION-v1",
            ],
            "actual_public_k31_evaluation": "only after every public conformance, false-positive, source-binding, and integration world passes",
            "actual_result_branches": list(candidate["allowed_branches"]),
            "result_receipt": "record exact public inputs, implementation hashes, proof/completeness evidence, branch, residuals, and zero root authority",
        },
        "fail_closed_stop_rules": {
            "any_public_validation_world_fails": "STOP_CANNOT_CHECK_NO_ACTUAL_K31_EVALUATION",
            "candidate_or_falsifier_source_binding_mismatch": "CANNOT_CHECK",
            "positive_branch_missing_formula_bound_parent_UNSAT_current_word_or_full32_equality": "CANNOT_CHECK",
            "negative_branch_missing_universal_separation_or_exhaustive_completeness_proof": "CANNOT_CHECK",
            "marginal_only_or_partial_prefix_evidence": "CANNOT_CHECK",
            "candidate_and_falsifier_disagree": "CANNOT_CHECK_AND_PRESERVE_DISAGREEMENT",
        },
        "forbidden": [
            "any implementation, world materialization, or execution before this authorization merge",
            "hidden-world materialization, label access, validation, or execution",
            "native parametric k selection, scan, extrapolation, or execution beyond public k31",
            "reuse of consumed k20 as fresh hidden validation",
            "changing candidate/falsifier/source/branch identities after evaluated result access",
            "claiming computation alone as proof or same-context work as independent peer review",
            "cover, circuit, novelty, P-versus-NP, or root promotion",
        ],
        "public_only_boundary": {
            "target_k": 31,
            "hidden_worlds_allowed": False,
            "native_parametric_expansion_allowed": False,
            "all_validation_inputs_and_receipts_must_be_public": True,
        },
        "result_state": "UNEVALUATED",
        "credit": {"mathematical_result": 0, "mathematical_saturation": 0, "software_process": 0, "independent_review": 0},
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def write() -> dict:
    document = build()
    OUTPUT.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return document


if __name__ == "__main__":
    write()
