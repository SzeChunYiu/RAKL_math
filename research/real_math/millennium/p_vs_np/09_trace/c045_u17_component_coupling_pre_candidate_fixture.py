"""Current-v3, result-blind pre-candidate fixture for the C045 incidence gate.

This module constructs governance artifacts only.  It deliberately has no
dependency on the frozen decoder, satisfiability code, finite cover machinery,
or any target evaluator.  Candidate generation is licensed only to freeze a
later incidence-classification plan; no mathematical candidate or target
output is produced here.
"""

from __future__ import annotations

from dataclasses import asdict
from enum import Enum
import hashlib
import json

from rakl.math_context import AnalogyScanStatus, MathContextFiber, MethodTransfer
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType
from rakl.root_coordinate_preservation import (
    BridgeEdge,
    CoordinateAuthority,
    EdgeProofStatus,
    Obligation,
    RegisteredStateObservation,
    RootCoordinatePreservationReceipt,
)
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


ATOM = "O9d12a2a1b-C045"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
APPLICATION_BASE_SHA = "e768b7da7dc48739ccb581dea0eb2cfeb8a701e7"
C044_RETROSPECTIVE_COMMIT = "58ef4f6d18fd7ee621a0ad4e0534922fa19a03e3"
C044_RESULT_BLOB = "93121efbc29b8f917afd8b50f6876359c3c5f9e5"
C044_FAILURE_BLOB = "6e02d33c05e13a3a1a634a953d02f6e0a724d75b"
C044_TOOL_BLOB = "fd68bfb412dfdab77296ee664a7722a3031325ad"
C043_TOOL_BLOB = "6d2ba546cce8686a21c13e3291109f8ae945bc44"
C043_FAILURE_BLOB = "df83caec4a0c95da2a5c929dfc2957794f41c358"

ATOMIZATION_PATH = (
    "research/real_math/millennium/p_vs_np/02_problem_dag/"
    "O9d12a2a1b_C045_ATOMIZATION_20260812.json"
)
CONTEXT_PATH = (
    "research/real_math/millennium/p_vs_np/01_frontier/"
    "O9d12a2a1b_C045_MATH_CONTEXT_FIBER_20260812.json"
)
MEMORY_PATH = (
    "research/real_math/millennium/p_vs_np/07_memory/"
    "O9d12a2a1b_C045_RESEARCH_MEMORY_REVIEW_20260812.json"
)
TRANSFORMATION_MEMORY_PATH = (
    "research/real_math/millennium/p_vs_np/07_memory/"
    "O9d12a2a1b_C045_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json"
)
EXPERT_PATH = (
    "research/real_math/millennium/p_vs_np/08_reviews/"
    "O9d12a2a1b_C045_EXPERT_CONTEXT_REVIEW_20260812.json"
)
SHORTCUT_PATH = (
    "research/real_math/millennium/p_vs_np/08_reviews/"
    "O9d12a2a1b_C045_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json"
)
TRACE_PATH = (
    "research/real_math/millennium/p_vs_np/09_trace/"
    "O9d12a2a1b_C045_PRE_CANDIDATE_TRACE_20260812.json"
)


def _hash(payload: object) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _jsonable(value):
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, tuple):
        return [_jsonable(item) for item in value]
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    return value


def _document(value) -> dict:
    return _jsonable(asdict(value))


def _with_artifact_hash(payload: dict) -> dict:
    document = dict(payload)
    document["artifact_hash"] = ""
    document["artifact_hash"] = _hash(document)
    return document


