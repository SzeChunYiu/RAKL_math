"""Strict pre-candidate packet for RH-ANA-003i.

This module classifies bounded method families and freezes the first discriminator.
It intentionally contains no mathematical candidate, target estimate, or evaluator.
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


ATOM = "RH-ANA-003i"
PARENT = "RH-ANA-003"
APPLICATION_BASE_SHA = "c5ebefad369a737f458ea1528cb6bfa9989b7265"
FRAMEWORK_PIN_SHA = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
FRAMEWORK_CURRENT_SHA = "e58b3b338c896487c37dfe2069c022e73cf9a974"
FROZEN_AT = "2026-08-12T09:05:00Z"
BASE = "research/real_math/millennium/riemann_hypothesis"

PATHS = {
    "source_packet": f"{BASE}/01_frontier/RH_ANA_003i_SOURCE_METHOD_TRANSFER_PACKET_20260812.json",
    "atomization": f"{BASE}/02_problem_dag/RH_ANA_003i_ATOMIZATION_20260812.json",
    "context": f"{BASE}/01_frontier/RH_ANA_003i_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/RH_ANA_003i_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/RH_ANA_003i_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/RH_ANA_003i_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/RH_ANA_003i_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/RH_ANA_003i_SEVEN_ROLE_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/RH_ANA_003i_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": f"{BASE}/09_trace/RH_ANA_003i_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003i_PRE_CANDIDATE_TRACE_20260812.json",
    "framework_binding": f"{BASE}/09_trace/RH_ANA_003i_FRAMEWORK_SUBJECT_FREEZE_20260812.json",
    "framework_observation": f"{BASE}/09_trace/RH_ANA_003i_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "gate": f"{BASE}/09_trace/RH_ANA_003i_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
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
            source_context="certified approximation and feasible-set projection",
            method=(
                "classify an internal constraint by the exact set of cutoff endpoints it permits, "
                "then test whether the endpoint projection is already the target one-sided obligation"
            ),
            shared_structure=(
                "an ordered internal record determines a cutoff endpoint",
                "a complement joins that endpoint to the exact target",
                "the claimed weakening is meaningful only if the feasible target set is strictly larger",
            ),
            required_assumptions=(
                "the constraint is defined on the actual arithmetic array",
                "its exact implication for the cutoff endpoint is derived before estimation",
                "the same natural-order complement and target scale are used",
            ),
            disanalogies=(
                "generic feasible paths are freely chosen whereas the von-Mangoldt/Laguerre path is fixed",
                "set-theoretic strictness in an ambient path class is not arithmetic attainability",
                "a small complement can collapse an apparently internal constraint back to endpoint control",
            ),
            repair_question=(
                "Does any source-defined family survive endpoint-projection and arithmetic-realization tests "
                "without containing, dominating, or reconstructing the running extremum or cutoff endpoint?"
            ),
            source_anchors=(
                "SzeChunYiu/RAKL_math issue #324",
                "draft PR #320@022da37dbdb9ae5d60e7877ac2cb7b7f6f8426c8 (proposal-only)",
            ),
        ),
        MethodTransfer(
            source_context="exact natural-order Abel complement and finite-degree Laguerre outer bound",
            method=(
                "preserve the proved fixed-index source-order limit and separately type the moving-index "
                "outer-complement estimate as shadow evidence before any internal-family search"
            ),
            shared_structure=(
                "same coefficients (1-Lambda(m)) L_{n-1}^{(1)}(log m)/m",
                "same natural integer order",
                "same cutoff log Y of order n^(5/3) log^2(n+e)",
            ),
            required_assumptions=(
                "C002 supplies fixed-n convergence only",
                "the moving-index complement rate remains proposal-only unless separately proved",
                "no regrouping or reordering is used",
            ),
            disanalogies=(
                "fixed-n convergence gives no moving-n rate",
                "outer-complement control gives no internal prefix control",
                "a source-order decomposition supplies no strict-weaker witness",
            ),
            repair_question=(
                "At the frozen moving cutoff, can internal-family applicability be decided before using "
                "any unproved complement rate, and can all complement premises be shown strictly weaker?"
            ),
            source_anchors=(
                f"git:{APPLICATION_BASE_SHA}:{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json",
                "draft PR #316@13062780d022c43395ed36d78e276c837bfb4352 (proposal-only)",
            ),
        ),
    )
    analogies = (
        CrossDomainAnalogy(
            source_kind="engineering safety certificate",
            source_situation=(
                "A monitor summarizes an internal trajectory while a certified error bar joins its final "
                "reading to a terminal safety quantity"
            ),
            common_abstraction=(
                "internal record",
                "terminal projection",
                "certified complement",
                "one-sided decision",
            ),
            source_to_target_mapping=(
                "internal record -> natural-order prefix array",
                "monitor constraint -> unnamed internal family",
                "final reading -> R_n(Y_n)",
                "error bar -> D_n(Y_n)",
                "terminal safety quantity -> S_n",
            ),
            shared_constraints=(
                "the complement is not optional",
                "the decision is one-sided",
                "a summary must be realized by the actual system",
            ),
            disanalogies=(
                "engineering trajectories may be designed or sampled; the arithmetic trajectory is fixed",
                "a safety analogy supplies no number-theoretic bound or target-domain witness",
            ),
            proposed_principle=(
                "project every proposed internal constraint to the terminal decision before estimating it"
            ),
            validation_obligation=(
                "derive its exact relation to R_n(Y_n), S_n, and D_n(Y_n), then reject endpoint reconstruction"
            ),
            provenance_note="proposal-only ordinary/engineering analogy; zero theorem authority",
        ),
        CrossDomainAnalogy(
            source_kind="game reachability / admissible-state invariant",
            source_situation=(
                "A game invariant is useful only when reachable legal positions satisfy it and its terminal "
                "projection does not simply encode winning"
            ),
            common_abstraction=("legal states", "reachability", "internal invariant", "terminal objective"),
            source_to_target_mapping=(
                "legal position -> actual von-Mangoldt/Laguerre prefix",
                "reachability -> arithmetic attainability",
                "terminal objective -> one-sided endpoint obligation",
            ),
            shared_constraints=(
                "ambient states outside the legal dynamics do not witness target strictness",
                "terminal equivalence must be rejected before local optimization",
            ),
            disanalogies=(
                "there is no move generator for alternative zeta coefficient paths",
                "the analogy cannot establish arithmetic realizability or an estimate",
            ),
            proposed_principle="test target-domain attainability before treating an ambient witness as evidence",
            validation_obligation=(
                "supply a TARGET_DOMAIN or TRANSFERRED_WITH_WITNESS realization record for any retained family"
            ),
            provenance_note="proposal-only game analogy; zero theorem authority",
        ),
    )
    payload = {
        "atom": ATOM,
        "base": APPLICATION_BASE_SHA,
        "coordinates": [
            "x_{n,m}=((1-Lambda(m))/m)L_{n-1}^{(1)}(log m) in natural integer order",
            "R_n(M)=sum_{2<=m<=M}x_{n,m}",
            "2<=M<=Y_n and Y_n=exp(C n^(5/3) log^2(n+e))",
            "S_n=S_{2Lambda}(n) and D_n(Y_n)=|S_n-R_n(Y_n)|",
            "non-extremal internal-family classification before any estimate",
            "target-domain realization and strict-premise comparison",
        ],
    }
    return MathContextFiber(
        atom_id=ATOM,
        object_context=(
            "The actual zeta-domain triangular array x_{n,m}=((1-Lambda(m))/m)"
            "L_{n-1}^{(1)}(log m), its natural-order prefixes R_n(M) through the frozen moving "
            "cutoff Y_n=exp(C n^(5/3) log^2(n+e)), the exact target S_n=S_{2Lambda}(n), "
            "and the natural-order complement D_n(Y_n)."
        ),
        structural_coordinates=tuple(payload["coordinates"]),
        equivalent_formulations=(
            "classify source-bound feasible sets by their exact projection onto R_n(Y_n)",
            "test whether an internal constraint plus D_n control reconstructs one-sided S_n control",
            "separate ambient path non-identification from fixed-zeta arithmetic attainability",
            "decide whether a bounded family search survives before any moving-prefix estimate",
        ),
        solved_analogues=(
            "deterministic certified-error transfer from a cutoff value to a terminal value",
            "finite ordered decompositions with an explicit suffix/complement",
        ),
        near_solved_analogues=(
            "R7 strict-cut excursion with explicit suffix and representation-only path witness",
            "R8 effective-endpoint dichotomy for running negative excursion plus complement",
            "R9 proposal-only outer-complement scale reduction leaving strict-prefix attainability open",
        ),
        method_transfers=transfers,
        explicit_disanalogies=(
            "C002 fixed-n convergence is not a moving-n complement rate or prefix bound",
            "PR #316 and PR #320 are proposal/shadow evidence, not theorem authority",
            "a non-extremal label alone does not make an obligation weaker",
            "moments, block constraints, occupancy constraints, and feasible sets may still encode the endpoint",
            "ambient signed paths are not alternative von-Mangoldt realizations",
            "natural order forbids infinite reordering or independent regrouping",
            "same-context expert roles provide zero independent-review credit",
        ),
        source_anchors=tuple(anchor for transfer in transfers for anchor in transfer.source_anchors),
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=analogies,
        analogy_scan_notes=(
            "Two structural analogies survive only as search-control proposals; neither supplies arithmetic authority."
        ),
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash=canonical_hash(payload),
    )


FAILURES = (
    "F-RH-ANA-003g-COMPLEMENT-FIRST-WEAKENING-FAIL",
    "F-RH-ANA-003g-AMBIENT-WITNESS-CURRENT-V3-REPRESENTATION-ONLY",
    "F-RH-ANA-003f-STRICT-CUT-SUFFIX-GLUE",
    "F-RH-ANA-003f-PATH-WITNESS-NOT-ARITHMETIC",
    "F-RH-ANA-003e-MOVING-PREFIX-POLYBOUND-NOT-WEAKER",
    "F-RH-ANA-003c-UNWITNESSED-WINDOW-GLUE",
    "R9-STRICT-PREFIX-ARITHMETIC-ATTAINABILITY-OBSTRUCTION",
)


def memory_review(context_hash: str) -> ResearchMemoryReview:
    payload = {"atom": ATOM, "context": context_hash, "failures": FAILURES}
    return ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash=f"git:{APPLICATION_BASE_SHA}:RH_C002_AND_GLOBAL_TOOL_SURFACES",
        failure_lattice_snapshot_hash=(
            "shadow:022da37dbdb9ae5d60e7877ac2cb7b7f6f8426c8+"
            "13062780d022c43395ed36d78e276c837bfb4352"
        ),
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "source-defined moment or distributional feasible-set constraints",
            "ordered block occupancy, energy, or multiscale balance constraints",
            "support-aware constraints using the actual von-Mangoldt/Laguerre array",
            "transform-domain internal constraints with exact inverse endpoint accounting",
            "running extrema and endpoint-dominating controls as negative controls only",
            "mollifier/resonance as a separately frozen rotation, not part of this family",
        ),
        relevant_tool_ids=("T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY",),
        relevant_failure_ids=FAILURES,
        selected_tool_ids=("T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY",),
        tool_applicability_notes=(
            "Applicable only to preserve existence and natural-order complement semantics for each fixed n.",
            "Not applicable to moving-n rates, internal-family control, Li positivity, or arithmetic attainability.",
        ),
        failure_reuse_notes=(
            "R7/R8 reject running-extremum and ambient-witness routes unless exact target-domain realization survives.",
            "R4/R7 require the exact natural-order suffix/complement to remain explicit.",
            "R6/R8 warn that a small complement may reconstruct endpoint strength rather than weaken it.",
            "R9 shadow evidence changes the proposed cutoff scale but leaves the strict-prefix arithmetic burden open.",
        ),
        unresolved_warnings=(
            "No source-defined non-extremal family has yet survived the endpoint-projection test.",
            "No TARGET_DOMAIN realization witness has yet been supplied.",
            "The PR #316 moving-complement rate and PR #320 dichotomy are shadow evidence only.",
            "SEARCH, JUMP, and GLUE remain unexhausted; LIFT is forbidden in this round.",
            "If bounded family search yields no survivor, rotate to a separately frozen mollifier/resonance context.",
        ),
        evidence_pointers=(
            "https://github.com/SzeChunYiu/RAKL_math/issues/324",
            "https://github.com/SzeChunYiu/RAKL_math/issues/315",
            "https://github.com/SzeChunYiu/RAKL_math/issues/265",
            "https://github.com/SzeChunYiu/RAKL_math/pull/320",
            "https://github.com/SzeChunYiu/RAKL_math/pull/316",
            f"git:{APPLICATION_BASE_SHA}:{BASE}/07_memory/RH_ANA_003_ABEL_001_C002_SCOPED_MATHEMATICAL_LESSON_20260812.json",
        ),
        artifact_hash=canonical_hash(payload),
    )


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-RH-ANA-003i-NONEXTREMAL-TARGET-REALIZATION",
        domain="analytic number theory / ordered arithmetic transforms",
        roles=(
            "actual natural-order coefficient array",
            "unnamed non-extremal internal-family constraint",
            "cutoff endpoint R_n(Y_n)",
            "exact target S_n",
            "natural-order complement D_n(Y_n)",
            "one-sided endpoint decision scale",
        ),
        relations=(
            "the internal family is evaluated only on 2<=M<=Y_n",
            "R_n(Y_n) is the final member of the same natural-order prefix",
            "D_n(Y_n)=|S_n-R_n(Y_n)| glues cutoff to target",
            "strict weakening requires premises and feasible target projection weaker than endpoint control",
        ),
        constraints=(
            "exact Coffey normalization",
            "natural source order without regrouping",
            "moving cutoff log Y_n=C n^(5/3) log^2(n+e)",
            "target-domain arithmetic realization",
            "no candidate object in this round",
        ),
        failure_mechanisms=(
            "internal constraint contains or dominates the cutoff endpoint",
            "constraint plus complement reconstructs the Q+D endpoint mechanism",
            "ambient witness is not attainable by the fixed arithmetic array",
            "premises silently import a root-sensitive endpoint obligation",
        ),
        invariants_to_preserve=(
            "exact x_{n,m}, R_n, S_n, D_n definitions",
            "natural order",
            "fixed source and shadow authority levels",
            "OPEN_NO_SOLUTION_CERTIFICATE",
        ),
        desired_transition=(
            "identify a source-bound internal-family class that survives endpoint projection, arithmetic realization, exact complement gluing, and strict-premise comparison",
        ),
        forbidden_losses=(
            "reordering or regrouping",
            "ambient-path-only attainability",
            "endpoint reconstruction",
            "shadow-to-theorem promotion",
            "candidate generation before the family discriminator",
            "LIFT without SEARCH/JUMP/GLUE exhaustion",
        ),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    target = obstruction()
    episodes = (
        ObstructionTransformationEpisode(
            episode_id="E-RH-R8-EFFECTIVE-ENDPOINT-AUDIT-SHADOW",
            source_domain=target.domain,
            source_context="draft PR #320 effective-endpoint dichotomy",
            source_obstruction=target,
            transformation_name="PROJECT_INTERNAL_CONTROL_TO_ENDPOINT_BEFORE_ESTIMATION",
            operation="test an internal control together with its exact complement against endpoint downside",
            preconditions=(
                "running-extremum family is fixed",
                "exact cutoff target and complement are fixed",
                "shadow authority is retained",
            ),
            resulting_relations=(
                "running-extremum plus complement controls one-sided endpoint downside",
            ),
            preserved_invariants=target.invariants_to_preserve,
            relaxed_or_broken_constraints=(),
            known_breakpoints=(
                "does not classify non-extremal families",
                "does not provide target-domain strictness",
                "source episode is proposal-only",
            ),
            evidence_pointers=("draft PR #320@022da37dbdb9ae5d60e7877ac2cb7b7f6f8426c8",),
            authority=TransformationEpisodeAuthority.PROPOSAL_ONLY,
            artifact_hash=canonical_hash({"episode": "R8-effective-endpoint-shadow"}),
        ),
        ObstructionTransformationEpisode(
            episode_id="E-RH-R9-OUTER-COMPLEMENT-SCALE-SHADOW",
            source_domain=target.domain,
            source_context="draft PR #316 finite-degree Laguerre outer majorant",
            source_obstruction=target,
            transformation_name="SHARPEN_OUTER_REPRESENTATION_BEFORE_ARITHMETIC_INPUT",
            operation="replace a crude envelope by exact finite-degree coefficient accounting",
            preconditions=(
                "R5 shadow Abel/PNT premise",
                "exact generalized Laguerre finite sum",
                "moving outer-complement question only",
            ),
            resulting_relations=("proposal-only smaller sufficient outer-complement cutoff",),
            preserved_invariants=target.invariants_to_preserve,
            relaxed_or_broken_constraints=(),
            known_breakpoints=(
                "controls the outer complement rather than the internal prefix",
                "does not supply arithmetic attainability or strict weakening",
                "source episode is proposal-only",
            ),
            evidence_pointers=("draft PR #316@13062780d022c43395ed36d78e276c837bfb4352",),
            authority=TransformationEpisodeAuthority.PROPOSAL_ONLY,
            artifact_hash=canonical_hash({"episode": "R9-outer-complement-shadow"}),
        ),
        ObstructionTransformationEpisode(
            episode_id="E-CROSSDOMAIN-LEGAL-STATE-REALIZATION-PROPOSAL",
            source_domain="games / reachability",
            source_context="legal-state reachability versus ambient-state counterexample",
            source_obstruction=target,
            transformation_name="REQUIRE_REACHABILITY_BEFORE_DIFFERENCE_WITNESS",
            operation="discard hostile states not reachable under the actual system rules",
            preconditions=(
                "a complete legal move system exists",
                "reachability is decidable or witnessed",
                "terminal projection is explicit",
            ),
            resulting_relations=("proposal to require target-domain realization before strictness credit",),
            preserved_invariants=target.invariants_to_preserve,
            relaxed_or_broken_constraints=(),
            known_breakpoints=(
                "no legal-move generator exists for alternative zeta paths",
                "analogy supplies no arithmetic realization theorem",
            ),
            evidence_pointers=(PATHS["context"],),
            authority=TransformationEpisodeAuthority.PROPOSAL_ONLY,
            artifact_hash=canonical_hash({"episode": "legal-state-proposal"}),
        ),
    )
    tm = build_transformation_memory(
        memory_id="RH-ANA-003i-TRANSFORMATION-MEMORY-20260812",
        source_universe=(
            "merged RH C002 fixed-n natural-order proof surface",
            "draft PR #320 R8 proposal/shadow episode",
            "draft PR #316 R9 proposal/shadow episode",
            "issues #265, #315, and #324",
            "bounded engineering/game analogy scan recorded in the context fiber",
        ),
        episodes=episodes,
        evidence_pointers=(PATHS["memory"], PATHS["source_packet"]),
    )
    review = ObstructionTransformationReview(
        review_id="RH-ANA-003i-OBSTRUCTION-REVIEW-20260812",
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
            "All retrieved episodes are proposal-only or incomplete for the desired transition.",
            "SEARCH has method families to test but no witnessed viable transformation yet.",
            "JUMP and GLUE are not exhausted and therefore LIFT is not authorized.",
            "No bounded cross-problem coverage receipt supports a recorded-knowledge no-match claim.",
            "The only licensed action is the frozen family discriminator; no candidate may be generated.",
        ),
        evidence_pointers=(
            PATHS["source_packet"],
            PATHS["memory"],
            "https://github.com/SzeChunYiu/RAKL_math/issues/324",
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
        receipt_id="RH-ANA-003i-ROOT-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="every nontrivial zero of zeta has real part one half",
        surrogate_coordinate="source-bound internal-prefix family at a moving natural-order cutoff",
        bridge_edges=(
            BridgeEdge(
                "RH003i-B1",
                "internal-family bound",
                "cutoff endpoint downside",
                "must not be assumed; exact family-specific projection is the first discriminator",
                EdgeProofStatus.UNPROVED,
                ("family definition", "endpoint-projection proof", "target-domain realization"),
            ),
            BridgeEdge(
                "RH003i-B2",
                "cutoff endpoint downside",
                "exact S_n downside",
                "requires the exact natural-order complement at the same moving scale",
                EdgeProofStatus.UNPROVED,
                ("moving-n complement theorem", "premise-strength audit"),
            ),
            BridgeEdge(
                "RH003i-B3",
                "S_n downside",
                "Li positivity and RH",
                "requires the complete Coffey/Li ledger and all-index one-sided implication",
                EdgeProofStatus.UNPROVED,
                ("archimedean ledger", "all-index sign bridge", "Li criterion"),
            ),
        ),
        obligations=(
            Obligation("RH003i-O1", "classify internal-family endpoint projection", True, False),
            Obligation("RH003i-O2", "prove target-domain realization", True, False),
            Obligation("RH003i-O3", "prove exact moving-scale complement from weaker premises", True, False),
        ),
        known_disanalogies=(
            "ambient path strictness is not arithmetic attainability",
            "fixed-n convergence is not moving-n control",
            "internal-family control is not Li positivity",
        ),
        source_authority=CoordinateAuthority.PROPOSAL_ONLY,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world=(
            "an internal constraint holds but either fixes the endpoint already or permits no actual arithmetic realization"
        ),
        registered_observations=(
            RegisteredStateObservation("C002", "fixed-n natural-order identity proved", "moving prefix open"),
            RegisteredStateObservation("RH003i-pre", "candidate absent", "root open"),
        ),
        reverification_triggers=(
            "family definition changes",
            "cutoff scale changes",
            "summation order changes",
            "a Li or RH implication is asserted",
        ),
        prior_failure_ids=FAILURES,
    )


def framework_subject(context_hash: str):
    binding = FrameworkSubjectFreezeBinding(
        binding_id="RH-ANA-003i-FRAMEWORK-SUBJECT-FREEZE-20260812",
        authoritative_framework_sha=FRAMEWORK_CURRENT_SHA,
        pre_candidate_packet_hash=context_hash.removeprefix("sha256:"),
        frozen_at_utc=FROZEN_AT,
        evidence_pointers=(
            f"git:{FRAMEWORK_CURRENT_SHA}:RAKL_VERSION.json",
            f"git:{FRAMEWORK_CURRENT_SHA}:skills/rakl-core/workflows/mathematical-research.md",
            f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/math_research_runtime.py",
            f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/semantic_shortcut.py",
            f"git:{FRAMEWORK_PIN_SHA}:config/rakl-framework-pin.json",
            "protected mathematical workflow/runtime/API/gate/schema diff from pin to current main is empty",
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=FRAMEWORK_CURRENT_SHA,
        intervening_diff=(),
        observation_evidence_pointers=(
            f"git:{FRAMEWORK_CURRENT_SHA}:RAKL_VERSION.json",
            "protected-surface comparison performed before packet materialization",
        ),
    )
    return binding, observation


def expert_review_document(context_hash: str) -> dict:
    roles = [
        ("analytic_number_theory_domain_lead", "Exact Coffey normalization and the proved fixed-n natural-order boundary must be separated from moving-n control.", "Keep C002 as the only merged theorem premise and reject silent Li-ledger completion."),
        ("laguerre_uniform_asymptotics_lead", "The n^(5/3) log^2 scale comes from proposal-only R9 evidence, not current theorem authority.", "Use it only as a frozen search scale and require any rate premise to be re-proved."),
        ("summation_gluing_lead", "Conditional convergence makes source order and the exact complement load-bearing.", "Reject reordering, regrouping, or deletion of the suffix."),
        ("target_domain_transfer_applicability_lead", "Ambient feasible paths cannot witness what the fixed arithmetic array realizes.", "Require target-domain or fully witnessed transfer realization before retention."),
        ("adversarial_falsification_lead", "A non-extremal name can still algebraically encode the endpoint or running extremum.", "Project every family to R_n(Y_n), S_n, and D_n before estimating."),
        ("formal_methods_dependency_lead", "Family definition, endpoint projection, realization, complement, and premise strength are distinct obligations.", "Freeze the discriminator and preserve CANNOT_CHECK rather than backfill a candidate."),
        ("novelty_research_value_lead", "The literature and shadow branches do not yet exhibit a surviving source-bound family.", "Make no novelty claim; rotate only after bounded search is recorded."),
    ]
    return seal({
        "schema_version": "1.0.0",
        "review_id": "RH-ANA-003i-SEVEN-ROLE-EXPERT-CONTEXT-REVIEW-20260812",
        "atom_id": ATOM,
        "context_hash": context_hash,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT",
        "role_reviews": [
            {"role": role, "objection": objection, "recommendation": recommendation}
            for role, objection, recommendation in roles
        ],
        "disagreements": [
            "The asymptotics lens retains the R9 scale as useful shadow guidance; the formal and domain lenses deny it premise authority.",
            "The transfer lens allows family taxonomies; the adversarial lens refuses any retained family until endpoint projection and realization are explicit.",
        ],
        "strongest_objection": (
            "No currently bound source supplies an actual target-domain non-extremal family with a strict-premise witness."
        ),
        "unresolved_uncertainty": [
            "whether any bounded source-defined family survives",
            "whether the moving complement rate can be proved from strictly weaker premises",
            "whether a source-bound family exists outside the screened taxonomies",
        ],
        "next_action_recommendation": (
            "Execute only the family-level endpoint-projection/realization/premise-strength discriminator; "
            "if no family survives, freeze a separate mollifier/resonance context."
        ),
        "independent_review_credit": 0,
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
        ResearchTraceEventType.NEXT_STEP_PROPOSED: PATHS["gate"],
    }
    entries = []
    previous = ""
    for index, kind in enumerate(kinds, 1):
        outputs = ["PRE_CANDIDATE_ONLY", "NO_TARGET_ESTIMATE", "ZERO_MATHEMATICAL_RESULT_CREDIT"]
        if kind is ResearchTraceEventType.CONTEXT_FROZEN:
            outputs.insert(0, context_hash)
        if kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            outputs.insert(0, memory_hash)
        if kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            outputs[:0] = [shortcut_hash, "selected_mode:CANNOT_CHECK", "LIFT_NOT_AUTHORIZED"]
        payload = {
            "event_id": f"RH-ANA-003i-E{index:02d}",
            "atom_id": ATOM,
            "event_type": kind.value,
            "timestamp": f"2026-08-12T09:05:{index:02d}Z",
            "state_summary": (
                "The active object is the actual natural-order von-Mangoldt/Laguerre prefix array at the frozen moving cutoff. "
                "No internal statistic, estimate, proof claim, Li implication, or RH conclusion has been proposed."
            ),
            "action_summary": kind.value,
            "evidence_pointers": [evidence[kind]],
            "alternatives_considered": [
                "reuse the running negative excursion",
                "treat an ambient signed path as target evidence",
                "estimate a moment or block family immediately",
                "first classify bounded source-defined families by endpoint projection and realization",
                "rotate immediately to mollifier/resonance",
            ],
            "decision_rationale": (
                "Prior failures show that endpoint reconstruction, complement conservation, and arithmetic attainability must be decided before estimation."
            ),
            "outputs": outputs,
            "uncertainties": [
                "no source-bound family has survived",
                "moving-complement authority remains shadow-only",
                "same-context review is not independent",
            ],
            "residuals": [
                "family-level endpoint projection and realization discriminator unexecuted",
                "SEARCH/JUMP/GLUE unexhausted",
                "root OPEN_NO_SOLUTION_CERTIFICATE",
            ],
            "next_steps": [
                "for each bounded family derive its exact relation to R_n(Y_n), S_n, and D_n(Y_n)",
                "reject endpoint or running-extremum reconstruction and ambient-only witnesses",
                "reject premises not strictly weaker than the endpoint/Li obligation",
                "if no family survives, open a separately frozen mollifier/resonance fiber",
                "do not generate a mathematical candidate in this round",
            ],
            "previous_event_hash": previous,
        }
        artifact_hash = canonical_hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **{**payload, "event_type": kind}))
        previous = artifact_hash
    return MathResearchTrace("RH-ANA-003i-PRE-CANDIDATE-TRACE-20260812", tuple(entries))


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
                "actual natural-order von-Mangoldt/Laguerre triangular array",
                "moving cutoff Y_n",
                "cutoff endpoint R_n(Y_n)",
                "exact target S_n and complement D_n(Y_n)",
                "bounded unnamed internal-family taxonomies",
            ),
            relations=(
                "natural-order prefix",
                "endpoint projection",
                "exact complement gluing",
                "target-domain realization",
                "strict-premise comparison",
            ),
            domain="analytic number theory / ordered arithmetic transforms",
            goal_type="freeze a candidate-free family discriminator",
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
        "packet_id": "RH-ANA-003i-SOURCE-METHOD-TRANSFER-PACKET-20260812",
        "atom_id": ATOM,
        "retrieved_before_candidate": True,
        "primary_sources": [
            {
                "id": "COFFEY-0706.0343v2",
                "citation": "M. W. Coffey, Relations and positivity results for the derivatives of the Riemann xi function, arXiv:0706.0343v2",
                "anchors": ["Proposition 2(a), equations (15)-(17)", "Discussion around equations (118)-(120)"],
                "pdf_sha256": "57cf784447e1f4156144ef3fd0253bb3452273918f470bcfbc063ee049c8cbc5",
                "authorized_use": "exact prime/Laguerre normalization and root-sensitive context",
            },
            {
                "id": "LI-1997",
                "citation": "X.-J. Li, The positivity of a sequence of numbers and the Riemann hypothesis, J. Number Theory 65 (1997), 325-333",
                "anchors": ["Li all-index positivity criterion"],
                "access_status": "BOUND_VIA_CURRENT_MAIN_SOURCE_PACKET_NOT_LIVE_RETRIEVED_THIS_ROUND",
                "authorized_use": "root-boundary context only",
            },
            {
                "id": "BOMBIERI-LAGARIAS-1999",
                "citation": "E. Bombieri and J. C. Lagarias, Complements to Li's Criterion for the Riemann Hypothesis, JNT 77 (1999), 274-287",
                "anchors": ["Theorem 2 arithmetic/Li criterion context as recorded in current-main RH source packets"],
                "access_status": "BOUND_VIA_CURRENT_MAIN_SOURCE_PACKET_NOT_LIVE_RETRIEVED_THIS_ROUND",
                "authorized_use": "exact Li/Weil ledger boundary; no internal-family theorem",
            },
            {
                "id": "VOROS-math0506326v2",
                "citation": "A. Voros, Sharpenings of Li's criterion for the Riemann Hypothesis, arXiv:math/0506326v2",
                "anchors": ["asymptotic criterion theorem, equations (17)-(18)"],
                "pdf_sha256": "dd360dab4379590e3597d4ee0be81c0b3b486e62693ee08cf79a37bae5c1c802",
                "authorized_use": "root-sensitive tempered/non-tempered contrast only",
            },
            {
                "id": "BELLOTTI-2508.02041v1",
                "citation": "C. Bellotti, A new zero-density estimate and an improved error term in the prime number theorem, arXiv:2508.02041v1",
                "anchors": ["Theorem 1.5", "equations (1.3)-(1.4)"],
                "pdf_sha256": "39a39e3dbc73506cf5dfd0b8a18b24e85302d305fa3059a60abcfa6f23292568",
                "authorized_use": "fixed-n C002 provenance and possible moving-complement premise only",
            },
            {
                "id": "DUNSTER-GIL-SEGURA-1705.01190v1",
                "citation": "T. M. Dunster, A. Gil, and J. Segura, Uniform asymptotic expansions for Laguerre polynomials, arXiv:1705.01190v1",
                "anchors": ["equation (1.1) exact finite Laguerre sum"],
                "pdf_sha256": "e93985f8ede2799f6e9f3b12dad2565228fefa0b1f662306e2caf9768d2b423c",
                "authorized_use": "formula/asymptotic method-transfer context; no target prefix theorem",
            },
            {
                "id": "CONREY-ETAL-2508.11108",
                "citation": "Conrey et al., arXiv:2508.11108 (2025)",
                "access_status": "DEFERRED_ALTERNATE_ROUTE_NOT_VERIFIED_THIS_ROUND",
                "authorized_use": "none in this atom; only a separately frozen rotation target",
            },
        ],
        "shadow_evidence": [
            {
                "id": "PR316-R9",
                "exact_head": "13062780d022c43395ed36d78e276c837bfb4352",
                "scope": "proposal-only coefficient majorant and outer-complement cutoff scale",
                "non_authority": "not a theorem premise and supplies no strict-prefix realization witness",
            },
            {
                "id": "PR320-R8",
                "exact_head": "022da37dbdb9ae5d60e7877ac2cb7b7f6f8426c8",
                "scope": "proposal-only effective-endpoint dichotomy for running negative excursion",
                "non_authority": "does not classify non-extremal families or prove target-domain strictness",
            },
        ],
        "bounded_method_transfer_matrix": [
            {
                "family": "moment or distributional feasible-set constraints",
                "status": "UNINSTANTIATED_FAMILY_ONLY",
                "first_discriminator": "derive exact endpoint projection and reject endpoint reconstruction",
            },
            {
                "family": "ordered block occupancy, energy, or multiscale balance constraints",
                "status": "UNINSTANTIATED_FAMILY_ONLY",
                "first_discriminator": "prove natural-order target realization and exact complement interface",
            },
            {
                "family": "support-aware arithmetic feasible sets",
                "status": "UNINSTANTIATED_FAMILY_ONLY",
                "first_discriminator": "show assumptions are strictly weaker than endpoint/Li control",
            },
            {
                "family": "transform-domain internal constraints",
                "status": "CANNOT_CHECK_SOURCE_ROUTE_NOT_VERIFIED",
                "first_discriminator": "bind an exact inverse map and forbid hidden regrouping",
            },
            {
                "family": "mollifier/resonance",
                "status": "DEFERRED_SEPARATE_CONTEXT_REQUIRED",
                "first_discriminator": "none in this packet",
            },
        ],
        "authority": "SOURCE_AND_METHOD_TRANSFER_CONTEXT_ONLY_NO_TARGET_RESULT",
        "mathematical_result_credit": False,
    })


def build_documents() -> dict[str, dict]:
    plan, fiber, memory, tm, shortcut, research_trace, preservation = build_current_gate_plan()
    binding, observation = framework_subject(fiber.packet_hash)
    source = source_packet_document()
    atom = seal({
        "schema_version": "1.0.0",
        "atomization_id": "RH-ANA-003i-ATOMIZATION-20260812",
        "recorded_at": FROZEN_AT,
        "atom_id": ATOM,
        "parent_atom_id": PARENT,
        "root_issue": 3,
        "control_issues": [265, 315, 324],
        "object": (
            "The actual zeta-domain natural-order triangular array x_{n,m}, prefixes R_n(M) for 2<=M<=Y_n, "
            "moving cutoff Y_n=exp(C n^(5/3) log^2(n+e)), exact S_n=S_{2Lambda}(n), and D_n(Y_n)."
        ),
        "qoi": (
            "Whether a source-bound non-extremal internal-family class is target-realized, uniformly controllable at the frozen scale, "
            "exactly composable with the complement, non-reconstructive of endpoint/running-extremum control, and based on strictly weaker premises."
        ),
        "target_scale_obligation": "log Y_n=C n^(5/3) log^2(n+e); C is frozen but no threshold or estimate is claimed",
        "first_discriminator": [
            "derive every retained family's exact relation to R_n(Y_n), S_n, and D_n(Y_n)",
            "reject containment, domination, or trivial reconstruction of endpoint/running-extremum control",
            "reject ambient signed-path witnesses without target arithmetic realization",
            "reject reordering or regrouping",
            "reject premises not strictly weaker than the endpoint/Li obligation",
            "if no target-domain family survives bounded search, rotate to a separately frozen mollifier/resonance fiber",
        ],
        "candidate_generation_allowed": False,
        "candidate_proposed": False,
        "target_result_accessed": False,
        "lift_authorized": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
        "authority_boundary": {
            "operational_metadata_zero_mathematical_credit": True,
            "grants_internal_family_existence": False,
            "grants_moving_prefix_bound": False,
            "grants_complement_rate": False,
            "grants_li_positivity": False,
            "grants_rh_authority": False,
        },
    })
    tool_snapshot = seal({
        "schema_version": "1.0.0",
        "snapshot_id": "RH-ANA-003i-TOOL-SNAPSHOT-20260812",
        "target_atom_id": ATOM,
        "application_base_commit": APPLICATION_BASE_SHA,
        "query_result": "MATCHES_FOUND",
        "tools": [{
            "tool_id": "T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY",
            "authority": "SCOPED_PROOF_BACKED_CURRENT_MAIN",
            "applicable_effect": "preserve fixed-n natural-order target and complement existence",
            "non_guarantees": ["no moving-n rate", "no internal-family bound", "no Li or RH implication"],
        }],
        "mathematical_credit": False,
    })
    failure_snapshot = seal({
        "schema_version": "1.0.0",
        "snapshot_id": "RH-ANA-003i-FAILURE-SNAPSHOT-20260812",
        "target_atom_id": ATOM,
        "failures": [
            {"failure_id": item, "status": "BOUND_SEARCH_WARNING", "blocks_all_reuse": False}
            for item in FAILURES
        ],
        "shadow_sources": [
            "draft PR #320@022da37dbdb9ae5d60e7877ac2cb7b7f6f8426c8",
            "draft PR #316@13062780d022c43395ed36d78e276c837bfb4352",
        ],
        "reuse_rule": "prior failure is a warning, not a blacklist; target-specific difference and cheapest repeat-failure tests are required",
        "mathematical_credit": False,
    })
    expert = expert_review_document(fiber.packet_hash)
    binding_document = seal(dict(binding.document()))
    observation_document = seal({
        "schema_version": "framework-subject-revalidation-observation-v1",
        "observation_id": "RH-ANA-003i-FRAMEWORK-REVALIDATION-20260812",
        "observed_current_main_sha": observation.observed_current_main_sha,
        "intervening_diff": [],
        "observation_evidence_pointers": list(observation.observation_evidence_pointers),
        "verdict": plan.framework_subject_gate.verdict.value,
        "licenses_candidate_materialization": plan.framework_subject_gate.licenses_candidate_materialization,
        "protected_surface_equal_to_application_pin": True,
        "grants_scientific_authority": False,
    })
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
        "receipt_id": "RH-ANA-003i-PRE-CANDIDATE-GATE-20260812",
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
            "trace_runtime_gate": plan.trace_gate.verdict.value,
            "trace_direct_audit_expected": "PASS",
            "preservation": plan.preservation_gate.verdict.value,
            "framework_subject": plan.framework_subject_gate.verdict.value,
            "selected_mode": shortcut.selected_mode.value,
            "candidate_generation_allowed": plan.candidate_generation_allowed,
            "licensed_action": "EXECUTE_FAMILY_LEVEL_ENDPOINT_REALIZATION_AND_PREMISE_STRENGTH_DISCRIMINATOR_ONLY",
            "lift_authorized": False,
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
    })
    return documents


def write_documents(root: Path = Path(".")) -> None:
    for name, document in build_documents().items():
        path = root / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_documents()
