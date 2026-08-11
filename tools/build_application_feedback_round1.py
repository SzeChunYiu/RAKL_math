#!/usr/bin/env python3
"""Build and audit the first RAKL_math -> RAKL feedback quarantine bundle.

The bundle is pinned to a producer commit which contains the lesson, result,
trace and context source files.  The bundle and import receipt therefore live
in a later commit.  ``--check`` reconstructs both objects from the producer
commit and fails if the committed transport artifacts differ.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_ROOT = ROOT / "framework" / "RAKL"
FRAMEWORK_SRC = FRAMEWORK_ROOT / "src"
if str(FRAMEWORK_SRC) not in sys.path:
    sys.path.insert(0, str(FRAMEWORK_SRC))

from rakl.application_feedback import (  # noqa: E402
    FeedbackImportVerdict,
    FeedbackKind,
    canonical_json_sha256,
    import_application_feedback,
    parse_application_feedback_bundle,
    stage_feedback_failure,
    stage_feedback_tool_candidate,
)


FRAMEWORK_COMMIT = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
FRAMEWORK_VERSION = "0.6.0"
REPOSITORY_URL = "https://github.com/SzeChunYiu/RAKL_math.git"
REPOSITORY_NAMESPACE = "github.com/SzeChunYiu/RAKL_math"
BUNDLE_PATH = ROOT / "receipts" / "application-feedback-round1-bundle-20260811.json"
RECEIPT_PATH = ROOT / "receipts" / "application-feedback-round1-import-20260811.json"
BASE = "research/meta/application_feedback/round1"

ITEMS = (
    (
        "o9_source_trace_hash",
        "FAILURE_EXPERIENCE",
        f"{REPOSITORY_NAMESPACE}::failure-experience::o9-source-trace-hash-v1",
    ),
    (
        "migrated_test_root",
        "FAILURE_EXPERIENCE",
        f"{REPOSITORY_NAMESPACE}::failure-experience::migrated-test-root-v1",
    ),
    (
        "framework_split_dangling_tests",
        "FAILURE_EXPERIENCE",
        f"{REPOSITORY_NAMESPACE}::failure-experience::framework-split-dangling-tests-v1",
    ),
    (
        "exact_framework_pin_runner",
        "TOOL_CANDIDATE",
        f"{REPOSITORY_NAMESPACE}::tool-candidate::exact-framework-pin-runner-v1",
    ),
)


def run_git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def git_bytes(repo: Path, specification: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(repo), "show", specification],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def load_json_at(commit: str, path: str) -> dict[str, Any]:
    document = json.loads(git_bytes(ROOT, f"{commit}:{path}"))
    if not isinstance(document, dict):
        raise ValueError(f"expected object at {commit}:{path}")
    return document


def blob_at(commit: str, path: str) -> str:
    return run_git(ROOT, "rev-parse", f"{commit}:{path}")


def sha256_bytes(value: bytes) -> str:
    import hashlib

    return hashlib.sha256(value).hexdigest()


def binding(commit: str, stem: str, payload: dict[str, Any]) -> dict[str, Any]:
    result_path = f"{BASE}/results/{stem}.json"
    trace_path = f"{BASE}/traces/{stem}.json"
    context_path = f"{BASE}/contexts/{stem}.json"
    result = load_json_at(commit, result_path)
    trace = load_json_at(commit, trace_path)
    result_bytes = git_bytes(ROOT, f"{commit}:{result_path}")
    trace_bytes = git_bytes(ROOT, f"{commit}:{trace_path}")
    context_bytes = git_bytes(ROOT, f"{commit}:{context_path}")
    observed = trace.get("observed_at_utc")
    if not isinstance(observed, str):
        raise ValueError(f"trace observed_at_utc missing: {trace_path}")
    return {
        "result_id": result["result_id"],
        "result_path": result_path,
        "result_git_blob_sha": blob_at(commit, result_path),
        "result_sha256": sha256_bytes(result_bytes),
        "trace_event_id": trace["event_id"],
        "trace_path": trace_path,
        "trace_git_blob_sha": blob_at(commit, trace_path),
        "trace_sha256": sha256_bytes(trace_bytes),
        "context_path": context_path,
        "context_git_blob_sha": blob_at(commit, context_path),
        "context_sha256": sha256_bytes(context_bytes),
        "observed_at_utc": observed,
    }


def build_bundle(producer_commit: str) -> dict[str, Any]:
    framework_head = run_git(FRAMEWORK_ROOT, "rev-parse", "HEAD")
    if framework_head != FRAMEWORK_COMMIT:
        raise ValueError(
            f"framework checkout is {framework_head}; expected {FRAMEWORK_COMMIT}"
        )
    pin = json.loads((ROOT / "config/rakl-framework-pin.json").read_text())
    if pin.get("commit") != FRAMEWORK_COMMIT:
        raise ValueError("machine-readable framework pin disagrees with bundle contract")
    remote = run_git(ROOT, "remote", "get-url", "origin")
    if remote.rstrip("/").removesuffix(".git") != REPOSITORY_URL.removesuffix(".git"):
        raise ValueError(f"unexpected producer origin: {remote}")

    items: list[dict[str, Any]] = []
    for stem, kind, item_id in ITEMS:
        source_path = f"{BASE}/lessons/{stem}.json"
        payload = load_json_at(producer_commit, source_path)
        items.append(
            {
                "item_id": item_id,
                "kind": kind,
                "source": {
                    "path": source_path,
                    "git_blob_sha": blob_at(producer_commit, source_path),
                },
                "payload": payload,
                "payload_canonical_sha256": canonical_json_sha256(payload),
                "application_bindings": binding(producer_commit, stem, payload),
                "supersedes": [],
            }
        )

    document: dict[str, Any] = {
        "schema_version": "application-feedback-bundle-v1",
        "bundle_id": f"{REPOSITORY_NAMESPACE}::feedback-bundle::round1-20260811",
        "producer": {
            "repository_namespace": REPOSITORY_NAMESPACE,
            "repository_url": REPOSITORY_URL,
            "commit_sha": producer_commit,
            "tree_sha": run_git(ROOT, "rev-parse", f"{producer_commit}^{{tree}}"),
        },
        "framework_requirement": {
            "repository_url": "https://github.com/SzeChunYiu/RAKL.git",
            "commit_sha": FRAMEWORK_COMMIT,
            "version": FRAMEWORK_VERSION,
        },
        "authority_envelope": {
            "requested_authority": "VERIFIED_LOCAL",
            "proposal_only": True,
            "inventory_mutation_allowed": False,
            "failure_lattice_mutation_allowed": False,
            "promotion_allowed": False,
        },
        "previous_bundle": None,
        "items": items,
    }
    document["bundle_canonical_sha256"] = canonical_json_sha256(document)
    return document


def import_bundle(document: dict[str, Any], producer_commit: str) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="rakl-math-feedback-") as temporary:
        checkout = Path(temporary) / "RAKL_math"
        subprocess.run(
            ["git", "clone", "-q", "--no-checkout", str(ROOT), str(checkout)],
            check=True,
        )
        run_git(checkout, "remote", "set-url", "origin", REPOSITORY_URL)
        run_git(checkout, "checkout", "-q", "--detach", producer_commit)
        receipt = import_application_feedback(
            document,
            source_repository=checkout,
            current_framework_commit_sha=FRAMEWORK_COMMIT,
            current_framework_version=FRAMEWORK_VERSION,
        )
    if receipt.verdict is not FeedbackImportVerdict.QUARANTINED_PROPOSAL:
        raise ValueError(
            f"feedback import did not quarantine: {receipt.verdict.value}: "
            + ", ".join(receipt.reasons)
        )
    bundle = parse_application_feedback_bundle(document)
    for item in bundle.items:
        if item.kind is FeedbackKind.FAILURE_EXPERIENCE:
            stage_feedback_failure(bundle, receipt, item.item_id)
        elif item.kind is FeedbackKind.TOOL_CANDIDATE:
            tool = stage_feedback_tool_candidate(bundle, receipt, item.item_id)
            if tool.authority.value != "HEURISTIC":
                raise ValueError("foreign tool authority was not downgraded")
    return receipt.to_dict()


def serialize(document: dict[str, Any]) -> str:
    return json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--producer-commit", required=True)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    producer = run_git(ROOT, "rev-parse", args.producer_commit)
    document = build_bundle(producer)
    receipt = import_bundle(copy.deepcopy(document), producer)
    expected = {BUNDLE_PATH: serialize(document), RECEIPT_PATH: serialize(receipt)}
    if args.check:
        mismatches = [
            str(path.relative_to(ROOT))
            for path, content in expected.items()
            if not path.exists() or path.read_text(encoding="utf-8") != content
        ]
        if mismatches:
            raise SystemExit("feedback artifacts differ: " + ", ".join(mismatches))
    else:
        for path, content in expected.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print(
        json.dumps(
            {
                "bundle_canonical_sha256": document["bundle_canonical_sha256"],
                "import_receipt_id": receipt["receipt_id"],
                "producer_commit": producer,
                "verdict": receipt["verdict"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