def context() -> MathContextFiber:
    residual_transfer = MethodTransfer(
        source_context="C043 exact fixed-split residual and full-history twin classification",
        method=(
            "classify exact prefix/suffix completion residuals, then recompute accumulated "
            "row and column neighbourhood equivalence before forming a quotient"
        ),
        shared_structure=(
            "same frozen recursive decoder family",
            "equal prefix/suffix split determines the new cross band",
            "full accumulated complement neighbourhoods determine twin classes",
        ),
        required_assumptions=(
            "decoder identity and split remain frozen",
            "fallback and canonical branches remain separate",
            "old bands are included before any twin or component claim",
        ),
        disanalogies=(
            "C043 classified the preceding extension rather than the untouched immediate successor",
            "a new residual class need not connect inherited support components",
            "residual or type growth supplies no cover lower bound",
        ),
        repair_question=(
            "Does exact full-history quotient support at the immediate successor remain "
            "component-separable, or does one exact support relation join inherited components?"
        ),
        source_anchors=(
            "research/real_math/millennium/p_vs_np/04_candidates/C043_FIRST_ROW_SPLIT_RESULT_20260812.md",
            "research/real_math/millennium/p_vs_np/01_frontier/O9d12a2a1b_C043_MATH_CONTEXT_FIBER_20260812.json",
        ),
    )
    component_transfer = MethodTransfer(
        source_context="C044 retrospective heterogeneous component-multiplexing upper lemma",
        method=(
            "test exact quotient support for cross-component complement coupling before "
            "reusing component-local upper constructions"
        ),
        shared_structure=(
            "finite exact quotient support",
            "component membership is determined by complement incidence",
            "component separability is a precondition of heterogeneous pair reuse",
        ),
        required_assumptions=(
            "parent component identities are exact",
            "target incidence is classified extensionally rather than sampled",
            "any downstream cover transfer preserves the full-cover polarity",
        ),
        disanalogies=(
            "C044 used a result-exposed parent target and has no strict discovery chronology",
            "the untouched successor can split, merge, extend, or couple parent types",
            "coupling falsifies one upper construction but does not prove a lower bound",
        ),
        repair_question=(
            "Which branch of the exact component-incidence gate is supported before any "
            "pair-family, fractional, or lower-bound search?"
        ),
        source_anchors=(
            f"git:{C044_RETROSPECTIVE_COMMIT}:C044_RETROSPECTIVE_Q16_MULTIPLEXING_RESULT_20260812.md",
            "research/real_math/millennium/p_vs_np/04_candidates/negative_history/C010_fixed_gadget_block_sum_ceiling.md",
        ),
    )
    payload = {
        "atom": ATOM,
        "target_extension": "U16_TO_U17_IMMEDIATE_SOURCE_EXTENSION",
        "coordinates": (
            "frozen immediate recursive extension",
            "canonical cross-band completion relation",
            "fallback branch kept separate",
            "full-history row and column neighbourhood twins",
            "quotient complement support components",
            "inherited-component incidence",
            "upper-bound-only downstream transfer",
        ),
        "sources": (
            "RAKL_math:C041-frozen-decoder-definition",
            "RAKL_math:C043-exact-residual-twins",
            f"git:{C044_RETROSPECTIVE_COMMIT}:C044-component-lemma",
            "ECCC-TR25-033:Definitions18-21",
        ),
    }
    return MathContextFiber(
        atom_id=ATOM,
        object_context=(
            "Result-blind immediate-successor incidence atom: classify only whether exact "
            "full-history quotient support preserves or breaks the parent component boundary "
            "before any cover, SAT, fractional, or lower-bound candidate is formed."
        ),
        structural_coordinates=payload["coordinates"],
        equivalent_formulations=(
            "connectivity of the bipartite quotient-complement support graph after exact twin recomputation",
            "whether a new exact row or column star is incident to more than one inherited active component",
            "the first precondition gate for reusing the heterogeneous component upper lemma",
        ),
        solved_analogues=(
            "C043 exact residual-to-twin classification at the preceding extension",
            "C044 finite component decomposition and heterogeneous upper construction",
        ),
        near_solved_analogues=(
            "finite automata residual equivalence classifies fixed-split rows but gives no cover authority",
        ),
        method_transfers=(residual_transfer, component_transfer),
        explicit_disanalogies=(
            "the target extension is untouched and no target incidence is known",
            "component coupling is not cover growth",
            "absence of coupling does not determine a local component cover",
            "finite incidence supplies no recurrence, circuit lower bound, or root authority",
            "computation is not proof",
        ),
        source_anchors=payload["sources"],
        analogy_scan_status=AnalogyScanStatus.NO_SAFE_BRIDGE_FOUND.value,
        analogy_scan_notes=(
            "Same-domain C043/C044 structural episodes cover the required classification and "
            "component gate. No cross-domain or everyday analogy is retained."
        ),
        frozen_at="2026-08-12T00:40:00+00:00",
        first_candidate_at=None,
        packet_hash=_hash(payload),
    )


def memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {
        "atom": ATOM,
        "context": context_hash,
        "selected_tools": ("T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",),
        "warnings": (
            "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING",
            "F-C044-HETEROGENEOUS-BLOCK-MULTIPLEXING",
            "F-C010-MULTIPLEXING",
        ),
        "source_blobs": (
            C043_TOOL_BLOB,
            C043_FAILURE_BLOB,
            C044_FAILURE_BLOB,
            C044_TOOL_BLOB,
        ),
    }
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash=(
            f"gitblob:{C043_TOOL_BLOB}+gitblob:{C044_TOOL_BLOB}"
        ),
        failure_lattice_snapshot_hash=(
            f"gitblob:{C043_FAILURE_BLOB}+gitblob:{C044_FAILURE_BLOB}"
        ),
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "exact fixed-split residual and full-history twin classification",
            "exact quotient support-component incidence gate",
            "heterogeneous component-local upper construction",
            "direct quotient pair-cover search",
            "fractional semi-filter packing",
        ),
        relevant_tool_ids=(
            "T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",
            "T-PNP-HETEROGENEOUS-BLOCK-MULTIPLEXING-UPPER",
        ),
        relevant_failure_ids=payload["warnings"],
        selected_tool_ids=("T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",),
        tool_applicability_notes=(
            "Select the C043 exact-neighbourhood tool only with fresh target validation: full-history twins and all old/new collisions must be reproved.",
            "The C044 heterogeneous tool remains a proposal pending fresh reuse assurance; use its no-cross-component-cell condition as a falsifier, not as a promoted theorem about the successor.",
        ),
        failure_reuse_notes=(
            "F-C043 blocks semantic or type counts as amplification proxies.",
            "F-C044 makes exact component incidence the first repeat-failure test before any cover search.",
            "F-C010 warns that nominally distinct components can reuse the same pair indices.",
        ),
        unresolved_warnings=(
            "The target outcome is unobserved.",
            "No target quotient, cell, witness, count, or cover has been generated.",
            "Coupling would only falsify a component-separable upper route; it would not prove hardness.",
            "Same-context review is not independent peer review.",
        ),
        evidence_pointers=(
            "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C043_TOOL_SNAPSHOT_20260812.json",
            "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C043_FIRST_ROW_SPLIT_FAILURE_DELTA_20260812.json",
            f"git:{C044_RETROSPECTIVE_COMMIT}:O9d12a2a1b_C044_HETEROGENEOUS_MULTIPLEXING_FAILURE_DELTA_20260812.json",
        ),
        artifact_hash=_hash(payload),
    )


