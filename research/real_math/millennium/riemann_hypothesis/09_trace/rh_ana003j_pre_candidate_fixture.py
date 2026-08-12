"""Strict pre-candidate packet for RH-ANA-003j.

This module freezes the quantifier mismatch between the proved fixed-``n``
natural-order Abel limit and any moving-endpoint or internal-prefix claim.  It
contains no target estimate, theorem candidate, or result evaluator.
"""
from __future__ import annotations

from dataclasses import asdict
from enum import Enum
import hashlib
import json
from pathlib import Path

from rakl.framework_candidate_freeze import (
    DiffPathClassification,
    DiffSurfaceClass,
    FrameworkSubjectFreezeBinding,
    FrameworkSubjectRevalidationObservation,
)
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
    TransformationEpisodeAuthority,
    build_transformation_memory,
)


ATOM = "RH-ANA-003j"
PARENT = "RH-ANA-003i"
APPLICATION_BASE_SHA = "b7ca6ac51fa8319b559e95402c47959c626f284a"
FRAMEWORK_PIN_SHA = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
FRAMEWORK_SEMANTICS_SHA = "2834760f4ae96684654a2080f5f36b24dc1d1ef7"
FRAMEWORK_CURRENT_SHA = "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
FROZEN_AT = "2026-08-12T10:18:00Z"
DISCRIMINATOR_FROZEN_AT = "2026-08-12T10:18:09Z"
PARAMETER_SCOPE = (
    "n is an integer >=1; Y is real >=2; C is one fixed real constant >0 inherited from the "
    "ANA-003i proposed cutoff (no sufficient value or threshold is proved); epsilon=(epsilon_n) "
    "is not frozen in this round and must be preregistered later with epsilon_n>0 before any result evaluation"
)
BASE = "research/real_math/millennium/riemann_hypothesis"

PATHS = {
    "source_packet": f"{BASE}/01_frontier/RH_ANA_003j_SOURCE_METHOD_TRANSFER_PACKET_20260812.json",
    "atomization": f"{BASE}/02_problem_dag/RH_ANA_003j_ATOMIZATION_20260812.json",
    "context": f"{BASE}/01_frontier/RH_ANA_003j_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/RH_ANA_003j_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/RH_ANA_003j_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/RH_ANA_003j_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/RH_ANA_003j_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/RH_ANA_003j_SEVEN_ROLE_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/RH_ANA_003j_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "quantifier_discriminator": f"{BASE}/08_reviews/RH_ANA_003j_QUANTIFIER_COMPATIBILITY_DISCRIMINATOR_20260812.json",
    "preservation": f"{BASE}/09_trace/RH_ANA_003j_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003j_PRE_CANDIDATE_TRACE_20260812.json",
    "framework_binding": f"{BASE}/09_trace/RH_ANA_003j_FRAMEWORK_SUBJECT_FREEZE_20260812.json",
    "framework_observation": f"{BASE}/09_trace/RH_ANA_003j_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "gate": f"{BASE}/09_trace/RH_ANA_003j_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}


def canonical_hash(value: object) -> str:
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


def seal(value: dict) -> dict:
    document = dict(value)
    document["artifact_hash"] = ""
    document["artifact_hash"] = canonical_hash(document)
    return document


