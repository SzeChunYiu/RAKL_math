from __future__ import annotations

import json
from pathlib import Path

from rakl.experience_substrate import (
    EpisodeOutcome,
    EpisodeStorageAdmission,
    InventoryAdmissionVerdict,
    TaskEpisode,
    resolve_inventory_admission,
    validate_episode,
)
from rakl.math_context import (
    AnalogyScanStatus,
    CrossDomainAnalogy,
    MathContextFiber,
    MethodTransfer,
)
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict
from rakl.semantic_shortcut import (
    ObstructionFingerprint,
    ObstructionTransformationEpisode,
    ObstructionTransformationReview,
    RouteSearchStatus,
    ShortcutMode,
    ShortcutReviewVerdict,
    StructuralMappingWitness,
    TransformationEpisodeAuthority,
    build_transformation_memory,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"


def _load(rel: str):
    return json.loads((BASE / rel).read_text())


def test_b2a1c_current_v3_packet_routes_jump_and_allows_frozen_verification() -> None:
    c = _load("01_frontier/NS-B2a1c_CONTEXT_FIBER_R2_20260812.json")
    m = _load("07_memory/NS-B2a1c_RESEARCH_MEMORY_REVIEW_R2_20260812.json")
    tm = _load("07_memory/NS-B2a1c_OBSTRUCTION_TRANSFORMATION_MEMORY_R2_20260812.json")
    sr = _load("07_memory/NS-B2a1c_OBSTRUCTION_TRANSFORMATION_REVIEW_R2_20260812.json")
    tr = _load("09_trace/NS-B2a1c_TRACE_R2_20260812.json")

    fiber = MathContextFiber(
        atom_id=c["atom_id"], object_context=c["object_context"],
        structural_coordinates=tuple(c["structural_coordinates"]), equivalent_formulations=tuple(c["equivalent_formulations"]),
        solved_analogues=tuple(c["solved_analogues"]), near_solved_analogues=tuple(c["near_solved_analogues"]),
        method_transfers=tuple(MethodTransfer(source_context=x["source_context"], method=x["method"], shared_structure=tuple(x["shared_structure"]), required_assumptions=tuple(x["required_assumptions"]), disanalogies=tuple(x["disanalogies"]), repair_question=x["repair_question"], source_anchors=tuple(x["source_anchors"])) for x in c["method_transfers"]),
        explicit_disanalogies=tuple(c["explicit_disanalogies"]), source_anchors=tuple(c["source_anchors"]),
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=tuple(CrossDomainAnalogy(source_kind=x["source_kind"], source_situation=x["source_situation"], common_abstraction=tuple(x["common_abstraction"]), source_to_target_mapping=tuple(x["source_to_target_mapping"]), shared_constraints=tuple(x["shared_constraints"]), disanalogies=tuple(x["disanalogies"]), proposed_principle=x["proposed_principle"], validation_obligation=x["validation_obligation"], provenance_note=x["provenance_note"]) for x in c["cross_domain_analogies"]),
        analogy_scan_notes=c["analogy_scan_notes"], frozen_at=c["frozen_at"], first_candidate_at=c["first_candidate_at"], packet_hash=c["packet_hash"],
    )
    memory = ResearchMemoryReview(
        target_atom_id=m["target_atom_id"], target_context_hash=m["target_context_hash"], tool_inventory_snapshot_hash=m["tool_inventory_snapshot_hash"], failure_lattice_snapshot_hash=m["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(m["tool_query_status"]), failure_query_status=MemoryQueryStatus(m["failure_query_status"]), candidate_method_families=tuple(m["candidate_method_families"]),
        relevant_tool_ids=tuple(m["relevant_tool_ids"]), relevant_failure_ids=tuple(m["relevant_failure_ids"]), selected_tool_ids=tuple(m["selected_tool_ids"]), tool_applicability_notes=tuple(m["tool_applicability_notes"]), failure_reuse_notes=tuple(m["failure_reuse_notes"]), unresolved_warnings=tuple(m["unresolved_warnings"]), evidence_pointers=tuple(m["evidence_pointers"]), artifact_hash=m["artifact_hash"], cross_problem_coverage_receipt_hash=m["cross_problem_coverage_receipt_hash"],
    )
    so = tm["episodes"][0]["source_obstruction"]
    source_obstruction = ObstructionFingerprint(obstruction_id=so["obstruction_id"], domain=so["domain"], roles=tuple(so["roles"]), relations=tuple(so["relations"]), constraints=tuple(so["constraints"]), failure_mechanisms=tuple(so["failure_mechanisms"]), invariants_to_preserve=tuple(so["invariants_to_preserve"]), desired_transition=tuple(so["desired_transition"]), forbidden_losses=tuple(so["forbidden_losses"]))
    e = tm["episodes"][0]
    episode = ObstructionTransformationEpisode(episode_id=e["episode_id"], source_domain=e["source_domain"], source_context=e["source_context"], source_obstruction=source_obstruction, transformation_name=e["transformation_name"], operation=e["operation"], preconditions=tuple(e["preconditions"]), resulting_relations=tuple(e["resulting_relations"]), preserved_invariants=tuple(e["preserved_invariants"]), relaxed_or_broken_constraints=tuple(e["relaxed_or_broken_constraints"]), known_breakpoints=tuple(e["known_breakpoints"]), evidence_pointers=tuple(e["evidence_pointers"]), authority=TransformationEpisodeAuthority(e["authority"]), artifact_hash=e["artifact_hash"], lineage_ids=tuple(e["lineage_ids"]))
    transformation_memory = build_transformation_memory(memory_id=tm["memory_id"], source_universe=tuple(tm["source_universe"]), episodes=(episode,), evidence_pointers=tuple(tm["evidence_pointers"]))
    assert transformation_memory.snapshot_hash == tm["snapshot_hash"]

    o = sr["obstruction"]
    target = ObstructionFingerprint(obstruction_id=o["obstruction_id"], domain=o["domain"], roles=tuple(o["roles"]), relations=tuple(o["relations"]), constraints=tuple(o["constraints"]), failure_mechanisms=tuple(o["failure_mechanisms"]), invariants_to_preserve=tuple(o["invariants_to_preserve"]), desired_transition=tuple(o["desired_transition"]), forbidden_losses=tuple(o["forbidden_losses"]))
    w = sr["jump_mapping_witnesses"][0]
    witness = StructuralMappingWitness(witness_id=w["witness_id"], episode_id=w["episode_id"], target_obstruction_id=w["target_obstruction_id"], role_mapping=tuple(tuple(x) for x in w["role_mapping"]), shared_relations=tuple(w["shared_relations"]), shared_constraints=tuple(w["shared_constraints"]), precondition_mapping=tuple(tuple(x) for x in w["precondition_mapping"]), unmatched_source_preconditions=tuple(w["unmatched_source_preconditions"]), disanalogies=tuple(w["disanalogies"]), target_validation_obligations=tuple(w["target_validation_obligations"]), evidence_pointers=tuple(w["evidence_pointers"]), artifact_hash=w["artifact_hash"])
    shortcut = ObstructionTransformationReview(review_id=sr["review_id"], target_atom_id=sr["target_atom_id"], target_context_hash=sr["target_context_hash"], research_memory_review_hash=sr["research_memory_review_hash"], episode_memory_snapshot_hash=sr["episode_memory_snapshot_hash"], obstruction=target, direct_search_status=RouteSearchStatus(sr["direct_search_status"]), jump_search_status=RouteSearchStatus(sr["jump_search_status"]), glue_search_status=RouteSearchStatus(sr["glue_search_status"]), selected_mode=ShortcutMode(sr["selected_mode"]), jump_mapping_witnesses=(witness,), selected_episode_ids=tuple(sr["selected_episode_ids"]), unresolved_warnings=tuple(sr["unresolved_warnings"]), evidence_pointers=tuple(sr["evidence_pointers"]), artifact_hash=sr["artifact_hash"])

    entries = tuple(ResearchTraceEntry(event_id=x["event_id"], atom_id=x["atom_id"], event_type=ResearchTraceEventType(x["event_type"]), timestamp=x["timestamp"], state_summary=x["state_summary"], action_summary=x["action_summary"], evidence_pointers=tuple(x["evidence_pointers"]), alternatives_considered=tuple(x["alternatives_considered"]), decision_rationale=x["decision_rationale"], outputs=tuple(x["outputs"]), uncertainties=tuple(x["uncertainties"]), residuals=tuple(x["residuals"]), next_steps=tuple(x["next_steps"]), artifact_hash=x["artifact_hash"], previous_event_hash=x["previous_event_hash"]) for x in tr["entries"])
    trace = MathResearchTrace(trace_id=tr["trace_id"], entries=entries)
    plan = plan_math_research(signature=ProblemSignature(objects=("F=1 ancient Euler producer","Section-4 cutoff consumer"), relations=("3/s1+2/l1=4","l1<=s1","condition (4.4)"), domain="Navier-Stokes Type-II source-interface audit", goal_type="verify producer-consumer asymptotic compatibility"), record=MathResearchRecord(claim_id="NS-B2a1c"), context_fiber=fiber, memory_review=memory, transformation_memory=transformation_memory, shortcut_review=shortcut, research_trace=trace)
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed is True
    assert "semantic_shortcut_mode:JUMP" in plan.planning_state.facts


def test_b2a1c_exact_algebra_and_shadow_episode_authority() -> None:
    # From l1<=s1 and 3/s1+2/l1=4: 4<=5/l1, hence l1<=5/4.
    l1_max = 5 / 4
    beta_min = 2 - (3 / 2) * l1_max
    assert beta_min == 1 / 8
    assert l1_max < 4 / 3  # beta<0 would require l1>4/3.

    raw = _load("07_memory/NS-B2a1c_TASK_EPISODE_R2_20260812.json")
    episode = TaskEpisode(episode_id=raw["episode_id"], task_id=raw["task_id"], atom_id=raw["atom_id"], context_hash=raw["context_hash"], problem_signature=tuple(raw["problem_signature"]), fibre_snapshot_hash=raw["fibre_snapshot_hash"], operator_ids=tuple(raw["operator_ids"]), action_trace=tuple(raw["action_trace"]), observation_ids=tuple(raw["observation_ids"]), verification_ids=tuple(raw["verification_ids"]), outcome=EpisodeOutcome(raw["outcome"]), residual_signature=tuple(raw["residual_signature"]), evidence_pointers=tuple(raw["evidence_pointers"]), artifact_hash=raw["artifact_hash"], timestamp=raw["timestamp"], cost=raw["cost"], storage_admission=EpisodeStorageAdmission(raw["storage_admission"]))
    assert validate_episode(episode) == ()
    admission = resolve_inventory_admission(episode)
    assert admission.verdict is InventoryAdmissionVerdict.PROPOSAL_SHADOW_STORED
    assert admission.retained_for_search is True
    assert admission.counts_toward_canonical_inventory is False