def target_obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-PNP-C045-IMMEDIATE-COMPONENT-COUPLING",
        domain="mathematics",
        roles=(
            "inherited quotient support components",
            "next exact cross-band relation",
            "accumulated endpoint fibres",
            "full-history twin classes",
            "component-incidence gate",
        ),
        relations=(
            "a source-defined word maps to one cross-band complement relation",
            "new relations update accumulated row and column fibres",
            "equal full fibres define quotient twins",
            "quotient support incidence determines inherited-component coupling",
        ),
        constraints=(
            "frozen decoder and immediate recursive extension",
            "fallback branch remains separate",
            "target incidence is unobserved before the gate",
            "full-cover polarity and parent provenance are preserved",
        ),
        failure_mechanisms=(
            "semantic or type growth remains component-isolated and globally multiplexable",
            "a new-band-only classification misses an old-band type collision",
            "sampled incidence is mistaken for an exact component statement",
        ),
        invariants_to_preserve=(
            "decoder identity",
            "full-history neighbourhood equality",
            "Definition-21 relevance semantics",
            "upper-bound-only quotient lift",
            "root remains open",
        ),
        desired_transition=(
            "select exactly one frozen component-incidence result branch before any downstream cover action",
        ),
        forbidden_losses=(
            "pre-gate target execution",
            "formula or type count used as an incidence proxy",
            "coupling interpreted as a lower bound",
            "decoder or evaluator mutation after freeze",
        ),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    source = ObstructionFingerprint(
        obstruction_id="OBS-PNP-C044-EXACT-COMPONENT-GATE",
        domain="mathematics",
        roles=(
            "inherited quotient support components",
            "next exact cross-band relation",
            "accumulated endpoint fibres",
            "full-history twin classes",
            "component-incidence gate",
        ),
        relations=(
            "a source-defined word maps to one cross-band complement relation",
            "new relations update accumulated row and column fibres",
            "equal full fibres define quotient twins",
            "quotient support incidence determines inherited-component coupling",
        ),
        constraints=(
            "frozen decoder and immediate recursive extension",
            "fallback branch remains separate",
            "target incidence is unobserved before the gate",
            "full-cover polarity and parent provenance are preserved",
        ),
        failure_mechanisms=(
            "semantic or type growth remains component-isolated and globally multiplexable",
            "a new-band-only classification misses an old-band type collision",
        ),
        invariants_to_preserve=(
            "decoder identity",
            "full-history neighbourhood equality",
            "Definition-21 relevance semantics",
            "upper-bound-only quotient lift",
            "root remains open",
        ),
        desired_transition=(
            "select exactly one frozen component-incidence result branch before any downstream cover action",
        ),
    )
    episode = ObstructionTransformationEpisode(
        episode_id="E-PNP-C044-EXACT-COMPONENT-COUPLING-GATE",
        source_domain="mathematics",
        source_context=(
            "C043 exact full-history twin quotient followed by the C044 exact support-component decomposition"
        ),
        source_obstruction=source,
        transformation_name="exact full-history component-incidence gate before cover amplification",
        operation=(
            "classify the exact accumulated quotient support, preserve inherited type provenance, "
            "and test the no-cross-component-cell precondition before any pair or lower-bound search"
        ),
        preconditions=(
            "parent quotient components are exact",
            "the decoder, recursive extension, split, and polarity are frozen",
            "target twins will be formed only from full accumulated neighbourhoods",
        ),
        resulting_relations=(
            "select exactly one frozen component-incidence result branch before any downstream cover action",
        ),
        preserved_invariants=(
            "decoder identity",
            "full-history neighbourhood equality",
            "Definition-21 relevance semantics",
            "upper-bound-only quotient lift",
            "root remains open",
        ),
        relaxed_or_broken_constraints=(),
        known_breakpoints=(
            "one exact relation joins distinct inherited components",
            "an old type splits or collides after accumulation",
            "the target support cannot be classified exactly",
            "a target result is exposed before candidate freeze",
        ),
        evidence_pointers=(
            "research/real_math/millennium/p_vs_np/04_candidates/C043_FIRST_ROW_SPLIT_RESULT_20260812.md",
            f"git:{C044_RETROSPECTIVE_COMMIT}:C044_RETROSPECTIVE_Q16_MULTIPLEXING_RESULT_20260812.md",
        ),
        authority=TransformationEpisodeAuthority.VERIFIED_LOCAL,
        artifact_hash=_hash(
            {
                "episode": "C044-exact-component-coupling-gate",
                "source_result_blob": C044_RESULT_BLOB,
                "authority": "VERIFIED_LOCAL_MATHEMATICAL_UPPER_LEMMA",
            }
        ),
        lineage_ids=("C010", "C013", "C043", "C044-RETROSPECTIVE"),
    )
    transformation_memory = build_transformation_memory(
        memory_id="PNP-C045-OTM-20260812",
        source_universe=(
            "RAKL_math PNP C010/C013/C043 current-main mathematical history",
            f"RAKL_math retrospective C044 commit {C044_RETROSPECTIVE_COMMIT}",
            "Cavalar-Oliveira Definition-21 model",
        ),
        episodes=(episode,),
        evidence_pointers=(
            "research/real_math/millennium/p_vs_np/04_candidates/negative_history/C010_fixed_gadget_block_sum_ceiling.md",
            "research/real_math/millennium/p_vs_np/04_candidates/negative_history/C013_quotient_blowup_ceiling.md",
            "research/real_math/millennium/p_vs_np/04_candidates/C043_FIRST_ROW_SPLIT_RESULT_20260812.md",
            f"git:{C044_RETROSPECTIVE_COMMIT}:C044_RETROSPECTIVE_Q16_MULTIPLEXING_RESULT_20260812.md",
        ),
    )
    mapping = StructuralMappingWitness(
        witness_id="MAP-PNP-C045-C044-COMPONENT-GATE",
        episode_id=episode.episode_id,
        target_obstruction_id=target_obstruction().obstruction_id,
        role_mapping=tuple((role, role) for role in source.roles),
        shared_relations=source.relations,
        shared_constraints=source.constraints,
        precondition_mapping=(
            (
                "parent quotient components are exact",
                "bind the accepted C043 parent twin quotient and the reviewed C044 component decomposition by source identity",
            ),
            (
                "the decoder, recursive extension, split, and polarity are frozen",
                "bind the unchanged C041 source definition and immediate U16-to-U17 extension before any target execution",
            ),
            (
                "target twins will be formed only from full accumulated neighbourhoods",
                "freeze full-history twin recomputation and explicit old-type collision branches as evaluator obligations",
            ),
        ),
        unmatched_source_preconditions=(),
        disanalogies=(
            "The source component statement was retrospective; C045 must preserve fresh result-blind chronology.",
            "The successor may split, merge, extend, or couple parent types.",
            "Passing or failing the incidence gate supplies no cover lower bound.",
        ),
        target_validation_obligations=(
            "freeze the five branch labels and complete target-incidence specification before execution",
            "derive the target syntax and residual classification analytically rather than from sampled outputs",
            "recompute full accumulated twins on both sides and account for every old/new collision",
            "return one exact branch with evidence or CANNOT_CHECK",
            "run no cover, fractional, SAT-search, or lower-bound action inside this gate",
        ),
        evidence_pointers=(ATOMIZATION_PATH, CONTEXT_PATH),
        artifact_hash=_hash(
            {
                "mapping": "C045<-C044-exact-component-gate",
                "target": "OBS-PNP-C045-IMMEDIATE-COMPONENT-COUPLING",
            }
        ),
    )
    review_payload = {
        "atom": ATOM,
        "context": context_hash,
        "memory": memory_hash,
        "snapshot": transformation_memory.snapshot_hash,
        "mode": "SEARCH",
        "episode": episode.episode_id,
    }
    review = ObstructionTransformationReview(
        review_id="PNP-C045-SHORTCUT-REVIEW-20260812",
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        research_memory_review_hash=memory_hash,
        episode_memory_snapshot_hash=transformation_memory.snapshot_hash,
        obstruction=target_obstruction(),
        direct_search_status=RouteSearchStatus.MATCHES_FOUND,
        jump_search_status=RouteSearchStatus.NOT_RUN,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.SEARCH,
        direct_candidate_episode_ids=(episode.episode_id,),
        direct_mapping_witnesses=(mapping,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=(
            "SEARCH licenses only a future incidence-classification plan.",
            "The target outcome remains unobserved.",
            "LIFT is not justified while this direct same-domain gate is available.",
        ),
        evidence_pointers=(CONTEXT_PATH, MEMORY_PATH, TRANSFORMATION_MEMORY_PATH),
        artifact_hash=_hash(review_payload),
    )
    return transformation_memory, review


def expert_review_document(context_hash: str) -> dict:
    return _with_artifact_hash(
        {
            "schema_version": "1.0.0",
            "review_id": "PNP-O9d12a2a1b-C045-EXPERT-CONTEXT-REVIEW-20260812",
            "recorded_at": "2026-08-12T00:44:00+00:00",
            "atom_id": ATOM,
            "context_hash": context_hash,
            "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
            "roles": [
                {
                    "role": "domain_theory",
                    "finding": "Component incidence is a precondition check for one upper construction, not a cover lower bound.",
                    "recommendation": "Freeze incidence branches before any downstream cover action.",
                },
                {
                    "role": "analogy_method_transfer",
                    "finding": "C043 residual classification and C044 component decomposition are same-domain transfers with explicit scope differences.",
                    "recommendation": "Select SEARCH and require fresh full-history target validation.",
                },
                {
                    "role": "adversarial_falsification",
                    "finding": "One exact cross-component support relation, one old-type collision, or incomplete incidence defeats a no-coupling classification.",
                    "recommendation": "Use the branch-complete incidence gate and return CANNOT_CHECK on incomplete support.",
                },
                {
                    "role": "formal_methods",
                    "finding": "The pre-candidate fixture must have no dependency capable of evaluating the target.",
                    "recommendation": "Enforce a source-level capability denylist and no candidate trace event.",
                },
                {
                    "role": "novelty_research_value",
                    "finding": "The finite gate is diagnostic; its value is selecting the next proof-DAG child without overclaiming.",
                    "recommendation": "Make no novelty, recurrence, circuit, or root claim.",
                },
            ],
            "strongest_objection": "Even genuine coupling only retires a separable upper construction; it does not establish growing cover complexity.",
            "disagreement": "The structural lens prioritizes the immediate incidence gate; the lower-bound lens would prefer a direct cover search, but the latter is downstream and more expensive.",
            "recommendation": "After all gates pass, freeze an incidence-classification plan only; do not execute it in this round.",
            "target_state": "TARGET_OUTCOME_UNOBSERVED",
            "candidate_identity": None,
            "root_status": "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE",
        }
    )


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
    role_outputs = (
        "domain: incidence is not a lower bound",
        "transfer: same-domain SEARCH requires fresh full-history validation",
        "falsification: one exact coupling relation or type collision is decisive",
        "verification: pre-gate target capability is forbidden",
        "novelty: finite diagnostic only",
    )
    entries = []
    previous = ""
    for index, kind in enumerate(kinds, start=1):
        evidence = (ATOMIZATION_PATH,)
        outputs = ("TARGET_OUTCOME_UNOBSERVED",)
        if kind is ResearchTraceEventType.CONTEXT_FROZEN:
            evidence = (CONTEXT_PATH,)
            outputs = (context_hash, "TARGET_OUTCOME_UNOBSERVED")
        elif kind is ResearchTraceEventType.EXPERT_CONTEXT_REVIEW:
            evidence = (EXPERT_PATH,)
            outputs = role_outputs
        elif kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            evidence = (MEMORY_PATH,)
            outputs = (memory_hash, "TARGET_OUTCOME_UNOBSERVED")
        elif kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            evidence = (SHORTCUT_PATH,)
            outputs = (shortcut_hash, "selected_mode:SEARCH", "TARGET_OUTCOME_UNOBSERVED")
        payload = {
            "event_id": f"O9d12a2a1b-C045-E{index:02d}",
            "atom_id": ATOM,
            "event_type": kind.value,
            "timestamp": f"2026-08-12T00:{44 + index:02d}:00+00:00",
            "state_summary": "Result-blind C045 immediate-successor component-incidence pre-candidate gate; no target output or candidate identity exists.",
            "action_summary": kind.value,
            "evidence_pointers": evidence,
            "alternatives_considered": (
                "count target formulas or types",
                "search a target pair family",
                "run fractional or lower-bound machinery",
                "freeze the exact incidence-classification gate only",
            ),
            "decision_rationale": "C043 and C044 make exact full-history component incidence the smallest discriminator that changes the proof DAG before any downstream cover action.",
            "outputs": outputs,
            "uncertainties": (
                "target incidence is unobserved",
                "same-context expert roles are not independent review",
            ),
            "residuals": (
                "immediate successor component-incidence branch unresolved",
                "no cover conclusion",
                "root OPEN",
            ),
            "next_steps": (
                "only after all gates pass, freeze an incidence-classification plan without executing it",
            ),
            "previous_event_hash": previous,
        }
        artifact_hash = _hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **payload))
        previous = artifact_hash
    return MathResearchTrace(
        trace_id="PNP-O9d12a2a1b-C045-PRETRACE-20260812",
        entries=tuple(entries),
    )