def context() -> MathContextFiber:
    transfers = (
        MethodTransfer(
            source_context="fixed-index natural-order Abel convergence (merged C002)",
            method=(
                "for each fixed integer n, integrate the natural-order partial sum A(t) "
                "against the fixed-degree Laguerre weight and pass Y to infinity"
            ),
            shared_structure=(
                "the same coefficients x_{n,m}=((1-Lambda(m))/m)L_{n-1}^{(1)}(log m)",
                "the same natural integer order",
                "the same row limit S_n and remainder |S_n-R_n(Y)|",
            ),
            required_assumptions=(
                "n is fixed before Y tends to infinity",
                "the implied derivative and tail constants may depend on n",
                "summation remains in natural order",
            ),
            disanalogies=(
                "the target evaluates a different row at every n",
                "the target cutoff Y_n is fixed before any row-wise threshold is known",
                "C002 supplies neither a quantitative modulus nor constants controlled in n",
            ),
            repair_question=(
                "Can one prove a quantitative threshold M(n,epsilon) for the C002 remainder and show "
                "M(n,epsilon_n)<=Y_n eventually?"
            ),
            source_anchors=(
                f"git:{APPLICATION_BASE_SHA}:{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json",
                f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/RH_ANA_003_ABEL_001_C002_SCOPED_MATHEMATICAL_LESSON_20260812.json",
            ),
        ),
        MethodTransfer(
            source_context="uniform convergence and diagonal substitution for a doubly indexed family",
            method=(
                "replace bare row-wise convergence by either a threshold independent of n or a controlled "
                "n-dependent modulus whose growth is explicitly dominated by the proposed diagonal"
            ),
            shared_structure=(
                "row index n and approximation parameter Y are distinct quantifier axes",
                "a diagonal evaluation substitutes Y=Y_n into a two-parameter error family",
                "valid substitution requires the diagonal to lie inside each row's proved validity region",
            ),
            required_assumptions=(
                "a modulus is proved rather than inferred from Y_n tending to infinity",
                "all n-dependence of constants and thresholds is exposed",
                "the comparison M(n,epsilon_n)<=Y_n holds eventually",
            ),
            disanalogies=(
                "full uniform convergence in n is stronger than the minimal diagonal-compatible modulus needed here",
                "no common domination or n-uniform Laguerre remainder bound is currently bound",
                "an endpoint modulus does not control the maximum over all internal prefixes M<=Y_n",
            ),
            repair_question=(
                "Is there a diagonal-compatible quantitative modulus, possibly n-dependent, at the frozen "
                "epsilon_n and Y_n, and what constants or regimes does it require?"
            ),
            source_anchors=(
                "elementary uniform-convergence/diagonal-substitution theorem",
                "hostile triangular-array example e_n(Y)=1_{Y<=Y_n}, which is row-wise eventually zero but equals one on the diagonal",
            ),
        ),
        MethodTransfer(
            source_context="dominated convergence with a common integrable majorant",
            method=(
                "obtain a limit interchange or uniform tail bound from domination that is valid across the varying family"
            ),
            shared_structure=(
                "the C002 proof represents the row remainder by a boundary term plus a tail integral",
                "uniform endpoint control would follow from a majorant whose tail is controlled at Y_n",
            ),
            required_assumptions=(
                "a common or quantitatively n-controlled majorant",
                "uniform control of Laguerre degree growth and all implied constants",
                "a tail integral estimate evaluated at the proposed Y_n",
            ),
            disanalogies=(
                "the polynomial degree grows with n",
                "C002's constants C_n are allowed to grow without a registered bound",
                "Bellotti's fixed source estimate alone does not dominate the full varying Laguerre family",
            ),
            repair_question=(
                "Can the boundary and tail-integral terms be majorized with explicit n-dependence small at Y_n?"
            ),
            source_anchors=(
                "C002 Abel remainder representation",
                "Dunster-Gil-Segura uniform Laguerre asymptotic context, not a target remainder theorem",
            ),
        ),
    )
    analogies = (
        CrossDomainAnalogy(
            source_kind="engineering fleet stabilization",
            source_situation=(
                "Every machine eventually reaches tolerance after its own startup time, while an operator asks "
                "whether machine n is within tolerance at a fleet deadline assigned to that machine"
            ),
            common_abstraction=(
                "row-specific eventual behavior",
                "moving observation deadline",
                "unknown stabilization-time function",
                "diagonal compatibility",
            ),
            source_to_target_mapping=(
                "machine index -> n",
                "elapsed time -> Y",
                "machine-specific stabilization time -> M(n,epsilon)",
                "fleet deadline -> Y_n",
                "tolerance error -> |S_n-R_n(Y)|",
            ),
            shared_constraints=(
                "each individual object may eventually stabilize",
                "the observation deadline varies with the object",
                "a deadline claim needs comparison with the stabilization time",
            ),
            disanalogies=(
                "engineering stabilization may be measured empirically whereas the target needs a number-theoretic proof",
                "the analogy supplies no Laguerre bound, modulus, complement estimate, or Li implication",
            ),
            proposed_principle=(
                "do not replace object-wise eventuality by a moving-deadline guarantee without bounding the object-wise threshold"
            ),
            validation_obligation=(
                "derive M(n,epsilon_n) in the target arithmetic setting and prove M(n,epsilon_n)<=Y_n eventually"
            ),
            provenance_note="proposal-only ordinary/engineering analogy; zero theorem authority",
        ),
        CrossDomainAnalogy(
            source_kind="algorithmic per-input termination versus scheduled timeout",
            source_situation=(
                "An algorithm terminates on every fixed input, but input n may still exceed a prescribed timeout T_n "
                "unless its input-dependent running time is bounded relative to T_n"
            ),
            common_abstraction=(
                "pointwise existence",
                "input-dependent threshold",
                "moving resource schedule",
                "missing quantitative modulus",
            ),
            source_to_target_mapping=(
                "input -> row n",
                "runtime threshold -> M(n,epsilon_n)",
                "timeout -> Y_n",
                "successful termination -> endpoint error within epsilon_n",
            ),
            shared_constraints=(
                "pointwise existence permits arbitrarily poor dependence on the outer index",
                "the scheduled diagonal must dominate the hidden threshold",
            ),
            disanalogies=(
                "runtime is discrete and operational; the RH remainder is analytic",
                "the analogy cannot prove any arithmetic rate",
            ),
            proposed_principle="make hidden threshold dependence an explicit mathematical object before diagonal substitution",
            validation_obligation="produce and verify a target-domain modulus/diagonal comparison or reject the transfer",
            provenance_note="proposal-only algorithms analogy; zero theorem authority",
        ),
    )
    payload = {
        "atom": ATOM,
        "base": APPLICATION_BASE_SHA,
        "coordinates": [
            "x_{n,m}=((1-Lambda(m))/m)L_{n-1}^{(1)}(log m) in natural integer order",
            "R_n(Y)=sum_{2<=m<=Y}x_{n,m} and S_n=S_{2Lambda}(n)",
            "row-wise source: forall n forall epsilon>0 exists M(n,epsilon) forall Y>=M: |R_n(Y)-S_n|<epsilon",
            "diagonal target: exists N forall n>=N: |R_n(Y_n)-S_n|<=epsilon_n",
            "minimal bridge: exists a proved modulus M with exists N forall n>=N: M(n,epsilon_n)<=Y_n",
            "full n-uniform convergence is sufficient but stronger than the minimal diagonal-compatible bridge",
            "endpoint R_n(Y_n) is distinct from sup_{2<=M<=Y_n}|R_n(M)| or any internal-prefix family",
            "natural order is exact and regrouping/reordering is forbidden",
            "target/complement transfer and the Li/RH bridge remain separate obligations",
        ],
    }
    return MathContextFiber(
        atom_id=ATOM,
        object_context=(
            "The two-parameter natural-order error E(n,Y)=|S_n-R_n(Y)| for the actual "
            "von-Mangoldt/Laguerre array, the proved fixed-n limit Y->infinity, the moving cutoff "
            "Y_n=exp(C n^(5/3) log^2(n+e)), a future preregistered positive tolerance sequence epsilon_n, and the distinction "
            "between the endpoint M=Y_n and every internal prefix M<=Y_n."
        ),
        structural_coordinates=tuple(payload["coordinates"]),
        equivalent_formulations=(
            "row-wise convergence: forall n forall epsilon>0 exists M(n,epsilon) forall Y>=M: E(n,Y)<epsilon",
            "diagonal control: E(n,Y_n)<=epsilon_n eventually",
            "diagonal-compatible modulus: choose a valid M(n,epsilon) and prove M(n,epsilon_n)<=Y_n eventually",
            "full uniform convergence: forall epsilon>0 exists M(epsilon) forall n forall Y>=M: E(n,Y)<epsilon; sufficient but not required",
            "endpoint versus internal-prefix: E(n,Y_n) does not imply a bound on sup_{2<=M<=Y_n}|R_n(M)|",
        ),
        solved_analogues=(
            "uniform convergence permits substitution along every divergent diagonal",
            "a controlled n-dependent modulus permits substitution along a particular diagonal that dominates it",
        ),
        near_solved_analogues=(
            "dominated-convergence tail control under a common or quantitatively controlled majorant",
            "uniform asymptotics for growing-degree Laguerre polynomials with explicit validity regimes",
            "algorithmic per-input termination upgraded to a scheduled timeout only through a runtime bound",
            "hostile triangular-array construction proposed for the later discriminator, not evaluated in this round",
        ),
        method_transfers=transfers,
        explicit_disanalogies=(
            "fixed-n convergence does not control a moving diagonal",
            "Y_n->infinity does not imply Y_n exceeds an arbitrary n-dependent convergence threshold",
            "a diagonal-compatible modulus is weaker than full uniform convergence and should not be conflated with it",
            "endpoint control does not imply control of all internal prefixes",
            "outer-complement control does not imply internal-prefix control",
            "C002 allows n-dependent constants and supplies no moving-n rate",
            "natural-order convergence grants no reordering or regrouping authority",
            "a bound on S_n still does not complete the Li ledger or prove RH",
            "same-context expert roles provide zero independent-review credit",
        ),
        source_anchors=tuple(anchor for transfer in transfers for anchor in transfer.source_anchors),
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=analogies,
        analogy_scan_notes=(
            "Two structural analogies survive only as search-control proposals. Their shared lesson is threshold comparison, not theorem authority."
        ),
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash=canonical_hash(payload),
    )


FAILURES = (
    "F-RH-ANA-003e-MOVING-PREFIX-POLYBOUND-NOT-WEAKER",
    "F-RH-ANA-003f-STRICT-CUT-SUFFIX-GLUE",
    "F-RH-ANA-003f-PATH-WITNESS-NOT-ARITHMETIC",
    "F-RH-ANA-003g-COMPLEMENT-FIRST-WEAKENING-FAIL",
    "R9-STRICT-PREFIX-ARITHMETIC-ATTAINABILITY-OBSTRUCTION",
)


def memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {"atom": ATOM, "context": context_hash, "failures": FAILURES}
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash=f"git:{APPLICATION_BASE_SHA}:RH_C002_SCOPED_TOOL_SURFACE",
        failure_lattice_snapshot_hash=f"git:{APPLICATION_BASE_SHA}:RH_ANA003e_i_FAILURE_SURFACES",
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "fixed-n natural-order Abel convergence",
            "quantitative Abel remainder with explicit n-dependence",
            "uniform or diagonal-compatible convergence modulus",
            "common or n-controlled domination of the boundary and tail-integral terms",
            "endpoint-to-prefix maximal inequalities",
            "exact endpoint-plus-complement target transfer",
        ),
        relevant_tool_ids=("T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY",),
        relevant_failure_ids=FAILURES,
        selected_tool_ids=("T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY",),
        tool_applicability_notes=(
            "Applicable only to the inner statement obtained after fixing n: existence of the natural-order row limit and exact row remainder representation.",
            "Not applicable to any diagonal rate, n-uniform constant, internal-prefix maximum, Li positivity, or RH implication.",
            "The reusable mathematical operation is Abel tail representation at fixed degree, not software replay or receipt validation.",
        ),
        failure_reuse_notes=(
            "The moving-prefix failure warns that a growing cutoff alone cannot repair missing n-dependence.",
            "The suffix-glue failure keeps endpoint, complement, and internal-prefix obligations separate.",
            "The ambient-path failure forbids replacing the arithmetic array by freely chosen rows.",
            "The complement-first failure forbids treating outer control as internal-prefix control.",
            "The R9 attainability obstruction remains a warning for any later strict-prefix route.",
        ),
        unresolved_warnings=(
            "No quantitative modulus M(n,epsilon) has been proved for the C002 remainder.",
            "No comparison M(n,epsilon_n)<=Y_n has been proved.",
            "No endpoint-to-all-prefix maximal estimate has been proved.",
            "SEARCH has a direct uniform-modulus transformation but its target preconditions are unmet.",
            "JUMP and GLUE remain unexhausted; LIFT is forbidden.",
        ),
        evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/01_frontier/RH_ANA_003i_MATH_CONTEXT_FIBER_20260812.json",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/RH_ANA_003i_RESEARCH_MEMORY_REVIEW_20260812.json",
        ),
        artifact_hash=canonical_hash(payload),
    )

