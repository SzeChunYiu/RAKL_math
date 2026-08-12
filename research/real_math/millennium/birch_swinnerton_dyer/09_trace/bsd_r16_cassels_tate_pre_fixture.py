"""Freeze the BSD R16 Cassels--Tate divisor/radical discriminator.

This fixture deliberately stops before primary-source access and before any
mathematical result.  It binds the exact R15 slack term, dual experience
memory, an unresolved obstruction--transformation review, role-separated
same-context objections, and the only permitted source-audit result branches.
"""
from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path

from rakl.math_context import AnalogyScanStatus, CrossDomainAnalogy, MathContextFiber, MethodTransfer, audit_math_context_fiber
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview, audit_research_memory_review
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, audit_research_trace
from rakl.semantic_shortcut import (
    ObstructionFingerprint,
    ObstructionTransformationReview,
    RouteSearchStatus,
    ShortcutMode,
    build_transformation_memory,
    audit_obstruction_transformation_review,
)


ATOM = "BSD-A1a3-CASSELSTATEDIV-CORANK-GATE"
BASE = "research/real_math/millennium/birch_swinnerton_dyer"
APPLICATION_BASE_SHA = "b128515b4e6a25676fb36cfe2a72450e4ecccc50"
FRAMEWORK_SHA = "a6946c740b50413faf0eee218cc490dd6383e9ab"
FROZEN_AT = "2026-08-12T11:31:00Z"
PATHS = {
    "context": f"{BASE}/01_frontier/BSD_A1a3_R16_CASSELSTATE_CONTEXT_FIBER_20260812.json",
    "memory": f"{BASE}/07_memory/BSD_A1a3_R16_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/BSD_A1a3_R16_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "shortcut": f"{BASE}/07_memory/BSD_A1a3_R16_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "trace": f"{BASE}/09_trace/BSD_A1a3_R16_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": f"{BASE}/09_trace/BSD_A1a3_R16_SOURCE_DISCRIMINATOR_FREEZE_20260812.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def seal(value: dict) -> dict:
    out = dict(value)
    out["artifact_hash"] = ""
    out["artifact_hash"] = canonical_hash(out)
    return out


def jsonable(value: object) -> object:
    """Normalize dataclass tuples/enums exactly as persisted JSON sees them."""
    return json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))


