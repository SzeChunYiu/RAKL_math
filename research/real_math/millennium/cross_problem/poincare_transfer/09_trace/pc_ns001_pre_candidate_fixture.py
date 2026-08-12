"""Strict source-success-to-open-problem pre-candidate packet.

The packet reconstructs a source-bound portion of Perelman's successful
Poincare program and licenses only a later falsifier of one proposed transfer
condition: sign-definite monotonicity of three-dimensional Navier--Stokes
enstrophy.  It contains no target vector field and executes no target algebra.
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


ATOM = "XM-PC-NS-001"
APPLICATION_BASE_SHA = "ec8a9eb5eeedaaf1d3f497a8688384256a2079e0"
FRAMEWORK_SHA = "43897d3afaf0038385102d5acc64793c05ec40f0"
FROZEN_AT = "2026-08-12T10:00:00Z"
BASE = "research/real_math/millennium/cross_problem/poincare_transfer"
PC_BASE = "research/real_math/millennium/poincare_conjecture"

PATHS = {
    "source_receipt": f"{PC_BASE}/00_sources/PC_SUCCESS_PRIMARY_SOURCE_RECEIPT_20260812.json",
    "success_chain": f"{PC_BASE}/01_frontier/PC_SUCCESS_TRANSFORMATION_CHAIN_20260812.json",
    "atomization": f"{BASE}/02_problem_dag/XM_PC_NS_001_ATOMIZATION_20260812.json",
    "context": f"{BASE}/01_frontier/XM_PC_NS_001_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/XM_PC_NS_001_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/XM_PC_NS_001_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/XM_PC_NS_001_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/XM_PC_NS_001_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/XM_PC_NS_001_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/XM_PC_NS_001_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": f"{BASE}/09_trace/XM_PC_NS_001_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": f"{BASE}/09_trace/XM_PC_NS_001_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": f"{BASE}/09_trace/XM_PC_NS_001_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
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


def source_receipt_document() -> dict:
    return _sealed({
        "schema_version": "1.0.0",
        "receipt_id": "PC-SUCCESS-PRIMARY-SOURCES-20260812",
        "retrieved_at": "2026-08-12T09:45:00Z",
        "sources": [
            {
                "source_id": "PERELMAN-I",
                "title": "The entropy formula for the Ricci flow and its geometric applications",
                "arxiv_id": "math/0211159v1",
                "url": "https://arxiv.org/pdf/math/0211159",
                "pdf_sha256": "945e278613c45ea1ab617b28c3095783d0e68958dc0546dfcfa9b42b9674fbe1",
                "bound_statements": [
                    "Equation (3.4): dW/dt is the integral of a squared tensor and is nonnegative under the coupled Ricci/conjugate-heat evolution.",
                    "Theorem 4.1: a smooth Ricci flow on a closed manifold at finite singular time is not locally collapsing.",
                    "Section 4.2 corollary: bounded-curvature blow-up sequences have complete ancient kappa-noncollapsed subsequential limits.",
                ],
            },
            {
                "source_id": "PERELMAN-II",
                "title": "Ricci flow with surgery on three-manifolds",
                "arxiv_id": "math/0303109v1",
                "url": "https://arxiv.org/pdf/math/0303109",
                "pdf_sha256": "6290421ec45e459a16a5ecad86d1162eecfed9f2c2646c7b2728f0503de8f706",
                "bound_statements": [
                    "Section 4.1 records pinching and canonical-neighborhood assumptions for the three-dimensional flow.",
                    "Sections 4.3-4.4 identify sufficiently thin horns by strong necks, cut middle two-spheres, cap, and continue the flow with discrete surgery times.",
                    "Section 5 proposition supplies time-dependent noncollapsing and canonical-neighborhood control for a global surgery solution.",
                ],
            },
            {
                "source_id": "PERELMAN-III",
                "title": "Finite extinction time for the solutions to the Ricci flow on certain three-manifolds",
                "arxiv_id": "math/0307245v1",
                "url": "https://arxiv.org/pdf/math/0307245",
                "pdf_sha256": "460606386f35a6b719970471a94452ecea7769e8c2caeff8820b8a483aebe0c6",
                "bound_statements": [
                    "Theorem 1.1: if a closed oriented three-manifold has no aspherical prime factors, every surgery flow becomes extinct in finite time.",
                    "Lemma 1.2 and Sections 1.3-1.4 use a least-area disk width with a one-sided differential inequality stable through surgery.",
                    "For a homotopy sphere the extinction argument, together with the surgery analysis, yields elliptization and hence the Poincare conclusion.",
                ],
            },
        ],
        "retrieval_command": "curl -L --fail https://arxiv.org/pdf/<id>; shasum -a 256",
        "authority": "PRIMARY_SOURCE_BINDING_FOR_SOURCE_SUCCESS_RECONSTRUCTION_ONLY",
        "non_guarantees": [
            "The receipt is not an independent reproof of Perelman's theorems.",
            "No Ricci-flow theorem transfers to Navier-Stokes without a target proof.",
        ],
    })


def success_chain_document(source_hash: str) -> dict:
    steps = [
        {
            "step_id": "PC-T1-ENTROPY",
            "obstruction": "singular rescaling may degenerate without a scale-aware control quantity",
            "transformation": "couple Ricci flow to the conjugate heat density and use Perelman's W/mu or reduced-volume monotonicity",
            "resulting_state": "a scale-sensitive monotone quantity whose defect is an integral square and whose collapse consequence can be tested",
            "enabling_assumptions": ["smooth Ricci flow before singular time", "closed source manifold for the stated mu theorem", "normalized positive conjugate-heat density", "Ricci-specific evolution identities"],
            "failure_modes": ["noncompact or surgery intervals require additional justification", "a monotone scalar alone does not classify high-curvature geometry"],
            "source": "PERELMAN-I eq. (3.4), Sections 6-7",
        },
        {
            "step_id": "PC-T2-NONCOLLAPSE",
            "obstruction": "bounded-curvature balls can collapse in normalized volume, destroying blow-up compactness",
            "transformation": "apply entropy/reduced-volume monotonicity to exclude local collapse",
            "resulting_state": "kappa-noncollapsed singularity models and complete ancient blow-up limits under the theorem's bounds",
            "enabling_assumptions": ["finite singular time", "closed initial manifold", "curvature bound on the tested ball", "Ricci-flow compactness hypotheses"],
            "failure_modes": ["no curvature bound means the stated ball test does not apply", "noncollapse does not itself identify a neck or permit surgery"],
            "source": "PERELMAN-I Theorem 4.1 and Section 4.2 corollary",
        },
        {
            "step_id": "PC-T3-CANONICAL-NEIGHBORHOODS",
            "obstruction": "arbitrary high-curvature geometry gives no controlled place to cut",
            "transformation": "classify high-curvature regions by canonical neighborhoods and locate strong delta-necks in horns",
            "resulting_state": "singular regions have controlled neck/cap models at the surgery scale",
            "enabling_assumptions": ["dimension three", "Hamilton-Ivey pinching", "kappa-noncollapse", "classification of relevant ancient kappa-solutions", "small epsilon and delta parameters"],
            "failure_modes": ["without canonical neighborhoods surgery has no exhaustive geometric interface", "higher dimensions admit different singular models"],
            "source": "PERELMAN-II Sections 1, 4.1 and 4.3",
        },
        {
            "step_id": "PC-T4-SURGERY-CONTINUATION",
            "obstruction": "the smooth evolution terminates at a singular time",
            "transformation": "cut controlled necks, discard prescribed components, glue standard caps, and restart with pinching preserved",
            "resulting_state": "a global Ricci flow with surgery whose surgery times are discrete on finite intervals",
            "enabling_assumptions": ["canonical-neighborhood theorem", "controlled surgery parameters", "cap construction preserving pinching", "noncollapse across the surgery construction"],
            "failure_modes": ["arbitrary deletion or capping can lose topology or estimates", "continuation alone does not force finite extinction"],
            "source": "PERELMAN-II Sections 4.4-5",
        },
        {
            "step_id": "PC-T5-FINITE-EXTINCTION",
            "obstruction": "a controlled global surgery flow could persist forever without the desired topological conclusion",
            "transformation": "use the least-area disk width and its surgery-stable differential inequality to force finite extinction",
            "resulting_state": "for manifolds with no aspherical prime factors, every such surgery flow becomes extinct in finite time; the homotopy-sphere case yields the Poincare conclusion",
            "enabling_assumptions": ["closed oriented three-manifold", "no aspherical prime factors", "nontrivial loop-space homotopy class", "surgery maps preserve the width inequality", "three-dimensional scalar-curvature evolution"],
            "failure_modes": ["aspherical prime factors are outside Theorem 1.1", "finite extinction is not a consequence of entropy monotonicity alone"],
            "source": "PERELMAN-III Theorem 1.1, Lemma 1.2, Sections 1.3-1.5",
        },
    ]
    return _sealed({
        "schema_version": "1.0.0",
        "chain_id": "PC-SUCCESS-CHAIN-ENTROPY-NONCOLLAPSE-SURGERY-EXTINCTION",
        "source_receipt_hash": source_hash,
        "object": "Perelman's successful three-dimensional Ricci-flow route to the Poincare conjecture",
        "transformation_chain": steps,
        "composition_obligations": [
            "T1 does not imply T3: noncollapse must be combined with three-dimensional singularity classification.",
            "T3 does not imply T5: controlled surgery continuation must be combined with the independent width/extinction inequality.",
            "Every topological conclusion is restricted to the source theorem's manifold hypotheses.",
        ],
        "success_lesson": "The reusable proposal-level pattern is not 'find a monotone quantity'; it is 'derive a source-specific monotone defect, prove degeneration control, classify bad regions, define a controlled restart, and add a terminal coercive quantity'.",
        "authority": "SOURCE_THEOREMS_PROOF_BACKED_IN_RICCI_FLOW_SCOPE_ONLY",
        "target_transfer_authority": "NONE",
    })


def context() -> MathContextFiber:
    transfer = MethodTransfer(
        source_context="Perelman's Ricci-flow success chain for closed three-manifolds",
        method="before importing the success pattern, isolate and test the first source-specific enabling identity: existence of a sign-definite monotone defect for the target evolution",
        shared_structure=(
            "both are nonlinear three-dimensional dissipative geometric/PDE evolutions",
            "both develop concentration scenarios analyzed by rescaling",
            "the target NS-B1a1 atom explicitly asks for a dimensionless monotone/no-recrossing scale-symmetry breaker",
        ),
        required_assumptions=(
            "the proposed target functional has an exact evolution identity",
            "the nonlinear production term has the sign needed for monotonicity or is dominated by dissipation",
            "the functional is tied to the target scale/compactness obstruction rather than merely finite on smooth data",
        ),
        disanalogies=(
            "Ricci W monotonicity is an identity coupled to a conjugate heat density; Navier-Stokes vortex stretching is not a squared Ricci-soliton defect",
            "Ricci surgery changes the manifold/metric at controlled necks; no analogous restart operation is authorized for a putative Navier-Stokes singularity",
            "Poincare finite extinction uses three-manifold topology and least-area disks absent from Navier-Stokes",
        ),
        repair_question="Is the unweighted three-dimensional Navier-Stokes enstrophy sign-monotone even instantaneously for all smooth divergence-free data, or can vortex stretching reverse the dissipative sign?",
        source_anchors=(PATHS["source_receipt"], PATHS["success_chain"], "research/real_math/millennium/navier_stokes/07_memory/NS-B1a1_C001_FAILURE_EXPERIENCE_DELTA_20260811.json"),
    )
    analogy = CrossDomainAnalogy(
        source_kind="controlled intervention / engineering fault handling",
        source_situation="A declining fault score is useful only if faults cannot hide in an unmeasured channel and every intervention has a verified restart and termination invariant.",
        common_abstraction=("monotone diagnostic", "degeneration control", "localized bad region", "controlled restart", "terminal coercivity"),
        source_to_target_mapping=("fault score -> PDE functional", "hidden channel -> sign-indefinite vortex stretching", "restart invariant -> post-singularity continuation obligation"),
        shared_constraints=("a scalar diagnostic alone cannot certify safe continuation", "unmeasured production can defeat monotonicity"),
        disanalogies=("engineered systems permit designed interventions", "the analogy supplies no PDE theorem"),
        proposed_principle="test the exact derivative identity before treating a successful source monotone as a transferable operation",
        validation_obligation="derive the Navier-Stokes enstrophy balance and give an exact smooth divergence-free counterexample if the derivative can be positive",
        provenance_note="proposal-only ordinary engineering analogy; no mathematical authority",
    )
    payload = {"atom": ATOM, "base": APPLICATION_BASE_SHA, "source": ["math/0211159", "math/0303109", "math/0307245"], "target": "NS-B1a1 enstrophy-monotonicity precondition"}
    return MathContextFiber(
        atom_id=ATOM,
        object_context="Cross-problem transfer atom: use the solved Poincare/Ricci-flow program as a parent success case, but test only whether its first enabling pattern--a sign-definite monotone defect--survives when the proposed target functional is three-dimensional Navier-Stokes enstrophy in the unresolved NS-B1a1 scale-symmetry-breaker lane.",
        structural_coordinates=("smooth periodic 3D incompressible Navier-Stokes before any singular time", "enstrophy one-half integral of vorticity squared", "exact competition between viscous dissipation and cubic vortex stretching", "instantaneous sign as the cheapest transfer discriminator", "NS-B1a1 remains a child of the open Clay regularity root"),
        equivalent_formulations=("sign of the enstrophy time derivative", "whether vortex stretching is always dominated by viscosity", "whether bare enstrophy can be the monotone component of a Perelman-shaped target chain"),
        solved_analogues=("Perelman W/mu and reduced-volume monotonicity under Ricci flow with the source-specific conjugate heat coupling",),
        near_solved_analogues=("two-dimensional Navier-Stokes enstrophy decay, where vortex stretching is absent", "NS-B1a1 retained dimensionless monotone/no-recrossing as an unresolved repair family"),
        method_transfers=(transfer,),
        explicit_disanalogies=transfer.disanalogies,
        source_anchors=transfer.source_anchors,
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(analogy,),
        analogy_scan_notes="A single guarded analogy survives only as a derivative-first falsification order. No surgery, extinction, or topology claim transfers.",
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash=_hash(payload),
    )


def memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {"atom": ATOM, "context": context_hash, "tools": ["T-XM-ROOT-BRIDGE-STABILITY-AUDIT"], "failures": ["F-NS-B1a1-SCALE-NEUTRAL-LOCAL-ENERGY-LEDGER"]}
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash="sha256:fa7c52385880128d6114b0d71f37f362dd382c1d91141e43497685b047c46a77",
        failure_lattice_snapshot_hash="sha256:62685017f70ca15ec3ebf096492d4fc4c329004578a6fd7baca360d74f53b528",
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=("copy a source monotone quantity by analogy", "derive and sign-test target enstrophy identity", "search directly for a new NS monotone", "import Ricci surgery semantics"),
        relevant_tool_ids=("T-XM-ROOT-BRIDGE-STABILITY-AUDIT",),
        relevant_failure_ids=("F-NS-B1a1-SCALE-NEUTRAL-LOCAL-ENERGY-LEDGER",),
        selected_tool_ids=("T-XM-ROOT-BRIDGE-STABILITY-AUDIT",),
        tool_applicability_notes=("Applicable only as a target-specific bridge falsifier: exact source success does not make enstrophy monotone.",),
        failure_reuse_notes=("The prior NS-B1a1 failure leaves a dimensionless monotone/no-recrossing repair open; it does not establish that bare enstrophy works.",),
        unresolved_warnings=("No Navier-Stokes candidate vector field has been frozen.", "Same-context review is not independent peer review.", "Any result is local to the enstrophy transfer condition and cannot close NS-B1a1 or the Clay root."),
        evidence_pointers=("research/real_math/millennium/cross_problem/07_memory/XM001_RESEARCH_TOOL_DELTA_20260811.json", "research/real_math/millennium/navier_stokes/07_memory/NS-B1a1_C001_FAILURE_EXPERIENCE_DELTA_20260811.json", PATHS["success_chain"]),
        artifact_hash=_hash(payload),
    )


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-XM-PC-NS-ENSTROPHY-SIGN",
        domain="mathematics / nonlinear PDE",
        roles=("dissipative evolution", "candidate monotone functional", "nonlinear production channel", "singular-scale obstruction"),
        relations=("functional derivative equals dissipative term plus nonlinear production", "source success requires sign-definite total defect", "target transfer fails if admissible data make production dominate"),
        constraints=("three dimensions", "smooth pre-singular regime", "smooth periodic divergence-free data", "positive viscosity", "instantaneous classical solution interval"),
        failure_mechanisms=("an uncontrolled production or collapse channel can invalidate scalar monotonicity as a singularity-control input",),
        invariants_to_preserve=("incompressibility", "periodicity and smoothness", "exact enstrophy identity", "open-root authority boundary"),
        desired_transition=("establish the candidate functional's sign-definite monotonicity before using it for singularity control",),
        forbidden_losses=("assuming away vortex stretching", "using two-dimensional dynamics", "claiming a Navier-Stokes solution", "treating computation as proof"),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    target = obstruction()
    source_obs = ObstructionFingerprint(
        obstruction_id="OBS-PC-SINGULAR-DEGENERATION",
        domain="three-dimensional Ricci flow",
        roles=("dissipative evolution", "candidate monotone functional", "nonlinear production channel", "singular-scale obstruction"),
        relations=("functional derivative equals dissipative term plus nonlinear production", "source success requires sign-definite total defect", "target transfer fails if admissible data make production dominate", "a coupled evolution identity makes the source functional derivative an integral square", "additional classification and intervention steps are separately required"),
        constraints=("three dimensions", "smooth pre-singular regime", "closed source manifold", "Ricci evolution", "normalized conjugate heat density", "source theorem hypotheses"),
        failure_mechanisms=("an uncontrolled production or collapse channel can invalidate scalar monotonicity as a singularity-control input",),
        invariants_to_preserve=("source theorem hypotheses", "scale normalization", "topological bookkeeping", "no target authority leakage"),
        desired_transition=("establish the candidate functional's sign-definite monotonicity before using it for singularity control",),
        forbidden_losses=("monotonicity-only proof narrative", "uncontrolled cutting", "dropping manifold hypotheses"),
    )
    episode = ObstructionTransformationEpisode(
        episode_id="E-PC-ENTROPY-NONCOLLAPSE-CANONICAL-SURGERY-EXTINCTION",
        source_domain="mathematics / geometric analysis",
        source_context="Perelman's proof-backed Poincare success chain",
        source_obstruction=source_obs,
        transformation_name="MONOTONE_DEFECT_THEN_DEGENERATION_CONTROL_THEN_CONTROLLED_RESTART_THEN_TERMINATION",
        operation="derive Ricci-specific entropy monotonicity; prove kappa-noncollapse; classify high-curvature canonical neighborhoods; perform controlled neck surgery; force finite extinction by a separate least-area width inequality",
        preconditions=("sign-definite source evolution identity", "quantitative noncollapse at singular scales", "exhaustive high-curvature classification", "controlled restart preserving estimates/topology", "terminal coercive width inequality"),
        resulting_relations=source_obs.desired_transition,
        preserved_invariants=source_obs.invariants_to_preserve,
        relaxed_or_broken_constraints=("smoothness is replaced by controlled surgery at discrete times",),
        known_breakpoints=("entropy monotonicity without noncollapse/classification", "surgery without canonical neighborhoods", "continuation without finite-extinction width", "target equations without analogous identities"),
        evidence_pointers=(PATHS["source_receipt"], PATHS["success_chain"]),
        authority=TransformationEpisodeAuthority.PROOF_BACKED,
        artifact_hash=_hash({"episode": "E-PC-ENTROPY-NONCOLLAPSE-CANONICAL-SURGERY-EXTINCTION", "sources": ["math/0211159", "math/0303109", "math/0307245"]}),
    )
    tm = build_transformation_memory(
        memory_id="XM-PC-NS-001-OBSTRUCTION-TRANSFORMATION-MEMORY-20260812",
        source_universe=("Perelman I math/0211159v1", "Perelman II math/0303109v1", "Perelman III math/0307245v1", "NS-B1a1 failure memory"),
        episodes=(episode,),
        evidence_pointers=(PATHS["source_receipt"], PATHS["success_chain"], "research/real_math/millennium/navier_stokes/07_memory/NS-B1a1_C001_FAILURE_EXPERIENCE_DELTA_20260811.json"),
    )
    mapping = StructuralMappingWitness(
        witness_id="MAP-PC-TO-NS-ENSTROPHY-PRECONDITION",
        episode_id=episode.episode_id,
        target_obstruction_id=target.obstruction_id,
        role_mapping=(("dissipative evolution", "dissipative evolution"), ("candidate monotone functional", "candidate monotone functional"), ("nonlinear production channel", "nonlinear production channel"), ("singular-scale obstruction", "singular-scale obstruction")),
        shared_relations=("functional derivative equals dissipative term plus nonlinear production", "source success requires sign-definite total defect", "target transfer fails if admissible data make production dominate"),
        shared_constraints=("three dimensions", "smooth pre-singular regime"),
        precondition_mapping=((episode.preconditions[0], "derive exact enstrophy identity and test its sign on frozen smooth divergence-free data"), (episode.preconditions[1], "not claimed; outside this first-condition falsifier"), (episode.preconditions[2], "not claimed; outside this first-condition falsifier"), (episode.preconditions[3], "not claimed; no Navier-Stokes surgery/restart is proposed"), (episode.preconditions[4], "not claimed; finite extinction has no target analogue here")),
        unmatched_source_preconditions=(),
        disanalogies=("Ricci entropy uses a coupled conjugate heat density; enstrophy has cubic vortex stretching", "Navier-Stokes has no authorized canonical-neighborhood surgery", "Poincare topology and least-area disks do not map to fluid regularity"),
        target_validation_obligations=("freeze one explicit smooth periodic divergence-free vector field before algebra execution", "derive the exact enstrophy derivative with stated torus normalization", "prove the sign by exact Fourier/trigonometric integration", "separate instantaneous no-transfer from any global-regularity claim"),
        evidence_pointers=(PATHS["success_chain"], "research/real_math/millennium/navier_stokes/01_frontier/NS-B1a1_CONTEXT_FIBER_20260811.json"),
        artifact_hash=_hash({"mapping": "MAP-PC-TO-NS-ENSTROPHY-PRECONDITION", "context": context_hash}),
    )
    review = ObstructionTransformationReview(
        review_id="XM-PC-NS-001-OBSTRUCTION-TRANSFORMATION-REVIEW-20260812",
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        research_memory_review_hash=memory_hash,
        episode_memory_snapshot_hash=tm.snapshot_hash,
        obstruction=target,
        direct_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        jump_search_status=RouteSearchStatus.MATCHES_FOUND,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.JUMP,
        jump_mapping_witnesses=(mapping,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=("JUMP licenses only a target precondition falsifier.", "The source theorem chain supplies no Navier-Stokes theorem authority.", "The root and NS-B1a1 remain open under every result branch."),
        evidence_pointers=(PATHS["context"], PATHS["memory"], PATHS["transformation_memory"]),
        artifact_hash=_hash({"review": "XM-PC-NS-001", "memory": tm.snapshot_hash, "mapping": mapping.artifact_hash}),
    )
    return tm, review


def expert_review_document(context_hash: str) -> dict:
    rows = [
        ("domain_theory_lead", "The 3D enstrophy identity includes vortex stretching; only an exact sign calculation can decide monotonicity.", "Test an explicit periodic divergence-free field and keep all constants and viscosity visible."),
        ("analogy_method_transfer_lead", "The source chain is composite; copying only the word monotone erases noncollapse, classification, surgery, and extinction preconditions.", "Transfer only the derivative-first falsification obligation."),
        ("adversarial_falsification_lead", "A cubic production term can dominate a quadratic viscous term after amplitude scaling if one base field has positive stretching integral.", "Freeze the field before evaluating the two exact integrals."),
        ("formal_methods_lead", "A symbolic or Fourier certificate must prove divergence-free and exact torus integrals; numerical quadrature is insufficient.", "Require exact rational multiples of pi^3 and an independently recomputed identity."),
        ("novelty_research_value_lead", "Nonmonotonic 3D enstrophy is classical; the value is a rigorously witnessed no-transfer lesson, not new mathematics.", "Make no novelty claim and preserve the narrow route-pruning scope."),
    ]
    return _sealed({
        "schema_version": "1.0.0",
        "review_id": "XM-PC-NS-001-EXPERT-CONTEXT-REVIEW-20260812",
        "atom_id": ATOM,
        "context_hash": context_hash,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
        "role_reviews": [{"role": r, "objection": o, "recommendation": x} for r, o, x in rows],
        "disagreements": ["The domain and novelty lenses expect a classical negative result; the transfer lens still values an exact falsifier because it blocks an invalid success-memory route."],
        "strongest_objection": "Even a positive instantaneous enstrophy derivative refutes only bare enstrophy monotonicity, not every possible Navier-Stokes monotone or no-recrossing mechanism.",
        "unresolved_uncertainty": "No target candidate field or integral result is present before the gate.",
        "next_action_recommendation": "After all gates pass, freeze one explicit divergence-free trigonometric field and a symbolic exact-integration evaluator; do not claim transfer beyond the sign condition.",
        "mathematical_result_credit": False,
        "independent_review_credit": 0,
    })


def trace(context_hash: str, memory_hash: str, shortcut_hash: str) -> MathResearchTrace:
    kinds = (ResearchTraceEventType.ATOMIZED, ResearchTraceEventType.CONTEXT_FROZEN, ResearchTraceEventType.ANALOGY_SCAN, ResearchTraceEventType.METHOD_TRANSFER_REVIEW, ResearchTraceEventType.EXPERT_CONTEXT_REVIEW, ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW, ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW, ResearchTraceEventType.NEXT_STEP_PROPOSED)
    evidence = {k: PATHS["context"] for k in kinds}
    evidence.update({ResearchTraceEventType.ATOMIZED: PATHS["atomization"], ResearchTraceEventType.EXPERT_CONTEXT_REVIEW: PATHS["expert_review"], ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW: PATHS["memory"], ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW: PATHS["shortcut_review"], ResearchTraceEventType.NEXT_STEP_PROPOSED: PATHS["gate"]})
    entries = []
    previous = ""
    for i, kind in enumerate(kinds, 1):
        outputs = ["PRE_CANDIDATE_ONLY", "TARGET_FIELD_NOT_FROZEN", "ROOT_OPEN"]
        if kind is ResearchTraceEventType.CONTEXT_FROZEN:
            outputs.insert(0, context_hash)
        if kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            outputs.insert(0, memory_hash)
        if kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            outputs[:0] = [shortcut_hash, "selected_mode:JUMP"]
        payload = {
            "event_id": f"XM-PC-NS-001-E{i:02d}", "atom_id": ATOM, "event_type": kind.value,
            "timestamp": f"2026-08-12T10:00:{i:02d}Z",
            "state_summary": "Perelman's success chain is source-bound; the active target asks only whether bare 3D Navier-Stokes enstrophy passes the first sign-definite monotonicity precondition.",
            "action_summary": kind.value, "evidence_pointers": [evidence[kind]],
            "alternatives_considered": ["copy the Ricci entropy narrative", "invent a new NS monotone", "test the enstrophy derivative sign first"],
            "decision_rationale": "The exact source chain shows monotonicity is necessary but not sufficient; JUMP therefore licenses the cheapest target-specific precondition falsifier before any larger transfer.",
            "outputs": outputs,
            "uncertainties": ["candidate field not yet frozen", "same-context review is not independent"],
            "residuals": ["enstrophy sign condition unresolved", "NS-B1a1 and Clay root open"],
            "next_steps": ["only after gate PASS, freeze one target field and exact symbolic evaluator", "preserve every result branch as local transfer evidence"],
            "previous_event_hash": previous,
        }
        artifact_hash = _hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **{**payload, "event_type": kind}))
        previous = artifact_hash
    return MathResearchTrace("XM-PC-NS-001-PRE-CANDIDATE-TRACE-20260812", tuple(entries))


def preservation_receipt() -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id="XM-PC-NS-001-ROOT-COORDINATE-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="a scale-critical monotone/no-recrossing or compactness mechanism sufficient to advance NS-B1a1 toward the Navier-Stokes regularity root",
        surrogate_coordinate="instantaneous monotonicity or nonmonotonicity of unweighted enstrophy on smooth periodic data",
        bridge_edges=(BridgeEdge("XM-PC-NS-B1", "enstrophy sign", "NS-B1a1 scale-symmetry breaker", "bare enstrophy would need scale-critical localization and recurrence control beyond an instantaneous sign", EdgeProofStatus.UNPROVED, ("exact enstrophy identity", "scale-critical relevance")), BridgeEdge("XM-PC-NS-B2", "NS-B1a1 scale-symmetry breaker", "Clay regularity root", "requires a complete blow-up exclusion or global regularity proof", EdgeProofStatus.UNPROVED, ("all Type-I and Type-II scenarios", "root proof DAG closure"))),
        obligations=(Obligation("XM-PC-NS-O1", "decide the instantaneous enstrophy sign condition", True, False), Obligation("XM-PC-NS-O2", "prove any surviving functional controls scale recurrence", True, False), Obligation("XM-PC-NS-O3", "close the Navier-Stokes root proof", True, False)),
        known_disanalogies=("Ricci entropy is not enstrophy", "Ricci surgery has no established Navier-Stokes analogue", "Poincare extinction is topological"),
        source_authority=CoordinateAuthority.ESTABLISHED,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world="smooth 3D Navier-Stokes data for which vortex stretching makes enstrophy increase at the initial time while the Ricci source identity remains valid in its own domain",
        registered_observations=(RegisteredStateObservation("PC-SOURCE", "source monotone identity", "Ricci degeneration control only with extra source theorems"), RegisteredStateObservation("NS-PRE", "target sign unresolved", "no NS-B1a1 or root consequence")),
        reverification_triggers=("functional changes", "target domain changes from 3D periodic NS", "a target scale-critical bridge is proved"),
        prior_failure_ids=("F-NS-B1a1-SCALE-NEUTRAL-LOCAL-ENERGY-LEDGER",),
    )


def build_current_gate_plan():
    fiber = context()
    memory = memory_review(fiber.packet_hash)
    tm, shortcut = transformation_memory_and_review(fiber.packet_hash, memory.artifact_hash)
    research_trace = trace(fiber.packet_hash, memory.artifact_hash, shortcut.artifact_hash)
    preservation = preservation_receipt()
    plan = plan_math_research(
        signature=ProblemSignature(objects=("Perelman success chain", "3D Navier-Stokes enstrophy", "vortex stretching"), relations=("source-success transfer", "exact evolution identity", "surrogate-to-root boundary"), domain="geometric analysis to nonlinear PDE transfer", goal_type="freeze a narrow no-transfer falsifier"),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=fiber, memory_review=memory, transformation_memory=tm, shortcut_review=shortcut, research_trace=research_trace,
        preservation_receipt=preservation, require_preservation_gate=True, expected_preservation_sha256=preservation.document()["receipt_canonical_sha256"],
    )
    return plan, fiber, memory, tm, shortcut, research_trace, preservation


def build_documents() -> dict[str, dict]:
    plan, fiber, memory, tm, shortcut, research_trace, preservation = build_current_gate_plan()
    source_receipt = source_receipt_document()
    success_chain = success_chain_document(source_receipt["artifact_hash"])
    atomization = _sealed({
        "schema_version": "1.0.0", "atomization_id": "XM-PC-NS-001-ATOMIZATION-20260812", "recorded_at": "2026-08-12T09:59:59Z", "atom_id": ATOM,
        "parent_success_case": "Poincare conjecture solved by Perelman's Ricci-flow program", "target_parent_atom": "NS-B1a1",
        "object": "The first enabling condition in a guarded transfer of the Poincare success chain: sign-definite monotonicity of a proposed target functional.",
        "qoi": "SIGN_OF_INITIAL_ENSTROPHY_DERIVATIVE_FOR_ONE_FROZEN_SMOOTH_3D_NS_FIELD",
        "allowed_result_branches": ["POSITIVE_DERIVATIVE_REFUTES_MONOTONICITY", "NONPOSITIVE_FOR_FROZEN_FIELD_ONLY", "CANNOT_CHECK"],
        "atomic_obligations": ["bind the source success chain", "derive the target enstrophy identity", "freeze a smooth divergence-free periodic field", "evaluate stretching and dissipation exactly", "preserve the open-root boundary"],
        "candidate_generation_allowed": False, "candidate_proposed": False, "target_field_frozen": False, "target_algebra_executed": False,
        "authority_boundary": {"source_success_is_established": True, "target_transfer_authority": "NONE", "grants_navier_stokes_progress": False, "grants_root_solution": False},
    })
    tool_snapshot = _sealed({"schema_version": "1.0.0", "snapshot_id": "XM-PC-NS-001-TOOL-SNAPSHOT-20260812", "target_atom_id": ATOM, "application_base_commit": APPLICATION_BASE_SHA, "tools": [{"tool_id": "T-XM-ROOT-BRIDGE-STABILITY-AUDIT", "authority": "VERIFIED_LOCAL", "applicability": "exact derivative-first falsification of a proposed source-to-target bridge", "non_guarantees": ["no source theorem transfer", "no root progress"]}], "poincare_research_tool_status": "NO_PROMOTION_SOURCE_CHAIN_ONLY"})
    failure_snapshot = _sealed({"schema_version": "1.0.0", "snapshot_id": "XM-PC-NS-001-FAILURE-SNAPSHOT-20260812", "target_atom_id": ATOM, "failures": [{"failure_id": "F-NS-B1a1-SCALE-NEUTRAL-LOCAL-ENERGY-LEDGER", "warning": "standard local-energy bookkeeping supplies no dimensionless monotone/no-recrossing rank"}], "difference_witness": {"changed_question": "test bare enstrophy rather than reuse the scale-neutral local-energy ledger", "restored_assumption": "none asserted; the sign condition is tested", "cheapest_repeat_failure_test": "exact initial enstrophy derivative on a frozen smooth field"}})
    expert = expert_review_document(fiber.packet_hash)
    documents = {"source_receipt": source_receipt, "success_chain": success_chain, "atomization": atomization, "context": _document(fiber), "tool_snapshot": tool_snapshot, "failure_snapshot": failure_snapshot, "memory": _document(memory), "transformation_memory": _document(tm), "expert_review": expert, "shortcut_review": _document(shortcut), "preservation": _jsonable(preservation.document()), "trace": _document(research_trace)}
    integrity = {"algorithm": "SHA-256", "canonicalization": "JSON_SORT_KEYS_COMPACT_UTF8", "scope": "FULL_PARSED_DOCUMENT", "inputs": {name: {"path": PATHS[name], "canonical_sha256": _hash(doc)} for name, doc in sorted(documents.items())}}
    gate = _sealed({
        "schema_version": "1.0.0", "receipt_id": "XM-PC-NS-001-PRE-CANDIDATE-GATE-20260812", "framework_commit": FRAMEWORK_SHA, "framework_version": "0.7.0", "application_base_commit": APPLICATION_BASE_SHA, "atom_id": ATOM,
        "full_document_integrity": integrity,
        "artifact_bindings": {"context_hash": fiber.packet_hash, "memory_review_hash": memory.artifact_hash, "transformation_memory_snapshot_hash": tm.snapshot_hash, "shortcut_review_hash": shortcut.artifact_hash, "trace_last_event_hash": research_trace.entries[-1].artifact_hash, "preservation_sha256": preservation.document()["receipt_canonical_sha256"]},
        "gate_verdicts": {"context": plan.context_gate.verdict.value, "dual_memory": plan.memory_gate.verdict.value, "obstruction_transformation": plan.shortcut_gate.verdict.value, "trace": plan.trace_gate.verdict.value, "preservation": plan.preservation_gate.verdict.value, "selected_mode": shortcut.selected_mode.value, "candidate_generation_allowed": plan.candidate_generation_allowed, "licensed_action": "FREEZE_ONE_EXPLICIT_3D_NS_ENSTROPHY_SIGN_FALSIFIER"},
        "chronology": {"source_chain_bound": True, "candidate_identity": None, "candidate_proposed": False, "target_field_frozen": False, "target_algebra_executed": False},
        "authority": {"source_success_authority": "PRIMARY_SOURCE_BOUND", "target_transfer_authority": "NONE", "mathematical_result_credit": False, "novelty_credit": False, "independent_review_credit": 0, "navier_stokes_root_status": "OPEN_NO_SOLUTION_CERTIFICATE"},
    })
    documents["gate"] = gate
    return documents


if __name__ == "__main__":
    print(json.dumps(build_documents(), indent=2, sort_keys=True))
