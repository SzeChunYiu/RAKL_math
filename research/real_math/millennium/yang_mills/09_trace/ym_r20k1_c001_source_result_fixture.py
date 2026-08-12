"""Materialize the source-first YM K1 C001 result.

This fixture evaluates the frozen source and norm obligations before any
target-level scalar or composition claim.  The acquired indexed-author audit
does not bind the required scale-uniform constant family and exact norm scope,
so the target application fails closed.  An elementary abstract scalar lemma
is recorded separately; it has no Yang--Mills application authority without
the missing source bridge.
"""
from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path

from rakl.failure_lattice import (
    FailureDiagnosisStatus,
    FailureExperience,
    FailureExperienceLattice,
    validate_failure_experience,
)
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    audit_research_trace,
)


ATOM = "YM-S1a2i-K1"
CANDIDATE_ID = "YM-S1a2i-K1-C001-SYMBOLIC-NEXT-RADIUS-MARGIN"
CANDIDATE_CORE_SHA256 = "sha256:5ea78a8c0440c99aea881020a030677be6fba1ea5b8cd69e3a6e6f26bab5d48f"
CANDIDATE_ARTIFACT_HASH = "sha256:702fa0ed51394e882d936ac046a162d8dcbcf89423efe4085d435a1e1f38e28d"
CANDIDATE_FREEZE_MERGE = "eea2fe72f0c06de3612589be0103d0fff5812a87"
AUTHORIZATION_MERGE = "cd8ca21bf0cb4b493a374d619d0f3ea5008cf018"
CONTEXT_HASH = "sha256:62b283503fa2f62349dea2b2bb8f67dc65e1b1d944cec01cbd5df8e0bed806ae"
SOURCE_AUDIT_RAW_SHA256 = "5d7f56df67fa566d4d4d066a811127fcf5234534d3274d159c533e29ee70768e"
SOURCE_AUDIT_GIT_BLOB = "1bb1372e783dd805e4f6f97ebd1c5475d100383d"
SOURCE_AUDIT_COMMIT = "c67226cf46fee0a72b492fed23f837593021ca57"

BASE = "research/real_math/millennium/yang_mills"
SOURCE_TEXT = f"{BASE}/03_sources/YM-S1a2i_R20_SOURCE_AUDIT.md"
CANDIDATE = f"{BASE}/04_candidates/YM-S1a2i_K1_C001_SCALAR_MARGIN_CANDIDATE_FREEZE_20260812.json"
AUTHORIZATION = f"{BASE}/09_trace/YM-S1a2i_K1_C001_POST_FREEZE_EVALUATION_AUTHORIZATION_20260812.json"
CANDIDATE_TRACE = f"{BASE}/09_trace/YM-S1a2i_K1_C001_CANDIDATE_FREEZE_TRACE_20260812.json"
PATHS = {
    "source": f"{BASE}/03_sources/YM-S1a2i_K1_C001_SOURCE_SCOPE_AUDIT_20260812.json",
    "result": f"{BASE}/05_oracles/YM-S1a2i_K1_C001_RESULT_20260812.json",
    "lesson": f"{BASE}/07_memory/YM-S1a2i_K1_C001_MATHEMATICAL_LESSON_20260812.json",
    "failure": f"{BASE}/07_memory/YM-S1a2i_K1_C001_FAILURE_EXPERIENCE_20260812.json",
    "dag": f"{BASE}/02_problem_dag/YM-S1a2i_K1_C001_RESULT_DAG_DELTA_20260812.json",
    "trace": f"{BASE}/09_trace/YM-S1a2i_K1_C001_RESULT_TRACE_20260812.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def seal(value: dict) -> dict:
    document = dict(value)
    document["artifact_hash"] = ""
    document["artifact_hash"] = canonical_hash(document)
    return document


def jsonable(value: object) -> object:
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(item) for item in value]
    if hasattr(value, "value"):
        return value.value
    return value


