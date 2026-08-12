from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker
from rakl.experience_substrate import (
    EpisodeOutcome,
    EpisodeStorageAdmission,
    TaskEpisode,
    episode_content_bytes,
    validate_episode,
)


ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework/RAKL"
RECEIPT = ROOT / "receipts/framework-episode-inventory-classification-extension-v2-ns-b2a1c-r2-20260812.json"
SCHEMA = ROOT / "schemas/framework-episode-inventory-classification-extension-v2-ns-b2a1c-r2.schema.json"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def git(repository: Path, *arguments: str, binary: bool = False) -> str | bytes:
    run = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        text=not binary,
    )
    return run.stdout if binary else run.stdout.strip()


def canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def runtime_episode(value: dict) -> TaskEpisode:
    return TaskEpisode(
        episode_id=value["episode_id"],
        task_id=value["task_id"],
        atom_id=value["atom_id"],
        context_hash=value["context_hash"],
        problem_signature=tuple(value["problem_signature"]),
        fibre_snapshot_hash=value["fibre_snapshot_hash"],
        operator_ids=tuple(value["operator_ids"]),
        action_trace=tuple(value["action_trace"]),
        observation_ids=tuple(value["observation_ids"]),
        verification_ids=tuple(value["verification_ids"]),
        outcome=EpisodeOutcome(value["outcome"]),
        residual_signature=tuple(value["residual_signature"]),
        evidence_pointers=tuple(value["evidence_pointers"]),
        artifact_hash=value["artifact_hash"],
        timestamp=value["timestamp"],
        cost=value["cost"],
        storage_admission=EpisodeStorageAdmission(value["storage_admission"]),
    )


def test_receipt_schema_hash_lineage_and_zero_authority_are_exact() -> None:
    receipt, schema = load(RECEIPT), load(SCHEMA)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
    assert receipt["artifact_hash"] == canonical_hash(receipt)
    assert all(value is False for value in receipt["authority_contract"].values())
    assert receipt["disposition"] == {
        "parent_receipt_modified": False,
        "prior_extensions_modified": False,
        "source_containers_modified": False,
        "classification_extension_registered": True,
        "task_episode_objects_registered": 1,
        "non_task_episode_containers_registered": 2,
        "classification_basis": "EXPLICIT_CONTAINER_IDENTITY_AND_CURRENT_TASK_EPISODE_SCHEMA_RUNTIME_CLASSIFICATION",
    }

    parent = receipt["lineage"]["frozen_parent_inventory"]
    parent_raw = git(
        ROOT,
        "show",
        f'{parent["merge_commit"]}:{parent["receipt_path"]}',
        binary=True,
    )
    assert isinstance(parent_raw, bytes)
    assert parent["frozen_episode_count"] == 19
    assert git(ROOT, "rev-parse", f'{parent["merge_commit"]}:{parent["receipt_path"]}') == parent["receipt_blob_at_merge"]
    assert "sha256:" + hashlib.sha256(parent_raw).hexdigest() == parent["receipt_file_sha256"]
    assert json.loads(parent_raw)["artifact_hash"] == parent["receipt_artifact_hash"]

    for prior in receipt["lineage"]["preserved_prior_extensions"]:
        raw = git(
            ROOT,
            "show",
            f'{prior["introduction_commit"]}:{prior["receipt_path"]}',
            binary=True,
        )
        assert isinstance(raw, bytes)
        assert git(ROOT, "rev-parse", f'{prior["introduction_commit"]}^{{tree}}') == prior["introduction_tree"]
        assert git(ROOT, "rev-parse", f'{prior["introduction_commit"]}:{prior["receipt_path"]}') == prior["git_blob_sha"]
        assert hashlib.sha256(raw).hexdigest() == prior["raw_sha256"]
        assert json.loads(raw)["artifact_hash"] == prior["receipt_artifact_hash"]


