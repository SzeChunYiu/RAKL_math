"""Append-only successor for the quarantined RH Abel C001 identity.

C001 remains byte-for-byte historical.  Post-merge review found a malformed
derivative-bound expression and a framework binding to the pre-gate file digest
rather than the frozen mathematical context hash.  Neither defect can be
repaired retroactively.  This fixture records the quarantine, then freezes a
new C002 identity with the corrected expression and binding.  It does not
evaluate either candidate.
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
OLD_CANDIDATE_ID = "RH-ANA-003-ABEL-001-C001-FIXED-N-NATURAL-ORDER-ABEL"
NEW_CANDIDATE_ID = "RH-ANA-003-ABEL-001-C002-FIXED-N-NATURAL-ORDER-ABEL"
REPAIR_BASE_SHA = "6016dd6a87d87b18d8f5498e2537b043a8468c04"
FRAMEWORK_SHA = "d594e6864f49ecf6dac394173082fbf0174b422e"
CONTEXT_PACKET_HASH = "1cefd235555778753fb0731e783ff94cd9b888b941813a5dc00b11e302362f2f"
PRE_GATE_RAW_SHA256 = "8fa0778327c198c7e5e1b3a7e6f9ebdb59735ef067e8545c7f0eb62cb38ff777"
OLD_WRONG_BINDING_VALUE = PRE_GATE_RAW_SHA256
OLD_CANDIDATE_CORE_SHA256 = "sha256:19a265e1498ad67db256c2ef1315a370d2b72107618f67c54fb7b0828eac3bcc"
OLD_CANDIDATE_RAW_SHA256 = "452f69fc29dbc5d1b97c7f966417856debc52b77bf65f4818cfa4716e3f8ee64"
OLD_BINDING_RAW_SHA256 = "9afa7c74c1e38ef633b8343606cd178cbcdfc352f3ab15f1ad6f6208efc11825"
OLD_TRACE_RAW_SHA256 = "6ee14c6153c8c40af0f136850c48c2b0bf627419d54626421f7770501934e050"
REVIEWED_AT = "2026-08-12T07:45:19Z"
BINDING_FROZEN_AT = "2026-08-12T07:48:00Z"
CANDIDATE_FROZEN_AT = "2026-08-12T07:48:10Z"

BASE = "research/real_math/millennium/riemann_hypothesis"
OLD_CANDIDATE = f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_FIXED_N_ABEL_CANDIDATE_FREEZE_20260812.json"
OLD_BINDING = f"{BASE}/09_trace/RH_ANA_003_ABEL_001_CANDIDATE_FRAMEWORK_SUBJECT_FREEZE_20260812.json"
OLD_TRACE = f"{BASE}/09_trace/RH_ANA_003_ABEL_001_CANDIDATE_FREEZE_TRACE_20260812.json"
PRE_GATE = f"{BASE}/09_trace/RH_ANA_003_ABEL_001_PRE_CANDIDATE_GATE_RECEIPT_20260812.json"
CONTEXT = f"{BASE}/01_frontier/RH_ANA_003_ABEL_001_MATH_CONTEXT_FIBER_20260812.json"
EVALUATOR = f"{BASE}/05_oracles/rh_ana003_abel001_inert_evaluator.py"
EVALUATOR_RAW_SHA256 = "b507a4d4555770dadfde5ea943086adc853c138c7caae2e1327b5b54fc471350"

PATHS = {
    "invalidation": f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C001_POSTMERGE_INVALIDATION_20260812.json",
    "candidate": f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_FIXED_N_ABEL_CANDIDATE_FREEZE_20260812.json",
    "proof_inputs": f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_PROOF_INPUT_FREEZE_20260812.json",
    "manifest": f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_INERT_EVALUATOR_FREEZE_20260812.json",
    "authorization": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_EVALUATION_AUTHORIZATION_20260812.json",
    "framework_binding": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_FRAMEWORK_SUBJECT_FREEZE_20260812.json",
    "framework_observation": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_SUCCESSOR_TRACE_20260812.json",
    "receipt": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_CANDIDATE_FREEZE_RECEIPT_20260812.json",
    "lesson": f"{BASE}/07_memory/RH_ANA_003_ABEL_001_C001_C002_MATHEMATICAL_LESSON_20260812.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def raw_hash(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def seal(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = ""
    result["artifact_hash"] = canonical_hash(result)
    return result


def invalidation_document() -> dict:
    return seal({
        "schema_version": "1.0.0",
        "invalidation_id": "RH-ANA-003-ABEL-001-C001-POSTMERGE-INVALIDATION-20260812",
        "atom_id": ATOM,
        "candidate_id": OLD_CANDIDATE_ID,
        "reviewed_at": REVIEWED_AT,
        "review_authority": "POSTMERGE_AUTOMATED_CODE_REVIEW_NOT_INDEPENDENT_MATHEMATICAL_PEER_REVIEW",
        "candidate_status": "QUARANTINED_STRICT_RAKL_IDENTITY_AND_MALFORMED_O2_PROPOSAL",
        "blocking_findings": [
            {
                "finding_id": "C001-B1-MALFORMED-DERIVATIVE-GROWTH-BOUND",
                "exact_original": "C_n(1+log t^(n-1))/t^2",
                "conventional_parse": "C_n(1+(n-1)log t)/t^2",
                "failure": "for n>=3 this does not dominate the actual fixed-n polynomial-log growth (log t)^(n-1)/t^2",
                "correct_successor": "C_n(1+(log t)^(n-1))/t^2",
                "scope": "O2 and every downstream obligation that cites that exact bound",
            },
            {
                "finding_id": "C001-B2-WRONG-FRAMEWORK-PACKET-BINDING",
                "original_binding_value": OLD_WRONG_BINDING_VALUE,
                "original_value_identity": "raw SHA-256 of the pre-candidate gate receipt file",
                "required_context_packet_hash": CONTEXT_PACKET_HASH,
                "failure": "the candidate framework freeze was not bound to the mathematical context packet used by the strict pre-candidate gate",
                "scope": "strict RAKL candidate-materialization chronology for C001",
            },
        ],
        "fail_closed_decision": {
            "original_files_rewritten": False,
            "original_candidate_identity_quarantined": True,
            "retroactive_chronology_repair_claimed": False,
            "may_describe_c001_as_strict_rakl_candidate": False,
            "may_use_c001_for_evaluation": False,
            "new_successor_identity_required": True,
            "reason": "a content-bearing mathematical obligation and its required framework-subject binding were both wrong at C001 freeze time",
        },
        "result_access": {
            "candidate_evaluator_executed": False,
            "candidate_result_accessed": False,
            "proof_result_accessed": False,
        },
        "historical_bindings": {
            "candidate_path": OLD_CANDIDATE,
            "candidate_core_sha256": OLD_CANDIDATE_CORE_SHA256,
            "candidate_raw_sha256": OLD_CANDIDATE_RAW_SHA256,
            "framework_binding_path": OLD_BINDING,
            "framework_binding_raw_sha256": OLD_BINDING_RAW_SHA256,
            "trace_path": OLD_TRACE,
            "trace_raw_sha256": OLD_TRACE_RAW_SHA256,
        },
        "authority": {
            "mathematical_result_credit": False,
            "mathematical_saturation_credit": False,
            "grants_theorem_truth": False,
            "grants_independent_review": False,
            "grants_li_or_rh_authority": False,
            "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
    })


def candidate_document() -> dict:
    old = json.loads(Path(OLD_CANDIDATE).read_text(encoding="utf-8"))
    old.pop("artifact_hash")
    old.pop("candidate_identity")
    core = dict(old)
    core.update({
        "candidate_id": NEW_CANDIDATE_ID,
        "frozen_at": CANDIDATE_FROZEN_AT,
        "successor_lineage": {
            "supersedes_candidate_id": OLD_CANDIDATE_ID,
            "supersedes_core_sha256": OLD_CANDIDATE_CORE_SHA256,
            "supersession_reason": "postmerge review found malformed O2 and invalid framework context binding",
            "predecessor_quarantined": True,
            "predecessor_chronology_repaired_retroactively": False,
            "result_access_before_successor_freeze": False,
        },
    })
    for row in core["proof_obligations"]:
        if row["id"] == "O2-KERNEL-DERIVATIVE":
            row["obligation"] = (
                "derive b_n'(t)=t^(-2)[(L_{n-1}^{(1)})'(log t)-L_{n-1}^{(1)}(log t)] "
                "and prove |b_n'(t)|<=C_n(1+(log t)^(n-1))/t^2 for all t>=1, "
                "where n>=1 is fixed before choosing C_n and taking t to infinity"
            )
    core["source_identity"] = {
        "repair_base_commit": REPAIR_BASE_SHA,
        "valid_pre_candidate_context": {
            "path": CONTEXT,
            "packet_hash": "sha256:" + CONTEXT_PACKET_HASH,
        },
        "pre_candidate_gate": {
            "path": PRE_GATE,
            "raw_sha256": PRE_GATE_RAW_SHA256,
            "note": "file digest is evidence identity only and is not substituted for the context packet hash",
        },
        "predecessor_invalidation": PATHS["invalidation"],
        "corrected_framework_binding": PATHS["framework_binding"],
    }
    core["target_access"] = {
        "proof_evaluator_imported_or_executed": False,
        "finite_identity_checked": False,
        "boundary_checked": False,
        "absolute_divergence_checked": False,
        "result_accessed": False,
    }
    core["credit_boundary"]["candidate_freeze_mathematical_result_credit"] = False
    core["credit_boundary"]["math_ledger_entry_created"] = False
    identity = {
        "candidate_id": NEW_CANDIDATE_ID,
        "canonical_core_sha256": canonical_hash(core),
        "identity_scope": "FULL_C002_CORE_BEFORE_IDENTITY_AND_ARTIFACT_HASH",
    }
    return seal({**core, "candidate_identity": identity})


def framework_documents():
    binding = FrameworkSubjectFreezeBinding(
        binding_id="RH-ANA-003-ABEL-001-C002-FRAMEWORK-FREEZE-20260812",
        authoritative_framework_sha=FRAMEWORK_SHA,
        pre_candidate_packet_hash=CONTEXT_PACKET_HASH,
        frozen_at_utc=BINDING_FROZEN_AT,
        evidence_pointers=(
            f"git:{REPAIR_BASE_SHA}:{CONTEXT}",
            f"git:{REPAIR_BASE_SHA}:{PRE_GATE}",
            f"git:{FRAMEWORK_SHA}:skills/rakl-core/workflows/mathematical-research.md",
            f"git:{FRAMEWORK_SHA}:src/rakl/framework_candidate_freeze.py",
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=FRAMEWORK_SHA,
        intervening_diff=(),
        observation_evidence_pointers=(
            f"git:{FRAMEWORK_SHA}:RAKL_VERSION.json",
            "live RAKL origin/main observed unchanged at C002 binding freeze",
        ),
    )
    report = audit_candidate_freeze_framework_subject(binding, observation, required=True)
    if report.verdict is not CandidateFreezeRevalidationVerdict.CURRENT_UNCHANGED:
        raise RuntimeError(report.reasons)
    return seal({
        **binding.document(),
        "corrects_invalid_predecessor_binding": OLD_BINDING,
        "predecessor_binding_value": OLD_WRONG_BINDING_VALUE,
        "predecessor_chronology_repaired_retroactively": False,
        "applies_only_to_candidate_id": NEW_CANDIDATE_ID,
    }), seal({
        "schema_version": "framework-subject-revalidation-observation-v1",
        "observation_id": "RH-ANA-003-ABEL-001-C002-FRAMEWORK-REVALIDATION-20260812",
        "observed_current_main_sha": observation.observed_current_main_sha,
        "intervening_diff": [],
        "observation_evidence_pointers": list(observation.observation_evidence_pointers),
        "verdict": report.verdict.value,
        "reasons": list(report.reasons),
        "licenses_candidate_materialization": report.licenses_candidate_materialization,
        "grants_scientific_authority": False,
        "applies_only_to_candidate_id": NEW_CANDIDATE_ID,
    })


def lesson_document(candidate: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "unit_id": "MATH-RH-ABEL-C001-C002-PARENTHESIZED-LOG-GROWTH-REPAIR",
        "atom_id": ATOM,
        "candidate_id": NEW_CANDIDATE_ID,
        "attempted_implication": (
            "For each fixed integer n>=1, b_n(t)=L_{n-1}^{(1)}(log t)/t should satisfy "
            "|b_n'(t)|<=C_n(1+(log t)^(n-1))/t^2 for t>=1, so the Bellotti-weighted "
            "Abel boundary and improper integral can be tested without any constant uniform in n."
        ),
        "exact_result_or_failure": (
            "C001 wrote C_n(1+log t^(n-1))/t^2. Under the conventional parse "
            "log(t^(n-1))=(n-1)log t, that envelope grows only linearly in log t. "
            "But (L_{n-1}^{(1)})'(u)-L_{n-1}^{(1)}(u) is a polynomial of degree n-1 "
            "with nonzero leading coefficient, so the written envelope is false for every fixed n>=3. "
            "It happens to have sufficient degree for n=1 and n=2. C002 only freezes the corrected "
            "parenthesized proposal; it does not prove the corrected bound or any Abel conclusion."
        ),
        "supported_and_competing_causes": [
            (
                "supported mathematical cause: operator precedence replaced the required degree-(n-1) "
                "polynomial growth in u=log t by degree-one growth, losing n-2 powers when n>=3"
            ),
            (
                "supported mathematical cause: the leading u^(n-1) term of "
                "(L_{n-1}^{(1)})'(u)-L_{n-1}^{(1)}(u) comes from -L_{n-1}^{(1)}(u) "
                "and cannot be absorbed by a linear-u envelope for n>=3"
            ),
            "competing mathematical cause not selected: Bellotti decay may still be insufficient after multiplication by the corrected derivative envelope",
            "competing mathematical cause not selected: an endpoint convention or sign error may independently invalidate the finite Abel identity",
        ],
        "scope": (
            "The diagnosed failure concerns the derivative-envelope statement for b_n on t>=1, "
            "with n fixed before t tends to infinity. It establishes no n-uniform estimate, "
            "no endpoint identity, no transformed-integral convergence, no natural-order convergence, "
            "no absolute-divergence result, no Li-coefficient sign, and no RH implication."
        ),
        "mathematical_falsifier": (
            "For the corrected proposal, exhibit a fixed n>=1 and a sequence t_k->infinity for which "
            "t_k^2|b_n'(t_k)|/(1+(log t_k)^(n-1)) is unbounded, or derive the exact polynomial "
            "and show that its degree or leading coefficient differs from the frozen Laguerre normalization."
        ),
        "mathematical_repair": (
            "Introduce u=log t, differentiate b_n(t)=L_{n-1}^{(1)}(u)/t explicitly, "
            "and state the envelope as |(L_{n-1}^{(1)})'(u)-L_{n-1}^{(1)}(u)| "
            "<=C_n(1+u^(n-1)) for u>=0. Then substitute u=log t, keeping the quantifier order "
            "for each fixed n, there exists C_n, for all t>=1. Test n=1, n=2, and n=3 separately "
            "before using the asymptotic polynomial-degree argument."
        ),
        "proof_source_evidence": [
            "L_{n-1}^{(1)}(u)=sum_{j=0}^{n-1}(-1)^j binom(n,j+1)u^j/j!",
            "b_n'(t)=t^(-2)[(L_{n-1}^{(1)})'(log t)-L_{n-1}^{(1)}(log t)] by the chain and product rules",
            "the leading coefficient of L_{n-1}^{(1)} is (-1)^(n-1)/(n-1)!, so the derivative difference has the nonzero opposite leading coefficient in degree n-1",
            CONTEXT,
            PATHS["candidate"],
        ],
        "nonmathematical_governance_note": (
            "The separate context-hash identity defect explains why C001 cannot retain strict RAKL chronology, "
            "but hashes, Git history, CI, schemas, and chronology are governance checks and receive zero mathematical lesson credit."
        ),
        "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
        "authority": "SCOPED_SPECIFICATION_FAILURE_LESSON_NO_THEOREM_RESULT_NO_NOVELTY",
        "mathematical_result_credit": False,
        "mathematical_saturation_credit": False,
    })


def trace_document(invalidation: dict, candidate: dict, binding: dict) -> dict:
    old = json.loads(Path(OLD_TRACE).read_text(encoding="utf-8"))
    entries = list(old["entries"])
    events = [
        {
            "event_id": "RH-ANA-003-ABEL-001-E10",
            "event_type": "REVIEWED",
            "timestamp": REVIEWED_AT,
            "state_summary": "Postmerge review found the malformed O2 envelope and wrong framework packet binding; C001 is quarantined without evaluation.",
            "action_summary": "Record both blockers and fail closed on strict chronology.",
            "evidence_pointers": [PATHS["invalidation"], OLD_CANDIDATE, OLD_BINDING, "https://github.com/SzeChunYiu/RAKL_math/pull/349"],
            "alternatives_considered": ["rewrite C001", "declare typo harmless", "append-only quarantine and successor"],
            "decision_rationale": "Both candidate mathematics and strict context identity are content-bearing; neither can be repaired retroactively.",
            "outputs": [invalidation["artifact_hash"], "C001_QUARANTINED", "NO_RESULT_ACCESSED"],
            "uncertainties": ["corrected fixed-n lemma remains unevaluated"],
            "residuals": ["valid successor identity required", "root open"],
            "next_steps": ["freeze a new correctly bound successor before any evaluation"],
        },
        {
            "event_id": "RH-ANA-003-ABEL-001-E11",
            "event_type": "RESIDUAL_OPENED",
            "timestamp": BINDING_FROZEN_AT,
            "state_summary": "The residual is exact: parenthesize the logarithmic power and bind a new candidate to context packet 1cefd235... rather than pre-gate file digest 8fa07783....",
            "action_summary": "Freeze corrected C002 framework-subject binding prospectively.",
            "evidence_pointers": [PATHS["framework_binding"], PATHS["framework_observation"], CONTEXT, PRE_GATE],
            "alternatives_considered": ["reuse invalid C001 binding", "bind receipt file digest again", "bind exact math context packet"],
            "decision_rationale": "The pre-candidate context remains valid and no result was accessed, so a new identity can be prospectively frozen without backfilling C001.",
            "outputs": [binding["artifact_hash"], "C002_BINDING_CURRENT_UNCHANGED"],
            "uncertainties": ["candidate truth remains unchecked"],
            "residuals": ["C002 proposal identity not yet frozen"],
            "next_steps": ["freeze C002 with corrected O2 and inert evaluator"],
        },
        {
            "event_id": "RH-ANA-003-ABEL-001-E12",
            "event_type": "CANDIDATE_PROPOSED",
            "timestamp": CANDIDATE_FROZEN_AT,
            "state_summary": "C002 is a new prospectively bound identity with explicit (log t)^(n-1); all proof obligations remain unevaluated.",
            "action_summary": "Freeze corrected candidate, proof inputs, branches, falsifiers, and inert authorization.",
            "evidence_pointers": [PATHS["candidate"], PATHS["proof_inputs"], PATHS["authorization"], PATHS["framework_binding"], PATHS["receipt"]],
            "alternatives_considered": ["evaluate C001", "evaluate C002 now", "commit C002 freeze before evaluation"],
            "decision_rationale": "New identity plus correct context binding is the only append-only strict path after the two blockers.",
            "outputs": [NEW_CANDIDATE_ID, candidate["candidate_identity"]["canonical_core_sha256"], "FROZEN_UNEVALUATED"],
            "uncertainties": ["every mathematical proof obligation remains unchecked", "same-context repair is not independent review"],
            "residuals": ["fixed-n lemma truth open", "Li and RH bridges open"],
            "next_steps": ["publish exact C002 freeze", "require separate successor authorization before evaluation"],
        },
    ]
    previous = entries[-1]["artifact_hash"]
    for event in events:
        event.update({"atom_id": ATOM, "previous_event_hash": previous})
        event["artifact_hash"] = canonical_hash(event)
        entries.append(event)
        previous = event["artifact_hash"]
    return {"trace_id": "RH-ANA-003-ABEL-001-C002-SUCCESSOR-TRACE-20260812", "entries": entries}


def build_documents() -> dict[str, dict]:
    if raw_hash(OLD_CANDIDATE) != OLD_CANDIDATE_RAW_SHA256:
        raise RuntimeError("C001 candidate history changed")
    if raw_hash(OLD_BINDING) != OLD_BINDING_RAW_SHA256:
        raise RuntimeError("C001 binding history changed")
    if raw_hash(OLD_TRACE) != OLD_TRACE_RAW_SHA256:
        raise RuntimeError("C001 trace history changed")
    invalidation = invalidation_document()
    candidate = candidate_document()
    binding, observation = framework_documents()
    lesson = lesson_document(candidate)
    proof_inputs = seal({
        "schema_version": "1.0.0",
        "proof_input_id": "RH-ANA-003-ABEL-001-C002-PROOF-INPUT-FREEZE-20260812",
        "candidate_id": NEW_CANDIDATE_ID,
        "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
        "frozen_at": CANDIDATE_FROZEN_AT,
        "proof_obligations": candidate["proof_obligations"],
        "allowed_result_branches": candidate["allowed_result_branches"],
        "status": "FROZEN_UNEVALUATED",
        "evaluation_authorized": False,
        "mathematical_result_credit": False,
    })
    manifest = seal({
        "schema_version": "1.0.0",
        "manifest_id": "RH-ANA-003-ABEL-001-C002-INERT-EVALUATOR-FREEZE-20260812",
        "candidate_id": NEW_CANDIDATE_ID,
        "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
        "evaluator": {"path": EVALUATOR, "raw_sha256": EVALUATOR_RAW_SHA256},
        "status": "FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED",
        "current_round_execution_authorized": False,
        "predecessor_candidate_execution_forbidden": True,
        "authority": {"proof_authority": False, "mathematical_result_credit": False, "li_or_rh_authority": False},
    })
    authorization = seal({
        "schema_version": "1.0.0",
        "authorization_id": "RH-ANA-003-ABEL-001-C002-EVALUATION-AUTHORIZATION-20260812",
        "candidate_id": NEW_CANDIDATE_ID,
        "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
        "current_round_evaluator_execution_authorized": False,
        "proof_derivation_authorized": False,
        "result_classification_authorized": False,
        "allowed_next_action": "COMMIT_PUBLIC_C002_FREEZE_ONLY",
        "future_work_requires_separate_successor_authorization": True,
        "result_state": "UNEVALUATED",
        "mathematical_result_credit": False,
    })
    trace = trace_document(invalidation, candidate, binding)
    documents = {
        "invalidation": invalidation,
        "candidate": candidate,
        "proof_inputs": proof_inputs,
        "manifest": manifest,
        "authorization": authorization,
        "framework_binding": binding,
        "framework_observation": observation,
        "trace": trace,
        "lesson": lesson,
    }
    integrity = {
        "algorithm": "SHA-256",
        "canonicalization": "JSON_SORT_KEYS_COMPACT_UTF8",
        "json_inputs": {name: {"path": PATHS[name], "canonical_sha256": canonical_hash(doc)} for name, doc in sorted(documents.items())},
        "historical_inputs": {
            "old_candidate": {"path": OLD_CANDIDATE, "raw_sha256": OLD_CANDIDATE_RAW_SHA256},
            "old_binding": {"path": OLD_BINDING, "raw_sha256": OLD_BINDING_RAW_SHA256},
            "old_trace": {"path": OLD_TRACE, "raw_sha256": OLD_TRACE_RAW_SHA256},
            "pre_gate": {"path": PRE_GATE, "raw_sha256": PRE_GATE_RAW_SHA256},
            "context": {"path": CONTEXT, "packet_hash": "sha256:" + CONTEXT_PACKET_HASH},
        },
    }
    documents["receipt"] = seal({
        "schema_version": "1.0.0",
        "receipt_id": "RH-ANA-003-ABEL-001-C002-CANDIDATE-FREEZE-20260812",
        "candidate_id": NEW_CANDIDATE_ID,
        "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
        "candidate_artifact_hash": candidate["artifact_hash"],
        "frozen_at": CANDIDATE_FROZEN_AT,
        "predecessor": {
            "candidate_id": OLD_CANDIDATE_ID,
            "status": "QUARANTINED",
            "strict_chronology_repaired_retroactively": False,
            "invalidation_path": PATHS["invalidation"],
        },
        "corrected_binding": {
            "context_packet_hash": CONTEXT_PACKET_HASH,
            "binding_path": PATHS["framework_binding"],
            "framework_sha": FRAMEWORK_SHA,
            "verdict": observation["verdict"],
            "licenses_candidate_materialization": observation["licenses_candidate_materialization"],
        },
        "chronology": {
            "repair_base_commit": REPAIR_BASE_SHA,
            "review_precedes_binding": True,
            "binding_precedes_candidate": True,
            "candidate_evaluator_imported_or_executed": False,
            "candidate_result_accessed": False,
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
        "allowed_next_action": "COMMIT_PUBLIC_C002_FREEZE_ONLY; EVALUATION REQUIRES SEPARATE SUCCESSOR AUTHORIZATION",
    })
    return documents


def write_documents(root: Path = Path(".")) -> None:
    for name, document in build_documents().items():
        path = root / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_documents()
