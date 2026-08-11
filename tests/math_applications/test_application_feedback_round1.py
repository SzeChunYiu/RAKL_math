from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = ROOT / "framework" / "RAKL"
BUNDLE_PATH = ROOT / "receipts/application-feedback-round1-bundle-20260811.json"
RECEIPT_PATH = ROOT / "receipts/application-feedback-round1-import-20260811.json"
EXPECTED_FRAMEWORK = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
EXPECTED_FRAMEWORK_URL = "https://github.com/SzeChunYiu/RAKL.git"
BUILDER_PATH = ROOT / "tools/build_application_feedback_round1.py"


def _load(path: Path) -> dict:
    document = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(document, dict)
    return document


def _canonical_json_sha256(value: object) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _run_builder(framework_source: Path) -> subprocess.CompletedProcess[str]:
    bundle = _load(BUNDLE_PATH)
    return subprocess.run(
        [
            sys.executable,
            str(BUILDER_PATH),
            "--producer-commit",
            bundle["producer"]["commit_sha"],
            "--framework-source",
            str(framework_source),
            "--check",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )


def _framework_clone(tmp_path: Path) -> Path:
    checkout = tmp_path / "framework-source"
    subprocess.run(
        ["git", "clone", "-q", str(FRAMEWORK_ROOT), str(checkout)], check=True
    )
    subprocess.run(
        [
            "git",
            "-C",
            str(checkout),
            "remote",
            "set-url",
            "origin",
            EXPECTED_FRAMEWORK_URL,
        ],
        check=True,
    )
    return checkout


def _load_builder_module():
    spec = importlib.util.spec_from_file_location(
        "round1_feedback_builder_test", BUILDER_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_round1_bundle_and_receipt_are_exactly_reproducible_and_quarantined() -> None:
    bundle = _load(BUNDLE_PATH)
    receipt = _load(RECEIPT_PATH)
    producer = bundle["producer"]["commit_sha"]

    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/build_application_feedback_round1.py"),
            "--producer-commit",
            producer,
            "--check",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    rebuilt = json.loads(completed.stdout)
    assert rebuilt == {
        "bundle_canonical_sha256": bundle["bundle_canonical_sha256"],
        "import_receipt_id": receipt["receipt_id"],
        "producer_commit": producer,
        "verdict": "QUARANTINED_PROPOSAL",
    }

    unhashed = copy.deepcopy(bundle)
    unhashed.pop("bundle_canonical_sha256")
    assert bundle["bundle_canonical_sha256"] == _canonical_json_sha256(unhashed)
    assert bundle["framework_requirement"] == {
        "repository_url": "https://github.com/SzeChunYiu/RAKL.git",
        "commit_sha": EXPECTED_FRAMEWORK,
        "version": "0.6.0",
    }
    assert receipt["verdict"] == "QUARANTINED_PROPOSAL"
    assert receipt["effective_authority"] == "HEURISTIC"
    assert receipt["mutation"] == {
        "inventory_mutation_performed": False,
        "failure_lattice_mutation_performed": False,
    }
    assert receipt["grants_scientific_authority"] is False
    assert receipt["grants_method_promotion"] is False
    assert [item["kind"] for item in bundle["items"]] == [
        "FAILURE_EXPERIENCE",
        "FAILURE_EXPERIENCE",
        "FAILURE_EXPERIENCE",
        "TOOL_CANDIDATE",
    ]
    assert receipt["quarantined_item_ids"] == [
        item["item_id"] for item in bundle["items"]
    ]


def test_round1_transport_artifacts_have_exact_git_bindings() -> None:
    bundle = _load(BUNDLE_PATH)
    producer = bundle["producer"]
    assert _git("cat-file", "-t", producer["commit_sha"]) == "commit"
    assert _git("rev-parse", f"{producer['commit_sha']}^{{tree}}") == producer["tree_sha"]
    for item in bundle["items"]:
        assert _git(
            "rev-parse", f"{producer['commit_sha']}:{item['source']['path']}"
        ) == item["source"]["git_blob_sha"]
        bindings = item["application_bindings"]
        for role in ("result", "trace", "context"):
            assert _git(
                "rev-parse",
                f"{producer['commit_sha']}:{bindings[f'{role}_path']}",
            ) == bindings[f"{role}_git_blob_sha"]


def test_round1_producer_is_reachable_from_merged_main_and_crosslinks_precede_freeze() -> None:
    bundle = _load(BUNDLE_PATH)
    producer = bundle["producer"]
    assert (
        subprocess.run(
            [
                "git",
                "-C",
                str(ROOT),
                "merge-base",
                "--is-ancestor",
                producer["commit_sha"],
                "HEAD",
            ],
            check=False,
        ).returncode
        == 0
    )
    producer_committed_at = datetime.fromisoformat(
        _git("show", "-s", "--format=%cI", producer["commit_sha"])
    )
    for item in bundle["items"]:
        bindings = item["application_bindings"]
        result = json.loads(
            _git("show", f"{producer['commit_sha']}:{bindings['result_path']}")
        )
        trace = json.loads(
            _git("show", f"{producer['commit_sha']}:{bindings['trace_path']}")
        )
        context = json.loads(
            _git("show", f"{producer['commit_sha']}:{bindings['context_path']}")
        )
        assert trace["result_id"] == result["result_id"] == bindings["result_id"]
        assert trace["context_id"] == context["context_id"]
        assert (
            datetime.fromisoformat(trace["observed_at_utc"].replace("Z", "+00:00"))
            <= producer_committed_at
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        ("result", "trace result_id does not match result"),
        ("context", "trace context_id does not match context"),
        ("future", "observation timestamp is after producer commit"),
    ),
)
def test_binding_validator_rejects_broken_crosslinks_and_future_observation(
    mutation: str, message: str
) -> None:
    builder = _load_builder_module()
    result = {"result_id": "result-1"}
    trace = {
        "event_id": "event-1",
        "result_id": "result-1",
        "context_id": "context-1",
        "observed_at_utc": "2026-08-11T08:00:00Z",
    }
    context = {"context_id": "context-1"}
    if mutation == "result":
        trace["result_id"] = "result-2"
    elif mutation == "context":
        trace["context_id"] = "context-2"
    else:
        trace["observed_at_utc"] = "2026-08-11T09:00:01Z"
    with pytest.raises(ValueError, match=message):
        builder.validate_binding_documents(
            result,
            trace,
            context,
            producer_committed_at="2026-08-11T09:00:00+00:00",
        )


def test_builder_rejects_wrong_framework_origin_before_import(tmp_path: Path) -> None:
    source = _framework_clone(tmp_path)
    marker = tmp_path / "imported"
    (source / "src/rakl/__init__.py").write_text(
        f"from pathlib import Path\nPath({str(marker)!r}).write_text('imported')\n",
        encoding="utf-8",
    )
    subprocess.run(
        [
            "git",
            "-C",
            str(source),
            "remote",
            "set-url",
            "origin",
            "https://example.invalid/not-rakl.git",
        ],
        check=True,
    )
    completed = _run_builder(source)
    assert completed.returncode != 0
    assert "unexpected framework origin" in completed.stderr
    assert not marker.exists()


def test_builder_rejects_dirty_framework_authority_before_import(tmp_path: Path) -> None:
    source = _framework_clone(tmp_path)
    marker = tmp_path / "imported"
    (source / "src/rakl/__init__.py").write_text(
        f"from pathlib import Path\nPath({str(marker)!r}).write_text('imported')\n",
        encoding="utf-8",
    )
    completed = _run_builder(source)
    assert completed.returncode != 0
    assert "framework authority paths are not clean" in completed.stderr
    assert not marker.exists()


def test_builder_uses_detached_historical_framework_when_source_head_moves(
    tmp_path: Path,
) -> None:
    source = _framework_clone(tmp_path)
    parent = subprocess.run(
        ["git", "-C", str(source), "rev-parse", f"{EXPECTED_FRAMEWORK}^"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    subprocess.run(
        ["git", "-C", str(source), "checkout", "-q", "--detach", parent], check=True
    )
    completed = _run_builder(source)
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert json.loads(completed.stdout)["verdict"] == "QUARANTINED_PROPOSAL"
