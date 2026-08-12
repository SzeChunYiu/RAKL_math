"""Prospective strict-v3 packet for the fixed-n Abel-interface atom.

This fixture contains no proof of the intended lemma and no target evaluator.
It may license only a public candidate/proof-input freeze.  Operational
assurance fields carry zero mathematical credit.
"""
from __future__ import annotations

from dataclasses import asdict
from enum import Enum
import hashlib
import json
from pathlib import Path

from rakl.framework_candidate_freeze import (
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
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
)
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


ATOM = "RH-ANA-003-ABEL-001"
PARENT_ATOM = "RH-ANA-003"
APPLICATION_BASE_SHA = "58de5548d337d4ea3c83b5fcde6ed5c6aee3f2e0"
FRAMEWORK_PIN_SHA = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
FRAMEWORK_CURRENT_SHA = "44058e21e16b085b421638fadad5086e31472f0f"
FROZEN_AT = "2026-08-12T07:23:10Z"
BELLOTTI_HTML_SHA256 = "2b57101a941e31c033ae2510efe8f4b3e81f22f025cd857fcb53d8ce77f3e634"

BASE = "research/real_math/millennium/riemann_hypothesis"
PATHS = {
    "source_packet": f"{BASE}/01_frontier/RH_ANA_003_ABEL_001_SOURCE_PACKET_20260812.json",
    "atomization": f"{BASE}/02_problem_dag/RH_ANA_003_ABEL_001_ATOMIZATION_20260812.json",
    "context": f"{BASE}/01_frontier/RH_ANA_003_ABEL_001_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/RH_ANA_003_ABEL_001_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/RH_ANA_003_ABEL_001_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/RH_ANA_003_ABEL_001_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/RH_ANA_003_ABEL_001_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/RH_ANA_003_ABEL_001_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/RH_ANA_003_ABEL_001_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_PRE_CANDIDATE_TRACE_20260812.json",
    "framework_binding": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_FRAMEWORK_SUBJECT_FREEZE_BINDING_20260812.json",
    "framework_observation": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "gate": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
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
    transfer = MethodTransfer(
        source_context="finite Abel summation for a naturally ordered sequence",
        method=(
            "replace a finite weighted sum by two cumulative-sum boundary terms "
            "and one integral against the derivative of the weight"
        ),
        shared_structure=(
            "a_m is read in its original integer order",
            "A(x) is the exact cumulative source state through floor(x)",
            "b_n is continuously differentiable on each fixed positive tail",
            "the finite identity precedes every limiting argument",
        ),
        required_assumptions=(
            "the finite endpoints and endpoint convention are fixed exactly",
            "A(x)=sum_{m<=x}a_m uses the same natural order as the target series",
            "b_n is C1 on the endpoint interval",
            "boundary decay and improper-integral convergence are proved separately before Y tends to infinity",
        ),
        disanalogies=(
            "finite Abel summation alone does not prove the infinite boundary vanishes",
            "the target weight depends on n and the prospective claim fixes n before the limit",
            "an absolutely convergent transformed integral does not make the original term series absolutely convergent",
            "no estimate uniform in n follows from a fixed-n argument",
        ),
        repair_question=(
            "For each already fixed n, do Bellotti's unconditional PNT error and "
            "the exact polynomial nature of L_{n-1}^{(1)} suffice to kill the "
            "Abel boundary and make the derivative integral convergent without "
            "reordering the original terms?"
        ),
        source_anchors=(
            "classical finite Abel/summation-by-parts identity",
            "https://arxiv.org/html/2508.02041v1#S1.Thmtheorem5",
            "https://arxiv.org/html/2508.02041v1#S1.E3",
            "https://arxiv.org/html/2508.02041v1#S1.E4",
        ),
    )
    analogy = CrossDomainAnalogy(
        source_kind="ordinary bookkeeping / event-sourced ledger",
        source_situation=(
            "A chronological ledger is reconciled by its running balance and "
            "time-varying weight without permuting transactions"
        ),
        common_abstraction=(
            "ordered signed increments",
            "cumulative state",
            "integration by parts against a changing weight",
        ),
        source_to_target_mapping=(
            "transaction increment -> a_m=1-Lambda(m)",
            "running balance -> A(x)=floor(x)-psi(x)",
            "time-varying weight -> b_n(x)",
            "chronological reconciliation -> natural-order Abel identity",
        ),
        shared_constraints=(
            "order is part of the object",
            "the cumulative state must use the same ordering",
            "the endpoint balance cannot be silently discarded",
        ),
        disanalogies=(
            "the ledger analogy supplies no analytic bound or theorem authority",
            "prime powers and Laguerre growth have no ordinary-ledger analogue",
            "the target limit is infinite and requires mathematical convergence",
        ),
        proposed_principle=(
            "move cancellation into the exact cumulative state before estimating, "
            "while preserving source order"
        ),
        validation_obligation=(
            "derive the exact finite endpoint identity, prove the Bellotti-based "
            "boundary and integral limits for fixed n, and independently test "
            "whether absolute convergence actually fails"
        ),
        provenance_note="proposal-only everyday analogy; zero theorem authority",
    )
    payload = {
        "atom": ATOM,
        "application_base": APPLICATION_BASE_SHA,
        "bellotti_v1_html_sha256": BELLOTTI_HTML_SHA256,
        "coordinates": [
            "a_m=1-Lambda(m)",
            "A(x)=sum_{m<=x}a_m=floor(x)-psi(x)",
            "b_n(x)=L_{n-1}^{(1)}(log x)/x",
            "fixed n before Y tends to infinity",
            "natural source order and exact finite endpoint convention",
        ],
    }
    return MathContextFiber(
        atom_id=ATOM,
        object_context=(
            "The exact fixed-index convergence interface between the natural-order "
            "prime/Laguerre term series and an Abel-transformed cumulative-PNT "
            "integral.  The object is the ordered series, not any rearrangement."
        ),
        structural_coordinates=tuple(payload["coordinates"]),
        equivalent_formulations=(
            "existence of the natural-order limit of finite partial sums for one fixed n",
            "vanishing of the Abel endpoint plus convergence of the exact derivative integral",
            "a Dirichlet/Abel convergence problem with cumulative source A(x) and fixed polynomial-log weight",
        ),
        solved_analogues=(
            "finite Abel summation for a C1 weight and its exact cumulative sequence",
            "Dirichlet tests in which cumulative cancellation is estimated before the weight derivative",
        ),
        near_solved_analogues=(
            "prime-number-theorem weighted sums with polynomial functions of log x",
            "conditionally convergent ordered arithmetic series whose transformed integral is absolutely convergent",
        ),
        method_transfers=(transfer,),
        explicit_disanalogies=(
            "fixed-n convergence is not n-uniform tail control",
            "the source-order limit is not an authorization to reorder the series",
            "Bellotti bounds psi(x)-x but does not mention Laguerre weights or Li coefficients",
            "unmerged PR316 and historical R4/R5 proposal branches supply no authority to this atom",
            "a local Abel-interface lemma does not imply a PR316 decay rate, Li positivity, or RH",
            "same-context review is not independent review and computation is not proof",
        ),
        source_anchors=transfer.source_anchors,
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(analogy,),
        analogy_scan_notes=(
            "One order-preserving ledger analogy survives only as a proposal for "
            "the cumulative-state transform; all mathematical authority remains target-specific."
        ),
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash=canonical_hash(payload),
    )


def memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {
        "atom": ATOM,
        "context": context_hash,
        "tools": [],
        "failures": [
            "F-RH-ANA-001-FINITE-LI-PREFIX",
            "F-RH-ANA-002-SUZUKI-NORM-NO-WEAKER-BRIDGE",
        ],
    }
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash="git:58de5548:RH_MAIN_TOOL_SURFACE",
        failure_lattice_snapshot_hash="git:58de5548:RH_MAIN_FAILURE_SURFACE",
        tool_query_status=MemoryQueryStatus.NO_RELEVANT_MATCH,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "finite Abel summation followed by fixed-n limit justification",
            "termwise absolute convergence",
            "series rearrangement or regrouping",
            "uniform-in-n Laguerre tail estimate",
        ),
        relevant_tool_ids=(),
        relevant_failure_ids=tuple(payload["failures"]),
        selected_tool_ids=(),
        tool_applicability_notes=(
            "NO_RELEVANT_MATCH: current canonical RH tool inventory contains no proved fixed-n Abel/Laguerre convergence tool",
        ),
        failure_reuse_notes=(
            "The finite-prefix failure forbids promoting any fixed-n or finite-index statement to all-index Li control.",
            "The Suzuki faithfulness failure warns that a positive or convergent surrogate still needs an exact transport to the root-relevant coordinate.",
        ),
        unresolved_warnings=(
            "The original weighted series may be conditional rather than absolute.",
            "The exact endpoint convention must be checked before taking Y to infinity.",
            "Constants depending on fixed n cannot be promoted to n-uniform bounds.",
            "No content or authority is imported from unmerged PR316 or historical R4/R5 branches.",
            "Same-context review is not independent peer review.",
        ),
        evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:{BASE}/04_candidates/negative_history/RH_ANA_001_FINITE_LI_PREFIX_NO_GO_20260811.md",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/RH_ANA_002_POSTAUDIT_FAILURE_EXPERIENCE_LATTICE_20260811.json",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/02_problem_dag/RH_ANA_003.yaml",
        ),
        artifact_hash=canonical_hash(payload),
    )


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-RH-ABEL001-ORDERED-LIMIT-INTERFACE",
        domain="analytic number theory / real analysis",
        roles=(
            "natural-order increments a_m",
            "cumulative source A(x)",
            "fixed-index Laguerre weight b_n",
            "finite endpoints X and Y",
            "improper natural-order limit",
        ),
        relations=(
            "A(x) is the exact cumulative sum of a_m through floor(x)",
            "finite Abel summation replaces the weighted sum by boundary terms and an integral",
            "Bellotti controls psi(x)-x and hence A(x) after the floor correction",
            "the fixed-n Laguerre factor is a polynomial in log x divided by x",
        ),
        constraints=(
            "n is fixed before the infinite endpoint limit",
            "the original integer order is preserved",
            "finite endpoint terms are retained exactly",
            "no unmerged branch is a theorem source",
        ),
        failure_mechanisms=(
            "termwise absolute values can destroy cumulative prime cancellation",
            "discarding a nonzero endpoint invalidates the infinite identity",
            "an n-dependent constant can be mistaken for a uniform estimate",
        ),
        invariants_to_preserve=(
            "natural source order",
            "exact a_m, A(x), and b_n definitions",
            "fixed-n quantifier order",
            "local-to-root authority boundary",
        ),
        desired_transition=(
            "license a candidate asking whether the exact finite identity extends to a fixed-n natural-order improper identity",
        ),
        forbidden_losses=(
            "series reordering",
            "silent n-uniformity",
            "PR316 rate claims",
            "Li-positivity or RH promotion",
        ),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    target = obstruction()
    source = ObstructionFingerprint(
        obstruction_id="OBS-SOURCE-FINITE-ABEL-SUMMATION",
        domain=target.domain,
        roles=target.roles,
        relations=target.relations,
        constraints=target.constraints,
        failure_mechanisms=target.failure_mechanisms,
        invariants_to_preserve=target.invariants_to_preserve,
        desired_transition=target.desired_transition,
        forbidden_losses=target.forbidden_losses,
    )
    episode = ObstructionTransformationEpisode(
        episode_id="E-CLASSICAL-FINITE-ABEL-SUMMATION",
        source_domain=target.domain,
        source_context="classical finite partial summation / Stieltjes integration by parts",
        source_obstruction=source,
        transformation_name="ORDERED_CUMULATIVE_SUMMATION_BY_PARTS",
        operation=(
            "for finite X<Y, replace sum_{X<m<=Y} a_m b(m) by "
            "A(Y)b(Y)-A(X)b(X)-integral_X^Y A(t)b'(t)dt"
        ),
        preconditions=(
            "A(t)=sum_{m<=t}a_m in the same order",
            "b is continuously differentiable on [X,Y]",
            "the half-open source interval and endpoint convention are fixed",
        ),
        resulting_relations=target.desired_transition,
        preserved_invariants=target.invariants_to_preserve,
        relaxed_or_broken_constraints=(),
        known_breakpoints=(
            "taking Y to infinity without a boundary proof",
            "reordering the original increments",
            "using a different cumulative convention at X or Y",
        ),
        evidence_pointers=("classical Abel summation identity",),
        authority=TransformationEpisodeAuthority.PROOF_BACKED,
        artifact_hash=canonical_hash({"episode": "E-CLASSICAL-FINITE-ABEL-SUMMATION"}),
    )
    tm = build_transformation_memory(
        memory_id="RH-ANA-003-ABEL-001-TRANSFORMATION-MEMORY-20260812",
        source_universe=(
            "classical finite Abel summation",
            "Bellotti arXiv:2508.02041v1 Theorem 1.5 and equations (1.3)-(1.4)",
            "canonical RH-ANA-001/002 failure surfaces on current main",
        ),
        episodes=(episode,),
        evidence_pointers=(
            "https://arxiv.org/html/2508.02041v1#S1.Thmtheorem5",
            PATHS["source_packet"],
        ),
    )
    mapping = StructuralMappingWitness(
        witness_id="MAP-RH-ABEL001-FINITE-TO-FIXED-N",
        episode_id=episode.episode_id,
        target_obstruction_id=target.obstruction_id,
        role_mapping=(
            (target.roles[0], target.roles[0]),
            (target.roles[1], target.roles[1]),
            (target.roles[2], target.roles[2]),
            (target.roles[3], target.roles[3]),
            (target.roles[4], target.roles[4]),
        ),
        shared_relations=target.relations,
        shared_constraints=target.constraints,
        precondition_mapping=(
            (episode.preconditions[0], "use A(t)=floor(t)-psi(t) exactly"),
            (episode.preconditions[1], "differentiate the fixed Laguerre polynomial weight exactly"),
            (episode.preconditions[2], "freeze sum_{X<m<=Y} and integral_X^Y with A(X),A(Y)"),
        ),
        unmatched_source_preconditions=(),
        disanalogies=(
            "the source episode is finite; the target adds an improper endpoint",
            "Bellotti and a fixed-n polynomial bound are still needed for the target limit",
            "the target series may remain non-absolutely convergent",
        ),
        target_validation_obligations=(
            "prove the exact finite endpoint identity",
            "prove A(Y)b_n(Y) tends to zero from Bellotti for fixed n",
            "prove the improper integral of |A(t)b_n'(t)| converges",
            "prove or refute absolute convergence of the original term series",
            "preserve every scope exclusion",
        ),
        evidence_pointers=(PATHS["source_packet"],),
        artifact_hash=canonical_hash({"mapping": "MAP-RH-ABEL001", "context": context_hash}),
    )
    review = ObstructionTransformationReview(
        review_id="RH-ANA-003-ABEL-001-OBSTRUCTION-REVIEW-20260812",
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
        unresolved_warnings=(
            "SEARCH licenses only a candidate freeze, not theorem truth",
            "the infinite endpoint and nonabsolute-convergence claims remain unevaluated",
            "the RH root remains open",
        ),
        evidence_pointers=(PATHS["context"], PATHS["memory"], PATHS["transformation_memory"]),
        artifact_hash=canonical_hash({"review": ATOM, "memory": tm.snapshot_hash}),
    )
    return tm, review


