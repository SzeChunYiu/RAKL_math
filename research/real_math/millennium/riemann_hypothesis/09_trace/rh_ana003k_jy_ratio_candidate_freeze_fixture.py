#!/usr/bin/env python3
"""Build the inert RH ANA003k JY floor-ratio candidate/falsifier freeze.

No limit is evaluated and no candidate branch is selected here.  The evaluator
identity is a symbolic proof contract only, and the authorization remains inert
until these exact bytes are merged into active main.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
BASE_SHA = "47fcc8f71f5d4801b3c337d50c3b17bb6b8a648d"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
ATOM = "RH-ANA-003k-JY-MOVING-DIAGONAL"
CANDIDATE_ID = "RH-ANA-003k-JY-C001-FLOOR-RATIO-ASYMPTOTIC"
BASE = "research/real_math/millennium/riemann_hypothesis"
PATHS = {
    "candidate": f"{BASE}/04_candidates/RH_ANA_003k_JY_C001_FLOOR_RATIO_CANDIDATE_FREEZE_20260812.json",
    "falsifier": f"{BASE}/05_oracles/RH_ANA_003k_JY_C001_FLOOR_RATIO_FALSIFIER_FREEZE_20260812.json",
    "evaluator": f"{BASE}/05_oracles/RH_ANA_003k_JY_C001_FLOOR_RATIO_EVALUATOR_IDENTITY_20260812.json",
    "lesson": f"{BASE}/07_memory/RH_ANA_003k_JY_C001_FLOOR_RATIO_MATHEMATICAL_LESSON_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003k_JY_C001_FLOOR_RATIO_CANDIDATE_FREEZE_TRACE_20260812.json",
    "authorization": f"{BASE}/09_trace/RH_ANA_003k_JY_C001_FLOOR_RATIO_EVALUATION_AUTHORIZATION_20260812.json",
}
EVIDENCE = {
    "pre_candidate_discriminator": (f"{BASE}/08_reviews/RH_ANA_003k_JY_MOVING_DIAGONAL_SYMBOLIC_DISCRIMINATOR_FREEZE_20260812.json", "bbc6c3aea57d17aadf32182991a793698b0cdb59116aedaeea8ee3744dd3b8f2"),
    "pre_candidate_gate": (f"{BASE}/09_trace/RH_ANA_003k_JY_MOVING_DIAGONAL_PRE_CANDIDATE_GATE_20260812.json", "796c7e2633f371ba67fa3b4e091639a925cbb4cdb8a61c2d913bf73c8f95bb98"),
    "pre_candidate_trace": (f"{BASE}/09_trace/RH_ANA_003k_JY_MOVING_DIAGONAL_PRE_CANDIDATE_TRACE_20260812.json", "4201a555046cc75fe582c1d6c1662a0cfad1b6477b763d58c9b5e15730da6d7c"),
    "jy_result": (f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_PUBLIC_VALIDATION_RESULT_20260812.json", "ee5cb68a30a234b7bf93f6988577bb22d59d41dc82e3678845c6d3dadac3a867"),
    "jy_lesson": (f"{BASE}/07_memory/RH_ANA_003j_D001_JY_C001_MATHEMATICAL_LESSON_20260812.json", "606f33868f5b485eb9f383e5c1cdd8061970d7b0dd58908939f291da04fc1f90"),
}
PREVIOUS_EVENT_HASH = "sha256:4319299f2a9c083c293e98be78cb5987bbb704d746e75acb7dd6904c97ea3470"


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def hash_with_blank(value: dict, field: str) -> str:
    subject = copy.deepcopy(value)
    subject[field] = ""
    return "sha256:" + hashlib.sha256(canonical(subject)).hexdigest()


def seal(value: dict) -> dict:
    value["artifact_hash"] = ""
    value["artifact_hash"] = hash_with_blank(value, "artifact_hash")
    return value


def raw_binding(name: str) -> dict:
    path, expected = EVIDENCE[name]
    observed = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
    if observed != expected:
        raise RuntimeError(f"{name}: {observed} != {expected}")
    return {"path": path, "raw_sha256": "sha256:" + observed}


def candidate_core() -> dict:
    return {
        "candidate_id": CANDIDATE_ID,
        "domain": "integers n>=1 and one arbitrary but fixed real C>0",
        "definitions": {
            "F_n": "[2(n+0.515)/0.8274]^2",
            "U_JY_n": "max(log 2,n-1,F_n)",
            "u_n_C": "C n^(5/3) log^2(n+e)",
            "Y_n_C": "exp(u_n(C))",
            "rho_C_n": "u_n(C)/F_n=(C(0.8274)^2/4) [n^(5/3)log^2(n+e)/(n+0.515)^2]",
        },
        "theorem_statement_to_evaluate_later": "For every fixed C>0, lim_(n->infinity) rho_C(n)=0. Consequently there exists N_C such that for every integer n>=N_C, u_n(C)<F_n<=U_JY(n)<=ceil(U_JY(n))<=tilde_m_JY(n,epsilon) for every epsilon>0. Hence Y_n(C)<tilde_M_JY(n,epsilon) for every epsilon>0 under the separately proved sufficient strict-search family.",
        "exact_scoped_interpretation_if_proved": "For every fixed C>0, the current Johnston--Yang sufficient certificate is eventually incompatible with the diagonal log Y_n=C n^(5/3)log^2(n+e), independently of epsilon. This is only failure of that sufficient certificate on that diagonal.",
        "non_implications": [
            "not failure of the actual natural-order remainder below U_JY",
            "not a lower bound on every possible sufficient modulus",
            "not internal-prefix control or failure thereof",
            "not Li coefficient negativity or positivity",
            "not evidence for or against the Riemann hypothesis",
        ],
    }


def candidate_document() -> dict:
    core = candidate_core()
    core_hash = "sha256:" + hashlib.sha256(canonical(core)).hexdigest()
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003K_JY_C001_FLOOR_RATIO_CANDIDATE_FREEZE",
        "atom_id": ATOM,
        **core,
        "candidate_identity": {"canonical_core_sha256": core_hash, "identity_scope": "candidate_core() exact canonical JSON"},
        "proof_obligations": [
            {"id": "PO1-RATIO-ALGEBRA", "obligation": "Derive rho_C(n) exactly from u_n(C)/F_n without dropping 0.515, changing 0.8274, or treating C as n-dependent."},
            {"id": "PO2-ELEMENTARY-LIMIT", "obligation": "Prove log^2(n+e)/n^(1/3) tends to 0 by an exact standard theorem or explicit epsilon argument; finite numerical fitting is insufficient."},
            {"id": "PO3-FIXED-C-QUANTIFIER", "obligation": "Keep the order forall fixed C>0, exists N_C, forall n>=N_C; do not claim one N uniform over unbounded C."},
            {"id": "PO4-FLOOR-CHAIN", "obligation": "From rho_C(n)<1 derive u_n(C)<F_n<=U_JY(n)<=ceil(U_JY(n)), with the correct ceiling direction."},
            {"id": "PO5-SUFFICIENT-SEARCH-BOUND", "obligation": "Use only the proved construction tilde_m_JY(n,epsilon)>=ceil(U_JY(n)) for every epsilon>0."},
            {"id": "PO6-EXPONENTIATION", "obligation": "Use strict monotonicity of exp to pass from u_n(C)<tilde_m_JY to Y_n(C)<tilde_M_JY."},
            {"id": "PO7-SCOPE", "obligation": "Classify only current-sufficient-certificate incompatibility and reject every actual-remainder, Li, or RH inference."},
        ],
        "chronology": {
            "application_base_sha": BASE_SHA,
            "framework_pin_sha": FRAMEWORK_SHA,
            "pre_candidate_packet_merged_before_candidate": True,
            "pre_candidate_merge_sha": BASE_SHA,
            "candidate_frozen_before_evaluation": True,
            "limit_proof_executed": False,
            "evaluator_executed": False,
            "result_accessed": False,
        },
        "evaluation_firewall": {
            "proof_attempt_run": False,
            "symbolic_limit_classified": False,
            "numerical_ratio_values_calculated": False,
            "eventual_cutoff_N_C_calculated": False,
            "branch_selected": False,
            "result_recorded": False,
        },
        "frozen_constant_contract": {"C": "arbitrary fixed real C>0", "C_may_depend_on_n": False, "numeric_C_selected": False, "epsilon_sequence_needed_for_floor_result": False},
        "evidence_bindings": {name: raw_binding(name) for name in EVIDENCE},
        "status": "FROZEN_UNEVALUATED_ELEMENTARY_ASYMPTOTIC_CANDIDATE",
        "authority": {"candidate_proposal_only": True, "mathematical_result": False, "proof": False, "formal_proof": False, "independent_review": False, "li_or_rh": False, "root_state": "OPEN_NO_SOLUTION_CERTIFICATE", "software_credit_units": 0},
    })


def falsifier_document(candidate: dict) -> dict:
    worlds = [
        ("CONTROL-EXACT-FIXED-C", "Exact definitions, fixed C>0, and all seven obligations", "PASS_CANDIDATE_THEOREM"),
        ("FAIL-C-DEPENDS-ON-N", "Replace fixed C by C_n=n^(1/3)/log^2(n+e)", "FAIL_QUANTIFIER_CONTRACT"),
        ("FAIL-WRONG-LOG-POWER-LIMIT", "Assert log^2(n+e)/n^(1/3) has a positive or infinite limit", "FAIL_ELEMENTARY_LIMIT"),
        ("FAIL-DROP-0515", "Replace n+0.515 by n without an exact comparison argument", "FAIL_RATIO_IDENTITY"),
        ("FAIL-CEILING-DIRECTION", "Infer ceil(U_JY)<=U_JY", "FAIL_FLOOR_CHAIN"),
        ("FAIL-CERTIFICATE-TO-OBJECT", "Infer actual remainder failure from tilde_M_JY>Y_n", "FAIL_SCOPE_OVERREACH"),
        ("FAIL-ENDPOINT-TO-PREFIX", "Infer internal-prefix or Li control from endpoint certificate comparison", "FAIL_SCOPE_OVERREACH"),
        ("FAIL-RH-INFERENCE", "Infer RH truth or falsity", "FAIL_SCOPE_OVERREACH"),
        ("CANNOT-CHECK-SOURCE", "Mismatch the bound tilde_m_JY>=ceil(U_JY) source/result bytes", "CANNOT_CHECK"),
        ("CANNOT-CHECK-PROOF", "Supply only finite numerical ratios without a symbolic limit proof", "CANNOT_CHECK"),
    ]
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003K_JY_C001_FLOOR_RATIO_FALSIFIER_FREEZE",
        "falsifier_id": "RH-ANA-003k-JY-C001-FLOOR-RATIO-FALSIFIER-20260812",
        "candidate_id": CANDIDATE_ID,
        "candidate_artifact_hash": candidate["artifact_hash"],
        "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
        "classification_vocabulary": ["PASS_CANDIDATE_THEOREM", "FAIL_RATIO_IDENTITY", "FAIL_ELEMENTARY_LIMIT", "FAIL_QUANTIFIER_CONTRACT", "FAIL_FLOOR_CHAIN", "FAIL_SCOPE_OVERREACH", "CANNOT_CHECK"],
        "worlds": [{"world_id": wid, "input_condition_or_mutation": cond, "expected_future_classification": label, "materialized": False} for wid,cond,label in worlds],
        "decisive_refuters": ["failure of rho_C algebra", "counterexample to the fixed-C limit", "incorrect quantifier order", "incorrect max/ceiling chain", "use of an unproved lower bound for tilde_m_JY", "any inference beyond current sufficient-certificate incompatibility"],
        "future_evaluator_contract": {"implementation_frozen": False, "execution_authorized_this_round": False, "must_check_all_candidate_raw_bindings": True, "must_check_each_proof_obligation_separately": True, "must_fail_closed_on_missing_symbolic_proof": True, "must_not_treat_expected_labels_as_results": True},
        "result_state": "NO_FALSIFIER_RUN_NO_RESULT_CLASSIFICATION",
        "status": "FROZEN_EXPECTED_WORLDS_NOT_MATERIALIZED_OR_EXECUTED",
        "authority": {"mathematical_result": False, "proof": False, "expected_labels_are_oracle_inputs_only": True, "independent_review": False, "li_or_rh": False},
    })


def evaluator_document(candidate: dict, falsifier: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003K_JY_C001_FLOOR_RATIO_EVALUATOR_IDENTITY_FREEZE",
        "evaluator_id": "RH-ANA-003k-JY-C001-FLOOR-RATIO-SYMBOLIC-EVALUATOR-v1",
        "candidate_id": CANDIDATE_ID,
        "exact_bindings": {"candidate_artifact_hash": candidate["artifact_hash"], "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"], "falsifier_artifact_hash": falsifier["artifact_hash"]},
        "evaluator_identity": {
            "kind": "INERT_SYMBOLIC_PROOF_CONTRACT_NO_IMPLEMENTATION",
            "future_entrypoint": "evaluate_rh_ana003k_jy_c001(candidate, falsifier, source_bindings)",
            "future_implementation_path": f"{BASE}/05_oracles/rh_ana003k_jy_c001_floor_ratio_evaluator.py",
            "required_checks_in_order": ["raw identity bindings", "PO1 ratio algebra", "PO2 elementary limit", "PO3 fixed-C quantifiers", "PO4 max/ceiling chain", "PO5 proved sufficient-search lower bound", "PO6 exponentiation", "PO7 scope firewall", "all planted worlds"],
            "allowed_outputs": ["PASS_CANDIDATE_THEOREM", "FAIL_RATIO_IDENTITY", "FAIL_ELEMENTARY_LIMIT", "FAIL_QUANTIFIER_CONTRACT", "FAIL_FLOOR_CHAIN", "FAIL_SCOPE_OVERREACH", "CANNOT_CHECK"],
            "proof_authority_requirement": "Exact written derivation or proof-producing formal artifact; computation alone is corroboration only.",
        },
        "current_round_firewall": {"implementation_exists": False, "evaluator_imported": False, "evaluator_executed": False, "worlds_materialized": False, "result_classified": False},
        "chronology": {"base_sha": BASE_SHA, "candidate_and_falsifier_frozen_in_same_inert_packet": True, "execution_requires_later_active_main activation": True, "result_accessed": False},
        "status": "IDENTITY_FROZEN_IMPLEMENTATION_AND_EXECUTION_FORBIDDEN_THIS_ROUND",
        "authority": {"evaluator_identity_only": True, "mathematical_result": False, "proof": False, "independent_review": False, "software_credit_units": 0},
    })


def lesson_document(candidate: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003K_JY_C001_SEVEN_FIELD_MATHEMATICAL_LESSON_FREEZE",
        "unit_id": "MATH-RH-ANA003K-JY-C001-FLOOR-RATIO",
        "candidate_id": CANDIDATE_ID,
        "candidate_hash": candidate["artifact_hash"],
        "attempted_implication": "Test whether the proved Johnston--Yang fixed-n sufficient certificate can cover the inherited moving diagonal log Y_n=C n^(5/3)log^2(n+e) for an arbitrary fixed C>0.",
        "exact_result_or_failure": "No result yet: the unevaluated candidate states that the diagonal-to-floor ratio tends to zero and would force eventual failure of this sufficient certificate, not failure of the actual remainder.",
        "supported_and_competing_causes": ["Supported input: tilde_m_JY starts at ceil(U_JY) and U_JY contains the quadratic F_n term.", "Candidate cause: n^(5/3)log^2 n is asymptotically smaller than n^2 for fixed C.", "Competing cause for object behavior: U_JY is a proof-domain floor and may be removable by a sharper below-floor envelope.", "Competing source of larger thresholds: epsilon-dependent excess can only strengthen certificate incompatibility once the floor obstruction is proved."],
        "scope": "Asymptotic compatibility of one proved sufficient endpoint certificate with the family log Y_n=C n^(5/3)log^2(n+e), separately for every fixed C>0.",
        "mathematical_falsifier": "Refute the exact ratio identity or fixed-C limit, the max/ceiling implication, or the proved tilde_m lower bound; also reject the candidate's interpretation if it is used to infer actual remainder behavior, internal-prefix control, Li signs, or RH.",
        "mathematical_repair": "If the candidate passes, search for a sharper envelope valid below the quadratic monotonicity floor or prospectively study a larger diagonal; if it fails, isolate the exact algebraic, asymptotic, or quantifier error before selecting a successor.",
        "proof_source_evidence": [EVIDENCE["pre_candidate_discriminator"][0], EVIDENCE["jy_result"][0], "Future symbolic derivation must prove log^2(n+e)/n^(1/3)->0 and the exact inequality chain; no numerical receipt can replace it."],
        "nonmathematical_governance_note": "Git, PR, CI, schemas, hashes, chronology, and repository activity receive zero mathematical credit.",
        "authority": {"lesson_is_pre_result": True, "mathematical_result": False, "independent_review": False, "root_state": "OPEN_NO_SOLUTION_CERTIFICATE"},
    })


def trace_document(candidate: dict, falsifier: dict, evaluator: dict, lesson: dict) -> dict:
    event = {
        "event_id": "RH-ANA003K-JY-C001-E09",
        "atom_id": ATOM,
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": "2026-08-12T17:10:00Z",
        "state_summary": "The pre-candidate packet is public; the exact fixed-C floor-ratio theorem, proof obligations, hostile worlds, and inert evaluator identity are now frozen without evaluation.",
        "action_summary": "Freeze the elementary asymptotic candidate and certificate-only consequence before any proof execution or world materialization.",
        "evidence_pointers": [PATHS["candidate"], PATHS["falsifier"], PATHS["evaluator"], PATHS["lesson"]],
        "alternatives_considered": ["evaluate the limit immediately", "analyze epsilon-dependent excess", "select a numerical C", "freeze the exact fixed-C floor candidate first"],
        "decision_rationale": "The mandatory quadratic floor is independent of epsilon and the already-frozen cheap discriminator identifies it as the least-cost next mathematical question; exact identities must precede result access.",
        "outputs": [candidate["artifact_hash"], falsifier["artifact_hash"], evaluator["artifact_hash"], "FROZEN_UNEVALUATED", "ZERO_MATHEMATICAL_RESULT_CREDIT"],
        "uncertainties": ["symbolic limit proof not executed", "actual remainder below U_JY unknown", "same-context work is not independent review"],
        "residuals": ["future evaluator implementation and proof execution", "sharper below-floor envelope question", "internal prefixes, Li signs, and RH remain open"],
        "next_steps": ["merge this inert identity packet", "in a later round activate exact evaluator bytes", "preserve any result at certificate-only scope"],
        "previous_event_hash": PREVIOUS_EVENT_HASH,
        "artifact_hash": "",
    }
    event["artifact_hash"] = hash_with_blank(event, "artifact_hash")
    return {"trace_id": "RH-ANA003K-JY-C001-CANDIDATE-FREEZE-TRACE-20260812", "parent_trace_raw_sha256": raw_binding("pre_candidate_trace")["raw_sha256"], "entries": [event]}


def authorization_document(candidate: dict, falsifier: dict, evaluator: dict, trace: dict) -> dict:
    bindings = {}
    for name, doc in (("candidate",candidate),("falsifier",falsifier),("evaluator",evaluator),("trace",trace)):
        path=PATHS[name]
        raw=hashlib.sha256((json.dumps(doc,indent=2,sort_keys=True)+"\n").encode()).hexdigest()
        bindings[name]={"path":path,"artifact_hash":doc["artifact_hash"] if "artifact_hash" in doc else doc["entries"][-1]["artifact_hash"],"raw_sha256":"sha256:"+raw}
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003K_JY_C001_POSTMERGE_EVALUATION_AUTHORIZATION",
        "authorization_id": "RH-ANA-003k-JY-C001-FLOOR-RATIO-EVALUATION-AUTHORIZATION-20260812",
        "candidate_id": CANDIDATE_ID,
        "exact_identity_bindings": bindings,
        "chronology": {"authorization_base_sha": BASE_SHA, "candidate_freeze_present_on_active_main": False, "authorization_present_on_active_main": False, "evaluator_implemented_or_executed": False, "world_materialized": False, "result_accessed": False},
        "current_round": {"allowed_action": "COMMIT_REVIEW_AND_MERGE_INERT_PACKET_ONLY", "implementation_authorized": False, "execution_authorized": False, "result_classification_authorized": False},
        "post_merge_activation": {"condition": "A later round must verify these exact raw bytes on active main and bind the active-main merge SHA.", "then_authorized": ["implement exactly the frozen symbolic evaluator", "materialize and run every frozen world", "evaluate the exact seven proof obligations", "emit one machine-readable result receipt without changing identities"], "candidate_or_falsifier_mutation_allowed": False, "scope_expansion_allowed": False},
        "forbidden": ["execute or classify the limit in this round", "materialize planted worlds in this round", "select numerical C or outcome-dependent C_n", "replace symbolic proof by numerical fitting", "infer actual remainder failure, internal-prefix behavior, Li signs, or RH"],
        "result_state": "UNEVALUATED",
        "status": "FROZEN_INERT_UNTIL_MERGED_AND_SEPARATELY_ACTIVATED",
        "authority": {"operational_authorization_only": True, "mathematical_result": False, "proof": False, "independent_review": False, "root_state": "OPEN_NO_SOLUTION_CERTIFICATE", "software_credit_units": 0},
    })


def build_all() -> dict[str,dict]:
    candidate=candidate_document()
    falsifier=falsifier_document(candidate)
    evaluator=evaluator_document(candidate,falsifier)
    lesson=lesson_document(candidate)
    trace=trace_document(candidate,falsifier,evaluator,lesson)
    authorization=authorization_document(candidate,falsifier,evaluator,trace)
    return {PATHS["candidate"]:candidate,PATHS["falsifier"]:falsifier,PATHS["evaluator"]:evaluator,PATHS["lesson"]:lesson,PATHS["trace"]:trace,PATHS["authorization"]:authorization}


def main() -> None:
    for relative,value in build_all().items():
        path=ROOT/relative
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(value,indent=2,sort_keys=True)+"\n")

if __name__ == "__main__":
    main()
