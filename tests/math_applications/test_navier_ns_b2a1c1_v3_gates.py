from __future__ import annotations

import json
from pathlib import Path

from rakl.experience_substrate import EpisodeOutcome, EpisodeStorageAdmission, TaskEpisode, validate_episode
from rakl.math_context import ContextGateVerdict, MathContextFiber, MethodTransfer, audit_math_context_fiber
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview, ResearchMemoryVerdict, audit_research_memory_review
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace, audit_research_trace
from rakl.semantic_shortcut import (
    ObstructionFingerprint,
    ObstructionTransformationEpisode,
    ObstructionTransformationMemory,
    ObstructionTransformationReview,
    RouteSearchStatus,
    ShortcutMode,
    ShortcutReviewVerdict,
    StructuralMappingWitness,
    TransformationEpisodeAuthority,
    audit_obstruction_transformation_review,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"
CTX_HASH = "sha256:0bb23767bf43d6d478cd702045f3697241e01d7394e3da9b800fa2ef048c6b64"
MEM_HASH = "sha256:0be8fdb93f5b25b2c23612313c35430559954d208441e926bf6b8e0188bc5090"
OTR_HASH = "sha256:9a088c0fa0c84f0f65626ff453eee157c401e2894e4e00f95c1c9c9cd45fa607"


def load(rel: str):
    return json.loads((BASE / rel).read_text())


def fingerprint(x: dict) -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id=x["obstruction_id"], domain=x["domain"], roles=tuple(x["roles"]),
        relations=tuple(x["relations"]), constraints=tuple(x["constraints"]),
        failure_mechanisms=tuple(x["failure_mechanisms"]),
        invariants_to_preserve=tuple(x["invariants_to_preserve"]),
        desired_transition=tuple(x["desired_transition"]), forbidden_losses=tuple(x["forbidden_losses"]),
    )


