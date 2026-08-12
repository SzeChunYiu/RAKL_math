"""Frozen pre-candidate packet for the NS-B2a1a2 moving-radius audit.

The inherited session already contained an informal escaping-bump direction.
Accordingly this packet claims no strict RAKL hypothesis-generation novelty.  It
licenses only a bounded mathematical validation of the fixed-radius-to-moving-
radius transfer.  It contains no bump parameters, candidate statement, or
observed outcome.
"""

from __future__ import annotations

from dataclasses import asdict, replace
from enum import Enum
import hashlib
import json
from pathlib import Path

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


ATOM = "NS-B2a1a2"
APPLICATION_BASE_SHA = "ac8c0745be8aed791a446fd55fcf5154cac01962"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
FROZEN_AT = "2026-08-12T08:00:00+00:00"
DOMAIN = "Navier-Stokes functional compactness calibration"

BASE = Path(__file__).resolve().parents[1]
PATHS = {
    "atomization": BASE / "02_problem_dag/NS_B2A1A2_DELTA_20260812.json",
    "context": BASE / "01_frontier/NS-B2a1a2_CONTEXT_FIBER_20260812.json",
    "memory": BASE / "07_memory/NS-B2a1a2_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": BASE / "07_memory/NS-B2a1a2_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": BASE / "08_reviews/NS-B2a1a2_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": BASE / "08_reviews/NS-B2a1a2_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "trace": BASE / "09_trace/NS-B2a1a2_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": BASE / "09_trace/NS-B2a1a2_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}


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


def _hash(payload: object) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _hashed_document(document: dict, field: str) -> dict:
    result = dict(document)
    result[field] = ""
    result[field] = _hash(result)
    return result


