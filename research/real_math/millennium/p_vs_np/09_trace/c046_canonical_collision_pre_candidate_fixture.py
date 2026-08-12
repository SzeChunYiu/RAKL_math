"""Strict RAKL-v3 pre-candidate packet for C046.

This fixture has no decoder, satisfiability, enumeration, or target-result
capability.  It may license only a later mathematical partition/separation
lemma candidate.  All assurance work is zero mathematical credit.
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

ATOM = "O9d12a2a1b-C046"
APPLICATION_BASE_SHA = "ac8c0745be8aed791a446fd55fcf5154cac01962"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
FROZEN_AT = "2026-08-12T02:15:00Z"
DECODER_BLOB = "fcc4814dd618da96ef9bb8144a4783a0a6e886e1"
DECODER_RAW_SHA256 = "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"
C045_LESSON_BLOB = "294cacf54775741e4b916ceed271ec7c6becfe74"
C045_FAILURE_BLOB = "12a8099833c27218550855bb37614e8cfb8b1274"

BASE = "research/real_math/millennium/p_vs_np"
PATHS = {
    "atomization": f"{BASE}/02_problem_dag/O9d12a2a1b_C046_ATOMIZATION_20260812.json",
    "context": f"{BASE}/01_frontier/O9d12a2a1b_C046_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/O9d12a2a1b_C046_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/O9d12a2a1b_C046_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/O9d12a2a1b_C046_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/O9d12a2a1b_C046_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/O9d12a2a1b_C046_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/O9d12a2a1b_C046_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": f"{BASE}/09_trace/O9d12a2a1b_C046_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": f"{BASE}/09_trace/O9d12a2a1b_C046_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": f"{BASE}/09_trace/O9d12a2a1b_C046_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
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
        source_context="inductive support invariants in recursively quadrant-defined relations",
        method="derive a family-wide projection or partition invariant from the recursive clauses before scanning finite levels for a desired intersection",
        shared_structure=(
            "relations are assembled from inherited and fresh blocks",
            "a fixed label prefix locates canonical source rows in a binary half",
            "the desired event is an intersection of two recursively constrained projections",
        ),
        required_assumptions=(
            "the one-sided recursive complement rule is unchanged",
            "the canonical encoding begins with a fixed leading bit",
            "row coordinates retain their binary order across levels",
        ),
        disanalogies=(
            "an invariant may rule out the desired target instead of selecting one",
            "projection separation does not determine quotient covers or lower bounds",
            "the finite U17 lesson was retrospective and is not prospective authority",
        ),
        repair_question="Does a recursive half-space invariant make every later canonical prefix-row collision impossible, or is there a least admissible level?",
        source_anchors=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/04_candidates/C041_fx_sat_one_sided.py@blob:{DECODER_BLOB}",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/10_feedback/C045_ROW_PROJECTION_COLLISION_MATHEMATICAL_LESSON_20260812.json@blob:{C045_LESSON_BLOB}",
        ),
    )
    analogy = CrossDomainAnalogy(
        source_kind="engineering / ordinary search",
        source_situation="before searching floors for a pipe intersection, verify whether the pipes are confined to disjoint shafts",
        common_abstraction=("desired intersection", "invariant partition", "feasibility before enumeration"),
        source_to_target_mapping=(
            "old active rows -> first shaft",
            "canonical prefix rows -> second shaft",
            "pipe intersection -> prefix-row collision",
        ),
        shared_constraints=("partition membership is preserved", "an intersection requires both projections to share a coordinate"),
        disanalogies=("physical shafts supply no theorem authority", "binary recursion needs its own induction proof"),
        proposed_principle="test family-wide partition feasibility before searching later finite targets",
        validation_obligation="prove both projection containments for every recursive level and exhibit a boundary-level falsifier if either containment fails",
        provenance_note="proposal-only ordinary engineering analogy; no mathematical authority",
    )
    payload = {
        "atom": ATOM,
        "base": APPLICATION_BASE_SHA,
        "coordinates": [
            "least n>=17 with a canonical UNSAT prefix row in accumulated Rows(U_n), or NONE",
            "one-sided recursion with complement support only in inherited old-old and old-new quadrants",
            "fixed MAGIC prefix of every canonical word",
            "binary lower-half versus upper-half row partition",
            "collision feasibility before finite target search",
        ],
        "sources": [DECODER_BLOB, C045_LESSON_BLOB, C045_FAILURE_BLOB],
    }
    return MathContextFiber(
        atom_id=ATOM,
        object_context="Target-blind feasibility atom: decide whether the frozen one-sided family can ever admit a later canonical UNSAT prefix row already present in the accumulated old complement row projection; only if feasible may a least finite target be selected.",
        structural_coordinates=tuple(payload["coordinates"]),
        equivalent_formulations=(
            "intersection of the old nonempty row projection with the canonical MAGIC-prefix row set",
            "lower-half/upper-half separation under the recursive embedding",
            "existence of a collision level before component-coupling evaluation",
        ),
        solved_analogues=("inductive invariant proofs for recursively embedded support sets",),
        near_solved_analogues=("C045 retrospective U17 projection-disjoint instance and necessity lesson",),
        method_transfers=(transfer,),
        explicit_disanalogies=(
            "the least target may not exist",
            "canonical syntax alone does not assert UNSAT",
            "a no-collision lemma is not a cover theorem, circuit lower bound, or P-versus-NP result",
            "computation is not proof and assurance is not mathematics",
        ),
        source_anchors=transfer.source_anchors,
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(analogy,),
        analogy_scan_notes="One proposal-only partition-feasibility analogy survives explicit mapping and disanalogy review.",
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash=_hash(payload),
    )


def memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {"atom": ATOM, "context": context_hash, "tools": ["T-PNP-PARTITION-INVARIANT-FEASIBILITY-FIRST"], "failures": ["F-C045-U17-PROJECTION-DISJOINT", "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING"]}
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash=f"gitblob:{C045_LESSON_BLOB}",
        failure_lattice_snapshot_hash=f"gitblob:{C045_FAILURE_BLOB}+gitref:C043-first-row-split",
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "finite level-by-level canonical enumeration",
            "recursive row-projection invariant",
            "fixed-prefix binary partition lemma",
            "target quotient and cover search",
        ),
        relevant_tool_ids=("T-PNP-PARTITION-INVARIANT-FEASIBILITY-FIRST",),
        relevant_failure_ids=("F-C045-U17-PROJECTION-DISJOINT", "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING"),
        selected_tool_ids=("T-PNP-PARTITION-INVARIANT-FEASIBILITY-FIRST",),
        tool_applicability_notes=("Applicable only to the unchanged one-sided recursion and fixed leading-bit canonical encoding; validate both containments inductively.",),
        failure_reuse_notes=(
            "C045 warns that fresh-half columns cannot repair row-projection disjointness.",
            "C043 warns that semantic multiplicity is not the requested collision or cover growth.",
        ),
        unresolved_warnings=(
            "No later target result has been accessed.",
            "The family-wide conclusion is not available until a candidate is frozen and checked.",
            "Same-context review is not independent peer review.",
        ),
        evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/10_feedback/C045_ROW_PROJECTION_COLLISION_MATHEMATICAL_LESSON_20260812.json@blob:{C045_LESSON_BLOB}",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/O9d12a2a1b_C045_U17_COUPLING_FAILURE_DELTA_20260812.json@blob:{C045_FAILURE_BLOB}",
        ),
        artifact_hash=_hash(payload),
    )


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-PNP-C046-LEAST-CANONICAL-ROW-COLLISION",
        domain="mathematics",
        roles=("recursively inherited support", "canonical prefix rows", "candidate collision level", "partition invariant"),
        relations=(
            "recursive clauses constrain support projection by binary half",
            "fixed leading bits constrain canonical prefixes by binary half",
            "a collision requires the two projections to intersect",
        ),
        constraints=("unchanged one-sided recursion", "fixed MAGIC canonical prefix", "target results remain unaccessed"),
        failure_mechanisms=("desired collision property may be globally forbidden by invariant partition",),
        invariants_to_preserve=("exact source definition", "canonical/fallback separation", "target blindness", "root authority boundary"),
        desired_transition=("replace unbounded finite target scan with family-wide feasibility decision",),
        forbidden_losses=("target-result leakage", "changing the recursive family", "promoting feasibility to root authority"),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    target = obstruction()
    source_obs = ObstructionFingerprint(
        obstruction_id="OBS-SOURCE-PARTITION-BEFORE-SEARCH",
        domain="mathematics",
        roles=("recursively inherited support", "canonical prefix rows", "candidate collision level", "partition invariant"),
        relations=target.relations,
        constraints=target.constraints,
        failure_mechanisms=target.failure_mechanisms,
        invariants_to_preserve=target.invariants_to_preserve,
        desired_transition=target.desired_transition,
        forbidden_losses=target.forbidden_losses,
    )
    episode = ObstructionTransformationEpisode(
        episode_id="E-PNP-C046-PARTITION-INVARIANT-BEFORE-TARGET-SCAN",
        source_domain="mathematics",
        source_context="recursive support feasibility checks before finite collision search",
        source_obstruction=source_obs,
        transformation_name="PARTITION_INVARIANT_FEASIBILITY_FIRST",
        operation="derive invariant projection containments, compare their cells, and search finite targets only if intersection remains possible",
        preconditions=("recursive support clauses are exhaustive", "fixed prefix determines a partition cell", "coordinate embedding preserves the partition"),
        resulting_relations=target.desired_transition,
        preserved_invariants=target.invariants_to_preserve,
        relaxed_or_broken_constraints=(),
        known_breakpoints=("another quadrant contributes support", "canonical encoding loses its fixed leading bit", "coordinate relabelling crosses the partition"),
        evidence_pointers=(f"git:{APPLICATION_BASE_SHA}:{BASE}/04_candidates/C041_fx_sat_one_sided.py@blob:{DECODER_BLOB}",),
        authority=TransformationEpisodeAuthority.PROOF_BACKED,
        artifact_hash=_hash({"episode": "E-PNP-C046-PARTITION-INVARIANT-BEFORE-TARGET-SCAN", "source": DECODER_BLOB}),
    )
    tm = build_transformation_memory(
        memory_id="PNP-C046-OBSTRUCTION-TRANSFORMATION-MEMORY-20260812",
        source_universe=("C041 frozen recursive definition", "C045 retrospective collision necessity lesson", "recursive invariant method"),
        episodes=(episode,),
        evidence_pointers=(episode.evidence_pointers[0], f"gitblob:{C045_LESSON_BLOB}"),
    )
    mapping = StructuralMappingWitness(
        witness_id="MAP-PNP-C046-PARTITION-INVARIANT",
        episode_id=episode.episode_id,
        target_obstruction_id=target.obstruction_id,
        role_mapping=tuple((role, role) for role in source_obs.roles),
        shared_relations=target.relations,
        shared_constraints=target.constraints,
        precondition_mapping=(
            (episode.preconditions[0], "prove recursive quadrants exhaust every support case"),
            (episode.preconditions[1], "prove MAGIC begins with one for every canonical word"),
            (episode.preconditions[2], "prove inherited row indices remain in the lower half"),
        ),
        unmatched_source_preconditions=(),
        disanalogies=("the route can conclude NONE rather than provide a finite target", "no cover consequence follows"),
        target_validation_obligations=("prove the support containment by induction", "prove the canonical prefix containment arithmetically", "check the level-2 base case", "fail if any recursive quadrant or prefix condition differs"),
        evidence_pointers=(episode.evidence_pointers[0],),
        artifact_hash=_hash({"mapping": "MAP-PNP-C046-PARTITION-INVARIANT", "context": context_hash}),
    )
    review = ObstructionTransformationReview(
        review_id="PNP-C046-OBSTRUCTION-TRANSFORMATION-REVIEW-20260812",
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
        artifact_hash=_hash({"review": "PNP-C046", "memory": tm.snapshot_hash, "mapping": mapping.artifact_hash}),
    )
    return tm, review


def expert_review_document(context_hash: str) -> dict:
    roles = [
        ("domain_theory_lead", "Check the recursive quadrants and MAGIC-prefix arithmetic before claiming a global separation.", "A fixed leading bit constrains syntax but UNSAT remains irrelevant if support projections are already disjoint."),
        ("analogy_method_transfer_lead", "Retain partition-first transfer only under exact embedding preservation.", "A building-shaft analogy proposes search order but supplies no proof."),
        ("adversarial_falsification_lead", "Attack the base level, inherited embedding, fallback row zero, and any complement support in lower quadrants.", "One high-half old support row or low-half canonical prefix refutes the lemma."),
        ("formal_methods_lead", "Bind quantifiers n>=2, row domains, half thresholds, and the difference between words and UNSAT words.", "The evaluator must be inert before explicit authorization and cannot enumerate targets."),
        ("novelty_research_value_lead", "Treat the likely lemma as a local source-definition consequence.", "Value is pruning an impossible search, not novelty or P-versus-NP progress."),
    ]
    return _sealed({
        "schema_version": "1.0.0",
        "review_id": "PNP-C046-EXPERT-CONTEXT-REVIEW-20260812",
        "atom_id": ATOM,
        "context_hash": context_hash,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
        "role_reviews": [{"role": role, "objection": objection, "recommendation": recommendation} for role, objection, recommendation in roles],
        "disagreements": ["Whether the invariant is too elementary for research value; all roles agree it is the cheapest feasibility discriminator."],
        "strongest_objection": "The old row projection containment must include the seed and every inherited embedding; otherwise the family-wide no-target conclusion is invalid.",
        "unresolved_uncertainty": "No candidate proof or result exists at this stage.",
        "next_action_recommendation": "After all gates pass, freeze a high-half separation lemma and inert proof-obligation evaluator; do not scan target levels.",
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
            "event_id": f"O9d12a2a1b-C046-E{i:02d}", "atom_id": ATOM,
            "event_type": kind.value, "timestamp": f"2026-08-12T02:15:{i:02d}Z",
            "state_summary": "C046 asks whether a qualifying later canonical collision target exists; no target result, candidate, or evaluator has been accessed or executed.",
            "action_summary": kind.value, "evidence_pointers": [evidence_map[kind]],
            "alternatives_considered": ["scan U18,U19,...", "run target decoder", "prove family-wide feasibility invariant"],
            "decision_rationale": "The C045 collision criterion and frozen recursive definition make a partition-invariant feasibility test cheaper and safer than level scanning; SEARCH maps this exact obstruction to invariant-first analysis.",
            "outputs": outputs,
            "uncertainties": ["candidate theorem not yet frozen", "same-context review is not independent"],
            "residuals": ["finite least collision or family-wide nonexistence unresolved", "root OPEN"],
            "next_steps": ["only after gate PASS, freeze the high-half separation lemma candidate and inert evaluator", "do not access any later target result"],
            "previous_event_hash": previous,
        }
        artifact_hash = _hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **{**payload, "event_type": kind}))
        previous = artifact_hash
    return MathResearchTrace("PNP-O9d12a2a1b-C046-PRE-CANDIDATE-TRACE-20260812", tuple(entries))


def preservation_receipt() -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id="PNP-C046-ROOT-COORDINATE-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="explicit superlogarithmic full-cover family with circuit and P-versus-NP bridge",
        surrogate_coordinate="existence or nonexistence of a canonical prefix-row collision in one frozen family",
        bridge_edges=(
            BridgeEdge("C046-B1", "collision feasibility", "cover obstruction", "a collision is only a precondition for testing one coupling mechanism", EdgeProofStatus.UNPROVED, ("collision exists", "legal cover polarity")),
            BridgeEdge("C046-B2", "cover obstruction", "P versus NP", "requires uniform superlogarithmic lower bound and exact complexity bridge", EdgeProofStatus.UNPROVED, ("uniformity", "explicitness", "source theorem alignment")),
        ),
        obligations=(
            Obligation("C046-O1", "prove feasibility lemma", True, False),
            Obligation("C046-O2", "supply a cover lower-bound mechanism", True, False),
            Obligation("C046-O3", "discharge asymptotic and complexity bridge", True, False),
        ),
        known_disanalogies=("search pruning is not root progress", "nonexistence in one construction does not decide P versus NP"),
        source_authority=CoordinateAuthority.PROPOSAL_ONLY,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world="the desired collision is impossible in this family while a different family admits a useful lower-bound mechanism",
        registered_observations=(
            RegisteredStateObservation("C045-U17", "projection-disjoint", "no backward coupling by this mechanism"),
            RegisteredStateObservation("C046-pre", "feasibility-unresolved", "root open"),
        ),
        reverification_triggers=("recursive rule changes", "canonical prefix changes", "a new family is proposed"),
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
            objects=("frozen recursive complement support", "canonical prefix rows", "least collision level or NONE"),
            relations=("recursive support embedding", "fixed-prefix binary partition", "projection intersection"),
            domain="circuit complexity / recursive bipartite graph covers",
            goal_type="freeze a family-wide collision-feasibility lemma before any finite target access",
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
        "schema_version": "1.0.0", "atomization_id": "PNP-C046-ATOMIZATION-20260812",
        "recorded_at": "2026-08-12T02:14:59Z", "atom_id": ATOM,
        "parent_atom_id": "O9d12a2a1b-C045-RETROSPECTIVE",
        "object": "The set of later canonical UNSAT prefix rows and the accumulated nonempty complement row projection in the frozen one-sided recursion.",
        "qoi": "LEAST_CANONICAL_UNSAT_PREFIX_ROW_COLLISION_OR_NONE",
        "allowed_result_branches": ["FINITE_LEAST_COLLISION_LEVEL", "NO_COLLISION_IN_FROZEN_ONE_SIDED_FAMILY", "CANNOT_CHECK"],
        "atomic_obligations": ["prove old row-projection containment", "prove canonical-prefix containment", "compare the partition cells", "only if intersection is feasible select a least finite target"],
        "candidate_generation_allowed": False, "candidate_proposed": False,
        "target_result_accessed": False, "target_state": "TARGET_RESULT_UNACCESSED",
        "authority_boundary": {"assurance_only_zero_credit": True, "grants_cover_lower_bound": False, "grants_p_vs_np_authority": False},
    })
    tool_snapshot = _sealed({
        "schema_version": "1.0.0", "snapshot_id": "PNP-C046-TOOL-SNAPSHOT-20260812", "target_atom_id": ATOM,
        "application_base_commit": APPLICATION_BASE_SHA,
        "tools": [{"tool_id": "T-PNP-PARTITION-INVARIANT-FEASIBILITY-FIRST", "source": "C045 collision necessity lesson plus C041 recursive definition", "preconditions": ["unchanged recursion", "fixed leading-bit encoding"], "guarantees": ["search-order pruning after target-specific proof"], "non_guarantees": ["no theorem before proof", "no cover or root authority"]}],
        "target_state": "TARGET_RESULT_UNACCESSED", "mathematical_credit": False,
    })
    failure_snapshot = _sealed({
        "schema_version": "1.0.0", "snapshot_id": "PNP-C046-FAILURE-SNAPSHOT-20260812", "target_atom_id": ATOM,
        "failures": [
            {"failure_id": "F-C045-U17-PROJECTION-DISJOINT", "warning": "fresh columns cannot couple backward without old/new row-projection collision"},
            {"failure_id": "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING", "warning": "semantic type growth does not imply collision or cover growth"},
        ],
        "difference_witness": {"changed_question": "family-wide feasibility instead of another finite coupling claim", "restored_assumption": "none asserted; prove invariant before reuse", "cheapest_repeat_failure_test": "derive both binary-half containments"},
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
        "schema_version": "1.0.0", "receipt_id": "PNP-C046-PRE-CANDIDATE-GATE-20260812",
        "framework_commit": FRAMEWORK_SHA, "framework_version": "0.7.0", "application_base_commit": APPLICATION_BASE_SHA, "atom_id": ATOM,
        "full_document_integrity": integrity,
        "artifact_bindings": {"context_hash": fiber.packet_hash, "memory_review_hash": memory.artifact_hash, "transformation_memory_snapshot_hash": tm.snapshot_hash, "shortcut_review_hash": shortcut.artifact_hash, "trace_last_event_hash": research_trace.entries[-1].artifact_hash, "preservation_sha256": preservation.document()["receipt_canonical_sha256"], "full_document_integrity_hash": _hash(integrity)},
        "gate_verdicts": {"context": plan.context_gate.verdict.value, "dual_memory": plan.memory_gate.verdict.value, "obstruction_transformation": plan.shortcut_gate.verdict.value, "trace": plan.trace_gate.verdict.value, "preservation": plan.preservation_gate.verdict.value, "selected_mode": shortcut.selected_mode.value, "candidate_generation_allowed": plan.candidate_generation_allowed, "licensed_action": "FREEZE_HIGH_HALF_SEPARATION_LEMMA_CANDIDATE_ONLY"},
        "application_authority": {"licensed_actions": ["FREEZE_HIGH_HALF_SEPARATION_LEMMA_CANDIDATE_ONLY"], "candidate_construction_authorized": True, "target_evaluator_execution_authorized": False, "finite_target_scan_authorized": False},
        "result_capability_firewall": {"allowed": ["read frozen definitions and prior reviewed lessons", "freeze a mathematical partition lemma candidate and inert evaluator"], "forbidden": ["execute or import the target decoder", "enumerate any later target", "inspect result-signaling successor branches", "report a target witness/count/cover"], "breach_policy": "MARK_RETROSPECTIVE_AND_SELECT_A_DIFFERENT_UNTOUCHED_FAMILY"},
        "chronology": {"candidate_identity": None, "candidate_proposed": False, "target_result_accessed": False, "target_state": "TARGET_RESULT_UNACCESSED", "public_candidate_freeze": "PENDING_AFTER_CANDIDATE_COMMIT_AND_PR"},
        "authority": {"assurance_only": True, "mathematical_saturation_credit": False, "mathematical_result_credit": False, "grants_theorem_truth": False, "grants_novelty": False, "grants_independent_review": False, "grants_p_vs_np_authority": False},
    })
    documents["gate"] = gate
    return documents


if __name__ == "__main__":
    print(json.dumps(build_documents(), indent=2, sort_keys=True))