def context_fiber() -> MathContextFiber:
    fiber = MathContextFiber(
        atom_id=ATOM,
        object_context=(
            "For one elliptic curve E/Q and prime p in the usual p-infinity Kummer Selmer structure, R15 gives "
            "corank Sel = rank E(Q) + corank Sha(E/Q)[p^infinity].  Test whether exact Cassels--Tate pairing "
            "structure constrains the maximal divisible Sha term strongly enough to remove this slack."
        ),
        structural_coordinates=(
            "same elliptic curve E/Q and prime p throughout",
            "D is the maximal divisible subgroup of Sha(E/Q)[p^infinity]",
            "the target quantity is corank_Zp D, not the order of a finite quotient",
            "pairing domain, codomain, radical, quotient and p=2 scope are load-bearing",
            "finite/nondegenerate alternating pairing consequences must not be transferred to D unless D survives the pairing",
        ),
        equivalent_formulations=(
            "R15 rank-two conclusion is equivalent to corank_Zp Sha(E/Q)[p^infinity]=0 after exact Selmer corank two",
            "for a cofinitely generated p-primary group, corank zero is equivalent here to finiteness",
            "the discriminator asks whether Cassels--Tate duality controls D itself or only Sha/D",
        ),
        solved_analogues=(
            "finite-dimensional symplectic vector spaces have even dimension under a nondegenerate alternating form",
        ),
        near_solved_analogues=(
            "R15 isolates D as the unique corank slack but supplies no pairing theorem",
        ),
        method_transfers=(
            MethodTransfer(
                source_context="R15 Kummer--Selmer corank decomposition",
                method="separate a global group into visible Mordell--Weil and hidden divisible Sha coordinates before applying structure theorems",
                shared_structure=("additive corank decomposition", "same E/Q and p", "one isolated slack coordinate"),
                required_assumptions=("usual Kummer Selmer exact sequence", "cofinite generation"),
                disanalogies=("R15 has no Cassels--Tate pairing statement", "a quotient pairing need not constrain its radical"),
                repair_question="On exactly which group is the source pairing nondegenerate, and is D retained, quotiented out, or assumed zero?",
                source_anchors=(f"git:{APPLICATION_BASE_SHA}:{BASE}/00_sources/BSD_A1a2_R15_KUMMER_SHA_EXACT_RANK_RESULT_20260812.json",),
            ),
        ),
        explicit_disanalogies=(
            "nondegenerate alternating form on a finite quotient is not a nondegenerate form on the full divisible group",
            "square order or even finite dimension is not zero corank",
            "assuming Sha finite would assume the target discriminator rather than prove it",
            "p=2 alternating/antisymmetric refinements cannot be imported from odd p without exact source scope",
        ),
        source_anchors=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/00_sources/BSD_A1a2_R15_KUMMER_SHA_EXACT_RANK_RESULT_20260812.json",
            "PRIMARY_SOURCE_PENDING_BY_DESIGN: exact Cassels--Tate theorem source is target-hidden until after this freeze",
        ),
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(
            CrossDomainAnalogy(
                source_kind="engineering",
                source_situation="a sensor is calibrated only after quotienting out a blind-mode subspace",
                common_abstraction=("measurement has a kernel", "nondegeneracy holds only after quotient by the kernel"),
                source_to_target_mapping=("blind mode -> divisible radical D", "calibrated quotient -> Sha/D", "sensor response -> pairing"),
                shared_constraints=("kernel elements are invisible", "quotient behavior cannot identify kernel size"),
                disanalogies=("engineering intuition supplies no arithmetic theorem", "Cassels--Tate hypotheses may alter the exact radical"),
                proposed_principle="audit the radical before using nondegeneracy to constrain a hidden component",
                validation_obligation="source-check the exact kernel/radical theorem and derive only its literal implication for corank D",
                provenance_note="proposal-only structural analogy generated before target-source access",
            ),
        ),
        analogy_scan_notes="Retained only as a proposal for the radical audit; it has zero theorem authority.",
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash="",
    )
    return replace(fiber, packet_hash=canonical_hash(asdict(fiber)))