def build_context() -> MathContextFiber:
    fiber = MathContextFiber(
        atom_id=ATOM,
        object_context=(
            "Audit the exact inference from convergence on every fixed Euler-scaled "
            "cylinder plus scale-normalized smallness on radii a_k tending to infinity "
            "to moving-radius energy tightness in the logarithmic Type-II window."
        ),
        structural_coordinates=(
            "fixed-radius local strong convergence on each bounded cylinder",
            "moving radii a_k tending to infinity while lambda_k a_k tends to zero",
            "logarithmic window 1 << h_k << L_k and F_k=(L_k/h_k)^gamma tending to infinity",
            "scale-normalized kinetic energy A(v,a)=a^-1 sup_t integral_{B(a)} |v|^2",
            "absolute mass may scale like a_k/F_k^2 despite A(v_k,a_k) tending to zero",
            "unbounded spatial domain permits translation or annular escape",
            "vanishing viscosity and pressure remain separate PDE obligations",
            "root status OPEN_NO_SOLUTION_CERTIFICATE",
        ),
        equivalent_formulations=(
            "Quantifier form: local convergence for each fixed R does not control a radius R=a_k depending on k.",
            "Tightness form: identify the uniform tail modulus missing between local L2 convergence and moving-ball mass convergence.",
            "Calibration form: test whether smooth divergence-free fields can be invisible on each fixed compact while retaining mass in a moving annulus.",
        ),
        solved_analogues=(
            "Lions concentration-compactness separates local compactness from tightness and escape at infinity.",
            "For locally strongly L2-convergent sequences, global L2 mass convergence is equivalent to uniform tail tightness.",
        ),
        near_solved_analogues=(
            "NS-B1a2 scale-correct divergence-free packed snapshots show that critical normalization can hide unfavorable absolute mass scaling.",
            "NS-B2a1a1 identifies the exact logarithmic moving window but leaves rate-compatible compactness open.",
        ),
        method_transfers=(
            MethodTransfer(
                source_context="Concentration-compactness on an unbounded domain",
                method="Split local convergence from escape at infinity and require an explicit uniform tightness modulus before passing a global or moving-domain quantity.",
                shared_structure=(
                    "convergence is available on every fixed bounded region",
                    "the target integration region grows with the sequence index",
                    "mass can move outside every fixed observer",
                ),
                required_assumptions=(
                    "the local topology controls the target integrand on fixed balls",
                    "a separately uniform tail condition controls the complement",
                ),
                disanalogies=(
                    "the target sequence is intended to arise from a vanishing-viscosity PDE",
                    "generic compactness supplies no pressure, time, or Euler rigidity theorem",
                ),
                repair_question="What uniform moving-annulus modulus is necessary and sufficient for fixed-radius L2 convergence to determine the moving-ball kinetic mass?",
                source_anchors=(
                    "P.-L. Lions, Ann. IHP C 1 (1984), 109-145",
                    "research/real_math/millennium/navier_stokes/01_frontier/NS-B2a1a1_LOG_MESOSCOPIC_WINDOW_AUDIT_20260812.md",
                ),
            ),
            MethodTransfer(
                source_context="NS-B1a2 critical divergence-free blob packing calibration",
                method="Use explicitly scaled smooth divergence-free blobs to test whether a proposed functional implication is valid before importing PDE dynamics.",
                shared_structure=(
                    "scale-normalized quantities are weaker than absolute mass control",
                    "smooth divergence-free calibration fields preserve the kinematic constraint",
                    "the intended inference is functional before it is dynamical",
                ),
                required_assumptions=(
                    "the calibration is used only to refute an abstract compactness implication",
                    "no calibration field is represented as a Navier-Stokes or Euler solution",
                ),
                disanalogies=(
                    "NS-B1a2 packs shrinking Type-I blobs in a bounded region",
                    "the target concerns one mesoscopic profile escaping to infinity in Euler-scaled variables",
                ),
                repair_question="Can the moving-radius implication fail already within smooth divergence-free kinematic fields, and which additional condition exactly repairs it?",
                source_anchors=(
                    "research/real_math/millennium/navier_stokes/01_frontier/NS-B1a2_C001_CRITICAL_BLOB_PACKING_AUDIT_20260811.md",
                    "research/real_math/millennium/navier_stokes/07_memory/NS-B1a2_C001_FAILURE_EXPERIENCE_DELTA_20260811.json",
                ),
            ),
        ),
        explicit_disanalogies=(
            "A functional escaping-mass construction is not a Navier-Stokes counterexample.",
            "A tail-tightness criterion does not prove that Seregin's PDE sequence satisfies it.",
            "Control of kinetic mass does not automatically control pressure work or signed flux.",
            "The inherited informal candidate direction predates this packet, so strict discovery credit is unavailable.",
        ),
        source_anchors=(
            "G. Seregin, arXiv:2606.29468v1, equations (2.2), (2.7), (2.9), and fixed-a compactness after (2.9)",
            "research/real_math/millennium/navier_stokes/01_frontier/NS-B2a1a1_LOG_MESOSCOPIC_WINDOW_AUDIT_20260812.md",
            "research/real_math/millennium/navier_stokes/02_problem_dag/NS_B2A1A1_DELTA_20260812.json",
            f"RAKL@{FRAMEWORK_SHA}",
        ),
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(
            CrossDomainAnalogy(
                source_kind="distributed-systems monitoring",
                source_situation="Every fixed monitor eventually reports no load while a job migrates outward through an expanding cluster; fleet-wide accounting requires a uniform no-escape invariant.",
                common_abstraction=(
                    "pointwise-in-observer convergence",
                    "observer domain grows with time",
                    "workload may escape every fixed observer",
                ),
                source_to_target_mapping=(
                    "fixed monitor -> fixed spatial ball",
                    "migrating job -> moving annular kinetic mass",
                    "fleet-wide accounting -> moving-ball integral",
                ),
                shared_constraints=("fixed observers do not give uniform control over a growing domain",),
                disanalogies=(
                    "computational load is not a divergence-free vector field",
                    "the analogy supplies no mathematical or PDE authority",
                ),
                proposed_principle="Add a uniform no-escape/tightness condition before transferring fixed-observer convergence to a growing observation domain.",
                validation_obligation="Prove the target statement directly in L2 and falsify the unqualified transfer with an explicit divergence-free construction.",
                provenance_note="Cross-domain proposal generator only; all target authority must come from direct analysis.",
            ),
        ),
        analogy_scan_notes="Games and ordinary queue analogies were screened but retained only through the stronger monitoring abstraction above.",
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash="",
    )
    document = _document(fiber)
    document["packet_hash"] = _hash(document)
    return replace(fiber, packet_hash=document["packet_hash"])


