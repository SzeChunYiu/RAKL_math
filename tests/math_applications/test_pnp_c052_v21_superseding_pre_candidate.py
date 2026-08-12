from __future__ import annotations

import importlib.util
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = BASE / "09_trace/c052_v21_superseding_pre_candidate_fixture.py"
FAILURE = BASE / "07_memory/O9d12a2a1b_C052_V2_INVALID_FREEZE_FAILURE_EXPERIENCE_20260812.json"
CONTEXT = BASE / "01_frontier/O9d12a2a1b_C052_V21_SEMANTIC_KERNEL_CONTEXT_20260812.json"
MEMORY = BASE / "07_memory/O9d12a2a1b_C052_V21_RESEARCH_MEMORY_REVIEW_20260812.json"
REVIEW = BASE / "08_reviews/O9d12a2a1b_C052_V21_EXPERT_CONTEXT_REVIEW_20260812.json"
TRACE = BASE / "09_trace/O9d12a2a1b_C052_V21_SUPERSEDING_PRE_CANDIDATE_TRACE_20260812.json"
REVALIDATION = BASE / "09_trace/O9d12a2a1b_C052_V21_FRAMEWORK_REVALIDATION_D21592B_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_v21_pre", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_v21_pre_candidate_artifacts_match_serializer() -> None:
    paths = [FAILURE, CONTEXT, MEMORY, REVIEW, TRACE, REVALIDATION]
    assert [load(path) for path in paths] == list(module().build())


def test_public_v2_is_preserved_as_invalid_zero_authority_history() -> None:
    failure = load(FAILURE)
    assert failure["public_commit"] == "5dd517842ed24bd91a3754312b15c519d394135c"
    assert failure["public_commit_time_utc"] == "2026-08-12T13:28:03Z"
    assert failure["observed_result"] == "V2_FREEZE_INVALID_TRAP_DOMAIN_AND_FUTURE_TIMESTAMP"
    assert failure["execution_or_result_accessed"] is False
    assert failure["superseded_not_rewritten"] is True
    assert failure["authority"] == "ZERO_AUTHORITY_INVALID_FREEZE_PRESERVED_NEGATIVE_HISTORY"


def test_repaired_packet_is_pre_candidate_only() -> None:
    context = load(CONTEXT)
    review = load(REVIEW)
    trace = load(TRACE)
    source = FIXTURE.read_text(encoding="utf-8")
    assert context["public_v2_input_authority"] == "PROPOSAL_ONLY_INVALID_FREEZE_NO_GATE_AUTHORITY"
    assert review["strongest_objection"] == (
        "A trap outside the C041 classifier domain can only elicit CANNOT_CHECK unless a valid sub-kernel and exact integration call path are frozen."
    )
    assert "def kernel_identity" not in source
    assert "def classifier_identity" not in source
    assert "CANDIDATE_PROPOSED" not in [entry["event_type"] for entry in trace["entries"][-9:]]
    assert trace["entries"][-1]["outputs"] == ["PUBLIC_MERGE_REQUIRED_BEFORE_CANDIDATE", "NO_CANDIDATE_IN_THIS_ROUND"]


def test_truthful_chronology_precedes_any_future_candidate() -> None:
    entries = load(TRACE)["entries"][-9:]
    assert [entry["event_type"] for entry in entries] == [
        "REVIEWED", "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW", "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW", "NEXT_STEP_PROPOSED",
    ]
    times = [datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00")) for entry in entries]
    assert times[0] < times[1]
    assert all(time == times[1] for time in times[1:8])
    assert times[7] < times[8]
    for previous, current in zip(load(TRACE)["entries"], load(TRACE)["entries"][1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]


def test_artifact_chronology_indices_match_their_trace_events() -> None:
    trace_entries = {
        entry["chronology_order_index"]: entry
        for entry in load(TRACE)["entries"][-9:]
    }
    expected = [
        (FAILURE, 24, "REVIEWED"),
        (CONTEXT, 26, "CONTEXT_FROZEN"),
        (REVIEW, 29, "EXPERT_CONTEXT_REVIEW"),
        (MEMORY, 30, "EXPERIENCE_MEMORY_REVIEW"),
        (REVALIDATION, 32, "NEXT_STEP_PROPOSED"),
    ]
    for path, index, event_type in expected:
        artifact = load(path)
        event = trace_entries[index]
        assert artifact["chronology_order_index"] == index
        assert event["event_type"] == event_type
        assert str(path.relative_to(ROOT)) in event["evidence_pointers"]
        assert artifact["observed_at_utc"] == event["timestamp"]


def test_artifact_hash_dependencies_do_not_point_forward_in_chronology() -> None:
    artifacts = [load(path) for path in [FAILURE, CONTEXT, REVIEW, MEMORY, REVALIDATION]]
    chronology_by_hash = {
        artifact["artifact_hash"]: artifact["chronology_order_index"]
        for artifact in artifacts
    }
    for artifact in artifacts:
        current_index = artifact["chronology_order_index"]
        for key, value in artifact.items():
            if key.endswith("_hash") and value in chronology_by_hash:
                assert chronology_by_hash[value] <= current_index
    assert "memory_hash" not in load(REVIEW)


def test_next_identity_requires_typed_kernel_and_integration_after_merge() -> None:
    context = load(CONTEXT)
    review = load(REVIEW)
    memory = load(MEMORY)
    assert context["typed_repair_obligations"] == [
        "semantic-coordinate decision kernel whose input domain admits the abstract subset trap",
        "C041 adapter that constructs support and H_k evidence before calling the exact kernel",
        "integration world proving the adapter invokes and propagates the exact kernel branch",
        "fresh hidden H_k witness-complete world excluding consumed k20",
    ]
    assert review["recommendation"] == (
        "Publish and merge this corrected pre-candidate packet before freezing any v2.1 kernel, classifier, falsifier, trap, or authorization identity."
    )
    assert memory["relevant_failure_ids"][0] == "F-PNP-C052-V2-INVALID-TRAP-DOMAIN-AND-FUTURE-TIMESTAMP"


def test_framework_observation_has_no_math_authority() -> None:
    observation = load(REVALIDATION)
    assert observation["observed_current_main_sha"] == "d21592b0ff8da988deabb923fd549891ff8ad9f0"
    assert observation["protected_mathematical_gate_files_changed"] == []
    assert observation["hidden_world_labels_accessed"] is False
    assert observation["mathematical_result_credit"] == 0
