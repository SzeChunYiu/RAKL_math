from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework/RAKL"
RECEIPT = ROOT / "receipts/framework-pr153-hash-contract-migration-20260811.json"
SCHEMA = ROOT / "schemas/framework-pr153-hash-contract-migration.schema.json"
INVENTORY_EXTENSION_REGISTRY = (
    (
        ROOT / "receipts/framework-episode-inventory-extension-h4d1b-20260811.json",
        ROOT / "schemas/framework-episode-inventory-extension.schema.json",
    ),
    (
        ROOT / "receipts/framework-episode-inventory-extension-h4d1c-20260811.json",
        ROOT / "schemas/framework-episode-inventory-extension-h4d1c.schema.json",
    ),
)
INVENTORY_CLASSIFICATION_EXTENSION_REGISTRY = (
    (
        ROOT / "receipts/framework-episode-inventory-classification-extension-v2-ns-b1a3b1-r2-20260811.json",
        ROOT / "schemas/framework-episode-inventory-classification-extension-v2.schema.json",
    ),
    (
        ROOT / "receipts/framework-episode-inventory-classification-extension-v2-ns-b2a1c-r2-20260812.json",
        ROOT / "schemas/framework-episode-inventory-classification-extension-v2-ns-b2a1c-r2.schema.json",
    ),
)
OLD_FRAMEWORK = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
TARGET_FRAMEWORK = "9027cc6beab7e935d714bbdf8e902b89b50caaa8"
PROVISIONAL_FRAMEWORK = "3d4dde94ed8d6be04641b96ecf89389de55b61ce"
INVENTORY_COMMIT = "bd36e1661053a07b53af8f0b8bdf44da7c9d677e"
SUCCESSOR_COMMIT = "3bdd4718d3091661d9a7b007cb4bafe706650d5b"


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


def _historical_episode_content_bytes(value: dict) -> bytes:
    """Reproduce the exact TaskEpisode identity contract at framework 9027cc6."""

    fields = (
        "episode_id", "task_id", "atom_id", "context_hash",
        "problem_signature", "fibre_snapshot_hash", "operator_ids",
        "action_trace", "observation_ids", "verification_ids", "outcome",
        "residual_signature", "evidence_pointers", "timestamp", "cost",
    )
    payload = {field: value[field] for field in fields}
    return json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def _assert_current_schema_rejects_historical_episode(value: dict) -> None:
    schema = _load(FRAMEWORK / "schemas/task-episode.schema.json")
    assert "storage_admission" in schema["required"]
    assert "storage_admission" not in value
    errors = list(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value)
    )
    assert len(errors) == 1
    assert errors[0].validator == "required"
    assert errors[0].message == "'storage_admission' is a required property"


def _pointer(document: dict, pointer: str) -> dict:
    value: object = document
    for token in ([] if pointer == "/" else pointer.removeprefix("/").split("/")):
        assert isinstance(value, dict)
        value = value[token]
    assert isinstance(value, dict)
    return value