def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-RH-ANA-003j-POINTWISE-DIAGONAL-QUANTIFIERS",
        domain="analytic number theory / uniform asymptotics / quantifier logic",
        roles=(
            "fixed row index n",
            "tail parameter Y",
            "row-wise threshold M(n,epsilon)",
            "moving cutoff Y_n",
            "tolerance epsilon_n",
            "endpoint R_n(Y_n)",
            "internal prefixes R_n(M) for M<=Y_n",
            "target S_n and exact endpoint complement",
        ),
        relations=(
            "C002 first fixes n and only then lets Y tend to infinity",
            "row-wise convergence permits the threshold to depend arbitrarily on n and epsilon",
            "diagonal substitution evaluates row n at Y=Y_n",
            "endpoint transfer requires Y_n to dominate a proved threshold at epsilon_n eventually",
            "all-prefix control requires a separate maximal estimate over M<=Y_n",
            "endpoint-to-target transfer requires the exact complement at the same n and cutoff",
        ),
        constraints=(
            "exact Coffey normalization",
            "natural integer order without regrouping",
            "C is fixed with C>0 and Y_n=exp(C n^(5/3) log^2(n+e)) is frozen as a proposed diagonal, not proved sufficient",
            "epsilon_n is a symbolic positive tolerance and is not frozen until a later candidate/result round preregisters its exact sequence",
            "no unregistered uniform constants",
            "no target evaluation in this round",
        ),
        failure_mechanisms=(
            "interchanging forall n with the asymptotic threshold without a modulus",
            "inferring diagonal validity only from Y_n tending to infinity",
            "hiding n-dependence in Abel or Laguerre constants",
            "promoting endpoint control to all-prefix control",
            "using complement control as internal-prefix control",
        ),
        invariants_to_preserve=(
            "exact x_{n,m}, R_n, S_n, and Y_n definitions plus the explicit not-yet-frozen epsilon_n scope",
            "natural order",
            "fixed-n versus moving-n quantifier distinction",
            "endpoint versus internal-prefix distinction",
            "source authority and OPEN_NO_SOLUTION_CERTIFICATE",
        ),
        desired_transition=(
            "replace bare pointwise convergence by a proved quantitative modulus whose n-dependence is explicit and whose threshold is eventually dominated by Y_n at epsilon_n"
        ,),
        forbidden_losses=(
            "silent quantifier exchange",
            "unproved uniform constants",
            "reordering or regrouping",
            "endpoint-to-prefix promotion",
            "complement-to-internal promotion",
            "process receipt promoted to mathematical evidence",
            "LIFT without bounded SEARCH/JUMP/GLUE exhaustion",
        ),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    target = obstruction()
    episodes = (
        ObstructionTransformationEpisode(
            episode_id="E-ANALYSIS-POINTWISE-TO-DIAGONAL-BY-MODULUS",
            source_domain="real analysis / uniform convergence",
            source_context="doubly indexed error family with row-wise limits",
            source_obstruction=target,
            transformation_name="EXPOSE_MODULUS_AND_COMPARE_DIAGONAL",
            operation=(
                "choose a proved threshold M(n,epsilon) for every row and verify that the proposed "
                "diagonal satisfies M(n,epsilon_n)<=Y_n eventually"
            ),
            preconditions=(
                "the source and target use the same two-parameter error family",
                "M(n,epsilon) is derived with every n-dependent constant explicit",
                "the exact positive sequence epsilon_n is preregistered before evaluation and the eventual comparison is proved for that sequence and Y_n",
            ),
            resulting_relations=(
                "the moving diagonal lies in the row-wise validity region",
                "E(n,Y_n)<epsilon_n eventually",
            ),
            preserved_invariants=target.invariants_to_preserve,
            relaxed_or_broken_constraints=(),
            known_breakpoints=(
                "bare pointwise convergence supplies no growth bound for M",
                "full uniform convergence is not necessary but an uncontrolled row-wise threshold is insufficient",
                "the transformation grants endpoint control only",
            ),
            evidence_pointers=(PATHS["context"], PATHS["source_packet"]),
            authority=TransformationEpisodeAuthority.PROPOSAL_ONLY,
            artifact_hash=canonical_hash({"episode": "pointwise-diagonal-modulus"}),
        ),
        ObstructionTransformationEpisode(
            episode_id="E-ANALYSIS-DOMINATION-TO-UNIFORM-TAIL",
            source_domain="measure theory / asymptotic analysis",
            source_context="family of tail integrals controlled by a common or quantitative majorant",
            source_obstruction=target,
            transformation_name="DOMINATE_BOUNDARY_AND_TAIL_UNIFORMLY",
            operation=(
                "bound the Abel boundary and tail-integral representation by an explicit family whose tail at Y_n is at most epsilon_n"
            ),
            preconditions=(
                "a common or n-controlled majorant exists",
                "Laguerre degree growth and all constants are explicit",
                "the majorant tail estimate is valid at the frozen moving cutoff",
            ),
            resulting_relations=("a quantitative endpoint modulus follows from the majorant",),
            preserved_invariants=target.invariants_to_preserve,
            relaxed_or_broken_constraints=(),
            known_breakpoints=(
                "C002 has constants C_n without a registered growth bound",
                "the polynomial degree grows with n",
                "no target majorant has been proved",
            ),
            evidence_pointers=(PATHS["context"],),
            authority=TransformationEpisodeAuthority.PROPOSAL_ONLY,
            artifact_hash=canonical_hash({"episode": "domination-uniform-tail"}),
        ),
        ObstructionTransformationEpisode(
            episode_id="E-CROSSDOMAIN-TIMEOUT-BOUND-PROPOSAL",
            source_domain="algorithms / resource scheduling",
            source_context="per-input termination versus an input-dependent timeout schedule",
            source_obstruction=target,
            transformation_name="BOUND_HIDDEN_RUNTIME_BEFORE_TIMEOUT_TRANSFER",
            operation="derive an input-dependent runtime bound and compare it with the scheduled timeout",
            preconditions=(
                "the relevant runtime measure is known",
                "the bound is valid uniformly over the promised input class",
                "the scheduled timeout dominates the bound",
            ),
            resulting_relations=("scheduled completion follows after the comparison",),
            preserved_invariants=target.invariants_to_preserve,
            relaxed_or_broken_constraints=(),
            known_breakpoints=(
                "the target remainder is analytic rather than algorithmic",
                "the analogy supplies no number-theoretic modulus",
            ),
            evidence_pointers=(PATHS["context"],),
            authority=TransformationEpisodeAuthority.PROPOSAL_ONLY,
            artifact_hash=canonical_hash({"episode": "timeout-bound-proposal"}),
        ),
    )
    tm = build_transformation_memory(
        memory_id="RH-ANA-003j-TRANSFORMATION-MEMORY-20260812",
        source_universe=(
            "merged RH C002 fixed-n natural-order proof surface",
            "ANA-003i context and failure warnings",
            "elementary pointwise/uniform/diagonal convergence contexts",
            "dominated-convergence and uniform-asymptotic method contexts",
            "bounded fleet-stabilization and algorithmic-timeout analogy scan",
        ),
        episodes=episodes,
        evidence_pointers=(PATHS["memory"], PATHS["source_packet"]),
    )
    review = ObstructionTransformationReview(
        review_id="RH-ANA-003j-OBSTRUCTION-REVIEW-20260812",
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        research_memory_review_hash=memory_hash,
        episode_memory_snapshot_hash=tm.snapshot_hash,
        obstruction=target,
        direct_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        jump_search_status=RouteSearchStatus.NOT_RUN,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.CANNOT_CHECK,
        unresolved_warnings=(
            "The direct modulus transformation is mathematically appropriate but its target preconditions are not proved.",
            "No explicit n-dependent bound for the C002 constants or threshold is bound.",
            "No comparison M(n,epsilon_n)<=Y_n is available.",
            "The domination and timeout episodes remain proposal-only for this target.",
            "SEARCH retains an unmet direct route; JUMP and GLUE are not exhausted, so LIFT is not authorized.",
            "The only licensed action is the frozen quantifier-compatibility discriminator; no result branch may be selected yet.",
        ),
        evidence_pointers=(
            PATHS["source_packet"],
            PATHS["memory"],
            PATHS["quantifier_discriminator"],
        ),
        artifact_hash=canonical_hash({
            "atom": ATOM,
            "context": context_hash,
            "memory": memory_hash,
            "tm": tm.snapshot_hash,
            "mode": "CANNOT_CHECK",
        }),
    )
    return tm, review

