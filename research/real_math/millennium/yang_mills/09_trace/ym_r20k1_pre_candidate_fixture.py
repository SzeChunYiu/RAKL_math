"""Strict pre-candidate packet for the YM R20 irrelevant-coordinate slack atom.

This packet contains no candidate lemma, threshold, proof, or observed outcome.
It freezes one cheap discriminator and withholds candidate materialization until
the packet and its pre-scratch receipt are durable on public ``main``.
"""

from __future__ import annotations

from dataclasses import asdict, replace
from enum import Enum
import hashlib
import json
from pathlib import Path

from rakl.framework_candidate_freeze import (
    FrameworkSubjectFreezeBinding,
    FrameworkSubjectRevalidationObservation,
)
from rakl.math_context import AnalogyScanStatus, CrossDomainAnalogy, MathContextFiber, MethodTransfer
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.pre_action_receipt import (
    PreActionFibreReceipt,
    RejectedRetrieval,
    RetrievalAuthority,
    SelectedRetrieval,
)
from rakl.pre_scratch_fibre_freeze import run_pre_scratch_fibre_freeze_hook
from rakl.problem_solving_algebra import ProblemSignature
from rakl.quantifier_compatibility import (
    GluingConsumer,
    ScopeAlignment,
    PermissionStatus,
    WitnessAuditVerdict,
    audit_quantifier_compatibility,
    build_fail_closed_unknown_witness,
)
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


ATOM = "YM-S1a2i-K1"
PARENT = "YM-S1a2i"
APPLICATION_BASE_SHA = "b7ca6ac51fa8319b559e95402c47959c626f284a"
FRAMEWORK_SHA = "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
FROZEN_AT = "2026-08-12T10:28:00+00:00"
HOOK_AT = "2026-08-12T10:29:00Z"
DOMAIN = "Yang-Mills nonautonomous RG invariant-region analysis"