def expert_review_document(context_hash: str) -> dict:
    rows = [
        (
            "domain_theory_lead",
            "The target is an ordered arithmetic series; bind Lambda, psi, Laguerre normalization, fixed n, and the endpoint convention exactly.",
            "Freeze one fixed-n lemma with no all-n or RH conclusion.",
        ),
        (
            "analogy_method_transfer_lead",
            "The ledger analogy preserves order but supplies no boundary decay.",
            "Transfer only the cumulative-state idea and require Bellotti plus target-specific polynomial estimates.",
        ),
        (
            "adversarial_falsification_lead",
            "Attack the endpoint signs, X/Y half-open convention, n=1, and any claim of absolute convergence.",
            "Use a prime-power-free arithmetic subsequence as the cheapest future absolute-convergence falsifier.",
        ),
        (
            "formal_methods_lead",
            "The finite identity, boundary limit, improper integral, and natural-order series existence are four distinct obligations.",
            "Freeze them separately and reject any evaluator that returns a theorem from numerical truncation.",
        ),
        (
            "novelty_research_value_lead",
            "Abel summation and Bellotti's PNT theorem are prior methods; likely value is dependency repair, not new mathematics.",
            "Make no novelty claim and do not import the unmerged PR316 rate.",
        ),
    ]
    return seal(
        {
            "schema_version": "1.0.0",
            "review_id": "RH-ANA-003-ABEL-001-EXPERT-CONTEXT-REVIEW-20260812",
            "atom_id": ATOM,
            "context_hash": context_hash,
            "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
            "role_reviews": [
                {"role": role, "objection": objection, "recommendation": recommendation}
                for role, objection, recommendation in rows
            ],
            "disagreements": [
                "The domain lens expects fixed-n convergence to be elementary after Bellotti; the adversarial lens insists the original series' nonabsolute character and endpoint convention remain separate proof obligations."
            ],
            "strongest_objection": (
                "A correct transformed integral does not authorize a rearranged series, an n-uniform rate, "
                "or an RH-relevant conclusion; all three overclaims must be frozen out."
            ),
            "unresolved_uncertainty": (
                "No target lemma, endpoint proof, or absolute-divergence witness has yet been evaluated in this strict chronology."
            ),
            "next_action_recommendation": (
                "After the full gate passes, freeze the exact fixed-n finite identity, Bellotti boundary obligations, "
                "conditional-not-absolute discriminator, allowed result branches, and an inert evaluator; do not execute it this round."
            ),
            "mathematical_result_credit": False,
            "mathematical_saturation_credit": False,
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
    evidence = {
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
    for index, kind in enumerate(kinds, 1):
        outputs = ["PRE_CANDIDATE_ONLY", "NO_TARGET_EVALUATION", "ZERO_MATHEMATICAL_RESULT_CREDIT"]
        if kind is ResearchTraceEventType.CONTEXT_FROZEN:
            outputs.insert(0, context_hash)
        if kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            outputs.insert(0, memory_hash)
        if kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            outputs[:0] = [shortcut_hash, "selected_mode:SEARCH"]
        payload = {
            "event_id": f"RH-ANA-003-ABEL-001-E{index:02d}",
            "atom_id": ATOM,
            "event_type": kind.value,
            "timestamp": f"2026-08-12T07:23:{10 + index:02d}Z",
            "state_summary": (
                "The active atom is only the fixed-n natural-order Abel convergence interface for "
                "a_m=1-Lambda(m), A=floor-psi, and b_n=Laguerre/log weight. No candidate, proof, "
                "evaluator result, PR316 rate, Li implication, or RH conclusion exists in this chronology."
            ),
            "action_summary": kind.value,
            "evidence_pointers": [evidence[kind]],
            "alternatives_considered": [
                "assume absolute convergence",
                "reorder prime-power and non-prime-power terms",
                "seek an n-uniform PR316-scale estimate",
                "freeze the exact fixed-n finite-to-infinite Abel interface",
            ],
            "decision_rationale": (
                "A source-order finite identity plus Bellotti boundary control is the smallest dependency "
                "repair; it can be falsified without importing any unmerged result branch."
            ),
            "outputs": outputs,
            "uncertainties": [
                "candidate theorem not yet frozen",
                "absolute versus conditional convergence not yet evaluated",
                "same-context review is not independent",
            ],
            "residuals": [
                "exact finite endpoint identity unevaluated",
                "infinite boundary and derivative integral unevaluated",
                "root OPEN_NO_SOLUTION_CERTIFICATE",
            ],
            "next_steps": [
                "only after gate PASS, freeze the exact lemma/proof inputs and inert evaluator",
                "do not execute or prove the candidate this round",
                "preserve exclusions of n-uniformity, reordering, PR316 rates, Li positivity, and RH",
            ],
            "previous_event_hash": previous,
        }
        artifact_hash = canonical_hash(payload)
        entries.append(
            ResearchTraceEntry(
                artifact_hash=artifact_hash,
                **{**payload, "event_type": kind},
            )
        )
        previous = artifact_hash
    return MathResearchTrace(
        "RH-ANA-003-ABEL-001-PRE-CANDIDATE-TRACE-20260812",
        tuple(entries),
    )


def preservation_receipt() -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id="RH-ANA-003-ABEL-001-ROOT-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="every nontrivial zero of zeta has real part one half",
        surrogate_coordinate="fixed-n natural-order convergence of one prime/Laguerre weighted series",
        bridge_edges=(
            BridgeEdge(
                "RH-ABEL-B1",
                "fixed-n ordered Abel identity",
                "exact full Li-coefficient arithmetic identity",
                "requires source-normalization and archimedean/gluing terms not proved here",
                EdgeProofStatus.UNPROVED,
                ("exact Coffey/Bombieri-Lagarias normalization", "all remaining terms"),
            ),
            BridgeEdge(
                "RH-ABEL-B2",
                "exact Li arithmetic identity",
                "all-index Li positivity",
                "requires sign control for every n, not mere convergence",
                EdgeProofStatus.UNPROVED,
                ("all-index uniformity", "one-sided sign control"),
            ),
            BridgeEdge(
                "RH-ABEL-B3",
                "all-index Li positivity",
                "Riemann Hypothesis",
                "requires exact Li criterion hypotheses and complete proof",
                EdgeProofStatus.UNPROVED,
                ("Li criterion", "root contract"),
            ),
        ),
        obligations=(
            Obligation("RH-ABEL-O1", "prove the fixed-n natural-order Abel identity", True, False),
            Obligation("RH-ABEL-O2", "bind it to the exact full Li decomposition", True, False),
            Obligation("RH-ABEL-O3", "prove all-index sign control", True, False),
        ),
        known_disanalogies=(
            "convergence is not positivity",
            "fixed n is not uniform in n",
            "a local arithmetic term is not the full Li coefficient",
        ),
        source_authority=CoordinateAuthority.PROPOSAL_ONLY,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world=(
            "the fixed-n series converges exactly but the full Li ledger still has an uncontrolled negative coordinate"
        ),
        registered_observations=(
            RegisteredStateObservation("RH-main", "RH-ANA-003 context required", "root open"),
            RegisteredStateObservation("ABEL001-pre", "candidate absent", "root open"),
        ),
        reverification_triggers=(
            "normalization changes",
            "n is allowed to vary with the endpoint",
            "the term order changes",
            "a Li or RH implication is asserted",
        ),
        prior_failure_ids=(
            "F-RH-ANA-001-FINITE-LI-PREFIX",
            "F-RH-ANA-002-SUZUKI-NORM-NO-WEAKER-BRIDGE",
        ),
    )


def framework_subject(context_hash: str):
    binding = FrameworkSubjectFreezeBinding(
        binding_id="RH-ANA-003-ABEL-001-FRAMEWORK-SUBJECT-FREEZE-20260812",
        authoritative_framework_sha=FRAMEWORK_CURRENT_SHA,
        pre_candidate_packet_hash=context_hash.removeprefix("sha256:"),
        frozen_at_utc=FROZEN_AT,
        evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:config/rakl-framework-pin.json@{FRAMEWORK_PIN_SHA}",
            f"git:{FRAMEWORK_CURRENT_SHA}:skills/rakl-core/workflows/mathematical-research.md",
            f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/math_research_runtime.py",
            "protected-surface diff 5dc0627..44058e2 observed empty before freeze",
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=FRAMEWORK_CURRENT_SHA,
        intervening_diff=(),
        observation_evidence_pointers=(
            f"git:{FRAMEWORK_CURRENT_SHA}:RAKL_VERSION.json",
            "git diff 5dc0627..44058e2 over skills/rakl-core, src/rakl math gates, method_specs, and schemas: empty",
        ),
    )
    return binding, observation


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
                "a_m=1-Lambda(m)",
                "A(x)=floor(x)-psi(x)",
                "b_n(x)=L_{n-1}^{(1)}(log x)/x",
                "natural-order partial sums",
            ),
            relations=(
                "cumulative source identity",
                "finite Abel summation",
                "boundary limit",
                "improper derivative integral",
            ),
            domain="analytic number theory / fixed-index real analysis",
            goal_type=(
                "license only a prospective fixed-n Abel-interface candidate/proof-input freeze"
            ),
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
    return seal(
        {
            "schema_version": "1.0.0",
            "packet_id": "RH-ANA-003-ABEL-001-SOURCE-PACKET-20260812",
            "atom_id": ATOM,
            "retrieved_before_candidate": True,
            "sources": [
                {
                    "id": "BELLOTTI-ARXIV-2508.02041v1",
                    "url": "https://arxiv.org/html/2508.02041v1",
                    "retrieved_html_sha256": BELLOTTI_HTML_SHA256,
                    "theorem": "Theorem 1.5",
                    "quoted_input": "Delta(x) << exp(55 A_0) exp(-omega(x))",
                    "equation_1_3": "Delta(x)=|psi(x)-x|/x",
                    "equation_1_4": (
                        "omega(x)=d (log x)^(3/5)/(log log x)^(1/5), "
                        "d=(5^6 A_0^3/(2^2*3^4))^(1/5)"
                    ),
                    "authorized_use": (
                        "prospective sufficient source for fixed-n Abel boundary and integral estimates"
                    ),
                    "non_guarantees": [
                        "does not state the target Laguerre identity",
                        "does not provide n-uniformity",
                        "does not imply Li positivity or RH",
                    ],
                },
                {
                    "id": "CLASSICAL-FINITE-ABEL-SUMMATION",
                    "statement_scope": (
                        "finite ordered sequence, exact cumulative sum, C1 weight, exact endpoints"
                    ),
                    "authorized_use": "method-transfer source only; target endpoint identity must be derived",
                },
            ],
            "excluded_authority": [
                "unmerged PR316",
                "historical R4 proposal/shadow branch",
                "historical R5 proposal/shadow branch",
            ],
            "authority": "PRIMARY_SOURCE_PACKET_AND_STANDARD_METHOD_CONTEXT_ONLY_NO_TARGET_RESULT",
            "mathematical_result_credit": False,
        }
    )


def build_documents() -> dict[str, dict]:
    plan, fiber, memory, tm, shortcut, research_trace, preservation = build_current_gate_plan()
    source_packet = source_packet_document()
    atomization = seal(
        {
            "schema_version": "1.0.0",
            "atomization_id": "RH-ANA-003-ABEL-001-ATOMIZATION-20260812",
            "recorded_at": FROZEN_AT,
            "atom_id": ATOM,
            "parent_atom_id": PARENT_ATOM,
            "object": (
                "The fixed-n natural-order convergence interface for the arithmetic increments "
                "a_m=1-Lambda(m) weighted by b_n(m)=L_{n-1}^{(1)}(log m)/m."
            ),
            "qoi": "FIXED_N_NATURAL_ORDER_ABEL_IDENTITY_TRUTH_STATUS",
            "allowed_future_result_branches": [
                "PROVED_FIXED_N_NATURAL_ORDER_IDENTITY",
                "FINITE_ENDPOINT_IDENTITY_FALSE",
                "BELLOTTI_BOUNDARY_OR_INTEGRAL_INSUFFICIENT",
                "ABSOLUTE_DIVERGENCE_WITNESS_FALSE",
                "CANNOT_CHECK",
            ],
            "atomic_obligations": [
                "freeze n before every endpoint limit",
                "derive the exact finite half-open endpoint identity",
                "derive b_n' exactly",
                "use Bellotti v1 only to control A=floor-psi at infinity",
                "separate natural-order convergence from absolute convergence",
                "preserve all local-to-root exclusions",
            ],
            "candidate_generation_allowed": False,
            "candidate_proposed": False,
            "target_result_accessed": False,
            "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
            "authority_boundary": {
                "grants_fixed_n_lemma_truth": False,
                "grants_n_uniformity": False,
                "grants_li_positivity": False,
                "grants_rh_authority": False,
                "operational_metadata_zero_mathematical_credit": True,
            },
        }
    )
    tool_snapshot = seal(
        {
            "schema_version": "1.0.0",
            "snapshot_id": "RH-ANA-003-ABEL-001-TOOL-SNAPSHOT-20260812",
            "target_atom_id": ATOM,
            "application_base_commit": APPLICATION_BASE_SHA,
            "query_result": "NO_RELEVANT_MATCH",
            "tools": [],
            "warning": "No canonical current-main tool proves this target interface.",
            "mathematical_credit": False,
        }
    )
    failure_snapshot = seal(
        {
            "schema_version": "1.0.0",
            "snapshot_id": "RH-ANA-003-ABEL-001-FAILURE-SNAPSHOT-20260812",
            "target_atom_id": ATOM,
            "failures": [
                {
                    "failure_id": "F-RH-ANA-001-FINITE-LI-PREFIX",
                    "warning": "fixed or finite index information has no all-index authority without a separate uniform bridge",
                },
                {
                    "failure_id": "F-RH-ANA-002-SUZUKI-NORM-NO-WEAKER-BRIDGE",
                    "warning": "a well-defined positive surrogate does not transport to Li without a faithful unconditional bridge",
                },
            ],
            "difference_witness": {
                "changed_question": "convergence of one exact ordered arithmetic series rather than root positivity",
                "restored_assumption": "the target is explicitly local and makes no surrogate-to-root claim",
                "cheapest_repeat_failure_test": "attempt any n-uniform or Li implication and reject it unless a new exact bridge is supplied",
            },
            "mathematical_credit": False,
        }
    )
    expert = expert_review_document(fiber.packet_hash)
    binding, observation = framework_subject(fiber.packet_hash)
    binding_document = seal(dict(binding.document()))
    observation_document = seal(
        {
            "schema_version": "framework-subject-revalidation-observation-v1",
            "observation_id": "RH-ANA-003-ABEL-001-FRAMEWORK-REVALIDATION-20260812",
            "observed_current_main_sha": observation.observed_current_main_sha,
            "intervening_diff": [],
            "observation_evidence_pointers": list(observation.observation_evidence_pointers),
            "verdict": plan.framework_subject_gate.verdict.value,
            "licenses_candidate_materialization": plan.framework_subject_gate.licenses_candidate_materialization,
            "protected_surface_equal_to_application_pin": True,
            "grants_scientific_authority": False,
        }
    )
    documents = {
        "source_packet": source_packet,
        "atomization": atomization,
        "context": _document(fiber),
        "tool_snapshot": tool_snapshot,
        "failure_snapshot": failure_snapshot,
        "memory": _document(memory),
        "transformation_memory": _document(tm),
        "expert_review": expert,
        "shortcut_review": _document(shortcut),
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
    documents["gate"] = seal(
        {
            "schema_version": "1.0.0",
            "receipt_id": "RH-ANA-003-ABEL-001-PRE-CANDIDATE-GATE-20260812",
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
                "preservation_sha256": preservation.document()["receipt_canonical_sha256"],
                "framework_subject_binding_sha256": binding.binding_canonical_sha256,
                "full_document_integrity_hash": canonical_hash(integrity),
            },
            "full_document_integrity": integrity,
            "gate_verdicts": {
                "context": plan.context_gate.verdict.value,
                "dual_memory": plan.memory_gate.verdict.value,
                "obstruction_transformation": plan.shortcut_gate.verdict.value,
                "trace": plan.trace_gate.verdict.value,
                "preservation": plan.preservation_gate.verdict.value,
                "framework_subject": plan.framework_subject_gate.verdict.value,
                "selected_mode": shortcut.selected_mode.value,
                "candidate_generation_allowed": plan.candidate_generation_allowed,
                "licensed_action": "FREEZE_FIXED_N_ABEL_CANDIDATE_PROOF_INPUTS_AND_INERT_EVALUATOR_ONLY",
            },
            "chronology": {
                "candidate_identity": None,
                "candidate_proposed": False,
                "target_result_accessed": False,
                "evaluator_executed": False,
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
        }
    )
    return documents


def write_documents(root: Path = Path(".")) -> None:
    for name, document in build_documents().items():
        path = root / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    write_documents()
