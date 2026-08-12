#!/usr/bin/env python3
"""Capability-free integrity verifier for the C047 candidate freeze."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


BASE = Path("research/real_math/millennium/p_vs_np")
RECEIPT = BASE / "09_trace/O9d12a2a1b_C047_CANDIDATE_FREEZE_RECEIPT_20260812.json"
INPUTS = {
    "candidate": BASE / "04_candidates/O9d12a2a1b_C047_ORIENTATION_ONLY_SEPARATION_LEMMA_FREEZE_20260812.json",
    "evaluator_manifest": BASE / "05_falsification/O9d12a2a1b_C047_ORIENTATION_FEASIBILITY_EVALUATOR_FREEZE_20260812.json",
    "authorization": BASE / "09_trace/O9d12a2a1b_C047_EVALUATION_AUTHORIZATION_20260812.json",
    "trace": BASE / "09_trace/O9d12a2a1b_C047_CANDIDATE_FREEZE_TRACE_20260812.json",
    "feedback": BASE / "10_feedback/C047_COARSE_REPAIR_INTERFACE_CONGRUENCE_APPLICATION_FEEDBACK_PROPOSAL_20260812.json",
}
EVALUATOR = BASE / "05_falsification/c047_orientation_feasibility_evaluator.py"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("top-level JSON must be object")
    return value


def digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def audit_packet(root: Path) -> tuple[str, ...]:
    root = Path(root)
    errors: list[str] = []
    receipt = load(root / RECEIPT)
    subject = dict(receipt)
    subject["artifact_hash"] = ""
    if receipt.get("artifact_hash") != digest(subject):
        errors.append("receipt: artifact_hash mismatch")
    integrity = receipt.get("full_document_integrity", {})
    if receipt.get("full_document_integrity_hash") != digest(integrity):
        errors.append("receipt: integrity hash mismatch")
    json_inputs = integrity.get("json_inputs", {})
    if set(json_inputs) != set(INPUTS):
        errors.append("receipt: JSON input set mismatch")
    for name, path in INPUTS.items():
        binding = json_inputs.get(name, {})
        if binding.get("path") != path.as_posix():
            errors.append(f"{name}: path mismatch")
        elif binding.get("canonical_sha256") != digest(load(root / path)):
            errors.append(f"{name}: digest mismatch")
    evaluator_binding = integrity.get("byte_inputs", {}).get("evaluator_source", {})
    actual_evaluator = hashlib.sha256((root / EVALUATOR).read_bytes()).hexdigest()
    if evaluator_binding.get("path") != EVALUATOR.as_posix() or evaluator_binding.get("raw_sha256") != actual_evaluator:
        errors.append("evaluator: byte identity mismatch")
    authorization = load(root / INPUTS["authorization"])
    if authorization.get("current_task_evaluator_execution_authorized") is not False:
        errors.append("authorization: evaluator execution widened")
    if authorization.get("later_target_access_authorized") is not False:
        errors.append("authorization: later target access widened")
    return tuple(errors)


def verify_packet(root: Path) -> None:
    errors = audit_packet(root)
    if errors:
        raise RuntimeError("C047 candidate packet failed: " + "; ".join(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[5])
    args = parser.parse_args(argv)
    try:
        verify_packet(args.repo_root)
    except RuntimeError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps({"status": "PASS", "candidate": "C047-ORIENTATION-ONLY-SEPARATION-LEMMA-v1", "target_result_accessed": False, "evaluator_executed": False}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