def build_memory(context: MathContextFiber) -> ResearchMemoryReview:
    review = ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        tool_inventory_snapshot_hash="sha256:e392651dfa64976a1586a25fe709f37f2606914a0d3f043a5b0a2865834992f0",
        failure_lattice_snapshot_hash="sha256:4535ffd97ee4f2f89124375cd54960642cfae86ccd38ad392cff83c3a2839e29",
        tool_query_status=MemoryQueryStatus.NO_RELEVANT_MATCH,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "fixed-to-moving compactness transfer",
            "uniform-integrability and tail-tightness criterion",
            "smooth divergence-free escaping-mass calibration",
            "PDE-specific rate-compatible compactness",
        ),
        relevant_failure_ids=(
            "F-NS-B2a1a1-LOG-GAIN-MOVING-RADIUS-COMPACTNESS-MISMATCH",
            "F-NS-B2a1-DOUBLE-LIMIT-TAIL-INHERITANCE",
            "F-NS-B1a2-KINETIC-ENERGY-NONQUANTIZATION",
        ),
        selected_tool_ids=(),
        tool_applicability_notes=(
            "The scoped NS research-tool inventory is empty; no promoted tool can close the atom.",
        ),
        failure_reuse_notes=(
            "The parent mismatch makes the fixed-R versus R_k quantifier the direct target.",
            "The double-limit failure warns that a diagonal subsequence is not a uniform tail modulus.",
            "DifferenceWitness for NS-B1a2: its Type-I packed shrinking blobs differ from the Type-II moving-annulus setting, but its verified kinematic lesson that normalization can hide absolute mass is reusable only as calibration methodology.",
        ),
        unresolved_warnings=(
            "The inherited session supplied an informal escaping-bump direction before this freeze; strict context-first discovery credit is zero.",
            "No claim is made that source PDE solutions realize the calibration family.",
            "No governed exhaustive cross-problem coverage receipt was created.",
        ),
        evidence_pointers=(
            "research/real_math/millennium/navier_stokes/07_memory/NS_R001_RESEARCH_TOOL_INVENTORY_20260811.json",
            "research/real_math/millennium/navier_stokes/07_memory/NS-B2a1a1_EXPERIENCE_DELTA_20260812.json",
            "research/real_math/millennium/navier_stokes/07_memory/NS-B1a2_C001_FAILURE_EXPERIENCE_DELTA_20260811.json",
        ),
        artifact_hash="",
    )
    document = _document(review)
    document["artifact_hash"] = _hash(document)
    return replace(review, artifact_hash=document["artifact_hash"])


