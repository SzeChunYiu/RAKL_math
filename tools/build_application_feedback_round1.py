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
from contextlib import contextmanager
from datetime import datetime
import hashlib
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_ROOT = ROOT / "framework" / "RAKL"
FRAMEWORK_COMMIT = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
FRAMEWORK_VERSION = "0.6.0"
FRAMEWORK_REPOSITORY_URL = "https://github.com/SzeChunYiu/RAKL.git"
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


def git_succeeds(repo: Path, *args: str) -> bool:
    return (
        subprocess.run(
            ["git", "-C", str(repo), *args],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode
        == 0
    )


def normalized_repository_url(value: str) -> str:
    return value.strip().rstrip("/").removesuffix(".git")


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
    return hashlib.sha256(value).hexdigest()


def canonical_json_sha256(value: object) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def validate_binding_documents(
    result: dict[str, Any],
    trace: dict[str, Any],
    context: dict[str, Any],
    *,
    producer_committed_at: str,
) -> str:
    if trace.get("result_id") != result.get("result_id"):
        raise ValueError("trace result_id does not match result")
    if trace.get("context_id") != context.get("context_id"):
        raise ValueError("trace context_id does not match context")
    observed = trace.get("observed_at_utc")
    if not isinstance(observed, str) or not observed.endswith("Z"):
        raise ValueError("trace observed_at_utc missing or not strict UTC")
    try:
        observed_at = datetime.fromisoformat(observed.replace("Z", "+00:00"))
        committed_at = datetime.fromisoformat(producer_committed_at)
    except ValueError as exc:
        raise ValueError("trace or producer timestamp is invalid") from exc
    if observed_at.tzinfo is None or committed_at.tzinfo is None:
        raise ValueError("trace or producer timestamp lacks timezone")
    if observed_at > committed_at:
        raise ValueError("observation timestamp is after producer commit")
    return observed


def binding(commit: str, stem: str, *, producer_committed_at: str) -> dict[str, Any]:
    result_path = f"{BASE}/results/{stem}.json"
    trace_path = f"{BASE}/traces/{stem}.json"
    context_path = f"{BASE}/contexts/{stem}.json"
    result = load_json_at(commit, result_path)
    trace = load_json_at(commit, trace_path)
    context = load_json_at(commit, context_path)
    result_bytes = git_bytes(ROOT, f"{commit}:{result_path}")
    trace_bytes = git_bytes(ROOT, f"{commit}:{trace_path}")
    context_bytes = git_bytes(ROOT, f"{commit}:{context_path}")
    observed = validate_binding_documents(
        result,
        trace,
        context,
        producer_committed_at=producer_committed_at,
    )
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
    remote = run_git(ROOT, "remote", "get-url", "origin")
    if normalized_repository_url(remote) != normalized_repository_url(REPOSITORY_URL):
        raise ValueError(f"unexpected producer origin: {remote}")
    if not git_succeeds(ROOT, "merge-base", "--is-ancestor", producer_commit, "HEAD"):
        raise ValueError("producer commit is not reachable from current HEAD")
    producer_committed_at = run_git(
        ROOT, "show", "-s", "--format=%cI", producer_commit
    )

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
                "application_bindings": binding(
                    producer_commit,
                    stem,
                    producer_committed_at=producer_committed_at,
                ),
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
            "repository_url": FRAMEWORK_REPOSITORY_URL,
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


def verify_framework_source(source: Path) -> None:
    if not (source / ".git").exists():
        raise ValueError(f"historical framework source is not a Git checkout: {source}")
    origin = run_git(source, "remote", "get-url", "origin")
    if normalized_repository_url(origin) != normalized_repository_url(
        FRAMEWORK_REPOSITORY_URL
    ):
        raise ValueError(f"unexpected framework origin: {origin}")
    dirty = run_git(
        source,
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
        "--",
        "src",
        "schemas",
        "pyproject.toml",
    )
    if dirty:
        raise ValueError("framework authority paths are not clean")


def verify_historical_framework_checkout(checkout: Path) -> None:
    if run_git(checkout, "rev-parse", "HEAD") != FRAMEWORK_COMMIT:
        raise ValueError("historical framework checkout is not at the exact contract commit")
    origin = run_git(checkout, "remote", "get-url", "origin")
    if normalized_repository_url(origin) != normalized_repository_url(
        FRAMEWORK_REPOSITORY_URL
    ):
        raise ValueError(f"unexpected historical framework origin: {origin}")
    dirty = run_git(
        checkout,
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
        "--",
        "src",
        "schemas",
        "pyproject.toml",
    )
    if dirty:
        raise ValueError("historical framework authority paths are not clean")


@contextmanager
def historical_framework_checkout(source: Path) -> Iterator[Path]:
    source = source.expanduser().resolve()
    verify_framework_source(source)
    with tempfile.TemporaryDirectory(prefix="rakl-framework-round1-") as temporary:
        checkout = Path(temporary) / "RAKL"
        run_git(Path(temporary), "init", "-q", str(checkout))
        run_git(checkout, "remote", "add", "origin", FRAMEWORK_REPOSITORY_URL)
        if git_succeeds(source, "cat-file", "-e", f"{FRAMEWORK_COMMIT}^{{commit}}"):
            run_git(checkout, "fetch", "-q", "--no-tags", str(source), FRAMEWORK_COMMIT)
        else:
            run_git(
                checkout,
                "fetch",
                "-q",
                "--no-tags",
                "--depth=1",
                "origin",
                FRAMEWORK_COMMIT,
            )
        run_git(checkout, "checkout", "-q", "--detach", "FETCH_HEAD")
        verify_historical_framework_checkout(checkout)
        yield checkout


def load_feedback_api(framework_checkout: Path):
    source = str(framework_checkout / "src")
    if source not in sys.path:
        sys.path.insert(0, source)
    return importlib.import_module("rakl.application_feedback")


def import_bundle(
    document: dict[str, Any], producer_commit: str, feedback_api
) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="rakl-math-feedback-") as temporary:
        checkout = Path(temporary) / "RAKL_math"
        subprocess.run(
            ["git", "clone", "-q", "--no-checkout", str(ROOT), str(checkout)],
            check=True,
        )
        run_git(checkout, "remote", "set-url", "origin", REPOSITORY_URL)
        run_git(checkout, "checkout", "-q", "--detach", producer_commit)
        receipt = feedback_api.import_application_feedback(
            document,
            source_repository=checkout,
            current_framework_commit_sha=FRAMEWORK_COMMIT,
            current_framework_version=FRAMEWORK_VERSION,
        )
    if receipt.verdict is not feedback_api.FeedbackImportVerdict.QUARANTINED_PROPOSAL:
        raise ValueError(
            f"feedback import did not quarantine: {receipt.verdict.value}: "
            + ", ".join(receipt.reasons)
        )
    bundle = feedback_api.parse_application_feedback_bundle(document)
    for item in bundle.items:
        if item.kind is feedback_api.FeedbackKind.FAILURE_EXPERIENCE:
            feedback_api.stage_feedback_failure(bundle, receipt, item.item_id)
        elif item.kind is feedback_api.FeedbackKind.TOOL_CANDIDATE:
            tool = feedback_api.stage_feedback_tool_candidate(bundle, receipt, item.item_id)
            if tool.authority.value != "HEURISTIC":
                raise ValueError("foreign tool authority was not downgraded")
    return receipt.to_dict()


def serialize(document: dict[str, Any]) -> str:
    return json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--producer-commit", required=True)
    parser.add_argument(
        "--framework-source",
        default=str(FRAMEWORK_ROOT),
        help="clean RAKL Git checkout used only as an object source for the exact historical authority commit",
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    producer = run_git(ROOT, "rev-parse", args.producer_commit)
    document = build_bundle(producer)
    with historical_framework_checkout(Path(args.framework_source)) as framework_checkout:
        feedback_api = load_feedback_api(framework_checkout)
        if feedback_api.canonical_json_sha256(document["items"][0]["payload"]) != document[
            "items"
        ][0]["payload_canonical_sha256"]:
            raise ValueError("local canonical JSON implementation disagrees with framework")
        receipt = import_bundle(copy.deepcopy(document), producer, feedback_api)
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
