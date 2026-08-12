from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ATLAS = ROOT / "research/real_math/millennium/cross_problem/07_memory/GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_20260812.json"
EXPECTED_BASE = "ec8a9eb5eeedaaf1d3f497a8688384256a2079e0"
EXPECTED_FRAMEWORK = "43897d3afaf0038385102d5acc64793c05ec40f0"
LANES = {
    "p_vs_np",
    "riemann_hypothesis",
    "navier_stokes",
    "yang_mills",
    "hodge_conjecture",
    "birch_swinnerton_dyer",
}


def load() -> dict:
    return json.loads(ATLAS.read_text(encoding="utf-8"))


def canonical_hash(document: dict) -> str:
    payload = dict(document)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_atlas_is_exactly_bound_and_self_hashed() -> None:
    atlas = load()
    assert atlas["authority_universe"] == {
        "framework_sha": EXPECTED_FRAMEWORK,
        "kind": "MERGED_ORIGIN_MAIN_ONLY",
        "repository_sha": EXPECTED_BASE,
    }
    assert atlas["artifact_hash"] == canonical_hash(atlas)


def test_every_active_unsolved_lane_has_a_scoped_mathematical_failure_mechanism() -> None:
    atlas = load()
    mechanisms = atlas["failure_mechanisms"]
    assert {item["lane"] for item in mechanisms} == LANES
    assert len({item["id"] for item in mechanisms}) == len(mechanisms) == 6
    for item in mechanisms:
        assert item["source_items"]
        assert item["failed_inference"]
        assert item["proximate_cause"]
        assert item["root_cause_status"]
        assert item["root_cause"]
        assert item["falsifier"]
        assert item["repair"]
        assert item["scope"]
        assert item["evidence"]


def test_cross_problem_classes_preserve_disanalogies() -> None:
    atlas = load()
    known = {item["id"] for item in atlas["failure_mechanisms"]}
    classes = atlas["cross_problem_equivalence_classes"]
    assert len(classes) == 3
    for group in classes:
        assert set(group["members"]) <= known
        assert len(group["members"]) >= 2
        assert group["shared_structure"]
        assert group["disanalogy"]
        assert group["advisory"]


def test_feedback_is_proposal_only_zero_credit_and_falsifiable() -> None:
    atlas = load()
    feedback = atlas["self_rakl_feedback"]
    assert feedback["status"] == "APPLICATION_FEEDBACK_PROPOSAL_ONLY_NOT_PROMOTED"
    assert feedback["mathematical_credit_units"] == 0
    assert feedback["fresh_assurance_required"] is True
    assert feedback["framework_mutation_allowed"] is False
    assert feedback["same_context_review_is_independent"] is False
    assert feedback["falsifier"]
    assert atlas["credit_contract"] == {
        "atlas_synthesis_creates_new_mathematical_credit": False,
        "same_context_review_is_independent": False,
        "software_assurance_credit_units": 0,
        "source_mathematical_claims_remain_counted_only_in_global_math_ledger": True,
    }


def test_no_open_root_is_promoted() -> None:
    atlas = load()
    for lane in LANES:
        assert atlas["root_status"][lane] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert atlas["root_status"]["poincare_conjecture"] == "SOLVED_EXTERNALLY_NO_ACTIVE_APPLICATION_CLAIM"