def preservation_receipt() -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id="PNP-C045-ROOT-COORDINATE-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="explicit superlogarithmic full-cover family with a proved circuit-complexity and P-versus-NP bridge",
        surrogate_coordinate="finite immediate-successor quotient component incidence",
        bridge_edges=(
            BridgeEdge(
                edge_id="C045-BRIDGE-1",
                source_coordinate="finite immediate-successor quotient component incidence",
                target_coordinate="finite full-cover lower-bound mechanism",
                interface_map="coupling can only retire one separable upper construction; a lower-bound mechanism remains required",
                proof_status=EdgeProofStatus.UNPROVED,
                enabling_assumptions=("exact incidence classification", "source-valid full-cover model"),
            ),
            BridgeEdge(
                edge_id="C045-BRIDGE-2",
                source_coordinate="finite full-cover lower-bound mechanism",
                target_coordinate="explicit asymptotic superlogarithmic family",
                interface_map="requires a uniform recurrence or invariant and polynomial-time explicitness",
                proof_status=EdgeProofStatus.UNPROVED,
                enabling_assumptions=("uniformity", "asymptotic growth", "explicitness"),
            ),
            BridgeEdge(
                edge_id="C045-BRIDGE-3",
                source_coordinate="explicit asymptotic superlogarithmic family",
                target_coordinate="P versus NP root claim",
                interface_map="requires exact source transference and the registered complexity-theoretic bridge",
                proof_status=EdgeProofStatus.CONDITIONAL,
                enabling_assumptions=("statement alignment", "source theorem hypotheses"),
            ),
        ),
        obligations=(
            Obligation("C045-O1", "prove the exact incidence branch", True, False),
            Obligation("C045-O2", "construct and prove a cover lower-bound mechanism", True, False),
            Obligation("C045-O3", "prove uniform asymptotic growth and explicitness", True, False),
            Obligation("C045-O4", "discharge the circuit and root bridge", True, False),
        ),
        known_disanalogies=(
            "finite coupling is not cover growth",
            "retiring one upper construction is not a lower bound",
            "finite quotient behavior is not an asymptotic family theorem",
        ),
        source_authority=CoordinateAuthority.PROPOSAL_ONLY,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world=(
            "a finite quotient has cross-component support coupling but still admits a constant legal-pair cover"
        ),
        registered_observations=(
            RegisteredStateObservation(
                "C043-parent",
                "type-growth-without-direct-coupling-gate",
                "finite-upper-obstruction-only",
            ),
            RegisteredStateObservation(
                "C044-parent",
                "component-separable-support",
                "finite-upper-obstruction-only",
            ),
        ),
        reverification_triggers=(
            "target incidence branch is established",
            "a downstream cover mechanism is proposed",
            "the graph family or source transference changes",
        ),
        prior_failure_ids=(
            "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING",
            "F-C044-HETEROGENEOUS-BLOCK-MULTIPLEXING",
        ),
    )


