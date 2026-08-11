#!/usr/bin/env python3
"""Run and bind the O9d12a2a1a1b1 V5 pre-candidate assurance envelope.

The runner deliberately uses a two-commit/envelope boundary.  ``run`` tests an
already committed subject and writes immutable raw logs plus a self-hashed
machine receipt.  ``build-gate`` then binds those outputs into the final gate
receipt.  The gate receipt itself is not claimed to have been part of the
tested subject; the required final exact suite is run after it is created.

This is process assurance only.  It grants no theorem, proof, novelty,
P-versus-NP, independent-review, or framework-promotion authority.
"""

from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from typing import Any, Iterable, NoReturn

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
ATOM = "O9d12a2a1a1b1"
BASE_COMMIT = "c48293364c6bdf7e0c5d93f5e01d889008c9eb61"
BASE_TREE = "38c29ac6fcb19baa3a14876a2ed081456ef1e70b"
FRAMEWORK_PIN = "fe47a12c4bad8253658baaf37e1300cab15d0823"
APPLICATION_REPOSITORY = "https://github.com/SzeChunYiu/RAKL_math.git"
FRAMEWORK_REPOSITORY = "https://github.com/SzeChunYiu/RAKL.git"
PRIMARY_SOURCE_SHA256 = "3f7d98691f3ac28208df6e8669d860c45b6068781dd77c737eb1e780641fbea7"

MACHINE_SCHEMA_PATH = "schemas/pnp-o9d12a2a1a1b1-machine-run-v5.schema.json"
GATE_SCHEMA_PATH = "schemas/pnp-o9d12a2a1a1b1-pre-candidate-gate-v5.schema.json"
MACHINE_RECEIPT_PATH = "receipts/pnp-o9d12a2a1a1b1-machine-run-v5-20260811.json"
GATE_RECEIPT_PATH = "receipts/pnp-o9d12a2a1a1b1-pre-candidate-gate-v5-20260811.json"
FOCUSED_LOG_PATH = "receipts/logs/pnp-o9d12a2a1a1b1-focused-v5-20260811.log"
FULL_LOG_PATH = "receipts/logs/pnp-o9d12a2a1a1b1-full-v5-20260811.log"

FOCUSED_COMMAND = (
    "PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 PYTHONINTMAXSTRDIGITS=0 "
    "python tools/run_application_tests.py --framework framework/RAKL -- "
    "-k pnp_o9d12a2a1a1b1_pre_candidate_v5"
)
FULL_COMMAND = (
    "PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 PYTHONINTMAXSTRDIGITS=0 "
    "python tools/run_application_tests.py --framework framework/RAKL"
)
EXACT_ENVIRONMENT = {
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONNOUSERSITE": "1",
    "PYTHONINTMAXSTRDIGITS": "0",
}
MAX_FUTURE_SKEW_SECONDS = 5

# Every byte that the V5 focused test treats as an input is fixed here.  The
# order is part of both schemas; replacing an entry with a duplicate fails.
TESTED_INPUTS: tuple[tuple[str, str], ...] = (
    ("receipts/pnp-o9d12a2a1a1b1-v0-hostile-failure-20260811.json", "V0_FAILURE_CORRECTION"),
    ("receipts/pnp-o9d12a2a1a1b1-v2-hostile-failure-20260811.json", "V2_FAILURE_CORRECTION"),
    ("research/real_math/millennium/p_vs_np/02_problem_dag/O9d12a2a1a1b1_ATOMIZATION_V2_20260811.json", "ATOMIZATION"),
    ("research/real_math/millennium/p_vs_np/01_frontier/O9d12a2a1a1b1_MATH_CONTEXT_FIBER_V2_20260811.json", "MATH_CONTEXT_FIBER"),
    ("research/real_math/millennium/p_vs_np/01_frontier/O9d12a2a1a1b1_SOURCE_AND_TRANSFER_PACKET_V3_20260811.md", "SOURCE_SYNTHESIS"),
    ("research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1a1b1_TOOL_SNAPSHOT_V2_20260811.json", "TOOL_SNAPSHOT"),
    ("research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1a1b1_FAILURE_SNAPSHOT_V2_20260811.json", "FAILURE_SNAPSHOT"),
    ("research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1a1b1_NONCANONICAL_PARENT_WARNING_V2_20260811.json", "NONCANONICAL_PARENT_WARNING"),
    ("research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1a1b1_RESEARCH_MEMORY_REVIEW_V2_20260811.json", "RESEARCH_MEMORY_REVIEW"),
    ("research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1a1b1_MEMORY_FREEZE_V2_20260811.json", "MEMORY_FREEZE"),
    ("research/real_math/millennium/p_vs_np/08_reviews/SAME_CONTEXT_EXPERT_REVIEW_O9d12a2a1a1b1_PRE_CANDIDATE_V2_20260811.json", "EXPERT_CONTEXT_REVIEW"),
    ("research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1a1b1_PRE_CANDIDATE_TRACE_V3_20260811.json", "MATH_RESEARCH_TRACE"),
    ("research/real_math/millennium/p_vs_np/00_sources/ECCC_TR25_033_20250318.pdf", "PRIMARY_SOURCE_PDF"),
    ("research/real_math/millennium/p_vs_np/00_sources/ECCC_TR25_033_SOURCE_RETRIEVAL_RECEIPT_20260811.json", "SOURCE_RETRIEVAL_RECEIPT"),
    ("research/real_math/millennium/p_vs_np/01_frontier/O9d12a2a1a1b1_PROBLEM_FIBRE_V3_20260811.json", "PROBLEM_FIBRE"),
    ("research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1a1b1_PRE_ACTION_FIBRE_RECEIPT_V3_20260811.json", "PRE_ACTION_FIBRE_RECEIPT"),
    ("receipts/pnp-o9d12a2a1a1b1-pre-candidate-gate-20260811.json", "ORIGINAL_V0_GATE"),
    ("receipts/pnp-o9d12a2a1a1b1-pre-candidate-gate-v2-20260811.json", "ORIGINAL_V2_GATE"),
    ("schemas/pnp-o9d12a2a1a1b1-pre-candidate-gate.schema.json", "ORIGINAL_V0_GATE_SCHEMA"),
    ("schemas/pnp-o9d12a2a1a1b1-pre-candidate-gate-v2.schema.json", "ORIGINAL_V2_GATE_SCHEMA"),
    ("receipts/pnp-o9d12a2a1a1b1-machine-run-v3-20260811.json", "PRIOR_V3_MACHINE_RUN"),
    ("receipts/pnp-o9d12a2a1a1b1-pre-candidate-gate-v3-20260811.json", "PRIOR_V3_GATE"),
    ("schemas/pnp-o9d12a2a1a1b1-machine-run-v3.schema.json", "PRIOR_V3_MACHINE_SCHEMA"),
    ("schemas/pnp-o9d12a2a1a1b1-pre-candidate-gate-v3.schema.json", "PRIOR_V3_GATE_SCHEMA"),
    ("receipts/pnp-o9d12a2a1a1b1-v4-hostile-failure-20260811.json", "V4_FAILURE_CORRECTION"),
    ("receipts/pnp-o9d12a2a1a1b1-machine-run-v4-20260811.json", "PRIOR_V4_MACHINE_RUN"),
    ("receipts/pnp-o9d12a2a1a1b1-pre-candidate-gate-v4-20260811.json", "PRIOR_V4_GATE"),
    ("schemas/pnp-o9d12a2a1a1b1-machine-run-v4.schema.json", "PRIOR_V4_MACHINE_SCHEMA"),
    ("schemas/pnp-o9d12a2a1a1b1-pre-candidate-gate-v4.schema.json", "PRIOR_V4_GATE_SCHEMA"),
    (GATE_SCHEMA_PATH, "GATE_SCHEMA"),
    (MACHINE_SCHEMA_PATH, "MACHINE_RUN_SCHEMA"),
    ("tests/math_applications/test_pnp_o9d12a2a1a1b1_pre_candidate_v5.py", "FOCUSED_TEST"),
    ("tools/run_pnp_o9d12a2a1a1b1_pre_candidate_v5.py", "ASSURANCE_RUNNER"),
)

