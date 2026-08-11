from __future__ import annotations

from rakl.math_context import AnalogyScanStatus, MathContextFiber, MethodTransfer
from rakl.math_research_assurance import AssuranceVerdict, MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
)
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


ATOM = "synthetic-obstruction-gate-migration"
CONTEXT_HASH = "sha256:synthetic-context"
MEMORY_REVIEW_HASH = "sha256:synthetic-memory-review"
SHORTCUT_REVIEW_HASH = "sha256:synthetic-shortcut-review"


def _context() -> MathContextFiber:
    return MathContextFiber(
        atom_id=ATOM,
        object_context="synthetic current-gate obstruction used only for conformance",
        structural_coordinates=("finite state", "typed dependency"),
        equivalent_formulations=("a typed state blocks a registered obligation",),
        solved_analogues=("verified finite proof-state compression example",),
        method_transfers=(
            MethodTransfer(
                source_context="verified finite proof-state compression example",
                method="compress equivalent proof states",
                shared_structure=("finite typed dependency",),
                required_assumptions=("registered statement remains fixed",),
                disanalogies=("source and target statement identities differ",),
                repair_question="does compression preserve the exact target statement?",
                source_anchors=("synthetic-test:source",),
            ),
        ),
        explicit_disanalogies=("synthetic conformance is not mathematical evidence",),
        source_anchors=("synthetic-test:source",),
        analogy_scan_status=AnalogyScanStatus.NO_SAFE_BRIDGE_FOUND.value,
        analogy_scan_notes="bounded scan completed for this synthetic conformance fixture",
        frozen_at="2026-08-12T00:00:00+00:00",
        first_candidate_at="2026-08-12T00:20:00+00:00",
        packet_hash=CONTEXT_HASH,
    )


def _experience_memory_review() -> ResearchMemoryReview:
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=CONTEXT_HASH,
        tool_inventory_snapshot_hash="sha256:synthetic-tools",
        failure_lattice_snapshot_hash="sha256:synthetic-failures",
        tool_query_status=MemoryQueryStatus.NO_RELEVANT_MATCH,
        failure_query_status=MemoryQueryStatus.NO_RELEVANT_MATCH,
        candidate_method_families=("proof-state compression",),
        unresolved_warnings=("synthetic fixture grants no mathematical authority",),
        evidence_pointers=("synthetic-test:tools", "synthetic-test:failures"),
        artifact_hash=MEMORY_REVIEW_HASH,
    )


def _obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="synthetic-obstruction",
        domain="mathematics",
        roles=("proof state", "proof obligation"),
        relations=("state blocks obligation",),
        constraints=("registered statement remains fixed",),
        failure_mechanisms=("duplicate search branches",),
        invariants_to_preserve=("formal statement meaning",),
        desired_transition=("reduce search branching",),
        forbidden_losses=("formal statement meaning",),
    )