def build_current_gate_plan():
    fiber = context()
    memory = memory_review(fiber.packet_hash)
    transformation_memory, shortcut = transformation_memory_and_review(
        fiber.packet_hash, memory.artifact_hash
    )
    research_trace = trace(
        fiber.packet_hash, memory.artifact_hash, shortcut.artifact_hash
    )
    preservation = preservation_receipt()
    expected_preservation_sha256 = preservation.document()[
        "receipt_canonical_sha256"
    ]
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=(
                "frozen immediate recursive extension",
                "full-history row and column twins",
                "quotient complement support components",
            ),
            relations=(
                "cross-band relations update accumulated endpoint fibres",
                "equal full fibres define twins",
                "quotient support determines inherited-component incidence",
            ),
            domain="circuit complexity / discrete complexity / two-dimensional cover",
            goal_type=(
                "freeze a branch-complete immediate-successor incidence-classification plan without evaluating it"
            ),
        ),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=fiber,
        memory_review=memory,
        transformation_memory=transformation_memory,
        shortcut_review=shortcut,
        research_trace=research_trace,
        preservation_receipt=preservation,
        require_preservation_gate=True,
        expected_preservation_sha256=expected_preservation_sha256,
    )
    return (
        plan,
        fiber,
        memory,
        transformation_memory,
        shortcut,
        research_trace,
        preservation,
    )


