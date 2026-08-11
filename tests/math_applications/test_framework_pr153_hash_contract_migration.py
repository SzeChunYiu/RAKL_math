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
RECEIPT = ROOT / "receipts/framework-pr153-hash-contract-migration-20260811.json"
SCHEMA = ROOT / "schemas/framework-pr153-hash-contract-migration.schema.json"
OLD_FRAMEWORK = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
TARGET_FRAMEWORK = "9027cc6beab7e935d714bbdf8e902b89b50caaa8"


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


def _schema_at(commit: str, name: str) -> dict:
    raw = _git(FRAMEWORK, "show", f"{commit}:schemas/{name}", binary=True)
    assert isinstance(raw, bytes)
    value = json.loads(raw)
    assert isinstance(value, dict)
    return value


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


def _pointer(document: dict, pointer: str) -> dict:
    value: object = document
    for token in ([] if pointer == "/" else pointer.removeprefix("/").split("/")):
        assert isinstance(value, dict)
        value = value[token]
    assert isinstance(value, dict)
    return value


def test_receipt_schema_hash_framework_pin_and_non_authority_are_exact() -> None:
    receipt = _load(RECEIPT)
    schema = _load(SCHEMA)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    transition = receipt["framework_transition"]
    assert transition["previous_commit"] == OLD_FRAMEWORK
    assert transition["target_commit"] == TARGET_FRAMEWORK
    assert transition["status"] == "MERGED_FRAMEWORK_MAIN"
    pin = _load(ROOT / "config/rakl-framework-pin.json")
    assert pin["commit"] == TARGET_FRAMEWORK
    assert _git(ROOT, "rev-parse", "HEAD:framework/RAKL") == TARGET_FRAMEWORK
    assert _git(FRAMEWORK, "rev-parse", "HEAD") == TARGET_FRAMEWORK
    assert all(value is False for value in receipt["authority_contract"].values())


def test_episode_inventory_is_the_exact_frozen_19_object_audit() -> None:
    receipt = _load(RECEIPT)
    inventory = receipt["episode_inventory"]
    expected_paths = {
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_CANONICAL_RETROSPECTIVE_20260811.json",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_CANONICAL_RETROSPECTIVE_V2_20260811.json",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_SHADOW.json",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_PLECTIC_TASK_EPISODE_CANONICAL_RETROSPECTIVE_20260811.json",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_PLECTIC_TASK_EPISODE_SHADOW_20260811_R3.json",
        "research/real_math/millennium/cross_problem/07_memory/XM005_RETROSPECTIVE_TASK_EPISODE_20260811.json",
        "research/real_math/millennium/navier_stokes/07_memory/NS-B1a3_C001_FAILURE_EXPERIENCE_DELTA_20260811.json",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a1_C001_TASK_EPISODE_CANONICAL_20260811.json",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a1_C001_V3_TASK_EPISODE_20260811.json",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a2_C001_TASK_EPISODE_CANONICAL_20260811.json",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a2_C001_V3_TASK_EPISODE_20260811.json",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a3_C001_V3_TASK_EPISODE_20260811.json",
        "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1a1a_V3_TASK_EPISODE_SHADOW_20260811.json",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1b_TASK_EPISODE_20260811.json",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_TASK_EPISODE_CANONICAL_20260811.json",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_20260811.json",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1a_TASK_EPISODE_CANONICAL_20260811.json",
        "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_002_SUZUKI_FAITHFULNESS_TASK_EPISODE_20260811.json",
        "research/real_math/millennium/yang_mills/07_memory/YM-S1A1_DENSE_SOURCE_TASK_EPISODE_20260811.json",
    }
    assert len(inventory) == 19
    assert {item["path"] for item in inventory} == expected_paths
    discovered = set()
    for path in (ROOT / "research").rglob("*.json"):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and "episode_id" in value:
            discovered.add(str(path.relative_to(ROOT)))
    successor_paths = {item["successor_path"] for item in receipt["successor_bindings"]}
    assert discovered == expected_paths | successor_paths
    old_schema = _schema_at(OLD_FRAMEWORK, "task-episode.schema.json")
    new_schema = _schema_at(TARGET_FRAMEWORK, "task-episode.schema.json")
    for item in inventory:
        raw = _git(ROOT, "show", f'{item["source_commit"]}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert raw == (ROOT / item["path"]).read_bytes()
        assert item["git_blob_sha"] == _git(
            ROOT, "rev-parse", f'{item["source_commit"]}:{item["path"]}'
        )
        assert item["file_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
        value = json.loads(raw)
        for schema, key in [(old_schema, "old_schema_verdict"), (new_schema, "new_schema_verdict")]:
            errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value))
            assert item[key] == {
                "verdict": "PASS" if not errors else "FAIL",
                "error_count": len(errors),
            }
        if item["computed_runtime_digest"] is not None:
            runtime = _episode(value)
            assert item["computed_runtime_digest"] == hashlib.sha256(
                episode_content_bytes(runtime)
            ).hexdigest()


