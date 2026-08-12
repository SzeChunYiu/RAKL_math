"""Strict RAKL-v3 pre-candidate packet for C047.

This fixture has no decoder, satisfiability, enumeration, or target-result
capability.  It may license only a target-blind lemma candidate about whether
quadrant orientation alone can repair C046.  All assurance work is zero
mathematical credit.
"""
from __future__ import annotations

from dataclasses import asdict
from enum import Enum
import hashlib
import json

from rakl.math_context import AnalogyScanStatus, CrossDomainAnalogy, MathContextFiber, MethodTransfer
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType
from rakl.root_coordinate_preservation import (
    BridgeEdge, CoordinateAuthority, EdgeProofStatus, Obligation,
    RegisteredStateObservation, RootCoordinatePreservationReceipt,
)
from rakl.semantic_shortcut import (
    ObstructionFingerprint, ObstructionTransformationEpisode,
    ObstructionTransformationReview, RouteSearchStatus, ShortcutMode,
    StructuralMappingWitness, TransformationEpisodeAuthority,
    build_transformation_memory,
)

ATOM = "O9d12a2a1b-C047"
APPLICATION_BASE_SHA = "ec8a9eb5eeedaaf1d3f497a8688384256a2079e0"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
FROZEN_AT = "2026-08-12T02:59:20Z"
DECODER_BLOB = "fcc4814dd618da96ef9bb8144a4783a0a6e886e1"
DECODER_RAW_SHA256 = "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"
C046_RESULT_BLOB = "cca23988bad443f252c5be8489e6b1562b1acbb0"
C045_FAILURE_BLOB = "12a8099833c27218550855bb37614e8cfb8b1274"

