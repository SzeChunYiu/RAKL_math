from __future__ import annotations

import copy
from dataclasses import replace
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

from rakl.experience_substrate import (
    EpisodeOutcome,
    TaskEpisode,
    episode_content_bytes,
    validate_episode,
)


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
PR_BASE = "3ccdcc51aa312af8b8288ff7cf6f4a681966d1fd"
PR_HEAD = "ce3a6dfc2af3c5c3e7fc93616e3fd774097e4d9b"
PR_HEAD_TREE = "d70575ff2ad8d4c6277eac6fedbe050676b24d7a"
INTEGRATION_BASE = "24194bba4c88cc4be19dad03d59bfa79599d5ee9"
INTEGRATION_MERGE = "ac205c8b50f3db4ea2d8f186b81c99acb3c0142f"
FRAMEWORK = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"

CORRECTION = PNP / "10_case_study/O9d12a2a1a1a_PR78_SUCCESSOR_ASSURANCE_CORRECTION_20260811.json"
EPISODE = PNP / "10_case_study/O9d12a2a1a1a_TASK_EPISODE_CANONICAL_20260811.json"
SCHEMA = ROOT / "schemas/pnp-pr78-successor-assurance-correction.schema.json"
SHADOW = PNP / "09_trace/O9d12a2a1a1a_V3_TASK_EPISODE_SHADOW_20260811.json"
LESSON = PNP / "07_memory/O9d12a2a1a1a_LESSON_PROPOSAL_SHADOW_20260811.json"
PR104_EPISODE = PNP / "10_case_study/O9d12a2a1a1_TASK_EPISODE_CANONICAL_20260811.json"
PR104_EPISODE_SUCCESSOR = PNP / "10_case_study/O9d12a2a1a1_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_20260811.json"
PR104_HASH_CORRECTION = PNP / "10_case_study/O9d12a2a1a1_PR104_TASK_EPISODE_HASH_CORRECTION_20260811.json"
PR104_HASH_SCHEMA = ROOT / "schemas/pnp-pr104-task-episode-hash-correction.schema.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _git(*args: str, binary: bool = False) -> str | bytes:
    completed = subprocess.run(
        ["git", "-C", str(ROOT), *args], check=True, capture_output=True,
        text=not binary,
    )
    return completed.stdout if binary else completed.stdout.strip()


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _deleted_field_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    del payload["artifact_hash"]
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
    return parsed