def preservation_receipt() -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id="RH-ANA-003j-ROOT-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="every nontrivial zero of zeta has real part one half",
        surrogate_coordinate="moving-endpoint and internal-prefix control for the natural-order Abel rows",
        bridge_edges=(
            BridgeEdge(
                "RH003j-B1",
                "fixed-n natural-order Abel limit",
                "moving-diagonal endpoint rate",
                "requires a proved modulus M(n,epsilon) and eventual comparison M(n,epsilon_n)<=Y_n",
                EdgeProofStatus.UNPROVED,
                ("quantitative Abel remainder", "explicit n-dependence", "diagonal comparison"),
            ),
            BridgeEdge(
                "RH003j-B2",
                "moving-diagonal endpoint rate",
                "control of every internal prefix M<=Y_n",
                "requires a separate maximal/internal-prefix inequality; one endpoint cannot supply it",
                EdgeProofStatus.UNPROVED,
                ("prefix norm or maximal functional", "uniform prefix estimate"),
            ),
            BridgeEdge(
                "RH003j-B3",
                "endpoint and exact complement control",
                "S_n sign information, Li positivity, and RH",
                "requires the exact complement premise, Coffey/Li ledger, and all-index implication",
                EdgeProofStatus.UNPROVED,
                ("moving complement theorem", "all-index sign bridge", "Li criterion"),
            ),
        ),
        obligations=(
            Obligation("RH003j-O1", "derive a quantitative fixed-row modulus with explicit n-dependence", True, False),
            Obligation("RH003j-O2", "prove M(n,epsilon_n)<=Y_n eventually", True, False),
            Obligation("RH003j-O3", "separate endpoint from all-prefix control", True, False),
            Obligation("RH003j-O4", "preserve exact complement and Li/RH bridge obligations", True, False),
        ),
        known_disanalogies=(
            "pointwise convergence is not diagonal convergence",
            "diagonal-compatible control is not full n-uniform convergence",
            "endpoint control is not internal-prefix control",
            "fixed-n Abel convergence is not Li positivity",
        ),
        source_authority=CoordinateAuthority.PROPOSAL_ONLY,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world=(
            "e_n(Y)=1_{Y<=Y_n}: each fixed row is eventually zero, but the moving diagonal remains one"
        ),
        registered_observations=(
            RegisteredStateObservation("C002", "fixed-n natural-order identity and convergence recorded", "moving diagonal open"),
            RegisteredStateObservation("RH003j-pre", "quantifier discriminator frozen; no branch evaluated", "root open"),
        ),
        reverification_triggers=(
            "the positive sequence epsilon_n is first frozen or later changes",
            "Y_n changes",
            "a quantitative modulus or constant bound is proposed",
            "endpoint control is promoted to prefix or Li/RH control",
        ),
        prior_failure_ids=FAILURES,
    )