def test_five_successors_change_only_hash_identity_and_pass_strict_runtime() -> None:
    receipt = _load(RECEIPT)
    strict_schema = _schema_at(TARGET_FRAMEWORK, "task-episode.schema.json")
    assert len(receipt["successor_bindings"]) == 5
    for item in receipt["successor_bindings"]:
        parent = json.loads(
            _git(ROOT, "show", f'{item["parent_source_commit"]}:{item["parent_path"]}')
        )
        successor = _load(ROOT / item["successor_path"])
        parent_semantic = copy.deepcopy(parent)
        successor_semantic = copy.deepcopy(successor)
        parent_semantic.pop("artifact_hash")
        successor_semantic.pop("artifact_hash")
        assert parent_semantic == successor_semantic
        assert item["semantic_payload_changed"] is False
        assert item["authority_changed"] is False
        assert successor["artifact_hash"] == item["successor_raw_digest"]
        Draft202012Validator(strict_schema, format_checker=FormatChecker()).validate(successor)
        runtime = _episode(successor)
        assert validate_episode(runtime) == ()
        assert hashlib.sha256(episode_content_bytes(runtime)).hexdigest() == item["successor_raw_digest"]
        assert item["successor_blob"] == _git(
            ROOT, "rev-parse", f'{item["successor_commit"]}:{item["successor_path"]}'
        )


def test_all_eight_lesson_like_objects_remain_non_lesson_proposals() -> None:
    receipt = _load(RECEIPT)
    entries = receipt["lesson_like_inventory"]
    expected = {
        ("research/real_math/millennium/cross_problem/10_study_pattern/LESSON_PROPOSAL_EXAMPLE_20260811.json", "/"),
        ("research/real_math/millennium/navier_stokes/07_memory/NS-B1a3_C001_FAILURE_EXPERIENCE_DELTA_20260811.json", "/lesson_proposal"),
        ("research/real_math/millennium/p_vs_np/05_falsification/C025_SYNTHESIS_RECEIPT_20260811.json", "/method_lesson"),
        ("research/real_math/millennium/p_vs_np/05_falsification/C025_SYNTHESIS_RECEIPT_V2_20260811.json", "/method_lesson"),
        ("research/real_math/millennium/p_vs_np/07_memory/C025_POSTRESULT_ASSURANCE_ADDENDUM_20260811.json", "/method_lesson_candidate"),
        ("research/real_math/millennium/p_vs_np/07_memory/C025_POSTRESULT_ASSURANCE_ADDENDUM_V2_20260811.json", "/method_lesson_candidate"),
        ("research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1a1a_LESSON_PROPOSAL_SHADOW_20260811.json", "/"),
        ("research/real_math/millennium/yang_mills/07_memory/YM-S1A1_DENSE_SOURCE_TASK_EPISODE_20260811.json", "/reusable_lesson_proposal"),
    }
    assert {(item["path"], item["pointer"]) for item in entries} == expected
    lesson_schema = _schema_at(TARGET_FRAMEWORK, "lesson.schema.json")
    for item in entries:
        raw = _git(ROOT, "show", f'{item["source_commit"]}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert raw == (ROOT / item["path"]).read_bytes()
        value = _pointer(json.loads(raw), item["pointer"])
        errors = list(Draft202012Validator(lesson_schema).iter_errors(value))
        assert errors
        assert item["missing_framework_lesson_fields"]
        assert item["classification"] == "NOT_FRAMEWORK_LESSON_PROPOSAL_ONLY"
        assert item["authority"] == "PROPOSAL_ONLY"
