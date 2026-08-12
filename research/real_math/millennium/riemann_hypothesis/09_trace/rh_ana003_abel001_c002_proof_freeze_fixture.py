#!/usr/bin/env python3
"""Generate the prospective C002 hand-proof and evaluator freeze artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = "research/real_math/millennium/riemann_hypothesis"
CANDIDATE_ID = "RH-ANA-003-ABEL-001-C002-FIXED-N-NATURAL-ORDER-ABEL"
CANDIDATE_CORE = "sha256:b9bd54e72850dbc31b2fba344d978ee3660f0004bf81fb237347f0eb8b5ab3ab"
BASE_COMMIT = "301f6f9db54784d250a49c4a5766384df31989dd"
FROZEN_AT = "2026-08-12T08:04:00Z"
FRAMEWORK_PIN = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
FRAMEWORK_LIVE = "55132eddafd95065fd7afa217b53ead88f5763c2"
PROOF_INPUT_RAW = "c6dff171471e30276136564207c127f21ea1b69daf3f131c8d78c449a9c21923"
CANDIDATE_RAW = "7eb1e7e369dde0b6532ceae005f62fabf37e83abe2dd7cd663d1cd60137189a8"

PATHS = {
    "certificate": f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_HAND_PROOF_CERTIFICATE_FREEZE_20260812.json",
    "manifest": f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_EVALUATOR_FREEZE_20260812.json",
    "authorization": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json",
    "chronology": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_PROOF_INPUT_CHRONOLOGY_20260812.json",
    "receipt": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_HAND_PROOF_FREEZE_RECEIPT_20260812.json",
    "framework_revalidation": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_PROOF_ROUND_FRAMEWORK_REVALIDATION_20260812.json",
}
PROOF_INPUT = ROOT / f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_PROOF_INPUT_FREEZE_20260812.json"
CANDIDATE = ROOT / f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_FIXED_N_ABEL_CANDIDATE_FREEZE_20260812.json"
CHECKER = ROOT / f"{BASE}/05_oracles/rh_ana003_abel001_c002_proof_checker.py"


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def raw_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seal(value: dict) -> dict:
    value = dict(value)
    value.pop("artifact_hash", None)
    value["artifact_hash"] = canonical_hash(value)
    return value


def certificate_document() -> dict:
    obligations = [
        {
            "obligation_id": "O1-FINITE-ABEL-ENDPOINTS",
            "status": "PROVED_IN_FROZEN_HAND_CERTIFICATE",
            "proof": (
                "Let A(t)=sum_{m<=t}a_m, a right-continuous step function. For nonintegral 1<=X<Y, "
                "sum_{X<m<=Y}a_m b_n(m)=integral_(X,Y] b_n dA. Stieltjes integration by parts gives "
                "A(Y)b_n(Y)-A(X)b_n(X)-integral_X^Y A(t)b_n'(t)dt. Nonintegrality removes endpoint jumps, "
                "and the half-open convention is exactly X<m<=Y."
            ),
        },
        {
            "obligation_id": "O2-KERNEL-DERIVATIVE",
            "status": "PROVED_IN_FROZEN_HAND_CERTIFICATE",
            "proof": (
                "Put P_n(u)=L_{n-1}^{(1)}(u). Chain and product rules give "
                "b_n'(t)=t^(-2)(P_n'(log t)-P_n(log t)). P_n'-P_n is a degree-(n-1) polynomial "
                "with leading coefficient (-1)^n/(n-1)!. If C_n is the sum of the absolute values of "
                "its coefficients, then |P_n'(u)-P_n(u)|<=C_n(1+u^(n-1)) for u>=0, because every "
                "u^j with 0<=j<=n-1 is at most 1+u^(n-1). Thus the frozen derivative bound holds "
                "for all t>=1, with n fixed before C_n and the t-limit."
            ),
        },
        {
            "obligation_id": "O3-BELLOTTI-TO-A",
            "status": "PROVED_IN_FROZEN_HAND_CERTIFICATE",
            "proof": (
                "Bellotti v1 defines Delta(x)=|psi(x)-x|/x and omega(x)=d(log x)^(3/5)/(log log x)^(1/5), "
                "d=(5^6 A_0^3/(2^2*3^4))^(1/5)>0, and Theorem 1.5 gives "
                "Delta(x)<<exp(55A_0)exp(-omega(x)). Hence for some C and all sufficiently large x, "
                "|A(x)|=|floor(x)-psi(x)|<=|floor(x)-x|+|x-psi(x)|<=1+C x exp(-omega(x))."
            ),
        },
        {
            "obligation_id": "O4-FIXED-N-BOUNDARY",
            "status": "PROVED_IN_FROZEN_HAND_CERTIFICATE",
            "proof": (
                "For fixed n, |P_n(log Y)|<=D_n(1+(log Y)^(n-1)). Combining O3 with b_n(Y)=P_n(log Y)/Y "
                "bounds |A(Y)b_n(Y)| by D_n(1+(log Y)^(n-1))/Y plus "
                "CD_n(1+(log Y)^(n-1))exp(-omega(Y)). The first term tends to zero. For u=log Y, "
                "omega(Y)=d u^(3/5)/(log u)^(1/5), which dominates every constant multiple of log u; "
                "therefore the second term also tends to zero."
            ),
        },
        {
            "obligation_id": "O5-FIXED-N-INTEGRAL",
            "status": "PROVED_IN_FROZEN_HAND_CERTIFICATE",
            "proof": (
                "O2-O3 bound |A(t)b_n'(t)| by C_n(1+(log t)^(n-1))/t^2 plus "
                "CC_n(1+(log t)^(n-1))exp(-omega(t))/t for all sufficiently large t. The first term "
                "is integrable. In the second set u=log t: it becomes a constant times "
                "integral (1+u^(n-1))exp(-d u^(3/5)/(log u)^(1/5))du, which converges because its "
                "exponent is at least d u^(1/2) eventually. The finite initial interval is harmless."
            ),
        },
        {
            "obligation_id": "O6-NATURAL-ORDER-LIMIT",
            "status": "PROVED_IN_FROZEN_HAND_CERTIFICATE",
            "proof": (
                "Apply O1 for each nonintegral Y and let Y tend to infinity through the original upper cutoff. "
                "O4 removes A(Y)b_n(Y), and O5 permits the improper-integral limit, giving "
                "lim_{Y->infinity}sum_{X<m<=Y}a_m b_n(m)=-A(X)b_n(X)-integral_X^infinity A(t)b_n'(t)dt. "
                "No term is permuted, regrouped, or made n-uniform."
            ),
        },
        {
            "obligation_id": "O7-NONABSOLUTE-WITNESS",
            "status": "PROVED_IN_FROZEN_HAND_CERTIFICATE",
            "proof": (
                "For every k>=1, 6k has distinct prime divisors 2 and 3, so it is not a prime power; hence "
                "Lambda(6k)=0 and |a_(6k)|=1. Since P_n has degree n-1 and leading coefficient "
                "(-1)^(n-1)/(n-1)!, for fixed n there are c_n>0 and K_n such that "
                "|b_n(6k)|>=c_n(log k)^(n-1)/k for k>=K_n (with P_1=1 for n=1). This positive "
                "subseries diverges by comparison with the harmonic series, so sum_m |a_m b_n(m)| diverges."
            ),
        },
    ]
    return seal({
        "schema_version": "1.0.0",
        "certificate_id": "RH-ANA-003-ABEL-001-C002-HAND-PROOF-CERTIFICATE-20260812",
        "candidate_id": CANDIDATE_ID,
        "candidate_core_sha256": CANDIDATE_CORE,
        "candidate_raw_sha256": CANDIDATE_RAW,
        "proof_input_raw_sha256": PROOF_INPUT_RAW,
        "frozen_at": FROZEN_AT,
        "proof_kind": "SOURCE_BOUND_SAME_CONTEXT_HAND_PROOF",
        "obligations": obligations,
        "scoped_conclusion_if_certificate_checks": (
            "For every fixed integer n>=1 and every nonintegral X>=1, the frozen natural-order Abel tail "
            "identity holds and the corresponding original term series is not absolutely convergent."
        ),
        "falsifiers": [
            "a nonintegral endpoint example contradicting O1",
            "an exact Laguerre coefficient contradicting O2 or O7",
            "Bellotti v1 equations (1.3)-(1.4) or Theorem 1.5 do not support O3",
            "one fixed n for which either O4 or O5 fails",
            "one m=6k that is a prime power",
            "any proof step requires n-uniformity, reordering, PR316, Li positivity, or RH",
        ],
        "authority": {
            "same_context_hand_proof": True,
            "machine_formal": False,
            "independent_review": False,
            "novelty": False,
            "riemann_hypothesis": False,
            "root": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
        "credit": {
            "mathematical": ["O1-O7 hand derivation as one fixed-n Abel convergence/nonabsolute unit"],
            "software_process": 0,
            "git_ci_schema_hash_runtime": 0,
        },
        "explicit_exclusions": [
            "NO_N_UNIFORMITY", "NO_REORDERING_OR_REGROUPING", "NO_PR316_RATE", "NO_LI_POSITIVITY",
            "NO_RH_CLAIM", "NO_NOVELTY", "NO_INDEPENDENT_REVIEW", "NO_GLOBAL_LEDGER_UPDATE",
        ],
        "source_evidence": {
            "bellotti": {
                "source": "Bellotti, arXiv:2508.02041v1",
                "retrieved_html_sha256": "2b57101a941e31c033ae2510efe8f4b3e81f22f025cd857fcb53d8ce77f3e634",
                "equation_1_3": "Delta(x)=|psi(x)-x|/x",
                "equation_1_4": "omega(x)=d(log x)^(3/5)/(log log x)^(1/5)",
                "theorem_1_5": "Delta(x)<<exp(55A_0)exp(-omega(x))",
            },
            "laguerre_normalization": "L_{n-1}^{(1)}(u)=sum_{j=0}^{n-1}(-1)^j binom(n,j+1)u^j/j!",
            "classical_identity": "finite Stieltjes/Abel summation with half-open nonintegral endpoints",
        },
    })


def build_documents() -> dict[str, dict]:
    if raw_hash(PROOF_INPUT) != PROOF_INPUT_RAW or raw_hash(CANDIDATE) != CANDIDATE_RAW:
        raise RuntimeError("frozen C002 proof-input identity changed")
    certificate = certificate_document()
    checker_raw = raw_hash(CHECKER)
    manifest = seal({
        "schema_version": "1.0.0",
        "manifest_id": "RH-ANA-003-ABEL-001-C002-PROOF-EVALUATOR-FREEZE-20260812",
        "candidate_id": CANDIDATE_ID,
        "candidate_core_sha256": CANDIDATE_CORE,
        "certificate_artifact_hash": certificate["artifact_hash"],
        "proof_input_raw_sha256": PROOF_INPUT_RAW,
        "checker": {"path": str(CHECKER.relative_to(ROOT)), "raw_sha256": checker_raw},
        "frozen_at": FROZEN_AT,
        "required_obligations": [f"O{i}" for i in range(1, 8)],
        "allowed_result_branches": [
            "ALL_O1_O7_SUPPORTED_BY_FROZEN_HAND_PROOF", "FINITE_ENDPOINT_IDENTITY_FALSE",
            "DERIVATIVE_OR_BOUND_FALSE", "BELLOTTI_BOUNDARY_OR_INTEGRAL_INSUFFICIENT",
            "ABSOLUTE_DIVERGENCE_WITNESS_FALSE", "CANNOT_CHECK",
        ],
        "status": "FROZEN_NOT_EXECUTED_UNTIL_PUBLIC_COMMIT",
        "authority": "RECORD_CHECK_ONLY_NO_MACHINE_FORMAL_OR_INDEPENDENT_AUTHORITY",
    })
    authorization = seal({
        "schema_version": "1.0.0",
        "authorization_id": "RH-ANA-003-ABEL-001-C002-POST-FREEZE-PROOF-CHECK-20260812",
        "authorization_source": "direct operator instruction after C002 merged on main; operational authorization only",
        "candidate_id": CANDIDATE_ID,
        "candidate_core_sha256": CANDIDATE_CORE,
        "certificate_artifact_hash": certificate["artifact_hash"],
        "evaluator_raw_sha256": checker_raw,
        "proof_derivation_authorized": True,
        "proof_check_authorized": True,
        "result_classification_authorized": True,
        "requires_public_freeze_commit": True,
        "public_freeze_commit_at_authorization_freeze": None,
        "authorized_operation": "run exact frozen checker after committing and pushing these freeze artifacts",
        "authorized_scope": "O1-O7 only",
        "forbidden": ["n-uniformity", "reordering", "PR316 rate", "Li positivity", "RH", "global ledger update"],
        "independent_review_authority": False,
        "machine_formal_proof_authority": False,
    })
    chronology = seal({
        "schema_version": "1.0.0",
        "chronology_id": "RH-ANA-003-ABEL-001-C002-PROOF-INPUT-CHRONOLOGY-20260812",
        "candidate_id": CANDIDATE_ID,
        "evaluation_base_commit": BASE_COMMIT,
        "origin_main_at_freeze": BASE_COMMIT,
        "proof_input": {"path": str(PROOF_INPUT.relative_to(ROOT)), "raw_sha256": PROOF_INPUT_RAW},
        "candidate": {"path": str(CANDIDATE.relative_to(ROOT)), "raw_sha256": CANDIDATE_RAW},
        "certificate_artifact_hash": certificate["artifact_hash"],
        "evaluator_raw_sha256": checker_raw,
        "frozen_at": FROZEN_AT,
        "proof_checker_executed_before_freeze": False,
        "result_classified_before_freeze": False,
        "required_sequence": ["commit and push freeze", "execute exact checker", "record result in second commit"],
    })
    framework_revalidation = seal({
        "schema_version": "1.0.0",
        "observation_id": "RH-ANA-003-ABEL-001-C002-PROOF-ROUND-FRAMEWORK-REVALIDATION-20260812",
        "candidate_id": CANDIDATE_ID,
        "observed_at": FROZEN_AT,
        "pinned_framework_sha": FRAMEWORK_PIN,
        "live_framework_origin_main_sha": FRAMEWORK_LIVE,
        "protected_surface_hashes": {
            "skills/rakl-core/static/core/principles.md": "fe0e80d1a8adab1f948f8e23d8aea842dd5b5e9d9921024d9466c9df0aacd728",
            "skills/rakl-core/static/core/workflow.md": "65cc1a23563ac3c978a801bc38e9712ad083b8a0afb44bcd0f0c2231102adcfe",
            "skills/rakl-core/workflows/mathematical-research.md": "7fe020438097a975d9b944720bde01a731e4860f469de3c735d52ce714cb3888",
            "src/rakl/method_specs.py": "ea954bff0168638ec23e13957c5a8b29fdfeac9b2d125c4fe5091025238eae45",
        },
        "protected_surfaces_byte_identical_between_pin_and_live": True,
        "new_relevant_modules": [
            {
                "path": "src/rakl/authority_transport.py",
                "classification": "PROPOSAL_ONLY_NOT_CANONICAL_RUNTIME_WIRING",
                "applicability": "No authority is transported or inherited in this proof round; the result remains a new scoped same-context hand-proof record with no independent/formal/root authority.",
            },
            {
                "path": "src/rakl/evidence_binding_certificate.py",
                "classification": "PROPOSAL_ONLY_NOT_CANONICAL_RUNTIME_WIRING",
                "applicability": "No scientific promotion is requested; exact source, candidate, proof-input, certificate, and checker identities remain explicitly bound.",
            },
            {
                "path": "src/rakl/epistemic_evolution.py",
                "classification": "SELF_RAKL_CHALLENGER_SELECTION_ONLY",
                "applicability": "This application proof round does not promote or modify RAKL.",
            },
            {
                "path": "src/rakl/mechanism_fidelity.py",
                "classification": "KNOWN_WORLD_MECHANISM_BENCHMARK_ONLY",
                "applicability": "The target is a mathematical lemma, not a mechanism-identification or prediction claim.",
            },
        ],
        "verdict": "CURRENT_NONBLOCKING_PROPOSAL_ONLY_ADDITIONS",
        "licenses_checker_execution_after_public_freeze": True,
        "grants_mathematical_or_scientific_authority": False,
        "recheck_trigger": "live framework main moves again before the result commit or a canonical mathematical-authority gate changes",
    })
    receipt = seal({
        "schema_version": "1.0.0",
        "receipt_id": "RH-ANA-003-ABEL-001-C002-HAND-PROOF-FREEZE-RECEIPT-20260812",
        "candidate_id": CANDIDATE_ID,
        "frozen_at": FROZEN_AT,
        "base_commit": BASE_COMMIT,
        "inputs": {"proof_input_raw_sha256": PROOF_INPUT_RAW, "candidate_raw_sha256": CANDIDATE_RAW},
        "outputs": {
            "certificate_artifact_hash": certificate["artifact_hash"],
            "manifest_artifact_hash": manifest["artifact_hash"],
            "authorization_artifact_hash": authorization["artifact_hash"],
            "chronology_artifact_hash": chronology["artifact_hash"],
            "framework_revalidation_artifact_hash": framework_revalidation["artifact_hash"],
            "checker_raw_sha256": checker_raw,
        },
        "status": "PUBLIC_FREEZE_PENDING_COMMIT_NO_CHECKER_EXECUTION_NO_RESULT",
        "mathematical_result_credit": False,
        "global_ledger_updated": False,
        "next_action": "commit and push exact freeze, then execute checker",
    })
    return {
        "certificate": certificate,
        "manifest": manifest,
        "authorization": authorization,
        "chronology": chronology,
        "framework_revalidation": framework_revalidation,
        "receipt": receipt,
    }


def main() -> None:
    docs = build_documents()
    for name, document in docs.items():
        path = ROOT / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
