from __future__ import annotations

import hashlib
import json

from rakl.math_context import AnalogyScanStatus, MathContextFiber, MethodTransfer
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType
from rakl.semantic_shortcut import (
    ObstructionFingerprint,
    ObstructionTransformationEpisode,
    ObstructionTransformationReview,
    RouteSearchStatus,
    ShortcutMode,
    StructuralMappingWitness,
    TransformationEpisodeAuthority,
    build_transformation_memory,
)

ATOM = "O9d12a2a1b-C043"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
APPLICATION_BASE_SHA = "9074c257e4fd3179c56ffdedc859efc972cd1c88"


def _hash(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _context() -> MathContextFiber:
    payload = {
        "atom_id": ATOM,
        "object_context": "Post-C042 re-entry atom for the explicit C041 SAT/UNSAT recursive graph family: test whether later levels escape cheap exact full-cover structure before any renewed lower-bound amplification search.",
        "structural_coordinates": (
            "C041 recursive complement U_n and G_n=[2^n]^2\\U_n",
            "canonical MAGIC long-form old-to-new 3CNF encoding",
            "full Definition-21 cover complexity rho(G_n,G_NN)",
            "cyclic intersection complexity",
            "row and column complement-neighborhood twin types",
            "type-class cover upper construction",
            "N=2^n root-facing rate coordinate",
        ),
        "equivalent_formulations": (
            "Cavalar-Oliveira Theorem 30 exact equality between cover complexity and cyclic intersection complexity for non-trivial A and non-empty B",
            "Definition-21 cover graph as set cover over legal pair vertices and relevant semi-filters",
            "exact bipartite complement adjacency modulo row/column neighborhood types",
        ),
        "solved_analogues": (
            "Cavalar-Oliveira Theorem 30 exact cyclic-to-cover characterization",
            "C042 finite G9/G13 exact twin quotients with quotient cover number two",
        ),
        "near_solved_analogues": (
            "C041A exact odd-slice copy zero-augmentation",
            "XM015 exact first-step full-target fractional reoptimization caution; not strict current-gate authority",
        ),
        "explicit_disanalogies": (
            "SAT semantic hardness is not cover hardness",
            "finite G9/G13 quotient collapse is not a uniform quotient theorem",
            "type-count growth alone does not imply rho growth",
            "fractional packing does not control integral cover without a proved bridge",
        ),
        "source_anchors": (
            "ECCC-TR25-033:Definition21",
            "ECCC-TR25-033:Theorem30",
            "RAKL_math:C041",
            "RAKL_math:C042",
        ),
    }
    packet_hash = _hash(payload)
    transfer = MethodTransfer(
        source_context="Cavalar-Oliveira ECCC TR25-033 Definition 21 and Theorem 30",
        method="replace the cyclic intersection-complexity obligation by its exactly equal full cover-complexity representation before selecting a lower-bound operator",
        shared_structure=("same graph target", "same row/column generator basis", "same unrestricted Definition-21 pair universe"),
        required_assumptions=("target is non-trivial", "generator family is non-empty", "full cover object is retained"),
        disanalogies=("the theorem changes representation but supplies no lower bound", "finite quotient compression may keep rho small after semantic activation"),
        repair_question="what is the cheapest source-valid full-cover upper-bound discriminator after exact representation?",
        source_anchors=("ECCC-TR25-033:Definition21", "ECCC-TR25-033:Theorem30"),
    )
    return MathContextFiber(
        atom_id=ATOM,
        object_context=payload["object_context"],
        structural_coordinates=payload["structural_coordinates"],
        equivalent_formulations=payload["equivalent_formulations"],
        solved_analogues=payload["solved_analogues"],
        near_solved_analogues=payload["near_solved_analogues"],
        method_transfers=(transfer,),
        explicit_disanalogies=payload["explicit_disanalogies"],
        source_anchors=payload["source_anchors"],
        analogy_scan_status=AnalogyScanStatus.NO_SAFE_BRIDGE_FOUND.value,
        analogy_scan_notes="Same-domain exact characterization dominates. Cross-Millennium material was not used as a strict route; XM015 is retained only as a current-work caution because its own current-gate chronology is CANNOT_CHECK_STRICT.",
        frozen_at="2026-08-12T00:04:00+00:00",
        first_candidate_at=None,
        packet_hash=packet_hash,
    )


def _memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {
        "atom": ATOM,
        "context": context_hash,
        "tools": ["T-PNP-FRACTIONAL-SEMIFILTER-PACKING"],
        "failures": [
            "F-C042-SYNTAX-ACTIVATION-NO-UNSAT-SIGNAL",
            "F-C042-FIRST-UNSAT-QUOTIENT-COMPRESSION",
            "F-C024-FRACTIONAL-INTEGRALITY-GAP",
        ],
        "policy": "C042 quotient compression changes routing to a cheap exact upper-bound/type gate before any LP; C024 rejects treating fractional packing as an integral recurrence.",
    }
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash="gitblob:4797c50cf9345ce09be0206a4ace5a7f9b01d93a",
        failure_lattice_snapshot_hash="gitblob:76d7f20f181f345869b4a29eb9ff8cab445fd32a",
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=("exact cover representation", "neighborhood-type upper gate", "fractional semi-filter packing"),
        relevant_tool_ids=("T-PNP-FRACTIONAL-SEMIFILTER-PACKING",),
        relevant_failure_ids=tuple(payload["failures"]),
        selected_tool_ids=(),
        tool_applicability_notes=("Fractional packing is valid later but rejected for the immediate action because a source-valid exact cover upper gate is cheaper and prior integral/fractional failures are active.",),
        failure_reuse_notes=(
            "F-C042-FIRST-UNSAT-QUOTIENT-COMPRESSION changes routing: inspect exact later neighborhood types before any LP.",
            "F-C042-SYNTAX-ACTIVATION-NO-UNSAT-SIGNAL prevents parser activation from being scored as obstruction activation.",
            "F-C024-FRACTIONAL-INTEGRALITY-GAP prevents fractional-to-integral recurrence inference.",
        ),
        unresolved_warnings=("C042 is negative history, not retroactively current-Gate-C discovery authority.", "Later-level asymptotics remain open."),
        evidence_pointers=(
            "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C041_TOOL_SNAPSHOT_20260811.json",
            "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C042_ACTIVATION_QUOTIENT_FAILURE_DELTA_20260812.json",
            "RAKL_math:PR191",
        ),
        artifact_hash=_hash(payload),
    )