def test_all_three_paths_are_byte_exact_and_classified_under_the_pinned_current_contract() -> None:
    receipt = load(RECEIPT)
    audit = receipt["audit_binding"]
    assert git(ROOT, "rev-parse", f'{audit["current_main_at_audit"]}^{{tree}}') == audit["current_tree"]
    assert git(FRAMEWORK, "rev-parse", f'{audit["framework_commit"]}:schemas/task-episode.schema.json') == audit["task_episode_schema_blob"]
    assert git(FRAMEWORK, "rev-parse", f'{audit["framework_commit"]}:src/rakl/experience_substrate.py') == audit["experience_substrate_blob"]
    # This is a frozen historical audit.  A later execution pin may advance
    # while retaining the exact historical schema/runtime blobs checked above.
    assert git(
        FRAMEWORK,
        "merge-base",
        "--is-ancestor",
        audit["framework_commit"],
        "HEAD",
    ) == ""

    strict_schema_raw = git(
        FRAMEWORK,
        "show",
        f'{audit["framework_commit"]}:schemas/task-episode.schema.json',
        binary=True,
    )
    assert isinstance(strict_schema_raw, bytes)
    strict_schema = json.loads(strict_schema_raw)
    validator = Draft202012Validator(strict_schema, format_checker=FormatChecker())

    task_episode_count = 0
    non_task_count = 0
    for item in receipt["classifications"]:
        assert git(ROOT, "merge-base", "--is-ancestor", item["introduction_commit"], audit["current_main_at_audit"]) == ""
        assert git(ROOT, "merge-base", "--is-ancestor", item["current_version_commit"], audit["current_main_at_audit"]) == ""
        assert git(ROOT, "rev-parse", f'{item["introduction_commit"]}^{{tree}}') == item["introduction_tree"]
        assert git(ROOT, "rev-parse", f'{item["current_version_commit"]}^{{tree}}') == item["current_version_tree"]
        assert git(ROOT, "rev-parse", f'{item["current_version_commit"]}:{item["path"]}') == item["git_blob_sha"]
        assert git(ROOT, "rev-parse", f'{audit["current_main_at_audit"]}:{item["path"]}') == item["current_main_blob_sha"] == item["git_blob_sha"]
        raw = git(ROOT, "show", f'{audit["current_main_at_audit"]}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert raw == (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["raw_sha256"]
        value = json.loads(raw)
        assert value["episode_id"] == item["observed_episode_id"]
        errors = list(validator.iter_errors(value))

        if item["classification"] == "CURRENT_VALID_TASK_EPISODE_PROPOSAL_SHADOW":
            task_episode_count += 1
            assert item["strict_task_episode_schema_verdict"] == "PASS"
            assert item["strict_task_episode_schema_error_count"] == len(errors) == 0
            assert item["runtime_constructor_invoked"] is True
            assert item["runtime_constructor_disposition"] == "EXACT_TASK_EPISODE_VALIDATION_PASS"
            episode = runtime_episode(value)
            assert validate_episode(episode) == ()
            digest = hashlib.sha256(episode_content_bytes(episode)).hexdigest()
            assert digest == value["artifact_hash"] == item["stored_hash"] == item["computed_runtime_digest"]
            assert episode.storage_admission is EpisodeStorageAdmission.PROPOSAL_SHADOW_STORED
            assert item["storage_admission"] == "PROPOSAL_SHADOW_STORED"
        else:
            non_task_count += 1
            assert item["classification"] == "NON_TASK_EPISODE_CONTAINER_WITH_EPISODE_ID"
            assert item["strict_task_episode_schema_verdict"] == "FAIL"
            assert item["strict_task_episode_schema_error_count"] == len(errors) == 16
            assert item["runtime_constructor_invoked"] is False
            assert item["runtime_constructor_disposition"] == "NOT_APPLICABLE_NON_TASK_EPISODE_CONTAINER"

    assert (task_episode_count, non_task_count) == (1, 2)


def test_schema_rejects_identity_authority_classification_hash_and_omission_mutations() -> None:
    receipt, schema = load(RECEIPT), load(SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    hostile: list[dict] = []
    bad = copy.deepcopy(receipt); bad["authority_contract"]["grants_framework_authority"] = True; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["audit_binding"]["current_main_at_audit"] = "0" * 40; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["classifications"][0]["classification"] = "NON_TASK_EPISODE_CONTAINER_WITH_EPISODE_ID"; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["classifications"][1]["classification"] = "CURRENT_VALID_TASK_EPISODE_PROPOSAL_SHADOW"; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["classifications"][1]["stored_hash"] = "0" * 64; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["classifications"][0]["stored_hash"] += "\n"; hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["classifications"].pop(); hostile.append(bad)
    bad = copy.deepcopy(receipt); bad["artifact_hash"] = 7; hostile.append(bad)
    for value in hostile:
        assert list(validator.iter_errors(value))
