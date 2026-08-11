from __future__ import annotations

import json
from pathlib import Path
import subprocess

import jsonschema
import rakl


APPLICATION_ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = Path(rakl.__file__).resolve().parents[2]
EXPECTED_FRAMEWORK_COMMIT = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"


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
