"""Serialize the authorized public C052 k31 overlap result and lessons."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
DISCRIMINATOR = PNP / "04_candidates/c052_k31_overlap_discriminator.py"
FALSIFIER = PNP / "05_falsification/c052_k31_overlap_independent_falsifier.py"
NEGATIVE = PNP / "04_candidates/O9d12a2a1b_C052_K31_OVERLAP_NEGATIVE_CERTIFICATE_20260812.json"
CHECK = PNP / "05_falsification/O9d12a2a1b_C052_K31_OVERLAP_INDEPENDENT_CHECK_RESULT_20260812.json"
FAILURE = PNP / "07_memory/O9d12a2a1b_C052_K31_OVERLAP_FAILURE_EXPERIENCE_20260812.json"
LESSON = PNP / "07_memory/O9d12a2a1b_C052_K31_OVERLAP_MATHEMATICAL_LESSON_20260812.json"
REVIEW = PNP / "08_reviews/O9d12a2a1b_C052_K31_OVERLAP_SAME_CONTEXT_REVIEW_20260812.json"
RECEIPT = PNP / "09_trace/O9d12a2a1b_C052_K31_OVERLAP_RESULT_RECEIPT_20260812.json"

BASE_SHA = "8bfc825dd3fdf28a8914811d588102d8e6fd84ca"
AUTH_HASH = "sha256:036b653fcdc1e47a1b5361c017cd2d483e84632d37e07b8fa682741219ef17eb"
E09_HASH = "sha256:ed3015be353c6ca8aadf07f1900608682f4de1bb35d32d309cac80948ab642d3"


def digest(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def seal(document: dict) -> dict:
    core = dict(document)
    core.pop("artifact_hash", None)
    core["artifact_hash"] = digest(json.dumps(core, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    return core


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build() -> tuple[dict, ...]:
    candidate_result = load_module("k31_discriminator", DISCRIMINATOR).evaluate_public_k31()
    independent = load_module("k31_falsifier", FALSIFIER).run()
    if candidate_result["branch"] != "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE":
        raise RuntimeError("candidate result did not take frozen negative branch")
    if independent["actual_branch"] != candidate_result["branch"] or not independent["worlds_all_pass"] or not independent["integration_all_pass"]:
        raise RuntimeError("independent public checks disagree")

    negative = seal({
        "schema_version": "1.0.0",
        "certificate_id": candidate_result["certificate"]["certificate_id"],
        "candidate_id": "PNP-C052-K31-TARGET-BLIND-OVERLAP-CERTIFICATE-DISCRIMINATOR-v1",
        "branch": candidate_result["branch"],
        "proof_kind": "UNIVERSAL_CANONICAL_SYNTAX_SEPARATOR_WITH_EXHAUSTIVE_PUBLIC_CORROBORATION",
        "symbolic_proof": candidate_result["certificate"]["symbolic_steps"],
        "parent_cell": candidate_result["certificate"]["parent_cell"],
        "current_cells": candidate_result["certificate"]["current_cells"],
        "negative_obligations": candidate_result["certificate"]["negative_obligations"],
        "symbolic_separator_valid": candidate_result["certificate"]["symbolic_separator_valid"],
        "all_public_prefix_rows_separated": candidate_result["certificate"]["all_public_prefix_rows_separated"],
        "public_enumeration_rows": candidate_result["certificate"]["public_enumeration_rows"],
        "public_unique_prefixes_checked_with_multiplicity_by_v": candidate_result["certificate"]["public_unique_prefixes_checked_with_multiplicity_by_v"],
        "exact_result": "H_31 intersection P_32 is empty: every current prefix either has p[31]=1 while every H_31 label has h[31]=0, or has p[31]=0 and p[7:10]=100, which would map to an illegal parent variable code 00.",
        "proof_boundary": "The symbolic dichotomy is the proof; enumeration corroborates complete public support and does not create proof authority.",
        "hidden_or_native_executed": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    check = seal({
        "schema_version": "1.0.0",
        "check_id": "PNP-C052-K31-OVERLAP-INDEPENDENT-CHECK-20260812",
        "discriminator_raw_sha256": digest(DISCRIMINATOR.read_bytes()),
        "falsifier_raw_sha256": digest(FALSIFIER.read_bytes()),
        "candidate_branch": candidate_result["branch"],
        "independent_branch": independent["actual_branch"],
        "world_results": independent["world_results"],
        "worlds_all_pass": independent["worlds_all_pass"],
        "integration": independent["integration"],
        "integration_all_pass": independent["integration_all_pass"],
        "independently_rederived_source_binding_valid": independent["source_binding_valid"],
        "independent_current_support": [list(row) for row in independent["current_support"]],
        "independent_per_v_exhaustion": independent["per_v_exhaustion"],
        "negative_certificate_artifact_hash": negative["artifact_hash"],
        "authority": independent["authority"],
        "computation_authority": "CORROBORATION_ONLY_NOT_PROOF",
        "hidden_or_native_executed": False,
    })
    failure = seal({
        "schema_version": "1.0.0",
        "failure_id": "F-PNP-C052-K31-ACTUAL-OVERLAP-EMPTY-BY-SYNTAX-DICHOTOMY",
        "atom_id": "O9d12a2a1b-C052-K31-OVERLAP",
        "candidate_id": "PNP-C052-K31-TARGET-BLIND-OVERLAP-CERTIFICATE-DISCRIMINATOR-v1",
        "method_family": "off-window local obstruction escape followed by exact literal-transpose overlap",
        "observed_result": "H_31 intersection P_32 is empty despite removal of every forced-MAGIC obstruction among h[0..7].",
        "failure_mode": "a boundary-pad/current-payload dichotomy plus an illegal mapped parent token separates every full label",
        "mathematical_classification": "SCOPED_STRUCTURAL_LEMMA_AND_FAILED_LOCAL_TO_GLOBAL_IMPLICATION",
        "failed_implication": "Coordinate-wise removal of the old h[0..7] forced-MAGIC separator does not imply removal of every whole-label separator.",
        "residual_signature": ["marginal local escape", "full-word boundary obstruction", "p31 or token-100 separator", "exact bounded disjointness"],
        "selected_diagnosis": "The local h[0..7] obstruction was removed, but full 32-bit equality exposes two later canonical constraints: parent padding at h31 and parent token legality at h7..h9.",
        "diagnosis_status": "PROVED_EXACT_K31_SCOPE",
        "competing_diagnoses": ["H_31 is empty", "current support omitted", "UNSAT semantics causes separation", "marginal theorem implies overlap"],
        "broken_assumptions": ["coordinate-wise local variation composes into a common full label", "removing the first known separator removes all canonical separators"],
        "scope_conditions": ["k=31", "unchanged C041 canonical encoding", "unchanged C048 literal transpose", "exact parent/current support cells only"],
        "evidence_pointers": [str(NEGATIVE.relative_to(ROOT)), str(CHECK.relative_to(ROOT))],
        "local_repair_attempts": ["proved off-window marginal lemma", "tested exact full-label certificate rather than extrapolating marginals"],
        "verified_impossibility_scope": "H_31 intersection P_32 only",
        "warning_not_blacklist": "Future k or changed structural coordinates require a DifferenceWitness; this k31 result does not block them universally.",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    lesson = seal({
        "schema_version": "1.0.0",
        "lesson_id": "MATH-PNP-C052-K31-FULL-WORD-SEPARATOR-20260812",
        "failure_artifact_hash": failure["artifact_hash"],
        "seven_field_mathematical_lesson": {
            "attempted_implication": "Removing every local forced-MAGIC coordinate obstruction among h[0..7] at the least supported off-window cell might permit an actual H_31/P_32 common label.",
            "exact_result_or_failure": "It does not. H_31 intersection P_32 is empty by a two-case universal syntax separator: p31=1 conflicts with parent pad h31=0; otherwise the a+=4 or 6 header forces p[7:10]=100, mapping to illegal parent index 00.",
            "supported_and_competing_causes": "Supported cause is full-word canonical boundary/token legality. H_31 emptiness, missing current support, UNSAT semantics, and the old h0..h7 forced-MAGIC cause are excluded.",
            "scope": "Exact k31, parent (a,b,m)=(2,3,5), all three exact length64 current cells, unchanged C041/C048. No general-k, cover, circuit, or P-vs-NP implication.",
            "mathematical_falsifier": "One exact common label with a canonical UNSAT parent and canonical current word, or one current prefix outside both separator cases, refutes the certificate.",
            "repair_or_next_discriminator": "Before moving to another k, classify full-word boundary coordinates and mapped token legality—not only the first eight MAGIC coordinates—and require a DifferenceWitness showing both k31 separators disappear.",
            "proof_and_source_evidence": "Five-step symbolic separator proof, exact support equations, and independently reimplemented public enumeration across 82928 unique prefixes counted per v. Computation corroborates rather than proves.",
        },
        "reusable_mathematical_lessons": [
            {
                "lesson": "Quantifier order is load-bearing: forall coordinates there exists a witness is weaker than existence of one witness satisfying all coordinate demands.",
                "authority": "PROVED_IN_EXACT_K31_SCOPE",
                "scope": "The off-window marginals versus the exact H_31/P_32 intersection.",
                "validation": "A proposed transfer must display one common full label, not a family of coordinate witnesses.",
            },
            {
                "lesson": "Removing a known local coordinate separator is not monotone evidence that the two full constrained languages now intersect.",
                "authority": "PROVED_IN_EXACT_K31_SCOPE",
                "scope": "The failed implication from local h[0..7] variability to full 32-bit overlap.",
                "validation": "Search the remaining coordinates and block constraints for a universal separator before any overlap claim.",
            },
            {
                "lesson": "Canonical parity padding can become a fixed suffix invariant after an equal split and can separate a later prefix endpoint.",
                "authority": "PROVED_IN_EXACT_K31_SCOPE",
                "scope": "Parent raw length 61 gives x[61]=h[31]=0, excluding the current a+=1 cell.",
                "validation": "For a successor k, rederive raw length, padding, split position, and the matching current endpoint bit.",
            },
            {
                "lesson": "Token legality is a block constraint invisible to single-coordinate marginal checks: the shared block 100 decodes to forbidden variable zero.",
                "authority": "PROVED_IN_EXACT_K31_SCOPE",
                "scope": "Current a+ in {4,6}, where p[7:10]=100 maps to parent payload token 7.",
                "validation": "Map every shared bit block back to exact token phase and test the whole legal alphabet.",
            },
            {
                "lesson": "A syntactic superset separator can prove semantic-language disjointness without classifying which parent formulas are UNSAT.",
                "authority": "PROVED_IN_EXACT_K31_SCOPE",
                "scope": "All canonical parent words in the unique length-62 cell are separated, hence their UNSAT subset H_31 is separated.",
                "validation": "Prove the superset inclusion and universal separator; never replace semantic membership in a positive certificate.",
            },
            {
                "lesson": "Exact support equations can reduce a large word-language question to a finite symbolic case partition before enumeration.",
                "authority": "PROVED_IN_EXACT_K31_SCOPE",
                "scope": "The three length-64 cells split into a+=1 versus a+ in {4,6}.",
                "validation": "Prove support-cell exhaustiveness algebraically before using the case split.",
            },
            {
                "lesson": "A later-k retry needs a structural DifferenceWitness showing both the pad-endpoint and mapped-token separators disappear or are repaired.",
                "authority": "SEARCH_HEURISTIC",
                "scope": "Successors of this exact literal-transpose overlap route only.",
                "validation": "The cheapest falsifier recomputes boundary phase and token legality before constructing or testing formulas.",
            },
        ],
        "framework_feedback_boundary": "This is a mathematical search lesson: widen obstruction fingerprints from local comparison windows to all canonical boundary/token phases before claiming escape.",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    review = seal({
        "schema_version": "1.0.0",
        "review_id": "PNP-C052-K31-OVERLAP-SAME-CONTEXT-REVIEW-20260812",
        "negative_certificate_artifact_hash": negative["artifact_hash"],
        "check_artifact_hash": check["artifact_hash"],
        "role_reviews": {
            "domain_theory": "The separator applies to all exact support cells and does not depend on H_31 emptiness.",
            "adversarial_falsification": "The two cases exhaust every current prefix by p31; in the p31=0 case only a+=4/6 exist and both have p7..p9=100.",
            "formal_methods": "The h-to-parent coordinate mapping h[j]=x[30+j] makes h7..h9 exactly parent payload token 7; 00 is illegal for v=2 or 3.",
            "analogy_transfer": "Marginal protocol fields fail to compose into a whole message, but the analogy supplies no authority.",
            "research_value": "The result identifies a later full-word obstruction and a better next-screening coordinate; it is not a lower bound.",
        },
        "strongest_objection": "Could a current a+=1 prefix have p31=0? No: its first32 endpoint is the index bit of the eighth literal, and v+=1 forces code 1.",
        "blocking_concerns": [],
        "verdict": "EXACT_K31_EMPTY_RESULT_SURVIVES_SAME_CONTEXT_REVIEW",
        "review_boundary": "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
    })
    e10 = seal({
        "event_id": "O9d12a2a1b-C052-K31-OVERLAP-E10", "atom_id": "O9d12a2a1b-C052-K31-OVERLAP", "event_type": "FALSIFIER_RUN",
        "timestamp": "2026-08-12T15:18:29Z", "state_summary": "All public conformance/integration worlds pass and independent implementation agrees on the negative branch.",
        "action_summary": "Run authorized public worlds and exact k31 discriminator/falsifier only.", "evidence_pointers": [str(CHECK.relative_to(ROOT))],
        "outputs": [check["artifact_hash"], "PUBLIC_WORLDS_PASS", "NO_HIDDEN_OR_NATIVE"], "previous_event_hash": E09_HASH,
        "residuals": ["record exact branch", "root open"], "next_steps": ["record only the source-bound result"],
    })
    e11 = seal({
        "event_id": "O9d12a2a1b-C052-K31-OVERLAP-E11", "atom_id": "O9d12a2a1b-C052-K31-OVERLAP", "event_type": "RESULT_RECORDED",
        "timestamp": "2026-08-12T15:18:30Z", "state_summary": "H_31 intersection P_32 is empty in exact scope by a universal syntax separator.",
        "action_summary": "Record EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE and open the full-word-boundary residual.",
        "evidence_pointers": [str(NEGATIVE.relative_to(ROOT)), str(FAILURE.relative_to(ROOT)), str(LESSON.relative_to(ROOT))],
        "outputs": [negative["artifact_hash"], failure["artifact_hash"], "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE", "OPEN_NO_SOLUTION_CERTIFICATE"],
        "previous_event_hash": e10["artifact_hash"], "residuals": ["later-k route requires DifferenceWitness", "root open"],
        "next_steps": ["assimilate full-word boundary/token-phase lesson before any successor candidate"],
    })
    receipt = seal({
        "schema_version": "1.0.0", "result_id": "PNP-C052-K31-OVERLAP-RESULT-20260812", "application_base_sha": BASE_SHA,
        "authorization_artifact_hash": AUTH_HASH, "result_branch": candidate_result["branch"],
        "exact_mathematical_result": negative["exact_result"], "negative_certificate_artifact_hash": negative["artifact_hash"],
        "independent_check_artifact_hash": check["artifact_hash"], "failure_artifact_hash": failure["artifact_hash"],
        "lesson_artifact_hash": lesson["artifact_hash"], "same_context_review_artifact_hash": review["artifact_hash"],
        "implementation_hashes": {"candidate": digest(DISCRIMINATOR.read_bytes()), "independent_falsifier": digest(FALSIFIER.read_bytes())},
        "public_trace_deltas": [e10, e11], "hidden_or_native_executed": False,
        "mathematical_credit": ["exact k31 universal syntax-separation proof", "exhaustive parent/current support binding"],
        "zero_credit": ["Git/CI/hashes", "computation as proof", "independent peer review", "general-k/cover/circuit/P-vs-NP claims"],
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    return negative, check, failure, lesson, review, receipt


def write() -> tuple[dict, ...]:
    documents = build()
    for path, document in zip((NEGATIVE, CHECK, FAILURE, LESSON, REVIEW, RECEIPT), documents):
        path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return documents


if __name__ == "__main__":
    write()
