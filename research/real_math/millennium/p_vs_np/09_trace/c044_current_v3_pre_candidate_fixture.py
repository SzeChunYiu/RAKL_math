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

ATOM = "O9d12a2a1b-C044"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
APPLICATION_BASE_SHA = "bbc1edcac2dbb5825cfdb0b2cb612bb53137a4d5"
QUOTIENT_COMPLEMENT = (
    (0, 0),
    (1, 2),
    (2, 1),
    (2, 2),
    (4, 4),
    (5, 5),
    (5, 6),
    (6, 5),
    (7, 5),
    (7, 7),
)


def _hash(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def context() -> MathContextFiber:
    transfer = MethodTransfer(
        source_context="C042 exact G9/G13 quotient pair-cover witnesses",
        method="construct an explicit bounded legal-pair family on an exact twin quotient and prove every quotient-relevant semi-filter is covered",
        shared_structure=(
            "finite exact twin quotient",
            "Definition-21 relevant semi-filters and unrestricted legal pairs",
            "upper-bound quotient lift polarity",
        ),
        required_assumptions=(
            "exact quotient incidence is fixed",
            "full unrestricted pair universe is retained",
            "relevance uses the exact row/column generator traces",
        ),
        disanalogies=(
            "C044 has ten complement cells rather than the smaller C042 quotients",
            "the old exhaustive oracle is guarded at five complement cells",
            "C042 two-pair witnesses need not survive",
        ),
        repair_question="Can the exact ten-cell quotient be covered by a substantially smaller explicit pair family, or can a preserving relevant semi-filter falsify each bounded attempt?",
        source_anchors=(
            "research/real_math/millennium/p_vs_np/04_candidates/C042_ACTIVATION_QUOTIENT_RESULT_20260812.md",
            "ECCC-TR25-033:Definitions18-21",
        ),
    )
    payload = {
        "atom": ATOM,
        "quotient": QUOTIENT_COMPLEMENT,
        "coordinates": (
            "exact eight-by-eight G16 twin quotient",
            "ten complement cells",
            "Definition-21 full cover complexity",
            "relevant semi-filters",
            "legal pair multiplexing",
            "upper-bound quotient lift",
        ),
        "sources": (
            "RAKL_math:C043-result",
            "RAKL_math:C042-result",
            "ECCC-TR25-033:Definitions18-21",
            "ECCC-TR25-033:Theorem30",
        ),
    }
    return MathContextFiber(
        atom_id=ATOM,
        object_context="Post-C043 quotient-multiplexing atom: sharpen or falsify the eight-pair G16 type-class ceiling by attacking the exact eight-by-eight quotient directly before any larger-level or fractional lower-bound search.",
        structural_coordinates=payload["coordinates"],
        equivalent_formulations=(
            "set cover of all quotient-relevant semi-filters by legal pairs (E,H)",
            "cyclic intersection complexity through the exact Cavalar-Oliveira cover characterization when its hypotheses hold",
            "bounded explicit quotient pair certificate whose lift to G16 is upper-bound only",
        ),
        solved_analogues=("C042 exact finite quotient cover number two at the first syntax and first UNSAT-capable children",),
        near_solved_analogues=("C043 exact eight-type G16 quotient with rho(G16)<=8 but unknown quotient cover optimum",),
        method_transfers=(transfer,),
        explicit_disanalogies=(
            "finite local cover sharpening is not asymptotic growth",
            "type growth is not cover growth",
            "fractional packing is not integral cover control",
            "computation is not proof",
        ),
        source_anchors=payload["sources"],
        analogy_scan_status=AnalogyScanStatus.NO_SAFE_BRIDGE_FOUND.value,
        analogy_scan_notes="The same-domain C042 verified-local quotient-pair episode survives SEARCH, so no JUMP/GLUE/LIFT or cross-Millennium shortcut is used.",
        frozen_at="2026-08-12T00:10:00+00:00",
        first_candidate_at=None,
        packet_hash=_hash(payload),
    )


def memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {
        "atom": ATOM,
        "context": context_hash,
        "selected_tools": ("T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",),
        "rejected_tools": ("T-PNP-FRACTIONAL-SEMIFILTER-PACKING",),
        "failures": (
            "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING",
            "F-C042-FIRST-UNSAT-QUOTIENT-COMPRESSION",
            "F-C024-FRACTIONAL-INTEGRALITY-GAP",
        ),
    }
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash="gitblob:eaaafb86255724042b761d74de7c834d49af0df6+gitblob:4797c50cf9345ce09be0206a4ace5a7f9b01d93a",
        failure_lattice_snapshot_hash="gitblob:c9e47beb4059028d64f199249dfbbed663d9b668+gitblob:76d7f20f181f345869b4a29eb9ff8cab445fd32a",
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "exact quotient pair-cover certificate",
            "neighborhood-type upper falsifier",
            "fractional semi-filter packing",
        ),
        relevant_tool_ids=(
            "T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",
            "T-PNP-FRACTIONAL-SEMIFILTER-PACKING",
        ),
        relevant_failure_ids=payload["failures"],
        selected_tool_ids=("T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",),
        tool_applicability_notes=(
            "Select exact neighborhood quotient reuse to preserve the proved G16 compression and lift direction.",
            "Retrieve but reject fractional packing for the immediate action because C024 blocks any automatic integral-cover inference.",
        ),
        failure_reuse_notes=(
            "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING changes routing from semantic/type counting to quotient multiplexing itself.",
            "F-C042-FIRST-UNSAT-QUOTIENT-COMPRESSION makes small explicit pair families a first falsifier but does not predict success at ten cells.",
            "F-C024-FRACTIONAL-INTEGRALITY-GAP keeps LP work downstream of the direct integral quotient test.",
        ),
        unresolved_warnings=(
            "No uniform or later-level conclusion can follow from a G16 quotient certificate.",
            "Historical C042/C043 discovery chronology is not retroactively current-Gate-C compliant; only their recorded local mathematical source authority is reused.",
        ),
        evidence_pointers=(
            "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C043_POST_RESULT_TOOL_REUSE_DELTA_20260812.json",
            "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C043_FIRST_ROW_SPLIT_FAILURE_DELTA_20260812.json",
            "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C041_TOOL_SNAPSHOT_20260811.json",
        ),
        artifact_hash=_hash(payload),
    )


