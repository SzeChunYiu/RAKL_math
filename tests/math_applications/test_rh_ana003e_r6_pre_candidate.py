from __future__ import annotations

import json
from pathlib import Path

from rakl.math_context import CrossDomainAnalogy, MathContextFiber, MethodTransfer, ContextGateVerdict
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview, ResearchMemoryVerdict
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
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
CTX = RH / "01_frontier/RH_ANA_003e_CONTEXT_FIBER_20260812_R6.json"
MEM = RH / "07_memory/RH_ANA_003e_RESEARCH_MEMORY_REVIEW_20260812_R6.json"
TM = RH / "07_memory/RH_ANA_003e_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812_R6.json"
REV = RH / "08_reviews/RH_ANA_003e_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812_R6.json"
TRACE = RH / "09_trace/RH_ANA_003e_PRE_CANDIDATE_TRACE_20260812_R6.json"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _ob(raw: dict) -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id=raw["obstruction_id"], domain=raw["domain"],
        roles=tuple(raw["roles"]), relations=tuple(raw["relations"]),
        constraints=tuple(raw["constraints"]), failure_mechanisms=tuple(raw["failure_mechanisms"]),
        invariants_to_preserve=tuple(raw["invariants_to_preserve"]),
        desired_transition=tuple(raw["desired_transition"]),
        forbidden_losses=tuple(raw.get("forbidden_losses", [])),
    )


def _context() -> MathContextFiber:
    r = _load(CTX)
    transfers = tuple(MethodTransfer(
        source_context=x["source_context"], method=x["method"], shared_structure=tuple(x["shared_structure"]),
        required_assumptions=tuple(x["required_assumptions"]), disanalogies=tuple(x["disanalogies"]),
        repair_question=x["repair_question"], source_anchors=tuple(x["source_anchors"]),
    ) for x in r["method_transfers"])
    analogies = tuple(CrossDomainAnalogy(
        source_kind=x["source_kind"], source_situation=x["source_situation"], common_abstraction=tuple(x["common_abstraction"]),
        source_to_target_mapping=tuple(x["source_to_target_mapping"]), shared_constraints=tuple(x["shared_constraints"]),
        disanalogies=tuple(x["disanalogies"]), proposed_principle=x["proposed_principle"],
        validation_obligation=x["validation_obligation"], provenance_note=x["provenance_note"],
    ) for x in r["cross_domain_analogies"])
    return MathContextFiber(
        atom_id=r["atom_id"], object_context=r["object_context"], structural_coordinates=tuple(r["structural_coordinates"]),
        equivalent_formulations=tuple(r["equivalent_formulations"]), solved_analogues=tuple(r["solved_analogues"]),
        near_solved_analogues=tuple(r["near_solved_analogues"]), method_transfers=transfers,
        explicit_disanalogies=tuple(r["explicit_disanalogies"]), source_anchors=tuple(r["source_anchors"]),
        analogy_scan_status=r["analogy_scan_status"], cross_domain_analogies=analogies,
        analogy_scan_notes=r["analogy_scan_notes"], frozen_at=r["frozen_at"], first_candidate_at=r["first_candidate_at"],
        packet_hash=r["packet_hash"],
    )


