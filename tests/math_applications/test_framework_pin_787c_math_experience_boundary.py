from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
PIN_RECEIPT = ROOT / "receipts/framework-pin-sync-787c7e0-20260811.json"
PIN_SCHEMA = ROOT / "schemas/framework-pin-sync-787c7e0-receipt.schema.json"
BOUNDARY = PNP / "07_memory/O9d12a2a1a1b1_MATHEMATICAL_EXPERIENCE_BOUNDARY_20260811.json"
BOUNDARY_SCHEMA = ROOT / "schemas/pnp-mathematical-experience-boundary.schema.json"
ASSESSMENT = PNP / "08_reviews/C034_C040_EXTERNAL_LEDGER_ASSESSMENT_20260811.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _git(*args: str, cwd: Path = ROOT) -> str:
    return subprocess.run(
        ["git", "-C", str(cwd), *args],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()


def test_787c_pin_sync_receipt_is_exact_and_non_authorizing() -> None:
    receipt = _load(PIN_RECEIPT)
    schema = _load(PIN_SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(receipt)
    assert receipt["artifact_hash"] == _hash(receipt)

    delta = receipt["framework_delta"]
    framework = ROOT / "framework/RAKL"
    assert int(_git("rev-list", "--count", f'{delta["previous_commit"]}..{delta["current_commit"]}', cwd=framework)) == 11
    assert len(_git("diff", "--name-only", delta["previous_commit"], delta["current_commit"], cwd=framework).splitlines()) == 36
    assert _git("rev-parse", f'{delta["previous_commit"]}^{{tree}}', cwd=framework) == delta["previous_tree"]
    assert _git("rev-parse", f'{delta["current_commit"]}^{{tree}}', cwd=framework) == delta["current_tree"]
    assert _git("rev-parse", "HEAD", cwd=framework) == delta["current_commit"]

    assert receipt["compatibility_review"]["historical_artifacts_rewritten"] is False
    assert not any(receipt["authority_contract"].values())
    assert receipt["verification"] == {
        "subject_commit": "21412bea172a4b57183625cc2bd99a662b0ee8b8",
        "verified_at": "2026-08-11T17:48:08Z",
        "command": "python tools/run_application_tests.py --framework framework/RAKL",
        "tests_passed": 459,
        "exit_code": 0,
        "pin_equals_gitlink": True,
        "framework_authority_paths_clean": True,
        "status": "PASS_EXACT_APPLICATION_SUITE",
    }


def test_pnp_experience_boundary_keeps_only_mathematical_lessons_in_math_memory() -> None:
    boundary = _load(BOUNDARY)
    schema = _load(BOUNDARY_SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(boundary)
    assert boundary["artifact_hash"] == _hash(boundary)

    assessment = _load(ASSESSMENT)
    assert boundary["source_assessment"]["artifact_hash"] == assessment["artifact_hash"]
    assert assessment["packet_status"] == "QUARANTINED_EXTERNAL_PROPOSAL"

    mathematical_ids = {
        item["lesson_id"] for item in boundary["retained_mathematical_lessons"]
    }
    operational_ids = {
        item["event_id"] for item in boundary["excluded_operational_events"]
    }
    assert mathematical_ids.isdisjoint(operational_ids)
    by_lesson = {
        item["lesson_id"]: item for item in boundary["retained_mathematical_lessons"]
    }
    assert by_lesson["C034B-FINITE-CEILING-OVERGENERALIZATION"]["authority"] == (
        "RETROSPECTIVE_TARGET_EXPOSED_EXACT_REPLAY"
    )
    assert operational_ids == {
        "F-C034-PROCESS-GATE-DELAY",
        "F-C035-BATCH-WORKER-HANG",
        "F-C040-FULL-DUAL-LP-STALL",
        "GIT-CI-HASH-TIMESTAMP-PORTABILITY",
    }
    assert {
        item["lesson_id"]
        for item in boundary["retained_mathematical_lessons"]
        if item["promotion"] == "BOUNDED_FAILURE_EXPERIENCE_ELIGIBLE"
    } == {"C037-ARBITRARY-EXTENSION-NONMONOTONE"}
    assert boundary["next_inventory_contract"]["candidate_generation_allowed"] is False
    assert not any(boundary["authority_contract"].values())