def test_b2a1c1_r3_current_v3_context_and_memory_gates() -> None:
    x = load("01_frontier/NS-B2a1c1_CONTEXT_FIBER_R3_20260812.json")
    fiber = MathContextFiber(
        atom_id=x["atom_id"], object_context=x["object_context"],
        structural_coordinates=tuple(x["structural_coordinates"]),
        equivalent_formulations=tuple(x["equivalent_formulations"]),
        solved_analogues=tuple(x["solved_analogues"]), near_solved_analogues=tuple(x["near_solved_analogues"]),
        method_transfers=tuple(MethodTransfer(
            source_context=t["source_context"], method=t["method"], shared_structure=tuple(t["shared_structure"]),
            required_assumptions=tuple(t["required_assumptions"]), disanalogies=tuple(t["disanalogies"]),
            repair_question=t["repair_question"], source_anchors=tuple(t["source_anchors"]),
        ) for t in x["method_transfers"]),
        explicit_disanalogies=tuple(x["explicit_disanalogies"]), source_anchors=tuple(x["source_anchors"]),
        analogy_scan_status=x["analogy_scan_status"], cross_domain_analogies=(), analogy_scan_notes=x["analogy_scan_notes"],
        frozen_at=x["frozen_at"], first_candidate_at=x["first_candidate_at"], packet_hash=x["packet_hash"],
    )
    assert audit_math_context_fiber(fiber).verdict is ContextGateVerdict.PASS

    m = load("07_memory/NS-B2a1c1_RESEARCH_MEMORY_REVIEW_R3_20260812.json")
    review = ResearchMemoryReview(
        target_atom_id=m["target_atom_id"], target_context_hash=m["target_context_hash"],
        tool_inventory_snapshot_hash=m["tool_inventory_snapshot_hash"], failure_lattice_snapshot_hash=m["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(m["tool_query_status"]), failure_query_status=MemoryQueryStatus(m["failure_query_status"]),
        candidate_method_families=tuple(m["candidate_method_families"]), relevant_tool_ids=tuple(m["relevant_tool_ids"]),
        relevant_failure_ids=tuple(m["relevant_failure_ids"]), selected_tool_ids=tuple(m["selected_tool_ids"]),
        tool_applicability_notes=tuple(m["tool_applicability_notes"]), failure_reuse_notes=tuple(m["failure_reuse_notes"]),
        unresolved_warnings=tuple(m["unresolved_warnings"]), evidence_pointers=tuple(m["evidence_pointers"]),
        artifact_hash=m["artifact_hash"], cross_problem_coverage_receipt_hash=m["cross_problem_coverage_receipt_hash"],
    )
    assert audit_research_memory_review(review, atom_id="NS-B2a1c1", context_hash=CTX_HASH).verdict is ResearchMemoryVerdict.PASS


def test_b2a1c1_r3_current_v3_search_gate() -> None:
    m = load("07_memory/NS-B2a1c1_OBSTRUCTION_TRANSFORMATION_MEMORY_R3_20260812.json")
    e = m["episodes"][0]
    episode = ObstructionTransformationEpisode(
        episode_id=e["episode_id"], source_domain=e["source_domain"], source_context=e["source_context"],
        source_obstruction=fingerprint(e["source_obstruction"]), transformation_name=e["transformation_name"],
        operation=e["operation"], preconditions=tuple(e["preconditions"]), resulting_relations=tuple(e["resulting_relations"]),
        preserved_invariants=tuple(e["preserved_invariants"]), relaxed_or_broken_constraints=tuple(e["relaxed_or_broken_constraints"]),
        known_breakpoints=tuple(e["known_breakpoints"]), evidence_pointers=tuple(e["evidence_pointers"]),
        authority=TransformationEpisodeAuthority(e["authority"]), artifact_hash=e["artifact_hash"], lineage_ids=tuple(e["lineage_ids"]),
    )
    memory = ObstructionTransformationMemory(
        memory_id=m["memory_id"], source_universe=tuple(m["source_universe"]), episodes=(episode,),
        evidence_pointers=tuple(m["evidence_pointers"]), snapshot_hash=m["snapshot_hash"],
    )

    r = load("07_memory/NS-B2a1c1_OBSTRUCTION_TRANSFORMATION_REVIEW_R3_20260812.json")
    w = r["direct_mapping_witnesses"][0]
    witness = StructuralMappingWitness(
        witness_id=w["witness_id"], episode_id=w["episode_id"], target_obstruction_id=w["target_obstruction_id"],
        role_mapping=tuple(tuple(v) for v in w["role_mapping"]), shared_relations=tuple(w["shared_relations"]),
        shared_constraints=tuple(w["shared_constraints"]), precondition_mapping=tuple(tuple(v) for v in w["precondition_mapping"]),
        unmatched_source_preconditions=tuple(w["unmatched_source_preconditions"]), disanalogies=tuple(w["disanalogies"]),
        target_validation_obligations=tuple(w["target_validation_obligations"]), evidence_pointers=tuple(w["evidence_pointers"]),
        artifact_hash=w["artifact_hash"],
    )
    review = ObstructionTransformationReview(
        review_id=r["review_id"], target_atom_id=r["target_atom_id"], target_context_hash=r["target_context_hash"],
        research_memory_review_hash=r["research_memory_review_hash"], episode_memory_snapshot_hash=r["episode_memory_snapshot_hash"],
        obstruction=fingerprint(r["obstruction"]), direct_search_status=RouteSearchStatus(r["direct_search_status"]),
        jump_search_status=RouteSearchStatus(r["jump_search_status"]), glue_search_status=RouteSearchStatus(r["glue_search_status"]),
        selected_mode=ShortcutMode(r["selected_mode"]), direct_candidate_episode_ids=tuple(r["direct_candidate_episode_ids"]),
        direct_mapping_witnesses=(witness,), jump_mapping_witnesses=(), glue_witness=None,
        selected_episode_ids=tuple(r["selected_episode_ids"]), exhaustion_witness=None, missing_transformation_specification=None,
        unresolved_warnings=tuple(r["unresolved_warnings"]), evidence_pointers=tuple(r["evidence_pointers"]), artifact_hash=r["artifact_hash"],
    )
    report = audit_obstruction_transformation_review(
        review, atom_id="NS-B2a1c1", context_hash=CTX_HASH, research_memory_review_hash=MEM_HASH,
        transformation_memory=memory,
    )
    assert report.verdict is ShortcutReviewVerdict.PASS
    assert report.selected_mode is ShortcutMode.SEARCH


def _entry(x: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
        event_id=x["event_id"], atom_id=x["atom_id"], event_type=ResearchTraceEventType(x["event_type"]), timestamp=x["timestamp"],
        state_summary=x["state_summary"], action_summary=x["action_summary"], evidence_pointers=tuple(x["evidence_pointers"]),
        alternatives_considered=tuple(x["alternatives_considered"]), decision_rationale=x["decision_rationale"], outputs=tuple(x["outputs"]),
        uncertainties=tuple(x["uncertainties"]), residuals=tuple(x["residuals"]), next_steps=tuple(x["next_steps"]),
        artifact_hash=x["artifact_hash"], previous_event_hash=x["previous_event_hash"],
    )


def test_b2a1c1_r3_current_v3_trace_and_episode() -> None:
    pre = load("09_trace/NS-B2a1c1_PRE_CANDIDATE_TRACE_R3_20260812.json")
    result = load("09_trace/NS-B2a1c1_RESULT_TRACE_R3_20260812.json")
    pre_trace = MathResearchTrace(pre["trace_id"], tuple(_entry(x) for x in pre["entries"]))
    assert audit_pre_candidate_trace(pre_trace, atom_id="NS-B2a1c1", context_packet_hash=CTX_HASH, obstruction_transformation_review_hash=OTR_HASH).verdict is TraceGateVerdict.PASS
    full = MathResearchTrace("TRACE-NS-B2a1c1-R3-FULL", tuple(_entry(x) for x in pre["entries"] + result["entries"]))
    assert audit_research_trace(full).verdict is TraceGateVerdict.PASS

    x = load("07_memory/NS-B2a1c1_TASK_EPISODE_R3_20260812.json")
    ep = TaskEpisode(
        episode_id=x["episode_id"], task_id=x["task_id"], atom_id=x["atom_id"], context_hash=x["context_hash"],
        problem_signature=tuple(x["problem_signature"]), fibre_snapshot_hash=x["fibre_snapshot_hash"], operator_ids=tuple(x["operator_ids"]),
        action_trace=tuple(x["action_trace"]), observation_ids=tuple(x["observation_ids"]), verification_ids=tuple(x["verification_ids"]),
        outcome=EpisodeOutcome(x["outcome"]), residual_signature=tuple(x["residual_signature"]), evidence_pointers=tuple(x["evidence_pointers"]),
        artifact_hash=x["artifact_hash"], timestamp=x["timestamp"], cost=x["cost"], storage_admission=EpisodeStorageAdmission(x["storage_admission"]),
    )
    assert validate_episode(ep) == ()
    assert ep.storage_admission is EpisodeStorageAdmission.PROPOSAL_SHADOW_STORED

    dag = load("02_problem_dag/NS_B2A1C1_DELTA_20260812.json")
    assert dag["candidate"].endswith("R3")
    assert dag["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