def _memory() -> ResearchMemoryReview:
    r = _load(MEM)
    return ResearchMemoryReview(
        target_atom_id=r["target_atom_id"], target_context_hash=r["target_context_hash"],
        tool_inventory_snapshot_hash=r["tool_inventory_snapshot_hash"], failure_lattice_snapshot_hash=r["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(r["tool_query_status"]), failure_query_status=MemoryQueryStatus(r["failure_query_status"]),
        candidate_method_families=tuple(r["candidate_method_families"]), relevant_tool_ids=tuple(r["relevant_tool_ids"]),
        relevant_failure_ids=tuple(r["relevant_failure_ids"]), selected_tool_ids=tuple(r["selected_tool_ids"]),
        tool_applicability_notes=tuple(r["tool_applicability_notes"]), failure_reuse_notes=tuple(r["failure_reuse_notes"]),
        unresolved_warnings=tuple(r["unresolved_warnings"]), evidence_pointers=tuple(r["evidence_pointers"]), artifact_hash=r["artifact_hash"],
    )


def _tm_and_review():
    tm = _load(TM)
    episodes = []
    for x in tm["episodes"]:
        episodes.append(ObstructionTransformationEpisode(
            episode_id=x["episode_id"], source_domain=x["source_domain"], source_context=x["source_context"],
            source_obstruction=_ob(x["source_obstruction"]), transformation_name=x["transformation_name"], operation=x["operation"],
            preconditions=tuple(x["preconditions"]), resulting_relations=tuple(x["resulting_relations"]),
            preserved_invariants=tuple(x["preserved_invariants"]), relaxed_or_broken_constraints=tuple(x["relaxed_or_broken_constraints"]),
            known_breakpoints=tuple(x["known_breakpoints"]), evidence_pointers=tuple(x["evidence_pointers"]),
            authority=TransformationEpisodeAuthority(x["authority"]), artifact_hash=x["artifact_hash"], lineage_ids=tuple(x.get("lineage_ids", [])),
        ))
    built = build_transformation_memory(memory_id=tm["memory_id"], source_universe=tuple(tm["source_universe"]), episodes=tuple(episodes), evidence_pointers=tuple(tm["evidence_pointers"]))
    assert built.snapshot_hash == tm["snapshot_hash"]
    r = _load(REV)
    maps = tuple(StructuralMappingWitness(
        witness_id=x["witness_id"], episode_id=x["episode_id"], target_obstruction_id=x["target_obstruction_id"],
        role_mapping=tuple(tuple(y) for y in x["role_mapping"]), shared_relations=tuple(x["shared_relations"]),
        shared_constraints=tuple(x["shared_constraints"]), precondition_mapping=tuple(tuple(y) for y in x["precondition_mapping"]),
        unmatched_source_preconditions=tuple(x["unmatched_source_preconditions"]), disanalogies=tuple(x["disanalogies"]),
        target_validation_obligations=tuple(x["target_validation_obligations"]), evidence_pointers=tuple(x["evidence_pointers"]), artifact_hash=x["artifact_hash"],
    ) for x in r["direct_mapping_witnesses"])
    review = ObstructionTransformationReview(
        review_id=r["review_id"], target_atom_id=r["target_atom_id"], target_context_hash=r["target_context_hash"],
        research_memory_review_hash=r["research_memory_review_hash"], episode_memory_snapshot_hash=r["episode_memory_snapshot_hash"],
        obstruction=_ob(r["obstruction"]), direct_search_status=RouteSearchStatus(r["direct_search_status"]),
        jump_search_status=RouteSearchStatus(r["jump_search_status"]), glue_search_status=RouteSearchStatus(r["glue_search_status"]),
        selected_mode=ShortcutMode(r["selected_mode"]), direct_candidate_episode_ids=tuple(r["direct_candidate_episode_ids"]),
        direct_mapping_witnesses=maps, selected_episode_ids=tuple(r["selected_episode_ids"]),
        unresolved_warnings=tuple(r["unresolved_warnings"]), evidence_pointers=tuple(r["evidence_pointers"]), artifact_hash=r["artifact_hash"],
    )
    return built, review


def _trace() -> MathResearchTrace:
    r = _load(TRACE)
    entries = tuple(ResearchTraceEntry(
        event_id=x["event_id"], atom_id=x["atom_id"], event_type=ResearchTraceEventType(x["event_type"]), timestamp=x["timestamp"],
        state_summary=x["state_summary"], action_summary=x["action_summary"], evidence_pointers=tuple(x["evidence_pointers"]),
        alternatives_considered=tuple(x["alternatives_considered"]), decision_rationale=x["decision_rationale"], outputs=tuple(x["outputs"]),
        uncertainties=tuple(x["uncertainties"]), residuals=tuple(x["residuals"]), next_steps=tuple(x["next_steps"]),
        artifact_hash=x["artifact_hash"], previous_event_hash=x["previous_event_hash"],
    ) for x in r["entries"])
    return MathResearchTrace(trace_id=r["trace_id"], entries=entries)


def test_rh_ana003e_r6_current_v3_pre_candidate_gate_passes() -> None:
    ctx = _context(); mem = _memory(); tm, review = _tm_and_review(); trace = _trace()
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("Coffey moving prefix P_n(X_n)", "R5 ordered tail T_n(X_n)", "full S_Lambda(n)", "polynomial growth obligation"),
            relations=("S_Lambda=P+T", "T is superpolynomially small in the frozen R5 premise", "test obligation strength before estimation"),
            domain="analytic number theory", goal_type="falsify disguised root-strength moving-prefix obligations before candidate estimation",
        ),
        record=MathResearchRecord(claim_id="RH-ANA-003e"), context_fiber=ctx, memory_review=mem,
        transformation_memory=tm, shortcut_review=review, research_trace=trace,
    )
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.shortcut_gate.selected_mode is ShortcutMode.SEARCH
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert "semantic_shortcut_mode:SEARCH" in plan.planning_state.facts