def load(root: Path, relative: str) -> dict:
    value = json.loads((root / relative).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(relative)
    return value


def source_document(root: Path) -> dict:
    raw_sha = hashlib.sha256((root / SOURCE_TEXT).read_bytes()).hexdigest()
    if raw_sha != SOURCE_AUDIT_RAW_SHA256:
        raise RuntimeError("R20 acquired-source audit bytes changed")
    return seal(
        {
            "record_type": "YM_K1_C001_ACQUIRED_SOURCE_UNIFORMITY_AND_NORM_SCOPE_AUDIT",
            "atom_id": ATOM,
            "candidate_id": CANDIDATE_ID,
            "evaluated_obligations_in_frozen_order": [
                "O1-SOURCE-UNIFORMITY",
                "O4-NORM-AND-SCALE-SCOPE",
            ],
            "source_boundary": {
                "citation": "Jonathan J. Wilson (2026), author-uploaded/indexed Yang--Mills manuscript, Section 38, especially equations (573)--(580), Lemmas 38.2--38.4 and Theorem 38.5",
                "acquired_audit_path": SOURCE_TEXT,
                "acquired_audit_raw_sha256": SOURCE_AUDIT_RAW_SHA256,
                "acquired_audit_git_blob": SOURCE_AUDIT_GIT_BLOB,
                "acquired_audit_commit": SOURCE_AUDIT_COMMIT,
                "access_state": "Direct SSRN PDF remains HTTP 403; ResearchGate direct access previously returned HTTP 429/failed fetch. Findings are bounded to the already acquired indexed primary-author text.",
                "global_source_absence_claim": False,
            },
            "required_binding_audit": [
                {
                    "coordinate": "rho",
                    "required": "one finite 0<rho<1 valid uniformly for every admitted scale k",
                    "acquired_evidence": "the indexed audit reports a strict contraction factor rho<1 in equation (573)",
                    "status": "NOT_BOUND_AS_ONE_K_UNIFORM_CONSTANT_FAMILY_BY_ACQUIRED_EVIDENCE",
                },
                {
                    "coordinate": "c_K",
                    "required": "one positive graph-radius coefficient used at every admitted k and at k+1",
                    "acquired_evidence": "the indexed audit reports graph balls with radius c_K g^2",
                    "status": "NOT_BOUND_JOINTLY_WITH_THE_ONE_STEP_ESTIMATE_OVER_ALL_ADMITTED_K",
                },
                {
                    "coordinate": "C_K",
                    "required": "one finite nonnegative coefficient for the exact O(g_k^4) forcing bound, uniform in k",
                    "acquired_evidence": "the indexed audit reports only O(g_k^4) forcing for the K coordinate",
                    "status": "NO_EXACT_K_UNIFORM_FORCING_COEFFICIENT_BOUND_IN_ACQUIRED_AUDIT",
                },
                {
                    "coordinate": "b_0",
                    "required": "one positive cubic base-flow coefficient on the admitted scale range",
                    "acquired_evidence": "the indexed audit reports g'=g-b_0 g^3+r_k",
                    "status": "NOT_BOUND_AS_PART_OF_ONE_JOINT_K_UNIFORM_HYPOTHESIS_PACKET",
                },
                {
                    "coordinate": "C_beta",
                    "required": "one finite nonnegative remainder coefficient with |r_k|<=C_beta g_k^5 uniformly in k",
                    "acquired_evidence": "the indexed audit reports the displayed value-remainder inequality",
                    "status": "NOT_BOUND_AS_PART_OF_ONE_JOINT_K_UNIFORM_HYPOTHESIS_PACKET",
                },
                {
                    "coordinate": "K_norm_and_graph_ball_scope",
                    "required": "the exact scale-indexed norms and graph-ball domain for both ||K_k||_k and ||K_{k+1}||_{k+1}, with one-step theorem quantifiers covering every admitted k",
                    "acquired_evidence": "the indexed audit records scale-labelled K norms and the Section-38 graph-ball discussion",
                    "status": "EXACT_DEFINITIONS_AND_JOINT_THEOREM_SCOPE_NOT_BOUND_BY_ACQUIRED_AUDIT",
                },
            ],
            "obligation_results": {
                "O1-SOURCE-UNIFORMITY": "NOT_DISCHARGED_BY_ACQUIRED_EVIDENCE",
                "O4-NORM-AND-SCALE-SCOPE": "NOT_DISCHARGED_BY_ACQUIRED_EVIDENCE",
            },
            "bounded_conclusion": "The acquired evidence does not bind the exact uniform five-constant family and norm/scale scope required by C001. This does not assert that the inaccessible full source lacks such statements.",
            "classified_branch": "SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT",
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        }
    )


def abstract_scalar_certificate() -> dict:
    return {
        "statement": "For fixed finite real constants 0<rho<1, c_K>0, C_K>=0, b_0>0 and C_beta>=0, there exists epsilon>0 such that L(g)>=0 and M(g)>=0 for every 0<g<=epsilon.",
        "definitions": [
            "L(g)=1-b_0 g^2-C_beta g^4",
            "M(g)=L(g)^2-rho-(C_K/c_K)g^2",
        ],
        "existence_neighborhood_proof": [
            "L and M are polynomials, hence continuous at g=0.",
            "L(0)=1, so choose delta_L>0 such that |g|<delta_L implies |L(g)-1|<1/2 and therefore L(g)>1/2.",
            "M(0)=1-rho>0, so choose delta_M>0 such that |g|<delta_M implies |M(g)-(1-rho)|<(1-rho)/2 and therefore M(g)>(1-rho)/2.",
            "Choose epsilon=(1/2) min(delta_L,delta_M)>0. Then 0<g<=epsilon implies both strict inequalities, hence L(g)>=0 and M(g)>=0.",
        ],
        "conditional_composition_proof": [
            "From g_{k+1}=g_k-b_0 g_k^3+r_k and |r_k|<=C_beta g_k^5, r_k>=-C_beta g_k^5, hence g_{k+1}>=g_k L(g_k).",
            "If L(g_k)>=0 and g_k>0, then g_{k+1}>=g_k L(g_k)>=0 and therefore g_{k+1}^2>=g_k^2 L(g_k)^2.",
            "If M(g_k)>=0, then rho c_K g_k^2+C_K g_k^4<=c_K g_k^2 L(g_k)^2<=c_K g_{k+1}^2.",
            "Thus the K-ball and one-step estimate imply ||K_{k+1}||_{k+1}<=c_K g_{k+1}^2 only conditionally on the exact O1/O4 source and norm hypotheses.",
        ],
        "authority": "ELEMENTARY_ABSTRACT_PROOF_NOT_FORMALIZED",
        "target_application_authority": "NONE_WITHOUT_O1_AND_O4",
    }


def result_document(source: dict, candidate: dict, authorization: dict) -> dict:
    if candidate["artifact_hash"] != CANDIDATE_ARTIFACT_HASH:
        raise RuntimeError("candidate artifact identity mismatch")
    if candidate["candidate_identity"]["canonical_core_sha256"] != CANDIDATE_CORE_SHA256:
        raise RuntimeError("candidate core identity mismatch")
    if authorization["candidate_artifact_hash"] != CANDIDATE_ARTIFACT_HASH:
        raise RuntimeError("authorization/candidate binding mismatch")
    return seal(
        {
            "record_type": "YM_K1_C001_SOURCE_FIRST_RESULT",
            "atom_id": ATOM,
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": CANDIDATE_CORE_SHA256,
            "candidate_artifact_hash": CANDIDATE_ARTIFACT_HASH,
            "candidate_freeze_merge": CANDIDATE_FREEZE_MERGE,
            "post_freeze_authorization_merge": AUTHORIZATION_MERGE,
            "authorized_order_execution": [
                {
                    "obligation": "O1-SOURCE-UNIFORMITY",
                    "result": source["obligation_results"]["O1-SOURCE-UNIFORMITY"],
                },
                {
                    "obligation": "O4-NORM-AND-SCALE-SCOPE",
                    "result": source["obligation_results"]["O4-NORM-AND-SCALE-SCOPE"],
                },
                {
                    "obligation": "O2/O3/O5 target application",
                    "result": "NOT_REACHED_AFTER_FAIL_CLOSED_SOURCE_BRANCH",
                },
                {
                    "obligation": "FROZEN-FALSIFIER",
                    "result": "NOT_IMPORTED_NOT_EXECUTED_AFTER_EARLIER_SOURCE_BRANCH",
                },
            ],
            "abstract_scalar_proposition": abstract_scalar_certificate(),
            "separation_of_results": "The abstract scalar proposition is proved for any fixed admissible finite constants. The Yang--Mills target implication is neither established nor refuted because the acquired source evidence does not discharge the antecedent source/norm hypotheses.",
            "classified_branch": "SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT",
            "candidate_truth_status": "TARGET_APPLICATION_NOT_ESTABLISHED_NOT_REFUTED",
            "source_wide_status": "UNKNOWN_OUTSIDE_ACQUIRED_INDEXED_TEXT",
            "formal_proof": False,
            "independent_review": False,
            "novelty_claim": False,
            "mathematical_result_credit": "SCOPED_SOURCE_SUFFICIENCY_FAILURE_PLUS_ELEMENTARY_ABSTRACT_LEMMA_ONLY",
            "forbidden_scope_preserved": [
                "lambda-coordinate repair",
                "base-map injectivity or full graph transform",
                "Osterwalder--Schrader reconstruction",
                "continuum transport",
                "mass-gap conclusion",
            ],
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        }
    )


def lesson_document(source: dict, result: dict) -> dict:
    return seal(
        {
            "record_type": "YM_K1_C001_SEVEN_FIELD_MATHEMATICAL_LESSON",
            "atom_id": ATOM,
            "attempted_mathematical_implication": "Use a source-scoped k-uniform contraction ||K_{k+1}||_{k+1}<=rho||K_k||_k+C_K g_k^4, the graph radius ||K_k||_k<=c_K g_k^2, and two-sided base-flow control to prove the smaller next-radius bound ||K_{k+1}||_{k+1}<=c_K g_{k+1}^2 for all admitted k at sufficiently small coupling.",
            "exact_mathematical_result_or_failure": "The abstract scalar implication is valid for every fixed finite admissible constant family: continuity at g=0 gives a common positive neighborhood with L>=0 and M>=0, and the signed remainder plus M>=0 yields the desired composition. But the acquired indexed-author evidence does not bind one exact k-uniform family (rho,c_K,C_K,b_0,C_beta) together with the required scale-indexed norm and graph-ball theorem scope. Therefore the target application fails closed as SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT; C001 is not refuted and no Yang--Mills next-radius theorem is established.",
            "supported_and_competing_mathematical_causes": {
                "supported": "The missing bridge is source-level quantifier and norm transport: qualitative strict contraction and O(g^4) forcing do not by themselves instantiate the single uniform family and exact k-to-k+1 norm scope quantified by C001.",
                "competing": [
                    {
                        "cause": "the scalar margin itself may fail even for fixed admissible constants",
                        "status": "REFUTED_ABSTRACTLY_BY_CONTINUITY_AT_G_EQUALS_ZERO",
                    },
                    {
                        "cause": "the full inaccessible source may contain the needed uniform constants and exact norm theorem",
                        "status": "OPEN_NOT_TESTABLE_FROM_ACQUIRED_INDEXED_TEXT",
                    },
                    {
                        "cause": "a different source theorem or a direct derivation may provide the missing O1/O4 bridge",
                        "status": "OPEN",
                    },
                ],
            },
            "scope": "Only the K-coordinate one-step shrinking-radius implication of YM-S1a2i-K1-C001, using the already acquired indexed-author Section-38 evidence. It excludes lambda, base injectivity, the full graph transform, OS reconstruction, continuum transport and the mass gap. It does not claim the inaccessible source globally lacks the needed hypotheses.",
            "mathematical_falsifier": "For the abstract lemma, fixed admissible constants for which no neighborhood of zero has L>=0 and M>=0 would falsify it, but continuity and L(0)=1, M(0)=1-rho>0 exclude such a counterexample. For the target insufficiency classification, an exact source passage binding all five constants uniformly in k and proving the required k-to-k+1 norm/graph-ball scope would falsify the present missing-bridge diagnosis and authorize conditional composition re-evaluation.",
            "repair_or_next_discriminator": "Acquire a verifiable primary-source PDF or equivalent authoritative text and freeze exact page/equation/definition ranges that bind rho,c_K,C_K,b_0,C_beta as one k-uniform family and identify the precise norms/domain in equation (573). If that succeeds, re-run O2/O3/O5 using the already proved abstract lemma; if it fails, preserve the exact missing quantifier or norm bridge rather than inventing constants.",
            "proof_or_source_evidence": [
                PATHS["source"],
                PATHS["result"],
                SOURCE_TEXT,
                "elementary continuity proof for L(0)=1 and M(0)=1-rho>0, recorded in the result artifact",
            ],
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "zero_mathematical_credit": [
                "Git/branch/PR state",
                "CI/tests",
                "schemas/hashes/chronology",
                "telemetry/repository growth",
            ],
        }
    )


def failure_document(lesson: dict) -> dict:
    core = FailureExperience(
        failure_id="F-YM-K1-C001-SOURCE-UNIFORMITY-NORM-BRIDGE-UNBOUND",
        atom_id=ATOM,
        candidate_id=CANDIDATE_ID,
        context_packet_hash=CONTEXT_HASH,
        research_trace_event_id="YM-S1a2i-K1-E10",
        method_family="source-scoped strict-contraction margin for a shrinking O(g^2) K graph radius",
        failure_mode="the acquired indexed-author evidence does not instantiate the exact k-uniform constants and norm/graph-ball scope required by the otherwise valid abstract scalar composition",
        residual_signature=(
            "ABSTRACT_SCALAR_MARGIN_PROVED_FOR_FIXED_ADMISSIBLE_CONSTANTS",
            "K_UNIFORM_FIVE_CONSTANT_SOURCE_BINDING_UNBOUND",
            "EXACT_SCALE_INDEXED_NORM_AND_GRAPH_BALL_SCOPE_UNBOUND",
            "TARGET_NEXT_RADIUS_IMPLICATION_NOT_ESTABLISHED_NOT_REFUTED",
        ),
        broken_assumptions=(
            "qualitative rho<1 and O(g^4) notation suffice to provide one exact coefficient family uniform over every admitted k",
            "scale-labelled norm notation suffices to prove that the one-step estimate and graph-ball radius share the exact required theorem domain",
        ),
        scope_conditions=(
            "only the acquired indexed-author Section-38 evidence recorded by R20",
            "only the irrelevant K-coordinate C001 implication",
            "the inaccessible full source may contain stronger statements and is not globally classified",
            "the method remains reusable if exact O1/O4 source bindings are later supplied",
        ),
        competing_diagnoses=(
            "the scalar margin is mathematically false for fixed admissible constants",
            "the full source contains the exact bridge but current access did not expose it",
            "another derivation can establish the same uniform estimates independently",
            "the required source/norm bridge is genuinely absent in the target construction",
        ),
        selected_diagnosis="SUPPORTED_BOUNDED_EVIDENCE_INSUFFICIENCY: the abstract scalar algebra works, but the acquired source evidence does not discharge O1/O4; no source-wide absence or target impossibility is inferred.",
        diagnosis_status=FailureDiagnosisStatus.SUPPORTED,
        evidence_pointers=(PATHS["source"], PATHS["result"], PATHS["lesson"], SOURCE_TEXT),
        falsifier_or_attempt=lesson["mathematical_falsifier"],
        observed_result=lesson["exact_mathematical_result_or_failure"],
        artifact_hash="",
        timestamp="2026-08-12T12:02:00Z",
        local_repair_attempts=(
            "separated the fixed-constant scalar lemma from source applicability",
            "audited all five required constants before target composition",
            "audited exact k-to-k+1 norm and graph-ball scope before target composition",
            "retained primary-source retrieval as the cheapest next discriminator",
        ),
    )
    experience = replace(core, artifact_hash=canonical_hash(asdict(core)))
    if validate_failure_experience(experience):
        raise RuntimeError(validate_failure_experience(experience))
    return jsonable(asdict(FailureExperienceLattice(experiences=(experience,), links=())))


def dag_document(result: dict, lesson: dict) -> dict:
    return seal(
        {
            "record_type": "YM_K1_C001_RESULT_PROOF_DAG_DELTA",
            "atom_id": ATOM,
            "parent_atom_id": "YM-S1a2i",
            "nodes": [
                {
                    "id": "LEM-YM-K1-C001-ABSTRACT-SCALAR-MARGIN",
                    "status": "PROVED_BY_ELEMENTARY_CONTINUITY_AND_INEQUALITY_ARGUMENT",
                    "scope": "fixed finite constants satisfying 0<rho<1,c_K>0,C_K>=0,b_0>0,C_beta>=0",
                    "pointer": PATHS["result"],
                },
                {
                    "id": "OBL-YM-K1-C001-O1-O4-SOURCE-BRIDGE",
                    "status": "OPEN_ACQUIRED_EVIDENCE_INSUFFICIENT",
                    "scope": "one exact k-uniform constant family and exact scale-indexed K norm/graph-ball theorem domain",
                    "pointer": PATHS["source"],
                },
                {
                    "id": "CLAIM-YM-K1-C001-NEXT-RADIUS-INVARIANCE",
                    "status": "NOT_ESTABLISHED_NOT_REFUTED",
                    "depends_on": [
                        "LEM-YM-K1-C001-ABSTRACT-SCALAR-MARGIN",
                        "OBL-YM-K1-C001-O1-O4-SOURCE-BRIDGE",
                    ],
                },
            ],
            "classified_branch": result["classified_branch"],
            "open_children": [
                "exact primary-source uniformity extraction",
                "exact k-to-k+1 norm and graph-ball scope binding",
                "lambda/backward relevant graph contraction",
                "base-map inverse or reparametrization",
                "OS/continuum/mass-gap interfaces",
            ],
            "next_discriminator": lesson["repair_or_next_discriminator"],
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        }
    )


def _trace_entry(item: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
        event_id=item["event_id"],
        atom_id=item["atom_id"],
        event_type=ResearchTraceEventType(item["event_type"]),
        timestamp=item["timestamp"],
        state_summary=item["state_summary"],
        action_summary=item["action_summary"],
        evidence_pointers=tuple(item["evidence_pointers"]),
        alternatives_considered=tuple(item.get("alternatives_considered", [])),
        decision_rationale=item.get("decision_rationale", ""),
        outputs=tuple(item.get("outputs", [])),
        uncertainties=tuple(item.get("uncertainties", [])),
        residuals=tuple(item.get("residuals", [])),
        next_steps=tuple(item.get("next_steps", [])),
        artifact_hash=item["artifact_hash"],
        previous_event_hash=item.get("previous_event_hash", ""),
    )


def result_trace(candidate_trace: dict, source: dict, result: dict, lesson: dict) -> dict:
    entries = [_trace_entry(item) for item in candidate_trace["entries"]]
    specs = (
        (
            ResearchTraceEventType.PROOF_CHECKED,
            "Post-freeze authorization is public; source-first O1/O4 evaluation is active.",
            "Audit the acquired indexed-author evidence for the exact k-uniform five-constant family and scale-indexed norm/graph-ball scope, and check the elementary abstract scalar proof separately, before any target composition or import of the inert falsifier.",
            (PATHS["source"], AUTHORIZATION),
            (
                "O1:NOT_DISCHARGED_BY_ACQUIRED_EVIDENCE",
                "O4:NOT_DISCHARGED_BY_ACQUIRED_EVIDENCE",
                "ABSTRACT_SCALAR_MARGIN:PROVED_FOR_FIXED_ADMISSIBLE_CONSTANTS",
                "FROZEN_FALSIFIER:NOT_IMPORTED_NOT_EXECUTED",
            ),
            (
                "The inaccessible full source may contain stronger bindings.",
            ),
            (),
        ),
        (
            ResearchTraceEventType.RESULT_RECORDED,
            "The source/norm antecedent is unbound in acquired evidence; target composition stops fail closed.",
            "Classify SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT and record separately the elementary fixed-constant scalar lemma without target promotion.",
            (PATHS["source"], PATHS["result"], PATHS["lesson"]),
            (
                result["classified_branch"],
                "ABSTRACT_SCALAR_MARGIN:PROVED_FOR_FIXED_ADMISSIBLE_CONSTANTS",
                "TARGET_APPLICATION:NOT_ESTABLISHED_NOT_REFUTED",
            ),
            (
                "No exact source constants, numerical threshold or norm bridge are invented.",
            ),
            (),
        ),
        (
            ResearchTraceEventType.RESIDUAL_OPENED,
            "The algebraic margin is no longer the active obstruction; exact source quantifiers and norm transport are.",
            "Open primary-source uniformity and exact scale-indexed norm/domain binding as the next K-coordinate discriminator while retaining all deeper Yang--Mills obligations.",
            (PATHS["failure"], PATHS["dag"]),
            ("O1/O4_SOURCE_BRIDGE_OPEN",),
            (),
            (lesson["repair_or_next_discriminator"],),
        ),
        (
            ResearchTraceEventType.REVIEWED,
            "Role-separated same-context review accepts only the scoped source-insufficiency result and abstract lemma.",
            "Preserve the source-wide uncertainty, reject target/root promotion, and do not call the same-context review independent.",
            (PATHS["source"], PATHS["result"], PATHS["lesson"], PATHS["failure"]),
            (
                "domain: fixed-constant continuity proof is valid",
                "source-transfer: O1/O4 remain unbound",
                "adversarial: inaccessible-source possibility is preserved",
                "formal: no proof-assistant receipt",
                "novelty: no novelty claim",
                "independence: same-context only, zero independent-review credit",
            ),
            (
                "The source-wide existence or absence of the bridge remains unknown.",
            ),
            (lesson["repair_or_next_discriminator"],),
        ),
    )
    for offset, spec in enumerate(specs, 9):
        core = ResearchTraceEntry(
            event_id=f"YM-S1a2i-K1-E{offset:02d}",
            atom_id=ATOM,
            event_type=spec[0],
            timestamp=f"2026-08-12T12:0{offset - 8}:00Z",
            state_summary=spec[1],
            action_summary=spec[2],
            evidence_pointers=spec[3],
            outputs=spec[4],
            uncertainties=spec[5],
            residuals=("SOURCE_UNIFORMITY_AND_NORM_SCOPE_UNBOUND",) if spec[0] is ResearchTraceEventType.RESIDUAL_OPENED else (),
            next_steps=spec[6],
            artifact_hash="",
            previous_event_hash=entries[-1].artifact_hash,
        )
        entries.append(replace(core, artifact_hash=canonical_hash(asdict(core))))
    trace = MathResearchTrace(trace_id="TRACE-YM-S1a2i-K1-C001-RESULT-20260812", entries=tuple(entries))
    report = audit_research_trace(trace)
    if report.verdict.value != "PASS":
        raise RuntimeError(report.reasons)
    return jsonable(asdict(trace))


def build_documents(root: Path = Path(".")) -> dict[str, dict]:
    candidate = load(root, CANDIDATE)
    authorization = load(root, AUTHORIZATION)
    candidate_trace = load(root, CANDIDATE_TRACE)
    source = source_document(root)
    result = result_document(source, candidate, authorization)
    lesson = lesson_document(source, result)
    failure = failure_document(lesson)
    dag = dag_document(result, lesson)
    trace = result_trace(candidate_trace, source, result, lesson)
    return {
        "source": source,
        "result": result,
        "lesson": lesson,
        "failure": failure,
        "dag": dag,
        "trace": trace,
    }


def write(root: Path = Path(".")) -> None:
    for key, value in build_documents(root).items():
        path = root / PATHS[key]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write()
