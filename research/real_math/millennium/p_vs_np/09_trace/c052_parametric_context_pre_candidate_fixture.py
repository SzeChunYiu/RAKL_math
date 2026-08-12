"""Strict prospective C052 support-phase context and pre-candidate gate.

This fixture contains mathematical context and routing authority only.  It has no
new-k enumerator, decoder/SAT import, target selector, classifier candidate,
falsifier implementation, or evaluated result capability.
"""
from __future__ import annotations

from dataclasses import asdict, replace
from enum import Enum
import hashlib
import json

from rakl.failure_lattice import (
    DifferenceWitness,
    FailureDiagnosisStatus,
    FailureExperience,
    FailureExperienceLattice,
    ReuseVerdict,
    add_failure_experience,
    assess_method_reuse,
)
from rakl.framework_candidate_freeze import (
    FrameworkSubjectFreezeBinding,
    FrameworkSubjectRevalidationObservation,
)
from rakl.math_context import AnalogyScanStatus, CrossDomainAnalogy, MathContextFiber, MethodTransfer
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
    StructuralMappingWitness,
    TransformationEpisodeAuthority,
    build_transformation_memory,
)

ATOM = "O9d12a2a1b-C052"
PARENT = "O9d12a2a1b-C051"
ROUND_BASE_SHA = "cc39c7a2553c2e20aa7103652d1429675164016b"
HISTORICAL_PREACTION_SUBJECT_BASE_SHA = "b7ca6ac51fa8319b559e95402c47959c626f284a"
FRAMEWORK_PIN_SHA = "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
FRAMEWORK_CURRENT_SHA = "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
HISTORICAL_PREACTION_APPLICATION_PIN_SHA = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
FRAMEWORK_QUANTIFIER_RUNTIME_SHA256 = "cbbf7c125a505f4914a2253e75e5a809c67fb74e8193cc31d19ab3019938accc"
FRAMEWORK_QUANTIFIER_SCHEMA_SHA256 = "2874ab098fd28941c1e001abdb90b2a164d0af6fe282bbcbdf68bdb38403917f"
FROZEN_AT = "2026-08-12T10:35:00Z"
DECODER_BLOB = "fcc4814dd618da96ef9bb8144a4783a0a6e886e1"
C050_RESULT_BLOB = "f3eaad2496e80aa64b8081868021cc1a89304ef2"
C050_LESSON_BLOB = "b1b574cdd8ba43a4545c00a07bcb50a933c05941"
C050_FAILURE_BLOB = "7da72bf415296c616632bbad0ff16974a73f7737"
C051_RESULT_BLOB = "6bed55d3eb101ff165a72883adb89601d0345c39"
C051_LESSON_BLOB = "55d4bdf451a199f53c51c7fbebd6fb4935428059"
C051_FAILURE_BLOB = "c110b4b096293ee25960f76a327a344ca2beeda7"
PREACTION_BLOB = "70a8e8b2c7fef20ec6a2734c85ba5d809caa1ad4"
BASE = "research/real_math/millennium/p_vs_np"

PATHS = {
    "source_packet": f"{BASE}/01_frontier/O9d12a2a1b_C052_SOURCE_METHOD_TRANSFER_PACKET_20260812.json",
    "context": f"{BASE}/01_frontier/O9d12a2a1b_C052_MATH_CONTEXT_FIBER_20260812.json",
    "atomization": f"{BASE}/02_problem_dag/O9d12a2a1b_C052_ATOMIZATION_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/O9d12a2a1b_C052_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/O9d12a2a1b_C052_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/O9d12a2a1b_C052_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/O9d12a2a1b_C052_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/O9d12a2a1b_C052_SEVEN_ROLE_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/O9d12a2a1b_C052_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "quantifier_witness": f"{BASE}/08_reviews/O9d12a2a1b_C052_QUANTIFIER_COMPATIBILITY_WITNESS_20260812.json",
    "preservation": f"{BASE}/09_trace/O9d12a2a1b_C052_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": f"{BASE}/09_trace/O9d12a2a1b_C052_PRE_CANDIDATE_TRACE_20260812.json",
    "framework_binding": f"{BASE}/09_trace/O9d12a2a1b_C052_FRAMEWORK_SUBJECT_FREEZE_BINDING_20260812.json",
    "framework_observation": f"{BASE}/09_trace/O9d12a2a1b_C052_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "gate": f"{BASE}/09_trace/O9d12a2a1b_C052_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}


