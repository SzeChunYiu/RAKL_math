from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"
RECEIPT = BASE / "08_reviews/YM-S1A1_PACKET_PROVENANCE_ASSURANCE_20260811.json"
SCHEMA = ROOT / "schemas/packet-provenance-assurance-receipt.schema.json"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _git(*arguments: str, text: bool = True) -> str | bytes:
    completed = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        text=text,
    )
    return completed.stdout.strip() if text else completed.stdout


def _audit_binding(binding: dict) -> None:
    commit = binding["source_commit"]
    path = binding["path"]
    if _git("rev-parse", f"{commit}^{{tree}}") != binding["source_tree"]:
        raise ValueError("source_tree_mismatch")
    if _git("rev-parse", f"{commit}:{path}") != binding["git_blob"]:
        raise ValueError("source_blob_mismatch")
    source_bytes = _git("show", f"{commit}:{path}", text=False)
    source_sha = "sha256:" + hashlib.sha256(source_bytes).hexdigest()
    if source_sha != binding["file_sha256"]:
        raise ValueError("source_file_hash_mismatch")
    if source_bytes != (ROOT / path).read_bytes():
        raise ValueError("workspace_bytes_differ_from_bound_source")


def test_yms1a1_packet_artifacts_have_executable_git_provenance() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)

    expected = {
        "old_review",
        "live_review",
        "old_trace",
        "pre_review_trace",
        "live_trace",
        "packet_binding_receipt",
    }
    assert set(receipt["bindings"]) == expected
    for binding in receipt["bindings"].values():
        _audit_binding(binding)

    assert receipt["source_commit"] == "c854d7c77208a671e6a8dd6d8c22d17927cc01d6"
    assert receipt["source_tree"] == _git("rev-parse", "c854d7c^{tree}")
    assert all(
        binding["source_commit"] == receipt["source_commit"]
        for binding in receipt["bindings"].values()
    )
    _git("merge-base", "--is-ancestor", receipt["source_commit"], "HEAD")
    _git(
        "merge-base",
        "--is-ancestor",
        receipt["application_repository"]["base_main_commit"],
        "HEAD",
    )
    pin = json.loads((ROOT / "config/rakl-framework-pin.json").read_text())
    assert receipt["framework_pin"]["commit"] == pin["commit"]
    assert receipt["framework_pin"]["commit"] == _git(
        "rev-parse", "HEAD:framework/RAKL"
    )
    assert receipt["assurance_worlds"] == [
        {"world": "VALID_BOUND_SOURCE", "expected": "PASS", "observed": "PASS"},
        {
            "world": "WRONG_COMMIT_OR_BLOB",
            "expected": "FAIL",
            "observed": "FAIL",
        },
        {
            "world": "MISSING_SOURCE_PATH",
            "expected": "CANNOT_CHECK",
            "observed": "CANNOT_CHECK",
        },
    ]
    assert "NO_MATHEMATICAL_RESULT" in receipt["authority"]
    receipt_for_hash = copy.deepcopy(receipt)
    receipt_for_hash["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(receipt_for_hash)


def test_yms1a1_packet_git_provenance_fails_closed() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    live_review = receipt["bindings"]["live_review"]

    wrong_commit = copy.deepcopy(live_review)
    wrong_commit["source_commit"] = "21d349b20ff6373336974274be7752227223d478"
    try:
        _audit_binding(wrong_commit)
    except ValueError:
        pass
    else:
        raise AssertionError("wrong source commit must fail closed")

    wrong_blob = copy.deepcopy(live_review)
    wrong_blob["git_blob"] = "0" * 40
    try:
        _audit_binding(wrong_blob)
    except ValueError as exc:
        assert str(exc) == "source_blob_mismatch"
    else:
        raise AssertionError("wrong source blob must fail closed")

    missing_source = copy.deepcopy(live_review)
    missing_source["path"] += ".missing"
    try:
        _audit_binding(missing_source)
    except subprocess.CalledProcessError:
        pass
    else:
        raise AssertionError("missing source path must fail closed")