def _obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="O-PNP-C043-CYCLIC-TO-COVER-REENTRY",
        domain="mathematics / circuit complexity / two-dimensional cover",
        roles=("root-facing cyclic-intersection obligation", "exact cover-complexity surrogate"),
        relations=("cover complexity is exact surrogate for cyclic intersection complexity",),
        constraints=("target set non-trivial", "generator family non-empty", "same graph family and generator basis fixed"),
        failure_mechanisms=("direct lower-bound search can spend effort before checking exact cover-representation structure",),
        invariants_to_preserve=("exact target graph", "generator basis", "upper/lower-bound direction", "root authority boundary"),
        desired_transition=("replace cyclic intersection-complexity obligation by exactly equal cover-complexity obligation",),
        forbidden_losses=("restricted-cover substitution", "finite computation treated as asymptotic proof"),
    )


def _transformation_memory_and_review(context_hash: str, memory_hash: str):
    source_obstruction = ObstructionFingerprint(
        obstruction_id="SRC-CO25-CYCLIC-COVER-CHARACTERIZATION",
        domain="mathematics / circuit complexity / two-dimensional cover",
        roles=("cyclic intersection-complexity target", "cover-complexity object"),
        relations=("cover complexity is exact surrogate for cyclic intersection complexity",),
        constraints=("target set non-trivial", "generator family non-empty", "same graph family and generator basis fixed"),
        failure_mechanisms=("direct lower-bound search can spend effort before checking exact cover-representation structure",),
        invariants_to_preserve=("exact target graph", "generator basis", "upper/lower-bound direction", "root authority boundary"),
        desired_transition=("replace cyclic intersection-complexity obligation by exactly equal cover-complexity obligation",),
    )
    episode = ObstructionTransformationEpisode(
        episode_id="OT-PNP-CO25-THEOREM30-CYCLIC-TO-COVER",
        source_domain=source_obstruction.domain,
        source_context="Cavalar-Oliveira ECCC TR25-033 Definition 21 and Theorem 30",
        source_obstruction=source_obstruction,
        transformation_name="exact cyclic-to-cover representation",
        operation="replace cyclic intersection complexity by rho(A,B) with the same A and B",
        preconditions=("target set non-trivial", "generator family non-empty"),
        resulting_relations=("replace cyclic intersection-complexity obligation by exactly equal cover-complexity obligation",),
        preserved_invariants=("exact target graph", "generator basis", "upper/lower-bound direction", "root authority boundary"),
        relaxed_or_broken_constraints=(),
        known_breakpoints=("trivial target set", "empty generator family", "restricted cover substitution", "changed generator basis"),
        evidence_pointers=("ECCC-TR25-033:Definition21", "ECCC-TR25-033:Theorem30"),
        authority=TransformationEpisodeAuthority.SOURCE_EVENT_VERIFIED,
        artifact_hash=_hash({"source":"ECCC-TR25-033","theorem":30,"definition":21}),
    )
    memory = build_transformation_memory(
        memory_id="PNP-C043-OTM-20260812",
        source_universe=("current PNP application memory", "current primary circuit-complexity literature"),
        episodes=(episode,),
        evidence_pointers=("ECCC-TR25-033", "RAKL_math:C041", "RAKL_math:C042"),
    )
    mapping = StructuralMappingWitness(
        witness_id="MAP-PNP-C043-CO25-T30",
        episode_id=episode.episode_id,
        target_obstruction_id=_obstruction().obstruction_id,
        role_mapping=(("cyclic intersection-complexity target", "root-facing cyclic-intersection obligation"), ("cover-complexity object", "exact cover-complexity surrogate")),
        shared_relations=("cover complexity is exact surrogate for cyclic intersection complexity",),
        shared_constraints=("target set non-trivial", "generator family non-empty", "same graph family and generator basis fixed"),
        precondition_mapping=(("target set non-trivial", "verify each evaluated G_n is non-trivial"), ("generator family non-empty", "G_NN has row and column generators for N=2^n")),
        unmatched_source_preconditions=(),
        disanalogies=("Theorem 30 supplies representation, not amplification.", "C042 is finite and cannot justify a later-level quotient theorem."),
        target_validation_obligations=("verify G_n non-triviality", "retain full Definition-21 pair universe", "retain exact row/column generator basis", "do not infer asymptotics from finite type counts"),
        evidence_pointers=("ECCC-TR25-033:Definition21", "ECCC-TR25-033:Theorem30", "RAKL_math:C042"),
        artifact_hash=_hash({"mapping":"C043-T30","target":ATOM}),
    )
    review_payload = {"atom":ATOM,"context":context_hash,"memory_review":memory_hash,"transformation_snapshot":memory.snapshot_hash,"mode":"SEARCH","episode":episode.episode_id}
    review = ObstructionTransformationReview(
        review_id="PNP-C043-SHORTCUT-REVIEW-20260812",
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        research_memory_review_hash=memory_hash,
        episode_memory_snapshot_hash=memory.snapshot_hash,
        obstruction=_obstruction(),
        direct_search_status=RouteSearchStatus.MATCHES_FOUND,
        jump_search_status=RouteSearchStatus.NOT_RUN,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.SEARCH,
        direct_candidate_episode_ids=(episode.episode_id,),
        direct_mapping_witnesses=(mapping,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=("Representation transfer passed only; target neighborhood-type candidate still needs falsification.",),
        evidence_pointers=("ECCC-TR25-033", "RAKL_math:C041", "RAKL_math:C042"),
        artifact_hash=_hash(review_payload),
    )
    return memory, review


def _trace(context_hash: str, memory_hash: str, shortcut_hash: str) -> MathResearchTrace:
    kinds = (
        ResearchTraceEventType.ATOMIZED,
        ResearchTraceEventType.CONTEXT_FROZEN,
        ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
        ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    )
    previous = ""
    entries = []
    for index, kind in enumerate(kinds, start=1):
        outputs = (f"C043-preoutput-{index}",)
        if kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            outputs = (memory_hash,)
        elif kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            outputs = (shortcut_hash,)
        payload = {
            "event_id": f"O9d12a2a1b-C043-E{index:02d}",
            "atom_id": ATOM,
            "event_type": kind.value,
            "timestamp": f"2026-08-12T00:{3+index:02d}:00+00:00",
            "state_summary": "Current-v3 prospective C043 pre-candidate gate; C042 quotient compression changes route to an exact cover/type upper-bound discriminator before LP.",
            "action_summary": kind.value,
            "evidence_pointers": (context_hash,),
            "alternatives_considered": ("fractional LP now", "repeat fixed-lift augmentation", "bounded exact neighborhood-type discriminator"),
            "decision_rationale": "Use source-verified exact cyclic-to-cover SEARCH route; rotate away from saturated fractional/fixed-lift families; admit no candidate before current gate PASS.",
            "outputs": outputs,
            "uncertainties": ("later-level asymptotic type growth unknown", "same-context review is not independent review"),
            "residuals": ("no uniform lower bound", "no root certificate"),
            "next_steps": ("after gate PASS only, freeze a bounded first-post-C042 type-count falsifier",),
            "previous_event_hash": previous,
        }
        artifact_hash = _hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **payload))
        previous = artifact_hash
    return MathResearchTrace(trace_id="PNP-O9d12a2a1b-C043-PRETRACE-20260812", entries=tuple(entries))


def build_current_gate_plan():
    fiber = _context()
    memory_review = _memory_review(fiber.packet_hash)
    transformation_memory, shortcut_review = _transformation_memory_and_review(fiber.packet_hash, memory_review.artifact_hash)
    trace = _trace(fiber.packet_hash, memory_review.artifact_hash, shortcut_review.artifact_hash)
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("C041 recursive graph family", "full cover object", "cyclic intersection complexity", "neighborhood types"),
            relations=("Theorem-30 exact cyclic-to-cover equality", "C042 finite quotient collapse", "cheap upper gate before lower-bound amplification"),
            domain="circuit complexity / discrete complexity / two-dimensional cover",
            goal_type="discriminate whether the explicit SAT-coded family escapes low-complexity cover structure after C042",
        ),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=fiber,
        memory_review=memory_review,
        transformation_memory=transformation_memory,
        shortcut_review=shortcut_review,
        research_trace=trace,
    )
    return plan, fiber, memory_review, transformation_memory, shortcut_review, trace