def framework_subject(context_hash: str):
    binding = FrameworkSubjectFreezeBinding(
        binding_id="RH-ANA-003j-FRAMEWORK-SUBJECT-FREEZE-20260812",
        authoritative_framework_sha=FRAMEWORK_SEMANTICS_SHA,
        pre_candidate_packet_hash=context_hash.removeprefix("sha256:"),
        frozen_at_utc=FROZEN_AT,
        evidence_pointers=(
            f"git:{FRAMEWORK_SEMANTICS_SHA}:RAKL_VERSION.json",
            f"git:{FRAMEWORK_SEMANTICS_SHA}:skills/rakl-core/workflows/mathematical-research.md",
            f"git:{FRAMEWORK_SEMANTICS_SHA}:src/rakl/math_research_runtime.py",
            f"git:{FRAMEWORK_SEMANTICS_SHA}:src/rakl/semantic_shortcut.py",
            f"git:{FRAMEWORK_SEMANTICS_SHA}:src/rakl/quantifier_compatibility.py",
            f"git:{FRAMEWORK_SEMANTICS_SHA}:schemas/quantifier-compatibility-witness-v1.schema.json",
            f"git:{FRAMEWORK_PIN_SHA}:config/rakl-framework-pin.json",
            "protected pre-candidate math workflow/runtime/API/gate/schema diff from prior live main is empty",
            "new live quantifier witness is routing/gluing-only and grants zero theorem authority",
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=FRAMEWORK_CURRENT_SHA,
        intervening_diff=tuple(
            DiffPathClassification(path, DiffSurfaceClass.NON_METHOD_PUBLICATION_OR_RESEARCH)
            for path in (
                "research/HOSTED_ANTHROPIC_GLM_API.md",
                "research/glm52_mechanism_suite_v1_1/HOSTED_SMOKE_RECEIPT.json",
                "research/glm52_mechanism_suite_v1_1/OFFLINE_SELFTEST_RECEIPT.json",
                "research/glm52_mechanism_suite_v1_1/STATUS.md",
                "scripts/glm52_hosted_smoke.py",
            )
        ),
        observation_evidence_pointers=(
            f"git:{FRAMEWORK_CURRENT_SHA}:RAKL_VERSION.json",
            f"git-diff:{FRAMEWORK_SEMANTICS_SHA}..{FRAMEWORK_CURRENT_SHA}",
            "live main moved only on classified non-method GLM hosted-smoke research/script surfaces; quantifier semantics remain those frozen at 2834760",
        ),
    )
    return binding, observation


def expert_review_document(context_hash: str) -> dict:
    roles = [
        (
            "analytic_number_theory_domain_lead",
            "C002 proves a row limit only after fixing n; every Abel/Laguerre constant may depend on n.",
            "Retain C002 exactly and demand a quantitative remainder with explicit n-dependence before using Y_n.",
        ),
        (
            "uniform_asymptotics_lead",
            "The Laguerre degree grows with n, so a fixed-degree tail estimate cannot be read as uniform asymptotics.",
            "Expose validity regions and constants, then compare the resulting modulus with the n^(5/3) log^2 cutoff.",
        ),
        (
            "summation_gluing_lead",
            "The natural-order endpoint, outer complement, and all internal prefixes are three different control surfaces.",
            "Reject reordering and require separate endpoint, prefix-maximal, and complement obligations.",
        ),
        (
            "quantifier_formal_logic_lead",
            "forall n exists M(n,epsilon) does not imply that a prescribed Y_n eventually exceeds M(n,epsilon_n).",
            "Write source and target quantifiers side by side and require a witnessed modulus/diagonal comparison.",
        ),
        (
            "adversarial_falsification_lead",
            "Y_n tending to infinity is compatible with a row threshold growing still faster.",
            "Use the triangular hostile world e_n(Y)=1_{Y<=Y_n} to reject every pointwise-only transfer before arithmetic work.",
        ),
        (
            "formal_methods_dependency_lead",
            "A routing witness can expose a scope mismatch but cannot prove the missing analytic estimate.",
            "Freeze branches and dependencies; evaluate none until the exact modulus candidate is separately frozen.",
        ),
        (
            "novelty_research_value_lead",
            "The pointwise-versus-diagonal distinction is standard; value lies only in resolving the RH-specific modulus.",
            "Claim no novelty for the logic gate and prioritize an explicit target-domain remainder bound.",
        ),
    ]
    return seal({
        "schema_version": "1.0.0",
        "review_id": "RH-ANA-003j-SEVEN-ROLE-EXPERT-CONTEXT-REVIEW-20260812",
        "atom_id": ATOM,
        "context_hash": context_hash,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT",
        "role_reviews": [
            {"role": role, "objection": objection, "recommendation": recommendation}
            for role, objection, recommendation in roles
        ],
        "disagreements": [
            "The uniform-asymptotics lens would accept full n-uniform control; the logic lens notes that a diagonal-compatible n-dependent modulus is the weaker sufficient target.",
            "The domain lens prioritizes the endpoint remainder; the summation lens refuses to let endpoint success stand in for internal-prefix control.",
        ],
        "strongest_objection": (
            "The fact that Y_n tends to infinity is mathematically insufficient because the valid row threshold M(n,epsilon_n) may depend arbitrarily on n and may grow faster than Y_n."
        ),
        "unresolved_uncertainty": [
            "growth of the C002 boundary and tail-integral constants with n",
            "existence of a diagonal-compatible modulus at epsilon_n and Y_n",
            "whether any endpoint estimate can be strengthened to an internal-prefix maximal estimate",
        ],
        "next_action_recommendation": (
            "Execute only the frozen quantifier-compatibility discriminator: derive a target modulus, expose constants, "
            "and compare it with Y_n; select no result branch in this round."
        ),
        "independent_review_credit": 0,
        "process_assurance_mathematical_credit": 0,
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
    evidence = {
        ResearchTraceEventType.ATOMIZED: PATHS["atomization"],
        ResearchTraceEventType.CONTEXT_FROZEN: PATHS["context"],
        ResearchTraceEventType.ANALOGY_SCAN: PATHS["context"],
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW: PATHS["source_packet"],
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW: PATHS["expert_review"],
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW: PATHS["memory"],
        ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW: PATHS["shortcut_review"],
        ResearchTraceEventType.NEXT_STEP_PROPOSED: PATHS["quantifier_discriminator"],
    }
    entries = []
    previous = ""
    for index, kind in enumerate(kinds, 1):
        outputs = ["PRE_CANDIDATE_ONLY", "NO_EVALUATED_RESULT", "PROCESS_ASSURANCE_ZERO_MATHEMATICAL_CREDIT"]
        if kind is ResearchTraceEventType.CONTEXT_FROZEN:
            outputs.insert(0, context_hash)
        if kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            outputs.insert(0, memory_hash)
        if kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            outputs[:0] = [shortcut_hash, "selected_mode:CANNOT_CHECK", "LIFT_NOT_AUTHORIZED"]
        payload = {
            "event_id": f"RH-ANA-003j-E{index:02d}",
            "atom_id": ATOM,
            "event_type": kind.value,
            "timestamp": f"2026-08-12T10:18:{index:02d}Z",
            "state_summary": (
                "C002 supplies fixed-n natural-order convergence only. The moving-diagonal, all-prefix, complement, "
                "Li, and RH obligations remain open; no target modulus or result has been proposed."
            ),
            "action_summary": kind.value,
            "evidence_pointers": [evidence[kind]],
            "alternatives_considered": [
                "infer diagonal control because Y_n tends to infinity",
                "demand full uniform convergence in n",
                "seek the weaker diagonal-compatible n-dependent modulus",
                "promote endpoint control to all internal prefixes",
                "rotate to another RH method before resolving the quantifier mismatch",
            ],
            "decision_rationale": (
                "The minimal mathematical bridge is an explicit row modulus plus eventual domination by the frozen diagonal; "
                "full uniformity is stronger than necessary, while pointwise convergence alone is insufficient."
            ),
            "outputs": outputs,
            "uncertainties": [
                "no quantitative C002 modulus is bound",
                "n-dependence of Laguerre/Abel constants is unknown",
                "same-context review is not independent",
            ],
            "residuals": [
                "modulus and diagonal comparison unproved",
                "endpoint-to-prefix transfer unproved",
                "SEARCH/JUMP/GLUE unexhausted",
                "root OPEN_NO_SOLUTION_CERTIFICATE",
            ],
            "next_steps": [
                "derive or load a quantitative remainder modulus M(n,epsilon)",
                "expose every n-dependent constant and validity regime",
                "prove or refute M(n,epsilon_n)<=Y_n eventually",
                "if endpoint control survives, separately test internal-prefix and complement bridges",
                "do not select or evaluate a result branch in this round",
            ],
            "previous_event_hash": previous,
        }
        artifact_hash = canonical_hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **{**payload, "event_type": kind}))
        previous = artifact_hash
    return MathResearchTrace("RH-ANA-003j-PRE-CANDIDATE-TRACE-20260812", tuple(entries))


def build_current_gate_plan():
    fiber = context()
    memory = memory_review(fiber.packet_hash)
    tm, shortcut = transformation_memory_and_review(fiber.packet_hash, memory.artifact_hash)
    research_trace = trace(fiber.packet_hash, memory.artifact_hash, shortcut.artifact_hash)
    preservation = preservation_receipt()
    binding, observation = framework_subject(fiber.packet_hash)
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=(
                "two-parameter natural-order error E(n,Y)",
                "row-wise threshold M(n,epsilon)",
                "moving cutoff Y_n and tolerance epsilon_n",
                "endpoint R_n(Y_n)",
                "internal prefixes R_n(M) for M<=Y_n",
                "exact target S_n and complement",
            ),
            relations=(
                "fixed-n limit",
                "quantifier order",
                "diagonal substitution",
                "modulus growth comparison",
                "endpoint versus prefix scope",
                "exact complement gluing",
            ),
            domain="analytic number theory / uniform asymptotics / quantifier logic",
            goal_type="freeze a candidate-free quantifier-compatibility discriminator",
        ),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=fiber,
        memory_review=memory,
        transformation_memory=tm,
        shortcut_review=shortcut,
        research_trace=research_trace,
        preservation_receipt=preservation,
        require_preservation_gate=True,
        expected_preservation_sha256=preservation.document()["receipt_canonical_sha256"],
        framework_subject_binding=binding,
        framework_subject_observation=observation,
        require_framework_subject_gate=True,
    )
    return plan, fiber, memory, tm, shortcut, research_trace, preservation

