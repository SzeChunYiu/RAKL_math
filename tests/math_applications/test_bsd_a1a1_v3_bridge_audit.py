from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"


def _canonical_hash(payload: dict) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _hash_without_artifact(payload: dict) -> str:
    data = dict(payload)
    data.pop("artifact_hash")
    return _canonical_hash(data)


def test_bsd_v3_episode_proposal_is_quarantined_and_content_bound() -> None:
    proposal = json.loads(
        (
            BSD
            / "07_memory/BSD_A1a1_V3_BRIDGE_AUDIT_TASK_EPISODE_20260811.json"
        ).read_text(encoding="utf-8")
    )
    assert proposal["schema_version"] == "experience-episode-proposal-v0"
    assert proposal["artifact_type"] == "EXPERIENCE_EPISODE_PROPOSAL"
    assert proposal["status"] == "PROPOSAL_ONLY"
    assert proposal["source_role"] == "CONTRADICTION"
    assert proposal["reported_outcome"] == "PARTIAL_SUCCESS"
    assert proposal["residual_signature"]
    authority = proposal["authority_contract"]
    assert authority["effective_authority"] == "PROPOSAL_ONLY"
    assert authority["allowed_effect"] == "SEARCH_PRIORITY_ONLY"
    assert not any(
        authority[key]
        for key in (
            "grants_tool_authority",
            "grants_proof_authority",
            "grants_gluing_authority",
            "grants_theorem_authority",
            "grants_framework_authority",
            "grants_review_independence",
        )
    )
    assert len(proposal["source_bindings"]) == 3
    assert proposal["artifact_hash"] == _hash_without_artifact(proposal)


def test_rich_method_telemetry_records_v3_case_study_coordinates() -> None:
    telemetry = json.loads(
        (
            BSD / "07_memory/BSD_A1a1_V3_METHOD_TELEMETRY_20260811.json"
        ).read_text(encoding="utf-8")
    )
    assert telemetry["atom_id"] == "BSD-A1a1-THETA-ORDER-COMPARISON"
    assert telemetry["authority"] == "PROPOSAL_SHADOW_SEARCH_PRIORITY_ONLY"
    assert telemetry["outcome"] == "PARTIAL_SUCCESS"
    assert telemetry["gluing_assessment"]["classification"] == "LOCAL_TO_GLOBAL_RELATION_GAP"
    assert telemetry["gluing_assessment"]["grants_solution_authority"] is False
    assert telemetry["novelty_classification"]["class"] == "UNRESOLVED"
    assert set(telemetry["saturation_vector"]) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert telemetry["framework_semantic_authority"]["commit"] != telemetry["execution_dependency_pin"]["commit"]
    assert telemetry["artifact_hash"] == _hash_without_artifact(telemetry)


def test_observed_failure_does_not_promote_a_reusable_lesson() -> None:
    failure = json.loads(
        (
            BSD
            / "07_memory/BSD_A1a1_V3_BRIDGE_AUDIT_FAILURE_OBSERVED_20260811.json"
        ).read_text(encoding="utf-8")
    )
    assert failure["authority"] == "OBSERVED_ONLY"
    assert failure["reusable_lesson_status"] == "NOT_PROMOTED"
    assert failure["allowed_effect"] == "SEARCH_PRIORITY_WARNING_ONLY"
    assert len(failure["competing_diagnoses"]) >= 3
    assert failure["artifact_hash"] == _hash_without_artifact(failure)


def test_source_audit_keeps_local_success_separate_from_root_authority() -> None:
    text = (
        BSD
        / "01_frontier/BSD_A1a1_V3_COMPLEX_ANTICYCLOTOMIC_BRIDGE_AUDIT_20260811.md"
    ).read_text(encoding="utf-8")
    assert "LOCAL_SUCCESS != GLOBAL_BSD_BRIDGE" in text
    assert "NO_MATHEMATICAL_CANDIDATE" in text
    assert "ROOT_AUTHORITY_NONE" in text
    assert "not** a literature-wide nonexistence or novelty claim" in text
    assert "derived-height/regulator nondegeneracy" in text


def test_method_case_study_separates_semantic_authority_from_execution_pin() -> None:
    text = (
        BSD
        / "08_reviews/RAKL_METHOD_CASE_STUDY_BSD_ANALYTIC_20260811.md"
    ).read_text(encoding="utf-8")
    assert "framework_semantic_authority_ref" in text
    assert "execution_dependency_pin_ref" in text
    assert "219 passed, 5 failed" in text
    assert "Self-RAKL challenger hypothesis only" in text


def test_route_diagnostic_does_not_open_a_child_candidate() -> None:
    text = (
        BSD
        / "02_problem_dag/BSD_A1a1_V3_ROUTE_DIAGNOSTIC_20260811.yaml"
    ).read_text(encoding="utf-8")
    assert "status: OBSERVED_ROUTE_GAP" in text
    assert "mathematical_candidate: false" in text
    assert "theorem: false" in text
    assert "root: false" in text
    assert "freeze a fresh strict child context" in text
