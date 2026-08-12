"""Freeze the C053 k32 clean-phase candidate, proof plan, and falsifiers.

This module is intentionally inert.  It records exact mathematical
obligations for the 32 parameter pairs in the phase
``(a,m)=(4,3) -> (a+,m+)=(3,4)`` but never enumerates formula payloads,
decodes a formula, invokes SAT, compares a parent suffix with a current
prefix, or selects a result branch.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = "research/real_math/millennium/p_vs_np"
PNP = ROOT / BASE

CANDIDATE_OUT = PNP / "04_candidates/O9d12a2a1b_C053_K32_CLEAN_PHASE_COMPATIBILITY_IDENTITY_20260812.json"
EVALUATOR_OUT = PNP / "05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATOR_IDENTITY_20260812.json"
FALSIFIER_OUT = PNP / "05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_FALSIFIER_IDENTITY_20260812.json"
RECEIPT_OUT = PNP / "09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_CANDIDATE_FREEZE_RECEIPT_20260812.json"

APPLICATION_BASE_SHA = "47fcc8f71f5d4801b3c337d50c3b17bb6b8a648d"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
CANDIDATE_ID = "PNP-C053-K32-CLEAN-PHASE-FULL-WORD-COMPATIBILITY-v1"
EVALUATOR_ID = "PNP-C053-K32-CLEAN-PHASE-SOURCE-BOUND-EVALUATOR-v1"
FALSIFIER_ID = "PNP-C053-K32-CLEAN-PHASE-FALSIFIER-v1"
CANDIDATE_FROZEN_AT = "2026-08-12T16:31:00Z"
EVALUATOR_FROZEN_AT = "2026-08-12T16:31:01Z"
FALSIFIER_FROZEN_AT = "2026-08-12T16:31:02Z"
RECEIPT_FROZEN_AT = "2026-08-12T16:31:03Z"
PREVIOUS_EVENT_HASH = "sha256:56d1be41dc0ad67f65e8ac4e2e65c9ff95afea4d39f342a304b549961f13052d"

SOURCE_BINDINGS = {
    "context": {
        "path": f"{BASE}/01_frontier/O9d12a2a1b_C053_K32_PHASE_SCREEN_CONTEXT_20260812.json",
        "raw_sha256": "sha256:cd5a2292812a46fc21c7c20b5c0eae92f8607b92cdbd3b2569868aa5cf4fadac",
        "artifact_hash": "sha256:1f3e30329dd73f447b3963756edee0b338a6abaa8ffab39495a65476d0624b23",
        "git_blob": "4ae9414b1a6ed0b52be5f3a1271f272410b0aedd",
    },
    "structural_lemma": {
        "path": f"{BASE}/03_routes/O9d12a2a1b_C053_K32_PHASE_SCREEN_STRUCTURAL_LEMMA_20260812.json",
        "raw_sha256": "sha256:614724d6113c017ca3f2e57bf4a86b4df780c556ba488a93f6ea365db6981a01",
        "artifact_hash": "sha256:cb84056f781529860033575b18f545d323b51fd733b704a8d6762661da26b694",
        "git_blob": "4f53699945114a7dbd658319a20e10a8e591b559",
    },
    "memory_review": {
        "path": f"{BASE}/07_memory/O9d12a2a1b_C053_K32_PHASE_SCREEN_RESEARCH_MEMORY_REVIEW_20260812.json",
        "raw_sha256": "sha256:db76b3493245d250227ea6a934c40a1f1065474abe1c80cf5759441e8da14138",
        "artifact_hash": "sha256:2604d66f59996dcf40f3e38b6b16c55f6e054bb91650aa7dbda69172d0aab902",
        "git_blob": "e86855638fd363426c771241cf2f1ff1ca990c9b",
    },
    "shortcut_review": {
        "path": f"{BASE}/08_reviews/O9d12a2a1b_C053_K32_PHASE_SCREEN_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
        "raw_sha256": "sha256:22b2d704aed109557163e97dd06c4baa1dc86fa8532d4edabb2e00dcbdf95009",
        "artifact_hash": "sha256:77289fe8fc64137e3f1f08aae3e9f231bc67c42ee3954202f1c1c7802848bb8f",
        "git_blob": "10c67a542bb636656da8908eb69d70dbb2199bb3",
    },
    "pre_candidate_trace": {
        "path": f"{BASE}/09_trace/O9d12a2a1b_C053_K32_PHASE_SCREEN_PRE_CANDIDATE_TRACE_20260812.json",
        "raw_sha256": "sha256:e6263a6d60675c27a2da7cf050c2e7e11e48081bdfb04253505050b4419b9340",
        "last_event_id": "O9d12a2a1b-C053-K32-PHASE-SCREEN-E08",
        "last_event_hash": PREVIOUS_EVENT_HASH,
        "git_blob": "4a95c6a67f04d89effc736346341e62438c9a281",
    },
    "pre_candidate_gate": {
        "path": f"{BASE}/09_trace/O9d12a2a1b_C053_K32_PHASE_SCREEN_PRE_CANDIDATE_GATE_20260812.json",
        "raw_sha256": "sha256:da62e782f32c66ab480b7fcd4e01ee828077f7b99f270bfd7874f3ab7964fab0",
        "artifact_hash": "sha256:36b088e410c8e9a4aa863f40b454dee5bd77bdba719a4c07ced0ed85f6aae813",
        "git_blob": "00738e383668158ba7448f41dbaa80cf210a5ced",
    },
    "next_discriminator": {
        "path": f"{BASE}/09_trace/O9d12a2a1b_C053_K32_NEXT_DISCRIMINATOR_PROPOSAL_20260812.json",
        "raw_sha256": "sha256:2f6efa473c83250ddc4222841a8ed47eed9ef0eb917c672d70cf5b73c93db99b",
        "artifact_hash": "sha256:82e6847847ce3f1dafaa2191b17cc26abe0af040e46431c9b8ace5ab90511bb6",
        "git_blob": "5e76fa10c1c53c721a9def6cc6263ccd668d519a",
    },
    "mathematical_lesson": {
        "path": f"{BASE}/07_memory/O9d12a2a1b_C053_K32_PHASE_SCREEN_MATHEMATICAL_LESSON_20260812.json",
        "raw_sha256": "sha256:180f4857280c352a88698afa8a7d60e89b52a0de690bbe997a5b69f6610a4bb5",
        "artifact_hash": "sha256:3fdb26761ff17578299c7a23e9f53824d18f6ed5d2b61be462ef4e8b0b66b044",
        "git_blob": "74d1e708b4c73840f91c94a3b27ea659f8dbfc0f",
    },
    "c041_grammar": {
        "path": f"{BASE}/04_candidates/C041_fx_sat_one_sided.py",
        "raw_sha256": "sha256:c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a",
        "git_blob": "fcc4814dd618da96ef9bb8144a4783a0a6e886e1",
    },
    "c048_transfer_condition": {
        "path": f"{BASE}/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_TRANSFER_CONDITION_FREEZE_20260812.json",
        "raw_sha256": "sha256:e2a924e708c1ab17b78e06a3935fd48772c0c172b9f01b0c756de80f1430908b",
        "artifact_hash": "sha256:b03a1090e7b25222dc2377e309b8600b6e2064d6fc74f702b1f3f984d68cff5e",
        "git_blob": "fed9057163bec46325115e8f6cfbb5c6f3c3d485",
    },
}


def digest(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def seal(document: dict) -> dict:
    core = dict(document)
    core.pop("artifact_hash", None)
    core["artifact_hash"] = digest(
        json.dumps(core, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    )
    return core


def assert_sources() -> None:
    for binding in SOURCE_BINDINGS.values():
        path = ROOT / binding["path"]
        if digest(path.read_bytes()) != binding["raw_sha256"]:
            raise RuntimeError(f"bound source moved: {binding['path']}")
        if "artifact_hash" in binding:
            document = json.loads(path.read_text(encoding="utf-8"))
            actual = document.get("artifact_hash", document.get("packet_hash"))
            if actual != binding["artifact_hash"]:
                raise RuntimeError(f"bound content moved: {binding['path']}")
    trace = json.loads((ROOT / SOURCE_BINDINGS["pre_candidate_trace"]["path"]).read_text(encoding="utf-8"))
    if trace["entries"][-1]["artifact_hash"] != PREVIOUS_EVENT_HASH:
        raise RuntimeError("pre-candidate trace tip moved")


def candidate_identity() -> dict:
    parameter_pairs = [
        {"parent_v": parent_v, "current_v": current_v}
        for parent_v in range(8, 16)
        for current_v in range(4, 8)
    ]
    return seal({
        "schema_version": "1.0.0",
        "candidate_id": CANDIDATE_ID,
        "atom_id": "O9d12a2a1b-C053-K32-CLEAN-PHASE-COMPATIBILITY",
        "candidate_kind": "INERT_EXACT_32_PAIR_FULL_WORD_COMPATIBILITY_DISCRIMINATOR",
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_pin": FRAMEWORK_SHA,
        "frozen_at_utc": CANDIDATE_FROZEN_AT,
        "source_bindings": SOURCE_BINDINGS,
        "qoi": "For exactly parent (a,m)=(4,3), v in 8..15 and current (a,m)=(3,4), v+ in 4..7 at k=32, decide whether any canonical UNSAT parent suffix equals any canonical current 33-bit prefix.",
        "exact_phase": {
            "k": 32,
            "parent": {"a": 4, "m": 3, "v_range": [8, 15], "width": 5, "header_length": 18, "raw_length": 63, "encoded_length": 64, "padding": 1},
            "current": {"a": 3, "m": 4, "v_range": [4, 7], "width": 4, "header_length": 18, "raw_length": 66, "encoded_length": 66, "padding": 0},
            "parameter_pairs": parameter_pairs,
            "parameter_pair_count": 32,
        },
        "full_word_definitions": {
            "parent_word": "x=MAGIC||gamma(v)||gamma(3)||nine signed width-5 literal tokens||0, with each variable code in 1..v",
            "parent_split": "x=r||c with |r|=|c|=32; h=1||c has length 33",
            "parent_language": "h belongs to H_32 iff x is canonical in the exact parent phase and Dec(x) is UNSAT",
            "current_word": "y=MAGIC||gamma(v+)||gamma(4)||twelve signed width-4 literal tokens, with each variable code in 1..v+",
            "current_prefix": "p is the first 33 bits of y",
            "compatibility": "h=p byte-for-byte in all 33 positions",
        },
        "full_word_compatibility_obligations": [
            "W1 rederive the exact C041 source identity and the two support cells without importing candidate verdicts",
            "W2 quantify all 8*4=32 parameter pairs (v,v+) in {8,...,15}x{4,...,7}, with no data-dependent pair selection",
            "W3 enforce every parent field boundary, gamma code, sign bit, width-5 variable code in 1..v, clause boundary, and the final zero padding bit",
            "W4 enforce every current field boundary, gamma code, sign bit, width-4 variable code in 1..v+, and clause boundary through the first 33 bits",
            "W5 derive the exact coordinate equation h[0]=1 and h[j]=x[31+j] for 1<=j<=32, then impose all 33 equalities h[j]=p[j]",
            "W6 screen every complete mapped parent token and every cross-boundary partial block induced by the equality; the three known legal header tokens are necessary conditions only",
            "W7 for a positive branch exhibit x,y,r,c,h,p and independent canonical decodes, prove Dec(x) UNSAT, and verify h=p in all 33 positions",
            "W8 for a negative branch give a hand-checkable universal contradiction covering all 32 parameter pairs and all legal literal choices, or an exhaustive proof-producing search with a separately justified completeness theorem",
            "W9 return CANNOT_CHECK if UNSAT proof, coverage, canonicality, equality, source identity, or proof trust is incomplete or conflicting",
        ],
        "hand_proof_plan": [
            "P1 write the 33 coordinate equalities with both field-boundary tables before substituting any literal value",
            "P2 partition coordinates into complete aligned tokens, partial tokens crossing the split, and variable payload coordinates",
            "P3 propagate gamma/header and padding constraints symbolically for each of the 32 parameter pairs",
            "P4 derive any forced sign/variable-code relation and test it against the exact legal ranges 1..v and 1..v+",
            "P5 if syntax remains compatible, reconstruct the parent and current formulas and separate the semantic parent-UNSAT obligation from mere canonicality",
            "P6 seek a short universal contradiction first; otherwise state precisely what exhaustive completeness argument is still owed",
            "P7 use computation only as corroboration after the mathematical certificate is written",
        ],
        "allowed_branches": [
            "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS",
            "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF",
            "CANNOT_CHECK",
        ],
        "branch_contract": {
            "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS": "W1-W7 pass for at least one of the 32 frozen parameter pairs and no valid universal negative certificate conflicts",
            "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF": "W1-W6 and W8 pass for every one of the 32 frozen parameter pairs and no valid positive witness conflicts",
            "CANNOT_CHECK": "otherwise, including syntax-only survival, SAT without UNSAT proof, partial equality, incomplete pair coverage, source mismatch, ambiguity, or conflicting certificates",
        },
        "evaluation_authorized": False,
        "implementation": None,
        "result_state": "UNEVALUATED",
        "forbidden_scope": [
            "the other clean (6,2)->(3,4) phase",
            "the partial (6,2)->(11,1) phase",
            "global H_32 intersection P_33",
            "any k outside this frozen phase",
            "cover growth, circuits, novelty, P versus NP, or Millennium-root promotion",
        ],
        "mathematical_lesson": {
            "attempted_implication": "Survival of both known k31 syntax separators in all 32 parameter pairs may leave at least one full canonical parent/current word pair with equal 33-bit label and an UNSAT parent.",
            "exact_theorem_or_failure": "UNEVALUATED: this round proves no compatibility or incompatibility theorem; it freezes the exact full-word proposition and proof obligations.",
            "supported_and_competing_mathematical_causes": "Supported motivation is clean survival of endpoint and complete fixed-header-token separators. Competing obstructions are a different forced coordinate, partial-token inconsistency, clause-boundary incompatibility, or absence of an UNSAT parent among syntactically compatible words.",
            "scope": "Only the 32 pairs v in 8..15 and v+ in 4..7 for parent (4,3), current (3,4), k=32 under exact C041 encoding.",
            "mathematical_falsifier": "Any source-bound counterexample to an asserted universal step, incomplete coverage of the 32 pairs, failure of full 33-bit equality, noncanonical word, or satisfiable alleged parent refutes the corresponding branch.",
            "repair_or_next_mathematical_move": "After separate public authorization, derive field equalities by hand and run the cheapest universal syntax refuters before any formula enumeration or UNSAT proof search.",
            "proof_and_source_evidence": "The merged C053 structural lemma proves only that all 32 parameter pairs survive two syntax screens. Exact C041 grammar and C048 overlap equivalence are bound; no candidate outcome has been accessed.",
        },
        "mathematical_learning_credit_policy": {
            "credited_only": [
                "the exact full-word implication under study",
                "field-boundary and coordinate-equality obligations",
                "supported and competing mathematical obstructions",
                "falsifiable hand-proof plan",
            ],
            "zero_credit": ["Git", "CI", "schemas", "hashes", "chronology", "repository activity"],
        },
        "credit": {"mathematical_result": 0, "independent_review": 0, "Git_CI_schema_hash": 0},
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def evaluator_identity(candidate: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "evaluator_id": EVALUATOR_ID,
        "candidate_id": CANDIDATE_ID,
        "candidate_artifact_hash": candidate["artifact_hash"],
        "frozen_at_utc": EVALUATOR_FROZEN_AT,
        "identity_kind": "INERT_SOURCE_BOUND_MATHEMATICAL_CERTIFICATE_EVALUATOR",
        "input_contract": {
            "candidate_binding": "exact candidate artifact and source bindings",
            "positive_packet": "one full W1-W7 witness with an independently checkable UNSAT proof",
            "negative_packet": "one W1-W6,W8 universal proof covering every frozen pair and literal choice",
            "malformed_or_conflicting_packet": "anything incomplete, ambiguous, source-mismatched, partial, or mutually conflicting",
        },
        "branch_rules": candidate["branch_contract"],
        "required_rederivations": [
            "support-cell and 32-pair coverage",
            "parent/current canonical parsing and field boundaries",
            "all 33 split/equality coordinates",
            "parent UNSAT proof verification for a positive packet",
            "universal coverage/completeness verification for a negative packet",
        ],
        "trust_boundary": [
            "caller assertions do not establish canonicality, UNSAT, equality, or completeness",
            "candidate proof code cannot certify itself",
            "finite enumeration without a completeness proof cannot authorize the negative branch",
            "SAT/UNSAT solver output without a proof certificate is corroboration only",
        ],
        "implementation": None,
        "evaluation_authorized": False,
        "result_accessed": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def falsifier_identity(candidate: dict, evaluator: dict) -> dict:
    worlds = [
        ("C053-CLEAN-PHASE-PLANTED-POSITIVE-v1", "a complete synthetic W1-W7 packet", "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS"),
        ("C053-CLEAN-PHASE-PLANTED-NEGATIVE-v1", "a complete synthetic W1-W6,W8 packet", "INCOMPATIBLE_WITH_UNIVERSAL_FULL_WORD_PROOF"),
        ("C053-CLEAN-PHASE-SYNTAX-SURVIVAL-ONLY-v1", "only the 32/32 two-screen structural lemma", "CANNOT_CHECK"),
        ("C053-CLEAN-PHASE-PARTIAL-EQUALITY-v1", "a packet matching fewer than all 33 label coordinates", "CANNOT_CHECK"),
        ("C053-CLEAN-PHASE-SAT-PARENT-FALSE-POSITIVE-v1", "a full equality witness whose parent formula is satisfiable", "CANNOT_CHECK"),
        ("C053-CLEAN-PHASE-INCOMPLETE-PAIR-COVERAGE-v1", "a negative packet omitting at least one of the 32 parameter pairs", "CANNOT_CHECK"),
        ("C053-CLEAN-PHASE-SOURCE-MISMATCH-v1", "a packet with one mutated C041/C048/pre-candidate binding", "CANNOT_CHECK"),
        ("C053-CLEAN-PHASE-CONFLICTING-CERTIFICATES-v1", "simultaneously valid-looking positive and negative packets", "CANNOT_CHECK"),
        ("C053-CLEAN-PHASE-FRONTEND-BRANCH-PROPAGATION-v1", "all branches through the future full evaluator", "EXACT_BRANCH_PROPAGATION"),
    ]
    return seal({
        "schema_version": "1.0.0",
        "falsifier_id": FALSIFIER_ID,
        "candidate_id": CANDIDATE_ID,
        "candidate_artifact_hash": candidate["artifact_hash"],
        "evaluator_id": EVALUATOR_ID,
        "evaluator_artifact_hash": evaluator["artifact_hash"],
        "frozen_at_utc": FALSIFIER_FROZEN_AT,
        "identity_kind": "INERT_FUTURE_MATHEMATICAL_REFUTER_WORLD_MANIFEST",
        "future_worlds": [
            {"world_id": world_id, "future_materialization_obligation": obligation, "expected_branch": branch, "materialized": False}
            for world_id, obligation, branch in worlds
        ],
        "direct_mathematical_refuters": [
            "one claimed compatible witness violates a field boundary, variable range, clause boundary, padding bit, or one of the 33 equalities",
            "one claimed compatible parent formula is satisfiable or lacks an independently checkable UNSAT proof",
            "one legal literal assignment in any frozen parameter pair escapes a claimed universal contradiction",
            "a claimed exhaustive negative proof lacks a proof that its search covers every legal word in all 32 pairs",
            "any conclusion inferred merely from survival of the two old syntax screens",
        ],
        "independence_requirements": [
            "future falsifier rederives grammar, coordinates, and coverage rather than importing candidate verdicts",
            "future positive and negative verification paths share no caller-supplied authority Boolean",
            "same-context review is explicitly not independent peer review",
        ],
        "implementation": None,
        "worlds_materialized": False,
        "evaluation_authorized": False,
        "result_accessed": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def receipt(candidate: dict, evaluator: dict, falsifier: dict) -> dict:
    trace_delta = {
        "event_id": "O9d12a2a1b-C053-K32-CLEAN-PHASE-E09",
        "atom_id": "O9d12a2a1b-C053-K32-CLEAN-PHASE-COMPATIBILITY",
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": RECEIPT_FROZEN_AT,
        "state_summary": "Exact candidate, evaluator, proof-plan, and falsifier identities are frozen for the 32-pair clean phase; no word, formula, SAT/UNSAT fact, equality result, or branch is accessed.",
        "action_summary": "Freeze full-word mathematical obligations and counterexample-first evaluator worlds without executing them.",
        "evidence_pointers": [str(path.relative_to(ROOT)) for path in (CANDIDATE_OUT, EVALUATOR_OUT, FALSIFIER_OUT)],
        "alternatives_considered": ["evaluate immediately", "use only the old two-screen survival", "broaden to 128 or 24320 pairs", "freeze the smallest 32-pair full-word discriminator"],
        "decision_rationale": "The merged pre-candidate packet selected the smallest clean phase, and exact whole-word compatibility is the next unresolved mathematical implication.",
        "outputs": [candidate["artifact_hash"], evaluator["artifact_hash"], falsifier["artifact_hash"], "ZERO_EVALUATED_MATHEMATICAL_RESULT"],
        "uncertainties": ["full-word compatibility is unknown", "parent UNSAT membership is unknown", "same-context review is not independent"],
        "residuals": ["separate post-merge evaluation authorization required", "all 32 full-word obligations unevaluated", "P-versus-NP root open"],
        "next_steps": ["PR and merge identities only", "freeze a separate authorization round before materialization or evaluation"],
        "previous_event_hash": PREVIOUS_EVENT_HASH,
    }
    trace_delta["artifact_hash"] = digest(json.dumps(trace_delta, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    return seal({
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C053-K32-CLEAN-PHASE-CANDIDATE-FREEZE-RECEIPT-20260812",
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_pin": FRAMEWORK_SHA,
        "candidate_id": CANDIDATE_ID,
        "candidate_artifact_hash": candidate["artifact_hash"],
        "evaluator_id": EVALUATOR_ID,
        "evaluator_artifact_hash": evaluator["artifact_hash"],
        "falsifier_id": FALSIFIER_ID,
        "falsifier_artifact_hash": falsifier["artifact_hash"],
        "frozen_at_utc": RECEIPT_FROZEN_AT,
        "trace_delta": trace_delta,
        "chronology_firewall": {
            "candidate_identity_frozen": True,
            "evaluator_identity_frozen": True,
            "falsifier_identity_frozen": True,
            "implementation_created": False,
            "validation_world_materialized": False,
            "parent_or_current_word_constructed": False,
            "formula_decoded": False,
            "SAT_UNSAT_executed_or_accessed": False,
            "full_label_equality_executed_or_accessed": False,
            "overlap_result_accessed": False,
            "evaluation_authorized": False,
        },
        "next_authorized_action": "PR_REVIEW_MERGE_ONLY",
        "credit": {"mathematical_result": 0, "independent_review": 0, "Git_CI_schema_hash": 0},
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def build() -> tuple[dict, dict, dict, dict]:
    assert_sources()
    candidate = candidate_identity()
    evaluator = evaluator_identity(candidate)
    falsifier = falsifier_identity(candidate, evaluator)
    return candidate, evaluator, falsifier, receipt(candidate, evaluator, falsifier)


def write() -> tuple[dict, dict, dict, dict]:
    documents = build()
    for path, document in zip((CANDIDATE_OUT, EVALUATOR_OUT, FALSIFIER_OUT, RECEIPT_OUT), documents):
        path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return documents


if __name__ == "__main__":
    write()