def _hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _hex_hash(value: object) -> str:
    return _hash(value).removeprefix("sha256:")


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
    transfers = (
        MethodTransfer(
            source_context="fixed-cell linear Diophantine support and modular word phase",
            method=(
                "within each bit-length cell, rewrite the exact canonical length equation as an affine support "
                "constraint and compute the suffix start modulo the literal-token width before any instance choice"
            ),
            shared_structure=(
                "R=6+2a+2b+3m(1+a) and E=R+(R mod 2)",
                "parent support is E=2k and current support is E'=2(k+1)",
                "payload tokens have width 1+a and the suffix begins at word coordinate k",
                "a fixed MAGIC prefix supplies comparison bits independently of UNSAT semantics",
            ),
            required_assumptions=(
                "a=bit_length(v), b=bit_length(m), and their range constraints remain explicit",
                "support feasibility may depend only on a,b,m, but every forced variable-code bit claim quantifies v and every legal literal index separately inside the bit-length cell",
                "padding is the exact parity bit p=R mod 2 rather than an independent choice",
                "parent and current support variables are not silently identified",
                "no fixed-instance evidence is promoted to a universal class",
            ),
            disanalogies=(
                "bit-length cells vary with a and b, so one global affine equation is insufficient",
                "a phase match or mismatch is syntactic and does not establish canonical UNSAT",
                "an algebraically allowed support tuple need not realize an overlap label",
            ),
            repair_question=(
                "Can a later target-blind classifier partition the exact support cells by suffix phase and forced "
                "MAGIC conflict while retaining escape and unresolved branches?"
            ),
            source_anchors=(
                f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/04_candidates/C041_fx_sat_one_sided.py@blob:{DECODER_BLOB}",
                f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/09_trace/O9d12a2a1b_C052_PARAMETRIC_RESIDUE_PRE_ACTION_20260812.json@blob:{PREACTION_BLOB}",
            ),
        ),
        MethodTransfer(
            source_context="C050 and C051 exact fixed-level forced-coordinate separations",
            method=(
                "retain the two proved fixed-level failures as mandatory regression worlds for a symbolic "
                "support-phase classifier, not as induction bases for a universal theorem"
            ),
            shared_structure=(
                "both levels use the unchanged C041 canonical long form and equal split",
                "both suffix labels meet the fixed current MAGIC prefix",
                "both failures arise before UNSAT semantics from a forced variable-code bit",
            ),
            required_assumptions=(
                "C050 remains scoped to k=15 and C051 to k=19",
                "the classifier must reproduce both exact phase/conflict records",
                "a new class claim must quantify all support variables in its stated domain",
            ),
            disanalogies=(
                "the parent clause counts differ: m=3 versus m=4",
                "current support branches and encoded lengths differ",
                "two repeated instances do not determine every residue or bit-length cell",
                "C051 supplies retrospective mathematical verification, not prospective discovery credit",
            ),
            repair_question=(
                "Which exact support/phase cells inherit a forced conflict, and which cells remain escape-admissible "
                "or unresolved without selecting a new k?"
            ),
            source_anchors=(
                f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C050_K15_PROOF_CHECK_RESULT_20260812.json@blob:{C050_RESULT_BLOB}",
                f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C051_K19_PROOF_RESULT_20260812.json@blob:{C051_RESULT_BLOB}",
            ),
        ),
    )
    analogy = CrossDomainAnalogy(
        source_kind="engineering / cyclic conveyor alignment",
        source_situation=(
            "Items with variable-width repeating slots cross a fixed inspection mask; two observed collisions "
            "motivate tracking slot phase, but every claimed class still needs its own phase-domain proof"
        ),
        common_abstraction=("variable-width periodic block", "moving cut", "fixed comparison mask", "phase-indexed conflict"),
        source_to_target_mapping=(
            "slot width -> literal-token width 1+a",
            "cut position -> suffix start k",
            "inspection mask -> current MAGIC prefix",
            "item class -> exact parent/current support cell",
        ),
        shared_constraints=(
            "phase rather than coarse length controls the local interface",
            "one conflicting coordinate rules out exact synchronization",
            "different widths require separate residue accounting",
        ),
        disanalogies=(
            "the arithmetic code also has gamma headers, padding, and an UNSAT side condition",
            "the analogy supplies no support theorem, forced bit, or overlap result",
        ),
        proposed_principle="index the search by exact phase cells and preserve a hostile escape branch",
        validation_obligation=(
            "a later frozen falsifier must reject universality upon any supported cell without a proved forced conflict"
        ),
        provenance_note="proposal-only engineering analogy; zero theorem authority",
    )
    draft = MathContextFiber(
        atom_id=ATOM,
        object_context=(
            "The exact C041 canonical-code support relation and suffix/prefix interface, represented symbolically "
            "by parent and current bit-length cells, clause counts, parity padding, equal half-length k, and the "
            "suffix-start phase within width-(1+a) literal tokens; no new k is selected."
        ),
        structural_coordinates=(
            "v,m,k are positive integers; a=bit_length(v), b=bit_length(m)",
            "2^(a-1)<=v<=2^a-1 and 2^(b-1)<=m<=2^b-1",
            "header H(a,b)=6+2a+2b and literal-token width w(a)=1+a",
            "raw length R(a,b,m)=H(a,b)+3m w(a)",
            "padding p(a,b,m)=R(a,b,m) mod 2 in {0,1}; encoded length E=R+p",
            "parent support E(a,b,m)=2k; current support E(a_plus,b_plus,m_plus)=2(k+1)",
            "parent suffix-start phase phi_c0=(k-H(a,b)) mod w(a) is the token phase of c[0]=x[k], equivalently h[1]; phase 0=sign and phases 1..a=variable-code bits",
            "label h[0]=1 is prepended and has no parent-token phase; for j>=1, h[j]=x[k+j-1] has token phase (phi_c0+j-1) mod w(a)",
            "although E depends on v only through a, a forced-bit class must quantify every v with 2^(a-1)<=v<=2^a-1 and every legal literal index and sign in every canonical parent word; the analogous rule holds for v_plus",
            "every current canonical prefix begins with MAGIC=11100101, so p[j]=MAGIC[j] for 0<=j<=7",
            "a conflict class requires an explicitly quantified coordinate j and forced unequal bits on every canonical parent/current word in the claimed support cell",
        ),
        equivalent_formulations=(
            "piecewise affine support equations plus congruences inside fixed (a,b,a_plus,b_plus) cells",
            "intersection impossibility via one universally forced suffix-label/MAGIC disagreement",
            "escape admissibility when the exact support system survives but no forced conflict is proved",
            "three-way classifier: FORCED_CONFLICT, ESCAPE_ADMISSIBLE, or UNRESOLVED, with CANNOT_CHECK preserved",
        ),
        solved_analogues=(
            "linear Diophantine support and congruence classification inside one fixed bit-length cell",
            "finite cyclic phase tracking for concatenations of fixed-width tokens",
            "C050 k=15 and C051 k=19 exact forced-coordinate regression worlds",
        ),
        near_solved_analogues=(
            "semilinear language intersections with piecewise bit-length constraints",
            "variable-width word-border problems with a non-regular semantic UNSAT filter",
        ),
        method_transfers=transfers,
        explicit_disanalogies=(
            "C050 and C051 are bounded cases, not induction bases",
            "support and phase classification is not an overlap theorem or a proof of canonical UNSAT",
            "a forced conflict may depend on actual variable-code ranges, not phase alone",
            "an escape-admissible cell is not an overlap witness",
            "the fixed k=13 contaminated branch remains excluded from prospective design and certification",
            "no classifier result is accessed or selected in this round",
            "no finite or parametric code lemma is a cover lower bound, circuit lower bound, or P-versus-NP result",
        ),
        source_anchors=tuple(anchor for transfer in transfers for anchor in transfer.source_anchors),
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(analogy,),
        analogy_scan_notes=(
            "One phase-alignment analogy survives only as a proposal for search organization and a hostile validation obligation."
        ),
        frozen_at=FROZEN_AT,
        first_candidate_at=None,
        packet_hash="",
    )
    return replace(draft, packet_hash=_hash(_document(draft)))


