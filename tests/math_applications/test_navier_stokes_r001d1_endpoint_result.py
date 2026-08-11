from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"

RAKL_MAIN = "decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8"
APPLICATION_MAIN_INSPECTED = "5d6bdc6f566921f51a375fdc2e8035123cf4830c"
CANDIDATE_COMMIT = "54974135e15027d58eae1dba474aec685b74e4f7"
PRE_CANDIDATE_HEAD = "595abaa60190dbc63b335f0d1285d11995050e25"
PREDECESSOR_EVENT_HASH = "sha256:a20c9b69056e861518523ae3160cb3740a6205c9775505acdea52db3cbeb1b04"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: dict) -> str:
    payload = json.loads(json.dumps(value))
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_predeclared_endpoint_pulse_refutes_finite_l2_to_pointwise_coefficient() -> None:
    values = []
    for n in (4, 8, 12, 16):
        eps = 2.0 ** (-n)
        norm_sq = (eps ** -1) * eps
        j_value = 4.0 * eps ** (-0.25)
        assert math.isclose(norm_sq, 1.0, rel_tol=0.0, abs_tol=1e-15)
        values.append(j_value)
    assert values == sorted(values)
    assert values[-1] > values[0] * 8


def test_energy_line_exponent_deficits_are_exactly_the_registered_route_warning() -> None:
    for q1, q2 in ((2.0, 6.0), (3.0, 3.0), (4.0, 4.0), (6.0, 6.0)):
        inv_p1 = 0.75 - 1.5 / q1
        inv_p2 = 0.75 - 1.5 / q2
        inv_r = 1.0 / q1 + 1.0 / q2
        a = 1.5 * inv_r
        assert math.isclose(a + inv_p1 + inv_p2, 1.5, abs_tol=1e-12)

    for q in (2.0, 3.0, 4.0, 6.0):
        inv_p = 0.75 - 1.5 / q
        a = 1.5 * (1.0 / 3.0 + 1.0 / q)
        assert math.isclose(a + inv_p, 1.25, abs_tol=1e-12)


def test_v3_shadow_episode_is_search_priority_only_and_content_bound() -> None:
    wrapper = _load(
        "07_memory/NS_R001D1_C001_TASK_EPISODE_SHADOW_20260811.json"
    )
    assert wrapper["status"] == "PROPOSAL_SHADOW"
    authority = wrapper["authority_contract"]
    assert authority["allowed_effect"] == "SEARCH_PRIORITY_ONLY"
    assert all(
        authority[key] is False
        for key in (
            "grants_tool_authority",
            "grants_proof_authority",
            "grants_gluing_authority",
            "grants_theorem_authority",
            "grants_framework_authority",
            "grants_review_independence",
        )
    )
    episode = wrapper["episode"]
    assert episode["outcome"] == "FAILURE"
    assert episode["residual_signature"]
    assert episode["context_hash"].startswith("sha256:")
    assert episode["fibre_snapshot_hash"].startswith("sha256:")
    assert episode["artifact_hash"] == _canonical_hash(episode)


def test_fibre_snapshot_records_selected_and_rejected_retrievals() -> None:
    fibre = _load("07_memory/NS_R001D1_C001_FIBRE_SNAPSHOT_20260811.json")
    assert fibre["framework_main_sha"] == RAKL_MAIN
    assert fibre["application_main_inspected_sha"] == APPLICATION_MAIN_INSPECTED
    assert fibre["candidate_branch_head_sha"] == CANDIDATE_COMMIT
    assert fibre["artifact_hash"] == _canonical_hash(fibre)
    assert fibre["retrieval_outcomes"]["selected"]
    rejected = " ".join(
        item["item"] + " " + item["reason"]
        for item in fibre["retrieval_outcomes"]["rejected_or_deferred"]
    )
    assert "PR #33" in rejected
    assert "immediate new invariant invention" in rejected


def test_failure_record_is_scoped_to_proof_architecture() -> None:
    failure = _load(
        "07_memory/NS_R001D1_C001_FAILURE_EXPERIENCE_DELTA_20260811.json"
    )
    assert failure["failure_id"] == "F-NS-R001D1-C001-UNSIGNED-DUHAMEL-ENDPOINT"
    assert failure["diagnosis_status"] == "SUPPORTED"
    assert failure["artifact_hash"] == _canonical_hash(failure)
    scope = " ".join(failure["scope_conditions"])
    assert "unsigned global Lebesgue norms" in scope
    result = (BASE / "04_candidates/NS_R001D1_C001_DUHAMEL_ENDPOINT_RESULT_20260811.md").read_text(encoding="utf-8")
    assert "does **not** refute Navier" in result
    assert "RAKL_TRIVIAL" in result
    assert "DYNAMIC_HIGH_FREQUENCY_REPLENISHMENT" in result


def test_saturation_reopens_only_scoped_axes_and_never_claims_completeness() -> None:
    sat = _load("07_memory/NS_R001D1_C001_SATURATION_VECTOR_20260811.json")
    expected = {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert set(sat["axes"]) == expected
    assert sat["absolute_completeness_claim"] is False
    assert sat["novelty_classification"]["class"] == "RAKL_TRIVIAL"
    assert "KNOWLEDGE" not in sat["native_residual_reopened_axes"]
    assert set(sat["native_residual_reopened_axes"]).issubset(expected)
    assert sat["artifact_hash"] == _canonical_hash(sat)


def test_post_candidate_trace_delta_is_hash_chained_from_frozen_prefix() -> None:
    trace = _load("09_trace/NS_R001D1_RESULT_TRACE_DELTA_20260811.json")
    assert trace["predecessor_event_hash"] == PREDECESSOR_EVENT_HASH
    expected_types = [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
        "REVIEWED",
    ]
    assert [entry["event_type"] for entry in trace["entries"]] == expected_types
    previous = PREDECESSOR_EVENT_HASH
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        assert entry["artifact_hash"] == _canonical_hash(entry)
        previous = entry["artifact_hash"]
    assert trace["entries"][0]["timestamp"] == "2026-08-11T10:17:27+00:00"


def test_case_study_separates_math_representation_gluing_and_ci_failures() -> None:
    text = (
        BASE / "08_reviews/NS_R001D1_RAKL_METHOD_CASE_STUDY_20260811.md"
    ).read_text(encoding="utf-8")
    for marker in (
        "representation/proof architecture",
        "retrieval: **NO MATERIAL FAILURE OBSERVED**",
        "tooling/CI: **YES, SECONDARY**",
        "gluing: **YES, STILL OPEN**",
        "critical_closure_deficit_audit",
    ):
        assert marker in text
