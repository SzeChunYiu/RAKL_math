from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker
from rakl.experience_substrate import (
    EpisodeOutcome,
    TaskEpisode,
    episode_content_bytes,
    validate_episode,
)


ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework/RAKL"
RECEIPT = ROOT / "receipts/framework-episode-inventory-extension-h4d1b-20260811.json"
SCHEMA = ROOT / "schemas/framework-episode-inventory-extension.schema.json"
PARENT_RECEIPT = ROOT / "receipts/framework-pr153-hash-contract-migration-20260811.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _git(repository: Path, *arguments: str, binary: bool = False) -> str | bytes:
    run = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        text=not binary,
    )
    return run.stdout if binary else run.stdout.strip()


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _episode(value: dict) -> TaskEpisode:
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
    )


def test_extension_receipt_schema_hash_and_authority_are_exact() -> None:
    receipt = _load(RECEIPT)
    schema = _load(SCHEMA)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    assert receipt["classification"] == "POST_MIGRATION_CURRENT_VALID_RAW_EXACT"
    assert all(value is False for value in receipt["authority_contract"].values())
    assert receipt["disposition"] == {
        "parent_receipt_modified": False,
        "source_episode_modified": False,
        "extension_registered": True,
        "main_ci_repair_required": True,
    }


def test_parent_receipt_and_new_episode_are_content_bound_without_rewrite() -> None:
    receipt = _load(RECEIPT)
    parent = receipt["parent_inventory"]
    parent_raw = PARENT_RECEIPT.read_bytes()
    assert _git(ROOT, "rev-parse", f'{parent["merge_commit"]}:{parent["receipt_path"]}') == parent["receipt_blob_at_merge"]
    assert _git(ROOT, "show", f'{parent["merge_commit"]}:{parent["receipt_path"]}', binary=True) == parent_raw
    assert "sha256:" + hashlib.sha256(parent_raw).hexdigest() == parent["receipt_file_sha256"]
    assert _load(PARENT_RECEIPT)["artifact_hash"] == parent["receipt_artifact_hash"]

    source = receipt["source_binding"]
    assert source["repository_url"] == _load(PARENT_RECEIPT)["application_repository"]["repository"]
    assert source["current_main_at_audit"] == receipt["triggering_failure"]["head_sha"]
    assert _git(
        ROOT,
        "merge-base",
        "--is-ancestor",
        source["introduction_commit"],
        source["current_main_at_audit"],
    ) == ""
    episode_path = ROOT / source["path"]
    raw = episode_path.read_bytes()
    assert _git(ROOT, "show", f'{source["introduction_commit"]}:{source["path"]}', binary=True) == raw
    assert _git(ROOT, "rev-parse", f'{source["introduction_commit"]}:{source["path"]}') == source["git_blob_sha"]
    assert hashlib.sha256(raw).hexdigest() == source["raw_sha256"]
    assert _git(ROOT, "show", "-s", "--format=%T", source["introduction_commit"]) == source["introduction_tree"]
    assert _git(ROOT, "rev-parse", f'{source["current_main_at_audit"]}^{{tree}}') == source["current_tree"]
    assert _git(ROOT, "rev-parse", f'{source["current_main_at_audit"]}:{source["path"]}') == source["git_blob_sha"]
    assert _git(ROOT, "show", f'{source["current_main_at_audit"]}:{source["path"]}', binary=True) == raw
    assert parent["merge_commit"] == "b18fcd35855d67962e28036f4a445ab24d0c4406"
    assert len(_git(ROOT, "rev-list", "--parents", "-n", "1", parent["merge_commit"]).split()) == 3


def test_new_episode_passes_exact_historical_schema_runtime_and_hash_contract() -> None:
    receipt = _load(RECEIPT)
    framework = receipt["framework_binding"]
    current_framework = _git(FRAMEWORK, "rev-parse", "HEAD")
    assert framework["commit"] == "9027cc6beab7e935d714bbdf8e902b89b50caaa8"
    assert _git(
        FRAMEWORK,
        "merge-base",
        "--is-ancestor",
        framework["commit"],
        current_framework,
    ) == ""
    assert _git(FRAMEWORK, "rev-parse", f'{framework["commit"]}:schemas/task-episode.schema.json') == framework["task_episode_schema_blob"]
    assert _git(FRAMEWORK, "rev-parse", f'{framework["commit"]}:src/rakl/experience_substrate.py') == framework["experience_substrate_blob"]

    value = _load(ROOT / receipt["source_binding"]["path"])
    schema_raw = _git(
        FRAMEWORK,
        "show",
        f'{framework["commit"]}:schemas/task-episode.schema.json',
        binary=True,
    )
    assert isinstance(schema_raw, bytes)
    Draft202012Validator(
        json.loads(schema_raw), format_checker=FormatChecker()
    ).validate(value)
    episode = _episode(value)
    digest = hashlib.sha256(episode_content_bytes(episode)).hexdigest()
    assert validate_episode(episode) == ()
    assert receipt["runtime_binding"] == {
        "stored_hash": value["artifact_hash"],
        "computed_runtime_digest": digest,
        "schema_verdict": "PASS",
        "runtime_verdict": "PASS",
        "runtime_reasons": [],
    }


def test_triggering_main_failure_is_preserved_as_exact_repair_provenance() -> None:
    failure = _load(RECEIPT)["triggering_failure"]
    assert failure == {
        "run_id": 31506541609,
        "head_sha": "111a3f95c72b0a418f968708bd3eda77ef98bccf",
        "passed": 418,
        "failed": 1,
        "failure_test": "tests/math_applications/test_framework_pr153_hash_contract_migration.py::test_episode_inventory_is_the_exact_frozen_19_object_audit",
        "failure_reason": "new strict-valid H4d1b episode was not registered as a post-migration inventory extension",
    }


def test_schema_rejects_noncanonical_or_mutated_identity_fields() -> None:
    receipt = _load(RECEIPT)
    schema = _load(SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    mutations = []
    for section, field in (
        ("source_binding", "current_main_at_audit"),
        ("source_binding", "raw_sha256"),
        ("framework_binding", "commit"),
    ):
        hostile = copy.deepcopy(receipt)
        hostile[section][field] += "\n"
        mutations.append(hostile)
        hostile_integer = copy.deepcopy(receipt)
        hostile_integer[section][field] = 7
        mutations.append(hostile_integer)
    hostile_hash = copy.deepcopy(receipt)
    hostile_hash["artifact_hash"] += "\r\n"
    mutations.append(hostile_hash)
    hostile_authority = copy.deepcopy(receipt)
    hostile_authority["authority_contract"]["grants_framework_authority"] = True
    mutations.append(hostile_authority)
    hostile_classification = copy.deepcopy(receipt)
    hostile_classification["classification"] = "ARBITRARY_EXTENSION"
    mutations.append(hostile_classification)
    for hostile in mutations:
        assert list(validator.iter_errors(hostile))