BASE = "research/real_math/millennium/p_vs_np"
PATHS = {
    "atomization": f"{BASE}/02_problem_dag/O9d12a2a1b_C047_ATOMIZATION_20260812.json",
    "context": f"{BASE}/01_frontier/O9d12a2a1b_C047_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/O9d12a2a1b_C047_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/O9d12a2a1b_C047_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/O9d12a2a1b_C047_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/O9d12a2a1b_C047_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/O9d12a2a1b_C047_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/O9d12a2a1b_C047_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": f"{BASE}/09_trace/O9d12a2a1b_C047_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": f"{BASE}/09_trace/O9d12a2a1b_C047_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": f"{BASE}/09_trace/O9d12a2a1b_C047_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}


def _hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


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


def _sealed(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = ""
    result["artifact_hash"] = _hash(result)
    return result


def context() -> MathContextFiber:
    transfer = MethodTransfer(
        source_context="coordinate-change feasibility in recursively quadrant-defined relations",
        method="after a partition obstruction, isolate the smallest structural coordinate change and test whether its image actually intersects the desired syntactic class",
        shared_structure=(
            "relations are assembled from inherited and fresh blocks",
            "quadrant orientation determines whether a decoded prefix label is old or fresh",
            "a fixed MAGIC header constrains canonical row labels",
            "the desired event requires exact label equality, not merely occupancy of the same binary half",
        ),
        required_assumptions=(
            "the C041 decoder and equal prefix/suffix split remain unchanged",
            "the candidate changes only old-new versus prefix-preserving new-old quadrant placement",
            "the seed and inherited old-old embedding remain unchanged",
        ),
        disanalogies=(
            "putting support in the fresh row half need not align its header with a later canonical prefix",
            "exact transpose would place the suffix, not the prefix, on the fresh row and is outside this atom",
            "orientation feasibility does not determine quotient covers or lower bounds",
        ),
        repair_question="Does moving or copying the decoded prefix coordinate into the fresh-row quadrant suffice for canonical row-prefix coupling, or must the label map/split also change?",
        source_anchors=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/04_candidates/C041_fx_sat_one_sided.py@blob:{DECODER_BLOB}",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_PROOF_CHECK_RESULT_20260812.json@blob:{C046_RESULT_BLOB}",
        ),
    )
    analogy = CrossDomainAnalogy(
        source_kind="engineering / addressing",
        source_situation="moving a cable into the correct rack does not connect it when the plug pinout remains shifted",
        common_abstraction=("coarse location repair", "fine label alignment", "exact connection requirement"),
        source_to_target_mapping=(
            "rack half -> old/fresh row quadrant",
            "pinout -> binary header alignment",
            "electrical connection -> exact row-prefix collision",
        ),
        shared_constraints=("coarse placement is necessary but not sufficient", "success requires equality at the finer interface"),
        disanalogies=("rack wiring supplies no theorem authority", "binary strings require exact source-specific proof"),
        proposed_principle="after repairing a coarse partition obstruction, test fine interface congruence before enumerating outcomes",
        validation_obligation="classify every possible high fresh-row label under the frozen decoder and compare it symbolically with a current canonical prefix",
        provenance_note="proposal-only engineering analogy; no mathematical authority",
    )
    payload = {
        "atom": ATOM,
        "base": APPLICATION_BASE_SHA,
        "coordinates": [
            "quadrant-orientation-only successor family with unchanged equal split and decoder",
            "old-new, prefix-preserving new-old, or their two-sided union",
            "fresh-row label 2^(n-1)+r where r is the old prefix coordinate",
            "current canonical n-bit row prefix beginning with fixed MAGIC",
            "exact label collision rather than coarse high-half occupancy",
        ],
        "sources": [DECODER_BLOB, C046_RESULT_BLOB, C045_FAILURE_BLOB],
    }
    return MathContextFiber(
        atom_id=ATOM,
        object_context="Target-blind repair-feasibility atom: decide whether changing only quadrant orientation, while keeping the C041 equal split, prefix coordinate, decoder, seed, and inherited embedding fixed, can make a complement row equal a current canonical MAGIC prefix.",
        structural_coordinates=tuple(payload["coordinates"]),
        equivalent_formulations=(
            "intersection of orientation-generated fresh rows with current canonical MAGIC-prefix rows",
            "binary header congruence after prepending the fresh-half bit",
            "feasibility of prefix-preserving mirror or two-sided support before any target enumeration",
        ),
        solved_analogues=("C046 lower-half versus MAGIC high-half separation in the original one-sided orientation",),
        near_solved_analogues=("prefix-code synchronization and delimiter alignment under one-bit shifts",),
        method_transfers=(transfer,),
        explicit_disanalogies=(
            "coarse high-half occupancy does not imply exact row equality",
            "the all-zero contradiction and canonical MAGIC branch must both be classified",
            "suffix-to-fresh-row transpose, overlapping splits, and relabelled encodings are outside this atom",
            "an orientation result is not a cover theorem, circuit lower bound, or P-versus-NP result",
            "computation is not proof and assurance is not mathematics",
        ),
        source_anchors=transfer.source_anchors,
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(analogy,),
        analogy_scan_notes="One proposal-only coarse-location versus fine-interface analogy survives explicit mapping and disanalogy review.",
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash=_hash(payload),
    )


def memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {"atom": ATOM, "context": context_hash, "tools": ["T-PNP-C046-PARTITION-INVARIANT-FEASIBILITY-FIRST"], "failures": ["F-C045-U17-PROJECTION-DISJOINT", "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING"]}
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash=f"gitblob:{C046_RESULT_BLOB}",
        failure_lattice_snapshot_hash=f"gitblob:{C045_FAILURE_BLOB}+gitref:C043-first-row-split",
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "prefix-preserving new-old mirror",
            "old-new plus prefix-preserving new-old two-sided union",
            "exact transpose with suffix on the fresh row",
            "overlapping split or coordinate relabelling",
        ),
        relevant_tool_ids=("T-PNP-C046-PARTITION-INVARIANT-FEASIBILITY-FIRST",),
        relevant_failure_ids=("F-C045-U17-PROJECTION-DISJOINT", "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING"),
        selected_tool_ids=("T-PNP-C046-PARTITION-INVARIANT-FEASIBILITY-FIRST",),
        tool_applicability_notes=("C046's invariant-first operation is reusable only as a search-order heuristic: after changing the quadrant, rederive the exact high-row label language and compare it with MAGIC prefixes.",),
        failure_reuse_notes=(
            "C045 warns that fresh columns alone cannot couple backward; C047 materially changes row occupancy but must prove that this restores equality rather than merely a coarse half.",
            "C043 warns that semantic multiplicity and support growth do not imply the requested collision or cover growth.",
        ),
        unresolved_warnings=(
            "No later target result has been accessed.",
            "No conclusion about mirror or two-sided feasibility is available until a candidate is publicly frozen and checked.",
            "Exact transpose and relabelled/split-changing variants are intentionally outside the first repair atom.",
            "Same-context review is not independent peer review.",
        ),
        evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_PROOF_CHECK_RESULT_20260812.json@blob:{C046_RESULT_BLOB}",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/O9d12a2a1b_C045_U17_COUPLING_FAILURE_DELTA_20260812.json@blob:{C045_FAILURE_BLOB}",
        ),
        artifact_hash=_hash(payload),
    )


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-PNP-C047-ORIENTATION-ONLY-ROW-COLLISION-REPAIR",
        domain="mathematics",
        roles=("inherited support", "orientation-generated fresh rows", "canonical prefix rows", "exact label interface"),
        relations=(
            "quadrant placement controls which decoded coordinate receives a new leading fresh-half bit",
            "the decoder classifies non-tautological words into all-zero and MAGIC forms",
            "a collision requires exact binary equality between a generated row and a current canonical prefix",
        ),
        constraints=("unchanged decoder and equal split", "prefix coordinate remains the semantic row coordinate", "only quadrant orientation may change", "target results remain unaccessed"),
        failure_mechanisms=("coarse high-half repair may leave the generated binary header shifted relative to MAGIC",),
        invariants_to_preserve=("SAT reduction direction", "canonical/fallback separation", "target blindness", "root authority boundary"),
        desired_transition=("decide whether orientation alone restores exact canonical row coupling",),
        forbidden_losses=("target-result leakage", "silent decoder or label-map change", "promoting feasibility to root authority"),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    target = obstruction()
    source_obs = ObstructionFingerprint(
        obstruction_id="OBS-SOURCE-COARSE-REPAIR-THEN-INTERFACE-CHECK",
        domain="mathematics",
        roles=("inherited support", "orientation-generated fresh rows", "canonical prefix rows", "exact label interface"),
        relations=target.relations,
        constraints=target.constraints,
        failure_mechanisms=target.failure_mechanisms,
        invariants_to_preserve=target.invariants_to_preserve,
        desired_transition=target.desired_transition,
        forbidden_losses=target.forbidden_losses,
    )
    episode = ObstructionTransformationEpisode(
        episode_id="E-PNP-C047-COARSE-REPAIR-THEN-INTERFACE-CHECK",
        source_domain="mathematics",
        source_context="C046 recursive support partition and prefix-code alignment analysis",
        source_obstruction=source_obs,
        transformation_name="COARSE_REPAIR_THEN_FINE_INTERFACE_CONGRUENCE",
        operation="after changing the support quadrant, classify the exact generated row-label language and compare it symbolically with the required canonical prefix language",
        preconditions=("recursive support clauses are exhaustive", "decoder output branches are exhaustive", "quadrant placement induces a fixed binary label map"),
        resulting_relations=target.desired_transition,
        preserved_invariants=target.invariants_to_preserve,
        relaxed_or_broken_constraints=(),
        known_breakpoints=("the decoder changes", "the split becomes unequal or overlapping", "the suffix rather than prefix is placed on the fresh row", "a coordinate relabelling is introduced"),
        evidence_pointers=(f"git:{APPLICATION_BASE_SHA}:{BASE}/04_candidates/C041_fx_sat_one_sided.py@blob:{DECODER_BLOB}",),
        authority=TransformationEpisodeAuthority.PROOF_BACKED,
        artifact_hash=_hash({"episode": "E-PNP-C047-COARSE-REPAIR-THEN-INTERFACE-CHECK", "source": DECODER_BLOB}),
    )
    tm = build_transformation_memory(
        memory_id="PNP-C047-OBSTRUCTION-TRANSFORMATION-MEMORY-20260812",
        source_universe=("C041 frozen recursive definition", "C045 coupling failure", "C046 high-half separation result", "prefix-code alignment method"),
        episodes=(episode,),
        evidence_pointers=(episode.evidence_pointers[0], f"gitblob:{C046_RESULT_BLOB}"),
    )
    mapping = StructuralMappingWitness(
        witness_id="MAP-PNP-C047-COARSE-REPAIR-INTERFACE",
        episode_id=episode.episode_id,
        target_obstruction_id=target.obstruction_id,
        role_mapping=tuple((role, role) for role in source_obs.roles),
        shared_relations=target.relations,
        shared_constraints=target.constraints,
        precondition_mapping=(
            (episode.preconditions[0], "define mirror and two-sided successors with no hidden quadrant"),
            (episode.preconditions[1], "classify all-zero, MAGIC canonical, and tautology fallback branches"),
            (episode.preconditions[2], "derive the exact n-bit fresh-row form from the prefix coordinate"),
        ),
        unmatched_source_preconditions=(),
        disanalogies=("C046 separated coarse halves whereas C047 changes the occupied half", "exact transpose and label-map changes are outside scope", "no cover consequence follows"),
        target_validation_obligations=("derive every possible new high row without enumerating targets", "compare each header with MAGIC", "include inherited old rows", "fail closed if decoder or coordinate placement differs"),
        evidence_pointers=(episode.evidence_pointers[0],),
        artifact_hash=_hash({"mapping": "MAP-PNP-C047-PARTITION-INVARIANT", "context": context_hash}),
    )
    review = ObstructionTransformationReview(
        review_id="PNP-C047-OBSTRUCTION-TRANSFORMATION-REVIEW-20260812",
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        research_memory_review_hash=memory_hash,
        episode_memory_snapshot_hash=tm.snapshot_hash,
        obstruction=target,
        direct_search_status=RouteSearchStatus.MATCHES_FOUND,
        jump_search_status=RouteSearchStatus.NOT_RUN,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.SEARCH,
        direct_candidate_episode_ids=(episode.episode_id,),
        direct_mapping_witnesses=(mapping,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=("route selection is proposal-only", "target theorem truth remains unchecked", "root remains open"),
        evidence_pointers=(PATHS["context"], PATHS["memory"], PATHS["transformation_memory"]),
        artifact_hash=_hash({"review": "PNP-C047", "memory": tm.snapshot_hash, "mapping": mapping.artifact_hash}),
    )
    return tm, review


def expert_review_document(context_hash: str) -> dict:
    roles = [
        ("domain_theory_lead", "Distinguish a prefix-preserving new-old mirror from the literal matrix transpose, which places the suffix on the fresh row.", "Scope the first atom to orientation-only prefix placement; do not generalize to transpose or relabelled families."),
        ("analogy_method_transfer_lead", "Retain coarse-location versus interface-alignment transfer only with exact bit mapping.", "The rack/pinout analogy proposes a discriminator but supplies no proof."),
        ("adversarial_falsification_lead", "Attack the all-zero contradiction, short header lengths, inherited old rows, and both mirror-only and two-sided variants.", "Any generated high row equal to a current MAGIC prefix refutes a separation candidate."),
        ("formal_methods_lead", "Bind the level convention, equal split, prefix coordinate, fresh leading bit, and exhaustive decoder branches.", "The evaluator must be inert before public freeze and must not import the decoder or enumerate later targets."),
        ("novelty_research_value_lead", "Treat any result as a scoped classification of one minimal repair.", "Value is identifying whether quadrant orientation suffices and the exact next repair condition, not novelty or P-versus-NP progress."),
    ]
    return _sealed({
        "schema_version": "1.0.0",
        "review_id": "PNP-C047-EXPERT-CONTEXT-REVIEW-20260812",
        "atom_id": ATOM,
        "context_hash": context_hash,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
        "role_reviews": [{"role": role, "objection": objection, "recommendation": recommendation} for role, objection, recommendation in roles],
        "disagreements": ["Whether exact transpose should be included now; the adversarial and formal lenses require excluding it because it changes which decoded coordinate becomes the fresh row."],
        "strongest_objection": "Calling prefix-preserving new-old placement a transpose would erase a load-bearing coordinate distinction and invalidate the scope.",
        "unresolved_uncertainty": "No candidate proof or result exists at this stage.",
        "next_action_recommendation": "After all gates pass, freeze one target-blind quadrant-orientation feasibility lemma and inert symbolic proof-obligation evaluator; do not scan target levels.",
        "mathematical_saturation_credit": False,
        "mathematical_result_credit": False,
    })


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
    evidence_map = {
        ResearchTraceEventType.ATOMIZED: PATHS["atomization"],
        ResearchTraceEventType.CONTEXT_FROZEN: PATHS["context"],
        ResearchTraceEventType.ANALOGY_SCAN: PATHS["context"],
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW: PATHS["context"],
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW: PATHS["expert_review"],
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW: PATHS["memory"],
        ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW: PATHS["shortcut_review"],
        ResearchTraceEventType.NEXT_STEP_PROPOSED: PATHS["gate"],
    }
    entries = []
    previous = ""
    for i, kind in enumerate(kinds, 1):
        outputs = ["PRE_CANDIDATE_ONLY", "TARGET_RESULT_UNACCESSED", "ZERO_MATHEMATICAL_CREDIT"]
        if kind is ResearchTraceEventType.CONTEXT_FROZEN: outputs.insert(0, context_hash)
        if kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW: outputs.insert(0, memory_hash)
        if kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW: outputs[:0] = [shortcut_hash, "selected_mode:SEARCH"]
        payload = {
            "event_id": f"O9d12a2a1b-C047-E{i:02d}", "atom_id": ATOM,
            "event_type": kind.value, "timestamp": f"2026-08-12T02:59:{20+i:02d}Z",
            "state_summary": "C047 asks whether prefix-preserving mirror or two-sided quadrant placement alone can repair the C046 row-collision impossibility; no candidate result, later target, or evaluator has been accessed or executed.",
            "action_summary": kind.value, "evidence_pointers": [evidence_map[kind]],
            "alternatives_considered": ["scan later finite targets", "use exact transpose with suffix row", "change encoding or split", "test orientation-only interface congruence"],
            "decision_rationale": "C046 proves the original quadrant is impossible, so the smallest repair is a quadrant change; the selected SEARCH episode requires checking exact label-interface congruence before any finite target search.",
            "outputs": outputs,
            "uncertainties": ["candidate theorem not yet frozen", "same-context review is not independent"],
            "residuals": ["orientation-only repair feasibility unresolved", "exact transpose and label-map repairs outside scope", "root OPEN"],
            "next_steps": ["only after gate PASS, freeze the quadrant-orientation feasibility lemma candidate and inert evaluator", "do not access any later target result"],
            "previous_event_hash": previous,
        }
        artifact_hash = _hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **{**payload, "event_type": kind}))
        previous = artifact_hash
    return MathResearchTrace("PNP-O9d12a2a1b-C047-PRE-CANDIDATE-TRACE-20260812", tuple(entries))


