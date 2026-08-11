from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
CROSS = ROOT / "research/real_math/millennium/cross_problem"
STUDY = CROSS / "10_study_pattern"
MEMORY = CROSS / "07_memory"
CANDIDATES = CROSS / "04_candidates"
SOURCE_COMMIT = "0c59960d31c1d752005476507ef6dbdb80938e48"
SOURCE_TREE = "a67a57d5a5fd289340b2884859cc0cf63364c813"
SOURCE_PATH = (
    "research/real_math/millennium/cross_problem/07_memory/"
    "XM005_SOURCE_AND_METHOD_RECEIPT_20260811.json"
)
SOURCE_BLOB = "20eff9295791e86def20024b030e539057d50e58"
SOURCE_SHA256 = "5ef7c80695b1a77bd22790a08c73299162b570262e07da3a4b9bed49eee14065"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: dict) -> str:
    unhashed = copy.deepcopy(value)
    unhashed["artifact_hash"] = ""
    raw = json.dumps(
        unhashed,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def test_xm005_episode_uses_merged_shadow_schema_and_grants_no_authority() -> None:
    schema = _load(STUDY / "EXPERIENCE_EPISODE_PROPOSAL.schema.json")
    episode = _load(MEMORY / "XM005_METHOD_TASK_EPISODE_PROPOSAL_20260811.json")
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(episode)
    assert episode["artifact_hash"] == _canonical_hash(episode)
    assert episode["status"] == "PROPOSAL_ONLY"
    assert episode["source_role"] == "CONTRADICTION"
    contract = episode["authority_contract"]
    assert contract["effective_authority"] == "PROPOSAL_ONLY"
    assert contract["allowed_effect"] == "SEARCH_PRIORITY_ONLY"
    for key, value in contract.items():
        if key.startswith("grants_"):
            assert value is False


def test_xm005_source_binding_is_git_and_content_exact() -> None:
    episode = _load(MEMORY / "XM005_METHOD_TASK_EPISODE_PROPOSAL_20260811.json")
    binding = episode["source_bindings"][0]
    assert binding["commit_sha"] == SOURCE_COMMIT
    assert binding["tree_sha"] == SOURCE_TREE
    assert binding["path"] == SOURCE_PATH
    assert binding["git_blob_sha"] == SOURCE_BLOB
    assert binding["content_sha256"] == SOURCE_SHA256
    assert _git("rev-parse", f"{SOURCE_COMMIT}^{{tree}}") == SOURCE_TREE
    assert _git("rev-parse", f"{SOURCE_COMMIT}:{SOURCE_PATH}") == SOURCE_BLOB
    source_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{SOURCE_COMMIT}:{SOURCE_PATH}"],
        check=True,
        capture_output=True,
    ).stdout
    assert hashlib.sha256(source_bytes).hexdigest() == SOURCE_SHA256


def test_xm005_calibration_keeps_conditional_counterexample_boundary() -> None:
    text = (
        CANDIDATES / "XM005_MOVING_CORE_RIGIDITY_CALIBRATION_20260811.md"
    ).read_text(encoding="utf-8")
    assert "world-tube occupancy" in text
    assert "2a/|c|" in text
    assert "kinematically compatible" in text
    assert "deliberately conditional" in text
    assert "not claimed as a literal counterexample" in text
    assert "no-incoming-energy" in text
    assert "NO_NS_CANDIDATE" in text
    assert "NO_ROOT_AUTHORITY" in text


def test_method_case_study_covers_six_roots_and_separates_diagnosis() -> None:
    text = (MEMORY / "RAKL_METHOD_CASE_STUDY_20260811_R1.md").read_text(
        encoding="utf-8"
    )
    for marker in (
        "P vs NP",
        "Riemann Hypothesis",
        "Navier–Stokes",
        "Yang–Mills",
        "Hodge",
        "BSD",
    ):
        assert marker in text
    assert "observed episode -> competing diagnosis -> scoped lesson hypothesis" in text
    assert "SUPPORTED_PROCESS_PATTERN" in text
    assert "RootCoordinatePreservationReceipt" in text
    assert "RAKL framework issue #119" in text
    assert "No RAKL architecture variant is promoted" in text
