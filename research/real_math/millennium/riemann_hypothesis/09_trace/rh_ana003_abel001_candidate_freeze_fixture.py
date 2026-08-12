"""Prospective candidate/proof-input freeze for RH-ANA-003-ABEL-001.

The pre-candidate gate is already public in the parent commit.  This fixture
freezes the exact proposition and a deliberately inert evaluator.  It does not
derive, check, prove, or classify the proposition in this round.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from rakl.framework_candidate_freeze import (
    CandidateFreezeRevalidationVerdict,
    FrameworkSubjectFreezeBinding,
    FrameworkSubjectRevalidationObservation,
    audit_candidate_freeze_framework_subject,
)


ATOM = "RH-ANA-003-ABEL-001"
CANDIDATE_ID = "RH-ANA-003-ABEL-001-C001-FIXED-N-NATURAL-ORDER-ABEL"
APPLICATION_PARENT_SHA = "f0732a8641489b9803d0c5b5f38020fe073d67ea"
FRAMEWORK_SHA = "d594e6864f49ecf6dac394173082fbf0174b422e"
CONTEXT_PACKET_HASH = "8fa0778327c198c7e5e1b3a7e6f9ebdb59735ef067e8545c7f0eb62cb38ff777"
PRE_GATE_BLOB = "e2ec60062a6b8ad036b7521960eb0c221ad5ea84"
PRE_GATE_RAW_SHA256 = "8fa0778327c198c7e5e1b3a7e6f9ebdb59735ef067e8545c7f0eb62cb38ff777"
PRE_TRACE_BLOB = "ae45ccdfb783e89e27ec31e74d7d711b51ef51cf"
PRE_TRACE_RAW_SHA256 = "51038cfe7bfd7b05667150f30e031adda54d498472bd8a984e4ed2fcbb6766a8"
EVALUATOR_RAW_SHA256 = "b507a4d4555770dadfde5ea943086adc853c138c7caae2e1327b5b54fc471350"
FROZEN_AT = "2026-08-12T07:30:00Z"

BASE = "research/real_math/millennium/riemann_hypothesis"
PRE_GATE = f"{BASE}/09_trace/RH_ANA_003_ABEL_001_PRE_CANDIDATE_GATE_RECEIPT_20260812.json"
PRE_TRACE = f"{BASE}/09_trace/RH_ANA_003_ABEL_001_PRE_CANDIDATE_TRACE_20260812.json"
EVALUATOR = f"{BASE}/05_oracles/rh_ana003_abel001_inert_evaluator.py"
PATHS = {
    "candidate": f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_FIXED_N_ABEL_CANDIDATE_FREEZE_20260812.json",
    "proof_inputs": f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_PROOF_INPUT_FREEZE_20260812.json",
    "manifest": f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_INERT_EVALUATOR_FREEZE_20260812.json",
    "authorization": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_EVALUATION_AUTHORIZATION_20260812.json",
    "framework_binding": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_CANDIDATE_FRAMEWORK_SUBJECT_FREEZE_20260812.json",
    "framework_observation": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_CANDIDATE_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_CANDIDATE_FREEZE_TRACE_20260812.json",
    "receipt": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_CANDIDATE_FREEZE_RECEIPT_20260812.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def seal(value: dict) -> dict:
    document = dict(value)
    document["artifact_hash"] = ""
    document["artifact_hash"] = canonical_hash(document)
    return document


def candidate_document() -> dict:
    core = {
        "schema_version": "1.0.0",
        "candidate_id": CANDIDATE_ID,
        "atom_id": ATOM,
        "candidate_kind": "FIXED_N_NATURAL_ORDER_CONVERGENCE_LEMMA_PROPOSAL",
        "frozen_at": FROZEN_AT,
        "quantifier_order": "FOR_EACH_FIXED_INTEGER_N_GE_1__THEN_TAKE_Y_TO_INFINITY",
        "definitions": {
            "von_mangoldt": "Lambda(m)=log p if m=p^j for a prime p and integer j>=1; Lambda(m)=0 otherwise",
            "source_sequence": "a_m=1-Lambda(m)",
            "chebyshev_psi": "psi(x)=sum_{m<=x}Lambda(m)",
            "cumulative_source": "A(x)=sum_{m<=x}a_m=floor(x)-psi(x)",
            "kernel": "b_n(x)=L_{n-1}^{(1)}(log x)/x",
            "laguerre_normalization": (
                "L_{n-1}^{(1)}(u)=sum_{j=0}^{n-1}(-1)^j binom(n,j+1)u^j/j!"
            ),
        },
        "candidate_statement": {
            "finite_endpoint_identity": (
                "For real 1<=X<Y that are not positive integers, "
                "sum_{X<m<=Y} a_m b_n(m) = A(Y)b_n(Y)-A(X)b_n(X) "
                "- integral_X^Y A(t)b_n'(t)dt."
            ),
            "boundary_claim": "lim_{Y->infinity} A(Y)b_n(Y)=0",
            "integral_claim": "integral_X^infinity |A(t)b_n'(t)|dt<infinity",
            "natural_order_tail_identity": (
                "lim_{Y->infinity}sum_{X<m<=Y}a_m b_n(m)="
                "-A(X)b_n(X)-integral_X^infinity A(t)b_n'(t)dt"
            ),
            "convergence_class": (
                "the natural-order series converges for each fixed n, but the original term series "
                "sum_m |a_m b_n(m)| does not converge absolutely"
            ),
        },
        "proof_obligations": [
            {
                "id": "O1-FINITE-ABEL-ENDPOINTS",
                "obligation": "derive the displayed finite half-open identity with X,Y nonintegral and exact A(X),A(Y) terms",
                "status": "FROZEN_UNEVALUATED",
            },
            {
                "id": "O2-KERNEL-DERIVATIVE",
                "obligation": (
                    "derive b_n'(t)=t^(-2)[(L_{n-1}^{(1)})'(log t)-L_{n-1}^{(1)}(log t)] "
                    "and bound it by C_n(1+log t^(n-1))/t^2 for fixed n"
                ),
                "status": "FROZEN_UNEVALUATED",
            },
            {
                "id": "O3-BELLOTTI-TO-A",
                "obligation": (
                    "from Bellotti v1 Theorem 1.5 and equations (1.3)-(1.4), derive for sufficiently large x "
                    "|A(x)|<=1+C x exp(-d(log x)^(3/5)/(log log x)^(1/5))"
                ),
                "status": "FROZEN_UNEVALUATED",
            },
            {
                "id": "O4-FIXED-N-BOUNDARY",
                "obligation": "combine O2-O3 with fixed n to prove A(Y)b_n(Y)->0",
                "status": "FROZEN_UNEVALUATED",
            },
            {
                "id": "O5-FIXED-N-INTEGRAL",
                "obligation": "combine O2-O3 with fixed n to prove integral_X^infinity |A(t)b_n'(t)|dt<infinity",
                "status": "FROZEN_UNEVALUATED",
            },
            {
                "id": "O6-NATURAL-ORDER-LIMIT",
                "obligation": "take Y to infinity only after O1,O4,O5 and preserve original integer order",
                "status": "FROZEN_UNEVALUATED",
            },
            {
                "id": "O7-NONABSOLUTE-WITNESS",
                "obligation": (
                    "for m=6k, prove Lambda(m)=0 because 6k has at least prime factors 2 and 3, so |a_m|=1; "
                    "use the leading coefficient (-1)^(n-1)/(n-1)! of L_{n-1}^{(1)} to obtain "
                    "|b_n(6k)|>=c_n(log k)^(n-1)/k for all sufficiently large k; conclude divergence "
                    "of the absolute subseries, including n=1"
                ),
                "status": "FROZEN_UNEVALUATED",
            },
        ],
        "bellotti_source_binding": {
            "source": "Bellotti, arXiv:2508.02041v1",
            "theorem": "Theorem 1.5",
            "equation_1_3": "Delta(x)=|psi(x)-x|/x",
            "equation_1_4": (
                "omega(x)=d(log x)^(3/5)/(log log x)^(1/5), "
                "d=(5^6 A_0^3/(2^2*3^4))^(1/5)"
            ),
            "theorem_bound": "Delta(x)<<exp(55 A_0)exp(-omega(x))",
            "retrieved_v1_html_sha256": "2b57101a941e31c033ae2510efe8f4b3e81f22f025cd857fcb53d8ce77f3e634",
            "use_scope": "sufficient boundary source for fixed n only",
        },
        "allowed_result_branches": [
            "PROVED_FIXED_N_NATURAL_ORDER_IDENTITY",
            "FINITE_ENDPOINT_IDENTITY_FALSE",
            "BELLOTTI_BOUNDARY_OR_INTEGRAL_INSUFFICIENT",
            "ABSOLUTE_DIVERGENCE_WITNESS_FALSE",
            "CANNOT_CHECK",
        ],
        "falsifiers": {
            "finite_identity": [
                "one endpoint convention for which the displayed signs or boundary terms are false",
                "a direct finite example contradicting the formula",
            ],
            "boundary_integral": [
                "Bellotti v1 does not imply the stated A bound",
                "the fixed Laguerre derivative grows faster than the frozen polynomial-log bound",
                "the transformed improper integral diverges for one fixed n",
            ],
            "nonabsolute": [
                "one m=6k that is a prime power",
                "failure of the leading Laguerre term to dominate eventually",
                "convergence of the stated positive comparison subseries",
            ],
            "scope": [
                "any proof step requires a constant uniform in n",
                "any regrouping or permutation of the original term series",
                "any use of unmerged PR316 or historical R4/R5 as theorem authority",
            ],
        },
        "seven_field_mathematical_rubric": {
            "attempted_implication": (
                "Bellotti cumulative PNT decay plus exact finite Abel summation implies a fixed-n natural-order "
                "tail identity while the original term series remains nonabsolute"
            ),
            "exact_result_or_failure": "UNEVALUATED_CANDIDATE_FREEZE_ONLY",
            "supported_and_competing_causes": [
                "supported proposal: cumulative cancellation survives through A=floor-psi",
                "competing failure: an endpoint sign/convention error invalidates the identity",
                "competing failure: Bellotti decay is insufficient after the exact derivative",
                "competing failure: the m=6k absolute-divergence witness is malformed",
            ],
            "scope": "each fixed integer n>=1; natural order; exact nonintegral endpoints",
            "mathematical_falsifier": "any item in the frozen falsifier map",
            "mathematical_repair": (
                "if an endpoint convention fails, restate the exact finite Stieltjes identity; if Bellotti is insufficient, "
                "narrow to the proven boundary; if m=6k fails, replace it only prospectively with a proved arithmetic subsequence"
            ),
            "proof_source_evidence": [
                "classical finite Abel summation",
                "Bellotti arXiv:2508.02041v1 Theorem 1.5 and equations (1.3)-(1.4)",
                "exact generalized Laguerre finite polynomial normalization",
                "elementary arithmetic fact that 6k is not a prime power",
            ],
        },
        "explicit_exclusions": [
            "NO_N_UNIFORMITY",
            "NO_SERIES_REORDERING_OR_REGROUPING",
            "NO_PR316_RATE_OR_CUTOFF_CLAIM",
            "NO_LI_COEFFICIENT_SIGN_CLAIM",
            "NO_RIEMANN_HYPOTHESIS_CLAIM",
            "NO_NOVELTY_CLAIM",
            "NO_INDEPENDENT_REVIEW_CLAIM",
        ],
        "target_access": {
            "proof_evaluator_imported_or_executed": False,
            "finite_identity_checked": False,
            "boundary_checked": False,
            "absolute_divergence_checked": False,
            "result_accessed": False,
        },
        "source_identity": {
            "application_parent_commit": APPLICATION_PARENT_SHA,
            "pre_candidate_gate": {
                "path": PRE_GATE,
                "git_blob": PRE_GATE_BLOB,
                "raw_sha256": PRE_GATE_RAW_SHA256,
            },
            "pre_candidate_trace": {
                "path": PRE_TRACE,
                "git_blob": PRE_TRACE_BLOB,
                "raw_sha256": PRE_TRACE_RAW_SHA256,
            },
        },
        "credit_boundary": {
            "candidate_freeze_mathematical_result_credit": False,
            "operational_metadata_zero_math_credit": [
                "Git/branch/PR chronology",
                "CI/tests",
                "schemas/hashes/serialization",
                "framework subject and evaluator wiring",
            ],
            "math_ledger_entry_created": False,
        },
    }
    identity = {
        "candidate_id": CANDIDATE_ID,
        "canonical_core_sha256": canonical_hash(core),
        "identity_scope": "FULL_CANDIDATE_CORE_BEFORE_IDENTITY_AND_ARTIFACT_HASH",
    }
    return seal({**core, "candidate_identity": identity})


def framework_documents():
    binding = FrameworkSubjectFreezeBinding(
        binding_id="RH-ANA-003-ABEL-001-CANDIDATE-FRAMEWORK-FREEZE-20260812",
        authoritative_framework_sha=FRAMEWORK_SHA,
        pre_candidate_packet_hash=CONTEXT_PACKET_HASH,
        frozen_at_utc=FROZEN_AT,
        evidence_pointers=(
            f"git:{FRAMEWORK_SHA}:RAKL_VERSION.json",
            f"git:{FRAMEWORK_SHA}:skills/rakl-core/workflows/mathematical-research.md",
            f"git:{FRAMEWORK_SHA}:src/rakl/math_research_runtime.py",
            f"git:{APPLICATION_PARENT_SHA}:{PRE_GATE}",
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=FRAMEWORK_SHA,
        intervening_diff=(),
        observation_evidence_pointers=(
            f"git:{FRAMEWORK_SHA}:RAKL_VERSION.json",
            "protected math-gate surface unchanged since pre-candidate observation",
        ),
    )
    report = audit_candidate_freeze_framework_subject(binding, observation, required=True)
    if report.verdict is not CandidateFreezeRevalidationVerdict.CURRENT_UNCHANGED:
        raise RuntimeError(report.reasons)
    return (
        seal(dict(binding.document())),
        seal(
            {
                "schema_version": "framework-subject-revalidation-observation-v1",
                "observation_id": "RH-ANA-003-ABEL-001-CANDIDATE-FRAMEWORK-REVALIDATION-20260812",
                "observed_current_main_sha": observation.observed_current_main_sha,
                "intervening_diff": [],
                "observation_evidence_pointers": list(observation.observation_evidence_pointers),
                "verdict": report.verdict.value,
                "reasons": list(report.reasons),
                "licenses_candidate_materialization": report.licenses_candidate_materialization,
                "grants_scientific_authority": False,
            }
        ),
    )


def build_documents() -> dict[str, dict]:
    candidate = candidate_document()
    binding, observation = framework_documents()
    proof_inputs = seal(
        {
            "schema_version": "1.0.0",
            "proof_input_id": "RH-ANA-003-ABEL-001-PROOF-INPUT-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "frozen_at": FROZEN_AT,
            "inputs": {
                "finite_identity": candidate["candidate_statement"]["finite_endpoint_identity"],
                "exact_definitions": candidate["definitions"],
                "bellotti": candidate["bellotti_source_binding"],
                "absolute_divergence_subsequence": (
                    "m=6k, so Lambda(6k)=0; compare eventual Laguerre leading term against "
                    "sum_k (log k)^(n-1)/k"
                ),
            },
            "proof_obligations": candidate["proof_obligations"],
            "allowed_result_branches": candidate["allowed_result_branches"],
            "status": "FROZEN_UNEVALUATED",
            "evaluation_authorized": False,
            "mathematical_result_credit": False,
        }
    )
    manifest = seal(
        {
            "schema_version": "1.0.0",
            "manifest_id": "RH-ANA-003-ABEL-001-INERT-EVALUATOR-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "frozen_at": FROZEN_AT,
            "status": "FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED",
            "evaluator": {"path": EVALUATOR, "raw_sha256": EVALUATOR_RAW_SHA256},
            "required_future_obligations": [row["id"] for row in candidate["proof_obligations"]],
            "allowed_future_result_branches": candidate["allowed_result_branches"],
            "inert_behavior": "Every invocation raises TargetEvaluationNotAuthorized.",
            "current_round_execution_authorized": False,
            "authority": {
                "proof_authority": False,
                "mathematical_result_credit": False,
                "li_or_rh_authority": False,
            },
        }
    )
    authorization = seal(
        {
            "schema_version": "1.0.0",
            "authorization_id": "RH-ANA-003-ABEL-001-EVALUATION-AUTHORIZATION-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "evaluator_raw_sha256": EVALUATOR_RAW_SHA256,
            "current_round_evaluator_execution_authorized": False,
            "proof_derivation_authorized": False,
            "result_classification_authorized": False,
            "allowed_next_action": "COMMIT_PUBLIC_FREEZE_ONLY",
            "future_work_requires_separate_successor_authorization": True,
            "result_state": "UNEVALUATED",
            "mathematical_result_credit": False,
        }
    )
    pre_trace = json.loads(Path(PRE_TRACE).read_text(encoding="utf-8"))
    entries = list(pre_trace["entries"])
    event = {
        "event_id": "RH-ANA-003-ABEL-001-E09",
        "atom_id": ATOM,
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": FROZEN_AT,
        "state_summary": (
            "The exact fixed-n natural-order Abel lemma, Bellotti boundary inputs, m=6k nonabsolute witness, "
            "scope exclusions, allowed result branches, and inert evaluator identity are frozen without evaluation."
        ),
        "action_summary": "Freeze candidate and proof inputs only; preserve evaluation firewall.",
        "evidence_pointers": [
            PATHS["candidate"],
            PATHS["proof_inputs"],
            PATHS["manifest"],
            PATHS["authorization"],
            PATHS["framework_binding"],
            PATHS["framework_observation"],
            PRE_GATE,
        ],
        "alternatives_considered": [
            "evaluate immediately",
            "freeze an n-uniform rate",
            "import PR316",
            "freeze only the exact fixed-n dependency lemma",
        ],
        "decision_rationale": (
            "The fixed-n dependency is the smallest self-contained atom; prospective freezing prevents endpoint, "
            "result-branch, and scope rescue after evaluation."
        ),
        "outputs": [
            CANDIDATE_ID,
            candidate["candidate_identity"]["canonical_core_sha256"],
            "FROZEN_UNEVALUATED",
            "ZERO_MATHEMATICAL_RESULT_CREDIT",
        ],
        "uncertainties": [
            "every proof obligation remains unchecked",
            "same-context candidate design is not independent review",
        ],
        "residuals": [
            "fixed-n lemma truth open",
            "n-uniformity excluded",
            "Li and RH bridges open",
            "root OPEN_NO_SOLUTION_CERTIFICATE",
        ],
        "next_steps": [
            "commit and publish exact freeze before any evaluation",
            "obtain a separate successor authorization",
            "evaluate every obligation and retain any failure without widening scope",
        ],
        "previous_event_hash": entries[-1]["artifact_hash"],
    }
    event["artifact_hash"] = canonical_hash(event)
    entries.append(event)
    trace = {
        "trace_id": "RH-ANA-003-ABEL-001-CANDIDATE-FREEZE-TRACE-20260812",
        "entries": entries,
    }
    documents = {
        "candidate": candidate,
        "proof_inputs": proof_inputs,
        "manifest": manifest,
        "authorization": authorization,
        "framework_binding": binding,
        "framework_observation": observation,
        "trace": trace,
    }
    integrity = {
        "algorithm": "SHA-256",
        "canonicalization": "JSON_SORT_KEYS_COMPACT_UTF8",
        "json_inputs": {
            name: {"path": PATHS[name], "canonical_sha256": canonical_hash(document)}
            for name, document in sorted(documents.items())
        },
        "byte_inputs": {
            "evaluator": {"path": EVALUATOR, "raw_sha256": EVALUATOR_RAW_SHA256},
            "pre_gate": {
                "path": PRE_GATE,
                "git_blob": PRE_GATE_BLOB,
                "raw_sha256": PRE_GATE_RAW_SHA256,
            },
            "pre_trace": {
                "path": PRE_TRACE,
                "git_blob": PRE_TRACE_BLOB,
                "raw_sha256": PRE_TRACE_RAW_SHA256,
            },
        },
    }
    documents["receipt"] = seal(
        {
            "schema_version": "1.0.0",
            "receipt_id": "RH-ANA-003-ABEL-001-CANDIDATE-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "candidate_artifact_hash": candidate["artifact_hash"],
            "frozen_at": FROZEN_AT,
            "chronology": {
                "application_parent_commit": APPLICATION_PARENT_SHA,
                "pre_candidate_gate_committed_before_candidate": True,
                "candidate_publication_status": "TO_BE_COMMITTED_BEFORE_ANY_EVALUATION",
                "proof_evaluator_imported_or_executed": False,
                "result_accessed": False,
            },
            "framework_subject": {
                "framework_sha": FRAMEWORK_SHA,
                "verdict": observation["verdict"],
                "licenses_candidate_materialization": observation["licenses_candidate_materialization"],
            },
            "full_document_integrity": integrity,
            "full_document_integrity_hash": canonical_hash(integrity),
            "authority": {
                "candidate_is_mathematical_proposal": True,
                "target_theorem_truth": False,
                "independent_review": False,
                "mathematical_result_credit": False,
                "mathematical_saturation_credit": False,
                "li_or_rh_authority": False,
                "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
            },
            "math_ledger_entry_created": False,
            "allowed_next_action": "COMMIT_PUBLIC_FREEZE_ONLY; EVALUATION REQUIRES SEPARATE SUCCESSOR AUTHORIZATION",
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
