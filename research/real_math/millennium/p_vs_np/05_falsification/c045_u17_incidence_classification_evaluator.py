#!/usr/bin/env python3
"""Frozen C045 certificate classifier for a later post-freeze task.

This module does not import a decoder, enumerate the target, or construct any
incidence relation.  A later authorized task must separately produce a complete
analytic/exhaustive certificate.  Only then may this frozen classifier select
one of the five preregistered branches.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


POST_FREEZE_AUTHORIZATION_REQUIRED = True
CANDIDATE_ID = "C045-U17-INCIDENCE-CLASSIFICATION-PLAN-v1"
APPLICATION_BASE_SHA = "4653b516349d158279a8792aa503c209ed0cecab"
FROZEN_AT = "2026-08-12T01:18:28Z"
DECODER_GIT_BLOB = "fcc4814dd618da96ef9bb8144a4783a0a6e886e1"
DECODER_RAW_SHA256 = "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"
SPARSE_GIT_BLOB = "f81c4b20af57528432e1077810528be02450c7c3"
SPARSE_RAW_SHA256 = "a151014f45b0fd6ac7a0235b01b0f6fd8de8b7b2d1d816dca3e8dd4e6dd32e3b"

BRANCHES = (
    "NO_NEW_SEMANTIC_CELL",
    "NO_CROSS_COMPONENT_COUPLING",
    "CROSS_COMPONENT_COUPLING_WITNESS",
    "OLD_TYPE_COLLISION_OR_SPLIT",
    "CANNOT_CHECK",
)
ANALYTIC_OBLIGATIONS = ("C045-A1", "C045-A2", "C045-A3", "C045-A4")
EXHAUSTIVE_OBLIGATIONS = (
    "C045-E1",
    "C045-E2",
    "C045-E3",
    "C045-E4",
    "C045-E5",
    "C045-E6",
    "C045-E7",
)


class EvidenceContractError(RuntimeError):
    """Raised when post-freeze authorization or evidence syntax is invalid."""


def _load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise EvidenceContractError(f"{path}: top-level JSON must be an object")
    return value


def _self_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def validate_post_freeze_authorization(authorization: dict) -> None:
    required = {
        "status": "AUTHORIZED_POST_FREEZE_EXECUTION",
        "candidate_id": CANDIDATE_ID,
        "authorized_action": "RUN_C045_INCIDENCE_CERTIFICATE_CLASSIFIER",
        "target_access_authorized": True,
        "evaluator_raw_sha256": _self_sha256(),
    }
    for key, expected in required.items():
        if authorization.get(key) != expected:
            raise EvidenceContractError(f"authorization mismatch: {key}")
    authorized_at = authorization.get("authorized_at")
    if not isinstance(authorized_at, str) or authorized_at <= FROZEN_AT:
        raise EvidenceContractError("authorization must postdate the freeze")
    receipt_path = authorization.get("freeze_receipt_path")
    receipt_hash = authorization.get("freeze_receipt_artifact_hash")
    if not isinstance(receipt_path, str) or not receipt_path:
        raise EvidenceContractError("authorization lacks freeze receipt path")
    if not isinstance(receipt_hash, str) or not receipt_hash.startswith("sha256:"):
        raise EvidenceContractError("authorization lacks freeze receipt hash")
    receipt = _load_object(Path(receipt_path))
    receipt_payload = dict(receipt)
    receipt_payload["artifact_hash"] = ""
    if receipt.get("artifact_hash") != receipt_hash:
        raise EvidenceContractError("authorization receipt hash mismatch")
    if _canonical_sha256(receipt_payload) != receipt_hash:
        raise EvidenceContractError("freeze receipt artifact hash is invalid")
    if receipt.get("candidate_id") != CANDIDATE_ID:
        raise EvidenceContractError("freeze receipt candidate mismatch")
    evaluator_binding = (
        receipt.get("full_document_integrity", {})
        .get("byte_inputs", {})
        .get("evaluator_source", {})
    )
    if evaluator_binding.get("raw_sha256") != _self_sha256():
        raise EvidenceContractError("freeze receipt evaluator hash mismatch")


def _source_identity_errors(certificate: dict) -> list[str]:
    identity = certificate.get("source_identity")
    if not isinstance(identity, dict):
        return ["SOURCE_IDENTITY_MISSING"]
    expected = {
        "application_base_commit": APPLICATION_BASE_SHA,
        "decoder_git_blob": DECODER_GIT_BLOB,
        "decoder_raw_sha256": DECODER_RAW_SHA256,
        "sparse_semantics_git_blob": SPARSE_GIT_BLOB,
        "sparse_semantics_raw_sha256": SPARSE_RAW_SHA256,
        "target_extension": "U16_TO_U17_IMMEDIATE_SOURCE_EXTENSION",
    }
    return [
        f"SOURCE_IDENTITY_MISMATCH:{key}"
        for key, expected_value in expected.items()
        if identity.get(key) != expected_value
    ]


def _obligation_errors(certificate: dict) -> list[str]:
    errors: list[str] = []
    groups = (
        ("analytic_obligations", ANALYTIC_OBLIGATIONS),
        ("exhaustive_obligations", EXHAUSTIVE_OBLIGATIONS),
    )
    for field, required_ids in groups:
        obligations = certificate.get(field)
        if not isinstance(obligations, dict):
            errors.append(f"{field.upper()}_MISSING")
            continue
        if set(obligations) != set(required_ids):
            errors.append(f"{field.upper()}_SET_INCOMPLETE")
            continue
        for obligation_id in required_ids:
            record = obligations.get(obligation_id)
            if not isinstance(record, dict):
                errors.append(f"{obligation_id}:RECORD_MISSING")
                continue
            if record.get("status") != "PROVED_OR_EXHAUSTIVELY_CHECKED":
                errors.append(f"{obligation_id}:NOT_DISCHARGED")
            pointer = record.get("evidence_pointer")
            if not isinstance(pointer, str) or not pointer:
                errors.append(f"{obligation_id}:EVIDENCE_MISSING")
    return errors


def _cannot_check(reasons: list[str]) -> dict:
    return {
        "candidate_id": CANDIDATE_ID,
        "branch": "CANNOT_CHECK",
        "reasons": sorted(set(reasons)),
        "authority": {
            "incidence_classification_only": True,
            "grants_cover_or_lower_bound_conclusion": False,
            "grants_circuit_lower_bound": False,
            "grants_p_vs_np_authority": False,
        },
    }


def classify_certificate(certificate: dict, authorization: dict) -> dict:
    """Classify a later complete certificate without generating target data."""

    validate_post_freeze_authorization(authorization)
    errors: list[str] = []
    if certificate.get("candidate_id") != CANDIDATE_ID:
        errors.append("CANDIDATE_ID_MISMATCH")
    errors.extend(_source_identity_errors(certificate))
    errors.extend(_obligation_errors(certificate))
    observations = certificate.get("branch_observations")
    if not isinstance(observations, dict):
        errors.append("BRANCH_OBSERVATIONS_MISSING")
        return _cannot_check(errors)
    if errors:
        return _cannot_check(errors)

    collision = observations.get("old_type_collision_or_split")
    new_cell = observations.get("new_semantic_cell_exists")
    coupling = observations.get("cross_component_coupling_exists")
    if not all(value in (True, False) for value in (collision, new_cell)):
        return _cannot_check(["COLLISION_OR_NEW_CELL_TRUTH_VALUE_INCOMPLETE"])

    no_collision_pointer = observations.get("no_old_type_collision_or_split_certificate")
    collision_pointer = observations.get("old_type_collision_or_split_evidence")
    if collision:
        if not isinstance(collision_pointer, str) or not collision_pointer:
            return _cannot_check(["COLLISION_OR_SPLIT_EVIDENCE_MISSING"])
        branch = "OLD_TYPE_COLLISION_OR_SPLIT"
        pointer = collision_pointer
    elif not isinstance(no_collision_pointer, str) or not no_collision_pointer:
        return _cannot_check(["NO_COLLISION_EXHAUSTIVE_CERTIFICATE_MISSING"])
    elif not new_cell:
        pointer = observations.get("no_new_semantic_cell_certificate")
        if not isinstance(pointer, str) or not pointer:
            return _cannot_check(["NO_NEW_CELL_EXHAUSTIVE_CERTIFICATE_MISSING"])
        branch = "NO_NEW_SEMANTIC_CELL"
    elif coupling not in (True, False):
        return _cannot_check(["COUPLING_TRUTH_VALUE_INCOMPLETE"])
    elif coupling:
        pointer = observations.get("cross_component_coupling_witness")
        if not isinstance(pointer, str) or not pointer:
            return _cannot_check(["COUPLING_WITNESS_MISSING"])
        branch = "CROSS_COMPONENT_COUPLING_WITNESS"
    else:
        pointer = observations.get("no_cross_component_coupling_certificate")
        if not isinstance(pointer, str) or not pointer:
            return _cannot_check(["NO_COUPLING_EXHAUSTIVE_CERTIFICATE_MISSING"])
        branch = "NO_CROSS_COMPONENT_COUPLING"

    if branch not in BRANCHES:
        return _cannot_check(["UNREGISTERED_BRANCH"])
    return {
        "candidate_id": CANDIDATE_ID,
        "branch": branch,
        "evidence_pointer": pointer,
        "authority": {
            "incidence_classification_only": True,
            "grants_cover_or_lower_bound_conclusion": False,
            "grants_circuit_lower_bound": False,
            "grants_p_vs_np_authority": False,
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--post-freeze-authorization", type=Path, required=True)
    parser.add_argument("--certificate", type=Path, required=True)
    args = parser.parse_args(argv)
    authorization = _load_object(args.post_freeze_authorization)
    certificate = _load_object(args.certificate)
    print(
        json.dumps(
            classify_certificate(certificate, authorization), indent=2, sort_keys=True
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
