"""Deterministic C050 source-only selector/discriminator freeze.

The fixture proves only which untouched grammar regime is selected from public
length arithmetic.  It cannot import the decoder, compare target bits, decide
the intersection, or execute an evaluator.  All target work requires a public
successor authorization after this candidate identity is committed.
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


APPLICATION_BASE_SHA = "451d9506d365f06eb314323523ba123edd3ffb32"
FRAMEWORK_SHA = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
CONTEXT_PACKET_HASH = "b50f857493e88680bd74943321316451b379c664e0e39d7d2d709f01d5be2a56"
PRE_GATE_BLOB = "e8a37f3ce0a55bcbeb6f1671b2373c50464c837f"
PRE_GATE_RAW_SHA256 = "74f40f30ed54eb5e6fa5160455cc83d27e6b7d52be4fdc63b83e30ed67654add"
PRE_TRACE_BLOB = "005538668d3bd85f09a4f1c94b24d968c6539213"
PRE_TRACE_RAW_SHA256 = "311c890d50851ccb7523e625b3952bf44601c9871980d9b699dd7fcafe2766c4"
EVALUATOR_RAW_SHA256 = "76aa37db99021e324955e157759f1985904182b90bf14939dcafb353e8cf2607"
FROZEN_AT = "2026-08-12T06:14:09Z"
ATOM_ID = "O9d12a2a1b-C050"
CANDIDATE_ID = "C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1"

BASE = "research/real_math/millennium/p_vs_np"
PRE_GATE = f"{BASE}/09_trace/O9d12a2a1b_C050_PRE_CANDIDATE_GATE_RECEIPT_20260812.json"
PRE_TRACE = f"{BASE}/09_trace/O9d12a2a1b_C050_PRE_CANDIDATE_TRACE_20260812.json"
EVALUATOR = f"{BASE}/05_falsification/c050_k15_alignment_inert_evaluator.py"
PATHS = {
    "candidate": f"{BASE}/04_candidates/O9d12a2a1b_C050_K15_SELECTOR_DISCRIMINATOR_FREEZE_20260812.json",
    "manifest": f"{BASE}/05_falsification/O9d12a2a1b_C050_K15_ALIGNMENT_EVALUATOR_FREEZE_20260812.json",
    "authorization": f"{BASE}/09_trace/O9d12a2a1b_C050_K15_EVALUATION_AUTHORIZATION_20260812.json",
    "framework_binding": f"{BASE}/09_trace/O9d12a2a1b_C050_K15_FRAMEWORK_SUBJECT_FREEZE_BINDING_20260812.json",
    "framework_observation": f"{BASE}/09_trace/O9d12a2a1b_C050_K15_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "trace": f"{BASE}/09_trace/O9d12a2a1b_C050_K15_CANDIDATE_FREEZE_TRACE_20260812.json",
    "receipt": f"{BASE}/09_trace/O9d12a2a1b_C050_K15_CANDIDATE_FREEZE_RECEIPT_20260812.json",
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
    candidate_core = {
        "schema_version": "1.0.0",
        "candidate_id": CANDIDATE_ID,
        "atom_id": ATOM_ID,
        "candidate_kind": "TARGET_BLIND_SELECTOR_AND_TWO_SIDED_DISCRIMINATOR_CANDIDATE",
        "frozen_at": FROZEN_AT,
        "object": "The exact decoder-specific language intersection H_15 ∩ P_16 under the unchanged C041 grammar and C048 swapped reduction.",
        "qoi": "EXACT_H15_INTERSECTION_P16_CLASSIFICATION",
        "selector": {
            "definition": "k*=min{k>=14: a source-explicit canonical UNSAT word of encoded length 2k exists and at least one canonical word of encoded length 2(k+1) exists}",
            "eligible_domain": "integers k>=14; the quarantined family is excluded by process identity, not by its mathematical content",
            "selected_k": 15,
            "selection_target_blind": True,
            "uses_overlap_bits": False,
            "uses_decoder_or_evaluator": False,
            "uses_target_result": False,
            "length_function": "R(v,m)=8+(2*bit_length(v)-1)+(2*bit_length(m)-1)+3*m*(1+bit_length(v)); E(v,m)=R(v,m)+(R(v,m) mod 2)",
        },
        "selector_proof": {
            "gamma_length_lemma": "For n>=1, |gamma(n)|=2*bit_length(n)-1.",
            "unsat_clause_lower_bound": "Every one-clause 3CNF is satisfiable, so canonical UNSAT requires m>=2.",
            "length_28_impossibility": {
                "claim": "There is no canonical UNSAT long-form word of encoded length 28.",
                "v_eq_1": {
                    "E_1_2": 24,
                    "E_1_3": 30,
                    "monotonic_for_m_ge_3": True,
                },
                "v_ge_2_m_ge_2_minimum": {
                    "attained_at": [2, 2],
                    "encoded_length": 32,
                },
                "exhaustion_argument": "With m>=2, v=1 jumps from encoded length 24 at m=2 to 30 at m=3 and increases thereafter; v>=2 has bit_length(v)>=2 and is minimized at v=2,m=2 with encoded length 32. These cases exhaust all canonical UNSAT parameters.",
            },
            "length_30_unsat_capable_regime": {
                "claim": "The unique canonical UNSAT-capable length-30 parameter regime is v=1,m=3.",
                "parameters": {"v": 1, "m": 3},
                "raw_length": 30,
                "encoded_length": 30,
                "padding": False,
                "explicit_formula": "(z OR z OR z) AND (not-z OR not-z OR not-z) AND (z OR z OR z)",
                "unsat_proof": "The first two clauses force z and not-z respectively; the third clause is redundant, so no assignment satisfies all three.",
                "parameter_exhaustion": "For m=2 the only smaller-width case has length 24 and bit_length(v)>=2 gives at least 32; for m=3, v=1 gives 30 and bit_length(v)>=2 gives at least 42; m>=4 gives at least 38 already at v=1.",
            },
            "length_32_canonical_regimes": [
                {
                    "v_range": [2, 3],
                    "m": 2,
                    "raw_length": 32,
                    "padding": False,
                },
                {
                    "v_range": [8, 15],
                    "m": 1,
                    "raw_length": 31,
                    "encoded_length": 32,
                    "padding": True,
                },
            ],
            "length_32_exhaustion_argument": "For m=1, encoded length 32 occurs exactly at bit_length(v)=4, hence 8<=v<=15, with raw length 31 and one zero pad. For m=2 it occurs exactly at bit_length(v)=2, hence v in {2,3}, with raw length 32. At m=3, v=1 gives 30 and bit_length(v)>=2 gives at least 42; m>=4 gives at least 38. Thus the two listed regimes are exhaustive.",
            "selector_conclusion": "The least eligible source-only half-length is k*=15: length 28 is UNSAT-impossible, length 30 has an explicit canonical UNSAT formula, and length 32 has canonical current words.",
            "authority": "SAME_CONTEXT_SOURCE_GRAMMAR_DERIVATION_FROZEN_NOT_INDEPENDENT_REVIEW",
        },
        "discriminator": {
            "qoi": "EXACT_H15_INTERSECTION_P16_CLASSIFICATION",
            "predicted_result": None,
            "positive_witness": "x=r||c has length 30 with |r|=|c|=15; x has an explicit canonical parse and a mathematical UNSAT proof; y has length 32 with an explicit canonical parse; prefix_16(y)=1||c bit-for-bit.",
            "negative_certificate": "A symbolic proof exhausts every frozen length-30 parent branch and every frozen length-32 current branch and derives a contradiction to canonical parsing, exact equality, or parent UNSAT.",
            "allowed_result_branches": [
                "EXACT_OVERLAP_WITNESS",
                "SCOPED_OVERLAP_IMPOSSIBILITY",
                "BOUNDED_NO_MATCH_ONLY",
                "CANNOT_CHECK",
            ],
            "bounded_no_match_scope": "A finite or incomplete search cannot be generalized beyond its exact checked domain.",
            "swapped_reduction": "Retain x=r||c -> (2^15+c,r) for the transposed graph; no encoding, split, label, or coordinate change is allowed.",
        },
        "proof_obligations_for_future_evaluation": [
            "PARENT_LENGTH_30_PARAMETER_EXHAUSTION",
            "CURRENT_LENGTH_32_PARAMETER_BRANCH_EXHAUSTION",
            "EXACT_CANONICAL_PARENT_PARSE",
            "EXACT_CANONICAL_CURRENT_PARSE",
            "EXACT_1C_EQUALS_PREFIX16_BITWISE",
            "PARENT_UNSAT_PROOF_INDEPENDENT_OF_SYNTAX",
            "SWAPPED_REDUCTION_PRESERVED",
            "BOUNDED_SCOPE_ONLY",
        ],
        "falsifiers": {
            "selector": [
                "a canonical UNSAT long-form encoding of length 28",
                "failure of the explicit v=1,m=3 length-30 formula to be canonical and UNSAT",
                "absence of every listed canonical length-32 regime",
                "an omitted canonical length-32 parameter regime",
                "any selector dependence on overlap bits or a target result",
            ],
            "future_positive_branch": [
                "either word lacks its stated canonical parse",
                "one unequal bit in prefix_16(y)=1||c",
                "one satisfying assignment for the claimed UNSAT parent formula",
                "a changed split, encoding, or swapped reduction",
            ],
            "future_impossibility_branch": [
                "one explicit canonical pair satisfying exact equality with a mathematical UNSAT proof for the parent",
                "one omitted parent or current grammar branch",
                "a bounded miss presented as an unbounded theorem",
            ],
        },
        "difference_witness_vs_k12": {
            "prior_failure_id": "C049-K12-FIRST-ADMISSIBLE-OVERLAP-SEPARATION-v1",
            "changed_structural_coordinate": "The parent half-length changes from 12 to 15: the v=1,m=3 length-30 split occurs three payload bits after the 12-bit header, rather than at the k=12 payload boundary.",
            "failed_assumption_not_transported": "The k=12 proof's complete-payload suffix pattern and its single forced shared-bit mismatch are not assumed at k=15.",
            "new_current_branch_structure": "Length 32 has both unpadded v in {2,3},m=2 branches and padded v in {8,...,15},m=1 branches; every branch must be checked.",
            "why_old_falsifier_may_not_apply": "The suffix coordinate map and current-prefix field map differ materially, so the old fixed-bit location has no authority until all new offsets are derived.",
            "cheapest_repeat_failure_test": "After a separate public authorization, derive symbolic field offsets for the sole parent regime and every frozen current regime, then compare all 16 shared coordinates before any semantic UNSAT check.",
        },
        "result_access_firewall": {
            "allowed_now": [
                "use the frozen public grammar length formula",
                "prove source-only selector arithmetic and explicit source-side UNSAT nonvacuity",
                "freeze the exact two-sided discriminator and all future result branches",
                "freeze an inert evaluator identity without importing or executing it",
            ],
            "forbidden_now": [
                "inspect or use the quarantined family or any of its mathematical content",
                "import or execute the target decoder or any target-capable evaluator",
                "compare target shared bits",
                "determine or predict H_15 intersection P_16",
                "claim target theorem truth, mathematical saturation, cover growth, or P-versus-NP progress",
            ],
            "breach_policy": "Quarantine this candidate identity, preserve it as retrospective history, and open a fresh untouched-family successor.",
        },
        "target_access": {
            "decoder_imported_or_executed": False,
            "evaluator_imported_or_executed": False,
            "overlap_bits_compared": False,
            "target_result_accessed": False,
            "target_result_determined": False,
        },
        "non_guarantees": [
            "no claim that H_15 intersects or is disjoint from P_16",
            "no target parse, bit comparison, SAT/UNSAT evaluation, or result",
            "no cover lower bound, novelty, independent review, or P-versus-NP authority",
            "the selector derivation does not promote the target candidate",
        ],
        "source_identity": {
            "application_base_commit": APPLICATION_BASE_SHA,
            "framework_commit": FRAMEWORK_SHA,
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
            "mathematical_content": [
                "source-only selector length proof",
                "explicit UNSAT-capable length-30 construction",
                "exhaustive canonical length-32 parameter classification",
                "two-sided target discriminator, falsifiers, and k=12 DifferenceWitness",
            ],
            "assurance_only_zero_credit": [
                "Git/branch/PR chronology",
                "CI/tests",
                "schemas/hashes/serialization",
                "framework subject binding and evaluator wiring",
            ],
            "candidate_freeze_mathematical_result_credit": False,
            "math_ledger_entry_created": False,
        },
    }
    candidate_identity = {
        "candidate_id": CANDIDATE_ID,
        "canonical_core_sha256": canonical_hash(candidate_core),
        "identity_scope": "FULL_CANDIDATE_CORE_BEFORE_IDENTITY_AND_ARTIFACT_HASH",
    }
    return seal({**candidate_core, "candidate_identity": candidate_identity})


def framework_documents() -> tuple[dict, dict]:
    binding = FrameworkSubjectFreezeBinding(
        binding_id="PNP-C050-K15-FRAMEWORK-SUBJECT-FREEZE-20260812",
        authoritative_framework_sha=FRAMEWORK_SHA,
        pre_candidate_packet_hash=CONTEXT_PACKET_HASH,
        frozen_at_utc=FROZEN_AT,
        evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:config/rakl-framework-pin.json",
            f"git:{APPLICATION_BASE_SHA}:framework/RAKL",
            f"git:{FRAMEWORK_SHA}:src/rakl/math_research_runtime.py",
            f"git:{FRAMEWORK_SHA}:src/rakl/framework_candidate_freeze.py",
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=FRAMEWORK_SHA,
        intervening_diff=(),
        observation_evidence_pointers=(
            f"git:{APPLICATION_BASE_SHA}:config/rakl-framework-pin.json",
            f"git:{APPLICATION_BASE_SHA}:framework/RAKL",
        ),
    )
    report = audit_candidate_freeze_framework_subject(binding, observation, required=True)
    if report.verdict is not CandidateFreezeRevalidationVerdict.CURRENT_UNCHANGED:
        raise RuntimeError(f"framework subject is not current: {report.verdict.value}")
    binding_document = seal(
        {
            **binding.document(),
            "successor_of": f"{BASE}/09_trace/O9d12a2a1b_C050_FRAMEWORK_SUBJECT_FREEZE_BINDING_20260812.json",
            "successor_reason": "The authoritative framework advanced after the historical pre-candidate binding; this candidate freeze rebinds without rewriting historical chronology.",
            "grants_scientific_authority": False,
        }
    )
    observation_document = seal(
        {
            "schema_version": "framework-subject-revalidation-observation-v1",
            "observation_id": "PNP-C050-K15-FRAMEWORK-SUBJECT-REVALIDATION-20260812",
            "observed_current_main_sha": observation.observed_current_main_sha,
            "intervening_diff": [],
            "observation_evidence_pointers": list(observation.observation_evidence_pointers),
            "verdict": report.verdict.value,
            "reasons": list(report.reasons),
            "licenses_candidate_materialization": report.licenses_candidate_materialization,
            "grants_scientific_authority": False,
        }
    )
    return binding_document, observation_document


def build_documents() -> dict[str, dict]:
    candidate = candidate_document()
    framework_binding, framework_observation = framework_documents()
    manifest = seal(
        {
            "schema_version": "1.0.0",
            "manifest_id": "PNP-C050-K15-ALIGNMENT-EVALUATOR-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "frozen_at": FROZEN_AT,
            "status": "FROZEN_INERT_CONTRACT_NOT_IMPORTED_NOT_EXECUTED",
            "evaluator": {"path": EVALUATOR, "raw_sha256": EVALUATOR_RAW_SHA256},
            "required_future_obligations": candidate[
                "proof_obligations_for_future_evaluation"
            ],
            "allowed_future_result_branches": candidate["discriminator"][
                "allowed_result_branches"
            ],
            "target_result_capability": False,
            "inert_behavior": "Every invocation raises TargetEvaluationNotAuthorized; the module contains no decoder, parser, search, bit-comparison, or satisfiability capability.",
            "later_execution_gate": {
                "separate_post_publication_authorization_required": True,
                "current_task_execution_authorized": False,
                "decoder_import_forbidden": True,
                "target_bit_comparison_forbidden": True,
                "result_classification_forbidden": True,
            },
            "authority": {
                "proof_authority": False,
                "target_result_authority": False,
                "mathematical_result_credit": False,
                "mathematical_saturation_credit": False,
                "p_vs_np_authority": False,
            },
        }
    )
    authorization = seal(
        {
            "schema_version": "1.0.0",
            "authorization_id": "PNP-C050-K15-EVALUATION-AUTHORIZATION-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "evaluator_raw_sha256": EVALUATOR_RAW_SHA256,
            "current_task_evaluator_execution_authorized": False,
            "decoder_access_authorized": False,
            "target_bit_comparison_authorized": False,
            "target_result_access_authorized": False,
            "target_result_classification_authorized": False,
            "allowed_next_action": "COMMIT_PUBLIC_CANDIDATE_AND_INERT_EVALUATOR_FREEZE_ONLY",
            "future_target_work_requires_separate_successor_authorization": True,
            "target_result_state": "H15_INTERSECTION_P16_UNACCESSED_UNDETERMINED",
            "result_access_firewall": candidate["result_access_firewall"],
            "mathematical_result_credit": False,
            "math_ledger_entry_created": False,
        }
    )

    pre_trace = json.loads(Path(PRE_TRACE).read_text(encoding="utf-8"))
    entries = list(pre_trace["entries"])
    event = {
        "event_id": "O9d12a2a1b-C050-E09",
        "atom_id": ATOM_ID,
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": FROZEN_AT,
        "state_summary": "The public source grammar selects k*=15 without target access. The exact H_15 intersection P_16 discriminator and an inert evaluator identity are frozen; no shared target bit, decoder result, or outcome is accessed or predicted.",
        "action_summary": "Freeze the source-only length selector, all length-32 current grammar branches, two-sided result obligations, exact falsifiers, k=12 DifferenceWitness, current framework subject, and result-access firewall.",
        "evidence_pointers": [
            PATHS["candidate"],
            PATHS["manifest"],
            PATHS["authorization"],
            PATHS["framework_binding"],
            PATHS["framework_observation"],
            PRE_GATE,
        ],
        "alternatives_considered": [
            "choose an arbitrary later half-length",
            "adaptively scan a range",
            "reuse the k=12 fixed-bit mismatch",
            "freeze the least source-admissible untouched regime with a two-sided discriminator",
        ],
        "decision_rationale": "The grammar-only selector avoids adaptive multiplicity: length 28 cannot encode canonical UNSAT, length 30 has an explicit v=1,m=3 UNSAT construction, and length 32 has an exhaustively classified nonempty canonical syntax. No overlap coordinate is inspected.",
        "outputs": [
            CANDIDATE_ID,
            candidate["candidate_identity"]["canonical_core_sha256"],
            "K_STAR_15_SOURCE_ONLY_SELECTOR",
            "TWO_SIDED_DISCRIMINATOR_FROZEN",
            "TARGET_RESULT_UNACCESSED_UNDETERMINED",
            "ZERO_RESULT_LEDGER_CREDIT",
        ],
        "uncertainties": [
            "target overlap truth is wholly unchecked",
            "future symbolic branch proofs are not frozen",
            "same-context selector derivation is not independent review",
        ],
        "residuals": [
            "exact H_15 intersection P_16 classification remains open",
            "eight future proof obligations remain unexecuted",
            "cover and complexity bridges remain open",
            "root OPEN",
        ],
        "next_steps": [
            "commit and publish this exact freeze before any target work",
            "obtain a separate successor authorization before importing a target decoder or comparing a shared bit",
            "record either exact witness, scoped impossibility, bounded no-match, or cannot-check without widening scope",
        ],
        "previous_event_hash": entries[-1]["artifact_hash"],
    }
    event["artifact_hash"] = canonical_hash(event)
    entries.append(event)
    trace = {
        "trace_id": "PNP-O9d12a2a1b-C050-K15-CANDIDATE-FREEZE-TRACE-20260812",
        "entries": entries,
    }

    documents = {
        "candidate": candidate,
        "manifest": manifest,
        "authorization": authorization,
        "framework_binding": framework_binding,
        "framework_observation": framework_observation,
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
    receipt = seal(
        {
            "schema_version": "1.0.0",
            "receipt_id": "PNP-C050-K15-CANDIDATE-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"][
                "canonical_core_sha256"
            ],
            "candidate_artifact_hash": candidate["artifact_hash"],
            "frozen_at": FROZEN_AT,
            "chronology": {
                "application_parent_commit": APPLICATION_BASE_SHA,
                "candidate_frozen_after_c050_pre_candidate_gate": True,
                "candidate_publication_status": "TO_BE_COMMITTED_BEFORE_ANY_TARGET_ACCESS",
                "target_decoder_imported_or_executed": False,
                "target_evaluator_imported_or_executed": False,
                "target_overlap_bits_compared": False,
                "target_result_accessed": False,
                "target_result_determined": False,
            },
            "framework_subject": {
                "binding_path": PATHS["framework_binding"],
                "observation_path": PATHS["framework_observation"],
                "framework_sha": FRAMEWORK_SHA,
                "verdict": framework_observation["verdict"],
                "licenses_candidate_materialization": framework_observation[
                    "licenses_candidate_materialization"
                ],
            },
            "full_document_integrity": integrity,
            "full_document_integrity_hash": canonical_hash(integrity),
            "authority": {
                "candidate_is_mathematical_proposal": True,
                "selector_same_context_derivation_frozen": True,
                "target_theorem_truth": False,
                "independent_review": False,
                "mathematical_result_credit": False,
                "mathematical_saturation_credit": False,
                "p_vs_np_authority": False,
                "root_status": "OPEN",
            },
            "math_ledger_entry_created": False,
            "allowed_next_action": "COMMIT_PUBLIC_FREEZE_ONLY; TARGET WORK REQUIRES A SEPARATE SUCCESSOR AUTHORIZATION",
        }
    )
    documents["receipt"] = receipt
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