def preservation_receipt() -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id="PNP-C047-ROOT-COORDINATE-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="explicit superlogarithmic full-cover family with circuit and P-versus-NP bridge",
        surrogate_coordinate="whether a quadrant-orientation-only successor can restore canonical prefix-row collision feasibility",
        bridge_edges=(
            BridgeEdge("C047-B1", "orientation-repair feasibility", "cover obstruction", "an exact row collision is only a precondition for testing one coupling mechanism", EdgeProofStatus.UNPROVED, ("collision exists", "legal cover polarity")),
            BridgeEdge("C047-B2", "cover obstruction", "P versus NP", "requires uniform superlogarithmic lower bound and exact complexity bridge", EdgeProofStatus.UNPROVED, ("uniformity", "explicitness", "source theorem alignment")),
        ),
        obligations=(
            Obligation("C047-O1", "classify orientation-only collision feasibility", True, False),
            Obligation("C047-O2", "supply a cover lower-bound mechanism", True, False),
            Obligation("C047-O3", "discharge asymptotic and complexity bridge", True, False),
        ),
        known_disanalogies=("repair classification is not root progress", "failure of one orientation class does not decide P versus NP"),
        source_authority=CoordinateAuthority.PROPOSAL_ONLY,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world="orientation-only placement fails while an out-of-scope relabelled or suffix-row family admits useful coupling",
        registered_observations=(
            RegisteredStateObservation("C046", "original-orientation-impossible", "quadrant repair not yet classified"),
            RegisteredStateObservation("C047-pre", "orientation-feasibility-unresolved", "root open"),
        ),
        reverification_triggers=("decoder changes", "split or row-coordinate changes", "suffix-row transpose is admitted", "a new family is proposed"),
        prior_failure_ids=("F-C045-U17-PROJECTION-DISJOINT", "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING"),
    )