def build_transformation_packet(context: MathContextFiber, memory: ResearchMemoryReview):
    source_obstruction = ObstructionFingerprint(
        obstruction_id="O-NS-B1a2-NORMALIZED-BLOB-MASS-ESCAPE",
        domain=DOMAIN,
        roles=("approximating fields", "fixed bounded observers", "scale-dependent supports", "absolute mass"),
        relations=(
            "fixed bounded observers eventually miss scale-dependent supports",
            "scale-normalized control coexists with uncontrolled absolute mass",
        ),
        constraints=("unbounded spatial domain", "smooth divergence-free calibration", "no PDE-solution authority"),
        failure_mechanisms=("translation or scale escape to infinity", "normalization hides absolute mass"),
        invariants_to_preserve=("divergence-free kinematics", "exact scale normalization", "open root authority"),
        desired_transition=("separate fixed-radius convergence from moving-radius tightness",),
        forbidden_losses=("claiming a functional calibration is a PDE counterexample",),
    )
    episode = ObstructionTransformationEpisode(
        episode_id="OTEP-NS-B1a2-DIVERGENCE-FREE-SCALE-CALIBRATION",
        source_domain=DOMAIN,
        source_context="NS-B1a2 critical divergence-free blob packing audit",
        source_obstruction=source_obstruction,
        transformation_name="divergence_free_scale_calibration_then_tail_split",
        operation="Construct explicitly scaled divergence-free fields, compute normalized and absolute quantities separately, and isolate the missing tail condition.",
        preconditions=(
            "unbounded spatial domain",
            "target inference is functional before PDE dynamics",
            "calibration authority remains kinematic only",
        ),
        resulting_relations=("separate fixed-radius convergence from moving-radius tightness",),
        preserved_invariants=("divergence-free kinematics", "exact scale normalization", "open root authority"),
        relaxed_or_broken_constraints=(),
        known_breakpoints=(
            "PDE dynamics may forbid the calibration family",
            "pressure and time-regularity require separate verification",
        ),
        evidence_pointers=(
            "research/real_math/millennium/navier_stokes/01_frontier/NS-B1a2_C001_CRITICAL_BLOB_PACKING_AUDIT_20260811.md",
            "tests/math_applications/test_navier_b1a2_critical_blob_packing.py",
        ),
        authority=TransformationEpisodeAuthority.VERIFIED_LOCAL,
        artifact_hash="sha256:57c39805bbc2f7269589b541687b74d79e6d6a6386d936f9df338847cbe4db42",
    )
    transformation_memory = build_transformation_memory(
        memory_id="OTM-NS-B2a1a2-20260812",
        source_universe=(
            "same-domain NS functional calibration artifacts in the bounded application memory review",
            "generic concentration-compactness method transfer retained only as context",
        ),
        episodes=(episode,),
        evidence_pointers=(
            "research/real_math/millennium/navier_stokes/07_memory/NS-B2a1a2_RESEARCH_MEMORY_REVIEW_20260812.json",
            "research/real_math/millennium/navier_stokes/01_frontier/NS-B1a2_C001_CRITICAL_BLOB_PACKING_AUDIT_20260811.md",
        ),
    )

    target = ObstructionFingerprint(
        obstruction_id="O-NS-B2a1a2-FIXED-TO-MOVING-RADIUS",
        domain=DOMAIN,
        roles=("approximating fields", "fixed bounded observers", "moving integration balls", "absolute mass"),
        relations=(
            "fixed bounded observers eventually miss scale-dependent supports",
            "scale-normalized control coexists with uncontrolled absolute mass",
        ),
        constraints=("unbounded spatial domain", "smooth divergence-free calibration", "no PDE-solution authority"),
        failure_mechanisms=("translation or scale escape to infinity", "normalization hides absolute mass"),
        invariants_to_preserve=("divergence-free kinematics", "exact scale normalization", "open root authority"),
        desired_transition=("separate fixed-radius convergence from moving-radius tightness",),
        forbidden_losses=("claiming a functional calibration is a PDE counterexample",),
    )
    witness = StructuralMappingWitness(
        witness_id="SMW-NS-B2a1a2-B1a2-CALIBRATION",
        episode_id=episode.episode_id,
        target_obstruction_id=target.obstruction_id,
        role_mapping=(
            ("approximating fields", "approximating fields"),
            ("fixed bounded observers", "fixed bounded observers"),
            ("scale-dependent supports", "moving integration balls"),
            ("absolute mass", "absolute mass"),
        ),
        shared_relations=source_obstruction.relations,
        shared_constraints=source_obstruction.constraints,
        precondition_mapping=(
            ("unbounded spatial domain", "Euler-scaled space is R^3"),
            ("target inference is functional before PDE dynamics", "first test only the compactness implication"),
            ("calibration authority remains kinematic only", "forbid Navier-Stokes or Euler solution claims"),
        ),
        unmatched_source_preconditions=(),
        disanalogies=(
            "the source packs shrinking Type-I blobs while the target uses an expanding Type-II observation radius",
            "the target additionally audits a logarithmic F_k window and vanishing viscosity",
        ),
        target_validation_obligations=(
            "derive all moving-window exponents from exact definitions",
            "prove smoothness, divergence freedom, support geometry, local convergence, and mass identities",
            "state and prove a sharp uniform-tail repair condition",
            "reject every PDE-solution or root-authority escalation",
        ),
        evidence_pointers=(
            "research/real_math/millennium/navier_stokes/01_frontier/NS-B2a1a1_LOG_MESOSCOPIC_WINDOW_AUDIT_20260812.md",
            "research/real_math/millennium/navier_stokes/01_frontier/NS-B1a2_C001_CRITICAL_BLOB_PACKING_AUDIT_20260811.md",
        ),
        artifact_hash="sha256:bc4dbce251dd29020b01da77da20256d96256dfa4d2e39aedbcbb3144f3a76fb",
    )
    shortcut = ObstructionTransformationReview(
        review_id="OTR-NS-B2a1a2-20260812",
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        research_memory_review_hash=memory.artifact_hash,
        episode_memory_snapshot_hash=transformation_memory.snapshot_hash,
        obstruction=target,
        direct_search_status=RouteSearchStatus.MATCHES_FOUND,
        jump_search_status=RouteSearchStatus.NOT_RUN,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.SEARCH,
        direct_candidate_episode_ids=(episode.episode_id,),
        direct_mapping_witnesses=(witness,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=(
            "SEARCH chooses a validation pattern, not a theorem.",
            "The inherited informal construction direction predates this packet and earns no strict discovery credit.",
        ),
        evidence_pointers=(
            "research/real_math/millennium/navier_stokes/07_memory/NS-B2a1a2_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
            "research/real_math/millennium/navier_stokes/07_memory/NS-B2a1a2_RESEARCH_MEMORY_REVIEW_20260812.json",
        ),
        artifact_hash="",
    )
    document = _document(shortcut)
    document["artifact_hash"] = _hash(document)
    return transformation_memory, replace(shortcut, artifact_hash=document["artifact_hash"])


def build_expert_review(context: MathContextFiber) -> dict:
    return _hashed_document(
        {
            "review_id": "ECR-NS-B2a1a2-20260812",
            "atom_id": ATOM,
            "context_packet_hash": context.packet_hash,
            "roles": [
                {"role": "domain_theory_lead", "finding": "The parent supplies only fixed-a compactness; any calibration must preserve the source definition A=a^-1 sup integral and must not be called a PDE solution."},
                {"role": "analogy_method_transfer_lead", "finding": "Concentration-compactness suggests splitting local convergence from uniform tails; B1a2 supplies a same-domain kinematic construction pattern with a material scale disanalogy."},
                {"role": "adversarial_falsification_lead", "finding": "The cheapest discriminator is an escaping smooth divergence-free family whose support is missed by every fixed ball while a moving ball captures it."},
                {"role": "formal_methods_lead", "finding": "Freeze exact quantifiers, support inclusions, normalization identities, and an iff tail criterion; test polarity and false PDE-authority mutations."},
                {"role": "novelty_research_value_lead", "finding": "Escape at infinity is classical, so claim only a sharp source-interface calibration and no literature novelty; value lies in pruning the exact transfer."},
            ],
            "disagreements": [
                "The theory lead prefers proving the abstract tightness equivalence first; the falsification lead prefers constructing the hostile family first.",
                "No role claims that the functional obstruction is realized by Seregin's PDE sequence.",
            ],
            "strongest_objection": "A kinematic field can refute only the bare compactness inference, not a PDE-enhanced theorem whose hypotheses encode dynamics or pressure.",
            "unresolved_uncertainties": [
                "Whether source solutions possess a uniform moving-annulus modulus remains open.",
                "Whether a signed prelimit flux bypass can avoid moving-radius strong convergence remains open.",
            ],
            "recommendation": "After the runtime gate passes, validate one explicit smooth divergence-free escape construction and prove the exact uniform-tail repair criterion, with root authority fixed at none.",
            "same_context_not_independent_review": True,
            "frozen_at": "2026-08-12T08:02:00+00:00",
            "artifact_hash": "",
        },
        "artifact_hash",
    )


def _trace_entry(index: int, event_type: ResearchTraceEventType, previous: str, **fields) -> ResearchTraceEntry:
    entry = ResearchTraceEntry(
        event_id=f"NS-B2a1a2-E{index:02d}",
        atom_id=ATOM,
        event_type=event_type,
        timestamp=f"2026-08-12T08:{index:02d}:00+00:00",
        state_summary=fields.pop("state_summary"),
        action_summary=fields.pop("action_summary"),
        evidence_pointers=tuple(fields.pop("evidence_pointers")),
        previous_event_hash=previous,
        **fields,
    )
    document = _document(entry)
    document["artifact_hash"] = _hash(document)
    return replace(entry, artifact_hash=document["artifact_hash"])


def build_trace(context: MathContextFiber, memory: ResearchMemoryReview, shortcut: ObstructionTransformationReview, expert: dict) -> MathResearchTrace:
    specs = [
        (ResearchTraceEventType.ATOMIZED, dict(state_summary="Parent NS-B2a1a1 leaves rate-compatible mesoscopic compactness or tightness unresolved.", action_summary="Freeze child NS-B2a1a2 as the fixed-radius-to-moving-radius energy-transfer atom.", evidence_pointers=("research/real_math/millennium/navier_stokes/02_problem_dag/NS_B2A1A1_DELTA_20260812.json",), outputs=(ATOM,))),
        (ResearchTraceEventType.CONTEXT_FROZEN, dict(state_summary="The atom depends on fixed-versus-moving quantifiers, logarithmic normalization, and escape at infinity.", action_summary="Freeze structural coordinates, exact source definitions, analogues, disanalogies, and authority boundary.", evidence_pointers=(context.packet_hash,), outputs=(context.packet_hash,))),
        (ResearchTraceEventType.ANALOGY_SCAN, dict(state_summary="A cross-domain monitoring analogy survives only as a proposal generator.", action_summary="Map fixed observers, migrating load, and no-escape accounting to fixed balls, annular mass, and tightness.", evidence_pointers=(context.packet_hash,), outputs=("BRIDGES_RETAINED",), uncertainties=("The analogy supplies no mathematical authority.",))),
        (ResearchTraceEventType.METHOD_TRANSFER_REVIEW, dict(state_summary="Concentration-compactness and NS-B1a2 expose complementary local-tail and calibration methods.", action_summary="Record assumptions, disanalogies, and the minimal uniform-tail repair question.", evidence_pointers=(context.packet_hash,), outputs=("METHOD_TRANSFER_MATRIX_FROZEN",), uncertainties=("PDE dynamics may add structure absent from functional calibration.",))),
        (ResearchTraceEventType.EXPERT_CONTEXT_REVIEW, dict(state_summary="Five role-separated passes agree on a bounded functional discriminator and preserve the PDE objection.", action_summary="Freeze disagreements, strongest objection, uncertainty, and next-action recommendation.", evidence_pointers=(expert["artifact_hash"],), alternatives_considered=("abstract tightness lemma first", "hostile construction first", "direct PDE compactness theorem search"), decision_rationale="The construction and exact tail criterion jointly discriminate the bare transfer at minimal mathematical cost.", outputs=(expert["artifact_hash"],), uncertainties=tuple(expert["unresolved_uncertainties"]))),
        (ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW, dict(state_summary="The tool inventory has no match; three scoped failures warn about normalization and double limits.", action_summary="Freeze the dual success/failure memory review and DifferenceWitness.", evidence_pointers=(memory.artifact_hash,), alternatives_considered=("reuse a promoted compactness tool", "ignore prior kinematic calibrations"), decision_rationale="No promoted tool applies; prior failures constrain scope and prioritize an explicit tail falsifier.", outputs=(memory.artifact_hash,), uncertainties=tuple(memory.unresolved_warnings))),
        (ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW, dict(state_summary="A verified-local same-domain calibration episode is structurally mapped to the moving-radius obstruction.", action_summary="Select SEARCH and bind every source precondition, disanalogy, and target validation obligation.", evidence_pointers=(shortcut.artifact_hash,), alternatives_considered=("JUMP from generic concentration compactness", "GLUE partial episodes", "LIFT a new operator"), decision_rationale="The same-domain episode covers the desired transition and is fully mapped, so invention-last routing stops at SEARCH.", outputs=(shortcut.artifact_hash, "SEARCH"), uncertainties=tuple(shortcut.unresolved_warnings))),
        (ResearchTraceEventType.NEXT_STEP_PROPOSED, dict(state_summary="All pre-candidate context, memory, shortcut, and trace obligations are frozen.", action_summary="Propose only a bounded mathematical validation of the fixed-to-moving transfer, with exact normalization, hostile cases, and no PDE/root escalation.", evidence_pointers=(context.packet_hash, memory.artifact_hash, shortcut.artifact_hash), alternatives_considered=("attempt a source PDE theorem", "pursue signed flux bypass", "stop at the inherited qualitative warning"), decision_rationale="The bounded functional test can rigorously identify the missing assumption without pretending to solve the PDE residual.", outputs=("VALIDATION_ACTION_ONLY",), uncertainties=("Strict context-first discovery credit is zero because the inherited session anticipated the direction.",), next_steps=("Run the runtime gate; only after PASS freeze the exact validation candidate and executable falsifier.",))),
    ]
    entries = []
    previous = ""
    for index, (event_type, fields) in enumerate(specs):
        entry = _trace_entry(index, event_type, previous, **fields)
        entries.append(entry)
        previous = entry.artifact_hash
    return MathResearchTrace(trace_id="TRACE-NS-B2a1a2-20260812", entries=tuple(entries))


def build_plan():
    context = build_context()
    memory = build_memory(context)
    transformation_memory, shortcut = build_transformation_packet(context, memory)
    expert = build_expert_review(context)
    trace = build_trace(context, memory, shortcut, expert)
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("fixed-radius convergent field sequence", "moving radii", "scale-normalized kinetic energy", "absolute tail mass"),
            relations=("local convergence on every fixed ball", "moving ball grows with k", "normalization may hide absolute mass"),
            domain=DOMAIN,
            goal_type="validate or refute fixed-radius to moving-radius energy transfer",
        ),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=context,
        memory_review=memory,
        transformation_memory=transformation_memory,
        shortcut_review=shortcut,
        research_trace=trace,
    )
    return plan, context, memory, transformation_memory, shortcut, expert, trace