def memory_review(context: MathContextFiber) -> ResearchMemoryReview:
    review = ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        tool_inventory_snapshot_hash=canonical_hash({"bounded_inventory": ["R12 coefficient binding", "R15 corank decomposition"]}),
        failure_lattice_snapshot_hash=canonical_hash({"bounded_failures": ["F-BSD-A1A1-R8-SOURCE-FAMILY-REIMPORTS-ARITHMETIC-ENTRY"]}),
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=("Cassels--Tate radical/quotient audit", "finite alternating-pairing parity transfer"),
        relevant_tool_ids=("LEM-BSD-R12-PINFINITY-VP-CORANK-DIM", "LEM-BSD-R15-KUMMER-SHA-CORANK-DECOMPOSITION"),
        relevant_failure_ids=("F-BSD-A1A1-R8-SOURCE-FAMILY-REIMPORTS-ARITHMETIC-ENTRY",),
        selected_tool_ids=("LEM-BSD-R15-KUMMER-SHA-CORANK-DECOMPOSITION",),
        tool_applicability_notes=("R15 exactly identifies the target slack term but does not constrain it.",),
        failure_reuse_notes=("Reject any pairing route that assumes finite Sha or exact rank as an enabling premise.",),
        unresolved_warnings=("No exact Cassels--Tate source theorem has been accessed in this result-blind freeze.",),
        evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/00_sources/BSD_A1a2_R15_KUMMER_SHA_EXACT_RANK_RESULT_20260812.json",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/BSD_A1a1_R8_SOURCE_FAMILY_FAILURE_SHADOW_20260812.json",
        ),
        artifact_hash="",
    )
    return replace(review, artifact_hash=canonical_hash(asdict(review)))


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="O-BSD-R16-DIVISIBLE-RADICAL-SLACK",
        domain="arithmetic_geometry",
        roles=("exact_selmer_corank", "mordell_weil_rank", "divisible_sha_slack", "pairing", "pairing_radical_or_quotient"),
        relations=("selmer_corank_equals_rank_plus_sha_corank", "pairing_structure_may_apply_only_after_quotient"),
        constraints=("same_E_Q_and_p", "no_Sha_finiteness_premise", "exact_pairing_hypotheses", "p_equals_2_scope_explicit"),
        failure_mechanisms=("radical_is_invisible_to_pairing", "finite_quotient_parity_misapplied_to_divisible_corank", "target_assumed_as_hypothesis"),
        invariants_to_preserve=("R15_exact_corank_identity", "same_curve_and_prime", "proof_direction", "root_remains_open"),
        desired_transition=("determine_exact_pairing_implication_for_corank_of_maximal_divisible_sha_subgroup",),
        forbidden_losses=("replace_D_by_Sha_mod_D", "assume_D_zero", "infer_zero_from_even_parity", "ignore_2_primary_scope"),
    )


def transformation_memory():
    return build_transformation_memory(
        memory_id="OTM-BSD-R16-PRE-SOURCE-20260812",
        source_universe=(
            f"RAKL_math@{APPLICATION_BASE_SHA}:merged BSD R12/R15 mathematical records only",
            "target Cassels--Tate primary sources intentionally unaccessed until discriminator freeze",
        ),
        episodes=(),
        evidence_pointers=(f"git:{APPLICATION_BASE_SHA}:{BASE}/00_sources/BSD_A1a2_R15_KUMMER_SHA_EXACT_RANK_RESULT_20260812.json",),
    )


def shortcut_review(context: MathContextFiber, review: ResearchMemoryReview, memory) -> ObstructionTransformationReview:
    core = ObstructionTransformationReview(
        review_id="OTR-BSD-R16-PRE-SOURCE-20260812",
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        research_memory_review_hash=review.artifact_hash,
        episode_memory_snapshot_hash=memory.snapshot_hash,
        obstruction=obstruction(),
        direct_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        jump_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        glue_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        selected_mode=ShortcutMode.CANNOT_CHECK,
        unresolved_warnings=("SEARCH cannot be selected until an exact source episode accounts for the pairing domain, radical, quotient and hypotheses.",),
        evidence_pointers=(PATHS["context"], PATHS["memory"], PATHS["transformation_memory"]),
        artifact_hash="",
    )
    return replace(core, artifact_hash=canonical_hash(asdict(core)))


def _trace_entry(previous: str, *, idx: int, kind: ResearchTraceEventType, state: str, action: str,
                 evidence: tuple[str, ...], alternatives: tuple[str, ...] = (), rationale: str = "",
                 outputs: tuple[str, ...] = (), uncertainties: tuple[str, ...] = (), next_steps: tuple[str, ...] = ()) -> ResearchTraceEntry:
    entry = ResearchTraceEntry(
        event_id=f"BSD-R16-E{idx:02d}", atom_id=ATOM, event_type=kind,
        timestamp=f"2026-08-12T11:{31 + idx:02d}:00Z", state_summary=state, action_summary=action,
        evidence_pointers=evidence, alternatives_considered=alternatives, decision_rationale=rationale,
        outputs=outputs, uncertainties=uncertainties, next_steps=next_steps,
        artifact_hash="", previous_event_hash=previous,
    )
    return replace(entry, artifact_hash=canonical_hash(asdict(entry)))