def _validated_inventory_extension_paths() -> set[str]:
    paths: set[str] = set()
    strict_schema = _schema_at(TARGET_FRAMEWORK, "task-episode.schema.json")
    for receipt_path, schema_path in INVENTORY_EXTENSION_REGISTRY:
        receipt = _load(receipt_path)
        schema = _load(schema_path)
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(
            schema, format_checker=FormatChecker()
        ).validate(receipt)
        assert receipt["artifact_hash"] == _canonical_hash(receipt)
        assert all(value is False for value in receipt["authority_contract"].values())

        parent = receipt["parent_inventory"]
        assert parent["merge_commit"] == "b18fcd35855d67962e28036f4a445ab24d0c4406"
        parent_line = _git(ROOT, "rev-list", "--parents", "-n", "1", parent["merge_commit"])
        assert isinstance(parent_line, str) and len(parent_line.split()) == 3
        parent_raw = _git(
            ROOT,
            "show",
            f'{parent["merge_commit"]}:{parent["receipt_path"]}',
            binary=True,
        )
        assert isinstance(parent_raw, bytes)
        assert parent["receipt_blob_at_merge"] == _git(
            ROOT, "rev-parse", f'{parent["merge_commit"]}:{parent["receipt_path"]}'
        )
        assert parent["receipt_file_sha256"] == "sha256:" + hashlib.sha256(parent_raw).hexdigest()
        assert json.loads(parent_raw)["artifact_hash"] == parent["receipt_artifact_hash"]

        source = receipt["source_binding"]
        failure = receipt["triggering_failure"]
        assert source["repository_url"] == "https://github.com/SzeChunYiu/RAKL_math.git"
        assert source["repository_url"] == _load(RECEIPT)["application_repository"]["repository"]
        assert source["current_main_at_audit"] == failure["head_sha"]
        assert _git(
            ROOT,
            "merge-base",
            "--is-ancestor",
            source["introduction_commit"],
            source["current_main_at_audit"],
        ) == ""
        assert source["introduction_tree"] == _git(
            ROOT, "rev-parse", f'{source["introduction_commit"]}^{{tree}}'
        )
        assert source["current_tree"] == _git(
            ROOT, "rev-parse", f'{source["current_main_at_audit"]}^{{tree}}'
        )
        intro_blob = _git(
            ROOT, "rev-parse", f'{source["introduction_commit"]}:{source["path"]}'
        )
        current_blob = _git(
            ROOT, "rev-parse", f'{source["current_main_at_audit"]}:{source["path"]}'
        )
        assert intro_blob == current_blob == source["git_blob_sha"]
        raw = _git(
            ROOT,
            "show",
            f'{source["current_main_at_audit"]}:{source["path"]}',
            binary=True,
        )
        assert isinstance(raw, bytes)
        assert raw == (ROOT / source["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == source["raw_sha256"]

        framework = receipt["framework_binding"]
        assert framework["commit"] == TARGET_FRAMEWORK
        assert framework["task_episode_schema_blob"] == _git(
            FRAMEWORK, "rev-parse", f'{TARGET_FRAMEWORK}:schemas/task-episode.schema.json'
        )
        assert framework["experience_substrate_blob"] == _git(
            FRAMEWORK, "rev-parse", f'{TARGET_FRAMEWORK}:src/rakl/experience_substrate.py'
        )
        value = json.loads(raw)
        Draft202012Validator(
            strict_schema, format_checker=FormatChecker()
        ).validate(value)
        digest = hashlib.sha256(_historical_episode_content_bytes(value)).hexdigest()
        assert digest == value["artifact_hash"]
        _assert_current_schema_rejects_historical_episode(value)
        assert receipt["runtime_binding"]["stored_hash"] == value["artifact_hash"]
        assert receipt["runtime_binding"]["computed_runtime_digest"] == digest
        paths.add(source["path"])
    for receipt_path, schema_path in INVENTORY_CLASSIFICATION_EXTENSION_REGISTRY:
        receipt = _load(receipt_path)
        schema = _load(schema_path)
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(
            schema, format_checker=FormatChecker()
        ).validate(receipt)
        assert receipt["artifact_hash"] == _canonical_hash(receipt)
        assert all(value is False for value in receipt["authority_contract"].values())
        audit = receipt["audit_binding"]
        assert audit["current_tree"] == _git(
            ROOT, "rev-parse", f'{audit["current_main_at_audit"]}^{{tree}}'
        )
        for item in receipt["classifications"]:
            assert item["classification"] in {
                "NON_TASK_EPISODE_CONTAINER_WITH_EPISODE_ID",
                "CURRENT_VALID_TASK_EPISODE_PROPOSAL_SHADOW",
            }
            assert item["git_blob_sha"] == item["current_main_blob_sha"]
            assert item["current_main_blob_sha"] == _git(
                ROOT,
                "rev-parse",
                f'{audit["current_main_at_audit"]}:{item["path"]}',
            )
            paths.add(item["path"])
    assert len(paths) == len(INVENTORY_EXTENSION_REGISTRY) + sum(
        len(_load(receipt_path)["classifications"])
        for receipt_path, _ in INVENTORY_CLASSIFICATION_EXTENSION_REGISTRY
    )
    return paths


def _validated_inventory_classification_extension_paths() -> set[str]:
    """Validate exact TaskEpisode/non-TaskEpisode container classifications."""

    paths: set[str] = set()
    for receipt_path, schema_path in INVENTORY_CLASSIFICATION_EXTENSION_REGISTRY:
        receipt = _load(receipt_path)
        schema = _load(schema_path)
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
        assert receipt["artifact_hash"] == _canonical_hash(receipt)
        assert all(value is False for value in receipt["authority_contract"].values())

        audit = receipt["audit_binding"]
        assert audit["repository_url"] == _load(RECEIPT)["application_repository"]["repository"]
        assert audit["current_tree"] == _git(ROOT, "rev-parse", f'{audit["current_main_at_audit"]}^{{tree}}')
        strict_schema = _schema_at(audit["framework_commit"], "task-episode.schema.json")
        assert audit["task_episode_schema_blob"] == _git(
            FRAMEWORK, "rev-parse", f'{audit["framework_commit"]}:schemas/task-episode.schema.json'
        )
        assert audit["experience_substrate_blob"] == _git(
            FRAMEWORK, "rev-parse", f'{audit["framework_commit"]}:src/rakl/experience_substrate.py'
        )
        for item in receipt["classifications"]:
            assert _git(ROOT, "merge-base", "--is-ancestor", item["introduction_commit"], audit["current_main_at_audit"]) == ""
            assert item["introduction_tree"] == _git(ROOT, "rev-parse", f'{item["introduction_commit"]}^{{tree}}')
            assert _git(ROOT, "merge-base", "--is-ancestor", item.get("current_version_commit", item["introduction_commit"]), audit["current_main_at_audit"]) == ""
            current_version_commit = item.get("current_version_commit", item["introduction_commit"])
            if "current_version_tree" in item:
                assert item["current_version_tree"] == _git(ROOT, "rev-parse", f'{current_version_commit}^{{tree}}')
            version_blob = _git(ROOT, "rev-parse", f'{current_version_commit}:{item["path"]}')
            current_blob = _git(ROOT, "rev-parse", f'{audit["current_main_at_audit"]}:{item["path"]}')
            assert version_blob == current_blob == item["git_blob_sha"] == item["current_main_blob_sha"]
            raw = _git(ROOT, "show", f'{audit["current_main_at_audit"]}:{item["path"]}', binary=True)
            assert isinstance(raw, bytes)
            assert raw == (ROOT / item["path"]).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == item["raw_sha256"]
            value = json.loads(raw)
            assert value["episode_id"] == item["observed_episode_id"]
            errors = list(Draft202012Validator(strict_schema, format_checker=FormatChecker()).iter_errors(value))
            if item["classification"] == "CURRENT_VALID_TASK_EPISODE_PROPOSAL_SHADOW":
                assert item["strict_task_episode_schema_verdict"] == "PASS"
                assert item["strict_task_episode_schema_error_count"] == len(errors) == 0
                assert item["runtime_constructor_invoked"] is True
                assert item["runtime_constructor_disposition"] == "EXACT_TASK_EPISODE_VALIDATION_PASS"
                assert value["storage_admission"] == "PROPOSAL_SHADOW_STORED"
                assert item["stored_hash"] == value["artifact_hash"]
                assert item["computed_runtime_digest"] == value["artifact_hash"]
            else:
                assert item["classification"] == "NON_TASK_EPISODE_CONTAINER_WITH_EPISODE_ID"
                assert item["strict_task_episode_schema_verdict"] == "FAIL"
                assert item["strict_task_episode_schema_error_count"] == len(errors) > 0
                assert item["runtime_constructor_invoked"] is False
                assert item["runtime_constructor_disposition"] == "NOT_APPLICABLE_NON_TASK_EPISODE_CONTAINER"
            paths.add(item["path"])
    assert len(paths) == sum(
        len(_load(receipt_path)["classifications"])
        for receipt_path, _ in INVENTORY_CLASSIFICATION_EXTENSION_REGISTRY
    )
    return paths


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
    assert transition["target_tree"] == _git(
        FRAMEWORK, "rev-parse", f"{TARGET_FRAMEWORK}^{{tree}}"
    )
    expected_framework_paths = {
        "schemas/task-episode.schema.json",
        "schemas/lesson.schema.json",
        "src/rakl/experience_substrate.py",
    }
    assert {item["path"] for item in transition["changed_blob_bindings"]} == expected_framework_paths
    for item in transition["changed_blob_bindings"]:
        assert item["previous_blob"] == _git(
            FRAMEWORK, "rev-parse", f'{OLD_FRAMEWORK}:{item["path"]}'
        )
        assert item["target_blob"] == _git(
            FRAMEWORK, "rev-parse", f'{TARGET_FRAMEWORK}:{item["path"]}'
        )
    application = receipt["application_repository"]
    assert application == {
        "repository": "https://github.com/SzeChunYiu/RAKL_math.git",
        "inventory_commit": INVENTORY_COMMIT,
        "inventory_tree": _git(ROOT, "rev-parse", f"{INVENTORY_COMMIT}^{{tree}}"),
        "migration_base": INVENTORY_COMMIT,
        "successor_commit": SUCCESSOR_COMMIT,
    }
    assert _git(ROOT, "merge-base", "--is-ancestor", INVENTORY_COMMIT, SUCCESSOR_COMMIT) == ""
    pin_migration = receipt["pin_migration"]
    assert pin_migration == {
        "previous_commit": OLD_FRAMEWORK,
        "provisional_target_commit": PROVISIONAL_FRAMEWORK,
        "final_merged_commit": TARGET_FRAMEWORK,
        "exact_application_suite_status": "PASS_EXACT_APPLICATION_SUITE_417_TESTS",
        "push_allowed": True,
    }
    pin = _load(ROOT / "config/rakl-framework-pin.json")
    current_gitlink = _git(ROOT, "rev-parse", "HEAD:framework/RAKL")
    current_framework = _git(FRAMEWORK, "rev-parse", "HEAD")
    assert pin["commit"] == current_gitlink == current_framework
    assert _git(
        FRAMEWORK,
        "merge-base",
        "--is-ancestor",
        TARGET_FRAMEWORK,
        current_framework,
    ) == ""
    assert all(value is False for value in receipt["authority_contract"].values())


def test_episode_inventory_is_the_exact_frozen_19_object_audit() -> None:
    receipt = _load(RECEIPT)
    inventory = receipt["episode_inventory"]
    expected_classifications = {
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_CANONICAL_RETROSPECTIVE_20260811.json": "HISTORICAL_SUPERSEDED_HASH_INVALID",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_CANONICAL_RETROSPECTIVE_V2_20260811.json": "CURRENT_SUCCESSOR_HASH_INVALID",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_SHADOW.json": "IMMUTABLE_NONCANONICAL_SHADOW",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_PLECTIC_TASK_EPISODE_CANONICAL_RETROSPECTIVE_20260811.json": "CURRENT_SUCCESSOR_HASH_INVALID",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_PLECTIC_TASK_EPISODE_SHADOW_20260811_R3.json": "IMMUTABLE_NONCANONICAL_SHADOW",
        "research/real_math/millennium/cross_problem/07_memory/XM005_RETROSPECTIVE_TASK_EPISODE_20260811.json": "CURRENT_VALID_RAW_EXACT",
        "research/real_math/millennium/navier_stokes/07_memory/NS-B1a3_C001_FAILURE_EXPERIENCE_DELTA_20260811.json": "NON_TASK_EPISODE_CONTAINER_WITH_EPISODE_ID",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a1_C001_TASK_EPISODE_CANONICAL_20260811.json": "CURRENT_SUCCESSOR_HASH_INVALID",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a1_C001_V3_TASK_EPISODE_20260811.json": "IMMUTABLE_NONCANONICAL_ORIGINAL_SUPERSEDED",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a2_C001_TASK_EPISODE_CANONICAL_20260811.json": "CURRENT_SUCCESSOR_HASH_INVALID",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a2_C001_V3_TASK_EPISODE_20260811.json": "IMMUTABLE_NONCANONICAL_ORIGINAL_SUPERSEDED",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a3_C001_V3_TASK_EPISODE_20260811.json": "IMMUTABLE_NONCANONICAL_INCOMPLETE_TELEMETRY",
        "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1a1a_V3_TASK_EPISODE_SHADOW_20260811.json": "IMMUTABLE_NONCANONICAL_SHADOW",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1b_TASK_EPISODE_20260811.json": "IMMUTABLE_NONCANONICAL_RICH_TASK_EPISODE_RECORD",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_TASK_EPISODE_CANONICAL_20260811.json": "HISTORICAL_SUPERSEDED_HASH_INVALID",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_20260811.json": "CURRENT_VALID_RAW_EXACT",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1a_TASK_EPISODE_CANONICAL_20260811.json": "CURRENT_VALID_RAW_EXACT",
        "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_002_SUZUKI_FAITHFULNESS_TASK_EPISODE_20260811.json": "CURRENT_HASH_INVALID",
        "research/real_math/millennium/yang_mills/07_memory/YM-S1A1_DENSE_SOURCE_TASK_EPISODE_20260811.json": "IMMUTABLE_APPLICATION_EXTENDED_PROPOSAL_NOT_CORE_TASK_EPISODE",
    }
    expected_paths = set(expected_classifications)
    assert len(inventory) == 19
    assert {item["path"] for item in inventory} == expected_paths
    assert {item["path"]: item["classification"] for item in inventory} == expected_classifications
    expected_corrections = {
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_CANONICAL_RETROSPECTIVE_20260811.json": ["research/real_math/millennium/birch_swinnerton_dyer/08_reviews/BSD_A1a1_PR83_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"],
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_CANONICAL_RETROSPECTIVE_V2_20260811.json": ["research/real_math/millennium/birch_swinnerton_dyer/08_reviews/BSD_A1a1_PR83_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"],
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_PLECTIC_TASK_EPISODE_CANONICAL_RETROSPECTIVE_20260811.json": ["research/real_math/millennium/birch_swinnerton_dyer/08_reviews/BSD_A1a1_PR96_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"],
        "research/real_math/millennium/cross_problem/07_memory/XM005_RETROSPECTIVE_TASK_EPISODE_20260811.json": ["research/real_math/millennium/cross_problem/08_reviews/XM005_PR71_OPEN_HEAD_RETROSPECTIVE_ASSURANCE_20260811.json"],
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a1_C001_TASK_EPISODE_CANONICAL_20260811.json": ["research/real_math/millennium/navier_stokes/10_case_study/NS-B1a1_C001_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"],
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a2_C001_TASK_EPISODE_CANONICAL_20260811.json": ["research/real_math/millennium/navier_stokes/10_case_study/NS-B1a2_C001_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"],
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_TASK_EPISODE_CANONICAL_20260811.json": ["research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_PR104_TASK_EPISODE_HASH_CORRECTION_20260811.json"],
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_20260811.json": ["research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_PR104_TASK_EPISODE_HASH_CORRECTION_20260811.json"],
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1a_TASK_EPISODE_CANONICAL_20260811.json": ["research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1a_PR78_SUCCESSOR_ASSURANCE_CORRECTION_20260811.json"],
    }
    assert {
        item["path"]: item["prior_correction_paths"]
        for item in inventory if item["prior_correction_paths"]
    } == expected_corrections
    discovered = set()
    for path in (ROOT / "research").rglob("*.json"):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and "episode_id" in value:
            discovered.add(str(path.relative_to(ROOT)))
    successor_paths = {item["successor_path"] for item in receipt["successor_bindings"]}
    extension_paths = _validated_inventory_extension_paths()
    classification_extension_paths = _validated_inventory_classification_extension_paths()
    assert discovered == expected_paths | successor_paths | extension_paths | classification_extension_paths
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
            assert item["computed_runtime_digest"] == hashlib.sha256(
                _historical_episode_content_bytes(value)
            ).hexdigest()
        for correction_path in item["prior_correction_paths"]:
            assert _git(ROOT, "cat-file", "-e", f"{INVENTORY_COMMIT}:{correction_path}") == ""

    inventoried_successors = {
        item["successor_path"]: item["successor_hash"]
        for item in inventory if item["successor_path"] is not None
    }
    assert inventoried_successors == {
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_V3_20260811.json": "739810624ada5182b932e3b0d17b4acf429a483a136e99ebc93cd8b51d0ff310",
        "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a1_PLECTIC_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_V2_20260811.json": "eac326b757026bf4007f868c93a62f34f6738e29ea3575c5c26d968b393da95c",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a1_C001_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_V2_20260811.json": "0c71cf1a9f51389634b7a951f0a79f591b01e485ea106240dda54dea7f4e17b6",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a2_C001_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_V2_20260811.json": "5ad891912107c2b25645c1da5aff399d061c4f74bf8a813ff778869e9903c6d0",
        "research/real_math/millennium/p_vs_np/10_case_study/O9d12a2a1a1_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_20260811.json": "aa0a0a4a04e90d9b641cb9e302cc91fb4797e84bab37b11f8f747c07766e017e",
        "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_002_SUZUKI_FAITHFULNESS_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_V2_20260811.json": "3a1978d939947a84627310c4fcc29d9c0b4484206c6c41b839bc7f635183c948",
    }
    for successor_path, successor_hash in inventoried_successors.items():
        successor = _load(ROOT / successor_path)
        assert successor["artifact_hash"] == successor_hash


def test_five_successors_change_only_hash_identity_and_pass_strict_runtime() -> None:
    receipt = _load(RECEIPT)
    strict_schema = _schema_at(TARGET_FRAMEWORK, "task-episode.schema.json")
    assert len(receipt["successor_bindings"]) == 5
    inventory_crosslinks = {
        item["successor_path"]: item["successor_hash"]
        for item in receipt["episode_inventory"] if item["successor_path"] is not None
    }
    for item in receipt["successor_bindings"]:
        assert item["parent_source_commit"] == INVENTORY_COMMIT
        parent = json.loads(
            _git(ROOT, "show", f'{item["parent_source_commit"]}:{item["parent_path"]}')
        )
        successor = _load(ROOT / item["successor_path"])
        assert item["parent_blob"] == _git(
            ROOT, "rev-parse", f'{item["parent_source_commit"]}:{item["parent_path"]}'
        )
        assert item["parent_stored_hash"] == parent["artifact_hash"]
        assert item["successor_commit"] == SUCCESSOR_COMMIT
        successor_raw = _git(
            ROOT, "show", f'{item["successor_commit"]}:{item["successor_path"]}', binary=True
        )
        assert isinstance(successor_raw, bytes)
        assert item["successor_file_sha256"] == "sha256:" + hashlib.sha256(successor_raw).hexdigest()
        parent_semantic = copy.deepcopy(parent)
        successor_semantic = copy.deepcopy(successor)
        parent_semantic.pop("artifact_hash")
        successor_semantic.pop("artifact_hash")
        assert parent_semantic == successor_semantic
        assert item["semantic_payload_changed"] is False
        assert item["authority_changed"] is False
        assert successor["artifact_hash"] == item["successor_raw_digest"]
        assert inventory_crosslinks[item["successor_path"]] == item["successor_raw_digest"]
        Draft202012Validator(strict_schema, format_checker=FormatChecker()).validate(successor)
        assert hashlib.sha256(_historical_episode_content_bytes(successor)).hexdigest() == item["successor_raw_digest"]
        _assert_current_schema_rejects_historical_episode(successor)
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