def _validate(value: dict, schema_path: Path) -> None:
    schema = _load(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(value)


def _episode(value: dict) -> TaskEpisode:
    return TaskEpisode(
        episode_id=value["episode_id"], task_id=value["task_id"],
        atom_id=value["atom_id"], context_hash=value["context_hash"],
        problem_signature=tuple(value["problem_signature"]),
        fibre_snapshot_hash=value["fibre_snapshot_hash"],
        operator_ids=tuple(value["operator_ids"]),
        action_trace=tuple(value["action_trace"]),
        observation_ids=tuple(value["observation_ids"]),
        verification_ids=tuple(value["verification_ids"]),
        outcome=EpisodeOutcome(value["outcome"]),
        residual_signature=tuple(value["residual_signature"]),
        evidence_pointers=tuple(value["evidence_pointers"]),
        artifact_hash=value["artifact_hash"], timestamp=value["timestamp"],
        cost=value["cost"],
    )


def test_pr78_history_is_integrated_without_rewriting_any_of_six_added_files() -> None:
    receipt = _load(CORRECTION)
    assert _git("rev-parse", f"{PR_HEAD}^{{tree}}") == PR_HEAD_TREE
    assert _git("show", "-s", "--format=%P", INTEGRATION_MERGE).split() == [
        INTEGRATION_BASE, PR_HEAD
    ]
    paths = _git("diff", "--diff-filter=A", "--name-only", PR_BASE, PR_HEAD).splitlines()
    assert len(paths) == 6
    assert {item["path"] for item in receipt["preserved_artifacts"]} == set(paths)
    for item in receipt["preserved_artifacts"]:
        historical = _git("show", f"{PR_HEAD}:{item['path']}", binary=True)
        assert historical == (ROOT / item["path"]).read_bytes()
        assert _git("rev-parse", f"{PR_HEAD}:{item['path']}") == item["git_blob_sha"]
        assert "sha256:" + hashlib.sha256(historical).hexdigest() == item["content_sha256"]


def test_shadow_objects_are_explicitly_noncanonical_and_proposal_only() -> None:
    receipt = _load(CORRECTION)
    shadow = _load(SHADOW)
    lesson = _load(LESSON)
    task_schema = _load(ROOT / "framework/RAKL/schemas/task-episode.schema.json")
    shadow_errors = list(Draft202012Validator(task_schema).iter_errors(shadow))
    assert len(shadow_errors) == receipt["shadow_audit"]["task_episode_schema_error_count"]
    assert len(shadow_errors) > 0
    assert shadow["status"] == lesson["status"] == "PROPOSAL_ONLY"
    assert shadow["chronology"]["pre_candidate_credit"] is False
    assert shadow["chronology"]["fresh_child_context_frozen_before_result"] is False
    assert shadow["authority_contract"]["grants_framework_authority"] is False
    assert lesson["authority_contract"]["grants_framework_authority"] is False
    assert shadow["artifact_hash"] == _deleted_field_hash(shadow)
    assert lesson["artifact_hash"] == _deleted_field_hash(lesson)


def test_shadow_source_binding_defect_and_future_timestamp_are_preserved() -> None:
    receipt = _load(CORRECTION)
    shadow = _load(SHADOW)
    bindings = receipt["shadow_audit"]["source_binding_findings"]
    assert len(bindings) == 2
    for finding, binding in zip(bindings, shadow["source_bindings"], strict=True):
        actual_blob = _git("rev-parse", f"{binding['commit_sha']}:{binding['path']}")
        actual_content = _git("show", f"{binding['commit_sha']}:{binding['path']}", binary=True)
        actual_sha256 = "sha256:" + hashlib.sha256(actual_content).hexdigest()
        assert finding == {
            "path": binding["path"],
            "recorded_git_blob_sha": binding["git_blob_sha"],
            "actual_git_blob_sha": actual_blob,
            "recorded_content_sha256": (
                binding["content_sha256"]
                if binding["content_sha256"].startswith("sha256:")
                else "sha256:" + binding["content_sha256"]
            ),
            "actual_content_sha256": actual_sha256,
            "binding_valid": (
                binding["git_blob_sha"] == actual_blob
                and binding["content_sha256"].removeprefix("sha256:")
                == actual_sha256.removeprefix("sha256:")
            ),
        }
    assert [item["binding_valid"] for item in bindings] == [False, True]
    chronology = receipt["chronology_audit"]
    assert chronology["checked_timestamp_count"] == 2
    assert chronology["future_dated_claim_count"] == 1
    finding = chronology["future_dated_claims"][0]
    assert finding["path"] == str(LESSON.relative_to(ROOT))
    assert finding["pointer"] == "/recorded_at_utc"
    assert finding["timestamp"] == "2026-08-11T11:10:00Z"
    assert finding["introduced_commit_time"] == "2026-08-11T13:09:42+02:00"
    assert (_parse_time(finding["timestamp"]) - _parse_time(
        finding["introduced_commit_time"]
    )).total_seconds() == 18


def test_merged_pr104_prefixed_hash_bypass_is_preserved_and_recorded() -> None:
    receipt = _load(CORRECTION)
    historical = _episode(_load(PR104_EPISODE))
    actual_digest = hashlib.sha256(episode_content_bytes(historical)).hexdigest()
    assert len(historical.artifact_hash) == 71
    assert historical.artifact_hash != "sha256:" + actual_digest
    assert validate_episode(historical) == ()
    assert receipt["framework_gap_audit"] == {
        "gap_id": "FG-BD1A276-TASK-EPISODE-PREFIXED-HASH-BYPASS",
        "framework_commit": FRAMEWORK,
        "historical_episode_path": str(PR104_EPISODE.relative_to(ROOT)),
        "historical_recorded_hash": historical.artifact_hash,
        "historical_runtime_content_digest": actual_digest,
        "historical_validate_episode_result": [],
        "root_cause": "validate_episode verifies content only when artifact_hash length equals 64 while task-episode.schema.json accepts any nonempty string",
        "disposition": "PRESERVE_HISTORY_AND_USE_RAW_64_HEX_RUNTIME_HASH_FOR_SUCCESSOR",
        "grants_framework_change_authority": False,
    }


def test_pr104_versioned_runtime_hash_successor_is_exact_and_fail_closed() -> None:
    correction = _load(PR104_HASH_CORRECTION)
    _validate(correction, PR104_HASH_SCHEMA)
    assert correction["artifact_hash"] == _canonical_hash(correction)
    historical = _episode(_load(PR104_EPISODE))
    successor = _episode(_load(PR104_EPISODE_SUCCESSOR))
    expected = "aa0a0a4a04e90d9b641cb9e302cc91fb4797e84bab37b11f8f747c07766e017e"
    assert hashlib.sha256(episode_content_bytes(historical)).hexdigest() == expected
    assert successor.artifact_hash == expected
    assert episode_content_bytes(successor) == episode_content_bytes(historical)
    assert validate_episode(successor) == ()
    assert correction["historical"]["computed_episode_content_digest"] == expected
    assert correction["successor"]["artifact_hash"] == expected
    assert correction["authority_contract"] == {
        "effective_authority": "RUNTIME_HASH_IDENTITY_CORRECTION_ONLY",
        "grants_new_mathematical_result": False,
        "grants_strict_discovery_credit": False,
        "grants_proof_authority": False,
        "grants_p_vs_np_root_authority": False,
        "grants_theorem_authority": False,
        "grants_novelty_authority": False,
        "grants_framework_authority": False,
        "grants_review_independence": False,
    }
    hostile = replace(successor, task_id="forged-authority")
    assert validate_episode(hostile) == ("episode:artifact_hash_mismatch",)


@pytest.mark.parametrize(
    "field",
    [
        "grants_new_mathematical_result",
        "grants_strict_discovery_credit",
        "grants_p_vs_np_root_authority",
        "grants_theorem_authority",
        "grants_framework_authority",
        "grants_review_independence",
    ],
)
def test_pr104_hash_correction_authority_escalation_is_rejected(field: str) -> None:
    forged = copy.deepcopy(_load(PR104_HASH_CORRECTION))
    forged["authority_contract"][field] = True
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(PR104_HASH_SCHEMA)).validate(forged)