def build_current_gate_plan():
    fiber = context()
    memory = memory_review(fiber.packet_hash)
    tm, shortcut = transformation_memory_and_review(fiber.packet_hash, memory.artifact_hash)
    research_trace = trace(fiber.packet_hash, memory.artifact_hash, shortcut.artifact_hash)
    preservation = preservation_receipt()
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("orientation-only successor support", "orientation-generated fresh rows", "canonical prefix rows"),
            relations=("quadrant placement", "prefix-to-fresh-row binary map", "exact row-label intersection"),
            domain="circuit complexity / recursive bipartite graph covers",
            goal_type="freeze a target-blind quadrant-orientation repair-feasibility lemma before any later target access",
        ),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=fiber, memory_review=memory, transformation_memory=tm,
        shortcut_review=shortcut, research_trace=research_trace,
        preservation_receipt=preservation, require_preservation_gate=True,
        expected_preservation_sha256=preservation.document()["receipt_canonical_sha256"],
    )
    return plan, fiber, memory, tm, shortcut, research_trace, preservation


def build_documents() -> dict[str, dict]:
    plan, fiber, memory, tm, shortcut, research_trace, preservation = build_current_gate_plan()
    atomization = _sealed({
        "schema_version": "1.0.0", "atomization_id": "PNP-C047-ATOMIZATION-20260812",
        "recorded_at": "2026-08-12T02:59:19Z", "atom_id": ATOM,
        "parent_atom_id": "O9d12a2a1b-C046",
        "object": "The class of equal-split C041 successor recursions obtained by moving or copying the decoded prefix coordinate into a prefix-preserving new-old quadrant, with decoder, seed, and inherited embedding fixed.",
        "qoi": "ORIENTATION_ONLY_CANONICAL_ROW_COLLISION_FEASIBILITY",
        "allowed_result_branches": ["ORIENTATION_ONLY_REPAIR_FEASIBLE", "ORIENTATION_ONLY_REPAIR_IMPOSSIBLE", "CANNOT_CHECK"],
        "atomic_obligations": ["define mirror-only and two-sided orientation variants", "classify every possible generated row-label form", "compare exact generated headers with current MAGIC prefixes", "preserve exact-transpose and relabelling residuals"],
        "candidate_generation_allowed": False, "candidate_proposed": False,
        "target_result_accessed": False, "target_state": "TARGET_RESULT_UNACCESSED",
        "authority_boundary": {"assurance_only_zero_credit": True, "grants_cover_lower_bound": False, "grants_p_vs_np_authority": False},
    })
    tool_snapshot = _sealed({
        "schema_version": "1.0.0", "snapshot_id": "PNP-C047-TOOL-SNAPSHOT-20260812", "target_atom_id": ATOM,
        "application_base_commit": APPLICATION_BASE_SHA,
        "tools": [{"tool_id": "T-PNP-C046-PARTITION-INVARIANT-FEASIBILITY-FIRST", "source": "C046 high-half separation plus C041 recursive definition", "preconditions": ["exact target-specific coordinate map", "fixed decoder branches"], "guarantees": ["search-order pruning after target-specific proof"], "non_guarantees": ["worked once is not universal", "no theorem before proof", "no cover or root authority"]}],
        "target_state": "TARGET_RESULT_UNACCESSED", "mathematical_credit": False,
    })
    failure_snapshot = _sealed({
        "schema_version": "1.0.0", "snapshot_id": "PNP-C047-FAILURE-SNAPSHOT-20260812", "target_atom_id": ATOM,
        "failures": [
            {"failure_id": "F-C045-U17-PROJECTION-DISJOINT", "warning": "fresh columns cannot couple backward without exact old/new row-projection collision"},
            {"failure_id": "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING", "warning": "semantic type growth does not imply collision or cover growth"},
        ],
        "difference_witness": {"changed_question": "fresh-row orientation instead of the original old-row orientation", "restored_assumption": "coarse high-half occupancy only; exact equality remains unproved", "cheapest_repeat_failure_test": "derive generated row headers and compare symbolically with MAGIC"},
        "target_state": "TARGET_RESULT_UNACCESSED", "mathematical_credit": False,
    })
    expert = expert_review_document(fiber.packet_hash)
    documents = {
        "atomization": atomization, "context": _document(fiber), "tool_snapshot": tool_snapshot,
        "failure_snapshot": failure_snapshot, "memory": _document(memory),
        "transformation_memory": _document(tm), "expert_review": expert,
        "shortcut_review": _document(shortcut), "preservation": _jsonable(preservation.document()),
        "trace": _document(research_trace),
    }
    integrity = {"algorithm": "SHA-256", "canonicalization": "JSON_SORT_KEYS_COMPACT_UTF8", "scope": "FULL_PARSED_DOCUMENT_INCLUDING_DECLARED_RUNTIME_HASHES", "inputs": {name: {"path": PATHS[name], "canonical_sha256": _hash(doc)} for name, doc in sorted(documents.items())}}
    gate = _sealed({
        "schema_version": "1.0.0", "receipt_id": "PNP-C047-PRE-CANDIDATE-GATE-20260812",
        "framework_commit": FRAMEWORK_SHA, "framework_version": "0.7.0", "application_base_commit": APPLICATION_BASE_SHA, "atom_id": ATOM,
        "full_document_integrity": integrity,
        "artifact_bindings": {"context_hash": fiber.packet_hash, "memory_review_hash": memory.artifact_hash, "transformation_memory_snapshot_hash": tm.snapshot_hash, "shortcut_review_hash": shortcut.artifact_hash, "trace_last_event_hash": research_trace.entries[-1].artifact_hash, "preservation_sha256": preservation.document()["receipt_canonical_sha256"], "full_document_integrity_hash": _hash(integrity)},
        "gate_verdicts": {"context": plan.context_gate.verdict.value, "dual_memory": plan.memory_gate.verdict.value, "obstruction_transformation": plan.shortcut_gate.verdict.value, "trace": plan.trace_gate.verdict.value, "preservation": plan.preservation_gate.verdict.value, "selected_mode": shortcut.selected_mode.value, "candidate_generation_allowed": plan.candidate_generation_allowed, "licensed_action": "FREEZE_QUADRANT_ORIENTATION_FEASIBILITY_LEMMA_CANDIDATE_ONLY"},
        "application_authority": {"licensed_actions": ["FREEZE_QUADRANT_ORIENTATION_FEASIBILITY_LEMMA_CANDIDATE_ONLY"], "candidate_construction_authorized": True, "target_evaluator_execution_authorized": False, "finite_target_scan_authorized": False},
        "result_capability_firewall": {"allowed": ["read frozen definitions and prior reviewed lessons", "freeze one mathematical orientation-feasibility lemma candidate and inert symbolic evaluator"], "forbidden": ["execute or import the target decoder", "enumerate any later target", "inspect result-signaling successor branches", "report a target witness/count/cover", "silently include exact transpose or change the split/encoding"], "breach_policy": "MARK_RETROSPECTIVE_AND_SELECT_A_DIFFERENT_UNTOUCHED_FAMILY"},
        "chronology": {"candidate_identity": None, "candidate_proposed": False, "target_result_accessed": False, "target_state": "TARGET_RESULT_UNACCESSED", "public_candidate_freeze": "PENDING_AFTER_CANDIDATE_COMMIT_AND_PR"},
        "authority": {"assurance_only": True, "mathematical_saturation_credit": False, "mathematical_result_credit": False, "grants_theorem_truth": False, "grants_novelty": False, "grants_independent_review": False, "grants_p_vs_np_authority": False},
    })
    documents["gate"] = gate
    return documents


if __name__ == "__main__":
    print(json.dumps(build_documents(), indent=2, sort_keys=True))
