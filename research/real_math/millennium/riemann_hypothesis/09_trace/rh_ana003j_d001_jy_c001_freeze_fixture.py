#!/usr/bin/env python3
"""Freeze the RH ANA003j D001 Johnston--Yang direct-envelope candidate.

This deterministic fixture materializes a candidate identity, prospective
falsifier worlds, symbolic public validation inputs, and one hash-chained
``CANDIDATE_PROPOSED`` trace event.  It deliberately does not implement or run
an evaluator, evaluate an incomplete gamma function or envelope, calculate a
modulus value, choose epsilon_n or a diagonal cutoff, or classify a result.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
APPLICATION_BASE_SHA = "334c3cf0a405906fe14b07067d6d7f73b6170d4f"
SOURCE_COMMIT_SHA = "93ff7026d27a1cf1b4f698448e7a8501b04a07b7"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
ATOM = "RH-ANA-003j-D001-JY-SA001"
CANDIDATE_ID = "RH-ANA-003j-D001-JY-C001-DIRECT-ENVELOPE"
FROZEN_AT = "2026-08-12T15:10:00Z"
JY_PDF_SHA256 = "565993a6def48b237a68a92acba604f2c42f99165e0e71e390f8e21a313b74b2"

BASE = "research/real_math/millennium/riemann_hypothesis"
PATHS = {
    "candidate": f"{BASE}/04_candidates/RH_ANA_003j_D001_JY_C001_DIRECT_ENVELOPE_CANDIDATE_FREEZE_20260812.json",
    "falsifier": f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_FALSIFIER_FREEZE_20260812.json",
    "validation_inputs": f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_PUBLIC_VALIDATION_INPUTS_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003j_D001_JY_C001_CANDIDATE_FREEZE_TRACE_20260812.json",
}

EVIDENCE_PATHS = {
    "jy_source_assimilation": f"{BASE}/01_frontier/RH_ANA_003j_D001_JY_SOURCE_ASSIMILATION_PACKET_20260812.json",
    "jy_context": f"{BASE}/01_frontier/RH_ANA_003j_D001_JY_MATH_CONTEXT_FIBER_20260812.json",
    "jy_prior_failure_assimilation": f"{BASE}/07_memory/RH_ANA_003j_D001_JY_PRIOR_FAILURE_ASSIMILATION_20260812.json",
    "jy_memory_review": f"{BASE}/07_memory/RH_ANA_003j_D001_JY_RESEARCH_MEMORY_REVIEW_20260812.json",
    "jy_expert_review": f"{BASE}/08_reviews/RH_ANA_003j_D001_JY_EXPERT_SOURCE_ASSIMILATION_REVIEW_20260812.json",
    "jy_shortcut_review": f"{BASE}/08_reviews/RH_ANA_003j_D001_JY_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "jy_pre_candidate_trace": f"{BASE}/09_trace/RH_ANA_003j_D001_JY_PRE_CANDIDATE_TRACE_20260812.json",
    "c002_candidate": f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_FIXED_N_ABEL_CANDIDATE_FREEZE_20260812.json",
    "c002_proof_result": f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json",
    "d001_source_audit": f"{BASE}/03_sources/RH_ANA_003j_D001_EXACT_SOURCE_SCOPE_AUDIT_20260812.json",
    "d001_conditional_result": f"{BASE}/05_oracles/RH_ANA_003j_D001_MODULUS_SOURCE_RESULT_20260812.json",
    "d001_mathematical_lesson": f"{BASE}/07_memory/RH_ANA_003j_D001_MATHEMATICAL_LESSON_20260812.json",
    "d001_failure_experience": f"{BASE}/07_memory/RH_ANA_003j_D001_FAILURE_EXPERIENCE_20260812.json",
    "framework_pin": "config/rakl-framework-pin.json",
}

EXPECTED_RAW_SHA256 = {
    "jy_source_assimilation": "d3628027d20733d81524e48c864d4fdf6c58ade2c9eb88e2d6ec0a838dd72490",
    "jy_context": "a0d4f1604aa22868e3558a31e502887620c94ee3068acb3abff7e1574b208af3",
    "jy_prior_failure_assimilation": "3381b5ee16e436613ed3ed6d4ba6b40f5c949bb2b29c69d903bd80f44733486d",
    "jy_memory_review": "e2f3229d604d1e382a0f674555538c40cbc729e00b3155fba9a4e537574895a0",
    "jy_expert_review": "2d27323bcdc82bb75a8af89ae890c877fa869c32187e3a9b0c9f30c9a103ab5e",
    "jy_shortcut_review": "f81c57e7968d5f2bdb01e39cb0d32df0db4f10982d7ecc85b1445a29e67cb9fd",
    "jy_pre_candidate_trace": "aa0dba40ed2ab5872e6a3f915e14f8f0dcee34bdd509deda02dcfc824537606c",
    "c002_candidate": "7eb1e7e369dde0b6532ceae005f62fabf37e83abe2dd7cd663d1cd60137189a8",
    "c002_proof_result": "0d1dd6087f752307f4270ce97b1ad4f88d6809037a856c979837b85d94b91b6b",
    "d001_source_audit": "46abdbad71ecd04e47f255afb18a92482a65d5374feb5d33aa57e71080a01346",
    "d001_conditional_result": "2e9f247aa2aff699bbbd94ecb2ada4ed61d16e703172a555340f974069a7aedd",
    "d001_mathematical_lesson": "18b1ff51a40c2d5187516414791a840bb3624e56fb5c8d784f28269d4b31630c",
    "d001_failure_experience": "97eca225bd813ede522e6a8458f572c50c808d8bb9ad5acbdaaaa27dafb56c46",
    "framework_pin": "e97dbc1c49d9338b3340338b8173f0c8c3f2f6aff53be08af7e60d2b183dd6e7",
}


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def canonical_hash(value: dict, field: str = "artifact_hash") -> str:
    subject = copy.deepcopy(value)
    subject[field] = ""
    return "sha256:" + hashlib.sha256(canonical(subject)).hexdigest()


def seal(value: dict) -> dict:
    document = dict(value)
    document["artifact_hash"] = ""
    document["artifact_hash"] = canonical_hash(document)
    return document


def raw_binding(name: str) -> dict:
    path = EVIDENCE_PATHS[name]
    digest = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
    expected = EXPECTED_RAW_SHA256[name]
    if digest != expected:
        raise RuntimeError(f"raw evidence mismatch for {name}: {digest} != {expected}")
    return {"path": path, "raw_sha256": digest}


def evidence_bindings() -> dict[str, dict]:
    return {name: raw_binding(name) for name in EVIDENCE_PATHS}


def candidate_document() -> dict:
    core = {
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_DIRECT_ENVELOPE_CANDIDATE_FREEZE",
        "candidate_id": CANDIDATE_ID,
        "atom_id": ATOM,
        "status": "FROZEN_UNEVALUATED_DIRECT_ENVELOPE_PROPOSAL",
        "frozen_at_utc": FROZEN_AT,
        "object_qoi_context": {
            "object": "The exact C002 fixed-n natural-order endpoint remainder after a source-consistent substitution of the Johnston--Yang all-x Chebyshev-psi error bound.",
            "quantity_of_interest": "Whether the displayed direct incomplete-gamma envelope is a valid explicit upper bound and yields the displayed symbolic fixed-n modulus family.",
            "scope": "For each fixed integer n>=1, epsilon>0, and real endpoint Y only; candidate and falsifier freeze before any evaluation.",
        },
        "chronology": {
            "application_base_sha": APPLICATION_BASE_SHA,
            "source_assimilation_commit_sha": SOURCE_COMMIT_SHA,
            "source_assimilation_pr": "https://github.com/SzeChunYiu/RAKL_math/pull/400",
            "pre_candidate_packet_committed_before_candidate": True,
            "candidate_result_accessed_before_freeze": False,
            "evaluator_implemented_or_executed_before_freeze": False,
            "framework_pin_sha": FRAMEWORK_SHA,
        },
        "primary_source": {
            "authors": ["Daniel R. Johnston", "Andrew Yang"],
            "title": "Some explicit estimates for the error term in the prime number theorem",
            "arxiv": "2204.01980v2 [math.NT]",
            "version_date": "2022-04-20",
            "pdf_sha256": JY_PDF_SHA256,
            "doi": "10.1016/j.jmaa.2023.127460",
            "exact_anchors": [
                "Theorem 1.1, arXiv PDF page 2",
                "equation (1.3), arXiv PDF page 2",
                "Table 1, arXiv PDF page 3, X=log 2 row",
            ],
            "exact_bound": "For every real x>=2, |psi(x)-x| <= 9.39 x (log x)^1.515 exp(-0.8274 sqrt(log x)).",
            "exact_decimal_constants": {
                "amplitude": "9.39",
                "log_power_a": "1.515",
                "sqrt_log_decay_c": "0.8274",
                "x_threshold": "2",
            },
        },
        "normalization": {
            "Delta": "Delta(x)=|psi(x)-x|/x",
            "application_source": "A(x)=floor(x)-psi(x)",
            "required_transfer": "|A(x)| <= 1 + |psi(x)-x|",
            "transferred_bound": "For x>=2, |A(x)| <= 1 + 9.39 x (log x)^1.515 exp(-0.8274 sqrt(log x)).",
            "floor_error_one_is_mandatory": True,
        },
        "exact_definitions": {
            "domain": "n is an integer >=1; j is an integer with 0<=j<=n-1; u=log Y",
            "a": "1.515",
            "c": "0.8274",
            "h": "h_(n,j)=binom(n,j+1)/j!",
            "q": "q_(n,j)=binom(n+1,j+2)/j!",
            "P": "P_n(u)=L_(n-1)^(1)(u)=sum_(j=0)^(n-1)(-1)^j h_(n,j)u^j",
            "P_derivative_minus_P": "P_n'(u)-P_n(u)=sum_(j=0)^(n-1)(-1)^(j+1)q_(n,j)u^j",
            "H": "H_n(u)=sum_(j=0)^(n-1)h_(n,j)u^j",
            "Q": "Q_n(u)=sum_(j=0)^(n-1)q_(n,j)u^j",
            "upper_incomplete_gamma": "Gamma(alpha,z)=integral_z^infinity t^(alpha-1)exp(-t)dt",
        },
        "candidate_envelope": {
            "integral_identity": "integral_u^infinity s^(j+a)exp(-c sqrt(s))ds = 2 c^(-2j-2a-2) Gamma(2j+2a+2,c sqrt(u))",
            "specialized_integral_identity": "With a=1.515: integral_u^infinity s^(j+1.515)exp(-0.8274 sqrt(s))ds = 2(0.8274)^(-2j-5.03)Gamma(2j+5.03,0.8274 sqrt(u)).",
            "formula": "B_JY(n,u)=H_n(u)[exp(-u)+9.39u^1.515exp(-0.8274sqrt(u))]+sum_(j=0)^(n-1)q_(n,j)[Gamma(j+1,u)+18.78(0.8274)^(-2j-5.03)Gamma(2j+5.03,0.8274sqrt(u))].",
            "monotonicity_floor": "U_JY(n)=max(log 2,n-1,[2(n-1+1.515)/0.8274]^2).",
            "floor_rationale_to_validate": [
                "u^j exp(-u) is nonincreasing for u>=j, so n-1 covers every boundary floor-error monomial.",
                "u^(j+1.515)exp(-0.8274sqrt(u)) is nonincreasing when u>=[2(j+1.515)/0.8274]^2, so j=n-1 supplies the frozen maximum.",
                "Each upper incomplete-gamma term is nonincreasing as its positive lower endpoint increases.",
            ],
            "symbolic_modulus": {
                "log_threshold": "m_JY(n,epsilon)=the least integer m>=ceil(U_JY(n)) such that B_JY(n,m)<=epsilon/2",
                "threshold": "M_JY(n,epsilon)=exp(m_JY(n,epsilon))",
                "evaluation_status": "SYMBOLIC_DEFINITION_ONLY_NOT_EVALUATED",
            },
        },
        "candidate_implication_obligations": {
            "noninteger_endpoint": "For noninteger Y=exp(u), validate from the exact C002 Abel identity that |S_n-R_n(Y)|<=B_JY(n,u) for u>=U_JY(n).",
            "integer_endpoint": "For integer Y, set Y*=Y+1/2; validate R_n(Y*)=R_n(Y), log Y*>=log Y, and B_JY(n,log Y*)<=B_JY(n,log Y), so the same threshold extends to every real Y.",
            "modulus": "Only after the envelope and monotonicity obligations pass, validate that for every fixed n>=1 and epsilon>0, every real Y>=M_JY(n,epsilon) has |S_n-R_n(Y)|<epsilon.",
            "status": "FROZEN_CANDIDATE_OBLIGATIONS_NOT_PROVED_OR_TESTED_THIS_ROUND",
        },
        "independent_hostile_cross_check": {
            "role": "INDEPENDENT_ALGEBRAIC_CROSS_CHECK_NOT_PREFERRED_CANDIDATE",
            "constants": {"K": "172", "decay": "0.4", "x_threshold": "2"},
            "decay_gap": "D=0.8274-0.4=0.4274",
            "transformed_ratio": "With v=sqrt(u), the ratio is 9.39 v^3.03 exp(-Dv).",
            "derivative": "d/dv log(v^3.03 exp(-Dv))=3.03/v-D",
            "maximizer": "v*=3.03/D",
            "maximum": "9.39[3.03/(eD)]^3.03=171.43357721989227<172",
            "denominator_guard": "The denominator is D, not 2D; 3.03=2*1.515 already.",
            "source_consistency": "This is derived solely from Johnston--Yang and is never mixed with Bellotti constants.",
        },
        "bellotti_boundary": {
            "status": "EFFECTIVE_BUT_CONSTANT_AND_THRESHOLD_UNEXPOSED_IN_ACQUIRED_TEXT",
            "ineffectivity_claimed": False,
            "mixing_forbidden": [
                "9.39 is not Bellotti's K_B",
                "do not retain Bellotti's exp(55A_0) or d with the Johnston--Yang amplitude",
                "do not drop (log x)^1.515 without the explicit independent 172 domination proof",
            ],
        },
        "comparison_boundary": {
            "direct_versus_simple_order_claim": "NONE_FROZEN_OR_AUTHORIZED",
            "reason": "No pointwise or aggregate larger/smaller comparison was derived in this freeze round.",
        },
        "evaluation_firewall": {
            "evaluator_implemented": False,
            "evaluator_executed": False,
            "falsifier_run_event_emitted": False,
            "envelope_values_calculated": False,
            "M_values_calculated": False,
            "natural_order_remainder_tests_run": False,
            "epsilon_sequence_identity": None,
            "diagonal_cutoff_constant_identity": None,
            "diagonal_comparison_attempted": False,
            "result_classified": False,
        },
        "explicit_exclusions": [
            "NO_EVALUATOR_IMPLEMENTATION_OR_EXECUTION",
            "NO_B_JY_OR_M_JY_NUMERICAL_VALUES",
            "NO_NATURAL_ORDER_REMAINDER_TEST",
            "NO_EPSILON_N_SELECTION",
            "NO_DIAGONAL_C_SELECTION",
            "NO_INTERNAL_PREFIX_CONTROL",
            "NO_MATHEMATICAL_RESULT_CLAIM",
            "NO_NOVELTY_CLAIM",
            "NO_INDEPENDENT_REVIEW_CLAIM",
            "NO_LI_POSITIVITY_CLAIM",
            "NO_RIEMANN_HYPOTHESIS_CLAIM",
        ],
        "authority": {
            "candidate_proposal_only": True,
            "mathematical_result": False,
            "proof": False,
            "novelty": False,
            "independent_review": False,
            "li_positivity": False,
            "riemann_hypothesis": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "software_or_governance_credit_units": 0,
        },
        "evidence_bindings": evidence_bindings(),
    }
    identity = {
        "candidate_id": CANDIDATE_ID,
        "canonical_core_sha256": "sha256:" + hashlib.sha256(canonical(core)).hexdigest(),
        "identity_scope": "FULL_CANDIDATE_CORE_BEFORE_IDENTITY_AND_ARTIFACT_HASH",
    }
    return seal({**core, "candidate_identity": identity})


def falsifier_document(candidate: dict) -> dict:
    fail_worlds = [
        ("ALG-WRONG-GAMMA-ORDER", "algebra", "Replace every direct-tail order 2j+5.03 by 2j+4.03.", "The substitution r=c sqrt(s) fixes order 2j+2a+2=2j+5.03."),
        ("ALG-MISSING-FACTOR-TWO", "algebra", "Remove the leading factor 2 from the incomplete-gamma integral identity and the derived 18.78 amplitude.", "The Jacobian ds=2r c^(-2)dr supplies the factor 2."),
        ("ALG-WRONG-PREFACTOR-EXPONENT", "algebra", "Replace c^(-2j-5.03) by c^(-2j-4.03).", "The power after substitution is exactly -2j-2a-2=-2j-5.03."),
        ("NORM-OMIT-FLOOR-ONE", "normalization", "Use |A(x)|<=|psi(x)-x| and omit the additive floor-error one.", "A=floor(x)-psi(x) requires |floor(x)-x|<=1."),
        ("NORM-REDEFINE-A", "normalization", "Treat A(x) as exactly x-psi(x).", "The C002 cumulative source is floor(x)-psi(x), not x-psi(x)."),
        ("MONO-DROP-LOG-POWER", "monotonicity", "Use a floor with [2(n-1)/0.8274]^2 and omit +1.515 from the direct boundary term.", "The direct source boundary contains u^(j+1.515)."),
        ("MONO-BELOW-DOMAIN", "monotonicity", "Claim B_JY is nonincreasing below log 2 or below the frozen componentwise floor.", "The source and boundary derivative domains are part of the candidate obligation."),
        ("SOURCE-CALL-939-BELLOTTI", "source_mismatch", "Call 9.39 Bellotti's K_B.", "9.39 is the Johnston--Yang amplitude; Bellotti's K_B remains unexposed in the acquired text."),
        ("SOURCE-MIX-BELLOTTI-FACTORS", "source_mismatch", "Retain Bellotti's exp(55A_0) or d with the Johnston--Yang amplitude.", "Constants from distinct source profiles cannot be spliced without a separate derivation."),
        ("SOURCE-DROP-LOG-POWER", "source_mismatch", "Drop (log x)^1.515 without the explicit K=172, decay=0.4 domination proof.", "The Johnston--Yang source statement contains the log-power factor."),
    ]
    cannot_check_worlds = [
        ("CC-SOURCE-BYTES", "The Johnston--Yang PDF, exact hash, or v2 identity is unavailable or mismatched."),
        ("CC-C002-IDENTITY", "The exact C002 Abel identity or its A(x)=floor(x)-psi(x) normalization is unavailable."),
        ("CC-NUMERIC-CONTRACT", "Numerical special-function validation is requested outside a frozen input and precision contract."),
        ("CC-EVALUATOR-SOURCE", "A future evaluator lacks the required source bytes or cannot reproduce their raw SHA-256 bindings."),
    ]
    worlds = [
        {
            "world_id": world_id,
            "category": category,
            "input_mutation": mutation,
            "expected_future_classification": "FAIL",
            "classification_basis": reason,
        }
        for world_id, category, mutation, reason in fail_worlds
    ]
    worlds.extend(
        {
            "world_id": world_id,
            "category": "structural_unavailability",
            "input_condition": condition,
            "expected_future_classification": "CANNOT_CHECK",
            "classification_basis": "Missing or unfrozen authority-bearing input fails closed and cannot be relabeled PASS or FAIL.",
        }
        for world_id, condition in cannot_check_worlds
    )
    worlds.append(
        {
            "world_id": "CONTROL-EXACT-DIRECT-FORMULA",
            "category": "control",
            "input_condition": "Exact Johnston--Yang v2 source/hash, exact C002 identity and normalization, exact coefficient ledger, exact direct formula, exact U_JY floor, and all required bytes match the frozen packet.",
            "expected_future_classification": "PASS",
            "classification_basis": "Positive control for future evaluator validation only; this expected label is not an executed result.",
        }
    )
    return seal(
        {
            "schema_version": "1.0.0",
            "record_type": "RH_ANA003J_D001_JY_DIRECT_ENVELOPE_FALSIFIER_FREEZE",
            "falsifier_id": "RH-ANA-003j-D001-JY-C001-FALSIFIER-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "candidate_artifact_hash": candidate["artifact_hash"],
            "frozen_at_utc": "2026-08-12T15:10:01Z",
            "status": "FROZEN_EXPECTED_WORLDS_EVALUATOR_NOT_IMPLEMENTED_OR_EXECUTED",
            "classification_vocabulary": ["PASS", "FAIL", "CANNOT_CHECK"],
            "worlds": worlds,
            "future_evaluator_contract": {
                "implementation_path": None,
                "implementation_frozen": False,
                "execution_authorized_this_round": False,
                "must_check_candidate_identity": True,
                "must_check_all_raw_source_bindings": True,
                "must_not_infer_missing_inputs": True,
                "must_not_emit_a_mathematical_result_from_expected_labels": True,
            },
            "result_state": "NO_FALSIFIER_RUN_NO_RESULT_CLASSIFICATION",
            "authority": {
                "expected_labels_are_oracle_inputs_only": True,
                "proof": False,
                "mathematical_result": False,
                "independent_review": False,
                "li_or_rh_authority": False,
            },
        }
    )


def validation_inputs_document(candidate: dict, falsifier: dict) -> dict:
    rows = []
    for n in (1, 2, 3, 5):
        for suffix, constructor in (
            ("AT-U", f"U_JY({n})"),
            ("AT-CEIL-U", f"ceil(U_JY({n}))"),
            ("AFTER-CEIL-U", f"ceil(U_JY({n}))+1"),
        ):
            rows.append(
                {
                    "input_id": f"N{n}-{suffix}",
                    "n": n,
                    "j_domain": f"integers 0<=j<={n-1}",
                    "u_exact_constructor": constructor,
                    "u_decimal_value": None,
                    "B_JY_value": None,
                    "M_JY_value": None,
                }
            )
    return seal(
        {
            "schema_version": "1.0.0",
            "record_type": "RH_ANA003J_D001_JY_PUBLIC_VALIDATION_INPUT_FREEZE",
            "input_set_id": "RH-ANA-003j-D001-JY-C001-PUBLIC-SMALL-N-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "falsifier_artifact_hash": falsifier["artifact_hash"],
            "frozen_at_utc": "2026-08-12T15:10:02Z",
            "status": "FROZEN_SYMBOLIC_INPUTS_NOT_EXECUTED",
            "construction_rules": {
                "n_values": [1, 2, 3, 5],
                "u_values_for_each_n": ["U_JY(n)", "ceil(U_JY(n))", "ceil(U_JY(n))+1"],
                "U_JY": "max(log 2,n-1,[2(n-1+1.515)/0.8274]^2)",
                "exact_decimal_rule": "The decimal tokens 1.515 and 0.8274 are exact source-bound decimal constants; no rounded binary or printed U value is frozen.",
            },
            "inputs": rows,
            "intended_future_checks": [
                "Verify h_(n,j)=binom(n,j+1)/j!, q_(n,j)=binom(n+1,j+2)/j!, and the coefficient identity for P_n'-P_n.",
                "Verify the incomplete-gamma identity with order 2j+5.03, factor 2, and prefactor exponent -2j-5.03.",
                "Verify every component of B_JY is nonnegative on the frozen domain.",
                "Verify componentwise monotonicity at and above U_JY(n), including the +1.515 boundary power.",
                "Verify the noninteger Abel implication and the integer Y*=Y+1/2 endpoint extension without regrouping.",
            ],
            "numeric_precision_contract": {
                "status": "NOT_FROZEN_IN_THIS_ROUND",
                "consequence": "Any numerical special-function validation is CANNOT_CHECK until a later public precision contract is frozen.",
            },
            "comparison_rule": "Do not classify the direct envelope as larger or smaller than the simple 172 envelope unless a later exact derivation is frozen.",
            "execution_firewall": {
                "coefficient_values_calculated": False,
                "special_function_values_calculated": False,
                "envelope_values_calculated": False,
                "M_values_calculated": False,
                "natural_order_remainder_values_calculated": False,
            },
            "authority": {
                "inputs_only": True,
                "evaluation_result": False,
                "mathematical_result": False,
                "proof": False,
                "li_or_rh_authority": False,
            },
        }
    )


def trace_document(candidate: dict, falsifier: dict, inputs: dict) -> dict:
    pre_path = EVIDENCE_PATHS["jy_pre_candidate_trace"]
    pre_trace = json.loads((ROOT / pre_path).read_text(encoding="utf-8"))
    entries = copy.deepcopy(pre_trace["entries"])
    event = {
        "event_id": "RH-ANA003J-D001-JY-C001-E09",
        "atom_id": ATOM,
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": "2026-08-12T15:10:03Z",
        "state_summary": "The exact direct Johnston--Yang boundary-plus-tail envelope, symbolic modulus, planted PASS/FAIL/CANNOT_CHECK worlds, and symbolic small-n inputs are frozen after the public pre-candidate packet and before any evaluator or result access.",
        "action_summary": "Freeze C001 candidate identity and prospective falsifiers only; do not implement or execute evaluation.",
        "evidence_pointers": [
            PATHS["candidate"],
            PATHS["falsifier"],
            PATHS["validation_inputs"],
            pre_path,
        ],
        "alternatives_considered": [
            "freeze the direct Johnston--Yang envelope",
            "promote the simpler 172 domination as the preferred candidate",
            "mix Johnston--Yang amplitude with Bellotti factors",
            "calculate modulus values immediately",
        ],
        "decision_rationale": "The pre-candidate SEARCH review selected the source-consistent direct family; freezing exact algebra and hostile worlds now prevents post-result correction while the independent 172 derivation remains a cross-check only.",
        "outputs": [
            CANDIDATE_ID,
            candidate["candidate_identity"]["canonical_core_sha256"],
            falsifier["artifact_hash"],
            inputs["artifact_hash"],
            "FROZEN_UNEVALUATED",
            "NO_FALSIFIER_RUN",
            "ZERO_MATHEMATICAL_RESULT_CREDIT",
        ],
        "uncertainties": [
            "exact envelope implication remains unevaluated",
            "monotonicity and endpoint-extension obligations remain unevaluated",
            "no numerical special-function precision contract exists",
            "same-context freeze is not independent review",
        ],
        "residuals": [
            "future evaluator implementation and public precision contract",
            "future candidate-bound validation",
            "moving diagonal, internal prefixes, Li positivity, and RH remain open",
        ],
        "next_steps": [
            "commit and publish this freeze before evaluator implementation",
            "in a successor round implement the frozen evaluator without changing candidate identity or planted worlds",
            "retain any FAIL or CANNOT_CHECK result without threshold rescue",
        ],
        "previous_event_hash": entries[-1]["artifact_hash"],
        "artifact_hash": "",
    }
    event["artifact_hash"] = canonical_hash(event)
    entries.append(event)
    return {
        "trace_id": "RH-ANA003J-D001-JY-C001-CANDIDATE-FREEZE-TRACE-20260812",
        "entries": entries,
    }


def build_all() -> dict[str, dict]:
    candidate = candidate_document()
    falsifier = falsifier_document(candidate)
    inputs = validation_inputs_document(candidate, falsifier)
    trace = trace_document(candidate, falsifier, inputs)
    return {
        PATHS["candidate"]: candidate,
        PATHS["falsifier"]: falsifier,
        PATHS["validation_inputs"]: inputs,
        PATHS["trace"]: trace,
    }


def main() -> None:
    for relative, value in build_all().items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