def _transformation_memory_and_review():
    episode = ObstructionTransformationEpisode(
        episode_id="synthetic-direct-episode",
        source_domain="mathematics",
        source_context="verified finite proof-state compression example",
        source_obstruction=_obstruction(),
        transformation_name="compress equivalent proof states",
        operation="replace duplicate branches with one typed aggregate state",
        preconditions=("registered statement remains fixed",),
        resulting_relations=("reduce search branching",),
        preserved_invariants=("formal statement meaning",),
        relaxed_or_broken_constraints=(),
        known_breakpoints=("statement changes during compression",),
        evidence_pointers=("synthetic-test:episode",),
        authority=TransformationEpisodeAuthority.SOURCE_EVENT_VERIFIED,
        artifact_hash="sha256:synthetic-direct-episode",
    )
    transformation_memory = build_transformation_memory(
        memory_id="synthetic-transformation-memory",
        source_universe=("mathematics", "science", "engineering", "ordinary situations"),
        episodes=(episode,),
        evidence_pointers=("synthetic-test:transformation-memory",),
    )
    mapping = StructuralMappingWitness(
        witness_id="synthetic-direct-mapping",
        episode_id=episode.episode_id,
        target_obstruction_id="synthetic-obstruction",
        role_mapping=(("proof state", "proof state"), ("proof obligation", "proof obligation")),
        shared_relations=("state blocks obligation",),
        shared_constraints=("registered statement remains fixed",),
        precondition_mapping=(("registered statement remains fixed", "registered statement remains fixed"),),
        unmatched_source_preconditions=(),
        disanalogies=("source and target statement identities differ",),
        target_validation_obligations=("check target statement preservation",),
        evidence_pointers=("synthetic-test:mapping",),
        artifact_hash="sha256:synthetic-direct-mapping",
    )
    review = ObstructionTransformationReview(
        review_id="synthetic-shortcut-review",
        target_atom_id=ATOM,
        target_context_hash=CONTEXT_HASH,
        research_memory_review_hash=MEMORY_REVIEW_HASH,
        episode_memory_snapshot_hash=transformation_memory.snapshot_hash,
        obstruction=_obstruction(),
        direct_search_status=RouteSearchStatus.MATCHES_FOUND,
        jump_search_status=RouteSearchStatus.NOT_RUN,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.SEARCH,
        direct_candidate_episode_ids=(episode.episode_id,),
        direct_mapping_witnesses=(mapping,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=("target validation remains mandatory",),
        evidence_pointers=("synthetic-test:transformation-memory",),
        artifact_hash=SHORTCUT_REVIEW_HASH,
    )
    return transformation_memory, review


def _trace() -> MathResearchTrace:
    event_types = (
        ResearchTraceEventType.ATOMIZED,
        ResearchTraceEventType.CONTEXT_FROZEN,
        ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
        ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    )
    entries = []
    previous_hash = ""
    for index, event_type in enumerate(event_types, start=1):
        artifact_hash = f"sha256:synthetic-event-{index}"
        outputs = (f"synthetic-output:{index}",)
        if event_type is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            outputs = (MEMORY_REVIEW_HASH,)
        elif event_type is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            outputs = (SHORTCUT_REVIEW_HASH,)
        entries.append(
            ResearchTraceEntry(
                event_id=f"synthetic-event-{index}",
                atom_id=ATOM,
                event_type=event_type,
                timestamp=f"2026-08-12T00:{index:02d}:00+00:00",
                state_summary=f"synthetic state {index}",
                action_summary=f"synthetic action {index}",
                evidence_pointers=(CONTEXT_HASH,)
                if event_type is ResearchTraceEventType.CONTEXT_FROZEN
                else (f"synthetic-test:evidence-{index}",),
                alternatives_considered=("continue", "stop"),
                decision_rationale="bounded synthetic conformance rationale",
                outputs=outputs,
                uncertainties=("no mathematical authority",),
                next_steps=("run the current gate",),
                artifact_hash=artifact_hash,
                previous_event_hash=previous_hash,
            )
        )
        previous_hash = artifact_hash
    return MathResearchTrace(trace_id="synthetic-current-gate-trace", entries=tuple(entries))


def test_synthetic_current_gate_passes_without_mathematical_credit() -> None:
    transformation_memory, shortcut_review = _transformation_memory_and_review()
    record = MathResearchRecord(claim_id=ATOM)
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("synthetic proof state", "synthetic proof obligation"),
            relations=("state blocks obligation",),
            domain="mathematical assurance conformance",
            goal_type="exercise the current obstruction-transformation gate",
        ),
        record=record,
        context_fiber=_context(),
        memory_review=_experience_memory_review(),
        transformation_memory=transformation_memory,
        shortcut_review=shortcut_review,
        research_trace=_trace(),
    )

    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert plan.assurance.verdict is AssuranceVerdict.CANNOT_CHECK
    assert "semantic_shortcut_mode:SEARCH" in plan.planning_state.facts

