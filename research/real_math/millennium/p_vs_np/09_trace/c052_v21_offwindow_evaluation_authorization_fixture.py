"""Build the result-blind C052 off-window lemma evaluation authorization.

This fixture authorizes only a later proof check of the already-public lemma
obligations and the already-public k=31 regression.  It contains no proof,
formula witness, result, evaluator implementation, overlap value, hidden world,
or native-parametric evaluation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C052_V21_OFFWINDOW_UNSAT_ANCHOR_LEMMA_FREEZE_20260812.json"
FALSIFIER = PNP / "05_falsification/O9d12a2a1b_C052_V21_OFFWINDOW_LEMMA_FALSIFIER_MANIFEST_20260812.json"
FREEZE_RECEIPT = PNP / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_CANDIDATE_FREEZE_RECEIPT_20260812.json"
OUTPUT = PNP / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_EVALUATION_AUTHORIZATION_20260812.json"

BASE_COMMIT = "329a69493762fc7df086c45e8d194486bcb53ef3"
BASE_MERGED_AT_UTC = "2026-08-12T14:10:16Z"
FROZEN_AT_UTC = "2026-08-12T14:12:22Z"
CANDIDATE_ID = "PNP-C052-OFFWINDOW-UNSAT-ANCHOR-MARGINAL-LEMMA-v1"
EXPECTED_CANDIDATE_ARTIFACT_HASH = "sha256:04f0e62b88ee03c371c92f998340c842e82d822fed2f378dabb04eee549f1ab5"
EXPECTED_CANDIDATE_RAW_SHA256 = "sha256:9c1916588060aaa127b8c5a3828e9c5f07840e7f8ee986bba819829e6e3accab"
EXPECTED_CANDIDATE_GIT_BLOB = "02938109aa792a671440bafda1ac0dc577e0bded"
EXPECTED_FALSIFIER_ARTIFACT_HASH = "sha256:655487d3814bcfa2eeedc0ef87f0082f6dd17fbf6df0cf3741dabd9d8ed69675"
EXPECTED_FALSIFIER_RAW_SHA256 = "sha256:01fa7f0c38989ab8335d646bdbdddde2e7cc3ccce2475ae151ee42b4fa394bfc"
EXPECTED_FALSIFIER_GIT_BLOB = "ad9d03e2bbe761e74ccbc3c2a7b6c6f7959d4137"
EXPECTED_RECEIPT_ARTIFACT_HASH = "sha256:d5c400811bca69b77e5e35198ed6ed766ab24e8b9938325b94f6dc149e71f912"
EXPECTED_RECEIPT_RAW_SHA256 = "sha256:50197b46f4f55d96238c4e67a038ec7fcc279e1937e7d0b9f15c2fb8584ce008"
EXPECTED_RECEIPT_GIT_BLOB = "c29bf41888ca6b22908a57c29ade247a94c94176"


def digest(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def seal(document: dict) -> dict:
    core = dict(document)
    core.pop("artifact_hash", None)
    core["artifact_hash"] = digest(
        json.dumps(core, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    )
    return core


def _load_bound_sources() -> tuple[dict, dict, dict]:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    falsifier = json.loads(FALSIFIER.read_text(encoding="utf-8"))
    receipt = json.loads(FREEZE_RECEIPT.read_text(encoding="utf-8"))
    checks = [
        (candidate["candidate_id"], CANDIDATE_ID, "candidate id"),
        (falsifier["candidate_id"], CANDIDATE_ID, "falsifier candidate id"),
        (receipt["candidate_id"], CANDIDATE_ID, "receipt candidate id"),
        (candidate["artifact_hash"], EXPECTED_CANDIDATE_ARTIFACT_HASH, "candidate artifact hash"),
        (digest(CANDIDATE.read_bytes()), EXPECTED_CANDIDATE_RAW_SHA256, "candidate raw hash"),
        (falsifier["artifact_hash"], EXPECTED_FALSIFIER_ARTIFACT_HASH, "falsifier artifact hash"),
        (digest(FALSIFIER.read_bytes()), EXPECTED_FALSIFIER_RAW_SHA256, "falsifier raw hash"),
        (receipt["artifact_hash"], EXPECTED_RECEIPT_ARTIFACT_HASH, "receipt artifact hash"),
        (digest(FREEZE_RECEIPT.read_bytes()), EXPECTED_RECEIPT_RAW_SHA256, "receipt raw hash"),
    ]
    for actual, expected, label in checks:
        if actual != expected:
            raise RuntimeError(f"{label} mismatch: {actual} != {expected}")
    return candidate, falsifier, receipt


def build() -> dict:
    candidate, falsifier, receipt = _load_bound_sources()
    obligations = candidate["proof_obligations_for_future_authorized_check"]
    if obligations != [f"O{i}_{suffix}" for i, suffix in enumerate([
        "EXACT_C041_HEADER_TOKEN_RAW_AND_PADDED_LENGTH_IDENTITIES",
        "SEVEN_BIT_PAYLOAD_INTERVAL_TOUCHES_AT_MOST_TWO_CLAUSES",
        "M_GE_4_LEAVES_TWO_UNTOUCHED_CLAUSES",
        "OPPOSITE_REPEATED_UNIT_CLAUSES_ARE_CANONICAL_FOR_EVERY_V_IN_FULL_A_CELL",
        "RESERVED_ANCHOR_PAIR_MAKES_THE_WHOLE_FORMULA_UNSAT_INDEPENDENT_OF_TOUCHED_CLAUSES",
        "EVERY_SIGN_PHASE_HAS_BOTH_MARGINAL_VALUES_INSIDE_H_K",
        "EVERY_VARIABLE_INDEX_BIT_HAS_BOTH_LEGAL_MARGINAL_VALUES_FOR_EVERY_FIXED_V_IN_THE_FULL_A_CELL",
        "LITERAL_CONTENT_CHANGES_PRESERVE_HEADER_LENGTH_PADDING_AND_EXACT_H_K_BINDING",
        "H0_EQUALS_MAGIC0_AND_EACH_H1_THROUGH_H7_HAS_A_MAGIC_MATCHING_H_K_MEMBER",
        "K31_PARENT_PREMISES_AND_WINDOW_TO_CLAUSE_BINDING",
        "LENGTH64_CURRENT_SUPPORT_BRANCH_EXHAUSTION",
        "NO_SMALLER_ADJACENT_SUPPORTED_PREMISE_CELL",
        "MARGINAL_QUANTIFIER_IS_NOT_STRENGTHENED_TO_SINGLE_BIT_FLIP_OR_JOINT_PATTERN_COVERAGE",
    ], start=1)]:
        raise RuntimeError("candidate proof-obligation identity changed")

    return seal({
        "schema_version": "1.0.0",
        "authorization_id": "PNP-C052-V21-OFFWINDOW-EVALUATION-AUTHORIZATION-20260812",
        "atom_id": "O9d12a2a1b-C052-V2.1",
        "candidate_id": CANDIDATE_ID,
        "authorization_kind": "PUBLIC_RESULT_BLIND_PROOF_AND_PUBLIC_REGRESSION_AUTHORIZATION",
        "application_base_commit": BASE_COMMIT,
        "framework_pin": "d21592b0ff8da988deabb923fd549891ff8ad9f0",
        "source_bindings": {
            "candidate": {
                "path": str(CANDIDATE.relative_to(ROOT)),
                "artifact_hash": candidate["artifact_hash"],
                "raw_sha256": digest(CANDIDATE.read_bytes()),
                "git_blob_at_application_base": EXPECTED_CANDIDATE_GIT_BLOB,
            },
            "falsifier": {
                "path": str(FALSIFIER.relative_to(ROOT)),
                "falsifier_id": falsifier["falsifier_id"],
                "artifact_hash": falsifier["artifact_hash"],
                "raw_sha256": digest(FALSIFIER.read_bytes()),
                "git_blob_at_application_base": EXPECTED_FALSIFIER_GIT_BLOB,
            },
            "candidate_freeze_receipt": {
                "path": str(FREEZE_RECEIPT.relative_to(ROOT)),
                "artifact_hash": receipt["artifact_hash"],
                "raw_sha256": digest(FREEZE_RECEIPT.read_bytes()),
                "git_blob_at_application_base": EXPECTED_RECEIPT_GIT_BLOB,
            },
        },
        "chronology": {
            "candidate_freeze_public_merge": BASE_COMMIT,
            "candidate_freeze_public_merged_at_utc": BASE_MERGED_AT_UTC,
            "authorization_frozen_at_utc": FROZEN_AT_UTC,
            "evaluation_may_begin_only_after_authorization_public_merge": True,
            "proof_or_falsifier_executed_in_this_round": False,
            "formula_witness_constructed_in_this_round": False,
            "k31_regression_executed_in_this_round": False,
            "result_or_label_accessed_in_this_round": False,
            "overlap_native_or_hidden_execution_in_this_round": False,
        },
        "authorized_after_public_merge": {
            "proof_obligations_in_exact_order": list(obligations),
            "public_k31_regression": {
                "authorized": True,
                "public_only_not_hidden_validation": True,
                "selection_rule": candidate["smallest_planned_public_regression"]["selection_rule"],
                "required_current_encoded_length": candidate["smallest_planned_public_regression"]["required_current_encoded_length"],
                "expected_parent_cell": candidate["smallest_planned_public_regression"]["expected_parent_cell_for_future_proof"],
                "expected_current_cells": candidate["smallest_planned_public_regression"]["expected_exhaustive_current_cells_for_future_proof"],
                "must_discharge_obligations": ["O10", "O11", "O12"],
                "consumed_k20_not_reused_as_hidden_validation": True,
            },
            "falsifier_requirements": list(falsifier["ordered_future_checks"]),
            "allowed_result_branches": list(candidate["allowed_future_result_branches"]),
            "result_recording": "MACHINE_READABLE_RECEIPT_WITH_EXACT_PUBLIC_EVIDENCE_AFTER_CHECK_ONLY",
        },
        "marginal_not_independent_caveat": dict(candidate["marginal_not_independent_caveat"]),
        "fail_closed_rules": {
            "any_unchecked_O1_through_O13": "CANNOT_CHECK",
            "source_identity_mismatch": "CANNOT_CHECK",
            "incomplete_full_a_cell_or_length64_support_enumeration": "CANNOT_CHECK",
            "missing_formula_bound_H_k_or_UNSAT_evidence": "CANNOT_CHECK",
            "joint_pattern_or_single_bit_flip_strengthening": "CANDIDATE_REFUTED_OR_STATEMENT_NARROWED_TO_FROZEN_MARGINAL_SCOPE",
        },
        "forbidden_capabilities": [
            "overlap comparison or execution",
            "native parametric target selection or execution",
            "hidden-world materialization, label access, or execution",
            "reuse of consumed k20 as fresh hidden validation",
            "modification of the frozen candidate or falsifier after evaluated result access",
        ],
        "non_authority": [
            "this authorization contains no proof, result, or formula witness",
            "authorization and later computation are not a proof",
            "same-context review is not independent peer review",
            "no H_k intersection P_(k+1), cover, circuit, novelty, or P-versus-NP claim is authorized",
        ],
        "credit": {
            "mathematical_result": 0,
            "mathematical_saturation": 0,
            "software_process": 0,
            "independent_review": 0,
        },
        "result_state": "UNEVALUATED",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def write() -> dict:
    document = build()
    OUTPUT.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return document


if __name__ == "__main__":
    write()
