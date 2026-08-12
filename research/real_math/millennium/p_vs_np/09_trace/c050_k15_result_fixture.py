"""C050 k=15 scoped result after public candidate and local proof freeze."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


B = Path("research/real_math/millennium/p_vs_np")
CANDIDATE_ID = "C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1"
CANDIDATE_CORE_SHA256 = "sha256:c869e4726c36551b69f10407dd482f30d83f2b2a8129c5364ac2c08eda4c1d43"
CANDIDATE_ARTIFACT_HASH = "sha256:47bf8d99a7c5620b8ab8f2e3fadfb762125df921bed4b65fe2ddb56f4733c5e1"
CANDIDATE_PUBLIC_MERGE = "0b0f1840f99043a57050d625683ba8311fef3f24"
RESULT_BASE = "02c5fb7764116cf075d8dd5efd7b6fe835275ab9"
PROOF_INPUT_COMMIT = "db520bae16f64419778e9f73240db8af42227d85"
EXECUTED_AT = "2026-08-12T07:05:11Z"
RECORDED_AT = "2026-08-12T07:05:33Z"
RAW_OUTPUT_SHA256 = "5d00ee600df1002355c084533ad0c9f7ebc294eea43f92c6fa401cfb317e5faf"
CERTIFICATE = B / "04_candidates/O9d12a2a1b_C050_K15_PROOF_CERTIFICATE_FREEZE_20260812.json"
AUTHORIZATION = B / "09_trace/O9d12a2a1b_C050_K15_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json"
CHRONOLOGY = B / "09_trace/O9d12a2a1b_C050_K15_PROOF_INPUT_CHRONOLOGY_20260812.json"
CHECKER = B / "05_falsification/c050_k15_alignment_proof_checker.py"
CANDIDATE_TRACE = B / "09_trace/O9d12a2a1b_C050_K15_CANDIDATE_FREEZE_TRACE_20260812.json"
PATHS = {
    "result": B / "05_falsification/O9d12a2a1b_C050_K15_PROOF_CHECK_RESULT_20260812.json",
    "failure": B / "07_memory/O9d12a2a1b_C050_K15_FAILURE_EXPERIENCE_20260812.json",
    "lesson": B / "07_memory/O9d12a2a1b_C050_K15_MATHEMATICAL_LESSON_20260812.json",
    "review": B / "08_reviews/O9d12a2a1b_C050_K15_RESULT_REVIEW_20260812.json",
    "trace": B / "09_trace/O9d12a2a1b_C050_K15_POST_FREEZE_RESULT_TRACE_20260812.json",
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


def event(value: dict) -> dict:
    document = dict(value)
    document["artifact_hash"] = canonical_hash(document)
    return document


def build_documents() -> dict[str, dict]:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    authorization = json.loads(AUTHORIZATION.read_text(encoding="utf-8"))
    proof_chronology = json.loads(CHRONOLOGY.read_text(encoding="utf-8"))
    evaluator_output = {
        "candidate_id": CANDIDATE_ID,
        "checked_current_parameter_pairs": [[2, 2], [3, 2]]
        + [[v, 1] for v in range(8, 16)],
        "common_separating_coordinate": 3,
        "h15_fixed_bit": 1,
        "obligations_checked": 8,
        "p16_fixed_bit": 0,
        "status": "PASS",
        "verdict": "SCOPED_OVERLAP_IMPOSSIBILITY",
    }
    exact_result = {
        "lemma": "H_15 intersection P_16 is empty.",
        "parent_parameter_forcing": "Canonical UNSAT encoded length 30 uniquely forces v=1,m=3 with no padding.",
        "parent_field_alignment": "The 12-bit header is followed by sign||1 literal pairs; the 15-bit suffix starts at x[15], and x[17] is a fixed variable-code bit 1.",
        "current_branch_exhaustion": "P_16 has exactly the unpadded (v,m)=(2,2),(3,2) regimes and the padded (v,m)=(8,1),...,(15,1) regimes at encoded length 32; all begin canonical MAGIC.",
        "separation": "Every h in H_15 has h[3]=1, while every p in P_16 has p[3]=MAGIC[3]=0.",
        "noncanonical_boundary": "H_15 and P_16 use canonical long-form words; malformed-to-tautology and all-zero short-contradiction fallback branches of the total decoder are excluded by definition.",
        "scope_consequence": "The result is k=15 only; no conclusion is drawn for any other k or for cover growth.",
    }
    diagnosis = {
        "status": "SUPPORTED_BOUNDED",
        "cause": "At the unique length-30 UNSAT-capable parent regime, the changed half-split still places a fixed v=1 variable-code bit at H-label coordinate 3; every canonical current prefix retains MAGIC[3]=0.",
        "competing_causes_rejected": [
            "H_15 is empty: the explicit v=1,m=3 contradictory formula proves nonvacuity",
            "only one current branch was checked: both unpadded and all eight padded parameter regimes are exhausted",
            "UNSAT semantics creates the separating bit: the bit follows from canonical v=1 syntax before semantic filtering",
            "noncanonical total-decoder fallbacks change P_16: those branches are outside the frozen canonical-prefix language",
            "literal transposition itself creates separation: C048 reduction faithfulness is independent of decoder-specific label alignment",
            "the record checker supplies proof authority: mathematical credit belongs to the hand/symbolic certificate",
        ],
        "relation_to_c049": "SPECIALIZATION_AND_REPETITION_OF_FIXED_VARIABLE_CODE_VERSUS_MAGIC_MISMATCH",
        "unique_global_cause_claimed": False,
    }
    falsifier = (
        "A canonical UNSAT length-30 parent outside v=1,m=3; an omitted canonical length-32 current regime; "
        "an H_15 label with h[3]=0; a P_16 prefix with p[3]=1; one exact common label; or a changed grammar, split, or reduction refutes the corresponding scoped obligation."
    )
    result = seal(
        {
            "schema_version": "1.0.0",
            "result_id": "PNP-C050-K15-PROOF-CHECK-RESULT-20260812",
            "atom_id": "O9d12a2a1b-C050",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": CANDIDATE_CORE_SHA256,
            "candidate_artifact_hash": CANDIDATE_ARTIFACT_HASH,
            "status": "PASS_SAME_CONTEXT_HAND_PROOF_RECORD_CHECK",
            "execution": {
                "executed_at": EXECUTED_AT,
                "raw_output_sha256": RAW_OUTPUT_SHA256,
                "network_used": False,
                "target_decoder_imported_or_executed": False,
                "formula_words_enumerated": False,
                "checker_path": str(CHECKER),
                "checker_raw_sha256": "882c2c7eaf16edc050ff4a019b4bbe9a18fc6bc2257479d9da37cb3d8dd2f03a",
            },
            "chronology": {
                "candidate_public_merge": CANDIDATE_PUBLIC_MERGE,
                "candidate_merge_precedes_result_access": True,
                "result_base_commit": RESULT_BASE,
                "proof_input_commit": PROOF_INPUT_COMMIT,
                "proof_inputs_frozen_before_execution": True,
                "evaluation_base_commit": PROOF_INPUT_COMMIT,
                "result_accessed_at": EXECUTED_AT,
                "recorded_at": RECORDED_AT,
            },
            "inputs": {
                "certificate": {
                    "path": str(CERTIFICATE),
                    "artifact_hash": certificate["artifact_hash"],
                },
                "authorization": {
                    "path": str(AUTHORIZATION),
                    "artifact_hash": authorization["artifact_hash"],
                },
                "proof_input_chronology": {
                    "path": str(CHRONOLOGY),
                    "artifact_hash": proof_chronology["artifact_hash"],
                },
            },
            "evaluator_output": evaluator_output,
            "exact_mathematical_result": exact_result,
            "diagnosis": diagnosis,
            "falsifier": falsifier,
            "residual": "Whether H_k intersects P_(k+1) for any untouched k>15 remains open; no later target is selected here.",
            "authority": {
                "same_context_hand_derivation": True,
                "formal": False,
                "independent": False,
                "novelty": False,
                "root": "OPEN",
            },
            "credit": {
                "mathematical": [
                    "unique length-30 parent regime",
                    "exhaustive length-32 current branch classification",
                    "bit-3 symbolic separation",
                    "explicit UNSAT nonvacuity and bounded diagnosis",
                ],
                "computation_alone": 0,
                "software_process": 0,
                "ci_schema_hash_runtime": 0,
            },
        }
    )
    failure = seal(
        {
            "schema_version": "1.0.0",
            "failure_id": "F-PNP-C050-K15-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
            "atom_id": "O9d12a2a1b-C050",
            "candidate_id": CANDIDATE_ID,
            "method_family": "literal-transpose suffix-row overlap repair",
            "attempted_implication": "The first untouched later-k source-admissible regime might repair the k=12 row-label disjointness and produce H_15 intersection P_16 nonempty.",
            "observed_result": "H_15 intersection P_16 is empty by an exact zero-based bit-3 contradiction.",
            "residual_signature": [
                "field-boundary alignment",
                "fixed variable-code bit versus canonical MAGIC bit",
                "exact suffix/prefix equality failure",
                "bounded k-specific obstruction",
            ],
            "diagnosis": diagnosis,
            "broken_assumptions": [
                "changing the half-length and suffix alignment need not remove the earlier fixed-code-versus-header obstruction",
                "multiple current grammar branches do not help when all share the conflicting MAGIC coordinate",
            ],
            "typed_relations": [
                {
                    "relation": "INSTANCE_OF",
                    "target_failure_id": "F-PNP-C049-K12-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
                    "witness": "At k=12 the forced H bit was coordinate 4; at k=15 the changed split moves a forced v=1 variable-code bit to H coordinate 3, which again meets a zero in MAGIC. The coordinate differs, so the k=15 derivation is new scoped evidence but not a new global mechanism.",
                }
            ],
            "scope": [
                "k=15 only",
                "exact canonical long-form grammar and equal split",
                "all frozen encoded-length-32 parameter regimes",
                "C048 swapped reduction retained",
                "no finite-to-general extrapolation",
            ],
            "falsifier": falsifier,
            "residual": "Whether H_k intersects P_(k+1) for any untouched k>15 remains open and requires a fresh context, target-blind selector, field derivation, and frozen discriminator.",
            "evidence_pointers": [str(CERTIFICATE), str(PATHS["result"])],
            "local_repair_attempts": [
                "changed from the k=12 payload-boundary split to the target-blind source-admissible k=15 split",
                "exhausted both unpadded and padded current-word branch families",
            ],
            "timestamp": RECORDED_AT,
            "authority": "SCOPED_SAME_CONTEXT_DIAGNOSIS_NOT_GLOBAL_CAUSE_OR_IMPOSSIBILITY",
        }
    )
    lesson = seal(
        {
            "record_type": "SCOPED_MATHEMATICAL_LESSON",
            "unit_id": "MATH-PNP-C050-K15-FIXED-CODE-MAGIC-SEPARATION",
            "mathematical_unit_count": 1,
            "credit_type": "SCOPED_EXACT_SYMBOLIC_IMPOSSIBILITY_PROOF",
            "authority": "SAME_CONTEXT_SCOPED_MATHEMATICS_NO_P_VS_NP_ROOT_AUTHORITY",
            "application": {
                "repository": "SzeChunYiu/RAKL_math",
                "base_sha": RESULT_BASE,
                "candidate_public_merge": CANDIDATE_PUBLIC_MERGE,
                "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            },
            "seven_field_math_lesson": {
                "attempted_implication": "Moving from the k=12 payload-boundary split to the prospectively selected first untouched source-admissible half-length k=15 might make the canonical UNSAT suffix-row language overlap the next canonical-prefix language.",
                "exact_result_or_failure": "It does not: H_15 intersection P_16 is empty. Unique length-30 UNSAT syntax forces h[3]=1, while every canonical length-32 prefix in both exhaustive branch families has p[3]=MAGIC[3]=0.",
                "supported_and_competing_causes": "Supported bounded cause: the new split moves, but does not eliminate, a forced v=1 variable-code bit aligned against a zero of MAGIC. This is a specialization/repetition of C049 rather than a new global cause. H_15 vacuity, omitted padded branches, UNSAT semantics as the bit source, noncanonical decoder fallbacks, transpose faithfulness, and checker authority are rejected competing explanations.",
                "scope": "Exactly k=15 under the unchanged canonical long-form grammar, equal split, and C048 swapped reduction. P_16 and H_15 exclude malformed-to-tautology and all-zero short-contradiction fallback branches by definition. No statement is made for k>15, cover growth, circuit lower bounds, novelty, or P versus NP.",
                "falsifier": falsifier,
                "mathematical_repair": "For any later target, rederive the parent parameter regime, suffix offset, and every current prefix branch before candidate freeze; seek a level where no forced suffix variable-code coordinate collides with a fixed MAGIC zero, or prove a parametric obstruction under freshly gated chronology.",
                "proof_and_source_evidence": "The hand certificate proves unique v=1,m=3 length-30 parent syntax, supplies an explicit UNSAT formula, exhausts every frozen length-32 branch ((2,2),(3,2) unpadded and (8,1),...,(15,1) padded), and derives the common bit-3 contradiction. The record checker only verifies those frozen records and receives zero mathematical credit.",
            },
            "deduplication": {
                "new_global_cause_claimed": False,
                "relation_to_c049": "SPECIALIZATION_AND_REPETITION_OF_FIXED_VARIABLE_CODE_VERSUS_MAGIC_MISMATCH",
                "new_scoped_mathematical_unit_count": 1,
                "global_ledger_updated": False,
                "literature_novelty_claim": False,
                "independent_review_credit": 0,
                "assurance_metadata_mathematical_credit": 0,
            },
            "evidence_pointers": [
                str(CERTIFICATE),
                str(PATHS["result"]),
                str(PATHS["failure"]),
            ],
        }
    )
    review = seal(
        {
            "schema_version": "1.0.0",
            "review_id": "PNP-C050-K15-RESULT-REVIEW-20260812",
            "atom_id": "O9d12a2a1b-C050",
            "candidate_id": CANDIDATE_ID,
            "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW",
            "independent_review": False,
            "role_reviews": [
                {
                    "role": "domain_theory_lead",
                    "finding": "The length formulas force the sole parent regime and exhaust both current branch families; canonical-language definitions exclude total-decoder fallbacks.",
                    "verdict": "ACCEPT_SCOPED",
                },
                {
                    "role": "adversarial_falsification_lead",
                    "finding": "The strongest attacks are an omitted length-32 branch, a noncanonical fallback smuggled into P_16, or one common label; the certificate addresses the first two and freezes the third as falsifier.",
                    "verdict": "ACCEPT_SCOPED",
                },
                {
                    "role": "formal_methods_lead",
                    "finding": "The certificate is a hand proof with a deterministic record checker, not a proof-assistant theorem. Candidate and proof-input identities precede execution.",
                    "verdict": "ACCEPT_NONFORMAL",
                },
                {
                    "role": "novelty_research_value_lead",
                    "finding": "The k=15 coordinate differs from k=12 but the mechanism repeats fixed variable-code versus MAGIC mismatch; retain one scoped unit and no novelty or new-global-cause claim.",
                    "verdict": "ACCEPT_DEDUPLICATED",
                },
            ],
            "strongest_objection": "P_16 branch exhaustion would be false if total-decoder malformed/all-zero branches were included; the frozen P_16 definition is canonical-prefix only, and the certificate states this boundary explicitly.",
            "deduplication_note": "The changed separating coordinate is new k=15 evidence, but the failure mechanism is not a new global cause; it is a scoped specialization/repetition of C049.",
            "verdict": "ACCEPT_SCOPED_K15_EMPTY_INTERSECTION_HAND_PROOF",
            "unresolved_uncertainties": [
                "no independent or formal proof check",
                "no novelty search",
                "all k>15 remain open",
                "cover and complexity bridges remain open",
            ],
            "authority": {
                "mathematical_result": "SCOPED_SAME_CONTEXT_HAND_PROOF",
                "formal": False,
                "independent": False,
                "novelty": False,
                "root": "OPEN",
            },
            "evidence_pointers": [str(CERTIFICATE), str(PATHS["result"]), str(PATHS["lesson"])],
        }
    )

    entries = list(json.loads(CANDIDATE_TRACE.read_text(encoding="utf-8"))["entries"])
    falsifier_event = event(
        {
            "event_id": "O9d12a2a1b-C050-E10",
            "atom_id": "O9d12a2a1b-C050",
            "event_type": "FALSIFIER_RUN",
            "timestamp": EXECUTED_AT,
            "state_summary": "The public k=15 candidate and locally committed hand-proof inputs precede execution; the checker verifies all eight frozen obligations and every frozen length-32 parameter regime without importing the target decoder.",
            "action_summary": "Evaluate the exact certificate and authorization, including planted exhaustive branch identity and the common bit-3 contradiction.",
            "evidence_pointers": [str(CERTIFICATE), str(AUTHORIZATION), str(PATHS["result"])],
            "alternatives_considered": ["enumerate formula words", "inspect another k", "check only one current branch", "execute the frozen exact record operation"],
            "decision_rationale": "Only the exact certificate check preserves candidate identity, branch exhaustion, and bounded scope; mathematical authority remains with the hand proof.",
            "outputs": ["PASS_RECORD_CHECK", "SCOPED_OVERLAP_IMPOSSIBILITY", "ALL_FROZEN_LENGTH32_BRANCHES_CHECKED"],
            "uncertainties": ["same-context and nonformal", "other k open"],
            "residuals": ["k>15 overlap", "root OPEN"],
            "next_steps": ["record the scoped lemma, bounded diagnosis, and residual"],
            "previous_event_hash": entries[-1]["artifact_hash"],
        }
    )
    entries.append(falsifier_event)
    result_event = event(
        {
            "event_id": "O9d12a2a1b-C050-E11",
            "atom_id": "O9d12a2a1b-C050",
            "event_type": "RESULT_RECORDED",
            "timestamp": RECORDED_AT,
            "state_summary": "The exact k=15 overlap is empty by a hand-proved common bit-3 contradiction across every frozen current branch.",
            "action_summary": "Record the lemma, proof core, bounded cause, competing causes, falsifier, scope, and zero root authority.",
            "evidence_pointers": [str(PATHS["result"]), str(PATHS["failure"]), str(PATHS["lesson"])],
            "alternatives_considered": ["generalize from k=12 and k=15", "count checker execution as mathematics", "record k=15 only"],
            "decision_rationale": "The proof depends on the exact length-30 split, so only the frozen k=15 intersection is decided.",
            "outputs": ["H15_INTERSECTION_P16_EMPTY", "K15_ONLY", "ROOT_OPEN"],
            "uncertainties": ["no independent/formal/novelty check"],
            "residuals": ["all untouched k>15 remain open"],
            "next_steps": ["open a freshly gated later-k residual before any new candidate"],
            "previous_event_hash": entries[-1]["artifact_hash"],
        }
    )
    entries.append(result_event)
    residual_event = event(
        {
            "event_id": "O9d12a2a1b-C050-E12",
            "atom_id": "O9d12a2a1b-C050",
            "event_type": "RESIDUAL_OPENED",
            "timestamp": "2026-08-12T07:05:34Z",
            "state_summary": "The prospectively selected k=15 layer is closed negatively; no finite pair of negative levels establishes a parametric no-go.",
            "action_summary": "Preserve untouched k>15 overlap as an unselected residual and relate the failure narrowly to C049.",
            "evidence_pointers": [str(PATHS["failure"]), str(PATHS["lesson"])],
            "alternatives_considered": ["infer all-k impossibility", "select the next k now", "freeze only the open residual"],
            "decision_rationale": "The separating coordinate changes with field alignment, so a fresh context and target-blind selector are required before another candidate.",
            "outputs": ["K_GT_15_REMAINS_OPEN", "NO_FINITE_TO_GENERAL_EXTRAPOLATION"],
            "uncertainties": ["a later overlap may exist", "a parametric obstruction is unproved"],
            "residuals": ["fresh later-k context/memory/shortcut/trace gates required"],
            "next_steps": ["do not propose a new later-k candidate in this result round"],
            "previous_event_hash": entries[-1]["artifact_hash"],
        }
    )
    entries.append(residual_event)
    review_event = event(
        {
            "event_id": "O9d12a2a1b-C050-E13",
            "atom_id": "O9d12a2a1b-C050",
            "event_type": "REVIEWED",
            "timestamp": "2026-08-12T07:05:35Z",
            "state_summary": "Role-separated same-context review accepts the k=15 hand proof narrowly and explicitly denies independent, formal, novelty, global-cause, cover, and root authority.",
            "action_summary": "Review branch exhaustion, canonical-only scope, falsifiers, deduplication, and residual discipline.",
            "evidence_pointers": [str(PATHS["review"]), str(PATHS["lesson"])],
            "alternatives_considered": ["claim a new global failure cause", "claim independent review", "retain one deduplicated scoped unit"],
            "decision_rationale": "The coordinate-3 derivation is new scoped evidence, while its mechanism repeats the earlier fixed-code-versus-MAGIC family.",
            "outputs": ["ACCEPT_SCOPED_K15_RESULT", "NOT_INDEPENDENT", "NO_GLOBAL_LEDGER_UPDATE"],
            "uncertainties": review["unresolved_uncertainties"],
            "residuals": ["k>15 and root remain open"],
            "next_steps": ["separate synthesis may decide global-ledger treatment"],
            "previous_event_hash": entries[-1]["artifact_hash"],
        }
    )
    entries.append(review_event)
    trace = {
        "trace_id": "PNP-O9d12a2a1b-C050-K15-POST-FREEZE-RESULT-TRACE-20260812",
        "entries": entries,
    }
    return {
        "result": result,
        "failure": failure,
        "lesson": lesson,
        "review": review,
        "trace": trace,
    }


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