def _parent_failure_lattice() -> tuple[FailureExperienceLattice, FailureExperience, FailureExperience]:
    c050_core = dict(
        failure_id="F-PNP-C050-K15-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
        atom_id="O9d12a2a1b-C050",
        candidate_id="C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1",
        context_packet_hash="sha256:b50f857493e88680bd74943321316451b379c664e0e39d7d2d709f01d5be2a56",
        research_trace_event_id="O9d12a2a1b-C050-E13",
        method_family="literal-transpose suffix-row overlap repair",
        failure_mode="fixed variable-code bit versus canonical MAGIC bit",
        residual_signature=("field-boundary alignment", "fixed variable-code bit versus canonical MAGIC bit", "exact suffix/prefix equality failure", "bounded k-specific obstruction"),
        broken_assumptions=("moving the half-length need not remove the fixed-code/MAGIC obstruction", "multiple current branches do not help when all share the conflicting MAGIC bit"),
        scope_conditions=("k=15 only", "canonical long form and equal split", "exact length-30/32 support branches", "no finite-to-general extrapolation"),
        competing_diagnoses=("H_15 empty", "omitted current branch", "UNSAT semantics creates the bit", "transpose creates separation"),
        selected_diagnosis="The length-30 v=1,m=3 parent forces h[3]=1 while every length-32 current prefix has MAGIC[3]=0.",
        diagnosis_status=FailureDiagnosisStatus.SUPPORTED,
        evidence_pointers=(f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/07_memory/O9d12a2a1b_C050_K15_FAILURE_EXPERIENCE_20260812.json@blob:{C050_FAILURE_BLOB}", f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C050_K15_PROOF_CHECK_RESULT_20260812.json@blob:{C050_RESULT_BLOB}"),
        falsifier_or_attempt="A supported k=15 branch without the forced bit-3 conflict or one exact common label.",
        observed_result="H_15 intersection P_16 is empty by h[3]=1 versus p[3]=0.",
        timestamp="2026-08-12T07:05:33Z",
        local_repair_attempts=("moved from k=12 to k=15", "exhausted padded and unpadded current branches"),
    )
    c051_core = dict(
        failure_id="F-PNP-C051-K19-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
        atom_id="O9d12a2a1b-C051",
        candidate_id="C051-K19-RETROSPECTIVE-SUPPORT-DISCRIMINATOR-v1",
        context_packet_hash="sha256:8a06db5b4fdfcc3a11a7284772a8c4dfd8ccf6b8583438b84ff9bbc7efc2925f",
        research_trace_event_id="O9d12a2a1b-C051-R03",
        method_family="literal-transpose suffix-row overlap repair",
        failure_mode="fixed variable-code bit versus canonical MAGIC bit",
        residual_signature=("field-boundary alignment", "forced variable-code bit versus MAGIC[3]", "bounded exact suffix/prefix disjointness"),
        broken_assumptions=("moving from k=15 to k=19 need not remove the same phase conflict", "repetition at two levels does not imply a universal obstruction"),
        scope_conditions=("k=19 only", "canonical long form and equal split", "parent v=1,m=4", "current v in {4,5,6,7},m=2", "no finite-to-general extrapolation"),
        competing_diagnoses=("H_19 empty", "omitted current v branch", "UNSAT semantics creates the bit", "transpose creates separation"),
        selected_diagnosis="The length-38 v=1,m=4 parent forces h[3]=1 while every length-40 current prefix has MAGIC[3]=0.",
        diagnosis_status=FailureDiagnosisStatus.SUPPORTED,
        evidence_pointers=(f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/07_memory/O9d12a2a1b_C051_K19_FAILURE_EXPERIENCE_20260812.json@blob:{C051_FAILURE_BLOB}", f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C051_K19_PROOF_RESULT_20260812.json@blob:{C051_RESULT_BLOB}"),
        falsifier_or_attempt="A supported k=19 branch without the forced bit-3 conflict or one exact common label.",
        observed_result="H_19 intersection P_20 is empty by h[3]=1 versus p[3]=0.",
        timestamp="2026-08-12T09:54:30Z",
        local_repair_attempts=("rederived exact length-38/40 support", "proved H_19 nonvacuous by an explicit canonical UNSAT word"),
    )
    c050 = FailureExperience(**c050_core, artifact_hash=_hash({"projection": "C052-C050", "source_blob": C050_FAILURE_BLOB, "fields": _jsonable(c050_core)}))
    c051 = FailureExperience(**c051_core, artifact_hash=_hash({"projection": "C052-C051", "source_blob": C051_FAILURE_BLOB, "fields": _jsonable(c051_core)}))
    lattice = add_failure_experience(FailureExperienceLattice(), c050)
    lattice = add_failure_experience(lattice, c051)
    return lattice, c050, c051


