from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = (
    ROOT
    / "research/real_math/millennium/cross_problem/07_memory/"
    "GLOBAL_MATH_ONLY_SATURATION_LEDGER_20260812.json"
)

EXPECTED_LANES = {
    "p_vs_np",
    "riemann_hypothesis",
    "navier_stokes",
    "yang_mills",
    "hodge_conjecture",
    "birch_swinnerton_dyer",
    "poincare_conjecture",
}
ALLOWED_CREDIT_TYPES = {
    "PROOF_OR_LEMMA",
    "EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE",
    "BROKEN_MATHEMATICAL_ASSUMPTION",
    "TRANSFER_CONDITION",
    "MATHEMATICAL_FALSIFIER",
}
FORBIDDEN_CREDIT_TERMS = {
    "git",
    "branch state",
    "commit",
    "pull request",
    "pr state",
    "merge",
    "ci",
    "schema",
    "hash",
    "serialization",
    "runtime",
    "chronology",
}


def _load() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_global_ledger_is_content_bound_and_covers_the_full_portfolio() -> None:
    ledger = _load()
    assert ledger["artifact_hash"] == _canonical_hash(ledger)
    assert ledger["base_repository_sha"] == (
        "21d22075fa250e4ded412fd292b7942b87503266"
    )
    assert {lane["lane_id"] for lane in ledger["lanes"]} == EXPECTED_LANES
    assert len(ledger["lanes"]) == len(EXPECTED_LANES)
    assert ledger["claim_boundary"]["any_root_solved"] is False
    assert ledger["claim_boundary"]["framework_promotion_implied"] is False
    assert ledger["claim_boundary"]["absolute_saturation_claim"] is False
    assert ledger["authority_universe"]["kind"] == "MERGED_ORIGIN_MAIN_ONLY"
    assert ledger["authority_universe"]["pending_or_open_pr_material_counted"] is False


def test_credit_is_atomic_math_only_and_totals_are_recomputed() -> None:
    ledger = _load()
    entries = [entry for lane in ledger["lanes"] for entry in lane["credited_items"]]
    assert entries
    ids = [entry["item_id"] for entry in entries]
    assert len(ids) == len(set(ids))

    for entry in entries:
        assert entry["mathematical_credit"] is True
        assert entry["credit_units"] == 1
        assert entry["credit_type"] in ALLOWED_CREDIT_TYPES
        assert entry["authority"]
        assert entry["exact_claim"]
        assert entry["scope"]
        assert entry["non_implications"]
        assert entry["evidence_pointers"]
        for pointer in entry["evidence_pointers"]:
            path = pointer.split("#", 1)[0]
            if path.startswith("research/"):
                assert (ROOT / path).is_file(), pointer
        credit_surface = " ".join(
            [entry["exact_claim"], entry["scope"], entry["credit_type"]]
        ).lower()
        assert not any(re.search(r"\b" + re.escape(term) + r"\b", credit_surface) for term in FORBIDDEN_CREDIT_TERMS)

    assert ledger["totals"]["mathematical_credit_units"] == len(entries)
    by_lane = ledger["totals"]["mathematical_credit_units_by_lane"]
    assert by_lane == {
        lane["lane_id"]: len(lane["credited_items"]) for lane in ledger["lanes"]
    }
    by_type = ledger["totals"]["mathematical_credit_units_by_type"]
    assert sum(by_type.values()) == len(entries)
    assert by_type == {
        kind: sum(entry["credit_type"] == kind for entry in entries)
        for kind in sorted(ALLOWED_CREDIT_TYPES)
    }


def test_exclusions_are_explicit_zero_credit_provenance() -> None:
    ledger = _load()
    exclusions = ledger["excluded_provenance"]
    assert exclusions
    excluded_ids = [item["item_id"] for item in exclusions]
    assert len(excluded_ids) == len(set(excluded_ids))
    assert ledger["totals"]["excluded_provenance_items"] == len(exclusions)
    assert all(item["mathematical_credit"] is False for item in exclusions)
    assert all(item["credit_units"] == 0 for item in exclusions)
    categories = {item["category"] for item in exclusions}
    assert {
        "ASSURANCE_METADATA",
        "SOFTWARE_STUDY_PATTERN_EXAMPLE",
        "NON_MATHEMATICAL_INVENTORY",
        "SAME_CONTEXT_REVIEW",
        "PROCESS_OR_TELEMETRY_SHADOW",
    } <= categories

    study = next(
        item for item in exclusions
        if item["item_id"] == "EXCLUDED-CROSS-PROBLEM-STUDY-PATTERN-EXAMPLES"
    )
    assert any("LESSON_PROPOSAL_EXAMPLE" in p for p in study["evidence_pointers"])
    assert "preserved" in study["reason"].lower()
    assert "software" in study["reason"].lower()


def test_lane_boundaries_and_yang_mills_failure_are_narrow() -> None:
    ledger = _load()
    lanes = {lane["lane_id"]: lane for lane in ledger["lanes"]}
    assert lanes["poincare_conjecture"]["credited_items"] == []
    assert lanes["poincare_conjecture"]["status"] == "NO_ACTIVE_APPLICATION_ARTIFACTS"
    assert all(lane["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE" for lane in ledger["lanes"])

    ym = lanes["yang_mills"]
    gluing = next(
        item for item in ym["credited_items"]
        if item["item_id"] == "F-YM-S1A2-OS-SZZ-SAME-THEORY-GLUING-UNBOUND"
    )
    assert gluing["credit_type"] == "BROKEN_MATHEMATICAL_ASSUMPTION"
    joined = " ".join(gluing["non_implications"])
    assert "not a verified impossibility" in joined.lower()
    assert "missing theorem" in joined.lower()
    assert "continuum" in joined.lower()
    assert "root" in joined.lower()

    ns = lanes["navier_stokes"]
    escaping = next(item for item in ns["credited_items"] if item["item_id"] == "F-NS-B2A1A2-FIXED-TO-MOVING-RADIUS-ESCAPE")
    assert escaping["credit_type"] == "EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE"
    assert any("not a navier-stokes or euler solution" in item.lower() for item in escaping["non_implications"])


def test_global_artifact_audit_distinguishes_names_from_credit() -> None:
    audit = _load()["global_artifact_audit"]
    assert audit["filename_inventory"]["lesson_named_files"] == 8
    assert audit["filename_inventory"]["inventory_named_files"] == 32
    assert audit["filename_inventory"]["saturation_named_files"] == 2
    assert audit["rules"]["filename_or_record_name_never_mints_credit"] is True
    assert audit["rules"]["computation_alone_is_not_proof"] is True
    assert audit["rules"]["same_context_review_is_not_independent"] is True
    assert audit["rules"]["assurance_metadata_credit_units"] == 0
