from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema
import rakl


APPLICATION_ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = Path(rakl.__file__).resolve().parents[2]
EXPECTED_FRAMEWORK_COMMIT = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"


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
            / "receipts/framework-pin-sync-15f1c3a-20260811.json"
        ).read_text(encoding="utf-8")
    )
    payload = copy.deepcopy(receipt)
    payload["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(payload)
    assert receipt["current_framework_commit"] == EXPECTED_FRAMEWORK_COMMIT
    assert receipt["verification"] == {
        "command": "python tools/run_application_tests.py --framework framework/RAKL",
        "tests_passed": 166,
        "exit_code": 0,
        "pin_equals_gitlink": True,
        "framework_authority_paths_clean": True,
    }
    assert receipt["verdict"] == "PASS_APPLICATION_CONFORMANCE_ON_EXACT_FRAMEWORK_PIN"
    assert "NO_MATHEMATICAL_AUTHORITY_CHANGE" in receipt["authority"]