def failure_reuse_bundle(context_hash: str):
    lattice, c050, c051 = _parent_failure_lattice()
    witness_c050 = DifferenceWitness(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        method_family=c050.method_family,
        prior_failure_ids=(c050.failure_id,),
        changed_structural_coordinates=(
            "fixed k=15 is replaced by an explicitly quantified support domain with no selected target k",
            "the fixed bit-3 conclusion is replaced by a symbolic phase/forced-coordinate classifier with escape and unresolved branches",
            "C050's exact parent/current tuples become frozen regression inputs rather than a universal premise",
        ),
        restored_or_replaced_assumptions=(
            "replace blind half-length movement by exact support and phase coordinates",
            "replace the unjustified assumption of escape at a later k by a total class partition that may retain the old failure",
        ),
        prior_falsifier_escape_reason=(
            "C052 does not assert escape from C050; it asks whether other explicitly quantified phase cells inherit, escape, or leave unresolved the k=15 conflict"
        ),
        cheapest_repeat_failure_test=(
            "the later classifier/falsifier pair must reproduce the k=15 v=1,m=3 support cell and its h[3]=1 versus MAGIC[3]=0 conflict before any new class is trusted"
        ),
        evidence_pointers=(PATHS["context"], f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C050_K15_PROOF_CHECK_RESULT_20260812.json@blob:{C050_RESULT_BLOB}"),
    )
    witness_c051 = DifferenceWitness(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        method_family=c051.method_family,
        prior_failure_ids=(c051.failure_id,),
        changed_structural_coordinates=(
            "fixed k=19 is replaced by an explicitly quantified support domain with no selected target k",
            "the exact m=4 parent and length-40 current branches become regression inputs inside a symbolic phase classifier",
            "retrospective C051 verification is retained as bounded mathematics but supplies no prospective selection credit",
        ),
        restored_or_replaced_assumptions=(
            "replace split movement as repair by phase-indexed support classification",
            "replace two-case extrapolation by an explicit hostile escape-cell branch and CANNOT_CHECK",
        ),
        prior_falsifier_escape_reason=(
            "C052 does not assert escape from C051; a cell outside the exact k=19 support/phase assumptions is merely unclassified until the later frozen classifier proves its branch"
        ),
        cheapest_repeat_failure_test=(
            "the later classifier/falsifier pair must reproduce the k=19 v=1,m=4 parent cell and all frozen current support branches with the exact bit-3 conflict"
        ),
        evidence_pointers=(PATHS["context"], f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/05_falsification/O9d12a2a1b_C051_K19_PROOF_RESULT_20260812.json@blob:{C051_RESULT_BLOB}"),
    )
    assessments = []
    for witness in (witness_c050, witness_c051):
        assessment = assess_method_reuse(
            lattice,
            target_atom_id=ATOM,
            target_context_hash=context_hash,
            method_family=witness.method_family,
            relevant_failure_ids=witness.prior_failure_ids,
            difference_witness=witness,
        )
        if assessment.verdict is not ReuseVerdict.DIFFERENCE_WITNESSED:
            raise RuntimeError("C052 parent failure reuse did not establish DIFFERENCE_WITNESSED")
        assessments.append(assessment)
    doc = _sealed({
        "schema_version": "1.0.0",
        "snapshot_id": "PNP-C052-FAILURE-SNAPSHOT-20260812",
        "target_atom_id": ATOM,
        "projection_authority": "CANONICAL_SCHEMA_PROJECTION_NO_NEW_FAILURE_OR_MATHEMATICAL_CREDIT",
        "registered_failures": [_jsonable(asdict(c050)), _jsonable(asdict(c051))],
        "difference_witnesses": [_jsonable(asdict(witness_c050)), _jsonable(asdict(witness_c051))],
        "reuse_assessments": [_jsonable(asdict(item)) for item in assessments],
        "global_reuse_rule": "both bounded failures are mandatory regression warnings, never a blacklist or universal theorem",
        "new_level_result_accessed": False,
        "mathematical_credit": False,
    })
    return (witness_c050, witness_c051), tuple(assessments), doc


def memory_review(context_hash: str) -> ResearchMemoryReview:
    _, assessments, failure_snapshot = failure_reuse_bundle(context_hash)
    draft = ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context_hash,
        tool_inventory_snapshot_hash=f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:C049_FIXED_BIT_TOOL_WITH_C050_C051_REUSE_RECORDS",
        failure_lattice_snapshot_hash=_hash(failure_snapshot),
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=(
            "piecewise Diophantine support classifier",
            "modular suffix-phase and forced-coordinate classifier",
            "synchronized code-language product with semantic UNSAT filter deferred",
            "blind next-k scan (negative control only)",
        ),
        relevant_tool_ids=("T-PNP-C049-K12-FIXED-BIT-SEPARATION",),
        relevant_failure_ids=tuple(item.relevant_failure_ids[0] for item in assessments),
        selected_tool_ids=("T-PNP-C049-K12-FIXED-BIT-SEPARATION",),
        tool_applicability_notes=(
            "A proved forced unequal coordinate can certify a scoped disjointness class only after support, phase, and universal bit forcing are proved on that exact class.",
            "C050 and C051 show successful bounded reuse of the coordinate-first operation but do not promote any fixed coordinate or residue to a universal tool.",
        ),
        failure_reuse_notes=(
            "The exact DifferenceWitness against C050 converts k=15 into a mandatory regression world and preserves escape/unresolved branches.",
            "The exact DifferenceWitness against C051 converts k=19 into a separate mandatory regression world; retrospective verification supplies no prospective target-selection credit.",
            "Both executable assessments are DIFFERENCE_WITNESSED; neither asserts that any unexamined class escapes the old falsifier.",
        ),
        unresolved_warnings=(
            "No support-phase class beyond the two parent regression worlds has been classified.",
            "No new k, target residue, forced coordinate, or escape class has been selected.",
            "Syntax classification cannot establish canonical UNSAT or overlap.",
            "K13 remains excluded from prospective design and certification.",
            "Same-context roles are not independent peer review.",
        ),
        evidence_pointers=(PATHS["failure_snapshot"], PATHS["source_packet"], f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/09_trace/O9d12a2a1b_C052_PARAMETRIC_RESIDUE_PRE_ACTION_20260812.json@blob:{PREACTION_BLOB}"),
        artifact_hash="",
    )
    return replace(draft, artifact_hash=_hash(_document(draft)))


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="OBS-PNP-C052-FIXED-K-EVIDENCE-TO-PARAMETRIC-PHASE-CLASSIFIER",
        domain="mathematics / variable-width code synchronization",
        roles=(
            "explicit parent support cell",
            "explicit current support cell",
            "half-length k",
            "literal-token phase phi",
            "fixed MAGIC comparison coordinates",
            "target-blind symbolic classifier",
            "independent hostile supported-tuple falsifier",
        ),
        relations=(
            "parent and current encoded lengths differ by exactly two",
            "the suffix cut at x[k]=c[0]=h[1] induces phase modulo 1+a after the gamma header, while h[0] is a separate prepended bit",
            "h[0]=1 and h[j]=x[k+j-1] while the current prefix starts with MAGIC",
            "C050 and C051 are regression constraints, not universal premises",
        ),
        constraints=(
            "all integer and bit-length quantifiers are explicit",
            "padding is derived from parity",
            "no target k or residue is selected",
            "no decoder, SAT, overlap, or new-level result access",
            "C048 swapped reduction and canonical/fallback boundary are preserved",
        ),
        failure_mechanisms=(
            "blind k progression hides the repeated token phase",
            "two bounded conflicts are overgeneralized to all support cells",
            "an algebraic support cell is mistaken for an overlap or UNSAT witness",
            "a classifier omits a padding, bit-length, or hostile escape branch",
        ),
        invariants_to_preserve=(
            "exact C041 length and code grammar",
            "C048 synchronized intersection meaning",
            "C050/C051 bounded scope",
            "target blindness",
            "OPEN_NO_SOLUTION_CERTIFICATE",
        ),
        desired_transition=(
            "license only the later freeze of a target-blind total support-phase classifier identity and an independent hostile-tuple falsifier identity over the explicit quantifier domain",
        ),
        forbidden_losses=(
            "new-k enumeration",
            "target k or residue selection",
            "finite-to-universal extrapolation",
            "syntax-to-UNSAT promotion",
            "classifier or falsifier execution",
            "cover or root authority escalation",
        ),
    )


def transformation_memory_and_review(context_hash: str, memory_hash: str):
    target = obstruction()
    episode = ObstructionTransformationEpisode(
        episode_id="E-PNP-C052-REPARAMETERIZE-BY-SUPPORT-AND-TOKEN-PHASE",
        source_domain=target.domain,
        source_context="C041 exact length identity plus C050/C051 fixed-level phase-conflict proofs",
        source_obstruction=target,
        transformation_name="REPLACE_BLIND_INSTANCE_PROGRESSION_WITH_EXPLICIT_SUPPORT_PHASE_DOMAIN",
        operation=(
            "rewrite each fixed-k branch as parent/current support equations and a token-phase coordinate, then "
            "freeze a total classifier and hostile supported-tuple falsifier before selecting any result branch"
        ),
        preconditions=(
            "the exact C041 length formula and canonical grammar remain frozen",
            "all parent/current integer, bit-length, parity, phase, and padding quantifiers are explicit",
            "C050 and C051 are reproduced as regression obligations rather than induction premises",
            "escape-admissible, unresolved, and cannot-check outputs remain possible",
            "no target k, decoder, SAT, or overlap result is exposed before candidate/falsifier identity freeze",
        ),
        resulting_relations=target.desired_transition,
        preserved_invariants=target.invariants_to_preserve,
        relaxed_or_broken_constraints=(),
        known_breakpoints=(
            "one support cell is silently omitted",
            "bit-length ranges or parity padding are treated as free",
            "a phase class is called a theorem without universal forced-bit proof",
            "an escape-admissible class is called an overlap witness",
        ),
        evidence_pointers=(PATHS["context"], PATHS["source_packet"], f"git:{HISTORICAL_PREACTION_SUBJECT_BASE_SHA}:{BASE}/09_trace/O9d12a2a1b_C052_PARAMETRIC_RESIDUE_PRE_ACTION_20260812.json@blob:{PREACTION_BLOB}"),
        authority=TransformationEpisodeAuthority.PROOF_BACKED,
        artifact_hash=_hash({"episode": "C052-support-phase-reparameterization", "context": context_hash}),
    )
    tm = build_transformation_memory(
        memory_id="PNP-C052-OBSTRUCTION-TRANSFORMATION-MEMORY-20260812",
        source_universe=(
            "C041 exact canonical code grammar and length identity",
            "C048 exact synchronized-language equivalence",
            "C050 k=15 scoped phase-conflict proof",
            "C051 k=19 retrospective scoped phase-conflict verification",
            "C052 merged pre-action question",
        ),
        episodes=(episode,),
        evidence_pointers=(PATHS["memory"], PATHS["source_packet"]),
    )
    mapping = StructuralMappingWitness(
        witness_id="W-PNP-C052-SUPPORT-PHASE-SEARCH",
        episode_id=episode.episode_id,
        target_obstruction_id=target.obstruction_id,
        role_mapping=(
            ("explicit parent support cell", "explicit parent support cell"),
            ("explicit current support cell", "explicit current support cell"),
            ("half-length k", "half-length k"),
            ("literal-token phase phi", "literal-token phase phi"),
            ("fixed MAGIC comparison coordinates", "fixed MAGIC comparison coordinates"),
            ("target-blind symbolic classifier", "target-blind symbolic classifier"),
            ("independent hostile supported-tuple falsifier", "independent hostile supported-tuple falsifier"),
        ),
        shared_relations=target.relations,
        shared_constraints=target.constraints,
        precondition_mapping=tuple((item, item) for item in episode.preconditions),
        unmatched_source_preconditions=(),
        disanalogies=(
            "C050/C051 prove only two cells; the later classifier must preserve other branches",
            "the source proofs classify disjointness, while this gate licenses only classifier/falsifier identity freeze",
        ),
        target_validation_obligations=(
            "freeze the exact total classifier domain and result branches",
            "freeze an independent hostile supported-tuple falsifier identity",
            "prove both C050 and C051 regression expectations before any new class evaluation",
            "keep target selection and execution unauthorized",
        ),
        evidence_pointers=(PATHS["context"], PATHS["failure_snapshot"], PATHS["quantifier_witness"]),
        artifact_hash=_hash({"mapping": "C052-support-phase", "episode": episode.episode_id, "context": context_hash}),
    )
    review = ObstructionTransformationReview(
        review_id="PNP-C052-OBSTRUCTION-TRANSFORMATION-REVIEW-20260812",
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
            "SEARCH licenses only a later candidate/falsifier identity freeze, not a class result",
            "no target cell has been selected or evaluated",
            "LIFT is neither needed nor authorized",
            "root remains open",
        ),
        evidence_pointers=(PATHS["context"], PATHS["memory"], PATHS["transformation_memory"], PATHS["quantifier_witness"]),
        artifact_hash=_hash({"review": "C052", "memory": tm.snapshot_hash, "mapping": mapping.artifact_hash}),
    )
    return tm, review


