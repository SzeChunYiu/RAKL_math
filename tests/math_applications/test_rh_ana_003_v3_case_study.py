from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research" / "real_math" / "millennium" / "riemann_hypothesis"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _verify_self_hash(packet: dict, field: str = "artifact_hash") -> None:
    expected = packet[field]
    unsigned = dict(packet)
    unsigned.pop(field)
    assert _digest(unsigned) == expected


def test_rh_ana_003_context_and_memory_are_bound_before_candidate() -> None:
    context = _load(RH / "01_frontier" / "RH_ANA_003_CONTEXT_FIBER_20260811_R1.json")
    memory = _load(RH / "07_memory" / "RH_ANA_003_RESEARCH_MEMORY_REVIEW_20260811_R1.json")

    unsigned_context = dict(context)
    packet_hash = unsigned_context.pop("packet_hash")
    assert _digest(unsigned_context) == packet_hash
    assert context["first_candidate_at"] is None
    assert context["prospective_next_action"]["candidate_generation"] is False
    assert memory["target_context_hash"] == packet_hash
    _verify_self_hash(memory)


def test_rh_ana_003_trace_is_hash_chained_and_contains_no_candidate() -> None:
    parent = _load(RH / "09_trace" / "RH_ANA_003_TRACE_20260811_R1.json")
    continuation = _load(RH / "09_trace" / "RH_ANA_003_TRACE_CONTINUATION_20260811_R1.json")

    previous = None
    for event in parent["events"]:
        assert event["previous_event_hash"] == previous
        expected = event["artifact_hash"]
        unsigned = dict(event)
        unsigned.pop("artifact_hash")
        assert _digest(unsigned) == expected
        previous = expected
    assert parent["final_event_hash"] == previous
    _verify_self_hash(parent)

    assert continuation["parent_final_event_hash"] == previous
    for event in continuation["events"]:
        assert event["previous_event_hash"] == previous
        expected = event["artifact_hash"]
        unsigned = dict(event)
        unsigned.pop("artifact_hash")
        assert _digest(unsigned) == expected
        previous = expected
    assert continuation["final_event_hash"] == previous
    assert continuation["candidate_event_present"] is False
    assert continuation["promotion_event_present"] is False
    assert all(event["event_type"] != "CANDIDATE_PROPOSED" for event in parent["events"] + continuation["events"])
    _verify_self_hash(continuation)


def test_rh_ana_003_v3_episode_lesson_and_saturation_are_proposal_only() -> None:
    episode = _load(RH / "07_memory" / "RH_ANA_003_TASK_EPISODE_20260811_R1.json")
    lesson = _load(RH / "07_memory" / "RH_ANA_003_LESSON_PROPOSAL_20260811_R1.json")
    saturation = _load(RH / "09_trace" / "RH_ANA_003_SATURATION_UPDATE_20260811_R1.json")

    _verify_self_hash(episode)
    _verify_self_hash(lesson)
    _verify_self_hash(saturation)

    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["cost_proxy"]["new_mathematical_candidates"] == 0
    assert lesson["authority"] == "CANDIDATE"
    assert lesson["authority_effect"] == "SEARCH_PRIORITY_ONLY"
    assert lesson["supporting_episode_ids"] == [episode["episode_id"]]

    axes = {item["axis"] for item in saturation["axes"]}
    assert axes == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert saturation["bounded_saturated"] is False
    assert "OPERATOR" not in saturation["reopened_axes"]
    assert "META_METHOD" not in saturation["reopened_axes"]


def test_rh_ana_003_case_study_preserves_root_authority_boundary() -> None:
    audit = (RH / "01_frontier" / "RH_ANA_003_INDEX_HEIGHT_CANCELLATION_AUDIT_20260811_R1.md").read_text(encoding="utf-8")
    case_study = (RH / "09_trace" / "RAKL_METHOD_CASE_STUDY_RH_ANA_003_20260811_R1.md").read_text(encoding="utf-8")

    assert "NO_RH_CANDIDATE" in audit
    assert "RAKL_TRIVIAL" in audit
    assert "RAKL_METHOD_CASE_STUDY" in case_study
    assert "ROOT_AUTHORITY_NONE" in case_study
    assert "Local-to-global / gluing" in case_study
    assert "Seven-axis saturation update" in case_study
