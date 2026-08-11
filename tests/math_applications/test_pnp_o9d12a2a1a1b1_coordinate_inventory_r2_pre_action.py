from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
RECEIPT_PATH = (
    ROOT
    / "research/real_math/millennium/p_vs_np/09_trace/"
    "O9d12a2a1a1b1_COORDINATE_INVENTORY_R2_PRE_ACTION_20260811.json"
)
FRAMEWORK = ROOT / "framework/RAKL"
PIN = "242a39348291141d635a752b9e078fabdab011ea"
APPLICATION_BASE = "b7b9300a7a40e918a6e49bfc3e5e87a949148a5e"


def _canonical_sha256(document: dict[str, object]) -> str:
    payload = dict(document)
    payload["receipt_canonical_sha256"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()


def test_r2_coordinate_inventory_is_frozen_before_source_evaluation() -> None:
    receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    schema = json.loads(
        (FRAMEWORK / "schemas/pre-action-fibre-receipt-v1.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(receipt)
    assert receipt["receipt_canonical_sha256"] == _canonical_sha256(receipt)

    assert receipt["atom_id"] == "O9d12a2a1a1b1"
    assert receipt["sequence_index"] == 3
    assert receipt["framework_commit"] == PIN
    assert receipt["application_commit"] == APPLICATION_BASE
    assert _git("rev-parse", f"{APPLICATION_BASE}:framework/RAKL") == PIN

    discriminator = receipt["predeclared_discriminator"]
    for obligation in (
        "distinct from rho(A,B)",
        "universal construction-side upper bound",
        "common-resource multiplexing",
        "free union closure of B",
        "explicitly named target family",
        "Q=omega(log N)",
        "row-level DifferenceWitness",
    ):
        assert obligation in discriminator
    assert "cannot be converted into a bounded-family no-match claim" in discriminator
    assert receipt["allowed_outcome_branches"] == ["SUCCESS", "FAILURE", "BLOCKED"]

    rejected = {
        row["retrieval_id"]: row["rejection_reason"]
        for row in receipt["rejected_retrievals"]
    }
    assert {
        "RAKL-MATH-PR113-FREE-UNION-QUOTIENT",
        "RAKL-MATH-PR128-ZERO-COST-SHATTERING",
        "RAKL-MATH-PR154-INCREMENTAL-TRACE",
    } <= rejected.keys()
    assert "circular" in rejected["COORDINATE-EQUALS-RHO-OR-D-CYCLIC"]
    assert "no theorem authority" in rejected["RAKL-MATH-PR113-FREE-UNION-QUOTIENT"]
    assert "may not invent" in rejected["NEW-COORDINATE-OR-PROOF-CANDIDATE"]

    selected = {
        row["retrieval_id"]: row for row in receipt["selected_retrievals"]
    }
    assert selected["ECCC-TR25-033-PRIMARY-PDF"]["authority"] == "CANONICAL"
    assert selected["RAZBOROV-1989-PRIMARY-PDF"]["authority"] == "CANONICAL"
    assert selected["WIGDERSON-1993-PRIMARY-PDF"]["authority"] == "CANONICAL"

    # This is a discriminator freeze, not a result or candidate receipt.
    raw = RECEIPT_PATH.read_text(encoding="utf-8")
    assert '"candidate_id"' not in raw
    assert '"result"' not in raw