def quantifier_witness_document() -> dict:
    content = {
        "schema_version": "quantifier-compatibility-witness-v1",
        "witness_id": "PNP-C052-FIXED-INSTANCE-TO-PARAMETRIC-DOMAIN-WITNESS-20260812",
        "atom_id": ATOM,
        "source_claim_scope": (
            "C050 proves the k=15 support cell and C051 retrospectively verifies the k=19 support cell; C052 asks only to route a later classifier over the explicit support-phase domain"
        ),
        "point_global_scope": "MISALIGNED",
        "time_supremum_scope": "ALIGNED",
        "sequence_limit_scope": "ALIGNED",
        "norm_quantifier_scope": "ALIGNED",
        "point_global_substitution_permitted": "YES",
        "time_supremum_substitution_permitted": "NO",
        "sequence_limit_substitution_permitted": "NO",
        "norm_quantifier_substitution_permitted": "NO",
        "required_scope_witness": "PNP-C052-EXPLICIT-SUPPORT-PHASE-DOMAIN-PLUS-INDEPENDENT-HOSTILE-TUPLE-FALSIFIER-FREEZE",
        "gluing_status": "CONDITIONAL",
        "authority_claim": "ROUTING_GLUING_ONLY_NOT_THEOREM",
        "evidence_pointers": [PATHS["context"], PATHS["failure_snapshot"], f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/quantifier_compatibility.py@sha256:{FRAMEWORK_QUANTIFIER_RUNTIME_SHA256}", f"git:{FRAMEWORK_CURRENT_SHA}:schemas/quantifier-compatibility-witness-v1.schema.json@sha256:{FRAMEWORK_QUANTIFIER_SCHEMA_SHA256}"],
        "recorded_at_utc": FROZEN_AT,
        "condition": (
            "the later classifier quantifies every declared parent/current support variable, preserves regression and hostile escape branches, and is frozen with an independent falsifier identity before any result access"
        ),
        "unknown_fields": [],
        "misaligned_axes_without_substitution": [],
    }
    return {**content, "witness_canonical_sha256": _hex_hash(content)}


def expert_review_document(context_hash: str) -> dict:
    roles = [
        ("circuit_complexity_domain_lead", "The classifier concerns only the C041/C048 code-language interface, not a cover lower bound.", "Keep the C048 map fixed and preserve every downstream bridge as open."),
        ("combinatorics_on_words_lead", "A cut phase inside a variable-width token can control a local border, but actual forced bits depend on the full bit-length cell.", "Classify exact support cells and universal forced coordinates, not residue labels alone."),
        ("diophantine_modular_lead", "The length equation is piecewise affine only after a,b and parity ranges are explicit.", "Quantify v,m,a,b,k,p and independent current variables; derive padding rather than choose it."),
        ("analogy_method_transfer_lead", "Conveyor phase is a useful abstraction but has no gamma, canonicality, or UNSAT semantics.", "Use it only to organize phase cells and a hostile escape test."),
        ("adversarial_falsification_lead", "Two bit-3 conflicts can tempt an invalid universal induction.", "Search first for a supported cell where phase does not force any MAGIC conflict; one such cell refutes universality."),
        ("formal_methods_dependency_lead", "Support, phase, forced-bit universality, canonical parse, UNSAT, overlap, and root implications are distinct obligations.", "Freeze only classifier and falsifier identities next; prohibit decoder/SAT/result execution."),
        ("novelty_research_value_lead", "A parametric partition could explain the repeated morphology, but no partition or theorem exists yet.", "Value explanatory class structure; make no novelty, saturation, or P-versus-NP claim."),
    ]
    return _sealed({
        "schema_version": "1.0.0",
        "review_id": "PNP-C052-SEVEN-ROLE-EXPERT-CONTEXT-REVIEW-20260812",
        "atom_id": ATOM,
        "context_hash": context_hash,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
        "role_reviews": [{"role": role, "objection": objection, "recommendation": recommendation} for role, objection, recommendation in roles],
        "disagreements": [
            "The modular lens permits piecewise support classification; the words lens refuses any forced-bit class until actual variable-code ranges are universally bound.",
            "The domain lens values a later scoped code lemma; the novelty lens denies any current theorem or broader complexity significance.",
        ],
        "strongest_objection": (
            "The repeated k=15 and k=19 bit-3 obstruction does not license a universal quantifier: a single supported phase cell without a universally forced MAGIC conflict defeats the proposed family."
        ),
        "unresolved_uncertainty": [
            "whether any nontrivial support class has a universal forced conflict",
            "whether an explicit escape-admissible support cell exists",
            "whether phase alone suffices or finer variable-code coordinates are required",
        ],
        "next_action_recommendation": (
            "Only after this gate is public, freeze a target-blind total classifier identity and an independent hostile supported-tuple falsifier identity; do not enumerate, select, decode, solve, or report a new level."
        ),
        "independent_review_credit": 0,
        "mathematical_result_credit": False,
    })


def preservation_receipt() -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id="PNP-C052-ROOT-COORDINATE-PRESERVATION-20260812",
        root_claim_id=ATOM,
        root_coordinate="explicit superlogarithmic full-cover family with a valid circuit and P-versus-NP bridge",
        surrogate_coordinate="target-blind parametric classification of C041 support cells by suffix phase and forced MAGIC conflict",
        bridge_edges=(
            BridgeEdge("C052-B1", "support-phase classifier", "scoped code-language obstruction or escape theorem", "requires a frozen total classifier, universal forced-bit proof or exact escape witness, and independent falsification", EdgeProofStatus.UNPROVED, ("classifier identity", "falsifier identity", "all quantified cells covered")),
            BridgeEdge("C052-B2", "scoped code-language theorem", "literal-transpose row collision or obstruction", "requires the exact C048 synchronized-intersection equivalence and retained polarity", EdgeProofStatus.CONDITIONAL, ("C048 map", "canonical language scope")),
            BridgeEdge("C052-B3", "row collision or obstruction", "cover lower bound", "one code-interface class does not supply cover growth or a full-cover obstruction", EdgeProofStatus.UNPROVED, ("uniform family", "cover polarity", "growth proof")),
            BridgeEdge("C052-B4", "cover lower bound", "P versus NP", "requires an explicit asymptotic circuit/complexity bridge", EdgeProofStatus.UNPROVED, ("superlogarithmic bound", "uniformity", "source theorem alignment")),
        ),
        obligations=(
            Obligation("C052-O1", "freeze and later validate the total support-phase classifier and hostile falsifier", True, False),
            Obligation("C052-O2", "prove a scoped parametric obstruction or exact escape class without omitted quantifier branches", True, False),
            Obligation("C052-O3", "connect any code lemma to cover growth", True, False),
            Obligation("C052-O4", "discharge the circuit and P-versus-NP bridge", True, False),
        ),
        known_disanalogies=(
            "phase classification is not canonical UNSAT",
            "escape admissibility is not overlap",
            "a scoped code theorem is not cover growth",
            "two bounded failures are not a universal obstruction",
        ),
        source_authority=CoordinateAuthority.PROPOSAL_ONLY,
        target_authority=CoordinateAuthority.PROPOSAL_ONLY,
        cheapest_hostile_world="a supported parent/current parameter cell whose exact suffix phase forces no disagreement with any compared MAGIC coordinate",
        registered_observations=(
            RegisteredStateObservation("C050", "k15 forced bit-3 conflict", "bounded disjointness only"),
            RegisteredStateObservation("C051", "k19 forced bit-3 conflict", "retrospective bounded disjointness only"),
            RegisteredStateObservation("C052-pre", "classifier and falsifier absent", "root open"),
        ),
        reverification_triggers=("quantifier domain changes", "length or padding formula changes", "a target k is selected", "classifier/falsifier identity is frozen", "a class result or root implication is asserted"),
        prior_failure_ids=("F-PNP-C050-K15-FIXED-VARIABLE-BIT-VERSUS-MAGIC", "F-PNP-C051-K19-FIXED-VARIABLE-BIT-VERSUS-MAGIC"),
    )


