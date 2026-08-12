#!/usr/bin/env python3
"""Build the RH ANA003j D001 Johnston--Yang source-assimilation packet.

This fixture freezes source/context/memory/review/trace state only.  It does not
freeze a mathematical candidate, select a result branch, calculate modulus
values, or execute a numerical remainder test.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
BASE_SHA = "686a73336f00ebc9f9441c0c3f64042f5caf046f"
ATOM = "RH-ANA-003j-D001-JY-SA001"
PARENT_ATOM = "RH-ANA-003j"
TIME = "2026-08-12T14:50:00Z"
JY_PDF_SHA256 = "565993a6def48b237a68a92acba604f2c42f99165e0e71e390f8e21a313b74b2"

SOURCE_PACKET = "research/real_math/millennium/riemann_hypothesis/01_frontier/RH_ANA_003j_D001_JY_SOURCE_ASSIMILATION_PACKET_20260812.json"
CONTEXT = "research/real_math/millennium/riemann_hypothesis/01_frontier/RH_ANA_003j_D001_JY_MATH_CONTEXT_FIBER_20260812.json"
FAILURE_ASSIMILATION = "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_003j_D001_JY_PRIOR_FAILURE_ASSIMILATION_20260812.json"
MEMORY = "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_003j_D001_JY_RESEARCH_MEMORY_REVIEW_20260812.json"
EXPERT = "research/real_math/millennium/riemann_hypothesis/08_reviews/RH_ANA_003j_D001_JY_EXPERT_SOURCE_ASSIMILATION_REVIEW_20260812.json"
SHORTCUT = "research/real_math/millennium/riemann_hypothesis/08_reviews/RH_ANA_003j_D001_JY_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json"
TRACE = "research/real_math/millennium/riemann_hypothesis/09_trace/RH_ANA_003j_D001_JY_PRE_CANDIDATE_TRACE_20260812.json"

PRIOR = {
    "source_audit": "research/real_math/millennium/riemann_hypothesis/03_sources/RH_ANA_003j_D001_EXACT_SOURCE_SCOPE_AUDIT_20260812.json",
    "conditional_result": "research/real_math/millennium/riemann_hypothesis/05_oracles/RH_ANA_003j_D001_MODULUS_SOURCE_RESULT_20260812.json",
    "mathematical_lesson": "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_003j_D001_MATHEMATICAL_LESSON_20260812.json",
    "failure_experience": "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_003j_D001_FAILURE_EXPERIENCE_20260812.json",
    "c002_result": "research/real_math/millennium/riemann_hypothesis/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json",
    "dgs_normalization": "research/real_math/millennium/riemann_hypothesis/03_sources/RH_ANA_003j_D001_EXACT_SOURCE_SCOPE_AUDIT_20260812.json",
}


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def canonical_hash(value: dict, field: str = "artifact_hash") -> str:
    subject = copy.deepcopy(value)
    subject[field] = ""
    return "sha256:" + hashlib.sha256(canonical(subject)).hexdigest()


def raw_binding(path: str) -> dict:
    raw = (ROOT / path).read_bytes()
    return {"path": path, "raw_sha256": hashlib.sha256(raw).hexdigest()}


def source_packet() -> dict:
    value = {
        "artifact_hash": "",
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_PRE_CANDIDATE_SOURCE_ASSIMILATION",
        "packet_id": "RH-ANA-003j-D001-JY-SOURCE-ASSIMILATION-20260812",
        "status": "FROZEN_PRE_CANDIDATE_SOURCE_ASSIMILATION",
        "atom_id": ATOM,
        "parent_atom_id": PARENT_ATOM,
        "application_base_sha": BASE_SHA,
        "object_qoi_context": {
            "object": "The exact C002 natural-order Abel boundary-plus-tail remainder after replacing Bellotti's unexposed PNT constants by a separately sourced explicit Chebyshev-psi error theorem.",
            "quantity_of_interest": "Whether an authoritative source exposes a numerical normalized PNT constant and validity threshold sufficient to define an explicit candidate-family envelope without yet selecting or evaluating a mathematical candidate.",
            "scope": "Source assimilation and pre-candidate routing only for fixed n and the exact endpoint remainder.",
            "non_goals": [
                "freeze a candidate identity",
                "select or evaluate a result branch",
                "calculate any value of M(n,epsilon)",
                "run numerical natural-order remainder tests",
                "freeze epsilon_n or a diagonal cutoff constant",
                "claim internal-prefix control, Li positivity, novelty, independent review, or RH",
            ],
        },
        "primary_source": {
            "authors": ["Daniel R. Johnston", "Andrew Yang"],
            "title": "Some explicit estimates for the error term in the prime number theorem",
            "arxiv": "2204.01980v2 [math.NT]",
            "version_date": "2022-04-20",
            "url": "https://arxiv.org/pdf/2204.01980v2",
            "pdf_sha256": JY_PDF_SHA256,
            "publication": "Journal of Mathematical Analysis and Applications 527(2) (2023), article 127460",
            "doi": "10.1016/j.jmaa.2023.127460",
            "exact_anchors": [
                "Theorem 1.1, arXiv PDF page 2",
                "equation (1.3), arXiv PDF page 2",
                "Table 1, arXiv PDF page 3, row X=log 2",
            ],
            "exact_statement": "For every real x>=2, |psi(x)-x| <= 9.39 x (log x)^1.515 exp(-0.8274 sqrt(log x)).",
            "normalized_statement": "For every real x>=2, |psi(x)-x|/x <= 9.39 (log x)^1.515 exp(-0.8274 sqrt(log x)).",
            "exposed_constants": {"amplitude": 9.39, "log_power": 1.515, "sqrt_log_decay": 0.8274, "x_threshold": 2},
        },
        "normalization_binding": {
            "application_delta": "Delta(x)=|psi(x)-x|/x",
            "application_cumulative_source": "A(x)=floor(x)-psi(x)",
            "exact_transfer": "|A(x)|<=|floor(x)-x|+|x-psi(x)|<=1+|psi(x)-x|",
            "source_bound_after_transfer": "For x>=2, |A(x)|<=1+9.39 x (log x)^1.515 exp(-0.8274 sqrt(log x)).",
            "normalization_status": "EXACTLY_COMPATIBLE_AFTER_FLOOR_ERROR_ONE",
        },
        "source_branch_classification": {
            "bellotti_v1": {
                "status": "EFFECTIVE_BUT_CONSTANT_AND_THRESHOLD_UNEXPOSED_IN_ACQUIRED_TEXT",
                "preserved_finding": "Bellotti arXiv:2508.02041v1 states a qualitative << bound for sufficiently large x but the acquired text does not bind its implied constant K_B or threshold x_B.",
                "ineffectivity_claimed": False,
            },
            "johnston_yang_v2": {
                "status": "EXPLICIT_COMPUTABLE_SOURCE_BOUND_FOUND",
                "role": "new source input for a successor pre-candidate family; not a retroactive Bellotti constant extraction",
            },
            "global_absence_claim": False,
        },
        "prospective_candidate_families": {
            "candidate_identity": None,
            "candidate_generation_allowed": False,
            "selected_result_branch": None,
            "preferred_direct_jy_family": {
                "status": "FROZEN_AS_PREFERRED_FAMILY_ONLY_NOT_A_CANDIDATE",
                "definitions": [
                    "u=log Y, a=1.515, c=0.8274",
                    "h_(n,j)=binom(n,j+1)/j!, q_(n,j)=binom(n+1,j+2)/j!",
                    "H_n(u)=sum_(j=0)^(n-1) h_(n,j)u^j",
                ],
                "integral_identity": "For j>=0 and u>=0, integral_u^infinity s^(j+a) exp(-c sqrt(s)) ds = 2 c^(-2j-2a-2) Gamma(2j+2a+2,c sqrt(u)); with a=1.515 this is 2 c^(-2j-5.03) Gamma(2j+5.03,c sqrt(u)).",
                "envelope_formula": "B_JY(n,u)=H_n(u)[exp(-u)+9.39u^1.515exp(-0.8274sqrt(u))]+sum_(j=0)^(n-1)q_(n,j)[Gamma(j+1,u)+18.78(0.8274)^(-2j-5.03)Gamma(2j+5.03,0.8274sqrt(u))].",
                "monotonicity_floor_proposal": "U_JY(n)=max(log 2,n-1,[2(n-1+1.515)/0.8274]^2). Beyond U_JY every boundary monomial is nonincreasing and every upper incomplete-gamma tail decreases.",
                "symbolic_modulus_family_only": "After a future candidate freeze and validation, one may define m as the least integer >=ceil(U_JY(n)) satisfying B_JY(n,m)<=epsilon/2 and M=exp(m). No M value is calculated here.",
            },
            "simple_domination_cross_check_family": {
                "status": "FROZEN_AS_CROSS_CHECK_FAMILY_ONLY_NOT_A_CANDIDATE",
                "chosen_constants": {"effective_amplitude": 172, "sqrt_log_decay": 0.4, "x_threshold": 2},
                "rigorous_supremum": "For D=0.8274-0.4=0.4274 and v=sqrt(u), the ratio is 9.39 v^3.03 exp(-Dv). Its unique global maximum occurs at v*=3.03/D, because d/dv log(v^3.03 exp(-Dv))=3.03/v-D. The maximum is 9.39[3.03/(eD)]^3.03=171.43357721989227<172.",
                "optimizer_guard": "The denominator is D, not 2D: 3.03 already equals 2*1.515.",
                "source_bound_after_domination": "For x>=2, |A(x)|<=1+172x exp(-0.4sqrt(log x)).",
                "envelope_formula": "B_JY_SIMPLE(n,u)=H_n(u)[exp(-u)+172exp(-0.4sqrt(u))]+sum_(j=0)^(n-1)q_(n,j)[Gamma(j+1,u)+344(0.4)^(-2j-2)Gamma(2j+2,0.4sqrt(u))].",
                "monotonicity_floor_proposal": "U_JY_SIMPLE(n)=max(log 2,n-1,[2(n-1)/0.4]^2).",
            },
        },
        "invalid_mixed_source_transfers": [
            "Calling 9.39 or 172 Bellotti's missing K_B while retaining Bellotti's exp(55A_0) factor.",
            "Combining Johnston--Yang's numerical amplitude with Bellotti's Vinogradov--Korobov decay d without a proved domination.",
            "Claiming Johnston--Yang extracts or repairs constants inside Bellotti's proof rather than supplies a separate theorem.",
            "Dropping the factor (log x)^1.515 without the explicit supremum domination witness.",
            "Using endpoint control as internal-prefix or moving-diagonal control.",
        ],
        "frozen_firewall": {
            "M_values_calculated": False,
            "numerical_remainder_tests_run": False,
            "epsilon_sequence_identity": None,
            "diagonal_cutoff_constant_identity": None,
            "diagonal_comparison_attempted": False,
            "candidate_id": None,
        },
        "authority": {
            "source_assimilation_only": True,
            "mathematical_result_generated": False,
            "strict_discovery_credit": False,
            "proof_authority": False,
            "independent_review_authority": False,
            "root_solution_authority": False,
            "software_or_governance_credit_units": 0,
        },
        "evidence_bindings": {name: raw_binding(path) for name, path in PRIOR.items()},
        "recorded_at_utc": TIME,
    }
    value["artifact_hash"] = canonical_hash(value)
    return value


def context_fiber(source: dict) -> dict:
    value = {
        "atom_id": ATOM,
        "object_context": "Source assimilation for the fixed-n C002 Abel endpoint remainder: expose a valid numerical normalized PNT bound while preserving exact natural order, floor correction, coefficient ledger, and all open downstream quantifiers.",
        "structural_coordinates": [
            "source normalized error |psi(x)-x|/x",
            "application cumulative source A(x)=floor(x)-psi(x)",
            "log variable u=log Y",
            "finite Laguerre coefficient degree n-1",
            "boundary polynomial times PNT decay",
            "tail polynomial integrated against sqrt-log exponential decay",
            "fixed-n endpoint quantifier only",
        ],
        "equivalent_formulations": [
            "direct source profile 9.39u^1.515exp(-0.8274sqrt(u))",
            "proved weaker profile 172exp(-0.4sqrt(u)) for u>=log 2",
            "explicit computable threshold family defined by a monotone incomplete-gamma envelope after future validation",
        ],
        "solved_analogues": [
            "C002 exact fixed-n natural-order Abel boundary-plus-tail identity",
            "elementary incomplete-gamma evaluation of polynomial times sqrt-exponential tails",
        ],
        "near_solved_analogues": [
            "D001 conditional envelope with placeholders K_B,x_B from Bellotti",
            "Bellotti v1 effective asymptotic profile with constants and threshold unexposed in the acquired text",
        ],
        "method_transfers": [
            {
                "source_context": "Johnston--Yang explicit Chebyshev-psi error theorem",
                "method": "transfer the normalized all-x PNT error bound through |floor(x)-psi(x)|<=1+|psi(x)-x| and then through the exact C002 Abel identity",
                "shared_structure": ["same Chebyshev psi normalization", "same real x/Y variable", "absolute error upper bound"],
                "required_assumptions": ["x>=2", "exact Johnston--Yang v2 theorem text", "natural-order C002 identity", "fixed n"],
                "disanalogies": ["different decay profile from Bellotti", "does not itself mention Laguerre weights", "does not supply moving-n or internal-prefix control"],
                "repair_question": "After a separate candidate freeze, does the direct source-bound envelope validate for the exact C002 remainder on its declared monotonicity domain?",
                "source_anchors": ["Johnston--Yang arXiv:2204.01980v2 Theorem 1.1 p.2 eq. (1.3)", "Table 1 p.3 X=log 2 row", SOURCE_PACKET],
            },
            {
                "source_context": "D001 Bellotti-parameterized conditional envelope",
                "method": "reuse the exact coefficient and Abel-tail algebra but replace the unexposed source profile as one complete unit rather than mixing constants between sources",
                "shared_structure": ["boundary plus transformed tail", "H_n/q_n finite ledgers", "upper incomplete gamma evaluation"],
                "required_assumptions": ["all source constants and thresholds exposed", "one source profile retained consistently"],
                "disanalogies": ["Johnston--Yang has a log-power prefactor", "Bellotti's d and exp(55A_0) do not belong to Johnston--Yang"],
                "repair_question": "Which fully source-consistent direct or dominated Johnston--Yang family should a later frozen candidate test?",
                "source_anchors": [PRIOR["conditional_result"], PRIOR["source_audit"]],
            },
        ],
        "explicit_disanalogies": [
            "effective-but-unexposed does not mean ineffective",
            "a separate explicit theorem does not retroactively expose Bellotti's constants",
            "source assimilation is not an evaluated Abel result",
            "a fixed-n endpoint modulus is not a moving-diagonal comparison",
            "an endpoint bound is not an internal-prefix maximal bound",
            "software checks and chronology receive zero mathematical credit",
        ],
        "source_anchors": [
            "Johnston--Yang arXiv:2204.01980v2 Theorem 1.1 p.2 eq. (1.3), Table 1 p.3",
            "DOI 10.1016/j.jmaa.2023.127460",
            f"sha256:{JY_PDF_SHA256}",
            SOURCE_PACKET,
            PRIOR["c002_result"],
            PRIOR["mathematical_lesson"],
        ],
        "analogy_scan_status": "NO_SAFE_BRIDGE_FOUND",
        "cross_domain_analogies": [],
        "analogy_scan_notes": "No new cross-domain bridge is needed for this source-assimilation atom: the viable route is same-domain SEARCH using an explicit primary PNT theorem. Existing timeout/stabilization analogies remain proposal-only and add no authority.",
        "frozen_at": "2026-08-12T14:50:01Z",
        "first_candidate_at": None,
        "packet_hash": "",
    }
    value["packet_hash"] = canonical_hash(value, "packet_hash")
    return value


def prior_failure_assimilation(source: dict, context: dict) -> dict:
    value = {
        "artifact_hash": "",
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_APPEND_ONLY_PRIOR_FAILURE_ASSIMILATION",
        "assimilation_id": "RH-ANA-003j-D001-JY-PRIOR-FAILURE-ASSIMILATION-20260812",
        "target_atom_id": ATOM,
        "target_context_hash": context["packet_hash"],
        "prior_failure_id": "RH-ANA-003j-D001-BELLOTTI-UNEXPOSED-CONSTANTS",
        "prior_artifacts": [raw_binding(PRIOR["source_audit"]), raw_binding(PRIOR["conditional_result"]), raw_binding(PRIOR["mathematical_lesson"]), raw_binding(PRIOR["failure_experience"])],
        "append_only_disposition": "PRESERVE_PRIOR_BYTES_AND_SCOPE; ADD_SEPARATE_SOURCE_ASSIMILATION; DO_NOT_REWRITE_BELLOTTI_FINDING",
        "seven_field_assimilation": {
            "attempted_mathematical_implication": "Turn the fixed-n Abel identity and an acquired PNT decay theorem into an explicit n-dependent endpoint modulus by exposing every source and Laguerre constant.",
            "exact_result_or_failure": "D001 correctly found that acquired Bellotti v1 did not expose its implied constant or sufficiently-large-x threshold. Johnston--Yang v2 now supplies a separate explicit all-x PNT bound; this removes the source-coordinate absence for a successor family but does not retroactively change Bellotti or validate the Abel envelope.",
            "supported_and_competing_mathematical_causes": "Supported prior cause: loss of two quantitative coordinates in the acquired Bellotti statement. The hypothesis that no explicit PNT source is available is now refuted in the bounded search by Johnston--Yang. Bellotti ineffectivity remains unproved, and envelope-validation or normalization failure remains a competing future cause.",
            "scope": "Bellotti acquired-text classification plus Johnston--Yang v2 source substitution for the fixed-n C002 endpoint remainder only.",
            "mathematical_falsifier": "A mismatch in the Johnston--Yang theorem/version/hash, failure of Delta/A normalization, an invalid direct tail identity, or failure of a future frozen envelope test refutes the corresponding successor route; an exact Bellotti passage exposing K_B,x_B would separately falsify only the old missing-coordinate classification.",
            "repair_or_next_discriminator": "Freeze one source-consistent Johnston--Yang envelope candidate in a later child round, then test its exact algebra and remainder implication without selecting epsilon_n or diagonal C.",
            "proof_or_source_evidence": [
                "Johnston--Yang arXiv:2204.01980v2 Theorem 1.1 p.2 eq. (1.3), Table 1 p.3",
                f"PDF sha256:{JY_PDF_SHA256}",
                SOURCE_PACKET,
                PRIOR["conditional_result"],
                PRIOR["c002_result"],
            ],
        },
        "authority": {
            "new_mathematical_result": False,
            "prior_failure_erased": False,
            "bellotti_ineffectivity_claimed": False,
            "candidate_authority": False,
            "software_credit_units": 0,
        },
        "recorded_at_utc": "2026-08-12T14:50:02Z",
    }
    value["artifact_hash"] = canonical_hash(value)
    return value


def memory_review(source: dict, context: dict, failure: dict) -> dict:
    value = {
        "target_atom_id": ATOM,
        "target_context_hash": context["packet_hash"],
        "tool_inventory_snapshot_hash": raw_binding(PRIOR["conditional_result"])["raw_sha256"],
        "failure_lattice_snapshot_hash": failure["artifact_hash"],
        "tool_query_status": "MATCHES_FOUND",
        "failure_query_status": "MATCHES_FOUND",
        "candidate_method_families": [
            "direct Johnston--Yang source profile through C002 Abel identity",
            "proved simple Johnston--Yang domination (172,0.4,2) as cross-check",
            "invalid mixed Bellotti/Johnston--Yang profile",
        ],
        "relevant_tool_ids": ["T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY", "D001-CONDITIONAL-BOUNDARY-TAIL-ALGEBRA"],
        "relevant_failure_ids": ["RH-ANA-003j-D001-BELLOTTI-UNEXPOSED-CONSTANTS"],
        "selected_tool_ids": ["T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY"],
        "tool_applicability_notes": [
            "C002 applies to fixed-n natural-order endpoint remainders only.",
            "D001 coefficient and tail algebra is reusable only after replacing the whole PNT source profile consistently.",
            "No prior tool authorizes a candidate, modulus value, moving diagonal, internal prefixes, Li positivity, or RH.",
        ],
        "failure_reuse_notes": [
            "The old Bellotti finding is retained exactly as an acquired-source limitation.",
            "Johnston--Yang is a DifferenceWitness at the source coordinate: it supplies numerical constants and x>=2 in a separate theorem.",
            "The cheapest repeat-failure test is to reject any envelope that mixes Bellotti factors with Johnston--Yang constants.",
        ],
        "unresolved_warnings": [
            "The preferred direct envelope has not been frozen as a candidate or evaluated.",
            "No M(n,epsilon) value has been calculated.",
            "No numerical remainder test has been run.",
            "No moving-diagonal, prefix, complement, Li, novelty, or RH bridge is licensed.",
        ],
        "evidence_pointers": [SOURCE_PACKET, FAILURE_ASSIMILATION, PRIOR["c002_result"], PRIOR["conditional_result"]],
        "artifact_hash": "",
        "cross_problem_coverage_receipt_hash": "",
    }
    value["artifact_hash"] = canonical_hash(value)
    return value


def expert_review(source: dict, context: dict, memory: dict) -> dict:
    value = {
        "artifact_hash": "",
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_ROLE_SEPARATED_EXPERT_SOURCE_REVIEW",
        "review_id": "RH-ANA-003j-D001-JY-EXPERT-SOURCE-REVIEW-20260812",
        "atom_id": ATOM,
        "context_hash": context["packet_hash"],
        "memory_review_hash": memory["artifact_hash"],
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT_REVIEW",
        "lenses": [
            {"role": "domain_theory", "finding": "Johnston--Yang Theorem 1.1 has the exact Chebyshev psi normalization and an all-x threshold; transfer through A incurs only the floor-error one.", "strongest_objection": "The theorem has a different decay profile from Bellotti and must replace, not splice into, that profile."},
            {"role": "analogy_method_transfer", "finding": "Same-domain SEARCH dominates analogy: direct source substitution preserves the C002 object and order.", "strongest_objection": "No source statement itself supplies the Laguerre-weighted Abel envelope."},
            {"role": "adversarial_falsification", "finding": "The simple domination maximizer uses v=3.03/0.4274; 3.03 already equals twice 1.515.", "strongest_objection": "A 2D denominator or a dropped log power would invalidate K=172."},
            {"role": "formal_methods", "finding": "The tail substitution r=c sqrt(s) gives the exact Gamma order 2j+5.03 in the direct family.", "strongest_objection": "No exact candidate, theorem receipt, formal proof, or numerical remainder validation exists in this packet."},
            {"role": "novelty_research_value", "finding": "This is source assimilation and route repair, not a novelty claim.", "strongest_objection": "Do not count Git, fixtures, hashes, tests, or rediscovery of the source theorem as mathematical progress."},
        ],
        "disagreements": ["The direct family is tighter; the simple family is easier to audit. This packet ranks direct first but freezes neither as a candidate identity."],
        "unresolved_uncertainty": ["Future exact envelope validation", "future fixed-n modulus result", "moving-diagonal comparison", "internal-prefix control"],
        "recommendation": "Freeze a separate direct Johnston--Yang candidate only after this packet is public; retain the simple family as a hostile algebraic cross-check and keep all downstream identities unfrozen.",
        "evidence_pointers": [SOURCE_PACKET, CONTEXT, MEMORY],
        "recorded_at_utc": "2026-08-12T14:50:03Z",
    }
    value["artifact_hash"] = canonical_hash(value)
    return value


def shortcut_review(source: dict, context: dict, memory: dict, expert: dict) -> dict:
    obstruction_id = "OBS-RH-ANA003J-D001-MISSING-EXPLICIT-PNT-SOURCE-COORDINATES"
    witness = {
        "witness_id": "W-RH-ANA003J-D001-JY-DIRECT-SEARCH",
        "episode_id": "EP-JOHNSTON-YANG-2204.01980V2-THM1.1",
        "target_obstruction_id": obstruction_id,
        "role_mapping": [["source normalized Chebyshev-psi error", "target Delta(x)"], ["source x>=2 threshold", "target Abel validity source floor"], ["source explicit decay profile", "target boundary and transformed-tail integrand"]],
        "shared_relations": ["absolute normalized psi error controls A(x) after an additive floor-error one"],
        "shared_constraints": ["same Chebyshev psi", "real x>=2", "absolute upper bound", "natural-order Abel identity unchanged"],
        "precondition_mapping": [["x>=2", "future envelope domain has u=log Y>=log 2"], ["psi is standard Chebyshev psi", "application psi is sum of von Mangoldt through x"]],
        "unmatched_source_preconditions": [],
        "disanalogies": ["Johnston--Yang uses a sqrt-log exponential with log-power prefactor rather than Bellotti's Vinogradov--Korobov profile", "source theorem does not mention Laguerre weights or moving n"],
        "target_validation_obligations": ["freeze exact direct envelope as a later candidate", "verify tail identity and monotonicity floor", "test exact C002 remainder implication", "preserve endpoint-only and fixed-n scope"],
        "evidence_pointers": [SOURCE_PACKET, f"sha256:{JY_PDF_SHA256}"],
        "artifact_hash": "",
    }
    witness["artifact_hash"] = canonical_hash(witness)
    value = {
        "review_id": "RH-ANA-003j-D001-JY-OBSTRUCTION-REVIEW-20260812",
        "target_atom_id": ATOM,
        "target_context_hash": context["packet_hash"],
        "research_memory_review_hash": memory["artifact_hash"],
        "episode_memory_snapshot_hash": source["artifact_hash"],
        "obstruction": {
            "obstruction_id": obstruction_id,
            "domain": "analytic number theory / explicit PNT error / Abel summation",
            "roles": ["normalized PNT error source", "explicit source constant", "source validity threshold", "C002 fixed-n Abel remainder"],
            "relations": ["PNT error controls A(x)", "A(x) enters boundary and tail", "unexposed constants block source-complete instantiation"],
            "constraints": ["exact source/version/hash", "same psi normalization", "natural order", "fixed n", "no candidate or result in this round"],
            "failure_mechanisms": ["treating << as an exposed constant", "mixing constants from different source profiles", "dropping the log-power factor without domination"],
            "invariants_to_preserve": ["Bellotti finding", "D001 negative history", "C002 object/order", "endpoint-only scope", "OPEN root"],
            "desired_transition": ["locate a primary explicit PNT theorem whose numerical bound can seed a later source-consistent Abel-envelope candidate"],
            "forbidden_losses": ["ineffectivity overclaim", "mixed-source normalization", "candidate backfill", "software credit", "downstream diagonal or RH promotion"],
        },
        "direct_search_status": "MATCHES_FOUND",
        "jump_search_status": "NOT_RUN",
        "glue_search_status": "NOT_RUN",
        "selected_mode": "SEARCH",
        "direct_candidate_episode_ids": ["EP-JOHNSTON-YANG-2204.01980V2-THM1.1"],
        "direct_mapping_witnesses": [witness],
        "jump_mapping_witnesses": [],
        "glue_witness": None,
        "selected_episode_ids": ["EP-JOHNSTON-YANG-2204.01980V2-THM1.1"],
        "exhaustion_witness": None,
        "missing_transformation_specification": None,
        "unresolved_warnings": ["SEARCH licenses source assimilation only; target validation obligations remain", "preferred and cross-check families are not candidate identities", "no result branch or modulus value exists"],
        "evidence_pointers": [SOURCE_PACKET, CONTEXT, MEMORY, EXPERT],
        "artifact_hash": "",
    }
    value["artifact_hash"] = canonical_hash(value)
    return value


def trace(source: dict, context: dict, failure: dict, memory: dict, expert: dict, shortcut: dict) -> dict:
    specs = [
        ("ATOMIZED", "Freeze the source-coordinate child atom without reopening the moving diagonal.", [SOURCE_PACKET]),
        ("CONTEXT_FROZEN", "Bind exact normalization, source profile, equivalent direct/dominated formulations, and downstream scope exclusions.", [CONTEXT]),
        ("ANALOGY_SCAN", "Record NO_SAFE_BRIDGE_FOUND because same-domain explicit source SEARCH is available.", [CONTEXT]),
        ("METHOD_TRANSFER_REVIEW", "Map Johnston--Yang's normalized psi theorem into A(x), leaving Abel-envelope validation prospective.", [SOURCE_PACKET, CONTEXT]),
        ("EXPERT_CONTEXT_REVIEW", "Preserve role-separated objections and source-mixing falsifiers.", [EXPERT]),
        ("EXPERIENCE_MEMORY_REVIEW", "Assimilate the prior seven-field D001 failure append-only and query the C002 tool surface.", [FAILURE_ASSIMILATION, MEMORY]),
        ("OBSTRUCTION_TRANSFORMATION_REVIEW", "Select SEARCH for a same-domain explicit PNT source with a complete mapping witness.", [SHORTCUT]),
        ("NEXT_STEP_PROPOSED", "In a later child round, freeze the direct Johnston--Yang envelope as a candidate and the simple family as cross-check; do not evaluate now.", [SOURCE_PACKET, EXPERT, SHORTCUT]),
    ]
    entries=[]
    previous=""
    for index,(kind,action,pointers) in enumerate(specs,1):
        event={
            "event_id": f"RH-ANA003J-D001-JY-SA001-E{index:02d}",
            "atom_id": ATOM,
            "event_type": kind,
            "timestamp": f"2026-08-12T14:50:{10+index:02d}Z",
            "state_summary": "Johnston--Yang v2 supplies an explicit same-normalization PNT bound, while the D001 Bellotti limitation and all target-validation/downstream residuals remain preserved.",
            "action_summary": action,
            "evidence_pointers": pointers,
            "alternatives_considered": ["extract Bellotti constants line by line", "mix Johnston--Yang amplitude with Bellotti decay", "freeze direct Johnston--Yang family later", "retain CANNOT_CHECK"],
            "decision_rationale": "Same-domain explicit source evidence resolves the source-coordinate search at proposal level without authorizing a candidate or mathematical result.",
            "outputs": ["PRE_CANDIDATE_SOURCE_ASSIMILATION_ONLY", "NO_CANDIDATE_IDENTITY", "NO_M_VALUES", "NO_NUMERICAL_REMAINDER_TEST", "SOFTWARE_CREDIT_ZERO"],
            "uncertainties": ["future exact envelope validation", "moving diagonal remains unfrozen", "same-context review is not independent"],
            "residuals": ["candidate freeze pending", "fixed-n source-complete result pending", "diagonal/prefix/Li/RH obligations open"],
            "next_steps": ["publicly freeze a separate candidate/evaluator packet", "then validate exact algebra and remainder implication", "do not select epsilon_n or diagonal C yet"],
            "artifact_hash": "",
            "previous_event_hash": previous,
        }
        event["artifact_hash"] = canonical_hash(event)
        previous=event["artifact_hash"]
        entries.append(event)
    return {"trace_id": "RH-ANA003J-D001-JY-SA001-PRE-CANDIDATE-TRACE-20260812", "entries": entries}


def build_all() -> dict[str,dict]:
    source=source_packet(); context=context_fiber(source); failure=prior_failure_assimilation(source,context)
    memory=memory_review(source,context,failure); expert=expert_review(source,context,memory)
    shortcut=shortcut_review(source,context,memory,expert); research_trace=trace(source,context,failure,memory,expert,shortcut)
    return {SOURCE_PACKET:source, CONTEXT:context, FAILURE_ASSIMILATION:failure, MEMORY:memory, EXPERT:expert, SHORTCUT:shortcut, TRACE:research_trace}


def main() -> None:
    for relative,value in build_all().items():
        path=ROOT/relative; path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(value,indent=2,sort_keys=True)+"\n",encoding="utf-8")

if __name__ == "__main__":
    main()