ENVELOPE_OUTPUTS: tuple[tuple[str, str], ...] = (
    (MACHINE_RECEIPT_PATH, "MACHINE_RUN_RECEIPT"),
    (FOCUSED_LOG_PATH, "FOCUSED_RAW_LOG"),
    (FULL_LOG_PATH, "FULL_RAW_LOG"),
)


def fail(message: str) -> NoReturn:
    raise SystemExit(message)


def load_json(path: str | Path) -> dict[str, Any]:
    absolute = Path(path)
    if not absolute.is_absolute():
        absolute = ROOT / absolute
    value = json.loads(absolute.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {absolute}")
    return value


def raw_sha256(path: str | Path) -> str:
    absolute = Path(path)
    if not absolute.is_absolute():
        absolute = ROOT / absolute
    return hashlib.sha256(absolute.read_bytes()).hexdigest()


def canonical_hash(value: dict[str, Any], field: str = "artifact_hash") -> str:
    payload = copy.deepcopy(value)
    payload[field] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def git(*arguments: str, binary: bool = False, check: bool = True) -> str | bytes:
    completed = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=not binary,
        check=False,
    )
    if check and completed.returncode != 0:
        stderr = completed.stderr if isinstance(completed.stderr, str) else completed.stderr.decode(errors="replace")
        raise RuntimeError(f"git {' '.join(arguments)} failed: {stderr.strip()}")
    if binary:
        return completed.stdout
    return completed.stdout.strip()


def _valid_oid(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value) is not None


