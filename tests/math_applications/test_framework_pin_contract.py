from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema
import rakl


APPLICATION_ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = Path(rakl.__file__).resolve().parents[2]
EXPECTED_FRAMEWORK_COMMIT = "bfa2d65987ba5d3e46db1196ef56d1432f115f99"
HISTORICAL_F224_FRAMEWORK_COMMIT = "f224d91d9fbd2844a89921ca4a30b77a7954ecd2"
HISTORICAL_4EE_FRAMEWORK_COMMIT = "4ee5e9afe77870c684b798e0ed4c9fcee62a4365"
HISTORICAL_FRAMEWORK_COMMIT = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
FINAL_SYNC_RECEIPT = (
    APPLICATION_ROOT / "receipts/framework-pin-final-integration-bd1a276-20260811.json"
)
CURRENT_MAIN_SYNC_RECEIPT = (
    APPLICATION_ROOT / "receipts/framework-pin-sync-4ee5e9a-20260811.json"
)
FINAL_CURRENT_MAIN_SYNC_RECEIPT = (
    APPLICATION_ROOT / "receipts/framework-pin-sync-f224d91-20260811.json"
)


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_machine_readable_framework_pin_is_valid_and_loaded_exactly() -> None:
    pin = json.loads(
        (APPLICATION_ROOT / "config/rakl-framework-pin.json").read_text(
            encoding="utf-8"
        )
    )
    schema = json.loads(
        (APPLICATION_ROOT / "schemas/rakl-framework-pin.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(pin)

    assert pin["commit"] == EXPECTED_FRAMEWORK_COMMIT
    gitlink_commit = subprocess.run(
        [
            "git",
            "-C",
            str(APPLICATION_ROOT),
            "rev-parse",
            "HEAD:framework/RAKL",
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    assert gitlink_commit == pin["commit"]

    loaded_commit = subprocess.run(
        ["git", "-C", str(FRAMEWORK_ROOT), "rev-parse", "HEAD"],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    assert loaded_commit == pin["commit"]
    framework_status = subprocess.run(
        ["git", "-C", str(FRAMEWORK_ROOT), "status", "--porcelain"],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout
    assert framework_status == ""
    assert pin["authority"] == (
        "Dependency synchronization to exact clean RAKL origin/main bfa2d65987ba5d3e46db1196ef56d1432f115f99 observed 2026-08-12; "
        "mathematical/core workflow and C041 gate APIs are unchanged from 91f182a while later non-mathematical overlays are included; "
        "no proof, research, review-independence, or method-evolution authority"
    )


def test_framework_pin_sync_receipt_is_exact_and_non_authorizing() -> None:
    receipt = json.loads(
        (
            APPLICATION_ROOT
            / "receipts/framework-pin-sync-bd1a276-20260811.json"
        ).read_text(encoding="utf-8")
    )
    payload = copy.deepcopy(receipt)
    payload["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(payload)
    assert receipt["previous_framework_commit"] == HISTORICAL_FRAMEWORK_COMMIT
    assert receipt["current_framework_commit"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert receipt["verification"] == {
        "command": "python tools/run_application_tests.py --framework framework/RAKL",
        "tests_passed": 302,
        "exit_code": 0,
        "pin_equals_gitlink": True,
        "framework_authority_paths_clean": True,
        "status": "PASS_EXACT_APPLICATION_SUITE",
    }
    assert receipt["verdict"] == "PASS_APPLICATION_CONFORMANCE_ON_EXACT_FRAMEWORK_PIN"
    assert "NO_MATHEMATICAL_AUTHORITY_CHANGE" in receipt["authority"]
    compatibility = receipt["semantic_authority_compatibility"]
    assert compatibility["historical_artifacts_keep_recorded_framework_commits"] is True
    assert compatibility["historical_receipts_or_outputs_rewritten"] is False
    assert compatibility["new_execution_pin_applies_prospectively"] is True

    refresh = receipt["integration_refresh"]
    assert refresh["pre_refresh_pr_head"] == (
        "bfc9bc1c63cc0e8fffa583afef3b02f0e8085792"
    )
    assert refresh["merged_live_main_commit"] == (
        "2ddb51359292fd9638116b488ffff9a04397446b"
    )
    assert refresh["merged_live_main_tree"] == (
        "bc69a20f525cb74d547bb42055bf263ffc073110"
    )
    assert refresh["local_integration_merge_commit"] == (
        "02aa447d8eb77b0d274465e1928968d7ed480b63"
    )
    assert refresh["prerequisite_merges"] == {
        "pr79_merge": "d13bb40fab2448f983a73f5964ab2d3fd2db489c",
        "pr84_merge": "2ddb51359292fd9638116b488ffff9a04397446b",
    }
    assert refresh["historical_artifact_files_changed"] == []
    assert refresh["exact_suite_after_refresh"] == {
        "command": "python tools/run_application_tests.py --framework framework/RAKL",
        "tests_passed": 302,
        "exit_code": 0,
        "status": "PASS_EXACT_APPLICATION_SUITE_AFTER_LIVE_MAIN_REFRESH",
    }
    # Preserve the pushed predecessor as negative chronology/count history.
    assert receipt["framework_changed_files"] == 638
    assert datetime.fromisoformat(receipt["recorded_at"]) < datetime.fromisoformat(
        refresh["refreshed_at"]
    )

    historical_binding = receipt["historical_pin_receipt_binding"]
    historical_bytes = subprocess.run(
        [
            "git",
            "-C",
            str(APPLICATION_ROOT),
            "show",
            f"{historical_binding['application_commit']}:{historical_binding['path']}",
        ],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    assert "sha256:" + hashlib.sha256(historical_bytes).hexdigest() == (
        historical_binding["raw_sha256"]
    )
    historical = json.loads(historical_bytes)
    assert historical["current_framework_commit"] == HISTORICAL_FRAMEWORK_COMMIT
    assert historical["artifact_hash"] == historical_binding["artifact_hash"]


def test_final_framework_pin_integration_receipt_has_exact_counts_and_chronology() -> None:
    receipt = json.loads(FINAL_SYNC_RECEIPT.read_text(encoding="utf-8"))
    schema = json.loads(
        (
            APPLICATION_ROOT
            / "schemas/framework-pin-final-integration-receipt.schema.json"
        ).read_text(encoding="utf-8")
    )
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(receipt)
    payload = copy.deepcopy(receipt)
    payload["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(payload)

    predecessor = receipt["predecessor_receipt"]
    predecessor_bytes = subprocess.run(
        [
            "git", "-C", str(APPLICATION_ROOT), "show",
            f'{predecessor["commit"]}:{predecessor["path"]}',
        ],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    assert "sha256:" + hashlib.sha256(predecessor_bytes).hexdigest() == predecessor[
        "raw_sha256"
    ]
    predecessor_blob = subprocess.run(
        [
            "git", "-C", str(APPLICATION_ROOT), "rev-parse",
            f'{predecessor["commit"]}:{predecessor["path"]}',
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    assert predecessor_blob == predecessor["git_blob_sha"]
    predecessor_value = json.loads(predecessor_bytes)
    assert predecessor_value["artifact_hash"] == predecessor["artifact_hash"]
    assert predecessor_value["framework_changed_files"] == 638

    framework_delta = receipt["framework_delta"]
    commits = subprocess.run(
        [
            "git", "-C", str(FRAMEWORK_ROOT), "rev-list", "--count",
            f'{framework_delta["previous_commit"]}..{framework_delta["current_commit"]}',
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    changed_files = subprocess.run(
        [
            "git", "-C", str(FRAMEWORK_ROOT), "diff", "--name-only",
            framework_delta["previous_commit"], framework_delta["current_commit"],
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.splitlines()
    assert int(commits) == framework_delta["commits_between"] == 113
    assert len(changed_files) == framework_delta["changed_files"] == 635

    chronology = receipt["chronology"]
    assert datetime.fromisoformat(receipt["recorded_at"]) > datetime.fromisoformat(
        chronology["verification_observed_complete_at"]
    ) > datetime.fromisoformat(chronology["integration_merge_created_at"])
    assert receipt["application_integration"]["live_main_commit"] == (
        "48d1153c3b5fa749b1a6fd84212befb9e39daabe"
    )
    integration = receipt["application_integration"]
    integration_parents = subprocess.run(
        [
            "git", "-C", str(APPLICATION_ROOT), "show", "-s", "--format=%P",
            integration["local_integration_merge_commit"],
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.split()
    assert integration_parents == [
        integration["pre_refresh_pr_head"], integration["live_main_commit"]
    ]
    live_main_tree = subprocess.run(
        [
            "git", "-C", str(APPLICATION_ROOT), "rev-parse",
            f'{integration["live_main_commit"]}^{{tree}}',
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    assert live_main_tree == integration["live_main_tree"]
    assert receipt["verification"]["tests_passed"] == 307
    assert receipt["authority"].endswith("NO_MATHEMATICAL_AUTHORITY_CHANGE")


def test_current_main_pin_sync_receipt_is_exact_historical_and_non_authorizing() -> None:
    receipt = json.loads(CURRENT_MAIN_SYNC_RECEIPT.read_text(encoding="utf-8"))
    assert set(receipt) == {
        "schema_version",
        "receipt_id",
        "recorded_at",
        "framework_delta",
        "application_pin_integration",
        "current_gate_preservation",
        "verification",
        "authority_contract",
        "artifact_hash",
    }
    payload = copy.deepcopy(receipt)
    payload["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(payload)
    assert receipt["schema_version"] == "framework-pin-current-main-sync-receipt-v1"
    assert receipt["receipt_id"] == "RAKL-MATH-FRAMEWORK-PIN-SYNC-4EE5E9A-20260811"
    assert datetime.fromisoformat(receipt["recorded_at"]) > datetime.fromisoformat(
        receipt["verification"]["verified_at"]
    )

    delta = receipt["framework_delta"]
    assert delta["current_commit"] == HISTORICAL_4EE_FRAMEWORK_COMMIT
    assert delta["remote_main_at_observation"] == HISTORICAL_4EE_FRAMEWORK_COMMIT
    assert datetime.fromisoformat(delta["remote_main_observed_at"]) == datetime.fromisoformat(
        receipt["recorded_at"]
    )
    current_tree = subprocess.run(
        ["git", "-C", str(FRAMEWORK_ROOT), "rev-parse", f'{delta["current_commit"]}^{{tree}}'],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    assert current_tree == delta["current_tree"]
    commit_count = subprocess.run(
        [
            "git", "-C", str(FRAMEWORK_ROOT), "rev-list", "--count",
            f'{delta["previous_commit"]}..{delta["current_commit"]}',
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    changed_paths = subprocess.run(
        [
            "git", "-C", str(FRAMEWORK_ROOT), "diff", "--name-only",
            delta["previous_commit"], delta["current_commit"],
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.splitlines()
    assert int(commit_count) == delta["commits_between"] == 3
    assert changed_paths == delta["changed_paths"]
    assert len(changed_paths) == delta["changed_files"] == 15

    integration = receipt["application_pin_integration"]
    assert integration["pin_commit"] == receipt["verification"]["subject_commit"]
    for field, path in (
        ("config_blob", "config/rakl-framework-pin.json"),
        ("gitlink_commit", "framework/RAKL"),
        ("pin_contract_test_blob", "tests/math_applications/test_framework_pin_contract.py"),
    ):
        observed = subprocess.run(
            [
                "git", "-C", str(APPLICATION_ROOT), "rev-parse",
                f'{integration["pin_commit"]}:{path}',
            ],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        ).stdout.strip()
        assert observed == integration[field]
    assert integration["gitlink_commit"] == HISTORICAL_4EE_FRAMEWORK_COMMIT
    assert integration["historical_receipts_rewritten"] is False
    assert integration["mathematical_lesson_artifacts_mutated"] is False

    gate = receipt["current_gate_preservation"]
    for prefix, commit in (
        ("previous", delta["previous_commit"]),
        ("current", delta["current_commit"]),
    ):
        for field, path in (
            ("task_episode_schema_blob", gate["task_episode_schema_path"]),
            ("experience_substrate_blob", gate["experience_substrate_path"]),
        ):
            observed = subprocess.run(
                ["git", "-C", str(FRAMEWORK_ROOT), "rev-parse", f"{commit}:{path}"],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            ).stdout.strip()
            assert observed == gate[f"{prefix}_{field}"]
    schema_raw = subprocess.run(
        [
            "git", "-C", str(FRAMEWORK_ROOT), "show",
            f'{delta["current_commit"]}:{gate["task_episode_schema_path"]}',
        ],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    assert "storage_admission" in json.loads(schema_raw)["required"]
    assert gate["storage_admission_required"] is True
    assert gate["storage_admission_gate_weakened"] is False
    assert not any(receipt["authority_contract"].values())


def test_final_current_main_pin_sync_receipt_binds_f224_without_gate_drift() -> None:
    receipt = json.loads(FINAL_CURRENT_MAIN_SYNC_RECEIPT.read_text(encoding="utf-8"))
    payload = copy.deepcopy(receipt)
    payload["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(payload)
    assert receipt["receipt_id"] == "RAKL-MATH-FRAMEWORK-PIN-SYNC-F224D91-20260811"
    assert datetime.fromisoformat(receipt["recorded_at"]) > datetime.fromisoformat(
        receipt["verification"]["verified_at"]
    )

    delta = receipt["framework_delta"]
    assert delta["current_commit"] == HISTORICAL_F224_FRAMEWORK_COMMIT
    assert delta["remote_main_at_observation"] == HISTORICAL_F224_FRAMEWORK_COMMIT
    changed_paths = subprocess.run(
        [
            "git", "-C", str(FRAMEWORK_ROOT), "diff", "--name-only",
            delta["previous_commit"], delta["current_commit"],
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.splitlines()
    commit_count = subprocess.run(
        [
            "git", "-C", str(FRAMEWORK_ROOT), "rev-list", "--count",
            f'{delta["previous_commit"]}..{delta["current_commit"]}',
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    assert changed_paths == delta["changed_paths"]
    assert len(changed_paths) == delta["changed_files"] == 28
    assert int(commit_count) == delta["commits_between"] == 1

    integration = receipt["application_pin_integration"]
    assert integration["pin_commit"] == receipt["verification"]["subject_commit"]
    for field, path in (
        ("config_blob", "config/rakl-framework-pin.json"),
        ("gitlink_commit", "framework/RAKL"),
        ("pin_contract_test_blob", "tests/math_applications/test_framework_pin_contract.py"),
    ):
        observed = subprocess.run(
            [
                "git", "-C", str(APPLICATION_ROOT), "rev-parse",
                f'{integration["pin_commit"]}:{path}',
            ],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        ).stdout.strip()
        assert observed == integration[field]
    assert integration["gitlink_commit"] == HISTORICAL_F224_FRAMEWORK_COMMIT
    assert integration["historical_receipts_rewritten"] is False
    assert integration["mathematical_lesson_artifacts_mutated"] is False

    gate = receipt["current_gate_preservation"]
    assert gate["previous_task_episode_schema_blob"] == gate["current_task_episode_schema_blob"]
    assert gate["previous_experience_substrate_blob"] == gate["current_experience_substrate_blob"]
    schema_raw = subprocess.run(
        [
            "git", "-C", str(FRAMEWORK_ROOT), "show",
            f'{delta["current_commit"]}:{gate["task_episode_schema_path"]}',
        ],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    assert "storage_admission" in json.loads(schema_raw)["required"]
    assert gate["storage_admission_required"] is True
    assert gate["storage_admission_gate_weakened"] is False
    assert receipt["verification"]["tests_passed"] == 34
    assert receipt["verification"]["exit_code"] == 0
    assert not any(receipt["authority_contract"].values())