BASE = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[5]
R20_LESSON = "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_R20_MATHEMATICAL_LESSON_20260812.json"
FAILURE_ATLAS = "research/real_math/millennium/cross_problem/07_memory/GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_BSD_R15_SUCCESSOR_20260812.json"
TOOL_INVENTORY = "research/real_math/millennium/yang_mills/07_memory/YM-S1A1_RESEARCH_TOOL_INVENTORY_20260811.json"
R20_LESSON_BLOB = "463c5a0022c78ac4d6551c225f37ae4efb103242"
FAILURE_ATLAS_BLOB = "dbfe7d1d9f82c894bb68f1c988bbb26318c0416f"
TOOL_INVENTORY_BLOB = "bcd83b24d5bf28134d3ec2586386cc5dbd1b46e8"
R20_LESSON_ARTIFACT_SHA256 = "18c39a9a7ea90fede4fb3672d1e777886fea7e88e094f453bb8fada799018a73"
FAILURE_ATLAS_ARTIFACT_SHA256 = "db809b89815e0ca6a58eaa915e531bcd52d127f5449469dd087f349763f69d11"
TOOL_INVENTORY_RAW_SHA256 = "e392651dfa64976a1586a25fe709f37f2606914a0d3f043a5b0a2865834992f0"
PATHS = {
    "selection": BASE / "01_frontier/YM-S1a2i_K1_CROSS_MILLENNIUM_SELECTION_20260812.json",
    "atomization": BASE / "02_problem_dag/YM-S1a2i_K1_DELTA_20260812.json",
    "context": BASE / "01_frontier/YM-S1a2i_K1_CONTEXT_FIBER_20260812.json",
    "memory": BASE / "07_memory/YM-S1a2i_K1_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": BASE / "07_memory/YM-S1a2i_K1_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": BASE / "08_reviews/YM-S1a2i_K1_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": BASE / "08_reviews/YM-S1a2i_K1_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "quantifier": BASE / "08_reviews/YM-S1a2i_K1_QUANTIFIER_COMPATIBILITY_20260812.json",
    "trace": BASE / "09_trace/YM-S1a2i_K1_PRE_CANDIDATE_TRACE_20260812.json",
    "framework_binding": BASE / "09_trace/YM-S1a2i_K1_FRAMEWORK_SUBJECT_BINDING_20260812.json",
    "pre_action": BASE / "09_trace/YM-S1a2i_K1_PRE_ACTION_RECEIPT_20260812.json",
    "retrieval_bindings": BASE / "09_trace/YM-S1a2i_K1_RETRIEVAL_BINDINGS_REPAIR_20260812.json",
    "hook": BASE / "09_trace/YM-S1a2i_K1_PRE_SCRATCH_HOOK_RESULT_20260812.json",
    "gate": BASE / "09_trace/YM-S1a2i_K1_PRE_CANDIDATE_GATE_20260812.json",
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


def _hash(value: object, prefix: bool = True) -> str:
    raw = hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return "sha256:" + raw if prefix else raw


def _seal(value: dict, field: str = "artifact_hash") -> dict:
    result = dict(value)
    result[field] = ""
    result[field] = _hash(result)
    return result


def _source_binding(
    *,
    retrieval_id: str,
    relative_path: str,
    git_blob: str,
    selected_hash_semantics: str,
    expected_selected_sha256: str,
) -> dict:
    path = PROJECT_ROOT / relative_path
    raw = path.read_bytes()
    document = json.loads(raw)
    raw_sha256 = hashlib.sha256(raw).hexdigest()
    full_canonical_sha256 = _hash(document, prefix=False)
    declared = document.get("artifact_hash")
    recomputed_declared = None
    if declared is not None:
        payload = dict(document)
        payload["artifact_hash"] = ""
        recomputed_declared = _hash(payload)
        if declared != recomputed_declared:
            raise RuntimeError(f"{retrieval_id}: declared artifact hash does not recompute")
    if selected_hash_semantics == "DECLARED_ARTIFACT_HASH_WITHOUT_SHA256_PREFIX":
        selected = str(declared).removeprefix("sha256:")
    elif selected_hash_semantics == "RAW_FILE_SHA256_NO_DECLARED_ARTIFACT_HASH":
        if declared is not None:
            raise RuntimeError(f"{retrieval_id}: raw semantics forbidden when artifact_hash exists")
        selected = raw_sha256
    else:
        raise RuntimeError(f"{retrieval_id}: unknown selected hash semantics")
    if selected != expected_selected_sha256:
        raise RuntimeError(f"{retrieval_id}: selected payload hash drift")
    return {
        "retrieval_id": retrieval_id,
        "application_commit": APPLICATION_BASE_SHA,
        "path": relative_path,
        "git_blob": git_blob,
        "selected_payload_hash_semantics": selected_hash_semantics,
        "selected_payload_sha256": selected,
        "declared_artifact_hash": declared,
        "recomputed_declared_artifact_hash": recomputed_declared,
        "full_canonical_document_sha256": full_canonical_sha256,
        "raw_file_sha256": raw_sha256,
    }


def build_retrieval_bindings() -> dict:
    return _seal(
        {
            "schema_version": "ym-retrieval-content-binding-v1",
            "repair_id": "YM-S1a2i-K1-PR379-RETRIEVAL-BINDING-REPAIR-20260812",
            "atom_id": ATOM,
            "supersedes": {
                "merged_pr": 379,
                "merge_sha": "cc39c7a2553c2e20aa7103652d1429675164016b",
                "defect": "two SelectedRetrieval values used raw-file SHA256 while their JSON sources declared artifact_hash identities",
                "candidate_or_result_accessed_before_repair": False,
            },
            "selected_hash_rule": (
                "When a JSON memory artifact declares artifact_hash, SelectedRetrieval.payload_hash and the "
                "corresponding memory snapshot hash use that declared content identity without the sha256: prefix. "
                "Raw and full-canonical hashes remain separate byte/document checks."
            ),
            "bindings": [
                _source_binding(
                    retrieval_id="YM-R20-lesson",
                    relative_path=R20_LESSON,
                    git_blob=R20_LESSON_BLOB,
                    selected_hash_semantics="DECLARED_ARTIFACT_HASH_WITHOUT_SHA256_PREFIX",
                    expected_selected_sha256=R20_LESSON_ARTIFACT_SHA256,
                ),
                _source_binding(
                    retrieval_id="global-failure-atlas",
                    relative_path=FAILURE_ATLAS,
                    git_blob=FAILURE_ATLAS_BLOB,
                    selected_hash_semantics="DECLARED_ARTIFACT_HASH_WITHOUT_SHA256_PREFIX",
                    expected_selected_sha256=FAILURE_ATLAS_ARTIFACT_SHA256,
                ),
                _source_binding(
                    retrieval_id="YM-S1A1-research-tool-inventory",
                    relative_path=TOOL_INVENTORY,
                    git_blob=TOOL_INVENTORY_BLOB,
                    selected_hash_semantics="RAW_FILE_SHA256_NO_DECLARED_ARTIFACT_HASH",
                    expected_selected_sha256=TOOL_INVENTORY_RAW_SHA256,
                ),
            ],
            "authority": "PRE_CANDIDATE_BINDING_REPAIR_ONLY_NO_MATHEMATICAL_RESULT_CREDIT",
            "artifact_hash": "",
        }
    )


def build_selection() -> dict:
    return _seal({
        "selection_id": "CROSS-MILLENNIUM-NONPNP-NONRH-20260812-K1",
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_sha": FRAMEWORK_SHA,
        "selection_rule": "Highest expected mathematical information per cheapest exact discriminator on merged main; pending PRs, CI, Git, schemas and repository growth carry zero mathematical weight.",
        "lanes": [
            {"lane": "navier_stokes", "active_residual": "derive a source-valid uniform intermediate-annulus tail modulus", "cost": "requires new PDE ancestry/tail input", "selection": "DEFER"},
            {"lane": "hodge", "active_residual": "bind smoothness/properness to the exact witness-incidence morphism", "cost": "requires constructing the target incidence geometry, not only an abstract proxy", "selection": "DEFER"},
            {"lane": "birch_swinnerton_dyer", "active_residual": "control Sha[p-infinity] corank after Selmer corank two", "cost": "deep arithmetic input; no cheap source-valid discriminator currently frozen", "selection": "DEFER"},
            {"lane": "poincare", "active_residual": "no unsolved Clay root; only transfer/metamethod study remains", "cost": "cannot outrank an open root-facing mathematical obstruction", "selection": "DEFER"},
            {"lane": "yang_mills", "active_residual": "decide whether strict irrelevant contraction can pay the O(g^4) shrink of an O(g^2) graph radius", "cost": "one scalar invariant-region discriminator using already source-bound equations", "selection": "SELECT"},
        ],
        "selected_atom": ATOM,
        "rationale": "R20 explicitly left K-coordinate irreparability unsupported. Resolving this single coordinate separates a repairable stable block from the still-open relevant inverse/base-map obstructions without importing any continuum or mass-gap claim.",
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        "mathematical_credit": 0,
        "artifact_hash": "",
    })


def build_context() -> MathContextFiber:
    fiber = MathContextFiber(
        atom_id=ATOM,
        object_context=(
            "Determine only whether the source-scoped irrelevant K-coordinate estimate can be made invariant under the next, slightly smaller, O(g^2) graph radius."
        ),
        structural_coordinates=(
            "one-step irrelevant contraction factor rho strictly between zero and one",
            "higher-order K forcing of order g_k^4",
            "base flow g_{k+1}=g_k-b_0 g_k^3 plus a value remainder of order g_k^5",
            "target K radius c_K g_{k+1}^2 rather than c_K g_k^2",
            "constants must be uniform in the scale index k on one small-coupling interval",
            "relevant lambda coordinate, base injectivity and continuum gluing are excluded",
            "root status OPEN_NO_SOLUTION_CERTIFICATE",
        ),
        equivalent_formulations=(
            "Invariant-region form: compare the contracted-and-forced K bound with the next graph radius.",
            "Margin form: determine whether the O(g^2) contraction slack dominates the O(g^4) radius shrink and forcing uniformly for small g.",
            "Quantifier form: ask for one epsilon and source constants valid for every scale k and every 0<g_k<=epsilon.",
        ),
        solved_analogues=(
            "Elementary invariant-interval lemma: a fixed strict contraction plus a higher-order perturbation preserves a sufficiently small ball of fixed radius scale.",
            "Stable-coordinate graph transforms spend a uniform linear contraction margin against nonlinear higher-order forcing.",
        ),
        near_solved_analogues=(
            "YM R20 identifies rho<1 plus O(g^4) forcing as a plausible but unproved repair of the K-coordinate shrinking-radius step.",
            "Standard hyperbolic graph transforms close stable coordinates separately from inverse treatment of relevant coordinates.",
        ),
        method_transfers=(
            MethodTransfer(
                source_context="Small invariant balls under strict contraction and quadratic perturbation",
                method="Make the contraction slack explicit, bound the perturbation relative to it, and solve one smallness inequality before composing other coordinates.",
                shared_structure=("fixed strict contraction", "higher-order forcing", "small parameter", "invariant target ball"),
                required_assumptions=("uniform contraction margin", "uniform forcing constant", "positive lower control on the next radius"),
                disanalogies=("the target radius itself changes with g", "the Yang-Mills norm is scale dependent", "source text availability is bounded"),
                repair_question="Do the exact source-scoped constants and base lower bound suffice for one uniform small-coupling K-coordinate next-radius inequality?",
                source_anchors=("research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_R20_SOURCE_AUDIT.md",),
            ),
        ),
        explicit_disanalogies=(
            "K-coordinate invariance is not full graph-transform contraction.",
            "A value bound for the base remainder is not a derivative or injectivity theorem.",
            "Closing a UV coordinate gives no OS reconstruction, continuum nontriviality or mass gap.",
            "The source PDF remains unavailable for visual verification; target use is bounded to acquired indexed primary-author text.",
        ),
        source_anchors=(
            "research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_R20_SOURCE_AUDIT.md",
            "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_R20_MATHEMATICAL_LESSON_20260812.json",
            "research/real_math/millennium/cross_problem/07_memory/GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_BSD_R15_SUCCESSOR_20260812.json",
            f"RAKL@{FRAMEWORK_SHA}",
        ),
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(
            CrossDomainAnalogy(
                source_kind="capacity control",
                source_situation="A store compresses inventory by a fixed fraction each cycle while the allowed warehouse shrinks only by a higher-order amount and receives a smaller-order replenishment.",
                common_abstraction=("strict fractional slack", "smaller target", "higher-order disturbance"),
                source_to_target_mapping=("compression -> rho contraction", "warehouse radius -> c_K g^2", "replenishment -> O(g^4) forcing"),
                shared_constraints=("one uniform slack must dominate both shrinkage and disturbance",),
                disanalogies=("inventory has no Banach norm or RG scale dependence", "analogy supplies no theorem authority"),
                proposed_principle="Budget every loss against an explicit slack before declaring the smaller target invariant.",
                validation_obligation="Prove or refute the exact scalar inequality from the source-scoped bounds with all quantifiers and constants exposed.",
                provenance_note="Proposal generator only.",
            ),
        ),
        analogy_scan_notes="No additional everyday bridge was retained because it added no structural coordinate beyond explicit slack accounting.",
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash="",
    )
    doc = _document(fiber)
    doc["packet_hash"] = _hash(doc)
    return replace(fiber, packet_hash=doc["packet_hash"])


def build_memory(context: MathContextFiber) -> ResearchMemoryReview:
    review = ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        tool_inventory_snapshot_hash="sha256:" + TOOL_INVENTORY_RAW_SHA256,
        failure_lattice_snapshot_hash="sha256:" + FAILURE_ATLAS_ARTIFACT_SHA256,
        tool_query_status=MemoryQueryStatus.NO_RELEVANT_MATCH,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=("small invariant-region inequality", "stable-coordinate margin isolation", "full hyperbolic graph transform"),
        relevant_failure_ids=("FM-YM-R20-SHRINKING-DOMAIN-RELEVANT-MARGIN", "FM-YM-SAME-THEORY-INTERFACE-AND-DENSITY"),
        selected_tool_ids=(),
        tool_applicability_notes=("No promoted Yang-Mills research tool proves next-radius invariance.",),
        failure_reuse_notes=(
            "R20 is the direct warning: monotonic decrease of g alone has the wrong inequality polarity.",
            "DifferenceWitness: this child isolates only the K coordinate where rho<1 supplies structure absent from the forward relevant-coordinate estimate.",
            "Cheapest repeat-failure test: compare the full contracted-plus-forced K upper bound directly with c_K g_{k+1}^2, never with the old radius.",
        ),
        unresolved_warnings=("Uniformity in k is load-bearing.", "No result may be extrapolated to lambda, base inversion, OS reconstruction or the root."),
        evidence_pointers=(
            TOOL_INVENTORY,
            FAILURE_ATLAS,
            R20_LESSON,
            "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_RETRIEVAL_BINDINGS_REPAIR_20260812.json",
        ),
        artifact_hash="",
    )
    doc = _document(review); doc["artifact_hash"] = _hash(doc)
    return replace(review, artifact_hash=doc["artifact_hash"])