def framework_subject(context_hash: str):
    binding = FrameworkSubjectFreezeBinding(
        binding_id="PNP-C052-FRAMEWORK-SUBJECT-FREEZE-20260812",
        authoritative_framework_sha=FRAMEWORK_CURRENT_SHA,
        pre_candidate_packet_hash=context_hash.removeprefix("sha256:"),
        frozen_at_utc=FROZEN_AT,
        evidence_pointers=(
            f"git:{FRAMEWORK_CURRENT_SHA}:RAKL_VERSION.json",
            f"git:{FRAMEWORK_CURRENT_SHA}:skills/rakl-core/workflows/mathematical-research.md",
            f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/quantifier_compatibility.py@sha256:{FRAMEWORK_QUANTIFIER_RUNTIME_SHA256}",
            f"git:{FRAMEWORK_CURRENT_SHA}:schemas/quantifier-compatibility-witness-v1.schema.json@sha256:{FRAMEWORK_QUANTIFIER_SCHEMA_SHA256}",
            f"git:{FRAMEWORK_PIN_SHA}:config/rakl-framework-pin.json",
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=FRAMEWORK_CURRENT_SHA,
        intervening_diff=(),
        observation_evidence_pointers=(f"git-ls-remote:SzeChunYiu/RAKL:refs/heads/main:{FRAMEWORK_CURRENT_SHA}", f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/quantifier_compatibility.py"),
    )
    return binding, observation


def trace(context_hash: str, memory_hash: str, shortcut_hash: str, quantifier_hash: str) -> MathResearchTrace:
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
        ResearchTraceEventType.NEXT_STEP_PROPOSED: PATHS["quantifier_witness"],
    }
    entries = []
    previous = ""
    for index, kind in enumerate(kinds, 1):
        outputs = ["PRE_CANDIDATE_ONLY", "NO_NEW_LEVEL_RESULT_ACCESS", "NO_TARGET_K_SELECTED", "ZERO_PROCESS_MATHEMATICAL_CREDIT"]
        if kind is ResearchTraceEventType.CONTEXT_FROZEN:
            outputs.insert(0, context_hash)
        if kind is ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW:
            outputs.insert(0, memory_hash)
        if kind is ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW:
            outputs[:0] = [shortcut_hash, "selected_mode:SEARCH"]
        if kind is ResearchTraceEventType.NEXT_STEP_PROPOSED:
            outputs[:0] = [f"quantifier_witness:{quantifier_hash}", "LICENSE_IDENTITY_FREEZE_ONLY"]
        payload = {
            "event_id": f"O9d12a2a1b-C052-E{index:02d}",
            "atom_id": ATOM,
            "event_type": kind.value,
            "timestamp": f"2026-08-12T10:35:{index:02d}Z",
            "state_summary": (
                "C052 replaces blind later-k progression with the explicit C041 support/phase coordinate system. C050 and C051 are bounded regression worlds only. No new k, residue, forced coordinate, escape class, classifier identity, falsifier identity, decoder/SAT state, overlap result, or theorem candidate exists."
            ),
            "action_summary": kind.value,
            "evidence_pointers": [evidence[kind]],
            "alternatives_considered": ["blind next-k scan", "universalize the repeated bit-3 conflict", "change the encoding or split", "freeze only a later target-blind support-phase classifier and hostile falsifier identity"],
            "decision_rationale": (
                "The exact mathematical lessons identify suffix phase as the repeated causal coordinate, while their bounded scopes and the live quantifier witness forbid finite-to-global promotion without an explicit domain and falsifier."
            ),
            "outputs": outputs,
            "uncertainties": ["no nontrivial parametric class proved", "same-context review is not independent"],
            "residuals": ["support-phase classification unexecuted", "forced-conflict and escape classes unresolved", "UNSAT and overlap obligations untouched", "root OPEN_NO_SOLUTION_CERTIFICATE"],
            "next_steps": ["after public merge, freeze a target-blind total classifier identity and an independent hostile supported-tuple falsifier identity", "do not select or enumerate a target k", "do not import or execute decoder, SAT, overlap, or result capability", "freeze all result branches before later evaluation"],
            "previous_event_hash": previous,
        }
        artifact_hash = _hash(payload)
        entries.append(ResearchTraceEntry(artifact_hash=artifact_hash, **{**payload, "event_type": kind}))
        previous = artifact_hash
    return MathResearchTrace("PNP-O9d12a2a1b-C052-PRE-CANDIDATE-TRACE-20260812", tuple(entries))


def source_packet_document() -> dict:
    fields = ("attempted_implication", "exact_result_or_failure", "supported_and_competing_causes", "scope", "proof_and_source_evidence", "falsifier", "mathematical_repair")
    c050 = {
        "attempted_implication": "Moving from k=12 to the prospectively selected k=15 split might produce H_15 intersection P_16 nonempty.",
        "exact_result_or_failure": "H_15 intersection P_16 is empty: every H_15 label has h[3]=1 and every P_16 prefix has p[3]=MAGIC[3]=0.",
        "supported_and_competing_causes": "Supported bounded cause is the v=1 variable-code bit at the moved cut; H_15 vacuity, omitted current branches, UNSAT as the bit source, and transpose as the source are rejected.",
        "scope": "Exactly k=15, the canonical length-30/32 branches, unchanged equal split, and C048 reduction; no other k or root conclusion.",
        "proof_and_source_evidence": f"C050 hand/symbolic certificate and proof record at blob {C050_RESULT_BLOB}; computation and process metadata receive zero mathematical credit.",
        "falsifier": "A supported k=15 branch without h[3]=1 versus p[3]=0, an omitted branch, or one exact common label.",
        "mathematical_repair": "Rederive support, cut phase, and forced coordinates for any successor rather than assuming half-length movement repairs alignment.",
    }
    c051 = {
        "attempted_implication": "Changing from k=15 to k=19 might make the canonical UNSAT suffix label compatible with the next canonical prefix.",
        "exact_result_or_failure": "H_19 intersection P_20 is empty: every H_19 label has h[3]=1 and every P_20 prefix has p[3]=MAGIC[3]=0.",
        "supported_and_competing_causes": "Supported bounded cause is the repeated v=1 token phase; H_19 vacuity, omitted current v branches, UNSAT as the bit source, and transpose as the source are rejected.",
        "scope": "Exactly k=19, parent v=1,m=4, current v in {4,5,6,7},m=2, unchanged equal split and C048 reduction; retrospective verification only.",
        "proof_and_source_evidence": f"C051 exact proof certificate and retrospective proof record at blob {C051_RESULT_BLOB}; no prospective discovery credit.",
        "falsifier": "A supported k=19 branch without h[3]=1 versus p[3]=0, an omitted branch, or one exact common label.",
        "mathematical_repair": "Classify the exact suffix-start residue and forced coordinate before semantic work; preserve an explicit escape class instead of extrapolating two cases.",
    }
    assert set(c050) == set(fields) and set(c051) == set(fields)
    return _sealed({
        "schema_version": "1.0.0",
        "packet_id": "PNP-C052-SOURCE-METHOD-TRANSFER-PACKET-20260812",
        "atom_id": ATOM,
        "retrieved_before_candidate": True,
        "parent_seven_field_mathematical_lessons": [
            {"source_atom": "O9d12a2a1b-C050", "lesson_id": "MATH-PNP-C050-K15-FIXED-CODE-MAGIC-SEPARATION", "fields": c050},
            {"source_atom": "O9d12a2a1b-C051", "lesson_id": "MATH-PNP-C051-K19-FIXED-CODE-MAGIC-SEPARATION", "fields": c051},
        ],
        "method_transfer_matrix": [
            {"source_context": "fixed bit-length cell", "method": "affine support plus modular phase", "works_because": "a,b fix gamma widths and 1+a fixes token width", "broken_assumption": "a,b vary globally", "repair_question": "partition by exact bit-length cells"},
            {"source_context": "C050/C051 fixed conflicts", "method": "coordinate-first regression", "works_because": "one universal unequal coordinate proves scoped disjointness", "broken_assumption": "two cells do not cover the family", "repair_question": "retain total branches and hostile escape cells"},
        ],
        "quantifier_domain": {
            "parent": "forall k,a,b,m,v with positive integers, bit-length range constraints, derived padding p, and E(a,b,m)=2k",
            "current": "forall a_plus,b_plus,m_plus,v_plus with positive integers, bit-length range constraints, derived padding p_plus, and E(a_plus,b_plus,m_plus)=2(k+1)",
            "support_vs_content": "support depends on v only through a, but any forced variable-code bit assertion is universal over each v in its a-cell and every legal literal index/sign in every canonical word; likewise for v_plus",
            "phase": "phi_c0=(k-(6+2a+2b)) mod (1+a) is the phase of c[0]=x[k]=h[1]; h[0] is prepended, and phase(h[j])=(phi_c0+j-1) mod (1+a) for j>=1",
            "claim_scope": "every tuple in an explicitly frozen class; no inference from k=15 and k=19 alone",
        },
        "authority": "SOURCE_AND_METHOD_TRANSFER_CONTEXT_ONLY_NO_PARAMETRIC_RESULT",
        "credit": {"mathematical_results": 0, "git_ci_schema_hash_chronology": 0, "independent_review": 0},
    })


def build_current_gate_plan():
    fiber = context()
    memory = memory_review(fiber.packet_hash)
    tm, shortcut = transformation_memory_and_review(fiber.packet_hash, memory.artifact_hash)
    quantifier = quantifier_witness_document()
    research_trace = trace(fiber.packet_hash, memory.artifact_hash, shortcut.artifact_hash, quantifier["witness_canonical_sha256"])
    preservation = preservation_receipt()
    binding, observation = framework_subject(fiber.packet_hash)
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("C041 piecewise support cells", "parent suffix phase", "current MAGIC prefix", "C050/C051 regression worlds", "future classifier and hostile falsifier identities"),
            relations=("encoded-length support", "bit-length range", "parity padding", "modular token phase", "forced-coordinate conflict", "quantifier compatibility"),
            domain="circuit complexity / variable-width code-language synchronization",
            goal_type="license only a later target-blind classifier and independent falsifier identity freeze without selecting or evaluating a new level",
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


def build_documents() -> dict[str, dict]:
    plan, fiber, memory, tm, shortcut, research_trace, preservation = build_current_gate_plan()
    source = source_packet_document()
    quantifier = quantifier_witness_document()
    atomization = _sealed({
        "schema_version": "1.0.0",
        "atomization_id": "PNP-C052-ATOMIZATION-20260812",
        "recorded_at": FROZEN_AT,
        "atom_id": ATOM,
        "parent_atom_id": PARENT,
        "object": "The exact parametric support/phase system of the frozen C041 canonical code and C048 synchronized suffix/prefix interface, before any new target level is chosen.",
        "qoi": "PARAMETRIC_SUPPORT_PHASE_CLASSIFIER_IDENTITY_AND_FALSIFIER_PERMISSION",
        "allowed_later_result_branches": ["SCOPED_PARAMETRIC_OBSTRUCTION_CLASS", "EXPLICIT_ESCAPE_RESIDUE_CLASS", "MIXED_CLASSIFICATION_WITH_OPEN_BRANCHES", "CANNOT_CHECK"],
        "atomic_obligations": ["quantify parent/current k,a,b,m,v,phase,and derived padding", "reproduce C050 and C051 as separate regression worlds", "preserve hostile escape and unresolved branches", "freeze later classifier and independent falsifier identities before result access", "do not enumerate or select a new k", "do not import decoder/SAT/overlap capability", "do not state a parametric theorem candidate"],
        "candidate_generation_allowed_by_document": False,
        "candidate_proposed": False,
        "classifier_identity": None,
        "falsifier_identity": None,
        "parent_results_accessed": ["C050-k15", "C051-k19-retrospective"],
        "new_level_result_accessed": False,
        "target_k_selected": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
        "application_subject_binding": {
            "round_branch_base_commit": ROUND_BASE_SHA,
            "historical_preaction_subject_base_commit": HISTORICAL_PREACTION_SUBJECT_BASE_SHA,
            "distinction": "The C052 context round starts from cc39c7a; b7ca6ac is retained only as the immutable mathematical/source subject of the already merged C052 pre-action.",
        },
        "authority_boundary": {"assurance_only_zero_credit": True, "grants_parametric_theorem": False, "grants_cover_lower_bound": False, "grants_p_vs_np_authority": False},
    })
    tool_snapshot = _sealed({
        "schema_version": "1.0.0",
        "snapshot_id": "PNP-C052-TOOL-SNAPSHOT-20260812",
        "target_atom_id": ATOM,
        "round_branch_base_commit": ROUND_BASE_SHA,
        "historical_preaction_subject_base_commit": HISTORICAL_PREACTION_SUBJECT_BASE_SHA,
        "tools": [{"tool_id": "T-PNP-C049-K12-FIXED-BIT-SEPARATION", "operation": "prove one universal unequal coordinate only after exact target support and alignment are established", "successful_bounded_reuse": ["C050-k15", "C051-k19-retrospective"], "preconditions": ["explicit support domain", "exact cut phase", "universal bit forcing on the claimed class"], "guarantees": ["one proved unequal coordinate certifies disjointness only on the exact class"], "non_guarantees": ["no fixed coordinate, residue, or class transfers automatically", "no UNSAT, overlap, cover, or root authority"]}],
        "mathematical_credit": False,
    })
    _, reuse_assessments, failure_snapshot = failure_reuse_bundle(fiber.packet_hash)
    if any(item.verdict is not ReuseVerdict.DIFFERENCE_WITNESSED for item in reuse_assessments):
        raise RuntimeError("C052 failure reuse not licensed")
    expert = expert_review_document(fiber.packet_hash)
    binding, observation = framework_subject(fiber.packet_hash)
    binding_document = _sealed(dict(binding.document()))
    observation_document = _sealed({
        "schema_version": "framework-subject-revalidation-observation-v1",
        "observation_id": "PNP-C052-FRAMEWORK-SUBJECT-REVALIDATION-20260812",
        "observed_current_main_sha": observation.observed_current_main_sha,
        "intervening_diff": [],
        "observation_evidence_pointers": list(observation.observation_evidence_pointers),
        "verdict": plan.framework_subject_gate.verdict.value,
        "licenses_candidate_materialization": plan.framework_subject_gate.licenses_candidate_materialization,
        "application_pin": FRAMEWORK_PIN_SHA,
        "historical_preaction_application_pin": HISTORICAL_PREACTION_APPLICATION_PIN_SHA,
        "historical_pin_scope": "The 5dc0627 pin belongs only to the already merged C052 pre-action and is not the framework pin, runtime, or current-main subject of this context round.",
        "pin_lacks_live_quantifier_runtime": False,
        "live_quantifier_semantics_adopted": True,
        "grants_scientific_authority": False,
    })
    documents = {
        "source_packet": source,
        "context": _document(fiber),
        "atomization": atomization,
        "tool_snapshot": tool_snapshot,
        "failure_snapshot": failure_snapshot,
        "memory": _document(memory),
        "transformation_memory": _document(tm),
        "expert_review": expert,
        "shortcut_review": _document(shortcut),
        "quantifier_witness": quantifier,
        "preservation": _jsonable(preservation.document()),
        "trace": _document(research_trace),
        "framework_binding": binding_document,
        "framework_observation": observation_document,
    }
    integrity = {"algorithm": "SHA-256", "canonicalization": "JSON_SORT_KEYS_COMPACT_UTF8", "inputs": {name: {"path": PATHS[name], "canonical_sha256": _hash(document)} for name, document in sorted(documents.items())}}
    documents["gate"] = _sealed({
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C052-PRE-CANDIDATE-GATE-20260812",
        "application_base_commit": ROUND_BASE_SHA,
        "round_branch_base_commit": ROUND_BASE_SHA,
        "historical_preaction_subject_base_commit": HISTORICAL_PREACTION_SUBJECT_BASE_SHA,
        "application_subject_distinction": "cc39c7a is the base of this context round; b7ca6ac is only the historical frozen subject/base recorded by the merged pre-action.",
        "framework_current_commit": FRAMEWORK_CURRENT_SHA,
        "framework_application_pin": FRAMEWORK_PIN_SHA,
        "framework_runtime_commit": FRAMEWORK_CURRENT_SHA,
        "historical_preaction_application_pin": HISTORICAL_PREACTION_APPLICATION_PIN_SHA,
        "historical_preaction_pin_scope": "5dc0627 is provenance for the merged C052 pre-action only; it is not an active framework binding for this round.",
        "framework_method_version": "3.0.0",
        "atom_id": ATOM,
        "artifact_bindings": {"context_hash": fiber.packet_hash, "memory_review_hash": memory.artifact_hash, "transformation_memory_snapshot_hash": tm.snapshot_hash, "shortcut_review_hash": shortcut.artifact_hash, "quantifier_witness_sha256": quantifier["witness_canonical_sha256"], "trace_last_event_hash": research_trace.entries[-1].artifact_hash, "preservation_sha256": preservation.document()["receipt_canonical_sha256"], "framework_subject_binding_sha256": binding.binding_canonical_sha256, "full_document_integrity_hash": _hash(integrity)},
        "full_document_integrity": integrity,
        "gate_verdicts": {"context": plan.context_gate.verdict.value, "dual_memory": plan.memory_gate.verdict.value, "obstruction_transformation": plan.shortcut_gate.verdict.value, "trace": plan.trace_gate.verdict.value, "preservation": plan.preservation_gate.verdict.value, "framework_subject": plan.framework_subject_gate.verdict.value, "selected_mode": shortcut.selected_mode.value, "candidate_generation_allowed": plan.candidate_generation_allowed, "licensed_action": "FREEZE_C052_TARGET_BLIND_CLASSIFIER_AND_INDEPENDENT_FALSIFIER_IDENTITIES_ONLY"},
        "application_authority": {"candidate_construction_authorized": True, "only_identity_freeze_authorized": True, "target_blind_operator_required": True, "classifier_execution_authorized": False, "falsifier_execution_authorized": False, "new_k_enumeration_authorized": False, "target_k_selection_authorized": False, "decoder_sat_overlap_access_authorized": False, "parametric_theorem_candidate_authorized": False},
        "chronology": {"candidate_identity": None, "falsifier_identity": None, "candidate_proposed": False, "new_level_result_accessed": False, "target_k_selected": False, "next_public_freeze": "PENDING_TARGET_BLIND_CLASSIFIER_PLUS_FALSIFIER_IDENTITY_PR"},
        "authority": {"assurance_only": True, "mathematical_result_credit": False, "mathematical_saturation_credit": False, "git_ci_schema_hash_chronology_credit": 0, "grants_theorem_truth": False, "grants_novelty": False, "grants_independent_review": False, "grants_cover_or_p_vs_np_authority": False},
    })
    return documents


def write_documents(root=".") -> None:
    from pathlib import Path
    base = Path(root)
    for name, document in build_documents().items():
        path = base / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_documents()