def trace(context: MathContextFiber, review: ResearchMemoryReview, shortcut: ObstructionTransformationReview) -> MathResearchTrace:
    entries: list[ResearchTraceEntry] = []
    specs = (
        (ResearchTraceEventType.ATOMIZED, "R15 leaves one exact corank slack D.", "Freeze D rather than full refined BSD glue.", ("R15",), (), "", (ATOM,), (), ()),
        (ResearchTraceEventType.CONTEXT_FROZEN, "Object/QoI/scope fixed.", "Freeze context fiber before target-source access.", (context.packet_hash,), (), "", (context.packet_hash,), (), ()),
        (ResearchTraceEventType.ANALOGY_SCAN, "Radical invisibility is the active morphology.", "Retain one kernel/quotient analogy as proposal only.", (PATHS["context"],), (), "", ("RADICAL_BEFORE_NONDEGENERACY",), (), ()),
        (ResearchTraceEventType.METHOD_TRANSFER_REVIEW, "R15 decomposition is applicable; finite symplectic parity is not yet transferable.", "Separate D from Sha/D.", (PATHS["context"],), (), "", ("PAIRING_DOMAIN_AUDIT_REQUIRED",), (), ()),
        (ResearchTraceEventType.EXPERT_CONTEXT_REVIEW, "Five role-separated same-context passes preserve the source boundary.", "Record strongest objections before source search.", (PATHS["context"],), ("infer D=0", "infer only parity", "pairing controls only quotient", "cannot check"), "The cheapest discriminator is the exact radical theorem, not another global BSD carrier.", ("domain lead: distinguish Sha, D, and Sha/D", "transfer lead: parity transfers only after domain alignment", "falsification lead: D may be the radical", "formal lead: quantify E,p and pairing hypotheses", "novelty lead: expect stored theorem, new value only from exact composition diagnosis"), ("Exact p=2 and finiteness hypotheses unresolved pending source access.",), ()),
        (ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW, "R15 selected; arithmetic-premise reimport failure retained.", "Freeze dual-memory query.", (review.artifact_hash,), ("R12 coefficient binding", "R15 exact decomposition", "R8 premise-reimport warning"), "R15 directly identifies D; R8 forbids assuming it away.", (review.artifact_hash,), ("No all-literature completeness claim.",), ()),
        (ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW, "No exact target-source episode is available before source access.", "Freeze CANNOT_CHECK shortcut review.", (shortcut.artifact_hash,), ("SEARCH", "JUMP", "GLUE", "LIFT", "CANNOT_CHECK"), "CANNOT_CHECK is mandatory until a source episode accounts for every pairing precondition and quotient.", (shortcut.artifact_hash,), ("Route is unresolved, not exhausted.",), ()),
        (ResearchTraceEventType.NEXT_STEP_PROPOSED, "Candidate generation remains forbidden; bounded source audit is allowed.", "Source-check the exact Cassels--Tate radical/quotient theorem against frozen branches.", (PATHS["gate"],), ("unbounded pairing survey", "assume finite Sha", "derive parity from analogy", "exact radical source audit"), "The radical theorem maximally discriminates the proposed repair at low cost.", ("SOURCE_AUDIT_ONLY_NO_CANDIDATE",), ("Source may split odd-p and 2-primary cases.",), ("After public persistence, inspect exact theorem statements and classify one predeclared branch.",)),
    )
    for idx, spec in enumerate(specs, 1):
        entries.append(_trace_entry(entries[-1].artifact_hash if entries else "", idx=idx, kind=spec[0], state=spec[1], action=spec[2], evidence=spec[3], alternatives=spec[4], rationale=spec[5], outputs=spec[6], uncertainties=spec[7], next_steps=spec[8]))
    return MathResearchTrace(trace_id="TRACE-BSD-R16-PRE-SOURCE-20260812", entries=tuple(entries))


