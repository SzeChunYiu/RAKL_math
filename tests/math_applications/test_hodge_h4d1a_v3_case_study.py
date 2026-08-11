from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _assert_self_hash(raw: dict, field: str) -> None:
    payload = copy.deepcopy(raw)
    expected = payload[field]
    payload[field] = ""
    assert expected == _canonical_hash(payload)


def test_h4d1a_v3_shadow_episode_is_content_bound_and_non_authoritative() -> None:
    context = _load("01_frontier/H4d1a_CONTEXT_FIBER_20260811.json")
    fibre = _load("07_memory/H4d1a_V3_FIBRE_SNAPSHOT_20260811.json")
    episode = _load("07_memory/H4d1a_V3_TASK_EPISODE_20260811.json")
    failure = _load("07_memory/H4d1a_V3_FAILURE_OBSERVATION_20260811.json")

    _assert_self_hash(fibre, "snapshot_hash")
    _assert_self_hash(episode, "artifact_hash")
    _assert_self_hash(failure, "artifact_hash")

    assert fibre["context_hash"] == context["packet_hash"]
    assert episode["context_hash"] == context["packet_hash"]
    assert episode["fibre_snapshot_hash"] == fibre["snapshot_hash"]
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["residual_signature"]
    assert episode["cost"] == 4.0

    assert "F-H4D1-DETECTOR-KERNEL-GAP" in fibre["failure_history"]
    assert "THEOREM_INVENTION" in fibre["rejected_operator_ids"]
    assert "HODGE_BASE_ONLY_TO_WITNESS_INFERENCE" in fibre["rejected_operator_ids"]

    assert failure["episode_id"] == episode["episode_id"]
    assert failure["status"] == "OBSERVED_ONLY"
    assert failure["reusable_obstruction_authority"] == "NONE"
    assert failure["lesson_authority"] == "NONE"
    assert failure["allowed_effect"] == "SEARCH_PRIORITY_ONLY"
    assert len(failure["competing_diagnoses"]) >= 3


def test_h4d1a_postcal_trace_continues_frozen_chronology_without_candidate() -> None:
    old_trace = _load("09_trace/H4d1a_PRE_CANDIDATE_TRACE_20260811.json")
    trace = _load("09_trace/H4d1a_POSTCAL_TRACE_20260811.json")

    predecessor = old_trace["entries"][-1]["artifact_hash"]
    assert trace["predecessor_event_hash"] == predecessor
    assert trace["entries"][0]["previous_event_hash"] == predecessor

    previous = predecessor
    event_types = []
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = copy.deepcopy(entry)
        expected = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert expected == _canonical_hash(payload)
        previous = expected
        event_types.append(entry["event_type"])

    assert event_types == ["FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED"]
    assert "CANDIDATE_PROPOSED" not in event_types
    assert any("SOURCE_INSUFFICIENT_FOR_PROPER_ENVELOPE" in item for item in trace["entries"][1]["outputs"])
    assert any("H4d1a1-WITNESS-MODULI-PROJECTION" in item for item in trace["entries"][2]["outputs"])


def test_h4d1a_case_study_preserves_scope_and_v3_method_telemetry() -> None:
    result = (BASE / "03_routes/H4d1a_B_T1_REACHABILITY_CALIBRATION_20260811.md").read_text(
        encoding="utf-8"
    )
    case_study = (BASE / "08_reviews/H4d1a_RAKL_METHOD_CASE_STUDY_20260811.md").read_text(
        encoding="utf-8"
    )

    assert "SOURCE_INSUFFICIENT_FOR_PROPER_ENVELOPE" in result
    assert "F-H4D1A-CLASS-WITNESS-PERSISTENCE-GAP" in result
    assert "OBSERVED_ONLY" in result
    assert "ROOT_AUTHORITY_NONE" in result
    assert "H4d1a1-WITNESS-MODULI-PROJECTION" in result

    assert "RAKL_METHOD_CASE_STUDY" in case_study
    assert "representation + relation/gluing failure" in case_study
    assert "RELATION" in case_study and "REOPENED" in case_study
    assert "META_METHOD" in case_study
    assert "LOCAL_SECTION_IDENTITY" in case_study
    assert "INTERFACE_COVERAGE" in case_study
    assert "The framework hypothesis is **not** opened" in case_study
