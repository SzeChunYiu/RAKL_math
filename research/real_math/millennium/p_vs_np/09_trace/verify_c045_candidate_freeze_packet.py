#!/usr/bin/env python3
"""Verify the frozen C045 plan/evaluator packet without running the evaluator."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable


PNP = Path("research/real_math/millennium/p_vs_np")
RECEIPT_PATH = PNP / "09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_RECEIPT_20260812.json"
JSON_PATHS = {
    "pre_candidate_gate": PNP
    / "09_trace/O9d12a2a1b_C045_LATEST_RAKL_GATE_RECEIPT_20260812.json",
    "candidate": PNP
    / "04_candidates/O9d12a2a1b_C045_U17_INCIDENCE_CLASSIFICATION_PLAN_FREEZE_20260812.json",
    "evaluator_manifest": PNP
    / "05_falsification/O9d12a2a1b_C045_U17_INCIDENCE_EVALUATOR_FREEZE_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_TRACE_20260812.json",
}
BYTE_PATHS = {
    "evaluator_source": PNP
    / "05_falsification/c045_u17_incidence_classification_evaluator.py",
    "decoder_source": PNP / "04_candidates/C041_fx_sat_one_sided.py",
    "sparse_semantics_source": PNP / "05_falsification/c041_sparse_bridge_repair.py",
}
BRANCHES = [
    "NO_NEW_SEMANTIC_CELL",
    "NO_CROSS_COMPONENT_COUPLING",
    "CROSS_COMPONENT_COUPLING_WITNESS",
    "OLD_TYPE_COLLISION_OR_SPLIT",
    "CANNOT_CHECK",
]
PLAN_ONLY_AUTHORITY = {
    "generic_runtime_candidate_paths_non_authoritative": True,
    "licensed_actions": ["FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"],
    "candidate_construction_authorized": False,
    "target_evaluator_execution_authorized": False,
    "cover_or_lower_bound_conclusion_authorized": False,
}


class PacketIntegrityError(RuntimeError):
    """Raised when the candidate freeze packet fails closed."""


def _reject_duplicate_keys(pairs: Iterable[tuple[str, object]]) -> dict:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys)
    if not isinstance(value, dict):
        raise ValueError("top-level JSON must be an object")
    return value


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _raw_sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _git_blob_sha1(content: bytes) -> str:
    header = f"blob {len(content)}\0".encode("ascii")
    return hashlib.sha1(header + content).hexdigest()


def _artifact_hash(document: dict) -> str:
    payload = dict(document)
    payload["artifact_hash"] = ""
    return canonical_sha256(payload)


def audit_packet(repo_root: Path | str) -> tuple[str, ...]:
    root = Path(repo_root).resolve()
    errors: list[str] = []
    try:
        receipt = _load(root / RECEIPT_PATH)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return (f"receipt: cannot load: {exc}",)

    if receipt.get("artifact_hash") != _artifact_hash(receipt):
        errors.append("receipt: artifact_hash mismatch")
    integrity = receipt.get("full_document_integrity")
    if not isinstance(integrity, dict):
        return tuple(errors + ["receipt: full_document_integrity missing"])
    if receipt.get("full_document_integrity_hash") != canonical_sha256(integrity):
        errors.append("receipt: full_document_integrity_hash mismatch")
    if integrity.get("algorithm") != "SHA-256":
        errors.append("receipt: unsupported integrity algorithm")
    if integrity.get("json_canonicalization") != "JSON_SORT_KEYS_COMPACT_UTF8":
        errors.append("receipt: unsupported JSON canonicalization")
    if integrity.get("self_binding_excluded") != RECEIPT_PATH.as_posix():
        errors.append("receipt: self-binding exclusion mismatch")

    json_bindings = integrity.get("json_inputs")
    byte_bindings = integrity.get("byte_inputs")
    if not isinstance(json_bindings, dict) or set(json_bindings) != set(JSON_PATHS):
        return tuple(errors + ["receipt: JSON input set is not exact"])
    if not isinstance(byte_bindings, dict) or set(byte_bindings) != set(BYTE_PATHS):
        return tuple(errors + ["receipt: byte input set is not exact"])
    if "receipt" in json_bindings or "receipt" in byte_bindings:
        errors.append("receipt: circular self-binding is forbidden")

    documents: dict[str, dict] = {}
    for name, relative_path in JSON_PATHS.items():
        binding = json_bindings.get(name)
        if not isinstance(binding, dict):
            errors.append(f"{name}: binding missing")
            continue
        if binding.get("path") != relative_path.as_posix():
            errors.append(f"{name}: path mismatch")
            continue
        try:
            document = _load(root / relative_path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{name}: cannot load: {exc}")
            continue
        documents[name] = document
        if binding.get("canonical_sha256") != canonical_sha256(document):
            errors.append(f"{name}: full-document digest mismatch")
        declared_blob = binding.get("git_blob")
        if declared_blob is not None:
            content = (root / relative_path).read_bytes()
            if declared_blob != _git_blob_sha1(content):
                errors.append(f"{name}: git blob mismatch")

    byte_contents: dict[str, bytes] = {}
    for name, relative_path in BYTE_PATHS.items():
        binding = byte_bindings.get(name)
        if not isinstance(binding, dict):
            errors.append(f"{name}: byte binding missing")
            continue
        if binding.get("path") != relative_path.as_posix():
            errors.append(f"{name}: byte path mismatch")
            continue
        try:
            content = (root / relative_path).read_bytes()
        except OSError as exc:
            errors.append(f"{name}: cannot load bytes: {exc}")
            continue
        byte_contents[name] = content
        if binding.get("raw_sha256") != _raw_sha256(content):
            errors.append(f"{name}: raw SHA-256 mismatch")
        declared_blob = binding.get("git_blob")
        if declared_blob is not None and declared_blob != _git_blob_sha1(content):
            errors.append(f"{name}: git blob mismatch")

    if receipt.get("application_base_commit") != "4653b516349d158279a8792aa503c209ed0cecab":
        errors.append("receipt: stale application base")
    if receipt.get("framework_commit") != "43897d3afaf0038385102d5acc64793c05ec40f0":
        errors.append("receipt: framework identity mismatch")
    if receipt.get("application_authority") != PLAN_ONLY_AUTHORITY:
        errors.append("receipt: application authority is not plan-only")
    if receipt.get("review_authority") != (
        "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW"
    ):
        errors.append("receipt: same-context review boundary changed")
    expected_credit = {
        "mathematical_saturation_credit": False,
        "mathematical_result_credit": False,
        "strict_discovery_result_credit": False,
    }
    if receipt.get("credit") != expected_credit:
        errors.append("receipt: zero-credit boundary changed")
    chronology = receipt.get("chronology", {})
    for field in (
        "decoder_imported_or_executed",
        "evaluator_imported_or_executed",
        "target_enumerated",
        "target_output_accessed",
        "outcome_branch_selected",
    ):
        if chronology.get(field) is not False:
            errors.append(f"receipt: chronology {field} is not false")

    candidate = documents.get("candidate", {})
    if candidate.get("registered_branches") != BRANCHES:
        errors.append("candidate: registered branch set/order changed")
    if candidate.get("candidate_kind") != "TYPED_PLAN_ONLY_NO_TARGET_OUTPUT":
        errors.append("candidate: not a plan-only object")
    authority = candidate.get("authority", {})
    if authority.get("licensed_action_exercised") != "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY":
        errors.append("candidate: unlicensed action")
    if authority.get("generic_runtime_candidate_paths_non_authoritative") is not True:
        errors.append("candidate: generic runtime path treated as authoritative")
    if authority.get("grants_cover_or_lower_bound_conclusion") is not False:
        errors.append("candidate: cover/lower-bound authority changed")

    manifest = documents.get("evaluator_manifest", {})
    if manifest.get("status") != "FROZEN_FOR_LATER_POST_FREEZE_EXECUTION_NOT_RUN":
        errors.append("evaluator_manifest: status is not frozen/unrun")
    later_gate = manifest.get("later_execution_gate", {})
    if later_gate.get("current_task_execution_authorized") is not False:
        errors.append("evaluator_manifest: current-task execution authorized")
    if later_gate.get("post_freeze_authorization_required") is not True:
        errors.append("evaluator_manifest: post-freeze authorization not required")
    evaluator_binding = manifest.get("evaluator", {})
    evaluator_content = byte_contents.get("evaluator_source")
    if evaluator_content is not None and evaluator_binding.get("raw_sha256") != _raw_sha256(
        evaluator_content
    ):
        errors.append("evaluator_manifest: evaluator source hash mismatch")

    trace = documents.get("trace", {})
    entries = trace.get("entries")
    if not isinstance(entries, list) or len(entries) != 9:
        errors.append("trace: expected eight pre-candidate events plus one candidate-freeze event")
    else:
        event = entries[-1]
        candidate_events = [
            entry for entry in entries if entry.get("event_type") == "CANDIDATE_PROPOSED"
        ]
        if len(candidate_events) != 1:
            errors.append("trace: expected exactly one candidate proposal")
        if event.get("event_type") != "CANDIDATE_PROPOSED":
            errors.append("trace: final event is not the candidate proposal")
        if event.get("previous_event_hash") != (
            "sha256:83cb11b84072c529c9e617e448dfefaa693f04e6a6bd4ba9f737bc4aae0a3de9"
        ):
            errors.append("trace: pre-candidate chain binding mismatch")

    pre_gate = documents.get("pre_candidate_gate", {})
    if pre_gate.get("application_authority", {}).get("licensed_actions") != [
        "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"
    ]:
        errors.append("pre_candidate_gate: plan-only license changed")

    return tuple(errors)


def verify_packet(repo_root: Path | str) -> None:
    errors = audit_packet(repo_root)
    if errors:
        raise PacketIntegrityError("C045 candidate freeze failed: " + "; ".join(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[5])
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
                "candidate": "C045-U17-INCIDENCE-CLASSIFICATION-PLAN-v1",
                "licensed_action": "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY",
                "target_evaluator_execution_authorized": False,
                "target_output_accessed": False,
                "mathematical_result_credit": False,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
