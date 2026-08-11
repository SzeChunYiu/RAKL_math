from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research" / "real_math" / "millennium" / "p_vs_np"


def _load(relative: str):
    return json.loads((PNP / relative).read_text(encoding="utf-8"))


def _canon(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def test_r2_fibre_snapshot_hash_and_authority() -> None:
    fibre = _load("01_frontier/O9d12a2a1a1b1_R2_RESTRICTION_POLARITY_FIBRE_V3_20260811.json")
    digest = hashlib.sha256(_canon(fibre["snapshot"])).hexdigest()
    assert fibre["fibre_snapshot_hash"] == f"sha256:{digest}"
    assert fibre["snapshot"]["authority"] == "PROPOSAL_SHADOW_WORKING_FIBRE_ONLY"
    assert fibre["snapshot"]["memory"]["missed_prior_experience_later_found"] == []


def test_r2_task_episode_content_hash_is_current_v3_compatible() -> None:
    episode = _load("09_trace/O9d12a2a1a1b1_R2_TASK_EPISODE_PROPOSAL_20260811.json")
    payload = dict(episode)
    artifact_hash = payload.pop("artifact_hash")
    assert len(artifact_hash) == 64
    assert artifact_hash == hashlib.sha256(_canon(payload)).hexdigest()
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert "PNP-ROOT-OPEN_NO_SOLUTION_CERTIFICATE" in episode["residual_signature"]


def test_r2_trace_chain_binds_every_event() -> None:
    trace = _load("09_trace/O9d12a2a1a1b1_R2_RESTRICTION_POLARITY_HASH_CHAIN_20260811.json")
    previous = trace["genesis_fibre_hash"]
    for expected_sequence, event in enumerate(trace["events"], start=1):
        assert event["sequence"] == expected_sequence
        assert event["previous_event_hash"] == previous
        payload = dict(event)
        event_hash = payload.pop("event_hash")
        assert event_hash == "sha256:" + hashlib.sha256(_canon(payload)).hexdigest()
        previous = event_hash
    assert trace["terminal_hash"] == previous


def test_r2_local_math_and_gluing_are_separate() -> None:
    result = _load("01_frontier/O9d12a2a1a1b1_R2_RESTRICTION_POLARITY_RESULT_20260811.json")
    assert result["exact_local_claim"]["claim"].startswith("rho_full(x) <= rho_res(x)")
    assert result["local_mathematical_failure"] is None
    assert result["local_to_global_gluing_failure"]["status"] == "OPEN"
    assert result["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert result["verification"]["independent_review_count"] == 0


def test_r2_experience_objects_remain_distinct_and_shadow_only() -> None:
    experience = _load("07_memory/O9d12a2a1a1b1_R2_EXPERIENCE_SHADOW_20260811.json")
    assert experience["lineage_order"] == ["episode", "diagnosis", "failure", "obstruction", "lesson", "motif"]
    ids = [
        experience["episode"]["episode_id"],
        experience["diagnosis"]["diagnosis_id"],
        experience["failure"]["failure_id"],
        experience["obstruction"]["obstruction_id"],
        experience["lesson"]["lesson_id"],
        experience["motif"]["motif_id"],
    ]
    assert len(ids) == len(set(ids))
    assert experience["protected_retention"] is False


def test_r2_metrology_never_counts_repository_growth_as_learning() -> None:
    packet = _load("10_case_study/O9d12a2a1a1b1_R2_RAKL_METHOD_CASE_STUDY_AND_METRICS_20260811.json")
    metrics = packet["RAKL_CYCLE_METRICS"]
    assert metrics["rakl_method_version"] == "3.0.0"
    assert metrics["rakl_math_base"] == "350861b1c2755033893068e5519b8b06a6315aa6"
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert metrics["raw_repository_growth_counts_as_learning"] is False
    assert metrics["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_status"]["independent_mathematical_reviews"] == "0/3"
