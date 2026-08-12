"""Strict RAKL-v3 pre-candidate packet for C048.

This fixture has no decoder, satisfiability, enumeration, or target-result
capability.  It may license only a target-blind lemma candidate about the
literal suffix-as-row transpose left open by C047.  All assurance work is zero
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

ATOM = "O9d12a2a1b-C048"
APPLICATION_BASE_SHA = "9e36dd83874bfc9f8ef94a2ce2708769cc25861e"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
FROZEN_AT = "2026-08-12T03:51:00Z"
DECODER_BLOB = "fcc4814dd618da96ef9bb8144a4783a0a6e886e1"
DECODER_RAW_SHA256 = "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"
C047_RESULT_BLOB = "850737df2b015378d8735a1ea03cfea27aefb3e1"
C047_FAILURE_BLOB = "fa4dd6c82481640391b81339a02b2eaa2afb06a6"

BASE = "research/real_math/millennium/p_vs_np"
PATHS = {
    "atomization": f"{BASE}/02_problem_dag/O9d12a2a1b_C048_ATOMIZATION_20260812.json",
    "context": f"{BASE}/01_frontier/O9d12a2a1b_C048_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/O9d12a2a1b_C048_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/O9d12a2a1b_C048_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/O9d12a2a1b_C048_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/O9d12a2a1b_C048_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/O9d12a2a1b_C048_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/O9d12a2a1b_C048_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": f"{BASE}/09_trace/O9d12a2a1b_C048_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": f"{BASE}/09_trace/O9d12a2a1b_C048_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": f"{BASE}/09_trace/O9d12a2a1b_C048_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
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
        source_context="interface feasibility under literal transposition of a recursively defined relation",
        method="transpose the exact ordered-pair interface, then test label-language congruence and reduction preservation before any target enumeration",
        shared_structure=(
            "relations are assembled from inherited and fresh blocks",
            "literal transposition places the decoded suffix, rather than the prefix, on the fresh row",
            "a fixed MAGIC header constrains canonical row labels",
            "the desired event requires exact label equality, not merely occupancy of the same binary half",
        ),
        required_assumptions=(
            "the C041 decoder and equal prefix/suffix split remain unchanged",
            "the candidate changes only (r,M+c) to its literal transpose (M+c,r)",
            "the seed and inherited old-old embedding remain unchanged",
        ),
        disanalogies=(
            "the suffix does not inherit the leading MAGIC header from the decoded word",
            "an exact row collision need not preserve the associated graph-language reduction",
            "literal-transpose feasibility does not determine quotient covers or lower bounds",
        ),
        repair_question="Can a literal suffix-as-row transpose attain exact canonical row-prefix congruence while retaining a correctly directed polynomial 3SAT reduction?",
        source_anchors=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/04_candidates/C041_fx_sat_one_sided.py@blob:{DECODER_BLOB}",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C047_ORIENTATION_FEASIBILITY_PROOF_CHECK_RESULT_20260812.json@blob:{C047_RESULT_BLOB}",
        ),
    )
    analogy = CrossDomainAnalogy(
        source_kind="engineering / addressing",
        source_situation="moving a cable into the correct rack does not connect it when the plug pinout remains shifted",
        common_abstraction=("coarse location repair", "fine label alignment", "exact connection requirement"),
        source_to_target_mapping=(
            "cable reversal -> ordered-pair transposition",
            "pinout -> suffix-to-row binary-label alignment",
            "electrical connection -> exact row-prefix collision",
        ),
        shared_constraints=("coarse placement is necessary but not sufficient", "success requires equality at the finer interface"),
        disanalogies=("rack wiring supplies no theorem authority", "binary strings require exact source-specific proof"),
        proposed_principle="after repairing a coarse partition obstruction, test fine interface congruence before enumerating outcomes",
        validation_obligation="derive the literal-transpose row language, test exact intersection with canonical current prefixes, and separately audit the endpoint-swapped 3SAT reduction",
        provenance_note="proposal-only engineering analogy; no mathematical authority",
    )
    payload = {
        "atom": ATOM,
        "base": APPLICATION_BASE_SHA,
        "coordinates": [
            "literal-transpose-only successor family with unchanged equal split and decoder",
            "a complement point (r,M+c) is replaced by (M+c,r)",
            "fresh-row label 2^(n-1)+c where c is the decoded suffix coordinate",
            "current canonical n-bit row prefix beginning with fixed MAGIC",
            "exact label collision rather than coarse high-half occupancy",
        ],
        "sources": [DECODER_BLOB, C047_RESULT_BLOB, C047_FAILURE_BLOB],
    }
    return MathContextFiber(
        atom_id=ATOM,
        object_context="Target-blind repair-feasibility atom: decide whether the literal transpose (r,M+c) -> (M+c,r), with the C041 equal split, decoder, seed, and inherited embedding fixed, can make a complement row equal a current canonical MAGIC prefix without losing a correctly directed 3SAT reduction.",
        structural_coordinates=tuple(payload["coordinates"]),
        equivalent_formulations=(
            "intersection of literal suffix-generated fresh rows with current canonical MAGIC-prefix rows",
            "membership of decoded suffix c in the tail language {s: 1||s is a canonical current prefix}",
            "feasibility of endpoint-swapped graph-language reduction before any target enumeration",
        ),
        solved_analogues=("C047 prefix-as-row mirror separation under exact binary-header comparison",),
        near_solved_analogues=("prefix-code synchronization and delimiter alignment under one-bit shifts",),
        method_transfers=(transfer,),
        explicit_disanalogies=(
            "coarse high-half occupancy does not imply exact row equality",
            "the all-zero contradiction and canonical MAGIC branch must both be classified",
            "prefix mirror, overlapping splits, and relabelled encodings are outside this atom",
            "a literal-transpose result is not a cover theorem, circuit lower bound, or P-versus-NP result",
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
    payload = {"atom": ATOM, "context": context_hash, "tools": ["T-PNP-C046-PARTITION-INVARIANT-FEASIBILITY-FIRST"], "failures": ["F-PNP-C047-ORIENTATION-ONLY-INTERFACE-MISALIGNMENT", "F-C045-U17-PROJECTION-DISJOINT"]}
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash=f"gitblob:{C047_RESULT_BLOB}",
        failure_lattice_snapshot_hash=f"gitblob:{C047_FAILURE_BLOB}",
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "literal transpose with suffix on the fresh row",
            "literal transpose plus original old-new block",
            "header-aligned coordinate relabelling",
            "unequal or overlapping split",
        ),
        relevant_tool_ids=("T-PNP-C046-PARTITION-INVARIANT-FEASIBILITY-FIRST",),
        relevant_failure_ids=("F-PNP-C047-ORIENTATION-ONLY-INTERFACE-MISALIGNMENT", "F-C045-U17-PROJECTION-DISJOINT"),
        selected_tool_ids=("T-PNP-C046-PARTITION-INVARIANT-FEASIBILITY-FIRST",),
        tool_applicability_notes=("C046's invariant-first operation is reusable only as a search-order heuristic: derive the exact suffix-as-row language and compare it with MAGIC prefixes before target enumeration.",),
        failure_reuse_notes=(
            "C047 proves prefix-as-row mirroring shifts MAGIC; C048 materially changes the coordinate to the suffix and must rerun exact interface congruence rather than reuse that conclusion.",
            "C045 warns that fresh columns alone cannot couple backward; even an exact row collision is only a precondition for a later interaction argument.",
        ),
        unresolved_warnings=(
            "No later target result has been accessed.",
            "No conclusion about literal-transpose feasibility is available until a candidate is publicly frozen and checked.",
            "Relabelled and split-changing variants are intentionally outside this atom.",
            "Same-context review is not independent peer review.",
        ),
        evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C047_ORIENTATION_FEASIBILITY_PROOF_CHECK_RESULT_20260812.json@blob:{C047_RESULT_BLOB}",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/O9d12a2a1b_C047_ORIENTATION_REPAIR_FAILURE_EXPERIENCE_DELTA_20260812.json@blob:{C047_FAILURE_BLOB}",
        ),
        artifact_hash=_hash(payload),
    )


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-PNP-C048-LITERAL-SUFFIX-ROW-TRANSPOSE-ROW-COLLISION-REPAIR",
        domain="mathematics",
        roles=("decoded prefixes", "decoded suffixes", "literal-transpose fresh rows", "canonical current prefixes", "graph-language reduction"),
        relations=(
            "literal transposition sends suffix c to fresh row 1||c and prefix r to old column r",
            "the decoder classifies non-tautological words into all-zero and MAGIC forms",
            "a collision requires exact binary equality between a generated row and a current canonical prefix",
        ),
        constraints=("unchanged decoder and equal split", "suffix coordinate becomes the semantic fresh row", "only literal transposition may change", "target results remain unaccessed"),
        failure_mechanisms=("a suffix need not carry MAGIC, and endpoint swapping may invalidate an unrevised reduction map",),
        invariants_to_preserve=("correctly directed polynomial 3SAT reduction", "canonical/fallback separation", "target blindness", "root authority boundary"),
        desired_transition=("decide whether literal transpose restores exact canonical row coupling while preserving the graph-language interface",),
        forbidden_losses=("target-result leakage", "silent decoder or label-map change", "promoting feasibility to root authority"),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    target = obstruction()
    source_obs = ObstructionFingerprint(
        obstruction_id="OBS-SOURCE-TRANSPOSE-BOTH-ENDPOINTS-THEN-AUDIT",
        domain="mathematics",
        roles=target.roles,
        relations=target.relations,
        constraints=target.constraints,
        failure_mechanisms=target.failure_mechanisms,
        invariants_to_preserve=target.invariants_to_preserve,
        desired_transition=target.desired_transition,
        forbidden_losses=target.forbidden_losses,
    )
    episode = ObstructionTransformationEpisode(
        episode_id="E-PNP-C048-LITERAL-TRANSPOSE-TWO-INTERFACE-AUDIT",
        source_domain="mathematics",
        source_context="C047 fine-interface failure plus the exact C041 ordered-pair decoder",
        source_obstruction=source_obs,
        transformation_name="LITERAL_TRANSPOSE_THEN_INTERFACE_AND_REDUCTION_AUDIT",
        operation="transpose the exact decoded ordered pair, then audit both suffix-row interface congruence and endpoint-swapped SAT-reduction faithfulness",
        preconditions=("recursive support clauses are exhaustive", "decoder output branches are exhaustive", "the transpose swaps both endpoints without relabelling", "the graph-language reduction is rewritten with the same endpoint swap"),
        resulting_relations=target.desired_transition,
        preserved_invariants=target.invariants_to_preserve,
        relaxed_or_broken_constraints=(),
        known_breakpoints=("the decoder changes", "the split becomes unequal or overlapping", "only one endpoint is moved", "the old reduction map is retained after transposition", "a coordinate relabelling is introduced"),
        evidence_pointers=(f"git:{APPLICATION_BASE_SHA}:{BASE}/04_candidates/C041_fx_sat_one_sided.py@blob:{DECODER_BLOB}",),
        authority=TransformationEpisodeAuthority.PROOF_BACKED,
        artifact_hash=_hash({"episode": "E-PNP-C048-LITERAL-TRANSPOSE-TWO-INTERFACE-AUDIT", "source": DECODER_BLOB}),
    )
    tm = build_transformation_memory(
        memory_id="PNP-C048-OBSTRUCTION-TRANSFORMATION-MEMORY-20260812",
        source_universe=("C041 frozen recursive definition", "C045 coupling failure", "C046 partition result", "C047 fine-interface result", "transpose of ordered relations"),
        episodes=(episode,),
        evidence_pointers=(episode.evidence_pointers[0], f"gitblob:{C047_RESULT_BLOB}"),
    )
    mapping = StructuralMappingWitness(
        witness_id="MAP-PNP-C048-LITERAL-TRANSPOSE-TWO-INTERFACES",
        episode_id=episode.episode_id,
        target_obstruction_id=target.obstruction_id,
        role_mapping=tuple((role, role) for role in source_obs.roles),
        shared_relations=target.relations,
        shared_constraints=target.constraints,
        precondition_mapping=(
            (episode.preconditions[0], "define the literal-transpose-only successor with no hidden quadrant"),
            (episode.preconditions[1], "classify all-zero, MAGIC canonical, and tautology fallback branches"),
            (episode.preconditions[2], "derive the exact fresh row 1||c and old column r from (r,M+c)"),
            (episode.preconditions[3], "audit formula x=r||c against the swapped query (M+c,r), not the old query"),
        ),
        unmatched_source_preconditions=(),
        disanalogies=("C047 put the prefix on the fresh row whereas C048 puts the suffix there", "a relation transpose changes ordered query semantics as well as occupancy", "no cover consequence follows"),
        target_validation_obligations=("derive every possible new high row without enumerating targets", "compare the suffix-row language with canonical current prefixes", "prove or refute the endpoint-swapped 3SAT reduction", "treat collision without reduction faithfulness as failure", "fail closed if decoder or coordinate placement differs"),
        evidence_pointers=(episode.evidence_pointers[0],),
        artifact_hash=_hash({"mapping": "MAP-PNP-C048-TRANSPOSE-INVARIANTS", "context": context_hash}),
    )
    review = ObstructionTransformationReview(
        review_id="PNP-C048-OBSTRUCTION-TRANSFORMATION-REVIEW-20260812",
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
        artifact_hash=_hash({"review": "PNP-C048", "memory": tm.snapshot_hash, "mapping": mapping.artifact_hash}),
    )
    return tm, review


def expert_review_document(context_hash: str) -> dict:
    roles = [
        ("domain_theory_lead", "A literal transpose swaps both endpoints: (r,M+c) becomes (M+c,r); it is not the C047 prefix mirror.", "Test suffix-row intersection and the endpoint-swapped graph-language reduction as separate necessary obligations."),
        ("analogy_method_transfer_lead", "Retain the cable reversal analogy only with an exact ordered-pair and bit-label mapping.", "The analogy proposes a two-interface audit but supplies no proof."),
        ("adversarial_falsification_lead", "A single label collision is insufficient if the swapped query no longer represents satisfiability.", "Treat collision with broken SAT/language equivalence as a failed repair, and attack all-zero, malformed, and canonical branches."),
        ("formal_methods_lead", "Bind the level convention, equal split, suffix coordinate, fresh leading bit, and both swapped endpoints.", "The evaluator must be inert before public freeze and must not import the decoder or enumerate later targets."),
        ("novelty_research_value_lead", "Treat any result as a scoped classification of literal transposition.", "Value is the exact collision/reduction transfer condition, not novelty or P-versus-NP progress."),
    ]
    return _sealed({
        "schema_version": "1.0.0",
        "review_id": "PNP-C048-EXPERT-CONTEXT-REVIEW-20260812",
        "atom_id": ATOM,
        "context_hash": context_hash,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
        "role_reviews": [{"role": role, "objection": objection, "recommendation": recommendation} for role, objection, recommendation in roles],
        "disagreements": ["Whether row-label intersection alone could count as feasibility; the domain, adversarial, and formal lenses require separately preserving both endpoint semantics and the SAT/language equivalence."],
        "strongest_objection": "A literal transpose that creates a row collision but retains the old ordered query map is not a faithful repair; both endpoints and the reduction map must transpose together.",
        "unresolved_uncertainty": "No candidate proof or result exists at this stage.",
        "next_action_recommendation": "After all gates pass, freeze one target-blind literal-transpose feasibility lemma with separate interface-collision and reduction-faithfulness obligations; do not scan target levels.",
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
            "event_id": f"O9d12a2a1b-C048-E{i:02d}", "atom_id": ATOM,
            "event_type": kind.value, "timestamp": f"2026-08-12T03:51:{i:02d}Z",
            "state_summary": "C048 asks whether literal suffix-as-row transposition can repair C047 while preserving both endpoint semantics and a correctly directed graph-language reduction; no candidate result, later target, or evaluator has been accessed or executed.",
            "action_summary": kind.value, "evidence_pointers": [evidence_map[kind]],
            "alternatives_considered": ["scan later finite targets", "use a relabelled suffix row", "change encoding or split", "test literal transpose with exact two-endpoint semantics"],
            "decision_rationale": "C047 excludes the prefix mirror and explicitly leaves literal transpose open; the selected SEARCH episode requires exact interface congruence and endpoint-swapped reduction faithfulness before any finite target search.",
            "outputs": outputs,
            "uncertainties": ["candidate theorem not yet frozen", "same-context review is not independent"],
            "residuals": ["literal-transpose collision feasibility unresolved", "endpoint-swapped reduction faithfulness unresolved", "relabelled/split-changing repairs outside scope", "root OPEN"],
            "next_steps": ["only after gate PASS, freeze the literal-transpose feasibility lemma candidate and inert evaluator", "do not access any later target result"],
            "previous_event_hash": previous,
        }
        artifact_hash = _hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **{**payload, "event_type": kind}))
        previous = artifact_hash
    return MathResearchTrace("PNP-O9d12a2a1b-C048-PRE-CANDIDATE-TRACE-20260812", tuple(entries))


def preservation_receipt() -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id="PNP-C048-ROOT-COORDINATE-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="explicit superlogarithmic full-cover family with circuit and P-versus-NP bridge",
        surrogate_coordinate="whether the literal suffix-as-row transpose has exact row-label congruence and a faithful endpoint-swapped SAT reduction",
        bridge_edges=(
            BridgeEdge("C048-B1", "literal-transpose repair feasibility", "cover obstruction", "exact row collision plus a faithful swapped reduction are only preconditions for testing one coupling mechanism", EdgeProofStatus.UNPROVED, ("collision exists", "both endpoint semantics preserved", "legal cover polarity")),
            BridgeEdge("C048-B2", "cover obstruction", "P versus NP", "requires uniform superlogarithmic lower bound and exact complexity bridge", EdgeProofStatus.UNPROVED, ("uniformity", "explicitness", "source theorem alignment")),
        ),
        obligations=(
            Obligation("C048-O1", "classify literal-transpose collision feasibility and reduction faithfulness", True, False),
            Obligation("C048-O2", "supply a cover lower-bound mechanism", True, False),
            Obligation("C048-O3", "discharge asymptotic and complexity bridge", True, False),
        ),
        known_disanalogies=("repair classification is not root progress", "collision alone is not reduction faithfulness", "failure of one transpose class does not decide P versus NP"),
        source_authority=CoordinateAuthority.PROPOSAL_ONLY,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world="literal transpose creates a row collision but the unrevised ordered query no longer represents satisfiability",
        registered_observations=(
            RegisteredStateObservation("C047", "prefix-mirror-interface-impossible", "literal transpose not yet classified"),
            RegisteredStateObservation("C048-pre", "literal-transpose-feasibility-unresolved", "root open"),
        ),
        reverification_triggers=("decoder changes", "split or row-coordinate changes", "only one endpoint is transposed", "the reduction map changes", "a new family is proposed"),
        prior_failure_ids=("F-PNP-C047-ORIENTATION-ONLY-INTERFACE-MISALIGNMENT", "F-C045-U17-PROJECTION-DISJOINT"),
    )


def build_current_gate_plan():
    fiber = context()
    memory = memory_review(fiber.packet_hash)
    tm, shortcut = transformation_memory_and_review(fiber.packet_hash, memory.artifact_hash)
    research_trace = trace(fiber.packet_hash, memory.artifact_hash, shortcut.artifact_hash)
    preservation = preservation_receipt()
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("literal-transpose successor support", "suffix-generated fresh rows", "canonical prefix rows", "endpoint-swapped SAT reduction"),
            relations=("ordered-pair transposition", "suffix-to-fresh-row binary map", "exact row-label intersection", "graph query equivalence"),
            domain="circuit complexity / recursive bipartite graph covers",
            goal_type="freeze a target-blind literal-transpose repair-feasibility lemma with separate collision and reduction-faithfulness obligations before any later target access",
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
        "schema_version": "1.0.0", "atomization_id": "PNP-C048-ATOMIZATION-20260812",
        "recorded_at": "2026-08-12T03:51:00Z", "atom_id": ATOM,
        "parent_atom_id": "O9d12a2a1b-C047",
        "object": "The equal-split C041 literal-transpose successor obtained by replacing each decoded complement point (r,M+c) with (M+c,r), with decoder, seed, and inherited embedding fixed.",
        "qoi": "LITERAL_SUFFIX_ROW_TRANSPOSE_INTERFACE_AND_REDUCTION_FEASIBILITY",
        "allowed_result_branches": ["COLLISION_AND_REDUCTION_FAITHFUL", "COLLISION_WITH_BROKEN_REDUCTION", "NO_EXACT_COLLISION", "CANNOT_CHECK"],
        "atomic_obligations": ["define the exact two-endpoint transpose", "derive the suffix-as-row label language", "compare exact labels with current MAGIC prefixes", "prove or refute the endpoint-swapped 3SAT reduction", "treat collision without language equivalence as failed repair"],
        "candidate_generation_allowed": False, "candidate_proposed": False,
        "target_result_accessed": False, "target_state": "TARGET_RESULT_UNACCESSED",
        "authority_boundary": {"assurance_only_zero_credit": True, "grants_cover_lower_bound": False, "grants_p_vs_np_authority": False},
    })
    tool_snapshot = _sealed({
        "schema_version": "1.0.0", "snapshot_id": "PNP-C048-TOOL-SNAPSHOT-20260812", "target_atom_id": ATOM,
        "application_base_commit": APPLICATION_BASE_SHA,
        "tools": [{"tool_id": "T-PNP-C046-PARTITION-INVARIANT-FEASIBILITY-FIRST", "source": "C046 high-half separation plus C041 recursive definition", "preconditions": ["exact target-specific coordinate map", "fixed decoder branches"], "guarantees": ["search-order pruning after target-specific proof"], "non_guarantees": ["worked once is not universal", "no theorem before proof", "no cover or root authority"]}],
        "target_state": "TARGET_RESULT_UNACCESSED", "mathematical_credit": False,
    })
    failure_snapshot = _sealed({
        "schema_version": "1.0.0", "snapshot_id": "PNP-C048-FAILURE-SNAPSHOT-20260812", "target_atom_id": ATOM,
        "failures": [
            {"failure_id": "F-PNP-C047-ORIENTATION-ONLY-INTERFACE-MISALIGNMENT", "warning": "coarse fresh-row occupancy does not imply exact binary interface congruence"},
            {"failure_id": "F-C045-U17-PROJECTION-DISJOINT", "warning": "fresh columns cannot couple backward without exact old/new row-projection collision"},
        ],
        "difference_witness": {"changed_question": "suffix-as-row literal transpose instead of C047 prefix-as-row mirror", "restored_assumption": "the tested row coordinate is now the decoded suffix; exact equality and reduction faithfulness remain unproved", "cheapest_repeat_failure_test": "derive 1||c exactly, compare with the canonical-prefix language, and audit x=r||c against query (M+c,r)"},
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
        "schema_version": "1.0.0", "receipt_id": "PNP-C048-PRE-CANDIDATE-GATE-20260812",
        "framework_commit": FRAMEWORK_SHA, "framework_version": "0.7.0", "application_base_commit": APPLICATION_BASE_SHA, "atom_id": ATOM,
        "full_document_integrity": integrity,
        "artifact_bindings": {"context_hash": fiber.packet_hash, "memory_review_hash": memory.artifact_hash, "transformation_memory_snapshot_hash": tm.snapshot_hash, "shortcut_review_hash": shortcut.artifact_hash, "trace_last_event_hash": research_trace.entries[-1].artifact_hash, "preservation_sha256": preservation.document()["receipt_canonical_sha256"], "full_document_integrity_hash": _hash(integrity)},
        "gate_verdicts": {"context": plan.context_gate.verdict.value, "dual_memory": plan.memory_gate.verdict.value, "obstruction_transformation": plan.shortcut_gate.verdict.value, "trace": plan.trace_gate.verdict.value, "preservation": plan.preservation_gate.verdict.value, "selected_mode": shortcut.selected_mode.value, "candidate_generation_allowed": plan.candidate_generation_allowed, "licensed_action": "FREEZE_LITERAL_SUFFIX_ROW_TRANSPOSE_FEASIBILITY_LEMMA_CANDIDATE_ONLY"},
        "application_authority": {"licensed_actions": ["FREEZE_LITERAL_SUFFIX_ROW_TRANSPOSE_FEASIBILITY_LEMMA_CANDIDATE_ONLY"], "candidate_construction_authorized": True, "target_evaluator_execution_authorized": False, "finite_target_scan_authorized": False},
        "result_capability_firewall": {"allowed": ["read frozen definitions and prior reviewed lessons", "freeze one literal-transpose lemma candidate with separate interface and reduction obligations plus an inert symbolic evaluator"], "forbidden": ["execute or import the target decoder", "enumerate any later target", "inspect result-signaling successor branches", "report a target witness/count/cover", "count a collision as success without graph-language equivalence", "change the split/encoding or relabel coordinates"], "breach_policy": "MARK_RETROSPECTIVE_AND_SELECT_A_DIFFERENT_UNTOUCHED_FAMILY"},
        "chronology": {"candidate_identity": None, "candidate_proposed": False, "target_result_accessed": False, "target_state": "TARGET_RESULT_UNACCESSED", "public_candidate_freeze": "PENDING_AFTER_CANDIDATE_COMMIT_AND_PR"},
        "authority": {"assurance_only": True, "mathematical_saturation_credit": False, "mathematical_result_credit": False, "grants_theorem_truth": False, "grants_novelty": False, "grants_independent_review": False, "grants_p_vs_np_authority": False},
    })
    documents["gate"] = gate
    return documents


if __name__ == "__main__":
    print(json.dumps(build_documents(), indent=2, sort_keys=True))
