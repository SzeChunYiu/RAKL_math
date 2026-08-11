from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"


def _load(relative: str) -> dict:
    return json.loads((NS / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: dict, field: str) -> str:
    payload = dict(value)
    payload.pop(field, None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def test_b2a1_context_is_frozen_before_candidate_generation() -> None:
    context = _load("01_frontier/NS-B2a1_CONTEXT_FIBER_20260811.json")
    assert context["atom_id"] == "NS-B2a1"
    assert context["candidate_generation_allowed"] is False
    assert context["first_candidate_at"] is None
    assert context["packet_hash"] == _canonical_hash(context, "packet_hash")
    assert "fixed-radius diagonal compactness" in " ".join(context["explicit_disanalogies"])


def test_b2a1_preaction_receipt_binds_exact_subject_and_discriminator() -> None:
    receipt = _load("07_memory/NS_B2A1_PRE_ACTION_FIBRE_RECEIPT_20260811.json")
    assert receipt["framework_source"]["commit"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert receipt["application_source"]["base_commit"] == "4838969ecc18a091da79a059b58b8568634289b7"
    assert receipt["chosen_operator"] == "SOURCE_TAIL_INHERITANCE_AUDIT"
    assert receipt["allowed_outcome_branches"]["B"] == "ONLY_LOCAL_COMPACTNESS_AND_CRITICAL_BOUNDEDNESS"
    assert receipt["candidate_generation_allowed"] is False
    assert receipt["fibre_snapshot"]["universe_completeness_claim"] is False
    assert receipt["receipt_hash"] == _canonical_hash(receipt, "receipt_hash")


def test_b2a1_trace_is_hash_chained_across_pre_and_post_action() -> None:
    pre = _load("09_trace/NS_B2A1_PREACTION_TRACE_20260811.json")
    post = _load("09_trace/NS_B2A1_POSTACTION_TRACE_20260811.json")

    prior = None
    for event in pre["events"]:
        assert event["previous_event_hash"] == prior
        assert event["artifact_hash"] == _canonical_hash(event, "artifact_hash")
        prior = event["artifact_hash"]
    assert pre["events"][-1]["event_type"] == "NEXT_STEP_PROPOSED"
    assert pre["candidate_generation_allowed"] is False

    for event in post["events"]:
        assert event["previous_event_hash"] == prior
        assert event["artifact_hash"] == _canonical_hash(event, "artifact_hash")
        prior = event["artifact_hash"]
    assert [event["event_type"] for event in post["events"]] == [
        "FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"
    ]
    assert post["candidate_generation_allowed"] is False


def test_critical_shell_falsifier_has_exact_f1_scaling_order() -> None:
    # w_R = R^-1 phi((x-x_R)/R):
    # normalized kinetic energy R^-1 * R^-2 * R^3 = R^0.
    kinetic_exponent = -1 - 2 + 3
    # normalized spacetime gradient energy:
    # R^-1 * (R^-2)^2 * R^3 * R^2 = R^0.
    gradient_exponent = -1 - 4 + 3 + 2
    assert kinetic_exponent == 0
    assert gradient_exponent == 0


def test_b2a1_episode_is_bound_to_preaction_receipt_and_stays_non_authoritative() -> None:
    receipt = _load("07_memory/NS_B2A1_PRE_ACTION_FIBRE_RECEIPT_20260811.json")
    episode = _load("07_memory/NS_B2A1_TASK_EPISODE_20260811.json")
    failure = _load("07_memory/NS_B2A1_FAILURE_EXPERIENCE_20260811.json")

    assert episode["pre_action_receipt_hash"] == receipt["receipt_hash"]
    assert episode["fibre_snapshot_hash"] == receipt["receipt_hash"]
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["artifact_hash"] == _canonical_hash(episode, "artifact_hash")
    assert failure["status"] == "OBSERVED_ONLY"
    assert failure["diagnosis_status"] == "OBSERVED_ONLY"
    assert failure["authority_contract"]["grants_theorem_authority"] is False
    assert failure["authority_contract"]["grants_framework_authority"] is False
    assert failure["artifact_hash"] == _canonical_hash(failure, "artifact_hash")


def test_b2a1_cycle_metrics_are_seven_axis_and_fail_closed_on_unmeasured_resources() -> None:
    metrics = _load("07_memory/NS_B2A1_RAKL_CYCLE_METRICS_20260811.json")
    saturation = _load("07_memory/NS_B2A1_SATURATION_ROUND_20260811.json")

    expected_axes = {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION",
        "RELATION", "PATH", "META_METHOD",
    }
    assert set(metrics["retained_semantic_novelty"]) == expected_axes
    assert set(saturation["retained_novelty"]) == expected_axes
    assert metrics["retained_semantic_novelty"] == saturation["retained_novelty"]
    assert metrics["gate_status"]["candidate_generation_allowed"] is False
    assert metrics["gate_status"]["root_authority"] == "NONE"
    assert metrics["gate_status"]["independent_review_credit"] is False
    assert str(metrics["resource_proxies"]["model_input_tokens"]).startswith("CANNOT_MEASURE")
    assert str(metrics["state_fingerprints"]["pre_state"]).startswith("CANNOT_MEASURE")
    assert metrics["artifact_hash"] == _canonical_hash(metrics, "artifact_hash")
    assert saturation["artifact_hash"] == _canonical_hash(saturation, "artifact_hash")