def audit_git_state(
    source_binding: object,
    *,
    require_current_origin: bool = False,
    require_worktree_framework: bool = True,
) -> dict[str, Any]:
    """Execute the commit/tree/ancestry/gitlink relations, failing closed."""

    required = {
        "repository_url",
        "application_base_commit",
        "application_base_tree",
        "latest_main_at_freeze",
        "subject_commit",
        "subject_tree",
        "framework_repository_url",
        "framework_pin",
    }
    if not isinstance(source_binding, dict) or not required.issubset(source_binding):
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_GIT_BINDING_FIELDS"}
    oid_fields = (
        "application_base_commit",
        "application_base_tree",
        "latest_main_at_freeze",
        "subject_commit",
        "subject_tree",
        "framework_pin",
    )
    if any(not _valid_oid(source_binding.get(field)) for field in oid_fields):
        return {"verdict": "FAIL", "reason": "MALFORMED_GIT_OID"}
    if source_binding["repository_url"] != APPLICATION_REPOSITORY:
        return {"verdict": "FAIL", "reason": "APPLICATION_REPOSITORY_MISMATCH"}
    if source_binding["framework_repository_url"] != FRAMEWORK_REPOSITORY:
        return {"verdict": "FAIL", "reason": "FRAMEWORK_REPOSITORY_MISMATCH"}
    if source_binding["application_base_commit"] != BASE_COMMIT:
        return {"verdict": "FAIL", "reason": "APPLICATION_BASE_MISMATCH"}
    if source_binding["application_base_tree"] != BASE_TREE:
        return {"verdict": "FAIL", "reason": "APPLICATION_BASE_TREE_DECLARATION_MISMATCH"}
    if source_binding["latest_main_at_freeze"] != BASE_COMMIT:
        return {"verdict": "FAIL", "reason": "LATEST_MAIN_AT_FREEZE_MISMATCH"}
    if source_binding["framework_pin"] != FRAMEWORK_PIN:
        return {"verdict": "FAIL", "reason": "FRAMEWORK_PIN_MISMATCH"}

    try:
        base_tree = git("rev-parse", f"{BASE_COMMIT}^{{tree}}")
        subject_tree = git("rev-parse", f"{source_binding['subject_commit']}^{{tree}}")
        base_gitlink = git("rev-parse", f"{BASE_COMMIT}:framework/RAKL")
        subject_gitlink = git("rev-parse", f"{source_binding['subject_commit']}:framework/RAKL")
        pin_config = load_json("config/rakl-framework-pin.json")["commit"]
        origin_url = git("remote", "get-url", "origin")
    except (KeyError, OSError, RuntimeError, ValueError):
        return {"verdict": "CANNOT_CHECK", "reason": "GIT_OBJECT_OR_CONFIG_UNAVAILABLE"}
    if base_tree != BASE_TREE:
        return {"verdict": "FAIL", "reason": "EXECUTED_BASE_TREE_MISMATCH"}
    if subject_tree != source_binding["subject_tree"]:
        return {"verdict": "FAIL", "reason": "EXECUTED_SUBJECT_TREE_MISMATCH"}
    ancestor = subprocess.run(
        ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", BASE_COMMIT, source_binding["subject_commit"]],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0
    if not ancestor:
        return {"verdict": "FAIL", "reason": "BASE_NOT_ANCESTOR_OF_SUBJECT"}
    if base_gitlink != FRAMEWORK_PIN:
        return {"verdict": "FAIL", "reason": "BASE_FRAMEWORK_GITLINK_MISMATCH"}
    if subject_gitlink != FRAMEWORK_PIN:
        return {"verdict": "FAIL", "reason": "SUBJECT_FRAMEWORK_GITLINK_MISMATCH"}
    if pin_config != FRAMEWORK_PIN:
        return {"verdict": "FAIL", "reason": "PIN_CONFIG_MISMATCH"}
    if origin_url != APPLICATION_REPOSITORY:
        return {"verdict": "FAIL", "reason": "ORIGIN_URL_MISMATCH"}
    if require_current_origin:
        try:
            if git("rev-parse", "refs/remotes/origin/main") != BASE_COMMIT:
                return {"verdict": "FAIL", "reason": "ORIGIN_MAIN_MOVED_BEFORE_FREEZE"}
        except RuntimeError:
            return {"verdict": "CANNOT_CHECK", "reason": "ORIGIN_MAIN_REF_UNAVAILABLE"}
    if require_worktree_framework:
        try:
            framework_head = subprocess.run(
                ["git", "-C", str(ROOT / "framework/RAKL"), "rev-parse", "HEAD"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )
            if framework_head.returncode != 0:
                return {"verdict": "CANNOT_CHECK", "reason": "FRAMEWORK_WORKTREE_UNAVAILABLE"}
            if framework_head.stdout.strip() != FRAMEWORK_PIN:
                return {"verdict": "FAIL", "reason": "FRAMEWORK_WORKTREE_HEAD_MISMATCH"}
        except OSError:
            return {"verdict": "CANNOT_CHECK", "reason": "FRAMEWORK_WORKTREE_UNAVAILABLE"}
    return {
        "verdict": "PASS",
        "checked_relations": 12,
        "current_origin_main_at_freeze": bool(require_current_origin),
        "worktree_framework_head_checked": bool(require_worktree_framework),
    }


def source_binding_for(subject_commit: str, *, freeze_audit: bool) -> dict[str, Any]:
    subject_tree = str(git("rev-parse", f"{subject_commit}^{{tree}}"))
    binding: dict[str, Any] = {
        "repository_url": APPLICATION_REPOSITORY,
        "application_base_commit": BASE_COMMIT,
        "application_base_tree": BASE_TREE,
        "latest_main_at_freeze": BASE_COMMIT,
        "subject_commit": subject_commit,
        "subject_tree": subject_tree,
        "framework_repository_url": FRAMEWORK_REPOSITORY,
        "framework_pin": FRAMEWORK_PIN,
    }
    audit = audit_git_state(binding, require_current_origin=freeze_audit)
    if audit.get("verdict") != "PASS":
        fail(f"git audit did not pass: {audit}")
    binding["git_audit"] = audit
    return binding


def _committed_binding(subject_commit: str, path: str, kind: str) -> dict[str, Any]:
    absolute = ROOT / path
    if not absolute.is_file():
        fail(f"tested input missing: {path}")
    try:
        committed = git("show", f"{subject_commit}:{path}", binary=True)
        blob = str(git("rev-parse", f"{subject_commit}:{path}"))
    except RuntimeError as exc:
        fail(str(exc))
    current = absolute.read_bytes()
    if committed != current:
        fail(f"worktree bytes differ from tested subject commit: {path}")
    return {
        "path": path,
        "kind": kind,
        "commit": subject_commit,
        "git_blob_sha": blob,
        "raw_sha256": hashlib.sha256(current).hexdigest(),
        "size_bytes": len(current),
    }


def audit_input_bindings(receipt: object) -> dict[str, Any]:
    if not isinstance(receipt, dict):
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_MACHINE_RECEIPT"}
    source = receipt.get("source_binding")
    bindings = receipt.get("input_bindings")
    if not isinstance(source, dict) or not isinstance(bindings, list):
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_INPUT_BINDING_FIELDS"}
    subject = source.get("subject_commit")
    if not _valid_oid(subject) or len(bindings) != len(TESTED_INPUTS):
        return {"verdict": "FAIL", "reason": "MALFORMED_INPUT_BINDING_SET"}
    for binding, (path, kind) in zip(bindings, TESTED_INPUTS):
        if not isinstance(binding, dict):
            return {"verdict": "FAIL", "reason": "MALFORMED_INPUT_BINDING"}
        required = {"path", "kind", "commit", "git_blob_sha", "raw_sha256", "size_bytes"}
        if not required.issubset(binding):
            return {"verdict": "CANNOT_CHECK", "reason": "MISSING_INPUT_BINDING_FIELDS"}
        if binding["path"] != path or binding["kind"] != kind or binding["commit"] != subject:
            return {"verdict": "FAIL", "reason": "INPUT_PATH_KIND_OR_COMMIT_MISMATCH"}
        if not _valid_oid(binding["git_blob_sha"]):
            return {"verdict": "FAIL", "reason": "MALFORMED_INPUT_GIT_BLOB"}
        raw_hash = binding["raw_sha256"]
        if not isinstance(raw_hash, str) or re.fullmatch(r"[0-9a-f]{64}", raw_hash) is None:
            return {"verdict": "FAIL", "reason": "MALFORMED_INPUT_RAW_SHA256"}
        absolute = ROOT / path
        if not absolute.is_file():
            return {"verdict": "CANNOT_CHECK", "reason": "INPUT_FILE_UNAVAILABLE"}
        try:
            committed = git("show", f"{subject}:{path}", binary=True)
            blob = git("rev-parse", f"{subject}:{path}")
        except RuntimeError:
            return {"verdict": "CANNOT_CHECK", "reason": "INPUT_GIT_OBJECT_UNAVAILABLE"}
        current = absolute.read_bytes()
        if committed != current or hashlib.sha256(current).hexdigest() != raw_hash:
            return {"verdict": "FAIL", "reason": "INPUT_RAW_BYTES_MISMATCH"}
        if blob != binding["git_blob_sha"] or len(current) != binding["size_bytes"]:
            return {"verdict": "FAIL", "reason": "INPUT_BLOB_OR_SIZE_MISMATCH"}
    return {"verdict": "PASS", "checked_bindings": len(TESTED_INPUTS)}


def _parse_pytest_counts(output: str) -> tuple[int, int, int]:
    summaries = re.findall(r"(?:^|\n)=*\s*([^\n]*?(?:passed|failed)[^\n]*?)\s*=*(?:\n|$)", output)
    summary = summaries[-1] if summaries else output.splitlines()[-1] if output.splitlines() else ""
    def count(label: str) -> int:
        match = re.search(rf"(\d+)\s+{label}", summary)
        return int(match.group(1)) if match else 0
    return count("passed"), count("failed"), count("skipped")


def execution_argv(command: str) -> list[str]:
    """Execute the receipt-bound environment prefix as shell syntax, not argv[0]."""
    if not command or "\n" in command or "\r" in command:
        fail("run command is empty or multiline")
    return ["/bin/sh", "-c", command]


def _run_and_log(scope: str, command: str, log_path: str, *, execution_root: Path) -> dict[str, Any]:
    started_at = utc_now()
    started = time.monotonic()
    environment = os.environ.copy()
    environment.update(EXACT_ENVIRONMENT)
    completed = subprocess.run(
        execution_argv(command),
        cwd=execution_root,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    duration = round(time.monotonic() - started, 6)
    ended_at = utc_now()
    raw = completed.stdout.encode("utf-8")
    absolute = ROOT / log_path
    absolute.parent.mkdir(parents=True, exist_ok=True)
    absolute.write_bytes(raw)
    passed, failed_count, skipped = _parse_pytest_counts(completed.stdout)
    if completed.returncode != 0 or failed_count != 0 or passed < 1:
        fail(f"{scope} failed; inspect {log_path}")
    return {
        "scope": scope,
        "command": command,
        "environment": dict(EXACT_ENVIRONMENT),
        "started_at": started_at,
        "ended_at": ended_at,
        "duration_seconds": duration,
        "exit_code": completed.returncode,
        "result": "PASS",
        "passed": passed,
        "failed": failed_count,
        "skipped": skipped,
        "log_path": log_path,
        "log_sha256": hashlib.sha256(raw).hexdigest(),
        "log_size_bytes": len(raw),
    }


def _require_clean_subject_checkout(subject_commit: str) -> None:
    if git("rev-parse", "HEAD") != subject_commit:
        fail("current HEAD does not equal --subject-commit")
    if git("status", "--porcelain", "--untracked-files=all"):
        fail("current subject worktree is not clean")


def _prepare_isolated_subject(subject_commit: str, execution_root: Path) -> None:
    added = subprocess.run(
        ["git", "-C", str(ROOT), "worktree", "add", "--detach", str(execution_root), subject_commit],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False,
    )
    if added.returncode != 0:
        fail(f"could not create isolated subject worktree: {added.stderr.strip()}")
    submodule = subprocess.run(
        ["git", "-C", str(execution_root), "submodule", "update", "--init", "framework/RAKL"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False,
    )
    if submodule.returncode != 0:
        fail(f"could not initialize isolated framework pin: {submodule.stderr.strip()}")
    if subprocess.run(
        ["git", "-C", str(execution_root), "rev-parse", "HEAD"],
        stdout=subprocess.PIPE, text=True, check=False,
    ).stdout.strip() != subject_commit:
        fail("isolated execution HEAD mismatch")
    status = subprocess.run(
        ["git", "-C", str(execution_root), "status", "--porcelain", "--untracked-files=all"],
        stdout=subprocess.PIPE, text=True, check=False,
    )
    if status.returncode != 0 or status.stdout.strip():
        fail("isolated execution worktree is not clean")


def _timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def audit_machine_semantics(receipt: object) -> dict[str, Any]:
    """Recompute the exact run/log/chronology contract from receipt-bound bytes."""

    if not isinstance(receipt, dict):
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_MACHINE_RECEIPT"}
    runs = receipt.get("runs")
    if not isinstance(runs, list) or len(runs) != 2:
        return {"verdict": "FAIL", "reason": "INCOMPLETE_RUN_SET"}
    expected = (
        ("FOCUSED_V5_GATE_PRE_RECEIPT", FOCUSED_COMMAND, FOCUSED_LOG_PATH),
        ("EXACT_APPLICATION_SUITE_PRE_RECEIPT", FULL_COMMAND, FULL_LOG_PATH),
    )
    recorded = _timestamp(receipt.get("recorded_at"))
    if recorded is None:
        return {"verdict": "FAIL", "reason": "MALFORMED_MACHINE_TIMESTAMP"}
    now = datetime.now(timezone.utc)
    if (recorded - now).total_seconds() > MAX_FUTURE_SKEW_SECONDS:
        return {"verdict": "FAIL", "reason": "MACHINE_TIMESTAMP_IN_FUTURE"}
    source = receipt.get("source_binding")
    git_audit = source.get("git_audit") if isinstance(source, dict) else None
    required_execution_facts = {
        "subject_checkout_head_checked": True,
        "subject_checkout_clean_checked": True,
        "isolated_detached_execution": True,
    }
    if not isinstance(git_audit, dict) or any(git_audit.get(key) is not value for key, value in required_execution_facts.items()):
        return {"verdict": "FAIL", "reason": "SUBJECT_EXECUTION_PROVENANCE_MISSING"}
    counts: list[dict[str, int]] = []
    previous_end: datetime | None = None
    for run, (scope, command, log_path) in zip(runs, expected):
        if not isinstance(run, dict):
            return {"verdict": "FAIL", "reason": "MALFORMED_RUN"}
        if (run.get("scope"), run.get("command"), run.get("log_path")) != (scope, command, log_path):
            return {"verdict": "FAIL", "reason": "RUN_IDENTITY_MISMATCH"}
        if run.get("environment") != EXACT_ENVIRONMENT:
            return {"verdict": "FAIL", "reason": "RUN_ENVIRONMENT_MISMATCH"}
        if run.get("result") != "PASS" or run.get("exit_code") != 0 or run.get("failed") != 0:
            return {"verdict": "FAIL", "reason": "RUN_DID_NOT_PASS"}
        started, ended = _timestamp(run.get("started_at")), _timestamp(run.get("ended_at"))
        if started is None or ended is None or not (started <= ended <= recorded):
            return {"verdict": "FAIL", "reason": "IMPOSSIBLE_RUN_CHRONOLOGY"}
        if previous_end is not None and previous_end > started:
            return {"verdict": "FAIL", "reason": "RUN_SEQUENCE_OVERLAP_OR_REVERSAL"}
        previous_end = ended
        absolute = ROOT / log_path
        if not absolute.is_file():
            return {"verdict": "CANNOT_CHECK", "reason": "RUN_LOG_UNAVAILABLE"}
        raw = absolute.read_bytes()
        if hashlib.sha256(raw).hexdigest() != run.get("log_sha256") or len(raw) != run.get("log_size_bytes"):
            return {"verdict": "FAIL", "reason": "RUN_LOG_BINDING_MISMATCH"}
        passed, failed_count, skipped = _parse_pytest_counts(raw.decode("utf-8"))
        if (passed, failed_count, skipped) != (run.get("passed"), run.get("failed"), run.get("skipped")):
            return {"verdict": "FAIL", "reason": "RUN_COUNT_MISMATCH"}
        if passed < 1:
            return {"verdict": "FAIL", "reason": "EMPTY_RUN"}
        counts.append({"passed": passed, "failed": failed_count, "skipped": skipped})
    if receipt.get("all_required_runs_passed") is not True:
        return {"verdict": "FAIL", "reason": "RUN_COMPLETENESS_FLAG_FALSE"}
    authority = receipt.get("authority_contract")
    if not isinstance(authority, dict) or not authority or any(value is not False for value in authority.values()):
        return {"verdict": "FAIL", "reason": "MACHINE_AUTHORITY_ESCALATION"}
    return {"verdict": "PASS", "checked_runs": 2, "counts": counts}


def validate_document(document: dict[str, Any], schema_path: str) -> None:
    schema = load_json(schema_path)
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(document)


def write_json(path: str, value: dict[str, Any]) -> None:
    absolute = ROOT / path
    absolute.parent.mkdir(parents=True, exist_ok=True)
    temporary = absolute.with_suffix(absolute.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(absolute)


def build_machine_receipt(subject_commit: str) -> dict[str, Any]:
    _require_clean_subject_checkout(subject_commit)
    source_binding = source_binding_for(subject_commit, freeze_audit=True)
    source_binding["git_audit"].update({
        "subject_checkout_head_checked": True,
        "subject_checkout_clean_checked": True,
        "isolated_detached_execution": True,
    })
    inputs = [_committed_binding(subject_commit, path, kind) for path, kind in TESTED_INPUTS]
    with tempfile.TemporaryDirectory(prefix="rakl-math-pnp-v5-") as temporary:
        execution_root = Path(temporary) / "subject"
        try:
            _prepare_isolated_subject(subject_commit, execution_root)
            focused = _run_and_log("FOCUSED_V5_GATE_PRE_RECEIPT", FOCUSED_COMMAND, FOCUSED_LOG_PATH, execution_root=execution_root)
            full = _run_and_log("EXACT_APPLICATION_SUITE_PRE_RECEIPT", FULL_COMMAND, FULL_LOG_PATH, execution_root=execution_root)
            final_status = subprocess.run(
                ["git", "-C", str(execution_root), "status", "--porcelain", "--untracked-files=all"],
                stdout=subprocess.PIPE, text=True, check=False,
            )
            if final_status.returncode != 0 or final_status.stdout.strip():
                fail("isolated subject worktree became dirty during execution")
        finally:
            subprocess.run(
                ["git", "-C", str(ROOT), "worktree", "remove", "--force", str(execution_root)],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
            )
    receipt: dict[str, Any] = {
        "schema_version": "rakl-math-pnp-machine-run-v5",
        "receipt_id": "RAKL-MATH-PNP-O9d12a2a1a1b1-MACHINE-RUN-V5-20260811",
        "atom_id": ATOM,
        "recorded_at": utc_now(),
        "source_binding": source_binding,
        "input_bindings": inputs,
        "runs": [focused, full],
        "all_required_runs_passed": True,
        "authority_contract": {
            "mathematical_result": False,
            "proof_authority": False,
            "novelty_authority": False,
            "independent_peer_review": False,
            "p_vs_np_authority": False,
            "framework_promotion_authority": False,
        },
        "artifact_hash": "",
    }
    receipt["artifact_hash"] = canonical_hash(receipt)
    validate_document(receipt, MACHINE_SCHEMA_PATH)
    if audit_input_bindings(receipt).get("verdict") != "PASS":
        fail("generated machine input bindings did not pass executable audit")
    machine_audit = audit_machine_semantics(receipt)
    if machine_audit.get("verdict") != "PASS":
        fail(f"generated machine semantics did not pass executable audit: {machine_audit}")
    return receipt


def _raw_artifact(path: str, kind: str) -> dict[str, Any]:
    absolute = ROOT / path
    if not absolute.is_file():
        fail(f"gate artifact missing: {path}")
    raw = absolute.read_bytes()
    return {
        "path": path,
        "kind": kind,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
    }


def _canonical_unprefixed(document: dict[str, Any], hash_field: str) -> str:
    payload = copy.deepcopy(document)
    payload.pop(hash_field, None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def audit_historical_supersession() -> dict[str, Any]:
    """Validate the rejected gates, their schemas, corrections, and nested raw bindings."""

    try:
        v0_failure = load_json(TESTED_INPUTS[0][0])
        v2_failure = load_json(TESTED_INPUTS[1][0])
        v0_gate = load_json(TESTED_INPUTS[16][0])
        v2_gate = load_json(TESTED_INPUTS[17][0])
        v3_machine = load_json(TESTED_INPUTS[20][0])
        v3_gate = load_json(TESTED_INPUTS[21][0])
        v4_failure = load_json(TESTED_INPUTS[24][0])
        v4_machine = load_json(TESTED_INPUTS[25][0])
        v4_gate = load_json(TESTED_INPUTS[26][0])
        validate_document(v0_gate, TESTED_INPUTS[18][0])
        validate_document(v2_gate, TESTED_INPUTS[19][0])
        validate_document(v3_machine, TESTED_INPUTS[22][0])
        validate_document(v3_gate, TESTED_INPUTS[23][0])
        validate_document(v4_machine, TESTED_INPUTS[27][0])
        validate_document(v4_gate, TESTED_INPUTS[28][0])
    except (KeyError, OSError, ValueError, jsonschema.ValidationError, jsonschema.SchemaError):
        return {"verdict": "CANNOT_CHECK", "reason": "HISTORICAL_ARTIFACT_OR_SCHEMA_UNAVAILABLE"}
    documents = (v0_failure, v2_failure, v0_gate, v2_gate, v3_machine, v3_gate, v4_failure, v4_machine, v4_gate)
    if any(document.get("artifact_hash") != canonical_hash(document) for document in documents):
        return {"verdict": "FAIL", "reason": "HISTORICAL_SELF_HASH_MISMATCH"}

    def nested_hash(document: dict[str, Any], field: str, path: str) -> object:
        rows = document.get(field)
        if not isinstance(rows, list):
            return None
        matches = [row.get("raw_sha256") for row in rows if isinstance(row, dict) and row.get("path") == path]
        return matches[0] if len(matches) == 1 else None

    v0_path, v2_path = TESTED_INPUTS[16][0], TESTED_INPUTS[17][0]
    if nested_hash(v0_failure, "failed_packet_bindings", v0_path) != raw_sha256(v0_path):
        return {"verdict": "FAIL", "reason": "V0_CORRECTION_ORIGINAL_RAW_MISMATCH"}
    if nested_hash(v2_failure, "v2_bindings", v2_path) != raw_sha256(v2_path):
        return {"verdict": "FAIL", "reason": "V2_CORRECTION_ORIGINAL_RAW_MISMATCH"}
    v3_source = v3_machine.get("source_binding")
    v3_inputs = v3_machine.get("input_bindings")
    if not isinstance(v3_source, dict) or not _valid_oid(v3_source.get("subject_commit")) or not isinstance(v3_inputs, list):
        return {"verdict": "FAIL", "reason": "V3_HISTORICAL_BINDING_SET_MALFORMED"}
    v3_subject = v3_source["subject_commit"]
    for binding in v3_inputs:
        if not isinstance(binding, dict) or not isinstance(binding.get("path"), str):
            return {"verdict": "FAIL", "reason": "V3_HISTORICAL_INPUT_MALFORMED"}
        try:
            raw = git("show", f"{v3_subject}:{binding['path']}", binary=True)
            blob = git("rev-parse", f"{v3_subject}:{binding['path']}")
        except RuntimeError:
            return {"verdict": "CANNOT_CHECK", "reason": "V3_HISTORICAL_GIT_OBJECT_UNAVAILABLE"}
        assert isinstance(raw, bytes)
        if (
            binding.get("commit") != v3_subject
            or binding.get("git_blob_sha") != blob
            or binding.get("raw_sha256") != hashlib.sha256(raw).hexdigest()
            or binding.get("size_bytes") != len(raw)
        ):
            return {"verdict": "FAIL", "reason": "V3_HISTORICAL_INPUT_BINDING_MISMATCH"}
    v3_machine_path = TESTED_INPUTS[20][0]
    v3_machine_run = v3_gate.get("machine_run")
    if not isinstance(v3_machine_run, dict):
        return {"verdict": "FAIL", "reason": "V3_GATE_MACHINE_BINDING_MISSING"}
    if (
        v3_machine_run.get("raw_sha256") != raw_sha256(v3_machine_path)
        or v3_machine_run.get("artifact_hash") != v3_machine.get("artifact_hash")
    ):
        return {"verdict": "FAIL", "reason": "V3_GATE_MACHINE_BINDING_MISMATCH"}
    for log_key, hash_key in (("focused_log_path", "focused_log_sha256"), ("full_log_path", "full_log_sha256")):
        log_path = v3_machine_run.get(log_key)
        if not isinstance(log_path, str) or not (ROOT / log_path).is_file() or v3_machine_run.get(hash_key) != raw_sha256(log_path):
            return {"verdict": "FAIL", "reason": "V3_GATE_LOG_BINDING_MISMATCH"}
    if v4_failure.get("v4_status") != "REJECTED_ASSURANCE_ENVELOPE_PROVENANCE_AND_CHRONOLOGY":
        return {"verdict": "FAIL", "reason": "V4_FAILURE_STATUS_MISMATCH"}
    v4_rows = v4_failure.get("v4_bindings")
    if not isinstance(v4_rows, list) or len(v4_rows) != 2:
        return {"verdict": "FAIL", "reason": "V4_FAILURE_BINDINGS_MISSING"}
    for row, document_index, document in zip(v4_rows, (25, 26), (v4_machine, v4_gate)):
        path = TESTED_INPUTS[document_index][0]
        if (
            not isinstance(row, dict)
            or row.get("path") != path
            or row.get("raw_sha256") != raw_sha256(path)
            or row.get("artifact_hash") != document.get("artifact_hash")
        ):
            return {"verdict": "FAIL", "reason": "V4_FAILURE_NESTED_BINDING_MISMATCH"}
    return {
        "verdict": "PASS",
        "v0_original_raw_sha256": raw_sha256(v0_path),
        "v0_original_artifact_hash": v0_gate["artifact_hash"],
        "v2_original_raw_sha256": raw_sha256(v2_path),
        "v2_original_artifact_hash": v2_gate["artifact_hash"],
        "v3_machine_raw_sha256": raw_sha256(TESTED_INPUTS[20][0]),
        "v3_machine_artifact_hash": v3_machine["artifact_hash"],
        "v3_gate_raw_sha256": raw_sha256(TESTED_INPUTS[21][0]),
        "v3_gate_artifact_hash": v3_gate["artifact_hash"],
        "v4_failure_raw_sha256": raw_sha256(TESTED_INPUTS[24][0]),
        "v4_failure_artifact_hash": v4_failure["artifact_hash"],
        "v4_machine_raw_sha256": raw_sha256(TESTED_INPUTS[25][0]),
        "v4_machine_artifact_hash": v4_machine["artifact_hash"],
        "v4_gate_raw_sha256": raw_sha256(TESTED_INPUTS[26][0]),
        "v4_gate_artifact_hash": v4_gate["artifact_hash"],
        "checked_documents": 9,
        "checked_schemas": 6,
        "checked_v3_historical_inputs": len(v3_inputs),
    }


def audit_gate_bindings(gate: object, machine: object) -> dict[str, Any]:
    """Cross-bind every semantically load-bearing V5 gate field to executable bytes."""

    if not isinstance(gate, dict) or not isinstance(machine, dict):
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_GATE_OR_MACHINE"}
    if gate.get("source_binding") != machine.get("source_binding"):
        return {"verdict": "FAIL", "reason": "GATE_MACHINE_SOURCE_BINDING_MISMATCH"}
    if audit_git_state(gate.get("source_binding"), require_current_origin=False).get("verdict") != "PASS":
        return {"verdict": "FAIL", "reason": "GATE_GIT_BINDING_MISMATCH"}
    machine_time, gate_time = _timestamp(machine.get("recorded_at")), _timestamp(gate.get("recorded_at"))
    if machine_time is None or gate_time is None or gate_time < machine_time:
        return {"verdict": "FAIL", "reason": "IMPOSSIBLE_GATE_CHRONOLOGY"}
    if (gate_time - datetime.now(timezone.utc)).total_seconds() > MAX_FUTURE_SKEW_SECONDS:
        return {"verdict": "FAIL", "reason": "GATE_TIMESTAMP_IN_FUTURE"}
    machine_audit = audit_machine_semantics(machine)
    if machine_audit.get("verdict") != "PASS":
        return {"verdict": "FAIL", "reason": "MACHINE_SEMANTICS_NOT_PASS", "machine": machine_audit}

    expected_pairs = TESTED_INPUTS + ENVELOPE_OUTPUTS
    artifacts = gate.get("artifacts")
    if not isinstance(artifacts, list) or len(artifacts) != len(expected_pairs):
        return {"verdict": "FAIL", "reason": "GATE_ARTIFACT_SET_MISMATCH"}
    for item, (path, kind) in zip(artifacts, expected_pairs):
        if not isinstance(item, dict) or item.get("path") != path or item.get("kind") != kind:
            return {"verdict": "FAIL", "reason": "GATE_ARTIFACT_IDENTITY_MISMATCH"}
        absolute = ROOT / path
        if not absolute.is_file():
            return {"verdict": "CANNOT_CHECK", "reason": "GATE_ARTIFACT_UNAVAILABLE"}
        raw = absolute.read_bytes()
        if item.get("raw_sha256") != hashlib.sha256(raw).hexdigest() or item.get("size_bytes") != len(raw):
            return {"verdict": "FAIL", "reason": "GATE_ARTIFACT_RAW_BINDING_MISMATCH"}

    history = audit_historical_supersession()
    if history.get("verdict") != "PASS":
        return history
    v0_failure, v2_failure = load_json(TESTED_INPUTS[0][0]), load_json(TESTED_INPUTS[1][0])
    expected_supersession = {
        "v0_status": "REJECTED_PRE_CANDIDATE_AUTHORIZATION",
        "v0_correction_path": TESTED_INPUTS[0][0],
        "v0_correction_hash": v0_failure["artifact_hash"],
        "original_v0_gate_path": TESTED_INPUTS[16][0],
        "original_v0_gate_raw_sha256": history["v0_original_raw_sha256"],
        "original_v0_gate_artifact_hash": history["v0_original_artifact_hash"],
        "v2_status": "REJECTED_PRE_CANDIDATE_AUTHORIZATION",
        "v2_correction_path": TESTED_INPUTS[1][0],
        "v2_correction_hash": v2_failure["artifact_hash"],
        "original_v2_gate_path": TESTED_INPUTS[17][0],
        "original_v2_gate_raw_sha256": history["v2_original_raw_sha256"],
        "original_v2_gate_artifact_hash": history["v2_original_artifact_hash"],
        "v3_status": "HISTORICAL_PASS_AT_OWN_FREEZE_SUPERSEDED_FOR_CURRENT_MAIN",
        "prior_v3_machine_path": TESTED_INPUTS[20][0],
        "prior_v3_machine_raw_sha256": history["v3_machine_raw_sha256"],
        "prior_v3_machine_artifact_hash": history["v3_machine_artifact_hash"],
        "prior_v3_gate_path": TESTED_INPUTS[21][0],
        "prior_v3_gate_raw_sha256": history["v3_gate_raw_sha256"],
        "prior_v3_gate_artifact_hash": history["v3_gate_artifact_hash"],
        "v4_status": "REJECTED_ASSURANCE_ENVELOPE_PROVENANCE_AND_CHRONOLOGY",
        "v4_failure_path": TESTED_INPUTS[24][0],
        "v4_failure_raw_sha256": history["v4_failure_raw_sha256"],
        "v4_failure_artifact_hash": history["v4_failure_artifact_hash"],
        "prior_v4_machine_path": TESTED_INPUTS[25][0],
        "prior_v4_machine_raw_sha256": history["v4_machine_raw_sha256"],
        "prior_v4_machine_artifact_hash": history["v4_machine_artifact_hash"],
        "prior_v4_gate_path": TESTED_INPUTS[26][0],
        "prior_v4_gate_raw_sha256": history["v4_gate_raw_sha256"],
        "prior_v4_gate_artifact_hash": history["v4_gate_artifact_hash"],
        "historical_bytes_modified": False,
    }
    if gate.get("supersession") != expected_supersession:
        return {"verdict": "FAIL", "reason": "SUPERSESSION_BINDING_MISMATCH"}

    context, memory = load_json(TESTED_INPUTS[3][0]), load_json(TESTED_INPUTS[8][0])
    expert, trace = load_json(TESTED_INPUTS[10][0]), load_json(TESTED_INPUTS[11][0])
    fibre, pre_action = load_json(TESTED_INPUTS[14][0]), load_json(TESTED_INPUTS[15][0])
    if pre_action.get("receipt_canonical_sha256") != _canonical_unprefixed(pre_action, "receipt_canonical_sha256"):
        return {"verdict": "FAIL", "reason": "PRE_ACTION_CANONICAL_HASH_MISMATCH"}
    runtime = gate.get("runtime_gate")
    if not isinstance(runtime, dict):
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_RUNTIME_GATE"}
    scalar_expectations = {
        "context_packet_hash": context.get("packet_hash"),
        "memory_review_hash": memory.get("artifact_hash"),
        "expert_review_hash": expert.get("artifact_hash"),
        "trace_terminal_hash": trace.get("entries", [{}])[-1].get("artifact_hash"),
    }
    if any(runtime.get(key) != value for key, value in scalar_expectations.items()):
        return {"verdict": "FAIL", "reason": "RUNTIME_HASH_BINDING_MISMATCH"}
    expected_pass = {"verdict": "PASS", "reasons": ["runtime_reconstructed_in_focused_v5_test"]}
    if any(runtime.get(key) != expected_pass for key in ("context_gate", "memory_gate", "trace_gate")):
        return {"verdict": "FAIL", "reason": "RUNTIME_GATE_VERDICT_MISMATCH"}
    expected_plan = {"candidate_generation_allowed": True, "pre_candidate_actions": [], "candidate_paths_used": False, "candidate_identity": None}
    if runtime.get("plan_math_research") != expected_plan:
        return {"verdict": "FAIL", "reason": "PLAN_BINDING_MISMATCH"}
    if runtime.get("problem_fibre") != {"path": TESTED_INPUTS[14][0], "snapshot_hash": fibre.get("snapshot_hash"), "authority": "PROPOSAL_ONLY_RETRIEVAL_VIEW"}:
        return {"verdict": "FAIL", "reason": "PROBLEM_FIBRE_BINDING_MISMATCH"}
    if runtime.get("pre_action_fibre_receipt") != {
        "path": TESTED_INPUTS[15][0], "receipt_canonical_sha256": pre_action.get("receipt_canonical_sha256"),
        "action_executed": False, "authority": "PROPOSAL_ONLY_PROCESS_TELEMETRY",
    }:
        return {"verdict": "FAIL", "reason": "PRE_ACTION_BINDING_MISMATCH"}

    expected_machine = {
        "path": MACHINE_RECEIPT_PATH,
        "raw_sha256": raw_sha256(MACHINE_RECEIPT_PATH),
        "artifact_hash": machine.get("artifact_hash"),
        "focused_log_path": FOCUSED_LOG_PATH,
        "focused_log_sha256": raw_sha256(FOCUSED_LOG_PATH),
        "full_log_path": FULL_LOG_PATH,
        "full_log_sha256": raw_sha256(FULL_LOG_PATH),
        "all_required_runs_passed": True,
    }
    if gate.get("machine_run") != expected_machine:
        return {"verdict": "FAIL", "reason": "MACHINE_ENVELOPE_BINDING_MISMATCH"}
    primary = gate.get("primary_source_binding")
    if primary != {"path": TESTED_INPUTS[12][0], "url": "https://eccc.weizmann.ac.il/report/2025/033/download/", "raw_sha256": PRIMARY_SOURCE_SHA256, "retrieval_receipt_path": TESTED_INPUTS[13][0]}:
        return {"verdict": "FAIL", "reason": "PRIMARY_SOURCE_BINDING_MISMATCH"}
    authority = gate.get("authority_contract")
    if not isinstance(authority, dict) or not authority or any(value is not False for value in authority.values()):
        return {"verdict": "FAIL", "reason": "GATE_AUTHORITY_ESCALATION"}
    if gate.get("status") != "PROSPECTIVE_PROCESS_GATES_PASS_PRE_ACTION_FIBRE_FROZEN_NO_MATHEMATICAL_CANDIDATE":
        return {"verdict": "FAIL", "reason": "GATE_STATUS_MISMATCH"}
    if gate.get("next_action") != "SOURCE_NATIVE_T_RULE_THEOREM_INVENTORY_IN_A_SEPARATE_VERSIONED_ROUND":
        return {"verdict": "FAIL", "reason": "NEXT_ACTION_MISMATCH"}
    return {"verdict": "PASS", "checked_artifacts": len(expected_pairs), "historical": history, "machine": machine_audit}


def build_gate_receipt() -> dict[str, Any]:
    machine = load_json(MACHINE_RECEIPT_PATH)
    validate_document(machine, MACHINE_SCHEMA_PATH)
    if machine.get("artifact_hash") != canonical_hash(machine):
        fail("machine receipt self-hash mismatch")
    if audit_git_state(machine.get("source_binding"), require_current_origin=False).get("verdict") != "PASS":
        fail("machine receipt git bindings no longer execute")
    if audit_input_bindings(machine).get("verdict") != "PASS":
        fail("machine receipt input bindings no longer execute")
    artifacts = [_raw_artifact(path, kind) for path, kind in TESTED_INPUTS + ENVELOPE_OUTPUTS]
    for run, expected_log in zip(machine["runs"], (FOCUSED_LOG_PATH, FULL_LOG_PATH)):
        if run["log_path"] != expected_log or run["log_sha256"] != raw_sha256(expected_log):
            fail(f"machine receipt/log mismatch: {expected_log}")

    context = load_json(TESTED_INPUTS[3][0])
    memory = load_json(TESTED_INPUTS[8][0])
    expert = load_json(TESTED_INPUTS[10][0])
    trace = load_json(TESTED_INPUTS[11][0])
    problem_fibre = load_json(TESTED_INPUTS[14][0])
    pre_action = load_json(TESTED_INPUTS[15][0])
    v0_failure = load_json(TESTED_INPUTS[0][0])
    v2_failure = load_json(TESTED_INPUTS[1][0])
    history = audit_historical_supersession()
    if history.get("verdict") != "PASS":
        fail(f"historical supersession audit did not pass: {history}")

    fibre_hash = problem_fibre.get("snapshot_hash") or problem_fibre.get("fibre_snapshot_hash")
    if not isinstance(fibre_hash, str) or re.fullmatch(r"[0-9a-f]{64}", fibre_hash) is None:
        fail("problem fibre lacks an exact 64-hex snapshot hash")
    pre_action_hash = pre_action.get("receipt_canonical_sha256")
    if not isinstance(pre_action_hash, str) or re.fullmatch(r"[0-9a-f]{64}", pre_action_hash) is None:
        fail("pre-action receipt lacks receipt_canonical_sha256")
    if pre_action_hash != _canonical_unprefixed(pre_action, "receipt_canonical_sha256"):
        fail("pre-action receipt canonical hash does not recompute")

    source_binding = copy.deepcopy(machine["source_binding"])
    # ``current_origin_main_at_freeze`` records the executed run-time fact.  The
    # gate re-audits durable relations without pretending the remote can never move.
    receipt: dict[str, Any] = {
        "schema_version": "rakl-math-pnp-pre-candidate-gate-v5",
        "receipt_id": "RAKL-MATH-PNP-O9d12a2a1a1b1-PRE-CANDIDATE-GATE-V5-20260811",
        "atom_id": ATOM,
        "status": "PROSPECTIVE_PROCESS_GATES_PASS_PRE_ACTION_FIBRE_FROZEN_NO_MATHEMATICAL_CANDIDATE",
        "recorded_at": utc_now(),
        "source_binding": source_binding,
        "primary_source_binding": {
            "path": TESTED_INPUTS[12][0],
            "url": "https://eccc.weizmann.ac.il/report/2025/033/download/",
            "raw_sha256": PRIMARY_SOURCE_SHA256,
            "retrieval_receipt_path": TESTED_INPUTS[13][0],
        },
        "supersession": {
            "v0_status": "REJECTED_PRE_CANDIDATE_AUTHORIZATION",
            "v0_correction_path": TESTED_INPUTS[0][0],
            "v0_correction_hash": v0_failure["artifact_hash"],
            "original_v0_gate_path": TESTED_INPUTS[16][0],
            "original_v0_gate_raw_sha256": history["v0_original_raw_sha256"],
            "original_v0_gate_artifact_hash": history["v0_original_artifact_hash"],
            "v2_status": "REJECTED_PRE_CANDIDATE_AUTHORIZATION",
            "v2_correction_path": TESTED_INPUTS[1][0],
            "v2_correction_hash": v2_failure["artifact_hash"],
            "original_v2_gate_path": TESTED_INPUTS[17][0],
            "original_v2_gate_raw_sha256": history["v2_original_raw_sha256"],
            "original_v2_gate_artifact_hash": history["v2_original_artifact_hash"],
            "v3_status": "HISTORICAL_PASS_AT_OWN_FREEZE_SUPERSEDED_FOR_CURRENT_MAIN",
            "prior_v3_machine_path": TESTED_INPUTS[20][0],
            "prior_v3_machine_raw_sha256": history["v3_machine_raw_sha256"],
            "prior_v3_machine_artifact_hash": history["v3_machine_artifact_hash"],
            "prior_v3_gate_path": TESTED_INPUTS[21][0],
            "prior_v3_gate_raw_sha256": history["v3_gate_raw_sha256"],
            "prior_v3_gate_artifact_hash": history["v3_gate_artifact_hash"],
            "v4_status": "REJECTED_ASSURANCE_ENVELOPE_PROVENANCE_AND_CHRONOLOGY",
            "v4_failure_path": TESTED_INPUTS[24][0],
            "v4_failure_raw_sha256": history["v4_failure_raw_sha256"],
            "v4_failure_artifact_hash": history["v4_failure_artifact_hash"],
            "prior_v4_machine_path": TESTED_INPUTS[25][0],
            "prior_v4_machine_raw_sha256": history["v4_machine_raw_sha256"],
            "prior_v4_machine_artifact_hash": history["v4_machine_artifact_hash"],
            "prior_v4_gate_path": TESTED_INPUTS[26][0],
            "prior_v4_gate_raw_sha256": history["v4_gate_raw_sha256"],
            "prior_v4_gate_artifact_hash": history["v4_gate_artifact_hash"],
            "historical_bytes_modified": False,
        },
        "artifacts": artifacts,
        "runtime_gate": {
            "context_packet_hash": context["packet_hash"],
            "memory_review_hash": memory["artifact_hash"],
            "expert_review_hash": expert["artifact_hash"],
            "trace_terminal_hash": trace["entries"][-1]["artifact_hash"],
            "context_gate": {"verdict": "PASS", "reasons": ["runtime_reconstructed_in_focused_v5_test"]},
            "memory_gate": {"verdict": "PASS", "reasons": ["runtime_reconstructed_in_focused_v5_test"]},
            "trace_gate": {"verdict": "PASS", "reasons": ["runtime_reconstructed_in_focused_v5_test"]},
            "plan_math_research": {
                "candidate_generation_allowed": True,
                "pre_candidate_actions": [],
                "candidate_paths_used": False,
                "candidate_identity": None,
            },
            "problem_fibre": {
                "path": TESTED_INPUTS[14][0],
                "snapshot_hash": fibre_hash,
                "authority": "PROPOSAL_ONLY_RETRIEVAL_VIEW",
            },
            "pre_action_fibre_receipt": {
                "path": TESTED_INPUTS[15][0],
                "receipt_canonical_sha256": pre_action_hash,
                "action_executed": False,
                "authority": "PROPOSAL_ONLY_PROCESS_TELEMETRY",
            },
        },
        "machine_run": {
            "path": MACHINE_RECEIPT_PATH,
            "raw_sha256": raw_sha256(MACHINE_RECEIPT_PATH),
            "artifact_hash": machine["artifact_hash"],
            "focused_log_path": FOCUSED_LOG_PATH,
            "focused_log_sha256": raw_sha256(FOCUSED_LOG_PATH),
            "full_log_path": FULL_LOG_PATH,
            "full_log_sha256": raw_sha256(FULL_LOG_PATH),
            "all_required_runs_passed": True,
        },
        "authority_contract": {
            "candidate_proposed": False,
            "mathematical_result": False,
            "proof_authority": False,
            "novelty_authority": False,
            "independent_peer_review": False,
            "p_vs_np_authority": False,
            "framework_promotion_authority": False,
            "fibre_search_universe_complete": False,
        },
        "next_action": "SOURCE_NATIVE_T_RULE_THEOREM_INVENTORY_IN_A_SEPARATE_VERSIONED_ROUND",
        "artifact_hash": "",
    }
    receipt["artifact_hash"] = canonical_hash(receipt)
    validate_document(receipt, GATE_SCHEMA_PATH)
    gate_audit = audit_gate_bindings(receipt, machine)
    if gate_audit.get("verdict") != "PASS":
        fail(f"generated gate bindings did not pass executable audit: {gate_audit}")
    return receipt


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="operation", required=True)
    run_parser = subparsers.add_parser("run", help="execute focused/full tests and write machine receipt")
    run_parser.add_argument("--subject-commit", required=True)
    subparsers.add_parser("build-gate", help="bind machine outputs into the final gate receipt")
    subparsers.add_parser("audit", help="re-audit existing machine and gate receipts")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.operation == "run":
        if not _valid_oid(args.subject_commit):
            fail("--subject-commit must be one full lowercase 40-hex Git OID")
        receipt = build_machine_receipt(args.subject_commit)
        write_json(MACHINE_RECEIPT_PATH, receipt)
        print(json.dumps({"verdict": "PASS", "receipt": MACHINE_RECEIPT_PATH, "artifact_hash": receipt["artifact_hash"]}, sort_keys=True))
        return 0
    if args.operation == "build-gate":
        receipt = build_gate_receipt()
        write_json(GATE_RECEIPT_PATH, receipt)
        print(json.dumps({"verdict": "PASS", "receipt": GATE_RECEIPT_PATH, "artifact_hash": receipt["artifact_hash"]}, sort_keys=True))
        return 0

    machine = load_json(MACHINE_RECEIPT_PATH)
    validate_document(machine, MACHINE_SCHEMA_PATH)
    checks = {
        "machine_self_hash": machine.get("artifact_hash") == canonical_hash(machine),
        "git": audit_git_state(machine.get("source_binding"), require_current_origin=False),
        "inputs": audit_input_bindings(machine),
        "machine_semantics": audit_machine_semantics(machine),
        "historical_supersession": audit_historical_supersession(),
    }
    gate = load_json(GATE_RECEIPT_PATH)
    validate_document(gate, GATE_SCHEMA_PATH)
    checks["gate_self_hash"] = gate.get("artifact_hash") == canonical_hash(gate)
    checks["gate_bindings"] = audit_gate_bindings(gate, machine)
    if (
        not checks["machine_self_hash"]
        or not checks["gate_self_hash"]
        or checks["git"].get("verdict") != "PASS"
        or checks["inputs"].get("verdict") != "PASS"
        or checks["machine_semantics"].get("verdict") != "PASS"
        or checks["historical_supersession"].get("verdict") != "PASS"
        or checks["gate_bindings"].get("verdict") != "PASS"
    ):
        print(json.dumps({"verdict": "FAIL", "checks": checks}, sort_keys=True))
        return 1
    print(json.dumps({"verdict": "PASS", "checks": checks}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