def target_obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-PNP-C044-QUOTIENT-MULTIPLEX",
        domain="mathematics",
        roles=("exact finite quotient", "relevant semi-filter", "legal pair", "full graph lift"),
        relations=(
            "a legal pair covers a semi-filter exactly when preservation fails",
            "a quotient pair family lifts only as a full-graph upper certificate",
        ),
        constraints=(
            "exact quotient incidence is fixed",
            "full unrestricted pair universe is retained",
            "relevance uses the exact row/column generator traces",
        ),
        failure_mechanisms=("quotient semantic/type growth can still be multiplexed by few shared legal pairs",),
        invariants_to_preserve=("Definition-21 semantics", "G16 quotient incidence", "upper-bound lift polarity", "root authority boundary"),
        desired_transition=("replace the unknown quotient cover by a falsifiable bounded explicit pair-family certificate or a concrete preserving relevant semi-filter",),
        forbidden_losses=("restricted pair universe", "finite computation treated as asymptotic proof"),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    source = ObstructionFingerprint(
        obstruction_id="OBS-PNP-C042-EXPLICIT-QUOTIENT-COVER",
        domain="mathematics",
        roles=("exact finite quotient", "relevant semi-filter", "legal pair", "full graph lift"),
        relations=(
            "a legal pair covers a semi-filter exactly when preservation fails",
            "a quotient pair family lifts only as a full-graph upper certificate",
        ),
        constraints=(
            "exact quotient incidence is fixed",
            "full unrestricted pair universe is retained",
            "relevance uses the exact row/column generator traces",
        ),
        failure_mechanisms=("quotient semantic/type growth can still be multiplexed by few shared legal pairs",),
        invariants_to_preserve=("Definition-21 semantics", "G16 quotient incidence", "upper-bound lift polarity", "root authority boundary"),
        desired_transition=("replace the unknown quotient cover by a falsifiable bounded explicit pair-family certificate or a concrete preserving relevant semi-filter",),
    )
    episode = ObstructionTransformationEpisode(
        episode_id="E-PNP-C042-EXPLICIT-QUOTIENT-PAIR-COVER",
        source_domain="mathematics",
        source_context="C042 finite G9/G13 exact quotient pair-cover construction",
        source_obstruction=source,
        transformation_name="explicit quotient legal-pair cover with counterexample-first validation",
        operation="propose a bounded legal-pair family on the exact quotient, falsify it against relevant semi-filters, and retain it only after full source-valid coverage verification",
        preconditions=(
            "exact quotient incidence is fixed",
            "full unrestricted pair universe is retained",
            "relevance uses the exact row/column generator traces",
        ),
        resulting_relations=("replace the unknown quotient cover by a falsifiable bounded explicit pair-family certificate or a concrete preserving relevant semi-filter",),
        preserved_invariants=("Definition-21 semantics", "G16 quotient incidence", "upper-bound lift polarity", "root authority boundary"),
        relaxed_or_broken_constraints=(),
        known_breakpoints=(
            "candidate pairs fail on a relevant preserving semi-filter",
            "quotient incidence is incompletely represented",
            "a restricted pair family is confused with the full cover object",
        ),
        evidence_pointers=(
            "research/real_math/millennium/p_vs_np/04_candidates/C042_ACTIVATION_QUOTIENT_RESULT_20260812.md",
            "research/real_math/millennium/p_vs_np/05_falsification/C042_QUOTIENT_PAIR_WITNESS_RECEIPT_20260812.json",
        ),
        authority=TransformationEpisodeAuthority.VERIFIED_LOCAL,
        artifact_hash=_hash({"episode":"C042-explicit-quotient-pair-cover","authority":"VERIFIED_LOCAL"}),
        lineage_ids=("C013", "C042"),
    )
    memory = build_transformation_memory(
        memory_id="PNP-C044-OTM-20260812",
        source_universe=("RAKL_math PNP C042-C043 verified local mathematical episodes", "current primary circuit-complexity definitions"),
        episodes=(episode,),
        evidence_pointers=(
            "research/real_math/millennium/p_vs_np/04_candidates/C042_ACTIVATION_QUOTIENT_RESULT_20260812.md",
            "research/real_math/millennium/p_vs_np/04_candidates/C043_FIRST_ROW_SPLIT_RESULT_20260812.md",
            "ECCC-TR25-033:Definitions18-21",
        ),
    )
    mapping = StructuralMappingWitness(
        witness_id="MAP-PNP-C044-C042-PAIR-COVER",
        episode_id=episode.episode_id,
        target_obstruction_id=target_obstruction().obstruction_id,
        role_mapping=(("exact finite quotient", "exact finite quotient"), ("relevant semi-filter", "relevant semi-filter"), ("legal pair", "legal pair"), ("full graph lift", "full graph lift")),
        shared_relations=source.relations,
        shared_constraints=source.constraints,
        precondition_mapping=((item, item) for item in episode.preconditions),
        unmatched_source_preconditions=(),
        disanalogies=(
            "C044 quotient has ten complement cells and can support new preserving semi-filters absent from C042.",
            "The C042 exact-antichain oracle cannot be reused directly because its guard is five complement cells.",
        ),
        target_validation_obligations=(
            "freeze bounded pair-count predictions before execution",
            "return a concrete preserving relevant semi-filter for every failed pair family",
            "convert any surviving computational family into an explicit combinatorial coverage proof",
            "lift only in the upper-bound direction and claim no asymptotic consequence",
        ),
        evidence_pointers=(
            "research/real_math/millennium/p_vs_np/05_falsification/C043_FIRST_ROW_SPLIT_RECEIPT_20260812.json",
            "research/real_math/millennium/p_vs_np/05_falsification/full_cover_oracle.py",
        ),
        artifact_hash=_hash({"mapping":"C044<-C042-pair-cover","target":"OBS-PNP-C044-QUOTIENT-MULTIPLEX"}),
    )
    review_payload = {"atom":ATOM,"context":context_hash,"memory":memory_hash,"snapshot":memory.snapshot_hash,"mode":"SEARCH","episode":episode.episode_id}
    review = ObstructionTransformationReview(
        review_id="PNP-C044-SHORTCUT-REVIEW-20260812",
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        research_memory_review_hash=memory_hash,
        episode_memory_snapshot_hash=memory.snapshot_hash,
        obstruction=target_obstruction(),
        direct_search_status=RouteSearchStatus.MATCHES_FOUND,
        jump_search_status=RouteSearchStatus.NOT_RUN,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.SEARCH,
        direct_candidate_episode_ids=(episode.episode_id,),
        direct_mapping_witnesses=(mapping,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=("Source success changes routing only; it does not predict the C044 quotient cover number.",),
        evidence_pointers=("RAKL_math:C042", "RAKL_math:C043", "ECCC-TR25-033"),
        artifact_hash=_hash(review_payload),
    )
    return memory, review


def trace(context_hash: str, memory_hash: str, shortcut_hash: str) -> MathResearchTrace:
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
    role_objections = (
        "domain: finite cover sharpening has no root authority",
        "combinatorics: test multiplexing, not type counts",
        "encoding: semantics matter only if quotient incidence changes",
        "falsification: demand preserving semi-filter counterexamples",
        "verification: computation is calibration until explicit proof",
        "novelty: source provenance and local scope remain explicit",
    )
    entries = []
    previous = ""
    for index, kind in enumerate(kinds, start=1):
        outputs = (f"C044-preoutput-{index}",)
        evidence = ("research/real_math/millennium/p_vs_np/01_frontier/O9d12a2a1b_C044_CURRENT_V3_PRE_CANDIDATE_PACKET_20260812.json",)
        if kind is ResearchTraceEventType.CONTEXT_FROZEN:
            evidence = (context_hash,)
        if kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            outputs = (memory_hash,)
        if kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            outputs = (shortcut_hash,)
        if kind is ResearchTraceEventType.EXPERT_CONTEXT_REVIEW:
            outputs = role_objections
        payload = {
            "event_id": f"O9d12a2a1b-C044-E{index:02d}",
            "atom_id": ATOM,
            "event_type": kind.value,
            "timestamp": f"2026-08-12T00:{10+index:02d}:00+00:00",
            "state_summary": "Prospective current-v3 C044 quotient-multiplexing gate with no candidate identity yet.",
            "action_summary": kind.value,
            "evidence_pointers": evidence,
            "alternatives_considered": ("count more semantic rows/types", "run fractional LP now", "direct exact quotient pair-cover falsifier"),
            "decision_rationale": "C043 and C024 route away from saturated semantic/type counting and immediate fractional inference; verified-local C042 quotient pair-cover experience supports same-domain SEARCH.",
            "outputs": outputs,
            "uncertainties": ("ten-cell quotient cover number unknown", "same-context role separation is not independent review"),
            "residuals": ("rho quotient sharper upper bound unknown", "no asymptotic recurrence", "root OPEN"),
            "next_steps": ("only after all current gates PASS, freeze bounded pair-count predictions before any computation",),
            "previous_event_hash": previous,
        }
        artifact_hash = _hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **payload))
        previous = artifact_hash
    return MathResearchTrace(trace_id="PNP-O9d12a2a1b-C044-PRETRACE-20260812", entries=tuple(entries))


def build_current_gate_plan():
    fiber = context()
    memory = memory_review(fiber.packet_hash)
    transformation_memory, shortcut = transformation_memory_and_review(fiber.packet_hash, memory.artifact_hash)
    research_trace = trace(fiber.packet_hash, memory.artifact_hash, shortcut.artifact_hash)
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("C043 G16 twin quotient", "relevant semi-filters", "legal pairs", "quotient-to-G16 lift"),
            relations=("pair preservation failure covers semi-filter", "bounded quotient cover lifts as upper certificate"),
            domain="circuit complexity / discrete complexity / two-dimensional cover",
            goal_type="falsify or certify small legal-pair multiplexing on the exact G16 quotient",
        ),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=fiber,
        memory_review=memory,
        transformation_memory=transformation_memory,
        shortcut_review=shortcut,
        research_trace=research_trace,
    )
    return plan, fiber, memory, transformation_memory, shortcut, research_trace
