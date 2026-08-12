"""Materialize the RH ANA-003j D001 exact-source audit result.

The public D001 discriminator is evaluated against the exact C002, Bellotti v1,
and finite Laguerre inputs.  The source supports a conditional envelope once two
hidden Bellotti constants are named, but it does not expose those constants or
the sufficiently-large-x threshold.  Consequently no source-complete explicit
modulus, target tolerance sequence, cutoff constant, or diagonal comparison is
materialized.
"""
from __future__ import annotations

from dataclasses import asdict, replace
from enum import Enum
import hashlib
import json
from pathlib import Path

from rakl.failure_lattice import (
    FailureDiagnosisStatus,
    FailureExperience,
    FailureExperienceLattice,
    FailureLink,
    FailureRelation,
    validate_failure_experience,
)
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, audit_research_trace


ROOT = Path(__file__).resolve().parents[5]
ATOM = "RH-ANA-003j"
DISCRIMINATOR_ID = "RH-ANA-003j-D001-C002-EXPLICIT-BOUNDARY-TAIL-MODULUS-SOURCE-AUDIT"
APPLICATION_BASE_SHA = "b42535ea717f239ecc4402a74732bb45bbae77e1"
FREEZE_MERGE_SHA = APPLICATION_BASE_SHA
FREEZE_RAW_SHA256 = "9cd428ff6511796237ffc312f54cddab0e458e857e82ddb3b8baf3c125faf521"
FREEZE_GIT_BLOB = "e3f00958c8c2e07d803baf7556bc52cbe6fe15b6"
FRAMEWORK_LIVE_SHA = "6756ebec40b90f327d879410539f5146e188f34d"
CONTEXT_HASH = "sha256:08dc06f14c732d28d179d74ed109b0ee8f8af5efb8dce3895427c333ea3fb580"
BELLOTTI_PDF_SHA256 = "39a39e3dbc73506cf5dfd0b8a18b24e85302d305fa3059a60abcfa6f23292568"
DGS_PDF_SHA256 = "e93985f8ede2799f6e9f3b12dad2565228fefa0b1f662306e2caf9768d2b423c"
BASE = "research/real_math/millennium/riemann_hypothesis"
FREEZE = f"{BASE}/09_trace/RH_ANA_003j_MODULUS_SOURCE_DISCRIMINATOR_FREEZE_20260812.json"
PARENT_TRACE = f"{BASE}/09_trace/RH_ANA_003j_PRE_CANDIDATE_TRACE_20260812.json"
C002_CANDIDATE = f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_FIXED_N_ABEL_CANDIDATE_FREEZE_20260812.json"
C002_CERTIFICATE = f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_HAND_PROOF_CERTIFICATE_FREEZE_20260812.json"
C002_RESULT = f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json"
ANA2_FAILURE = f"{BASE}/07_memory/RH_ANA_002_POSTAUDIT_FAILURE_EXPERIENCE_LATTICE_20260811.json"
PATHS = {
    "source": f"{BASE}/03_sources/RH_ANA_003j_D001_EXACT_SOURCE_SCOPE_AUDIT_20260812.json",
    "result": f"{BASE}/05_oracles/RH_ANA_003j_D001_MODULUS_SOURCE_RESULT_20260812.json",
    "lesson": f"{BASE}/07_memory/RH_ANA_003j_D001_MATHEMATICAL_LESSON_20260812.json",
    "failure": f"{BASE}/07_memory/RH_ANA_003j_D001_FAILURE_EXPERIENCE_20260812.json",
    "dag": f"{BASE}/02_problem_dag/RH_ANA_003j_D001_RESULT_DAG_DELTA_20260812.json",
    "review": f"{BASE}/08_reviews/RH_ANA_003j_D001_SAME_CONTEXT_RESULT_REVIEW_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003j_D001_RESULT_TRACE_20260812.json",
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
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    return value


def load(root: Path, relative: str) -> dict:
    value = json.loads((root / relative).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(relative)
    return value


def raw_sha256(root: Path, relative: str) -> str:
    return hashlib.sha256((root / relative).read_bytes()).hexdigest()


def source_document(root: Path) -> dict:
    freeze_sha = raw_sha256(root, FREEZE)
    if freeze_sha != FREEZE_RAW_SHA256:
        raise RuntimeError("D001 public freeze byte identity mismatch")
    c002 = load(root, C002_RESULT)
    if c002["exact_mathematical_result"]["quantifiers"] != "for every fixed integer n>=1 and every nonintegral real X>=1":
        raise RuntimeError("C002 quantifier scope changed")
    return seal({
        "record_type": "RH_ANA003J_D001_EXACT_ACQUIRED_SOURCE_SCOPE_AUDIT",
        "atom_id": ATOM,
        "discriminator_id": DISCRIMINATOR_ID,
        "freeze_binding": {
            "public_merge_sha": FREEZE_MERGE_SHA,
            "path": FREEZE,
            "raw_sha256": FREEZE_RAW_SHA256,
            "git_blob": FREEZE_GIT_BLOB,
            "access_after_public_freeze": True,
        },
        "framework_observation": {
            "latest_observed_main_sha": FRAMEWORK_LIVE_SHA,
            "application_gitlink_edited": False,
            "classification": "PAPER1_PROJECTION_ONLY_AFTER_PRIOR_PAPER3_REGISTRATION_NO_MATHEMATICAL_GATE_CHANGE",
            "grants_mathematical_authority": False,
        },
        "exact_sources": [
            {
                "source_id": "C002-FIXED-N-NATURAL-ORDER-ABEL",
                "paths": [C002_CANDIDATE, C002_CERTIFICATE, C002_RESULT],
                "authorized_use": "exact natural-order boundary-plus-tail identity for each fixed n; no n-uniform or quantitative modulus authority",
                "observed_statement": "For fixed n and nonintegral X, the tail is -A(X)b_n(X)-integral_X^infinity A(t)b_n'(t)dt.",
            },
            {
                "source_id": "BELLOTTI-2508.02041v1",
                "citation": "Chiara Bellotti, A new zero-density estimate for zeta(s) and the error term in the prime number theorem, arXiv:2508.02041v1",
                "url": "https://arxiv.org/pdf/2508.02041v1",
                "pdf_sha256": BELLOTTI_PDF_SHA256,
                "anchors": ["Theorem 1.5, page 3", "proof of Theorem 1.5, pages 14-15", "equations (1.3), (1.4), and (5.2)"],
                "exact_scope_observed": [
                    "Theorem 1.5 states Delta(x) << exp(55 A_0) exp(-omega(x)).",
                    "Equation (1.4) gives omega(x)=d(log x)^(3/5)/(log log x)^(1/5), with d=(5^6 A_0^3/(2^2 3^4))^(1/5).",
                    "The proof begins 'Let x be sufficiently large', introduces an 'absolute large positive constant' H, and retains O and << constants through (5.2).",
                    "The introduction says the zero-density results can be made fully explicit, but the paper focuses on the theoretical aspect; it does not materialize a numerical Theorem-1.5 implied constant and validity threshold.",
                ],
                "exposed_constants": ["A_0 symbol", "d as an explicit function of A_0", "factor exp(55 A_0)"],
                "unexposed_required_constants": [
                    "a numerical or otherwise explicitly bound absolute implied constant K_B for Theorem 1.5",
                    "an explicit sufficiently-large-x threshold x_B on which the theorem bound holds",
                ],
                "ineffectivity_claimed": False,
                "global_source_absence_claimed": False,
            },
            {
                "source_id": "DUNSTER-GIL-SEGURA-1705.01190v1",
                "citation": "T. M. Dunster, A. Gil, and J. Segura, Uniform asymptotic expansions for Laguerre polynomials and related confluent hypergeometric functions, arXiv:1705.01190v1",
                "url": "https://arxiv.org/pdf/1705.01190v1",
                "pdf_sha256": DGS_PDF_SHA256,
                "anchor": "equation (1.1), page 2",
                "authorized_use": "exact finite Laguerre normalization only; no asymptotic remainder imported",
                "specialization": "L_(n-1)^(1)(u)=sum_(j=0)^(n-1) (-1)^j binom(n,j+1) u^j/j!",
            },
        ],
        "source_obligation_results": [
            {"obligation": "Bellotti absolute implied constant and dependency scope", "status": "NOT_EXPLICITLY_EXPOSED_BY_ACQUIRED_V1"},
            {"obligation": "Bellotti sufficiently-large-x threshold and dependency scope", "status": "NOT_EXPLICITLY_EXPOSED_BY_ACQUIRED_V1"},
            {"obligation": "exact coefficient norm for L_(n-1)^(1)", "status": "DERIVABLE_AS_FINITE_EXPRESSION_IN_N"},
            {"obligation": "exact coefficient norm for (L_(n-1)^(1))'-L_(n-1)^(1)", "status": "DERIVABLE_AS_FINITE_EXPRESSION_IN_N"},
            {"obligation": "quantitative boundary and transformed-tail bound", "status": "DERIVABLE_CONDITIONALLY_ON_K_B_AND_X_B"},
            {"obligation": "forall-Y modulus validity", "status": "DERIVABLE_CONDITIONALLY_ON_K_B_AND_X_B"},
        ],
        "selected_result_branch": "QUALITATIVE_OR_INEFFECTIVE_SOURCE_ONLY_NO_EXPLICIT_MODULUS",
        "branch_precision": (
            "The selected disjunct is QUALITATIVE/UNEXPOSED, not a proof of ineffectivity: the acquired v1 theorem uses << and sufficiently-large x without binding K_B or x_B. "
            "The finite Laguerre coordinates and a conditional envelope are derivable, but the frozen source-complete explicit modulus is not."
        ),
        "other_branches": {
            "EXPLICIT_SOURCE_DERIVED_MODULUS_MATERIALIZED": "NOT_SELECTED_MISSING_K_B_AND_X_B",
            "ACQUIRED_SOURCE_SCOPE_INSUFFICIENT_FOR_ONE_OR_MORE_REQUIRED_CONSTANTS": "SECONDARY_DIAGNOSIS_SUBSUMED_BY_SELECTED_QUALITATIVE_UNEXPOSED_BRANCH",
            "SOURCE_STATEMENT_OR_NORMALIZATION_MISMATCH": "NOT_SELECTED_BOTH_BOUND_AND_NORMALIZATION_ARE_PRESENT",
            "CANNOT_CHECK_EXACT_SOURCE_SCOPE": "NOT_SELECTED_EXACT_V1_PDFS_WERE_RETRIEVED_AND_HASH_MATCHED",
        },
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def conditional_envelope_certificate() -> dict:
    return {
        "authority": "SAME_CONTEXT_HAND_DERIVATION_CONDITIONAL_ON_UNEXPOSED_BELLOTTI_CONSTANTS",
        "definitions": [
            "P_n(u)=L_(n-1)^(1)(u)=sum_(j=0)^(n-1) (-1)^j h_(n,j) u^j, h_(n,j)=binom(n,j+1)/j!",
            "P_n'(u)-P_n(u)=sum_(j=0)^(n-1) (-1)^(j+1) q_(n,j)u^j, q_(n,j)=binom(n+1,j+2)/j!",
            "H_n(u)=sum_(j=0)^(n-1) h_(n,j)u^j and Q_n(u)=sum_(j=0)^(n-1)q_(n,j)u^j for u>=0",
            "Gamma(r,z)=integral_z^infinity t^(r-1)exp(-t)dt",
            "d=(5^6 A_0^3/(2^2 3^4))^(1/5)",
            "K_B>0 and x_B are placeholders for the unexposed Theorem-1.5 implied constant and validity threshold",
        ],
        "coefficient_identity_proof": [
            "For 0<=j<=n-2, the u^j coefficient of P_n'-P_n is (-1)^(j+1)[binom(n,j+2)+binom(n,j+1)]/j!.",
            "Pascal's identity makes this (-1)^(j+1)binom(n+1,j+2)/j!; the same formula at j=n-1 equals -(-1)^(n-1)/(n-1)!.",
            "Therefore |P_n(u)|<=H_n(u) and |P_n'(u)-P_n(u)|<=Q_n(u) for u>=0 with every n-dependence explicit.",
        ],
        "conditional_source_bound": (
            "If |psi(x)-x|/x <= K_B exp(55A_0)exp(-omega(x)) for all x>=x_B, then |A(x)|<=1+K_B exp(55A_0)x exp(-omega(x))."
        ),
        "elementary_omega_reduction": (
            "For s>=e, log s<=sqrt(s), hence omega(exp(s))=d s^(3/5)/(log s)^(1/5)>=d sqrt(s)."
        ),
        "conditional_envelope": {
            "variable": "u=log Y",
            "validity_floor": "U_0(n;d,x_B)=max(e, log x_B, n-1, [2(n-1)/d]^2)",
            "formula": (
                "B_(K_B,x_B)(n,u)=H_n(u)[exp(-u)+K_B exp(55A_0)exp(-d sqrt(u))] "
                "+ sum_(j=0)^(n-1) q_(n,j)[Gamma(j+1,u)+2K_B exp(55A_0)d^(-2j-2)Gamma(2j+2,d sqrt(u))]"
            ),
            "proved_implication": (
                "For every fixed n>=1 and nonintegral Y=exp(u) with u>=U_0, |S_n-R_n(Y)|<=B_(K_B,x_B)(n,u); for integer Y use Y*=Y+1/2, so R_n(Y*)=R_n(Y) and monotonicity gives B(n,log Y*)<=B(n,log Y). Hence the same threshold controls every real Y, including integer endpoints."
            ),
            "endpoint_extension": "R_n is constant on each interval [m,m+1), so the C002 nonintegral identity plus the monotone envelope extends the estimate to every real cutoff without regrouping or reordering.",
            "tail_derivation": [
                "The floor-error part gives integral_u^infinity Q_n(s)exp(-s)ds=sum_j q_(n,j)Gamma(j+1,u).",
                "The PNT-error part is bounded using s=r^2 by 2 sum_j q_(n,j)d^(-2j-2)Gamma(2j+2,d sqrt(u)).",
            ],
            "monotonicity_proof": (
                "On u>=U_0, every u^j exp(-u) and u^j exp(-d sqrt(u)) term is nonincreasing; every upper incomplete-gamma term decreases in its lower endpoint. Thus B is nonincreasing and tends to zero."
            ),
        },
        "conditional_modulus": {
            "log_threshold": (
                "m_(K_B,x_B)(n,epsilon)=the least integer m>=ceil(U_0) with B_(K_B,x_B)(n,m)<=epsilon/2"
            ),
            "threshold": "M_(K_B,x_B)(n,epsilon)=exp(m_(K_B,x_B)(n,epsilon))",
            "forall_Y_statement": (
                "For every real Y>=M_(K_B,x_B)(n,epsilon), the natural-order endpoint error is <epsilon."
            ),
            "existence": "B is nonincreasing and tends to zero, so the defining integer set is nonempty.",
            "source_complete_materialization_status": "NOT_MATERIALIZED_BECAUSE_K_B_AND_X_B_ARE_NOT_EXPOSED",
        },
        "scope_exclusions": [
            "no numerical or source-bound K_B",
            "no numerical or source-bound x_B",
            "no frozen epsilon_n",
            "no numerical cutoff constant C",
            "no comparison M(n,epsilon_n)<=Y_n",
            "no internal-prefix maximal bound",
            "no Li positivity or RH implication",
            "no formal proof or independent review",
        ],
    }


def result_document(source: dict) -> dict:
    return seal({
        "record_type": "RH_ANA003J_D001_MODULUS_SOURCE_RESULT",
        "atom_id": ATOM,
        "discriminator_id": DISCRIMINATOR_ID,
        "source_audit_hash": source["artifact_hash"],
        "selected_result_branch": source["selected_result_branch"],
        "exact_mathematical_result": {
            "laguerre_constant_ledger": (
                "The exact finite normalization yields h_(n,j)=binom(n,j+1)/j! and q_(n,j)=binom(n+1,j+2)/j!, so both polynomial coefficient envelopes are explicit finite expressions in n."
            ),
            "conditional_boundary_tail_modulus": conditional_envelope_certificate(),
            "source_completeness_failure": (
                "Bellotti v1 Theorem 1.5 supplies only Delta(x)<<exp(55A_0)exp(-omega(x)) for sufficiently large x. "
                "Its absolute implied constant K_B and sufficiently-large threshold x_B are not explicitly bound in the acquired v1, so D001 cannot materialize the required source-derived explicit M(n,epsilon)."
            ),
            "truth_boundary": (
                "The conditional envelope is a mathematical implication for any fixed admissible K_B,x_B satisfying the source inequality. "
                "It is not an unconditional explicit modulus artifact until exact source-valid K_B,x_B are supplied."
            ),
        },
        "target_identity_firewall": {
            "epsilon_sequence_identity": None,
            "cutoff_constant_identity": None,
            "diagonal_comparison_attempted": False,
            "M_n_epsilon_n_le_Y_n_status": "NOT_AUTHORIZED_NOT_EVALUATED",
        },
        "result_status": "SCOPED_SOURCE_SUFFICIENCY_FAILURE_WITH_CONDITIONAL_PARAMETERIZED_ENVELOPE",
        "formal_proof": False,
        "independent_review": False,
        "novelty_claim": False,
        "computation_as_proof": False,
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def lesson_document(source: dict, result: dict) -> dict:
    return seal({
        "record_type": "RH_ANA003J_D001_SEVEN_FIELD_MATHEMATICAL_LESSON",
        "atom_id": ATOM,
        "attempted_mathematical_implication": (
            "Turn the acquired fixed-n Abel identity and Bellotti prime-number-theorem decay into an explicit n-dependent modulus M(n,epsilon) by exposing every Laguerre, boundary, tail, and validity constant."
        ),
        "exact_mathematical_result_or_failure": (
            "The Laguerre coefficient ledgers and a monotone boundary-plus-tail envelope are derivable explicitly in n, conditional on constants K_B and x_B in Bellotti's estimate. "
            "But acquired Bellotti v1 states the estimate with << for sufficiently large x and does not expose K_B or x_B. Therefore the source-complete explicit modulus was not materialized; the selected branch is QUALITATIVE_OR_INEFFECTIVE_SOURCE_ONLY_NO_EXPLICIT_MODULUS, where only the qualitative/unexposed disjunct is asserted."
        ),
        "supported_and_competing_mathematical_causes": {
            "supported": (
                "The obstruction is not Laguerre degree bookkeeping: exact finite coefficients give h_(n,j) and q_(n,j). The obstruction is the source-level loss of two quantitative coordinates, the absolute implied constant and validity threshold, which prevents a fully instantiated modulus."
            ),
            "competing": [
                {"cause": "the exact Laguerre normalization is unavailable or mismatched", "status": "REFUTED_BY_DGS_EQUATION_1_1_SPECIALIZATION"},
                {"cause": "even with K_B,x_B the Abel tail cannot be bounded for all later Y", "status": "REFUTED_BY_THE_CONDITIONAL_MONOTONE_ENVELOPE_DERIVATION"},
                {"cause": "Bellotti's argument is genuinely ineffective", "status": "NOT_ESTABLISHED; THE PAPER SAYS RELATED RESULTS CAN BE MADE FULLY_EXPLICIT"},
                {"cause": "another explicit PNT theorem or a full constant extraction from the proof supplies valid K_B,x_B", "status": "OPEN"},
            ],
        },
        "scope": (
            "Exact acquired C002 natural-order fixed-n remainder, Bellotti arXiv:2508.02041v1, and DGS equation (1.1). "
            "The direct Abel formula uses a nonintegral cutoff, then step-function constancy and envelope monotonicity extend it to every real cutoff. The result is endpoint-only. It makes no claim that all literature lacks explicit PNT constants, and it does not address internal prefixes, epsilon_n, numerical C, diagonal compatibility, Li positivity, novelty, or RH."
        ),
        "mathematical_falsifier": (
            "An exact passage in the acquired Bellotti v1 that binds a valid numerical or explicit K_B and x_B for Theorem 1.5 falsifies the missing-source-coordinate classification. "
            "A counterexample to the coefficient identity, boundary-plus-tail inequality, omega lower bound, monotonicity domain, or integer-endpoint step-function extension falsifies the corresponding conditional envelope step."
        ),
        "repair_or_next_discriminator": (
            "Before revisiting epsilon_n or Y_n, freeze one authoritative explicit PNT bound with a numerical constant and validity range, or perform a separately frozen line-by-line constant extraction from Bellotti's proof including H, O, and every << dependency. Then substitute those exact values into the already derived conditional envelope and test source-complete modulus materialization."
        ),
        "proof_or_source_evidence": [
            PATHS["source"],
            PATHS["result"],
            "Bellotti arXiv:2508.02041v1, Theorem 1.5 and proof pages 14-15, PDF SHA-256 " + BELLOTTI_PDF_SHA256,
            "Dunster-Gil-Segura arXiv:1705.01190v1, equation (1.1), PDF SHA-256 " + DGS_PDF_SHA256,
            C002_RESULT,
        ],
        "zero_mathematical_credit": [
            "Git/branch/PR state",
            "CI/tests",
            "schemas/hashes/chronology",
            "telemetry/repository growth",
        ],
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def _experience_from_document(item: dict) -> FailureExperience:
    return FailureExperience(
        failure_id=item["failure_id"], atom_id=item["atom_id"], candidate_id=item["candidate_id"],
        context_packet_hash=item["context_packet_hash"], research_trace_event_id=item["research_trace_event_id"],
        method_family=item["method_family"], failure_mode=item["failure_mode"],
        residual_signature=tuple(item["residual_signature"]), broken_assumptions=tuple(item.get("broken_assumptions", ())),
        scope_conditions=tuple(item["scope_conditions"]), competing_diagnoses=tuple(item["competing_diagnoses"]),
        selected_diagnosis=item["selected_diagnosis"], diagnosis_status=FailureDiagnosisStatus(item["diagnosis_status"]),
        evidence_pointers=tuple(item["evidence_pointers"]), falsifier_or_attempt=item["falsifier_or_attempt"],
        observed_result=item["observed_result"], artifact_hash=item["artifact_hash"], timestamp=item["timestamp"],
        local_repair_attempts=tuple(item.get("local_repair_attempts", ())),
    )


def failure_document(root: Path, lesson: dict) -> dict:
    prior_doc = load(root, ANA2_FAILURE)
    prior = _experience_from_document(prior_doc["experiences"][0])
    core = FailureExperience(
        failure_id="F-RH-ANA003j-D001-BELLOTTI-CONSTANTS-UNEXPOSED",
        atom_id=ATOM,
        candidate_id=DISCRIMINATOR_ID,
        context_packet_hash=CONTEXT_HASH,
        research_trace_event_id="RH-ANA-003j-D001-E11",
        method_family="explicit source-derived modulus from a fixed-n natural-order Abel boundary-plus-tail representation",
        failure_mode=(
            "the acquired Bellotti v1 statement preserves decay but hides the absolute implied constant and sufficiently-large-x threshold needed to instantiate the otherwise derivable modulus"
        ),
        residual_signature=(
            "EXACT_LAGUERRE_COEFFICIENT_LEDGER_DERIVED",
            "CONDITIONAL_MONOTONE_BOUNDARY_TAIL_ENVELOPE_DERIVED",
            "BELLOTTI_IMPLIED_CONSTANT_UNEXPOSED",
            "BELLOTTI_VALIDITY_THRESHOLD_UNEXPOSED",
            "SOURCE_COMPLETE_EXPLICIT_MODULUS_NOT_MATERIALIZED",
        ),
        broken_assumptions=(
            "an asymptotic << theorem statement automatically exposes the constant needed by an explicit modulus",
            "the phrase sufficiently large x automatically exposes a usable validity threshold",
        ),
        scope_conditions=(
            "only Bellotti arXiv:2508.02041v1 as acquired and hash-bound",
            "only the C002 fixed-n natural-order endpoint remainder",
            "no claim of source-wide or literature-wide impossibility",
            "reuse is allowed if exact valid K_B,x_B are later bound",
        ),
        competing_diagnoses=(
            "Laguerre coefficient growth prevents an explicit n-ledger",
            "the transformed tail remains nonquantitative even after K_B,x_B are supplied",
            "Bellotti's proof is effective but the paper omits materialized constants",
            "another authoritative explicit PNT theorem can replace the missing source coordinates",
        ),
        selected_diagnosis=(
            "SUPPORTED_BOUNDED_SOURCE_SUFFICIENCY_FAILURE: exact finite Laguerre bookkeeping and a conditional envelope survive, but the acquired v1 does not expose K_B or x_B; this is not a theorem of ineffectivity or global impossibility."
        ),
        diagnosis_status=FailureDiagnosisStatus.SUPPORTED,
        evidence_pointers=(PATHS["source"], PATHS["result"], PATHS["lesson"], FREEZE, C002_RESULT),
        falsifier_or_attempt=lesson["mathematical_falsifier"],
        observed_result=lesson["exact_mathematical_result_or_failure"],
        artifact_hash="",
        timestamp="2026-08-12T12:33:00Z",
        local_repair_attempts=(
            "derived exact h_(n,j) and q_(n,j) rather than hiding n-dependence",
            "derived a monotone conditional envelope and conditional modulus",
            "separated unexposed constants from mathematical ineffectivity",
            "kept epsilon_n, numerical C, and diagonal comparison outside the result",
        ),
    )
    current = replace(core, artifact_hash=canonical_hash(asdict(core)))
    reasons = validate_failure_experience(current)
    if reasons:
        raise RuntimeError(reasons)
    link = FailureLink(
        source_id=current.failure_id,
        target_id=prior.failure_id,
        relation=FailureRelation.SHARES_BROKEN_ASSUMPTION_WITH,
        rationale=(
            "Both bounded audits show that a mathematically valid source object does not transport to the target when an additional source-level interface is unbound. The domains and causes are not asserted identical: ANA-002 lacks norm faithfulness, while D001 lacks quantitative constants and threshold."
        ),
        evidence_pointers=(PATHS["lesson"], ANA2_FAILURE),
    )
    return jsonable(asdict(FailureExperienceLattice(experiences=(prior, current), links=(link,))))


def dag_document(result: dict, lesson: dict) -> dict:
    return seal({
        "record_type": "RH_ANA003J_D001_RESULT_DAG_DELTA",
        "atom_id": ATOM,
        "nodes": [
            {
                "node_id": "LEM-RH-ANA003j-D001-EXACT-LAGUERRE-COEFFICIENT-LEDGER",
                "status": "PROVED_SAME_CONTEXT_HAND_DERIVATION",
                "scope": "finite generalized-Laguerre normalization for every integer n>=1",
                "pointer": PATHS["result"],
            },
            {
                "node_id": "LEM-RH-ANA003j-D001-CONDITIONAL-BOUNDARY-TAIL-MODULUS",
                "status": "PROVED_CONDITIONAL_ON_VALID_K_B_AND_X_B",
                "scope": "fixed n, natural order, direct nonintegral identity extended to every real endpoint by step constancy, explicit Bellotti placeholders K_B,x_B",
                "pointer": PATHS["result"],
            },
            {
                "node_id": "OBL-RH-ANA003j-D001-SOURCE-COMPLETE-K_B-X_B",
                "status": "OPEN_NOT_EXPOSED_BY_ACQUIRED_BELLOTTI_V1",
                "pointer": PATHS["source"],
            },
            {
                "node_id": "CLAIM-RH-ANA003j-D001-EXPLICIT-SOURCE-DERIVED-MODULUS",
                "status": "NOT_ESTABLISHED_NOT_REFUTED_GLOBALLY",
                "depends_on": [
                    "LEM-RH-ANA003j-D001-EXACT-LAGUERRE-COEFFICIENT-LEDGER",
                    "LEM-RH-ANA003j-D001-CONDITIONAL-BOUNDARY-TAIL-MODULUS",
                    "OBL-RH-ANA003j-D001-SOURCE-COMPLETE-K_B-X_B",
                ],
            },
            {
                "node_id": "CLAIM-RH-ANA003j-DIAGONAL-COMPATIBILITY",
                "status": "NOT_AUTHORIZED_EPSILON_N_AND_NUMERICAL_C_UNFROZEN",
            },
        ],
        "selected_result_branch": result["selected_result_branch"],
        "next_discriminator": lesson["repair_or_next_discriminator"],
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def review_document(source: dict, result: dict) -> dict:
    return seal({
        "record_type": "RH_ANA003J_D001_SAME_CONTEXT_RESULT_REVIEW",
        "atom_id": ATOM,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT",
        "roles": {
            "analytic_number_theory": "Theorem 1.5 has the required decay shape but retains <<, sufficiently-large-x, H and O constants; no source-complete K_B,x_B pair is stated.",
            "special_functions": "DGS equation (1.1) exactly yields the finite h and q coefficient ledgers; no large-degree asymptotic is needed or imported.",
            "adversarial_falsification": "The conditional envelope would be invalid if endpoint convention, integer step-function extension, omega lower bound, or monotonicity floor were suppressed; all remain explicit.",
            "formal_methods": "The displayed derivation is a same-context hand proof, not formal or computation-certified theorem authority.",
            "novelty_research_value": "The conditional estimates are elementary consequences of acquired inputs; no novelty is claimed. The useful result is the exact localization of the missing source coordinates.",
        },
        "strongest_objection": (
            "The full Bellotti proof may be made explicit by tracking every hidden constant, so the result cannot call the theorem ineffective or the modulus impossible."
        ),
        "resolution": (
            "Accepted. The selected branch asserts only that acquired v1 leaves K_B,x_B unexposed; ineffectivity and global absence are expressly not claimed."
        ),
        "scope_checks": {
            "source_branch_matches_freeze": source["selected_result_branch"] == "QUALITATIVE_OR_INEFFECTIVE_SOURCE_ONLY_NO_EXPLICIT_MODULUS",
            "epsilon_sequence_frozen": False,
            "numeric_cutoff_C_frozen": False,
            "diagonal_comparison_run": False,
            "rh_claim": False,
        },
        "result_hash": result["artifact_hash"],
        "blocking_concerns": [],
        "independent_review": False,
        "mathematical_result_credit": "SAME_CONTEXT_SCOPED_SOURCE_DIAGNOSIS_AND_CONDITIONAL_HAND_DERIVATION_ONLY",
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def _entry_from_dict(item: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
        event_id=item["event_id"], atom_id=item["atom_id"], event_type=ResearchTraceEventType(item["event_type"]),
        timestamp=item["timestamp"], state_summary=item["state_summary"], action_summary=item["action_summary"],
        evidence_pointers=tuple(item["evidence_pointers"]), alternatives_considered=tuple(item.get("alternatives_considered", ())),
        decision_rationale=item.get("decision_rationale", ""), outputs=tuple(item.get("outputs", ())),
        uncertainties=tuple(item.get("uncertainties", ())), residuals=tuple(item.get("residuals", ())),
        next_steps=tuple(item.get("next_steps", ())), artifact_hash=item["artifact_hash"],
        previous_event_hash=item["previous_event_hash"],
    )


def _append_entry(entries: list[ResearchTraceEntry], *, idx: int, kind: ResearchTraceEventType,
                  timestamp: str, state: str, action: str, evidence: tuple[str, ...],
                  outputs: tuple[str, ...] = (), residuals: tuple[str, ...] = (),
                  next_steps: tuple[str, ...] = ()) -> None:
    payload = {
        "event_id": f"RH-ANA-003j-D001-E{idx:02d}",
        "atom_id": ATOM,
        "event_type": kind.value,
        "timestamp": timestamp,
        "state_summary": state,
        "action_summary": action,
        "evidence_pointers": list(evidence),
        "alternatives_considered": [],
        "decision_rationale": "",
        "outputs": list(outputs),
        "uncertainties": ["same-context derivation is not independent review"],
        "residuals": list(residuals),
        "next_steps": list(next_steps),
        "artifact_hash": "",
        "previous_event_hash": entries[-1].artifact_hash,
    }
    payload["artifact_hash"] = canonical_hash(payload)
    entries.append(_entry_from_dict(payload))


def trace_document(root: Path, source: dict, result: dict, review: dict) -> dict:
    parent = load(root, PARENT_TRACE)
    entries = [_entry_from_dict(item) for item in parent["entries"]]
    _append_entry(
        entries, idx=9, kind=ResearchTraceEventType.FALSIFIER_RUN, timestamp="2026-08-12T12:31:00Z",
        state="D001 is publicly frozen; exact source access is authorized while epsilon_n and numerical C remain null.",
        action="Audit C002, Bellotti v1 and DGS equation (1.1) against the six frozen source obligations.",
        evidence=(FREEZE, PATHS["source"]), outputs=(source["selected_result_branch"],),
    )
    _append_entry(
        entries, idx=10, kind=ResearchTraceEventType.PROOF_CHECKED, timestamp="2026-08-12T12:32:00Z",
        state="Exact h and q coefficient ledgers and a conditional K_B,x_B envelope have been derived by hand.",
        action="Check coefficient algebra, boundary-tail substitution, omega lower bound, monotonicity floor and conditional modulus.",
        evidence=(PATHS["result"],), outputs=("CONDITIONAL_PARAMETERIZED_ENVELOPE_SUPPORTED", "NO_FORMAL_OR_INDEPENDENT_PROOF_CREDIT"),
    )
    _append_entry(
        entries, idx=11, kind=ResearchTraceEventType.RESULT_RECORDED, timestamp="2026-08-12T12:33:00Z",
        state="The acquired v1 leaves K_B and x_B unexposed; no source-complete explicit modulus is materialized.",
        action="Select the qualitative/unexposed source branch and preserve the conditional mathematical subresult.",
        evidence=(PATHS["source"], PATHS["result"], PATHS["lesson"]), outputs=(result["selected_result_branch"],),
        residuals=("explicit valid K_B missing", "explicit valid x_B missing", "diagonal comparison not authorized"),
    )
    _append_entry(
        entries, idx=12, kind=ResearchTraceEventType.RESIDUAL_OPENED, timestamp="2026-08-12T12:34:00Z",
        state="Only source-level quantitative coordinates block materialization; Laguerre bookkeeping and conditional tail control survive.",
        action="Open an explicit-PNT-source or separately frozen Bellotti constant-extraction discriminator.",
        evidence=(PATHS["failure"], PATHS["dag"]), residuals=("K_B/x_B source bridge",),
        next_steps=("freeze exact explicit PNT theorem identity before access", "do not select epsilon_n or numerical C yet"),
    )
    _append_entry(
        entries, idx=13, kind=ResearchTraceEventType.REVIEWED, timestamp="2026-08-12T12:35:00Z",
        state="Role-separated same-context review found no blocker after narrowing ineffectivity/global-absence language.",
        action="Retain only the scoped source diagnosis and conditional hand derivation.",
        evidence=(PATHS["review"],), outputs=(review["review_authority"], "NO_BLOCKING_CONCERNS"),
    )
    trace = MathResearchTrace("RH-ANA-003j-D001-RESULT-TRACE-20260812", tuple(entries))
    audit = audit_research_trace(trace)
    if audit.verdict.value != "PASS":
        raise RuntimeError(audit.reasons)
    return jsonable(asdict(trace))


def build_documents(root: Path = ROOT) -> dict[str, dict]:
    source = source_document(root)
    result = result_document(source)
    lesson = lesson_document(source, result)
    failure = failure_document(root, lesson)
    dag = dag_document(result, lesson)
    review = review_document(source, result)
    trace = trace_document(root, source, result, review)
    return {"source": source, "result": result, "lesson": lesson, "failure": failure, "dag": dag, "review": review, "trace": trace}


def write(root: Path = ROOT) -> None:
    for name, document in build_documents(root).items():
        path = root / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write()