def source_packet_document() -> dict:
    return seal({
        "schema_version": "1.0.0",
        "packet_id": "RH-ANA-003j-SOURCE-METHOD-TRANSFER-PACKET-20260812",
        "atom_id": ATOM,
        "retrieved_before_candidate": True,
        "primary_sources": [
            {
                "id": "C002-FIXED-N-ABEL",
                "citation": "RAKL_math merged C002 fixed-n natural-order Abel identity and convergence result",
                "anchors": ["exact_mathematical_result.quantifiers", "residual"],
                "exact_path": f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json",
                "authorized_use": "fixed-n natural-order row identity/convergence only",
            },
            {
                "id": "BELLOTTI-2508.02041v1",
                "citation": "C. Bellotti, A new zero-density estimate and an improved error term in the prime number theorem, arXiv:2508.02041v1",
                "anchors": ["Theorem 1.5", "equations (1.3)-(1.4)"],
                "pdf_sha256": "39a39e3dbc73506cf5dfd0b8a18b24e85302d305fa3059a60abcfa6f23292568",
                "authorized_use": "source estimate used by C002; no n-uniform Laguerre remainder follows",
            },
            {
                "id": "DUNSTER-GIL-SEGURA-1705.01190v1",
                "citation": "T. M. Dunster, A. Gil, and J. Segura, Uniform asymptotic expansions for Laguerre polynomials, arXiv:1705.01190v1",
                "anchors": ["equation (1.1) exact finite Laguerre sum"],
                "pdf_sha256": "e93985f8ede2799f6e9f3b12dad2565228fefa0b1f662306e2caf9768d2b423c",
                "authorized_use": "uniform-asymptotic search context only; no target modulus is imported",
            },
            {
                "id": "COFFEY-0706.0343v2",
                "citation": "M. W. Coffey, Relations and positivity results for the derivatives of the Riemann xi function, arXiv:0706.0343v2",
                "anchors": ["Proposition 2(a), equations (15)-(17)", "equations (118)-(120)"],
                "pdf_sha256": "57cf784447e1f4156144ef3fd0253bb3452273918f470bcfbc063ee049c8cbc5",
                "authorized_use": "exact normalization and root-sensitive context only",
            },
            {
                "id": "LI-1997",
                "citation": "X.-J. Li, The positivity of a sequence of numbers and the Riemann hypothesis, JNT 65 (1997), 325-333",
                "anchors": ["all-index positivity criterion"],
                "access_status": "BOUND_VIA_CURRENT_MAIN_SOURCE_PACKET_NOT_LIVE_RETRIEVED_THIS_ROUND",
                "authorized_use": "root bridge boundary only",
            },
        ],
        "source_target_quantifier_table": [
            {
                "transfer_id": "Q1_FIXED_N_TO_MOVING_DIAGONAL",
                "source_statement": "E(n,Y)=|S_n-R_n(Y)| tends to zero as Y tends to infinity for every fixed n",
                "source_quantifier_order": "forall n forall epsilon>0 exists M(n,epsilon) forall Y>=M(n,epsilon): E(n,Y)<epsilon",
                "target_statement": "the frozen diagonal achieves a future preregistered positive tolerance epsilon_n eventually",
                "target_quantifier_order": "exists N forall n>=N: E(n,Y_n)<=epsilon_n",
                "required_uniform_modulus": "a proved quantitative M(n,epsilon); full n-uniformity is sufficient but not necessary",
                "proposed_diagonal": "Y_n=exp(C n^(5/3) log^2(n+e))",
                "required_diagonal_comparison": "exists N forall n>=N: M(n,epsilon_n)<=Y_n",
                "constants_uniform_in_n": "UNKNOWN_NOT_SUPPLIED_BY_C002",
                "control_scope": "ENDPOINT_ONLY",
                "exact_complement_premise": "NOT_USED_FOR_ROW_LIMIT; REQUIRED_SEPARATELY_FOR_ENDPOINT_TO_S_n_SIGN_TRANSFER",
                "failure_branch": "POINTWISE_ONLY_NO_DIAGONAL_TRANSFER",
            },
            {
                "transfer_id": "Q2_DIAGONAL_ENDPOINT_TO_INTERNAL_PREFIXES",
                "source_statement": "E(n,Y_n)<=epsilon_n at one endpoint",
                "source_quantifier_order": "exists N forall n>=N: E(n,Y_n)<=epsilon_n",
                "target_statement": "a specified internal-prefix functional is controlled for every M<=Y_n",
                "target_quantifier_order": "exists N forall n>=N forall M with 2<=M<=Y_n: PREFIX_OBLIGATION(n,M)",
                "required_uniform_modulus": "a separate maximal or prefix-family estimate",
                "proposed_diagonal": "endpoint M=Y_n inside the prefix interval",
                "required_diagonal_comparison": "NOT_SUFFICIENT; ONE ENDPOINT DOES NOT CONTROL THE INTERVAL",
                "constants_uniform_in_n": "UNKNOWN",
                "control_scope": "FULL_PREFIX_TARGET_FROM_ENDPOINT_SOURCE",
                "exact_complement_premise": "OUTER_COMPLEMENT_DOES_NOT_SUPPLY_INTERNAL_PREFIX_CONTROL",
                "failure_branch": "ENDPOINT_ONLY_NO_INTERNAL_PREFIX_TRANSFER",
            },
            {
                "transfer_id": "Q3_ENDPOINT_PLUS_COMPLEMENT_TO_ROOT_BRIDGE",
                "source_statement": "moving endpoint and complement estimates at the same cutoff",
                "source_quantifier_order": "TO_BE_PROVED_WITH_EXPLICIT_ALL_LARGE_N_SCOPE",
                "target_statement": "all-index Li positivity and RH",
                "target_quantifier_order": "forall n>=1: lambda_n>0, plus the exact registered finite-index/ledger obligations",
                "required_uniform_modulus": "not merely an asymptotic endpoint modulus; exact complement and ledger obligations remain",
                "proposed_diagonal": "Y_n as above",
                "required_diagonal_comparison": "NECESSARY_BUT_NOT_SUFFICIENT_FOR_ROOT_BRIDGE",
                "constants_uniform_in_n": "UNKNOWN",
                "control_scope": "TARGET_AND_ROOT_BRIDGE",
                "exact_complement_premise": "D_n(Y_n) bound at the same n, cutoff, normalization, and source order",
                "failure_branch": "CANNOT_CHECK",
            },
        ],
        "allowed_future_result_branches": [
            "UNIFORM_MODULUS_AND_DIAGONAL_COMPATIBILITY_PROVED",
            "POINTWISE_ONLY_NO_DIAGONAL_TRANSFER",
            "ENDPOINT_ONLY_NO_INTERNAL_PREFIX_TRANSFER",
            "CANNOT_CHECK",
        ],
        "selected_result_branch": None,
        "mathematical_transfer_summary": (
            "The missing object is not a larger cutoff by itself but a quantitative convergence modulus with "
            "controlled n-dependence. The weakest sufficient bridge is diagonal compatibility, not necessarily full uniform convergence."
        ),
        "authority": "SOURCE_AND_METHOD_TRANSFER_CONTEXT_ONLY_NO_TARGET_RESULT",
        "mathematical_result_credit": False,
    })


def quantifier_discriminator_document(trace_last_event_hash: str) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "discriminator_id": "RH-ANA-003j-QUANTIFIER-COMPATIBILITY-DISCRIMINATOR-20260812",
        "atom_id": ATOM,
        "frozen_at": DISCRIMINATOR_FROZEN_AT,
        "pre_candidate_trace_last_event_hash": trace_last_event_hash,
        "parameter_scope": PARAMETER_SCOPE,
        "source_statement": "forall n forall epsilon>0 exists M(n,epsilon) forall Y>=M: E(n,Y)<epsilon",
        "target_statement": "exists N forall n>=N: E(n,Y_n)<=epsilon_n",
        "quantifier_axes": [
            "fixed n versus n tending to infinity",
            "Y tending to infinity after fixing n versus diagonal Y=Y_n",
            "row threshold M(n,epsilon) versus eventual diagonal comparison M(n,epsilon_n)<=Y_n",
            "existence of each row limit versus a quantitative modulus/rate",
            "endpoint R_n(Y_n) versus every internal prefix R_n(M), M<=Y_n",
            "exact natural order versus forbidden regrouping/reordering",
            "endpoint/complement target transfer versus the separate Li/RH bridge",
        ],
        "required_table_fields": [
            "source_statement",
            "source_quantifier_order",
            "target_statement",
            "target_quantifier_order",
            "required_uniform_modulus",
            "proposed_diagonal",
            "required_diagonal_comparison",
            "constants_uniform_in_n",
            "control_scope",
            "exact_complement_premise",
            "failure_branch",
        ],
        "cheapest_hostile_world_to_execute_later": {
            "definition": "e_n(Y)=1 when Y<=Y_n and e_n(Y)=0 when Y>Y_n",
            "expected_discrimination": (
                "each fixed row is eventually zero, while e_n(Y_n)=1; therefore a pointwise-only inference rule must reject diagonal transfer"
            ),
            "status": "FROZEN_NOT_EVALUATED",
            "target_authority": "LOGIC_HOSTILE_WORLD_ONLY_NOT_RH_EVIDENCE",
        },
        "required_target_validation": [
            "derive an explicit valid M(n,epsilon) from the natural-order Abel remainder",
            "expose all n-dependent Laguerre, boundary, and tail-integral constants",
            "prove M(n,epsilon_n)<=Y_n eventually",
            "state whether only endpoint or every internal prefix is controlled",
            "retain exact complement and Li/RH obligations separately",
        ],
        "allowed_future_result_branches": [
            "UNIFORM_MODULUS_AND_DIAGONAL_COMPATIBILITY_PROVED",
            "POINTWISE_ONLY_NO_DIAGONAL_TRANSFER",
            "ENDPOINT_ONLY_NO_INTERNAL_PREFIX_TRANSFER",
            "CANNOT_CHECK",
        ],
        "selected_result_branch": None,
        "live_framework_quantifier_semantics": {
            "framework_semantics_sha": FRAMEWORK_SEMANTICS_SHA,
            "observed_live_main_sha": FRAMEWORK_CURRENT_SHA,
            "source_scope_alignment": "MISALIGNED",
            "substitution_permission": "UNKNOWN_UNTIL_MODULUS_AND_COMPARISON_ARE_PROVED",
            "required_scope_witness": "UNKNOWN",
            "faithful_pre_result_status": "FAIL_CLOSED_UNKNOWN",
            "conditional_status_forbidden_without_explicit_bridge": True,
            "authority": "ROUTING_GLUING_ONLY_NOT_THEOREM",
        },
        "candidate_identity": None,
        "epsilon_sequence_identity": None,
        "epsilon_sequence_status": "TO_BE_FROZEN_BEFORE_RESULT_EVALUATION",
        "evaluator_capability": False,
        "evaluated_result": False,
        "status": "PRE_CANDIDATE_DISCRIMINATOR_FROZEN_NO_RESULT",
        "mathematical_lesson_boundary": {
            "attempted_mathematical_implication": (
                "forall n, lim_{Y->infinity} R_n(Y)=S_n  =>  |S_n-R_n(Y_n)|<=epsilon_n eventually"
            ),
            "exact_mathematical_state": (
                "The source quantifiers expose a row threshold M(n,epsilon), while the target additionally "
                "requires M(n,epsilon_n)<=Y_n eventually. No such modulus or comparison is proved in this round."
            ),
            "supported_mathematical_cause": (
                "The unbridged coordinate is the n-dependence of the convergence threshold, not the mere fact that Y_n tends to infinity."
            ),
            "competing_mathematical_causes": [
                "C002 may admit a useful but currently unproved n-dependent modulus",
                "full uniform convergence in n may fail while the particular diagonal remains compatible",
                "even a successful endpoint modulus may leave every internal-prefix maximum uncontrolled",
            ],
            "scope": "PRE_CANDIDATE_LOGICAL_AND_METHOD_TRANSFER_DIAGNOSIS_ONLY",
            "mathematical_falsifier_or_discriminator": (
                "Derive a valid target-domain M(n,epsilon) and determine whether M(n,epsilon_n)<=Y_n eventually; "
                "the frozen triangular-array hostile world separately tests any generic pointwise-only inference rule."
            ),
            "repair_or_next_mathematical_action": (
                "Bound the C002 Abel boundary and tail integral with every Laguerre/Abel constant explicit in n."
            ),
            "proof_or_source_evidence": [
                f"git:{APPLICATION_BASE_SHA}:{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json",
                PATHS["context"],
                PATHS["source_packet"],
            ],
            "evaluated_result": False,
            "process_assurance_mathematical_credit": 0,
        },
        "process_assurance_mathematical_credit": 0,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
