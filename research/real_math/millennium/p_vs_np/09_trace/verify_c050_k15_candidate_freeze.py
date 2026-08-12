#!/usr/bin/env python3
"""Capability-free integrity and scope verifier for the C050 candidate freeze."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


BASE = Path("research/real_math/millennium/p_vs_np")
RECEIPT = BASE / "09_trace/O9d12a2a1b_C050_K15_CANDIDATE_FREEZE_RECEIPT_20260812.json"
EVALUATOR = BASE / "05_falsification/c050_k15_alignment_inert_evaluator.py"
ARTIFACTS = {
    "candidate": BASE / "04_candidates/O9d12a2a1b_C050_K15_SELECTOR_DISCRIMINATOR_FREEZE_20260812.json",
    "manifest": BASE / "05_falsification/O9d12a2a1b_C050_K15_ALIGNMENT_EVALUATOR_FREEZE_20260812.json",
    "authorization": BASE / "09_trace/O9d12a2a1b_C050_K15_EVALUATION_AUTHORIZATION_20260812.json",
    "framework_binding": BASE / "09_trace/O9d12a2a1b_C050_K15_FRAMEWORK_SUBJECT_FREEZE_BINDING_20260812.json",
    "framework_observation": BASE / "09_trace/O9d12a2a1b_C050_K15_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "trace": BASE / "09_trace/O9d12a2a1b_C050_K15_CANDIDATE_FREEZE_TRACE_20260812.json",
}


class PacketIntegrityError(RuntimeError):
    pass


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("top-level JSON must be an object")
    return value


def _canonical_hash(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _raw_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _sealed_hash(document: dict) -> str:
    subject = dict(document)
    subject["artifact_hash"] = ""
    return _canonical_hash(subject)


def audit_packet(root: Path) -> tuple[str, ...]:
    root = Path(root)
    errors: list[str] = []
    try:
        receipt = _load(root / RECEIPT)
    except Exception as exc:
        return (f"receipt: cannot load: {exc}",)

    if receipt.get("artifact_hash") != _sealed_hash(receipt):
        errors.append("receipt: artifact_hash mismatch")
    integrity = receipt.get("full_document_integrity", {})
    if integrity.get("algorithm") != "SHA-256":
        errors.append("receipt: wrong digest algorithm")
    if integrity.get("canonicalization") != "JSON_SORT_KEYS_COMPACT_UTF8":
        errors.append("receipt: wrong canonicalization")
    if receipt.get("full_document_integrity_hash") != _canonical_hash(integrity):
        errors.append("receipt: full-document integrity hash mismatch")

    json_inputs = integrity.get("json_inputs", {})
    if set(json_inputs) != set(ARTIFACTS):
        errors.append("receipt: JSON input set is not exact")
    loaded: dict[str, dict] = {}
    for name, relative_path in ARTIFACTS.items():
        binding = json_inputs.get(name, {})
        if binding.get("path") != relative_path.as_posix():
            errors.append(f"{name}: path mismatch")
            continue
        try:
            document = _load(root / relative_path)
            loaded[name] = document
        except Exception as exc:
            errors.append(f"{name}: cannot load: {exc}")
            continue
        if binding.get("canonical_sha256") != _canonical_hash(document):
            errors.append(f"{name}: full-document digest mismatch")
        if name != "trace" and document.get("artifact_hash") != _sealed_hash(document):
            errors.append(f"{name}: artifact_hash mismatch")

    byte_inputs = integrity.get("byte_inputs", {})
    evaluator_binding = byte_inputs.get("evaluator", {})
    if evaluator_binding.get("path") != EVALUATOR.as_posix():
        errors.append("evaluator: path mismatch")
    else:
        try:
            actual_evaluator_hash = _raw_sha256(root / EVALUATOR)
        except Exception as exc:
            errors.append(f"evaluator: cannot load: {exc}")
        else:
            if evaluator_binding.get("raw_sha256") != actual_evaluator_hash:
                errors.append("evaluator: raw digest mismatch")
    for name in ("pre_gate", "pre_trace"):
        binding = byte_inputs.get(name, {})
        try:
            actual = _raw_sha256(root / binding["path"])
        except Exception as exc:
            errors.append(f"{name}: cannot verify: {exc}")
            continue
        if binding.get("raw_sha256") != actual:
            errors.append(f"{name}: raw digest mismatch")

    candidate = loaded.get("candidate", {})
    if candidate:
        identity = candidate.get("candidate_identity", {})
        core = dict(candidate)
        core.pop("artifact_hash", None)
        core.pop("candidate_identity", None)
        if identity.get("canonical_core_sha256") != _canonical_hash(core):
            errors.append("candidate: canonical core identity mismatch")
        if candidate.get("selector", {}).get("selected_k") != 15:
            errors.append("candidate: selector is not k=15")
        if candidate.get("discriminator", {}).get("predicted_result") is not None:
            errors.append("candidate: target result was predicted")
        expected_branches = [
            {"v_range": [2, 3], "m": 2, "raw_length": 32, "padding": False},
            {
                "v_range": [8, 15],
                "m": 1,
                "raw_length": 31,
                "encoded_length": 32,
                "padding": True,
            },
        ]
        if (
            candidate.get("selector_proof", {}).get("length_32_canonical_regimes")
            != expected_branches
        ):
            errors.append("candidate: length-32 branch set changed")
        access = candidate.get("target_access", {})
        if any(access.get(key) is not False for key in access):
            errors.append("candidate: target-access boundary widened")

    manifest = loaded.get("manifest", {})
    if manifest:
        if manifest.get("status") != "FROZEN_INERT_CONTRACT_NOT_IMPORTED_NOT_EXECUTED":
            errors.append("manifest: evaluator is not inert")
        if manifest.get("target_result_capability") is not False:
            errors.append("manifest: target result capability widened")
    authorization = loaded.get("authorization", {})
    if authorization:
        forbidden_flags = (
            "current_task_evaluator_execution_authorized",
            "decoder_access_authorized",
            "target_bit_comparison_authorized",
            "target_result_access_authorized",
            "target_result_classification_authorized",
        )
        if any(authorization.get(key) is not False for key in forbidden_flags):
            errors.append("authorization: target capability widened")
    observation = loaded.get("framework_observation", {})
    if observation:
        if observation.get("verdict") != "CURRENT_UNCHANGED":
            errors.append("framework: subject is not current")
        if observation.get("licenses_candidate_materialization") is not True:
            errors.append("framework: candidate materialization not licensed")
        if observation.get("grants_scientific_authority") is not False:
            errors.append("framework: scientific authority widened")
    trace = loaded.get("trace", {})
    if trace:
        entries = trace.get("entries", [])
        if not entries or entries[-1].get("event_type") != "CANDIDATE_PROPOSED":
            errors.append("trace: does not end at CANDIDATE_PROPOSED")
        trace_text = json.dumps(trace, sort_keys=True)
        if "FALSIFIER_RUN" in trace_text or "RESULT_RECORDED" in trace_text:
            errors.append("trace: post-candidate result event present")
    authority = receipt.get("authority", {})
    if authority.get("target_theorem_truth") is not False:
        errors.append("receipt: target theorem authority widened")
    if authority.get("mathematical_result_credit") is not False:
        errors.append("receipt: mathematical result credit widened")
    if receipt.get("math_ledger_entry_created") is not False:
        errors.append("receipt: math ledger created prematurely")
    return tuple(errors)


def verify_packet(root: Path) -> None:
    errors = audit_packet(root)
    if errors:
        raise PacketIntegrityError("C050 k=15 freeze failed: " + "; ".join(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root", type=Path, default=Path(__file__).resolve().parents[5]
    )
    args = parser.parse_args(argv)
    try:
        verify_packet(args.repo_root)
    except PacketIntegrityError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, sort_keys=True))
        return 1
    print(
        json.dumps(
            {
                "status": "PASS",
                "candidate_id": "C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1",
                "selected_k": 15,
                "target_result_accessed": False,
                "target_result_determined": False,
                "evaluator_execution_authorized": False,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
