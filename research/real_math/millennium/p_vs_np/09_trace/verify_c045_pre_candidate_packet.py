#!/usr/bin/env python3
"""Fail-closed full-document integrity verifier for the C045 packet.

The generic RAKL runtime hashes typed gate projections.  This application-level
verifier additionally binds every complete JSON input document used by the C045
pre-candidate gate.  It has no decoder, solver, search, or target-evaluator
capability.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable


PNP_RELATIVE = Path("research/real_math/millennium/p_vs_np")
GATE_RELATIVE = (
    PNP_RELATIVE
    / "09_trace/O9d12a2a1b_C045_LATEST_RAKL_GATE_RECEIPT_20260812.json"
)
INPUT_PATHS = {
    "atomization": PNP_RELATIVE
    / "02_problem_dag/O9d12a2a1b_C045_ATOMIZATION_20260812.json",
    "context": PNP_RELATIVE
    / "01_frontier/O9d12a2a1b_C045_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": PNP_RELATIVE
    / "07_memory/O9d12a2a1b_C045_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": PNP_RELATIVE
    / "07_memory/O9d12a2a1b_C045_FAILURE_SNAPSHOT_20260812.json",
    "memory": PNP_RELATIVE
    / "07_memory/O9d12a2a1b_C045_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": PNP_RELATIVE
    / "07_memory/O9d12a2a1b_C045_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": PNP_RELATIVE
    / "08_reviews/O9d12a2a1b_C045_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": PNP_RELATIVE
    / "08_reviews/O9d12a2a1b_C045_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": PNP_RELATIVE
    / "09_trace/O9d12a2a1b_C045_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": PNP_RELATIVE
    / "09_trace/O9d12a2a1b_C045_PRE_CANDIDATE_TRACE_20260812.json",
}


class PacketIntegrityError(RuntimeError):
    """Raised whenever the packet cannot be verified exactly."""


def _reject_duplicate_keys(pairs: Iterable[tuple[str, object]]) -> dict:
    document: dict[str, object] = {}
    for key, value in pairs:
        if key in document:
            raise ValueError(f"duplicate JSON key: {key}")
        document[key] = value
    return document


def _load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys)
    if not isinstance(value, dict):
        raise ValueError("top-level JSON value is not an object")
    return value


def canonical_document_sha256(document: object) -> str:
    encoded = json.dumps(
        document,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _gate_artifact_hash(gate: dict) -> str:
    payload = dict(gate)
    payload["artifact_hash"] = ""
    return canonical_document_sha256(payload)


def audit_packet(repo_root: Path | str) -> tuple[str, ...]:
    root = Path(repo_root).resolve()
    errors: list[str] = []
    gate_path = root / GATE_RELATIVE
    try:
        gate = _load_json(gate_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return (f"gate: cannot load canonical receipt: {exc}",)

    declared_gate_hash = gate.get("artifact_hash")
    if not isinstance(declared_gate_hash, str):
        errors.append("gate: missing artifact_hash")
    elif declared_gate_hash != _gate_artifact_hash(gate):
        errors.append("gate: artifact_hash mismatch")

    integrity = gate.get("full_document_integrity")
    if not isinstance(integrity, dict):
        return tuple(errors + ["gate: missing full_document_integrity"])
    if integrity.get("algorithm") != "SHA-256":
        errors.append("gate: unsupported full-document algorithm")
    if integrity.get("canonicalization") != "JSON_SORT_KEYS_COMPACT_UTF8":
        errors.append("gate: unsupported full-document canonicalization")
    if integrity.get("scope") != "FULL_PARSED_DOCUMENT_INCLUDING_DECLARED_RUNTIME_HASHES":
        errors.append("gate: incomplete full-document integrity scope")

    bindings = integrity.get("inputs")
    if not isinstance(bindings, dict):
        return tuple(errors + ["gate: full-document inputs are missing"])
    if set(bindings) != set(INPUT_PATHS):
        errors.append("gate: full-document input set is not exact")
    if "gate" in bindings:
        errors.append("gate: circular self-binding is forbidden")

    for name, relative_path in INPUT_PATHS.items():
        binding = bindings.get(name)
        if not isinstance(binding, dict):
            errors.append(f"{name}: missing full-document binding")
            continue
        if set(binding) != {"path", "canonical_sha256"}:
            errors.append(f"{name}: malformed full-document binding")
            continue
        expected_path = relative_path.as_posix()
        if binding.get("path") != expected_path:
            errors.append(f"{name}: bound path mismatch")
            continue
        if relative_path == GATE_RELATIVE:
            errors.append(f"{name}: circular gate binding")
            continue
        path = root / relative_path
        try:
            document = _load_json(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{name}: cannot load bound document: {exc}")
            continue
        actual = canonical_document_sha256(document)
        if binding.get("canonical_sha256") != actual:
            errors.append(f"{name}: full-document digest mismatch")

    declared_integrity_hash = gate.get("artifact_bindings", {}).get(
        "full_document_integrity_hash"
    )
    if declared_integrity_hash != canonical_document_sha256(integrity):
        errors.append("gate: full_document_integrity_hash mismatch")

    expected_authority = {
        "generic_runtime_candidate_paths_non_authoritative": True,
        "licensed_actions": ["FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"],
        "candidate_construction_authorized": False,
        "target_evaluator_execution_authorized": False,
    }
    if gate.get("application_authority") != expected_authority:
        errors.append("gate: application authority is not plan-only")
    if gate.get("gate_verdicts", {}).get("licensed_action") != (
        "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"
    ):
        errors.append("gate: unexpected licensed action")
    chronology = gate.get("chronology", {})
    if chronology.get("candidate_identity") is not None:
        errors.append("gate: candidate identity exists")
    if chronology.get("candidate_proposed") is not False:
        errors.append("gate: candidate proposal chronology is not false")
    if chronology.get("target_output_accessed") is not False:
        errors.append("gate: target output was accessed")

    authority = gate.get("authority", {})
    refresh = gate.get("refresh", {})
    for field in ("mathematical_saturation_credit", "mathematical_result_credit"):
        if authority.get(field) is not False:
            errors.append(f"gate: authority {field} is not zero")
        if refresh.get(field) is not False:
            errors.append(f"gate: refresh {field} is not zero")

    expert_path = root / INPUT_PATHS["expert_review"]
    try:
        expert = _load_json(expert_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"expert_review: cannot check review authority: {exc}")
    else:
        if expert.get("review_authority") != (
            "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW"
        ):
            errors.append("expert_review: same-context authority boundary changed")

    return tuple(errors)


def verify_packet(repo_root: Path | str) -> None:
    errors = audit_packet(repo_root)
    if errors:
        raise PacketIntegrityError("C045 packet integrity failed: " + "; ".join(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[5],
        help="RAKL_math repository root (default: inferred from this script)",
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
                "gate": GATE_RELATIVE.as_posix(),
                "verified_full_documents": sorted(INPUT_PATHS),
                "licensed_action": "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY",
                "mathematical_saturation_credit": False,
                "mathematical_result_credit": False,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