def build_documents() -> dict[str, dict]:
    plan, fiber, memory, transformation_memory, shortcut, research_trace, preservation = (
        build_current_gate_plan()
    )
    atomization = _with_artifact_hash(
        {
            "schema_version": "1.0.0",
            "atomization_id": "PNP-O9d12a2a1b-C045-ATOMIZATION-20260812",
            "recorded_at": "2026-08-12T00:39:00+00:00",
            "atom_id": ATOM,
            "parent_atom_id": "O9d12a2a1b-C044-RETROSPECTIVE",
            "target_extension": "U16_TO_U17_IMMEDIATE_SOURCE_EXTENSION",
            "object": "The untouched immediate recursive extension, its canonical cross-band relation, full accumulated row and column neighbourhood twins, and quotient support-component incidence.",
            "qoi": "EXACT_FULL_HISTORY_QUOTIENT_COMPONENT_INCIDENCE",
            "allowed_result_branches": [
                "NO_NEW_SEMANTIC_CELL",
                "NO_CROSS_COMPONENT_COUPLING",
                "CROSS_COMPONENT_COUPLING_WITNESS",
                "OLD_TYPE_COLLISION_OR_SPLIT",
                "CANNOT_CHECK",
            ],
            "atomic_obligations": [
                "freeze the immediate source-defined extension without evaluating it",
                "keep fallback and canonical branches separate",
                "classify target residuals analytically only after a later candidate freeze",
                "recompute full-history twins on both sides and account for old-type collisions",
                "classify quotient support incidence before any cover action",
            ],
            "candidate_generation_allowed": False,
            "candidate_proposed": False,
            "target_output_accessed": False,
            "target_state": "TARGET_OUTCOME_UNOBSERVED",
            "authority_boundary": {
                "incidence_is_not_cover_growth": True,
                "finite_computation_is_proof": False,
                "grants_circuit_lower_bound": False,
                "grants_p_vs_np_authority": False,
            },
        }
    )
    tool_snapshot = _with_artifact_hash(
        {
            "schema_version": "1.0.0",
            "snapshot_id": "PNP-C045-TOOL-SNAPSHOT-20260812",
            "target_atom_id": ATOM,
            "tools": [
                {
                    "tool_id": "T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",
                    "source_blob": C043_TOOL_BLOB,
                    "applicability": "APPLICABLE_WITH_FRESH_FULL_HISTORY_VALIDATION",
                    "use": "classify exact accumulated twins and quotient support only",
                    "non_guarantees": ["no target outcome", "no lower bound", "no recurrence"],
                },
                {
                    "tool_id": "T-PNP-HETEROGENEOUS-BLOCK-MULTIPLEXING-UPPER",
                    "source_blob": C044_TOOL_BLOB,
                    "applicability": "PROPOSAL_ONLY_WARNING_NOT_SELECTED_TOOL",
                    "use": "supply the no-cross-component-cell repeat-failure condition",
                    "non_guarantees": ["not promoted by one retrospective use", "no target prediction"],
                },
            ],
            "target_state": "TARGET_OUTCOME_UNOBSERVED",
        }
    )
    failure_snapshot = _with_artifact_hash(
        {
            "schema_version": "1.0.0",
            "snapshot_id": "PNP-C045-FAILURE-SNAPSHOT-20260812",
            "target_atom_id": ATOM,
            "failures": [
                {
                    "failure_id": "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING",
                    "source_blob": C043_FAILURE_BLOB,
                    "warning": "type or semantic growth is not cover-resource growth",
                },
                {
                    "failure_id": "F-C044-HETEROGENEOUS-BLOCK-MULTIPLEXING",
                    "source_blob": C044_FAILURE_BLOB,
                    "warning": "run the exact component-incidence gate before cover search",
                },
                {
                    "failure_id": "F-C010-MULTIPLEXING",
                    "warning": "distinct components may reuse local pair indices",
                },
            ],
            "reuse_assessment": "DIFFERENCE_WITNESSED_ONLY_BY_UNTOUCHED_IMMEDIATE_EXTENSION; RUN_OLD_COUPLING_FALSIFIER_FIRST",
            "target_state": "TARGET_OUTCOME_UNOBSERVED",
        }
    )
    expert = expert_review_document(fiber.packet_hash)
    documents = {
        "atomization": atomization,
        "context": _document(fiber),
        "tool_snapshot": tool_snapshot,
        "failure_snapshot": failure_snapshot,
        "memory": _document(memory),
        "transformation_memory": _document(transformation_memory),
        "expert_review": expert,
        "shortcut_review": _document(shortcut),
        "preservation": _jsonable(preservation.document()),
        "trace": _document(research_trace),
    }
    gate = _with_artifact_hash(
        {
            "schema_version": "1.0.0",
            "receipt_id": "PNP-C045-LATEST-RAKL-PRE-CANDIDATE-GATE-20260812",
            "framework_commit": FRAMEWORK_SHA,
            "framework_version": "0.7.0",
            "application_base_commit": APPLICATION_BASE_SHA,
            "atom_id": ATOM,
            "artifact_bindings": {
                "context_hash": fiber.packet_hash,
                "memory_review_hash": memory.artifact_hash,
                "transformation_memory_snapshot_hash": transformation_memory.snapshot_hash,
                "shortcut_review_hash": shortcut.artifact_hash,
                "trace_last_event_hash": research_trace.entries[-1].artifact_hash,
                "preservation_sha256": preservation.document()["receipt_canonical_sha256"],
            },
            "gate_verdicts": {
                "context": plan.context_gate.verdict.value,
                "dual_memory": plan.memory_gate.verdict.value,
                "obstruction_transformation": plan.shortcut_gate.verdict.value,
                "trace": plan.trace_gate.verdict.value,
                "preservation": plan.preservation_gate.verdict.value,
                "selected_mode": shortcut.selected_mode.value,
                "candidate_generation_allowed": plan.candidate_generation_allowed,
                "licensed_action": "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY",
            },
            "result_capability_firewall": {
                "allowed": [
                    "read committed definitions and prior proofs",
                    "freeze context, memory, shortcut, trace, and branch specification",
                    "form a later incidence-classification plan",
                ],
                "forbidden": [
                    "execute target decoder or satisfiability logic",
                    "run target enumeration, pair search, fractional program, or oracle",
                    "construct or report a target cell, cover, counterexample, count, or outcome",
                    "inspect unreviewed target-result branches",
                ],
                "breach_policy": "MARK_RETROSPECTIVE_AND_MOVE_STRICT_ASSURANCE_TO_A_NEW_UNTOUCHED_TARGET",
            },
            "chronology": {
                "candidate_identity": None,
                "candidate_proposed": False,
                "target_output_accessed": False,
                "target_state": "TARGET_OUTCOME_UNOBSERVED",
            },
            "authority": {
                "assurance_only": True,
                "grants_mathematical_result": False,
                "grants_theorem_truth": False,
                "grants_novelty": False,
                "grants_independent_review": False,
                "grants_p_vs_np_authority": False,
            },
        }
    )
    documents["gate"] = gate
    return documents