def test_canonical_retrospective_episode_is_runtime_and_schema_valid() -> None:
    episode = _load(EPISODE)
    _validate(episode, ROOT / "framework/RAKL/schemas/task-episode.schema.json")
    episode_object = _episode(episode)
    assert len(episode_object.artifact_hash) == 64
    assert episode_object.artifact_hash == hashlib.sha256(
        episode_content_bytes(episode_object)
    ).hexdigest()
    assert validate_episode(episode_object) == ()
    hostile_mutation = replace(
        episode_object,
        action_trace=episode_object.action_trace + ("forged authority escalation",),
    )
    assert validate_episode(hostile_mutation) == ("episode:artifact_hash_mismatch",)


def test_correction_is_fail_closed_and_keeps_child_candidate_gate_closed() -> None:
    correction = _load(CORRECTION)
    _validate(correction, SCHEMA)
    assert correction["artifact_hash"] == _canonical_hash(correction)
    assert correction["correction"] == {
        "historical_bytes_mutated": False,
        "repairs_original_chronology": False,
        "strict_discovery_credit": "NO_STRICT_DISCOVERY_CREDIT",
        "lesson_disposition": "QUARANTINED_PROPOSAL_ONLY",
        "retained_local_result": "FIXED_LAMBDA_ANTECEDENT_MEMBERSHIP_CONGRUENCE",
    }
    assert correction["prospective_gate"]["atom_id"] == "O9d12a2a1a1b"
    assert correction["prospective_gate"]["candidate_generation_allowed"] is False
    assert correction["authority_contract"] == {
        "effective_authority": "RETROSPECTIVE_SCOPED_ROUTE_PRUNING_ONLY",
        "grants_strict_discovery_credit": False,
        "grants_proof_authority": False,
        "grants_p_vs_np_root_authority": False,
        "grants_theorem_authority": False,
        "grants_novelty_authority": False,
        "grants_framework_authority": False,
        "grants_review_independence": False,
        "may_backfill_chronology": False,
    }
    candidate_dir = PNP / "04_candidates"
    candidates = list(candidate_dir.glob("*O9d12a2a1a1b*")) if candidate_dir.exists() else []
    assert candidates == []


@pytest.mark.parametrize(
    ("section", "field", "value"),
    [
        ("authority_contract", "grants_strict_discovery_credit", True),
        ("authority_contract", "grants_p_vs_np_root_authority", True),
        ("authority_contract", "grants_theorem_authority", True),
        ("authority_contract", "grants_framework_authority", True),
        ("authority_contract", "grants_review_independence", True),
        ("authority_contract", "may_backfill_chronology", True),
        ("prospective_gate", "candidate_generation_allowed", True),
    ],
)
def test_hostile_authority_escalation_is_schema_rejected(
    section: str, field: str, value: object
) -> None:
    forged = copy.deepcopy(_load(CORRECTION))
    forged[section][field] = value
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(SCHEMA)).validate(forged)


def test_framework_and_successor_hash_bindings_are_exact() -> None:
    correction = _load(CORRECTION)
    assert _git("rev-parse", "HEAD:framework/RAKL") == FRAMEWORK
    assert correction["framework_authority"]["commit"] == FRAMEWORK
    for item in correction["successors"]:
        path = ROOT / item["path"]
        if item["hash_mode"] == "EMBEDDED_SELF_HASH":
            assert item["artifact_hash"] == "sha256:" + _load(path)["artifact_hash"]
        else:
            assert item["hash_mode"] == "FILE_SHA256"
            assert item["artifact_hash"] == _file_hash(path)