def build_documents() -> dict[str, dict]:
    context = context_fiber()
    review = memory_review(context)
    memory = transformation_memory()
    shortcut = shortcut_review(context, review, memory)
    public_trace = trace(context, review, shortcut)
    context_report = audit_math_context_fiber(context)
    memory_report = audit_research_memory_review(review, atom_id=ATOM, context_hash=context.packet_hash)
    shortcut_report = audit_obstruction_transformation_review(shortcut, atom_id=ATOM, context_hash=context.packet_hash, research_memory_review_hash=review.artifact_hash, transformation_memory=memory)
    trace_report = audit_research_trace(public_trace)
    gate = seal({
        "record_type": "BSD_R16_RESULT_BLIND_SOURCE_DISCRIMINATOR_FREEZE",
        "cycle_id": "BSD-A1A3-CASSELSTATE-DIVISIBLE-CORANK-20260812-R16",
        "atom_id": ATOM,
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_main_sha": FRAMEWORK_SHA,
        "framework_drift_review": "29d3824..a6946c changes only publication/empirical research scaffolds, scoreboards and related tests; protected mathematical gate surfaces unchanged",
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        "target_access": {"cassels_tate_primary_source_accessed": False, "result_observed": False, "result_classified": False},
        "frozen_question": "Does the exact Cassels--Tate pairing theorem constrain corank_Zp D for the maximal divisible subgroup D of Sha(E/Q)[p^infinity], or does it become nondegenerate only after quotienting by D?",
        "source_audit_obligations": ["exact curve/field/polarization hypotheses", "pairing domain and codomain", "left and right kernels", "maximal divisible subgroup identification", "induced quotient pairing", "odd-p versus p=2 scope", "which consequences require finite Sha"],
        "allowed_result_branches": ["FORCES_ZERO_DIVISIBLE_CORANK", "PARITY_ONLY_ON_DIVISIBLE_CORANK", "PAIRING_DESCENDS_ONLY_TO_QUOTIENT_NO_DIVISIBLE_CORANK_CONTROL", "CANNOT_CHECK_EXACT_SOURCE_SCOPE"],
        "predeclared_falsifier": "The proposed pairing repair fails if the maximal divisible subgroup D lies in the pairing radical and nondegeneracy is asserted only on Sha/D; finite-quotient parity or square-order conclusions then cannot imply corank D=0.",
        "authority": {"candidate_generation_allowed": False, "source_audit_allowed_after_public_persistence": True, "mathematical_result_credit": False, "independent_review": False},
        "future_result_lesson_contract": {
            "current_status": "NO_RESULT_NO_LESSON",
            "required_seven_fields": ["attempted_mathematical_implication", "exact_mathematical_result_or_failure", "supported_and_competing_mathematical_causes", "scope", "mathematical_falsifier", "repair_or_next_discriminator", "proof_or_source_evidence"],
            "zero_math_credit": ["Git/branch/PR state", "CI/tests", "schemas/hashes/chronology", "telemetry/repository growth"],
        },
        "gate_reports": {"context": context_report.verdict.value, "memory": memory_report.verdict.value, "shortcut": shortcut_report.verdict.value, "trace_integrity": trace_report.verdict.value},
        "document_hashes": {"context": context.packet_hash, "memory": review.artifact_hash, "transformation_memory": memory.snapshot_hash, "shortcut": shortcut.artifact_hash, "trace_last_event": public_trace.entries[-1].artifact_hash},
    })
    return {
        "context": jsonable(asdict(context)), "memory": jsonable(asdict(review)),
        "transformation_memory": jsonable(asdict(memory)), "shortcut": jsonable(asdict(shortcut)),
        "trace": jsonable(asdict(public_trace)), "gate": gate,
    }


def write(root: Path = Path(".")) -> None:
    for key, value in build_documents().items():
        path = root / PATHS[key]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write()
