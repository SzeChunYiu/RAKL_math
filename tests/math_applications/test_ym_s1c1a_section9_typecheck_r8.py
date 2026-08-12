import hashlib
import json
from pathlib import Path


RECEIPT = Path(
    "research/real_math/millennium/yang_mills/10_case_study/"
    "YM-S1c1a_SECTION9_TYPECHECK_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260811_R8.json"
)
AXES = {
    "KNOWLEDGE",
    "OPERATOR",
    "EXPERIENCE_PATTERN",
    "OBSTRUCTION",
    "RELATION",
    "PATH",
    "META_METHOD",
}
RESIDUAL = (
    "RES-YM-S1c1a-R8-TRAJECTORY-TO-SECTION9-SCHEME-EMBEDDING-"
    "OR-VANISHING-INTERTRAJECTORY-ESTIMATE"
)


def _canonical_bytes(obj):
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def _sha(obj):
    return hashlib.sha256(_canonical_bytes(obj)).hexdigest()


def test_r8_shadow_metrology_and_gate_integrity():
    data = json.loads(RECEIPT.read_text(encoding="utf-8"))

    assert "PROPOSAL_SHADOW" in data["authority"]
    assert data["TaskEpisode"]["storage_admission"] == "PROPOSAL_SHADOW_STORED"

    metrics = data["RAKL_CYCLE_METRICS"]
    novelty = metrics["retained_semantic_novelty"]
    assert set(novelty) == AXES
    assert all(value == 0 for value in novelty.values())
    assert metrics["raw_repository_growth_counts_as_learning"] is False
    assert metrics["residual_after"] == RESIDUAL

    gates = metrics["gate_status"]
    assert gates["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert gates["scientific_authority"] == "NO_PROMOTION_TRANSITION_INVOKED"
    assert gates["independent_mathematical_reviews"] == 0

    for key, value in metrics["new_ids"].items():
        if key.startswith("new_protected_"):
            assert value == []

    gluing = data["typed_gluing_audit"]
    assert gluing["compatible"] is False
    assert gluing["all_sections_verified"] is False
    assert gluing["complete_coverage"] is False
    assert gluing["v3_gluing_episode_outcome"] == "FAILURE"
    assert {
        item["key"] for item in gluing["obstructions"]
    } == {"parameter_identity", "comparison_modulus", "common_limit_pair"}


def test_r8_trace_chronology_and_hash_chain():
    data = json.loads(RECEIPT.read_text(encoding="utf-8"))
    events = data["trace"]["events"]
    required_prefix = [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert [event["event_type"] for event in events[:7]] == required_prefix

    previous = None
    for event in events:
        assert event["previous_event_hash"] == previous
        hashed_payload = {
            "event_type": event["event_type"],
            "timestamp": event["timestamp"],
            "previous_event_hash": event["previous_event_hash"],
            "payload": event["payload"],
        }
        assert _sha(hashed_payload) == event["artifact_hash"]
        previous = event["artifact_hash"]

    assert data["trace"]["head_hash"] == previous


def test_r8_fibre_and_episode_content_hashes():
    data = json.loads(RECEIPT.read_text(encoding="utf-8"))

    fibre = dict(data["MathContextFiber"])
    expected_fibre_hash = fibre.pop("fibre_snapshot_hash")
    assert _sha(fibre) == expected_fibre_hash

    episode = dict(data["TaskEpisode"])
    expected_episode_hash = episode.pop("artifact_hash")
    assert _sha(episode) == expected_episode_hash