def build_documents() -> dict[str, dict]:
    plan, fiber, memory, tm, shortcut, research_trace, preservation = build_current_gate_plan()
    binding, observation = framework_subject(fiber.packet_hash)
    source = source_packet_document()
    atom = seal({
        "schema_version": "1.0.0",
        "atomization_id": "RH-ANA-003j-ATOMIZATION-20260812",
        "recorded_at": FROZEN_AT,
        "atom_id": ATOM,
        "parent_atom_id": PARENT,
        "root_issue": 3,
        "control_issues": [265, 315, 324],
        "object": (
            "The two-parameter error E(n,Y)=|S_n-R_n(Y)| for the actual zeta-domain natural-order array, "
            "the C002 fixed-n limit, moving cutoff Y_n=exp(C n^(5/3) log^2(n+e)), tolerance epsilon_n, "
            "endpoint R_n(Y_n), internal prefixes R_n(M) for M<=Y_n, and exact complement D_n(Y_n)."
        ),
        "parameter_scope": PARAMETER_SCOPE,
        "qoi": (
            "Whether the fixed-n pointwise Abel limit has a proved quantitative modulus M(n,epsilon) whose "
            "n-dependence is compatible with the moving diagonal, specifically M(n,epsilon_n)<=Y_n eventually; "
            "and which additional obligations separate endpoint, internal-prefix, complement, and Li/RH control."
        ),
        "source_quantifier_normal_form": "forall n forall epsilon>0 exists M(n,epsilon) forall Y>=M: E(n,Y)<epsilon",
        "target_quantifier_normal_form": "exists N forall n>=N: E(n,Y_n)<=epsilon_n",
        "missing_bridge_normal_form": "exists a proved M and exists N forall n>=N: M(n,epsilon_n)<=Y_n",
        "target_scale_obligation": (
            "C is one fixed real constant >0 inherited from ANA-003i and log Y_n=C n^(5/3) log^2(n+e); "
            "no sufficient C is proved. The exact positive sequence epsilon_n is TO_BE_FROZEN before any evaluated result."
        ),
        "first_discriminator": [
            "derive a valid quantitative modulus M(n,epsilon) for the C002 natural-order remainder",
            "make every n-dependent Abel/Laguerre constant and validity regime explicit",
            "prove or refute M(n,epsilon_n)<=Y_n eventually; Y_n tending to infinity is not sufficient",
            "state whether the conclusion controls only R_n(Y_n) or every R_n(M) with M<=Y_n",
            "preserve natural order and reject every reordering or regrouping",
            "keep exact complement and Li/RH bridge premises as separate unproved obligations",
        ],
        "candidate_generation_allowed": False,
        "candidate_proposed": False,
        "target_result_accessed": False,
        "lift_authorized": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
        "authority_boundary": {
            "operational_metadata_zero_mathematical_credit": True,
            "grants_uniform_modulus": False,
            "grants_diagonal_compatibility": False,
            "grants_moving_prefix_bound": False,
            "grants_complement_rate": False,
            "grants_li_positivity": False,
            "grants_rh_authority": False,
        },
    })
    tool_snapshot = seal({
        "schema_version": "1.0.0",
        "snapshot_id": "RH-ANA-003j-TOOL-SNAPSHOT-20260812",
        "target_atom_id": ATOM,
        "application_base_commit": APPLICATION_BASE_SHA,
        "query_result": "MATCHES_FOUND",
        "tools": [{
            "tool_id": "T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY",
            "authority": "SCOPED_PROOF_BACKED_CURRENT_MAIN",
            "applicable_effect": "preserve fixed-n natural-order identity, row limit, and exact row remainder representation",
            "non_guarantees": [
                "no bound on M(n,epsilon)",
                "no moving-n or diagonal rate",
                "no n-uniform constants",
                "no all-prefix maximal bound",
                "no Li or RH implication"
            ],
        }],
        "mathematical_credit": False,
    })
    failure_details = {
        "F-RH-ANA-003e-MOVING-PREFIX-POLYBOUND-NOT-WEAKER": {
            "attempted_mathematical_implication": "use a moving-prefix polynomial bound as a premise weaker than endpoint/Li control",
            "exact_mathematical_failure": "the registered premise-strength audit did not establish a strictly weaker route to the target endpoint obligation",
            "supported_mathematical_cause": "the proposed prefix premise can dominate or reconstruct the endpoint-scale control it was meant to replace",
            "competing_mathematical_causes": ["cutoff scale too small", "polynomial degree growth too large", "arithmetic realization missing"],
            "scope": "moving natural-order prefix families at the registered RH cutoff",
            "mathematical_falsifier": "exhibit a target-domain prefix premise with an exact feasible-set witness strictly larger than the endpoint-controlled set",
            "repair_or_next_discriminator": "derive the exact endpoint projection and premise inclusion before estimating the family",
        },
        "F-RH-ANA-003f-STRICT-CUT-SUFFIX-GLUE": {
            "attempted_mathematical_implication": "transfer a strict-cut prefix statement to the exact target while suppressing or weakening the suffix",
            "exact_mathematical_failure": "the target identity retains the natural-order suffix/complement, so the prefix implication does not close without it",
            "supported_mathematical_cause": "the decomposition is additive in the exact source order and the omitted suffix is load-bearing",
            "competing_mathematical_causes": ["prefix estimate itself too weak", "cutoff chosen in a wrong asymptotic regime", "normalization mismatch"],
            "scope": "natural-order strict-cut decompositions of the registered von-Mangoldt/Laguerre sum",
            "mathematical_falsifier": "prove the exact suffix is negligible under premises strictly weaker than the desired endpoint/Li statement",
            "repair_or_next_discriminator": "keep the suffix explicit and test prefix and complement estimates as separate obligations at the same cutoff",
        },
        "F-RH-ANA-003f-PATH-WITNESS-NOT-ARITHMETIC": {
            "attempted_mathematical_implication": "use an ambient signed path as a strictness or attainability witness for the arithmetic prefix family",
            "exact_mathematical_failure": "membership in an ambient path class does not show realization by the fixed von-Mangoldt/Laguerre array",
            "supported_mathematical_cause": "the target coefficients are arithmetically fixed rather than freely selectable",
            "competing_mathematical_causes": ["ambient witness violates natural order", "family definition encodes the endpoint", "transfer map is non-surjective"],
            "scope": "strictness and feasibility witnesses for actual RH arithmetic prefixes",
            "mathematical_falsifier": "construct or prove existence of a target-domain arithmetic realization satisfying the witness constraints",
            "repair_or_next_discriminator": "require TARGET_DOMAIN realization or a fully proved transfer witness before strictness credit",
        },
        "F-RH-ANA-003g-COMPLEMENT-FIRST-WEAKENING-FAIL": {
            "attempted_mathematical_implication": "start from outer-complement control and infer that the remaining internal premise is a weaker route",
            "exact_mathematical_failure": "a small complement can make the internal premise equivalent in strength to endpoint control rather than strictly weaker",
            "supported_mathematical_cause": "the identity joining prefix endpoint, complement, and S_n conserves the target burden",
            "competing_mathematical_causes": ["complement estimate unavailable", "one-sided signs misaligned", "finite-index obligations omitted"],
            "scope": "endpoint-plus-complement decompositions at the same moving cutoff",
            "mathematical_falsifier": "prove exact premise inclusion showing the combined premises admit target cases excluded by direct endpoint control",
            "repair_or_next_discriminator": "audit premise strength only after writing the exact endpoint-complement identity",
        },
        "R9-STRICT-PREFIX-ARITHMETIC-ATTAINABILITY-OBSTRUCTION": {
            "attempted_mathematical_implication": "use a sharpened outer-complement cutoff to close a strict internal-prefix route",
            "exact_mathematical_failure": "outer-complement scale improvement does not supply an arithmetic strict-prefix realization or maximal bound",
            "supported_mathematical_cause": "outer-tail and internal-prefix controls are different mathematical objects",
            "competing_mathematical_causes": ["outer cutoff rate remains unproved", "endpoint projection collapses strictness", "uniform-in-n constants missing"],
            "scope": "R9 proposal-only cutoff scale and actual natural-order prefixes",
            "mathematical_falsifier": "prove a source-bound arithmetic prefix family realized at the cutoff with exact endpoint projection and a strict-premise witness",
            "repair_or_next_discriminator": "separate the diagonal endpoint modulus from any later internal-prefix maximal inequality",
        },
    }
    failure_snapshot = seal({
        "schema_version": "1.0.0",
        "snapshot_id": "RH-ANA-003j-FAILURE-SNAPSHOT-20260812",
        "target_atom_id": ATOM,
        "failures": [dict(
            failure_id=item,
            status="PARENT_BOUND_MATHEMATICAL_WARNING_NOT_REEVALUATED_THIS_ROUND",
            blocks_all_reuse=False,
            proof_or_source_evidence=[
                f"git:{APPLICATION_BASE_SHA}:{BASE}/01_frontier/RH_ANA_003i_MATH_CONTEXT_FIBER_20260812.json",
                f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/RH_ANA_003i_RESEARCH_MEMORY_REVIEW_20260812.json",
            ],
            process_assurance_mathematical_credit=0,
            **failure_details[item],
        ) for item in FAILURES],
        "parent_context": f"git:{APPLICATION_BASE_SHA}:{BASE}/01_frontier/RH_ANA_003i_MATH_CONTEXT_FIBER_20260812.json",
        "reuse_rule": "prior failure is a warning, not a blacklist; target-specific difference and cheapest repeat-failure tests are required",
        "mathematical_credit": False,
    })
    expert = expert_review_document(fiber.packet_hash)
    binding_document = seal(dict(binding.document()))
    observation_document = seal({
        "schema_version": "framework-subject-revalidation-observation-v1",
        "observation_id": "RH-ANA-003j-FRAMEWORK-REVALIDATION-20260812",
        "observed_current_main_sha": observation.observed_current_main_sha,
        "intervening_diff": [
            {"path": item.path, "surface_class": item.surface_class.value}
            for item in observation.intervening_diff
        ],
        "observation_evidence_pointers": list(observation.observation_evidence_pointers),
        "verdict": plan.framework_subject_gate.verdict.value,
        "licenses_candidate_materialization": plan.framework_subject_gate.licenses_candidate_materialization,
        "application_pin_lacks_live_quantifier_compatibility_surface": True,
        "live_quantifier_semantics_applied_manually_fail_closed": True,
        "grants_scientific_authority": False,
    })
    discriminator = quantifier_discriminator_document(research_trace.entries[-1].artifact_hash)
    documents = {
        "source_packet": source,
        "atomization": atom,
        "context": _document(fiber),
        "tool_snapshot": tool_snapshot,
        "failure_snapshot": failure_snapshot,
        "memory": _document(memory),
        "transformation_memory": _document(tm),
        "expert_review": expert,
        "shortcut_review": _document(shortcut),
        "quantifier_discriminator": discriminator,
        "preservation": _jsonable(preservation.document()),
        "trace": _document(research_trace),
        "framework_binding": binding_document,
        "framework_observation": observation_document,
    }
    integrity = {
        "algorithm": "SHA-256",
        "canonicalization": "JSON_SORT_KEYS_COMPACT_UTF8",
        "inputs": {
            name: {"path": PATHS[name], "canonical_sha256": canonical_hash(document)}
            for name, document in sorted(documents.items())
        },
    }
    documents["gate"] = seal({
        "schema_version": "1.0.0",
        "receipt_id": "RH-ANA-003j-PRE-CANDIDATE-GATE-20260812",
        "application_base_commit": APPLICATION_BASE_SHA,
        "framework_current_commit": FRAMEWORK_CURRENT_SHA,
        "framework_application_pin": FRAMEWORK_PIN_SHA,
        "atom_id": ATOM,
        "artifact_bindings": {
            "context_hash": fiber.packet_hash,
            "memory_review_hash": memory.artifact_hash,
            "transformation_memory_snapshot_hash": tm.snapshot_hash,
            "shortcut_review_hash": shortcut.artifact_hash,
            "trace_last_event_hash": research_trace.entries[-1].artifact_hash,
            "quantifier_discriminator_hash": discriminator["artifact_hash"],
            "preservation_sha256": preservation.document()["receipt_canonical_sha256"],
            "framework_subject_binding_sha256": binding.binding_canonical_sha256,
            "full_document_integrity_hash": canonical_hash(integrity),
        },
        "full_document_integrity": integrity,
        "gate_verdicts": {
            "context": plan.context_gate.verdict.value,
            "dual_memory": plan.memory_gate.verdict.value,
            "obstruction_transformation": plan.shortcut_gate.verdict.value,
            "trace_runtime_gate": plan.trace_gate.verdict.value,
            "trace_direct_audit_expected": "PASS",
            "preservation": plan.preservation_gate.verdict.value,
            "framework_subject": plan.framework_subject_gate.verdict.value,
            "selected_mode": shortcut.selected_mode.value,
            "candidate_generation_allowed": plan.candidate_generation_allowed,
            "licensed_action": "FREEZE_QUANTIFIER_COMPATIBILITY_DISCRIMINATOR_ONLY_NO_EVALUATION",
            "lift_authorized": False,
        },
        "chronology": {
            "candidate_identity": None,
            "candidate_proposed": False,
            "target_result_accessed": False,
            "evaluator_executed": False,
            "discriminator_frozen_after_trace": True,
            "selected_result_branch": None,
        },
        "authority": {
            "assurance_only": True,
            "mathematical_result_credit": False,
            "mathematical_saturation_credit": False,
            "grants_theorem_truth": False,
            "grants_novelty": False,
            "grants_independent_review": False,
            "grants_li_or_rh_authority": False,
        },
    })
    return documents


def write_documents(root: Path = Path(".")) -> None:
    for name, document in build_documents().items():
        path = root / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_documents()
