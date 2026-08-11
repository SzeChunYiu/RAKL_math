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
EXPECTED_FRAMEWORK_COMMIT = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
HISTORICAL_FRAMEWORK_COMMIT = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
FINAL_SYNC_RECEIPT = (
    APPLICATION_ROOT / "receipts/framework-pin-final-integration-bd1a276-20260811.json"
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
    assert receipt["current_framework_commit"] == EXPECTED_FRAMEWORK_COMMIT
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
        chronology["verification_completed_at"]
    ) > datetime.fromisoformat(chronology["integration_merge_created_at"])
    assert receipt["application_integration"]["live_main_commit"] == (
        "2ddb51359292fd9638116b488ffff9a04397446b"
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
    assert receipt["verification"]["github_check"]["completed_at"] == chronology[
        "verification_completed_at"
    ]
    assert receipt["verification"]["tests_passed"] == 302
    assert receipt["authority"].endswith("NO_MATHEMATICAL_AUTHORITY_CHANGE")
