from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys

from jsonschema import Draft202012Validator, FormatChecker

from rakl.application_feedback import canonical_json_sha256


ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = ROOT / "framework" / "RAKL"
BUNDLE_PATH = ROOT / "receipts/application-feedback-round1-bundle-20260811.json"
RECEIPT_PATH = ROOT / "receipts/application-feedback-round1-import-20260811.json"
EXPECTED_FRAMEWORK = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"


def _load(path: Path) -> dict:
    document = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(document, dict)
    return document


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


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
    assert bundle["bundle_canonical_sha256"] == canonical_json_sha256(unhashed)
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


def test_round1_transport_artifacts_satisfy_framework_schemas_and_git_bindings() -> None:
    bundle = _load(BUNDLE_PATH)
    receipt = _load(RECEIPT_PATH)
    for schema_name, document in (
        ("application-feedback-bundle.schema.json", bundle),
        ("application-feedback-import-receipt.schema.json", receipt),
    ):
        schema = _load(FRAMEWORK_ROOT / "schemas" / schema_name)
        Draft202012Validator.check_schema(schema)
        errors = tuple(
            Draft202012Validator(
                schema, format_checker=FormatChecker()
            ).iter_errors(document)
        )
        assert errors == ()

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
