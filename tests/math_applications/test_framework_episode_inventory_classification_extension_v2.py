from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "receipts/framework-episode-inventory-classification-extension-v2-ns-b1a3b1-r2-20260811.json"
SCHEMA = ROOT / "schemas/framework-episode-inventory-classification-extension-v2.schema.json"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def git(*arguments: str, binary: bool = False) -> str | bytes:
    run = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        text=not binary,
    )
    return run.stdout if binary else run.stdout.strip()


def canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_classification_extension_schema_hash_lineage_and_non_authority_are_exact() -> None:
    receipt, schema = load(RECEIPT), load(SCHEMA)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
    assert receipt["artifact_hash"] == canonical_hash(receipt)
    assert all(value is False for value in receipt["authority_contract"].values())
    assert receipt["disposition"] == {
        "parent_receipt_modified": False,
        "prior_extension_modified": False,
        "source_containers_modified": False,
        "classification_extension_registered": True,
        "classification_basis": "EXPLICIT_CONTAINER_IDENTITY_AND_STRICT_TASK_EPISODE_SCHEMA_FAILURE",
    }
    for lineage in receipt["lineage"].values():
        raw = git("show", f'{lineage["merge_commit"] if "merge_commit" in lineage else lineage["introduction_commit"]}:{lineage["receipt_path"]}', binary=True)
        assert isinstance(raw, bytes)
        if "receipt_blob_at_merge" in lineage:
            assert git("rev-parse", f'{lineage["merge_commit"]}:{lineage["receipt_path"]}') == lineage["receipt_blob_at_merge"]
            assert "sha256:" + hashlib.sha256(raw).hexdigest() == lineage["receipt_file_sha256"]
        else:
            assert git("rev-parse", f'{lineage["introduction_commit"]}:{lineage["receipt_path"]}') == lineage["git_blob_sha"]
            assert hashlib.sha256(raw).hexdigest() == lineage["raw_sha256"]


def test_classified_paths_are_byte_exact_non_task_containers() -> None:
    receipt = load(RECEIPT)
    audit = receipt["audit_binding"]
    assert len(receipt["classifications"]) == 2
    for item in receipt["classifications"]:
        raw = git("show", f'{audit["current_main_at_audit"]}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert raw == (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["raw_sha256"]
        assert git("rev-parse", f'{item["introduction_commit"]}:{item["path"]}') == item["git_blob_sha"]
        value = json.loads(raw)
        assert value["episode_id"] == item["observed_episode_id"]
        assert item["classification"] == "NON_TASK_EPISODE_CONTAINER_WITH_EPISODE_ID"
        assert item["strict_task_episode_schema_verdict"] == "FAIL"
        assert item["strict_task_episode_schema_error_count"] > 0
        assert item["runtime_constructor_invoked"] is False


def test_schema_rejects_authority_identity_hash_and_omission_mutations() -> None:
    receipt, schema = load(RECEIPT), load(SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    hostile: list[dict] = []
    bad = copy.deepcopy(receipt); bad["authority_contract"]["grants_framework_authority"] = True; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["classifications"][0]["classification"] = "TASK_EPISODE"; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["classifications"][0]["raw_sha256"] += "\n"; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["classifications"].pop(); hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["artifact_hash"] = 7; hostile.append(bad)
    for value in hostile:
        assert list(validator.iter_errors(value))