def build_shortcut(context: MathContextFiber, memory: ResearchMemoryReview):
    source = ObstructionFingerprint(
        obstruction_id="O-ELEMENTARY-STRICT-CONTRACTION-HIGHER-ORDER-FORCING",
        domain="elementary invariant-region analysis",
        roles=("current radius", "strict contraction", "higher-order forcing", "small parameter"),
        relations=("contraction creates leading-order slack", "forcing is asymptotically smaller than slack"),
        constraints=("uniform contraction below one", "uniform forcing coefficient"),
        failure_mechanisms=("forcing exceeds unused slack",),
        invariants_to_preserve=("nonnegative radius", "uniform quantifiers"),
        desired_transition=("a sufficiently small ball maps into itself",),
        forbidden_losses=("post-result threshold selection",),
    )
    episode = ObstructionTransformationEpisode(
        episode_id="OTEP-ELEMENTARY-STRICT-CONTRACTION-SMALL-BALL",
        source_domain="elementary invariant-region analysis",
        source_context="Fixed-radius strict contraction with a quadratic-in-radius perturbation",
        source_obstruction=source,
        transformation_name="spend_contraction_margin_against_higher_order_forcing",
        operation="Separate leading contraction slack from higher-order forcing and freeze the smallness threshold before evaluation.",
        preconditions=("contraction factor strictly below one", "forcing coefficient uniform", "positive radius coefficient"),
        resulting_relations=("a sufficiently small ball maps into itself",),
        preserved_invariants=("uniform quantifiers", "nonnegative radius"),
        relaxed_or_broken_constraints=(),
        known_breakpoints=("contraction approaches one without uniform margin", "forcing is not higher order", "target radius changes without lower control"),
        evidence_pointers=("research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_R20_SOURCE_AUDIT.md",),
        authority=TransformationEpisodeAuthority.PROOF_BACKED,
        artifact_hash="sha256:9340739d2e7be6e3d8a85f5752fe8fa08b26f58688a497b8e68b825ca37e1cd0",
    )
    tm = build_transformation_memory(
        memory_id="OTM-YM-S1a2i-K1-20260812",
        source_universe=("elementary invariant-region analysis", "merged R20 source-scoped failure record"),
        episodes=(episode,),
        evidence_pointers=("research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_RESEARCH_MEMORY_REVIEW_20260812.json",),
    )
    target = ObstructionFingerprint(
        obstruction_id="O-YM-R20-K-NEXT-RADIUS",
        domain=DOMAIN,
        roles=("current K radius", "rho contraction", "O(g^4) forcing", "small coupling"),
        relations=("contraction creates leading-order slack", "forcing is asymptotically smaller than slack", "radius shrink is also higher order"),
        constraints=("uniform contraction below one", "uniform forcing coefficient", "source constants uniform in k", "next radius requires lower base-flow control"),
        failure_mechanisms=("forcing exceeds unused slack", "old radius substituted for smaller next radius"),
        invariants_to_preserve=("nonnegative radius", "uniform quantifiers", "scale-index uniformity", "same K norm and source theory", "open root authority"),
        desired_transition=("a sufficiently small ball maps into itself",),
        forbidden_losses=("post-result threshold selection", "claiming full graph contraction"),
    )
    witness = StructuralMappingWitness(
        witness_id="SMW-YM-R20K1-ELEMENTARY-MARGIN",
        episode_id=episode.episode_id,
        target_obstruction_id=target.obstruction_id,
        role_mapping=(("current radius", "current K radius"), ("strict contraction", "rho contraction"), ("higher-order forcing", "O(g^4) forcing"), ("small parameter", "small coupling")),
        shared_relations=("contraction creates leading-order slack", "forcing is asymptotically smaller than slack"),
        shared_constraints=("uniform contraction below one", "uniform forcing coefficient"),
        precondition_mapping=(("contraction factor strictly below one", "R20 records rho<1"), ("forcing coefficient uniform", "must be checked from the source-scoped bound"), ("positive radius coefficient", "c_K>0 in the graph ball")),
        unmatched_source_preconditions=(),
        disanalogies=("the target radius shrinks with g_{k+1}", "the target uses a scale-dependent polymer norm"),
        target_validation_obligations=("use a lower bound for g_{k+1}", "keep every constant uniform in k", "freeze threshold before testing", "exclude all non-K conclusions"),
        evidence_pointers=("research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_R20_SOURCE_AUDIT.md",),
        artifact_hash="sha256:9c4713cc5cbd9ac2a51496996223920af05b4da00ba3b60ae05f5907ed84f21b",
    )
    review = ObstructionTransformationReview(
        review_id="OTR-YM-S1a2i-K1-20260812",
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        research_memory_review_hash=memory.artifact_hash,
        episode_memory_snapshot_hash=tm.snapshot_hash,
        obstruction=target,
        direct_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        jump_search_status=RouteSearchStatus.MATCHES_FOUND,
        glue_search_status=RouteSearchStatus.NOT_RUN,
        selected_mode=ShortcutMode.JUMP,
        jump_mapping_witnesses=(witness,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=("SEARCH selects a validation operation, not a theorem.", "The moving-radius disanalogy is the entire target discriminator."),
        evidence_pointers=("research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",),
        artifact_hash="",
    )
    doc = _document(review); doc["artifact_hash"] = _hash(doc)
    return tm, replace(review, artifact_hash=doc["artifact_hash"])


def build_expert(context: MathContextFiber) -> dict:
    return _seal({
        "review_id": "ECR-YM-S1a2i-K1-20260812", "atom_id": ATOM, "context_packet_hash": context.packet_hash,
        "roles": [
            {"role": "domain_theory_lead", "finding": "Equation (573) and a two-sided base-flow bound must be source-bound; no K lemma repairs lambda or the continuum interface."},
            {"role": "analogy_method_transfer_lead", "finding": "The elementary small-ball method applies only after the changing-radius lower bound and scale-uniform constants are mapped."},
            {"role": "adversarial_falsification_lead", "finding": "Test rho approaching one, missing lower base control, nonuniform forcing, and equality at the registered threshold."},
            {"role": "formal_methods_lead", "finding": "Freeze quantifiers and all positive constants; distinguish existence of epsilon from an evaluated explicit threshold."},
            {"role": "novelty_research_value_lead", "finding": "The inequality is elementary and not novel; value is exact diagnosis separation inside R20."},
        ],
        "disagreements": ["Theory lead prefers primary-source reinspection; falsification lead says the conditional scalar implication can be decided first."],
        "strongest_objection": "If the acquired source does not give constants uniform in k or a lower bound on g_{k+1}, the target application is CANNOT_CHECK even if an abstract inequality is true.",
        "unresolved_uncertainties": ["PDF visual verification remains unavailable.", "Source-wide stronger stable-manifold material may be unexposed."],
        "recommendation": "After durable public freeze, evaluate exactly one K-coordinate next-radius discriminator and preserve CANNOT_CHECK if source uniformity is absent.",
        "same_context_not_independent_review": True,
        "frozen_at": "2026-08-12T10:28:20+00:00", "artifact_hash": "",
    })


def build_quantifier(context: MathContextFiber):
    """Freeze the unresolved source-uniformity question with the fixed fail-closed API.

    The indexed source surface has not yet established that one norm and one
    constant family apply uniformly for every scale.  This pre-candidate packet
    therefore records UNKNOWN rather than disguising the gap as CONDITIONAL.
    """

    return build_fail_closed_unknown_witness(
        witness_id="QCW-YM-S1a2i-K1-20260812",
        atom_id=ATOM,
        source_claim_scope=(
            "one-step source bounds proposed for every scale k on one small-coupling "
            "domain; k-uniform constants and same-norm transport remain to be source-bound"
        ),
        recorded_at_utc="2026-08-12T10:28:20Z",
        evidence_pointers=(
            context.packet_hash,
            "research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_R20_SOURCE_AUDIT.md",
            f"RAKL@{FRAMEWORK_SHA}:src/rakl/quantifier_compatibility.py",
        ),
        point_global_scope=ScopeAlignment.ALIGNED,
        time_supremum_scope=ScopeAlignment.ALIGNED,
        sequence_limit_scope=ScopeAlignment.UNKNOWN,
        norm_quantifier_scope=ScopeAlignment.UNKNOWN,
        point_global_substitution_permitted=PermissionStatus.NO,
        time_supremum_substitution_permitted=PermissionStatus.NO,
        sequence_limit_substitution_permitted=PermissionStatus.UNKNOWN,
        norm_quantifier_substitution_permitted=PermissionStatus.UNKNOWN,
        required_scope_witness="UNKNOWN",
    )


def _entry(i: int, event_type: ResearchTraceEventType, previous: str, state: str, action: str, evidence, **kwargs):
    entry = ResearchTraceEntry(event_id=f"YM-S1a2i-K1-E{i:02d}", atom_id=ATOM, event_type=event_type,
        timestamp=f"2026-08-12T10:{28+i:02d}:00+00:00", state_summary=state, action_summary=action,
        evidence_pointers=tuple(evidence), previous_event_hash=previous, **kwargs)
    doc = _document(entry); doc["artifact_hash"] = _hash(doc)
    return replace(entry, artifact_hash=doc["artifact_hash"])


def build_trace(context, memory, shortcut, expert, quantifier):
    specs = [
        (ResearchTraceEventType.ATOMIZED, "R20 leaves K-coordinate irreparability explicitly unsupported.", "Freeze only the K next-radius margin as child atom.", ("research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_R20_MATHEMATICAL_LESSON_20260812.json",)),
        (ResearchTraceEventType.CONTEXT_FROZEN, "The child separates stable contraction slack from relevant/base/continuum obligations.", "Freeze exact structural coordinates and source boundary.", (context.packet_hash,)),
        (ResearchTraceEventType.ANALOGY_SCAN, "One capacity-budget analogy survives as proposal-only.", "Retain only explicit slack accounting.", (context.packet_hash,)),
        (ResearchTraceEventType.METHOD_TRANSFER_REVIEW, "Elementary invariant-region analysis supplies a conditional method.", "Bind its uniformity assumptions and changing-radius disanalogy.", (context.packet_hash,)),
        (ResearchTraceEventType.EXPERT_CONTEXT_REVIEW, "Five same-context roles preserve the source-uniformity objection.", "Freeze disagreements and cheapest falsifiers.", (expert["artifact_hash"],)),
        (ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW, "R20 failure is directly relevant and no promoted tool closes it.", "Freeze DifferenceWitness and repeat-failure polarity test.", (memory.artifact_hash,)),
        (ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW, "A proof-backed elementary margin episode maps by cross-domain JUMP with changing-radius validation obligations.", "Freeze the structural mapping, material disanalogies and typed quantifier fail-close.", (shortcut.artifact_hash, quantifier.witness_canonical_sha256)),
        (ResearchTraceEventType.NEXT_STEP_PROPOSED, "All pre-candidate discovery objects are frozen, but execution remains withheld until public durability.", "After merge only, freeze one result-blind K-coordinate discriminator candidate.", (context.packet_hash, memory.artifact_hash, shortcut.artifact_hash)),
    ]
    out=[]; prev=""
    for i,(typ,state,action,evidence) in enumerate(specs):
        extra = {}
        if typ is ResearchTraceEventType.EXPERT_CONTEXT_REVIEW:
            extra = {
                "alternatives_considered": ("primary-source reinspection first", "conditional scalar discriminator first"),
                "decision_rationale": "The scalar discriminator is cheapest but must fail closed on missing source uniformity.",
                "uncertainties": tuple(expert["unresolved_uncertainties"]),
                "outputs": (expert["artifact_hash"],),
            }
        elif typ is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            extra = {
                "alternatives_considered": ("repeat the invalid monotonicity step", "attempt the full relevant graph transform"),
                "decision_rationale": "R20 directly isolates the K-coordinate competing diagnosis and its cheapest polarity test.",
                "uncertainties": tuple(memory.unresolved_warnings),
                "outputs": (memory.artifact_hash,),
            }
        elif typ is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            extra = {
                "alternatives_considered": ("same-domain SEARCH", "GLUE", "LIFT"),
                "decision_rationale": "No same-domain proved episode is available; the elementary proof-backed episode survives only as JUMP with explicit target validation.",
                "uncertainties": tuple(shortcut.unresolved_warnings),
                "outputs": (shortcut.artifact_hash, "JUMP"),
            }
        elif typ is ResearchTraceEventType.NEXT_STEP_PROPOSED:
            extra = {
                "alternatives_considered": ("evaluate before public durability", "open a full graph-transform candidate", "freeze one K discriminator after merge"),
                "decision_rationale": "One coordinate maximizes information while preserving chronology and all root boundaries.",
                "uncertainties": ("Source k-uniformity may remain CANNOT_CHECK.",),
                "outputs": ("NO_CANDIDATE_NO_RESULT",),
                "next_steps": ("Merge this packet.", "Revalidate live framework and receipt durability.", "Freeze one result-blind K candidate in a separate round."),
            }
        e=_entry(i,typ,prev,state,action,evidence, **extra)
        out.append(e); prev=e.artifact_hash
    return MathResearchTrace(trace_id="TRACE-YM-S1a2i-K1-PRE-20260812", entries=tuple(out))


def build_plan():
    context=build_context(); memory=build_memory(context); tm,shortcut=build_shortcut(context,memory); expert=build_expert(context); quantifier=build_quantifier(context); trace=build_trace(context,memory,shortcut,expert,quantifier)
    binding=FrameworkSubjectFreezeBinding(binding_id="FSB-YM-S1a2i-K1-20260812", authoritative_framework_sha=FRAMEWORK_SHA,
        pre_candidate_packet_hash=context.packet_hash.removeprefix("sha256:"), frozen_at_utc=FROZEN_AT, evidence_pointers=(f"RAKL@{FRAMEWORK_SHA}",))
    observation=FrameworkSubjectRevalidationObservation(observed_current_main_sha=FRAMEWORK_SHA, intervening_diff=(), observation_evidence_pointers=(f"git-ls-remote:RAKL/main={FRAMEWORK_SHA}",))
    plan=plan_math_research(
        signature=ProblemSignature(objects=("K coordinate", "running coupling", "shrinking graph radius"), relations=("strict irrelevant contraction", "higher-order forcing", "next-radius comparison"), domain=DOMAIN, goal_type="classify source-scoped K next-radius invariance"),
        record=MathResearchRecord(claim_id=ATOM), context_fiber=context, memory_review=memory,
        transformation_memory=tm, shortcut_review=shortcut, research_trace=trace,
        preservation_receipt=None, expected_preservation_sha256=None,
        framework_subject_binding=binding, framework_subject_observation=observation,
        require_framework_subject_gate=True,
    )
    return plan,context,memory,tm,shortcut,expert,quantifier,trace,binding


def build_pre_action(context: MathContextFiber) -> PreActionFibreReceipt:
    return PreActionFibreReceipt(
        receipt_id="PRE-YM-S1a2i-K1-20260812", framework_repository="SzeChunYiu/RAKL", framework_commit=FRAMEWORK_SHA,
        application_repository="SzeChunYiu/RAKL_math", application_commit=APPLICATION_BASE_SHA,
        task_id="YM-root-5", atom_id=ATOM, context_hash=context.packet_hash, fibre_snapshot_hash=context.packet_hash,
        operator_ids=("SOURCE_SCOPED_SCALAR_INVARIANT_REGION_DISCRIMINATOR",),
        selected_retrievals=(
            SelectedRetrieval(f"RAKL/main@{FRAMEWORK_SHA[:8]}", RetrievalAuthority.CANONICAL, "d05e7e19bb57e43f1fbffb2ccc5bbe8745caa34f8b032fd62e32a08595fc4a89"),
            SelectedRetrieval("YM-R20-lesson", RetrievalAuthority.CANONICAL, R20_LESSON_ARTIFACT_SHA256),
            SelectedRetrieval("global-failure-atlas", RetrievalAuthority.CANONICAL, FAILURE_ATLAS_ARTIFACT_SHA256),
        ),
        rejected_retrievals=(
            RejectedRetrieval("Navier-Stokes-B2a1a3", "requires new PDE tail input rather than the selected cheap scalar discriminator"),
            RejectedRetrieval("Hodge-C008", "requires target incidence geometry not present on merged main"),
            RejectedRetrieval("BSD-Sha-finiteness", "deep arithmetic input and no cheap merged-main discriminator"),
        ),
        predeclared_discriminator="Using only source-bound k-uniform constants, decide whether strict irrelevant contraction plus higher-order forcing fits the next O(g_{k+1}^2) K radius on one predeclared small-coupling interval; otherwise return ASSUMPTIONS_INSUFFICIENT or CANNOT_CHECK.",
        allowed_outcome_branches=("SUCCESS", "PARTIAL_SUCCESS", "FAILURE", "BLOCKED", "UNKNOWN"),
        frozen_at_utc=HOOK_AT, sequence_index=21,
    )


def build_documents():
    retrieval_bindings=build_retrieval_bindings(); plan,context,memory,tm,shortcut,expert,quantifier,trace,binding=build_plan(); pre=build_pre_action(context)
    hook = dict(run_pre_scratch_fibre_freeze_hook(
        hook_id="HOOK-YM-S1a2i-K1-20260812",
        hook_invoked_at_utc=HOOK_AT,
        consequential_turn=True,
        receipt_id=pre.receipt_id,
        framework_repository=pre.framework_repository,
        framework_commit=pre.framework_commit,
        application_repository=pre.application_repository,
        application_commit=pre.application_commit,
        task_id=pre.task_id,
        atom_id=pre.atom_id,
        context_hash=pre.context_hash,
        fibre_snapshot_hash=pre.fibre_snapshot_hash,
        operator_ids=pre.operator_ids,
        selected_retrievals=pre.selected_retrievals,
        rejected_retrievals=pre.rejected_retrievals,
        predeclared_discriminator=pre.predeclared_discriminator,
        allowed_outcome_branches=pre.allowed_outcome_branches,
        sequence_index=pre.sequence_index,
    ).document())
    atom=_seal({"atom_id":ATOM,"parent_atom_id":PARENT,"qoi":"IRRELEVANT_K_NEXT_RADIUS_INVARIANCE","exact_obstruction":"R20 used the old radius; decide whether rho<1 supplies enough uniform slack for the smaller next radius.","allowed_results":["CONDITIONAL_SLACK_PROVED","ASSUMPTIONS_INSUFFICIENT","COUNTEREXAMPLE","CANNOT_CHECK"],"candidate_identity":None,"candidate_proposed":False,"result_accessed":False,"root_state":"OPEN_NO_SOLUTION_CERTIFICATE","artifact_hash":""})
    gate=_seal({"atom_id":ATOM,"application_base_sha":APPLICATION_BASE_SHA,"framework_sha":FRAMEWORK_SHA,
        "runtime_gates":{"context":plan.context_gate.verdict.value,"memory":plan.memory_gate.verdict.value,"shortcut":plan.shortcut_gate.verdict.value,"trace":plan.trace_gate.verdict.value,"framework_subject":plan.framework_subject_gate.verdict.value,"runtime_candidate_generation_allowed":plan.candidate_generation_allowed},
        "operational_candidate_materialization_allowed":False,
        "release_condition":"Only after this exact packet and hook receipt are merged to public main and revalidated against live RAKL main.",
        "pre_scratch_durability":{"receipt_path":"research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_PRE_ACTION_RECEIPT_20260812.json","status":"BUILT_NOT_PERSISTED_PENDING_PUBLIC_MAIN_MERGE","required_acknowledgement":"A hash-matching DurablePersistenceAcknowledgement bound to the public Git blob must precede candidate exposure."},
        "pre_candidate_binding_repair":{
            "status":"REPAIRED_BEFORE_CANDIDATE_OR_RESULT_ACCESS",
            "artifact_hash":retrieval_bindings["artifact_hash"],
            "supersedes_pr379_raw_hash_ambiguity":True
        },
        "future_material_result_contract":{
            "mathematical_credit_only":True,
            "required_fields":["attempted_mathematical_implication","exact_mathematical_result_or_failure","supported_and_competing_mathematical_causes","scope","mathematical_falsifier","repair_or_next_discriminator","proof_or_source_evidence"],
            "zero_credit_fields":["git_state","ci_status","schema_validation","hash_chronology","telemetry","repository_growth"],
            "current_status":"NO_RESULT_NO_LESSON"
        },
        "licensed_after_release":"Freeze one result-blind K-coordinate scalar discriminator only.","mathematical_credit":0,"root_state":"OPEN_NO_SOLUTION_CERTIFICATE","artifact_hash":""})
    return {"selection":build_selection(),"atomization":atom,"context":_document(context),"memory":_document(memory),"transformation_memory":_document(tm),"expert_review":expert,"shortcut_review":_document(shortcut),"quantifier":dict(quantifier.document()),"trace":_document(trace),"framework_binding":dict(binding.document()),"pre_action":dict(pre.document()),"retrieval_bindings":retrieval_bindings,"hook":hook,"gate":gate}


def write_documents():
    for name,doc in build_documents().items():
        path=PATHS[name]; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(doc,indent=2,ensure_ascii=False)+"\n")


if __name__ == "__main__":
    write_documents()
