#!/usr/bin/env python3
"""Build the fresh post-activation RH-ANA-003k floor-ratio result packet."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = "research/real_math/millennium/riemann_hypothesis"
CANDIDATE_ID = "RH-ANA-003k-JY-C001-FLOOR-RATIO-ASYMPTOTIC"
CANDIDATE_HASH = "sha256:f99b6553969d2e035e87bc7c62f5ad7f163c69e09ce55278d3e34329028ba1bf"
FALSIFIER_HASH = "sha256:df91c4f87bd590da80557e3d00057eab029fb07d28732e02bb21d023a26d5daa"
ACTIVATION_HASH = "sha256:e15340e1af6a8afefc784a3d37449819b49809fb21e757055954596308ce4660"
ACTIVATION_MERGE = "c2479b8c258146be582306d6d75b8af6b3149a81"
ACTIVATION_HEAD = "e6bcb8ac5c01a5d2075b1be9349b30cf413a820a"
HAND_PROOF_HASH = "sha256:806dc96800a6f793bd6cbab5aaad24c6d2a23bffed13f447f00430c4f5e15af8"
HAND_PROOF_RAW = "sha256:7b8487fa68d7e3067841a52c8b88dc2fed698204ca616055207575d5bc7ef0c3"
HAND_PROOF_COMMIT = "2cbc8c07c28707b90134445ca44a6aadd183b9ff"
EXECUTED_AT = "2026-08-12T17:50:00Z"
RECORDED_AT = "2026-08-12T17:51:00Z"
REVIEWED_AT = "2026-08-12T17:52:00Z"
RAW_EXECUTION_OUTPUT = "sha256:dd1aa15001f7b7f7c93be9924170207b80d3b286e315df54bad98772dc594512"
FRAMEWORK_PIN = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
FRAMEWORK_MAIN = "b680e50a82c6753cf982864cc5b2af172c6f19c6"
PREVIOUS_EVENT_HASH = "sha256:2dc0eb8969c1b5e39e53796b30a208d4c09f241bced53ec5e36dc2bfa05d662e"

PATHS = {
    "candidate": f"{BASE}/04_candidates/RH_ANA_003k_JY_C001_FLOOR_RATIO_CANDIDATE_FREEZE_20260812.json",
    "falsifier": f"{BASE}/05_oracles/RH_ANA_003k_JY_C001_FLOOR_RATIO_FALSIFIER_FREEZE_20260812.json",
    "activation": f"{BASE}/09_trace/RH_ANA_003k_JY_C001_FLOOR_RATIO_EXECUTION_ACTIVATION_20260812.json",
    "hand_proof": f"{BASE}/05_oracles/RH_ANA_003k_JY_C001_FLOOR_RATIO_HAND_PROOF_20260812T174900Z.json",
    "evaluator": f"{BASE}/05_oracles/rh_ana003k_jy_c001_floor_ratio_evaluator.py",
    "result": f"{BASE}/05_oracles/RH_ANA_003k_JY_C001_POST_ACTIVATION_RESULT_20260812T175100Z.json",
    "lesson": f"{BASE}/07_memory/RH_ANA_003k_JY_C001_POST_ACTIVATION_MATHEMATICAL_LESSON_20260812T175100Z.json",
    "review": f"{BASE}/08_reviews/RH_ANA_003k_JY_C001_POST_ACTIVATION_RESULT_REVIEW_20260812T175200Z.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003k_JY_C001_POST_ACTIVATION_RESULT_TRACE_20260812T175200Z.json",
    "framework_revalidation": f"{BASE}/09_trace/RH_ANA_003k_JY_C001_POST_ACTIVATION_FRAMEWORK_REVALIDATION_20260812T175100Z.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def seal(value: dict) -> dict:
    value = dict(value)
    value.pop("artifact_hash", None)
    value["artifact_hash"] = canonical_hash(value)
    return value


def raw_sha256(path: str) -> str:
    return "sha256:" + hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load_hand_proof() -> dict:
    proof = json.loads((ROOT / PATHS["hand_proof"]).read_text())
    if proof["artifact_hash"] != HAND_PROOF_HASH or raw_sha256(PATHS["hand_proof"]) != HAND_PROOF_RAW:
        raise RuntimeError("hand-proof identity mismatch")
    return proof


def evaluator_module():
    path = ROOT / PATHS["evaluator"]
    spec = importlib.util.spec_from_file_location("rh_ana003k_jy_c001_fresh_result_evaluator", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def machine_receipt(proof: dict) -> dict:
    obligations = {
        key: verdict == "PASS_EXACT_HAND_PROOF"
        for key, verdict in proof["proof_obligation_verdicts"].items()
    }
    output = evaluator_module().materialize_and_run_frozen_worlds(ROOT, obligations)
    return {
        **output,
        "executed_at_utc": EXECUTED_AT,
        "hand_proof_artifact_hash": HAND_PROOF_HASH,
        "hand_proof_commit": HAND_PROOF_COMMIT,
        "raw_execution_output_sha256": RAW_EXECUTION_OUTPUT,
        "corroboration_only_not_proof": True,
    }


def result_document() -> dict:
    proof = load_hand_proof()
    machine = machine_receipt(proof)
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003K_JY_C001_POST_ACTIVATION_RESULT_RECEIPT",
        "result_id": "RH-ANA-003k-JY-C001-POST-ACTIVATION-RESULT-20260812T175100Z",
        "candidate_id": CANDIDATE_ID,
        "candidate_artifact_hash": CANDIDATE_HASH,
        "falsifier_artifact_hash": FALSIFIER_HASH,
        "status": "PASS_FIXED_C_FLOOR_RATIO__CURRENT_SUFFICIENT_CERTIFICATE_INCOMPATIBILITY_ONLY",
        "identity_lineage": {
            "valid_final_result_identity": "RH-ANA-003k-JY-C001-POST-ACTIVATION-RESULT-20260812T175100Z",
            "valid_final_result_identity_count": 1,
            "hand_proof_record_is_input_not_competing_final_result": True,
            "earlier_uncommitted_draft_status": "INVALID_CHRONOLOGY_NEVER_COMMITTED_OR_PUSHED_NOT_EVIDENCE",
            "earlier_draft_content_used_as_evidence": False,
            "earlier_draft_identity_promoted_or_reused": False,
        },
        "chronology": {
            "result_round_base_sha": ACTIVATION_MERGE,
            "activation_head_sha": ACTIVATION_HEAD,
            "activation_public_merge_sha": ACTIVATION_MERGE,
            "activation_artifact_hash": ACTIVATION_HASH,
            "activation_public_before_hand_proof": True,
            "hand_proof_commit": HAND_PROOF_COMMIT,
            "hand_proof_commit_precedes_record_checker_execution": True,
            "candidate_or_falsifier_mutated": False,
            "record_checker_executed_at_utc": EXECUTED_AT,
            "result_recorded_at_utc": RECORDED_AT,
        },
        "input_bindings": {
            "candidate_raw_sha256": raw_sha256(PATHS["candidate"]),
            "falsifier_raw_sha256": raw_sha256(PATHS["falsifier"]),
            "activation_raw_sha256": raw_sha256(PATHS["activation"]),
            "hand_proof_raw_sha256": HAND_PROOF_RAW,
            "evaluator_raw_sha256": raw_sha256(PATHS["evaluator"]),
        },
        "hand_proof": {
            "path": PATHS["hand_proof"],
            "artifact_hash": HAND_PROOF_HASH,
            "obligation_verdicts": proof["proof_obligation_verdicts"],
            "proof_is_primary_authority_for_scoped_result": True,
        },
        "exact_mathematical_result": {
            "ratio_identity": "rho_C(n)=[C(0.8274)^2/4][n^2/(n+0.515)^2][log^2(n+e)/n^(1/3)].",
            "asymptotic": "For every fixed real C>0, rho_C(n)=O_C(log^2(n)/n^(1/3)) and rho_C(n)->0.",
            "quantifiers": "forall fixed C>0, exists N_C, forall integers n>=N_C; no N uniform over unbounded C",
            "certificate_chain": "For every epsilon>0 in the proved strict-search family, u_n(C)<F_n<=U_JY(n)<=ceil(U_JY(n))<=tilde_m_JY(n,epsilon), hence Y_n(C)<tilde_M_JY(n,epsilon).",
            "interpretation": "The fixed-C diagonal eventually lies below the current sufficient certificate's mandatory floor, so that sufficient certificate does not certify the diagonal there.",
        },
        "machine_validation_receipt": machine,
        "proof_computation_boundary": {
            "proof": "Exact division by F_n, exponential-series domination and squeezing, fixed-C quantifiers, max/ceiling order, the already proved strict-search start, and monotonicity of exp prove the scoped statement.",
            "computation": "The merged evaluator checked frozen bytes and the ten planted classifications only after the hand-proof commit; this is corroboration and receives zero theorem credit.",
        },
        "non_implications": [
            "no failure or lower bound for the actual natural-order remainder",
            "no claim about a sharper below-floor sufficient envelope or every possible sufficient modulus",
            "no internal-prefix control or failure",
            "no Li-coefficient sign conclusion",
            "no evidence for or against RH",
        ],
        "residuals": [
            "a source-justified sufficient envelope below the quadratic U_JY floor",
            "the actual remainder on the fixed-C diagonal",
            "internal prefixes, Li signs, formalization, novelty, independent review, and RH",
        ],
        "authority": {
            "same_context_hand_proof": True,
            "scoped_mathematical_result": True,
            "formal_proof": False,
            "independent_review": False,
            "novelty": False,
            "actual_jy_remainder": False,
            "li_signs": False,
            "riemann_hypothesis": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "software_credit_units": 0,
        },
        "credit": {
            "mathematical": ["one elementary fixed-C current-sufficient-certificate floor-incompatibility lemma"],
            "record_checker_computation_alone": 0,
            "git_ci_schema_hash_runtime": 0,
        },
    })


def lesson_document(result: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "record_type": "SCOPED_MATHEMATICAL_LESSON",
        "unit_id": "MATH-RH-ANA003K-JY-C001-POST-ACTIVATION-FIXED-C-FLOOR",
        "mathematical_unit_count": 1,
        "credit_type": "SCOPED_PROOF_OR_LEMMA",
        "authority": "SAME_CONTEXT_SCOPED_MATHEMATICS_NO_RH_ROOT_AUTHORITY",
        "seven_field_math_lesson": {
            "attempted_implication": "Test whether the currently proved Johnston--Yang sufficient strict-search certificate can cover log Y_n=C n^(5/3)log^2(n+e), separately for each arbitrary fixed C>0.",
            "exact_result_or_failure": "The ratio to the mandatory quadratic floor tends to zero for every fixed C>0. Consequently the diagonal is eventually below F_n, U_JY, ceil(U_JY), and tilde_m_JY, so Y_n(C)<tilde_M_JY. This is failure of the current sufficient certificate to reach that diagonal, not failure of the actual remainder.",
            "supported_and_competing_causes": "Supported cause: exact division leaves a bounded n^2/(n+0.515)^2 factor times the vanishing scale log^2(n+e)/n^(1/3). Fixed C preserves this degree gap. The competing growing-C_n world can erase the gap but is outside the frozen quantifier. A sharper envelope valid below U_JY could still control the actual remainder. Epsilon-dependent excess cannot lower a strict-search threshold below its mandatory start.",
            "scope": "One arbitrary fixed real C>0 at a time and only the current sufficient strict-search certificate. No cutoff uniform over unbounded C; no actual-remainder, internal-prefix, Li-sign, novelty, independent-review, formal-proof, or RH authority.",
            "falsifier": "Refute the exact ratio identity or logarithm-over-power limit; let C depend on n; reverse the max/ceiling chain; break the bound tilde_m_JY>=ceil(U_JY); or infer actual remainder, prefixes, Li signs, or RH from certificate insufficiency.",
            "mathematical_repair": "A positive successor must freeze and validate a source-complete envelope whose proof domain extends below the quadratic U_JY floor, or prospectively freeze a larger diagonal. It may not alter the evaluated theorem, choose C after outcomes, or relabel certificate insufficiency as object failure.",
            "proof_and_source_evidence": "Exact algebra for F_n; t_n=(1/3)log(n+e); exp(t)>=t^3/6; squeezing; fixed-C scalar multiplication; max and ceiling order; strict monotonicity of exp; and the earlier proved strict-search start m0=ceil(U_JY). The record checker, planted software worlds, Git, CI, hashes, schemas, and chronology receive zero mathematical credit.",
        },
        "deduplication": {
            "new_scoped_mathematical_unit_count": 1,
            "global_ledger_updated": False,
            "independent_review_credit": 0,
            "assurance_metadata_mathematical_credit": 0,
            "literature_novelty_claim": False,
        },
        "evidence_pointers": [PATHS["candidate"], PATHS["activation"], PATHS["hand_proof"], PATHS["result"]],
        "result_artifact_hash": result["artifact_hash"],
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def review_document(result: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "review_id": "RH-ANA-003k-JY-C001-POST-ACTIVATION-RESULT-REVIEW-20260812T175200Z",
        "candidate_id": CANDIDATE_ID,
        "review_kind": "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
        "reviewed_at_utc": REVIEWED_AT,
        "roles": {
            "domain_theory": "The exact degree gap is 2-5/3=1/3; 0.515, 0.8274, and fixed C remain present throughout.",
            "analogy_method_transfer": "Only the standard theorem that logarithms lose to positive powers transfers; it gives no remainder or RH authority.",
            "adversarial_falsification": "The growing-C_n, dropped-0.515, reversed-ceiling, missing-source, and certificate-to-object worlds are the cheapest decisive attacks.",
            "formal_methods": "The exponential-series squeeze is an exact hand proof. The evaluator is a record checker rather than a proof assistant.",
            "novelty_research_value": "No novelty claim is made. The scoped value is decisive route pruning for the current sufficient certificate.",
        },
        "strongest_objection": "Being below a sufficient threshold says only that this certificate is unavailable; it does not show the actual remainder is large or uncontrolled.",
        "blocking_concerns": [],
        "verdict": "INTERNALLY_COHERENT_SCOPED_CERTIFICATE_INCOMPATIBILITY_NO_HIGHER_AUTHORITY",
        "authority": {"independent": False, "formal": False, "novelty": False, "rh": False},
        "result_artifact_hash": result["artifact_hash"],
    })


def trace_document(result: dict, lesson: dict, review: dict) -> dict:
    previous = PREVIOUS_EVENT_HASH
    specifications = [
        ("E10", "FALSIFIER_RUN", EXECUTED_AT, "After the committed exact hand proof, materialize all ten frozen worlds through the merged evaluator.", ["TEN_OF_TEN_EXPECTED_LABELS", "PASS_CANDIDATE_THEOREM"]),
        ("E11", "RESULT_RECORDED", RECORDED_AT, "Record the fixed-C limit and only its current-sufficient-certificate consequence.", [result["artifact_hash"]]),
        ("E12", "RESIDUAL_OPENED", RECORDED_AT, "Keep below-floor envelopes, actual remainder, prefixes, Li signs, and RH open.", ["BELOW_FLOOR_ENVELOPE_OPEN", "ACTUAL_REMAINDER_OPEN", "RH_OPEN"]),
        ("E13", "REVIEWED", REVIEWED_AT, "Run role-separated same-context review without independent-review inflation.", [review["artifact_hash"], lesson["artifact_hash"]]),
    ]
    entries = []
    for suffix, event_type, timestamp, action, outputs in specifications:
        row = {
            "event_id": f"RH-ANA003K-JY-C001-{suffix}-POST-ACTIVATION",
            "atom_id": "RH-ANA-003k-JY-MOVING-DIAGONAL",
            "event_type": event_type,
            "timestamp": timestamp,
            "state_summary": "Candidate and evaluator activation are public; the hand proof is committed before computational corroboration.",
            "action_summary": action,
            "evidence_pointers": [PATHS["activation"], PATHS["hand_proof"], PATHS["result"], PATHS["lesson"], PATHS["review"]],
            "alternatives_considered": ["infer actual remainder failure", "allow n-dependent C", "retain current-certificate fixed-C scope"],
            "decision_rationale": "The exact proof supports only the fixed-C floor ratio and the consequent unavailability of this sufficient certificate at the diagonal.",
            "outputs": outputs,
            "uncertainties": ["actual remainder, formal proof, independent review, novelty, Li signs, and RH remain unresolved"],
            "residuals": ["no sufficient below-floor envelope has been supplied"],
            "next_steps": ["freeze a separate below-floor-envelope or larger-diagonal atom before any successor candidate"],
            "previous_event_hash": previous,
        }
        row = seal(row)
        previous = row["artifact_hash"]
        entries.append(row)
    return seal({
        "schema_version": "1.0.0",
        "trace_id": "RH-ANA003K-JY-C001-POST-ACTIVATION-RESULT-TRACE-20260812T175200Z",
        "parent_trace": f"{BASE}/09_trace/RH_ANA_003k_JY_C001_FLOOR_RATIO_CANDIDATE_FREEZE_TRACE_20260812.json",
        "activation_public_merge_sha": ACTIVATION_MERGE,
        "hand_proof_commit": HAND_PROOF_COMMIT,
        "entries": entries,
    })


def framework_revalidation_document() -> dict:
    return seal({
        "schema_version": "1.0.0",
        "observation_id": "RH-ANA003K-JY-C001-POST-ACTIVATION-FRAMEWORK-REVALIDATION-20260812T175100Z",
        "candidate_id": CANDIDATE_ID,
        "observed_at_utc": RECORDED_AT,
        "application_framework_pin": FRAMEWORK_PIN,
        "framework_origin_main_observed": FRAMEWORK_MAIN,
        "protected_mathematical_surface_changed_since_pin": False,
        "intervening_change_scope": "Quantifier co-witness proposal-shadow implementation, schema, tests, and self-RAKL receipts only; it cannot grant proof authority and changes no protected mathematical gate used here.",
        "verdict": "CURRENT_NONBLOCKING_NO_NEW_APPLICABLE_CANONICAL_MATH_GATE",
        "licenses_exact_scoped_result_recording": True,
        "grants_mathematical_or_scientific_authority": False,
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        "recheck_trigger": "framework main moves before merge or a protected mathematical authority surface changes",
    })


def build_documents() -> dict[str, dict]:
    result = result_document()
    lesson = lesson_document(result)
    review = review_document(result)
    trace = trace_document(result, lesson, review)
    framework_revalidation = framework_revalidation_document()
    return {
        "result": result,
        "lesson": lesson,
        "review": review,
        "trace": trace,
        "framework_revalidation": framework_revalidation,
    }


def main() -> None:
    for name, document in build_documents().items():
        path = ROOT / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
