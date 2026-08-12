#!/usr/bin/env python3
"""Materialize the authorized JY C001 fixed-n result and math lesson."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE_SHA = "aa6386126229bdfcae57fcf10a5b46ee8e91b83b"
AUTH_MERGE_SHA = BASE_SHA
CANDIDATE_ID = "RH-ANA-003j-D001-JY-C001-DIRECT-ENVELOPE"
BASE = "research/real_math/millennium/riemann_hypothesis"
EVALUATOR = f"{BASE}/05_oracles/rh_ana003j_d001_jy_c001_evaluator.py"
AUTHORIZATION = f"{BASE}/09_trace/RH_ANA_003j_D001_JY_C001_EXECUTION_AUTHORIZATION_20260812.json"
AUTHORIZATION_RAW_SHA256 = "6d2ee14ddff6bd99bf4001ba732113622a174b7518dc47324dd403e665a89b6f"
EVALUATOR_RAW_SHA256 = "55c73c2975924683ed537d394af75475022a6703a7a63c9d3a7c46bfeac31267"
PATHS = {
    "result": f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_PUBLIC_VALIDATION_RESULT_20260812.json",
    "lesson": f"{BASE}/07_memory/RH_ANA_003j_D001_JY_C001_MATHEMATICAL_LESSON_20260812.json",
    "review": f"{BASE}/08_reviews/RH_ANA_003j_D001_JY_C001_SAME_CONTEXT_RESULT_REVIEW_20260812.json",
}


def canonical_hash(value: dict) -> str:
    subject = copy.deepcopy(value)
    subject["artifact_hash"] = ""
    raw = json.dumps(subject, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def seal(value: dict) -> dict:
    value["artifact_hash"] = ""
    value["artifact_hash"] = canonical_hash(value)
    return value


def raw_hash(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def evaluator_module():
    if raw_hash(EVALUATOR) != EVALUATOR_RAW_SHA256:
        raise RuntimeError("evaluator identity mismatch")
    if raw_hash(AUTHORIZATION) != AUTHORIZATION_RAW_SHA256:
        raise RuntimeError("authorization identity mismatch")
    spec = importlib.util.spec_from_file_location("jy_c001_authorized_evaluator", ROOT / EVALUATOR)
    if not spec or not spec.loader:
        raise RuntimeError("cannot load evaluator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def result_document(output: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_C001_FIXED_N_DIRECT_ENVELOPE_RESULT",
        "result_id": "RH-ANA-003j-D001-JY-C001-RESULT-20260812",
        "candidate_id": CANDIDATE_ID,
        "result_status": "PASS_FIXED_N_DIRECT_ENVELOPE__LEAST_M_COMPUTABILITY_CANNOT_CHECK__COMPUTABLE_SUFFICIENT_TILDE_MODULUS",
        "recorded_at_utc": "2026-08-12T15:50:00Z",
        "chronology": {
            "result_base_sha": BASE_SHA,
            "authorization_path": AUTHORIZATION,
            "authorization_raw_sha256": AUTHORIZATION_RAW_SHA256,
            "authorization_artifact_hash": "sha256:74a46f4ac7101292452ae6e3c12e311c15f5b95ec60f22ed3f49677278809bc2",
            "authorization_merge_sha": AUTH_MERGE_SHA,
            "authorization_present_on_active_main_before_execution": True,
            "evaluator_raw_sha256": EVALUATOR_RAW_SHA256,
        },
        "proved_fixed_n_result": {
            "scope": "For each fixed integer n>=1 and epsilon>0, natural order and all real endpoints Y.",
            "coefficient_identity": "For 0<=j<=n-1, the coefficient of u^j in P_n'(u)-P_n(u) is (-1)^(j+1)q_(n,j), q_(n,j)=binom(n+1,j+2)/j!, by direct differentiation and Pascal's identity (including the top degree separately).",
            "normalization": "A(x)=floor(x)-psi(x), hence |A(x)|<=1+|psi(x)-x|; omitting +1 is invalid.",
            "change_of_variables_proof": [
                "In integral_u^infinity s^(j+a)exp(-c sqrt(s))ds set r=c sqrt(s), so s=(r/c)^2 and ds=2r c^(-2)dr.",
                "Therefore s^(j+a)ds=2c^(-2j-2a-2)r^(2j+2a+1)dr, with lower endpoint c sqrt(u).",
                "Thus the integral is exactly 2c^(-2j-2a-2)Gamma(2j+2a+2,c sqrt(u)); for a=1.515 the order and negative exponent are 2j+5.03 and the source amplitude becomes 18.78.",
            ],
            "envelope": "B_JY(n,u)=H_n(u)[exp(-u)+9.39u^1.515exp(-0.8274sqrt(u))]+sum_(j=0)^(n-1)q_(n,j)[Gamma(j+1,u)+18.78(0.8274)^(-2j-5.03)Gamma(2j+5.03,0.8274sqrt(u))].",
            "monotonicity_domain": "Only for u>=U_JY(n)=max(log 2,n-1,[2(n-1+1.515)/0.8274]^2): each u^jexp(-u) decreases for u>=j; each u^(j+1.515)exp(-0.8274sqrt(u)) decreases for u>=[2(j+1.515)/0.8274]^2; upper incomplete gamma decreases with its increasing lower endpoint.",
            "noninteger_bound": "For noninteger Y=exp(u) with u>=U_JY(n), the exact C002 Abel identity and the source-consistent Johnston--Yang bound give |S_n-R_n(Y)|<=B_JY(n,u).",
            "integer_endpoint_extension": "For integer Y let Y*=Y+1/2. Then R_n(Y*)=R_n(Y), log Y*>=log Y, and monotonicity gives B_JY(n,log Y*)<=B_JY(n,log Y). Thus the same real-Y threshold applies without regrouping.",
            "frozen_least_modulus": {
                "definition": "m_JY(n,epsilon) is the least integer m>=ceil(U_JY(n)) with B_JY(n,m)<=epsilon/2; M_JY(n,epsilon)=exp(m_JY(n,epsilon)).",
                "existence": "PROVED because B_JY is nonnegative, nonincreasing, and tends to zero for fixed n.",
                "least_index_computability": "CANNOT_CHECK",
                "blocker": "Certified interval refinement need not decide the non-strict comparison B_JY(n,m)<=epsilon/2 when equality holds, so a sequential search can stall before the least index. General constructive-real epsilon adds the same equality-decision obstruction.",
            },
            "computable_sufficient_tilde_modulus_algorithm": [
                "Input a fixed integer n>=1 and positive rational epsilon; compute the symbolic start m0=ceil(U_JY(n)).",
                "At dovetail stage k=1,2,..., compute certified enclosures for every B_JY(n,m), m0<=m<=m0+k, each with enclosure width at most 2^(-k).",
                "As soon as any enclosure has certified upper endpoint strictly below epsilon/2, choose the smallest such m at that stage and output it as tilde_m_JY(n,epsilon).",
                "Define the sufficient real threshold tilde_M_JY(n,epsilon)=exp(tilde_m_JY(n,epsilon)); if an integer cutoff is operationally required, use ceil(exp(tilde_m_JY(n,epsilon))).",
                "Termination follows because B_JY(n,m) tends to zero, so some later m has the strict margin B_JY(n,m)<epsilon/2; computability of exp and upper incomplete gamma supplies arbitrarily tight certified enclosures.",
                "This dovetailed strict-search threshold is not claimed to equal the frozen least-index M_JY.",
            ],
            "strict_epsilon_and_all_real_Y": "If Y>=tilde_M_JY then log Y>=tilde_m_JY and B_JY(n,log Y)<=B_JY(n,tilde_m_JY)<epsilon/2<epsilon. For integer Y the Y* argument above only decreases B. Hence |S_n-R_n(Y)|<epsilon for every real Y>=tilde_M_JY.",
            "numerical_M_values_materialized": False,
        },
        "machine_validation_receipt": output,
        "proof_computation_boundary": {
            "proof": "Exact coefficient arithmetic, the r=c sqrt(s) substitution, derivative sign calculations, gamma-tail monotonicity, endpoint identity, and limit argument establish the scoped result.",
            "computation": "The twelve fixed public rows and fifteen planted worlds corroborate implementation/algebra; 100-dps direct quadrature versus gammainc is corroboration only and is not theorem authority.",
        },
        "authority": {
            "fixed_n_direct_envelope": True,
            "frozen_least_M_exists": True,
            "frozen_least_M_computability": "CANNOT_CHECK",
            "computable_sufficient_tilde_M_algorithm": True,
            "numerical_M_value": False,
            "formal_proof": False,
            "independent_review": False,
            "novelty": False,
            "epsilon_n_or_diagonal": False,
            "li_positivity": False,
            "riemann_hypothesis": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
    })


def lesson_document(result: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_C001_SEVEN_FIELD_MATHEMATICAL_LESSON",
        "unit_id": "MATH-RH-ANA003J-D001-JY-C001-DIRECT-ENVELOPE",
        "candidate_id": CANDIDATE_ID,
        "result_hash": result["artifact_hash"],
        "attempted_implication": "Transfer Johnston--Yang's explicit all-x Chebyshev-psi error through A=floor-psi and the exact C002 Abel identity to a source-complete fixed-n direct envelope and a computable symbolic modulus.",
        "exact_result_or_failure": "The coefficient ledger, integral substitution, boundary/tail envelope, monotonicity on the frozen U_JY domain, and all-real endpoint extension prove the scoped fixed-n envelope and existence of the frozen least modulus. Least-index computability is CANNOT_CHECK because non-strict equality may stall interval refinement. A separately versioned dovetailed strict-search tilde_M is a computable sufficient modulus. No numerical modulus is produced and no moving-diagonal conclusion follows.",
        "supported_and_competing_causes": [
            "Supported: retaining the floor-error +1 creates the exp(-u) boundary and Gamma(j+1,u) tail components.",
            "Supported: r=c sqrt(s) forces factor 2, order 2j+5.03, and exponent -2j-5.03.",
            "Supported: the log-power shifts the monotonicity floor by +1.515; omitting it would understate the valid domain.",
            "Refuted competing transfer: Johnston--Yang's amplitude cannot be spliced with Bellotti's exp(55A_0) or d.",
            "Unresolved competing issue: fixed-n computability does not bound M_JY along an n-dependent epsilon_n or cutoff.",
            "Material failure preserved: existence of the frozen least index does not imply an algorithm that decides its non-strict defining inequality at equality.",
        ],
        "scope": "Each fixed n>=1, epsilon>0, exact natural order, endpoint remainder only, every real Y above the symbolic threshold; no n-uniform, internal-prefix, or diagonal statement.",
        "mathematical_falsifier": "A coefficient counterexample; failure of the substitution identity; a direct boundary monomial increasing at/above U_JY; an invalid C002 endpoint identity; failure of R_n(Y+1/2)=R_n(Y) at integer Y; or a source/version/hash normalization mismatch refutes the corresponding step.",
        "mathematical_repair": "If a falsifier fires, preserve the failure and repair only its exact coordinate: coefficient normalization, floor error, substitution Jacobian/order, monotonicity floor, endpoint convention, or whole-source profile. For the least-index decidability obstruction, retain frozen M_JY as existence-only and use the separately named strict-search tilde_M sufficient threshold; never relabel it as the least modulus. Never repair by mixing constants, changing epsilon after evaluation, or widening to a diagonal claim.",
        "proof_source_evidence": [
            "Johnston--Yang arXiv:2204.01980v2 Theorem 1.1 p.2, equation (1.3), Table 1 p.3 X=log 2 row",
            "PDF sha256:565993a6def48b237a68a92acba604f2c42f99165e0e71e390f8e21a313b74b2",
            "Exact C002 natural-order Abel identity and coefficient normalization",
            PATHS["result"],
        ],
        "mathematical_research_lessons": [
            "A source substitution is safe only as a complete profile transfer; exposed amplitude, decay, log power, and validity domain travel together.",
            "Cumulative-source normalization can create a separate analytic component: floor(x)-x is not cosmetic and generates its own boundary and gamma-tail terms.",
            "Change-of-variables bookkeeping simultaneously fixes Jacobian, gamma order, and prefactor exponent, so hostile mutations should target all three independently.",
            "Polynomial powers change the derivative-sign domain; the +1.515 in U_JY is a load-bearing consequence of the source log power.",
            "Step-function endpoint repair needs both equality of the remainder and the correct monotonicity direction after shifting Y upward.",
            "Existence of a least threshold under a non-strict computable-real inequality does not ensure decidability; a dovetailed strict-margin search yields a computable sufficient threshold but not necessarily the least one.",
            "Independent high-precision agreement is useful corroboration but cannot replace the exact substitution derivation.",
        ],
        "nonmathematical_governance_note": "Git, PR, CI, schema, serialization, fixture, and hash checks receive zero mathematical-lesson and theorem credit.",
        "framework_delta": "NONE; no reusable framework change is proposed or promoted.",
    })


def review_document(result: dict, lesson: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_C001_SAME_CONTEXT_RESULT_REVIEW",
        "review_id": "RH-ANA-003j-D001-JY-C001-SAME-CONTEXT-REVIEW-20260812",
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT_REVIEW",
        "result_hash": result["artifact_hash"],
        "lesson_hash": lesson["artifact_hash"],
        "lenses": [
            {"role": "domain_theory", "finding": "The bound is source-consistent and fixed-n only.", "objection": "No diagonal rate follows from symbolic computability."},
            {"role": "analogy_method_transfer", "finding": "Whole-profile source substitution succeeds.", "objection": "Bellotti constants cannot be retained."},
            {"role": "adversarial_falsification", "finding": "All planted algebra/normalization/domain/source mutations classify as frozen.", "objection": "Endpoint equality and strict epsilon must remain explicit."},
            {"role": "formal_methods", "finding": "The proof is exact hand algebra with machine exact-arithmetic checks.", "objection": "This is not a formal proof assistant receipt."},
            {"role": "novelty_research_value", "finding": "The result repairs source completeness for the scoped modulus atom.", "objection": "No novelty or RH claim is supported."},
        ],
        "strongest_objection": "The least-integer modulus may grow too quickly for any useful moving diagonal; that comparison is explicitly unfrozen and untested.",
        "verdict": "PASS_SCOPED_FIXED_N_RESULT_ONLY",
        "nonclaims": ["independent review", "formal proof", "novelty", "epsilon_n", "diagonal C", "Li positivity", "RH"],
    })


def build_all() -> dict[str, dict]:
    output = evaluator_module().run_validation(ROOT)
    if output["overall_classification"] != "PASS":
        raise RuntimeError("authorized evaluator did not pass")
    result = result_document(output)
    lesson = lesson_document(result)
    review = review_document(result, lesson)
    return {PATHS["result"]: result, PATHS["lesson"]: lesson, PATHS["review"]: review}


def main() -> None:
    for relative, value in build_all().items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