def build_documents() -> dict[str, dict]:
    plan, context, memory, transformation_memory, shortcut, expert, trace = build_plan()
    atomization = _hashed_document(
        {
            "atom_id": ATOM,
            "parent_atom_id": "NS-B2a1a1",
            "qoi": "FIXED_RADIUS_TO_MOVING_RADIUS_ENERGY_TRANSFER",
            "exact_obstruction": "Fixed-radius compactness has no k-uniform rate at a_k tending to infinity and supplies no absolute tail tightness.",
            "allowed_results": ["BARE_TRANSFER_REFUTED_SHARP_TIGHTNESS_CONDITION", "TRANSFER_PROVED_UNDER_SOURCE_HYPOTHESES", "CANNOT_CHECK"],
            "application_base_sha": APPLICATION_BASE_SHA,
            "framework_sha": FRAMEWORK_SHA,
            "candidate_identity": None,
            "candidate_proposed": False,
            "candidate_generation_allowed": False,
            "inherited_direction_preexisted_gate": True,
            "strict_discovery_credit": False,
            "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
            "authority": "PROPOSAL_SHADOW_ONLY",
            "artifact_hash": "",
        },
        "artifact_hash",
    )
    gate = _hashed_document(
        {
            "atom_id": ATOM,
            "application_base_sha": APPLICATION_BASE_SHA,
            "framework_sha": FRAMEWORK_SHA,
            "gate_verdicts": {
                "context": plan.context_gate.verdict.value,
                "memory": plan.memory_gate.verdict.value,
                "shortcut": plan.shortcut_gate.verdict.value,
                "trace": plan.trace_gate.verdict.value,
                "candidate_generation_allowed": plan.candidate_generation_allowed,
            },
            "licensed_action": "FREEZE_AND_VALIDATE_BOUNDED_FUNCTIONAL_TRANSFER_CANDIDATE_ONLY",
            "authority": {
                "mathematical_result_credit": False,
                "strict_discovery_credit": False,
                "navier_stokes_solution_authority": False,
                "root_authority": "NONE",
            },
            "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
            "artifact_hash": "",
        },
        "artifact_hash",
    )
    return {
        "atomization": atomization,
        "context": _document(context),
        "memory": _document(memory),
        "transformation_memory": _document(transformation_memory),
        "expert_review": expert,
        "shortcut_review": _document(shortcut),
        "trace": _document(trace),
        "gate": gate,
    }


def write_documents() -> None:
    for name, document in build_documents().items():
        path = PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_documents()
