from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"


def load(rel: str) -> dict:
    return json.loads((RH / rel).read_text())


def test_r10_fixed_n_abel_result_is_scoped_and_not_root() -> None:
    result = load("04_candidates/RH_ANA_003_ABEL_001_FIXED_N_ABEL_RESULT_20260812_R10.json")
    assert result["result_branch"] == "PROVED_FIXED_N_NATURAL_ORDER_IDENTITY"
    assert [item["status"] for item in result["proof_obligations"]] == ["PASS"] * 7
    assert result["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert "NO_N_UNIFORMITY" in result["authority_boundary"]
    assert "NO_RIEMANN_HYPOTHESIS_CLAIM" in result["authority_boundary"]
    assert result["formal_verifier"] == "NOT_RUN"
    assert result["same_context_review_independent_credit"] == 0


def test_r10_task_episode_is_exact_content_bound_shadow() -> None:
    episode = load("07_memory/RH_ANA_003_ABEL_001_TASK_EPISODE_RESULT_20260812_R10.json")
    payload = {key: value for key, value in episode.items() if key != "artifact_hash"}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert episode["artifact_hash"] == hashlib.sha256(raw).hexdigest()
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "SUCCESS"
    assert "UNIFORM_IN_N_CONTROL_OPEN" in episode["residual_signature"]


def test_r10_trace_extends_frozen_candidate_and_never_promotes_root() -> None:
    trace = load("09_trace/RH_ANA_003_ABEL_001_RESULT_TRACE_20260812_R10.json")
    entries = trace["entries"]
    assert entries[0]["previous_event_hash"] == "sha256:5180c3e6f829b8e75e6398196221f4df5a7b40d34f0fa5997e7a35649747cc0d"
    assert [entry["event_type"] for entry in entries] == ["FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"]
    for left, right in zip(entries, entries[1:]):
        assert right["previous_event_hash"] == left["artifact_hash"]
    assert all(entry["event_type"] != "PROMOTED" for entry in entries)


def test_r10_case_study_has_required_seven_axis_receipt() -> None:
    case = load("10_case_study/RAKL_METHOD_CASE_STUDY_RH_ANA_003_ABEL_001_20260812_R10.json")
    assert case["schema"] == "RAKL_METHOD_CASE_STUDY"
    assert case["retained_semantic_novelty_counts"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert all(value == 0 for value in case["protected_canonical_novelty_counts"].values())
    assert case["search_policy"]["rakl_changed_action"] is True
    assert case["falsifier_and_verification"]["independent_review_credit"] == 0


def test_r10_episode_diagnosis_obstruction_lesson_are_distinct() -> None:
    episode = load("07_memory/RH_ANA_003_ABEL_001_TASK_EPISODE_RESULT_20260812_R10.json")
    diagnosis = load("07_memory/RH_ANA_003_ABEL_001_DIAGNOSIS_20260812_R10.json")
    obstruction = load("07_memory/RH_ANA_003_ABEL_001_OBSTRUCTION_20260812_R10.json")
    lesson = load("07_memory/RH_ANA_003_ABEL_001_LESSON_20260812_R10.json")
    assert diagnosis["episode_id"] == episode["episode_id"]
    assert obstruction["source_episode_id"] == episode["episode_id"]
    assert episode["episode_id"] in lesson["supporting_episode_ids"]
    assert diagnosis["status"] == "SUPPORTED_LOCAL"
    assert obstruction["authority"] == "PROPOSAL_SHADOW_OBSTRUCTION_ONLY"
    assert lesson["authority"] == "CANDIDATE"


def test_r10_same_context_expert_cell_has_zero_independent_credit() -> None:
    expert = load("08_reviews/RH_ANA_003_ABEL_001_EXPERT_RESULT_20260812_R10.json")
    assert len(expert["roles"]) == 7
    assert expert["same_context_review"] is True
    assert expert["independent_review_credit"] == 0
