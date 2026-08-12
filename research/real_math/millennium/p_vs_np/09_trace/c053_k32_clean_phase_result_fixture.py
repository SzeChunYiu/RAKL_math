"""Serialize the authorized C053 hand proof, exact corroboration, and lesson."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
DISCRIMINATOR = PNP / "04_candidates/c053_k32_clean_phase_discriminator.py"
CHECKER = PNP / "05_falsification/c053_k32_clean_phase_independent_checker.py"
POSITIVE = PNP / "04_candidates/O9d12a2a1b_C053_K32_CLEAN_PHASE_POSITIVE_CERTIFICATE_20260812.json"
CHECK = PNP / "05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_INDEPENDENT_CHECK_RESULT_20260812.json"
LESSON = PNP / "07_memory/O9d12a2a1b_C053_K32_CLEAN_PHASE_MATHEMATICAL_LESSON_20260812.json"
REVIEW = PNP / "08_reviews/O9d12a2a1b_C053_K32_CLEAN_PHASE_SAME_CONTEXT_REVIEW_20260812.json"
RECEIPT = PNP / "09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_RESULT_RECEIPT_20260812.json"

BASE_SHA = "31cc68929a947311b9abfcc7b397c83b8ec30d3f"
AUTHORIZATION_HASH = "sha256:078ed4be2cf0f4da62f8960d7cb19519b73a2ac797f219ba8f5dd7f6d48dd299"
PREVIOUS_EVENT_HASH = "sha256:70be8e174b8f7e05c94cc1cac73296ac1e7cb889b2917be7d9517f5097a1d02b"
BRANCH = "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS"


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
    candidate = load_module("c053_candidate", DISCRIMINATOR).evaluate()
    independent = load_module("c053_checker", CHECKER).run()
    if candidate["branch"] != BRANCH or independent["actual_branch"] != BRANCH:
        raise RuntimeError("positive branch not established")
    if not independent["worlds_all_pass"]:
        raise RuntimeError("hostile worlds failed")
    witness = candidate["witness"]
    if witness["truth_table_satisfying_assignment_count"] != 0:
        raise RuntimeError("corroborative truth table disagrees with hand proof")

    positive = seal({
        "schema_version": "1.0.0",
        "certificate_id": "PNP-C053-K32-CLEAN-PHASE-FORMULA-BOUND-UNSAT-WITNESS-v1",
        "candidate_id": "PNP-C053-K32-CLEAN-PHASE-FULL-WORD-COMPATIBILITY-v1",
        "branch": BRANCH,
        "chosen_frozen_pair": {"parent_v": 8, "current_v": 5},
        "frozen_pair_universe": [{"parent_v": v, "current_v": vp} for v in range(8, 16) for vp in range(4, 8)],
        "existential_scope_note": "One W1-W7 witness in the frozen 32-pair universe decides the exact existential compatibility candidate; no claim is made that the other 31 pairs are compatible.",
        "parent_field_boundaries": [
            {"field": "MAGIC", "coordinates": "x[0:8]", "bits": witness["x"][0:8]},
            {"field": "gamma(8)", "coordinates": "x[8:15]", "bits": witness["x"][8:15]},
            {"field": "gamma(3)", "coordinates": "x[15:18]", "bits": witness["x"][15:18]},
            {"field": "nine width-5 literal tokens", "coordinates": "x[18:63]", "bits": witness["x"][18:63]},
            {"field": "parity pad", "coordinates": "x[63]", "bits": witness["x"][63]},
        ],
        "current_field_boundaries": [
            {"field": "MAGIC", "coordinates": "y[0:8]", "bits": witness["y"][0:8]},
            {"field": "gamma(5)", "coordinates": "y[8:13]", "bits": witness["y"][8:13]},
            {"field": "gamma(4)", "coordinates": "y[13:18]", "bits": witness["y"][13:18]},
            {"field": "twelve width-4 literal tokens", "coordinates": "y[18:66]", "bits": witness["y"][18:66]},
        ],
        "parent_formula": {
            "variable_count": 8,
            "clauses": [
                "(x2 OR x2 OR NOT x5)",
                "(NOT x2 OR NOT x2 OR NOT x2)",
                "(x2 OR x2 OR x5)",
            ],
            "literal_tokens": ["00010", "00010", "10101", "10010", "10010", "10010", "00010", "00010", "00101"],
            "canonical_word_x": witness["x"],
        },
        "current_formula": {
            "variable_count": 5,
            "clauses": [
                "(x2 OR x1 OR x1)",
                "(x4 OR x1 OR x1)",
                "(x1 OR x1 OR x1)",
                "(x1 OR x1 OR x1)",
            ],
            "canonical_word_y": witness["y"],
            "note": "Only the first four current literals determine p[0:33]; the remaining eight legal x1 literals complete a canonical word.",
        },
        "hand_derivation": [
            "For current v+=5, MAGIC||gamma(5)||gamma(4)=111001010010100100. Under h[j]=x[31+j], its p[2:17] bits become parent tokens 3,4,5, each 10010=NOT x2, so the middle parent clause is the unit NOT x2 after duplicate removal.",
            "Choose the first four current tokens as x2,x1,x1,x4. Their overlapping bits make parent tokens 6,7,8 equal 00010,00010,00101, so the last parent clause is x2 OR x2 OR x5; the current token x4 also supplies p[32]=0, matching the parent parity pad.",
            "Because p[1]=1, parent token 2 need only end in 1; choose it as 10101=NOT x5 and choose parent tokens 0,1 as 00010=x2. The first parent clause is x2 OR x2 OR NOT x5.",
            "Resolve (x2 OR NOT x5) with NOT x2 to derive NOT x5. Resolve (x2 OR x5) with NOT x2 to derive x5. Resolving x5 with NOT x5 yields the empty clause; hence Dec(x) is UNSAT.",
            "The displayed canonical encodings give h=1||x[32:64]=111001010010100100001000010001010=y[0:33]=p in all 33 coordinates.",
        ],
        "resolution_certificate": [
            {"step": "R1", "premises": ["C0", "C1"], "pivot": "x2", "resolvent": "NOT x5"},
            {"step": "R2", "premises": ["C2", "C1"], "pivot": "x2", "resolvent": "x5"},
            {"step": "R3", "premises": ["R1", "R2"], "pivot": "x5", "resolvent": "EMPTY"},
        ],
        "label_h": witness["h"],
        "current_prefix_p": witness["p"],
        "all_33_coordinate_equalities": witness["coordinate_rows"],
        "positive_obligations": witness["positive_obligations"],
        "exact_result": "The frozen 32-pair clean phase is compatible: pair (parent v,current v+)=(8,5) has a canonical UNSAT parent whose 33-bit label equals a canonical current prefix.",
        "proof_authority": "HAND_RESOLUTION_AND_EXPLICIT_CANONICAL_WORD_EQUALITY",
        "computational_corroboration": {"truth_table_assignments_checked": 256, "satisfying_assignments": 0, "authority": "CORROBORATION_ONLY"},
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    check = seal({
        "schema_version": "1.0.0",
        "check_id": "PNP-C053-K32-CLEAN-PHASE-INDEPENDENT-CHECK-20260812",
        "discriminator_raw_sha256": digest(DISCRIMINATOR.read_bytes()),
        "checker_raw_sha256": digest(CHECKER.read_bytes()),
        "candidate_branch": candidate["branch"],
        "independent_branch": independent["actual_branch"],
        "independently_rederived_source_binding_valid": independent["source_valid"],
        "independent_positive_obligations": independent["positive_obligations"],
        "independent_parent_word": independent["parent_word"],
        "independent_current_word": independent["current_word"],
        "independent_label": independent["label"],
        "independent_prefix": independent["prefix"],
        "independent_resolution_check": independent["resolution_implication_check"],
        "independent_truth_table_satisfying_assignment_count": independent["truth_table_satisfying_assignment_count"],
        "world_results": independent["world_results"],
        "worlds_all_pass": independent["worlds_all_pass"],
        "positive_certificate_artifact_hash": positive["artifact_hash"],
        "authority": independent["authority"],
        "computation_authority": independent["computation_authority"],
    })
    lesson = seal({
        "schema_version": "1.0.0",
        "lesson_id": "MATH-PNP-C053-K32-CLEAN-PHASE-COMPATIBILITY-20260812",
        "positive_certificate_artifact_hash": positive["artifact_hash"],
        "seven_field_mathematical_lesson": {
            "attempted_implication": "After both k31 separator families disappear in the 32-pair (4,3)->(3,4) k32 phase, does at least one full 33-bit compatibility survive with a genuinely UNSAT parent?",
            "exact_result_or_failure": "Yes. At (v,v+)=(8,5), the displayed canonical words satisfy h=p in all 33 coordinates, and the parent clauses resolve to both x5 and NOT x5 under the forced unit NOT x2.",
            "supported_and_competing_causes": "Supported cause is constructive cross-boundary token alignment: the current v+=5 header produces three parent NOT-x2 tokens, while four current literals and three freely chosen parent-prefix literals complete a three-clause contradiction. Mere two-screen survival, accidental partial equality, a satisfiable parent, and source drift are excluded.",
            "scope": "Only the exact frozen k32 existential over parent (a,m)=(4,3), v=8..15 and current (a+,m+)=(3,4), v+=4..7, under unchanged C041/C048. The witness decides existence but does not classify the other 31 pairs or imply cover growth, circuit bounds, novelty, or P versus NP.",
            "mathematical_falsifier": "A bad field boundary, illegal variable code, any unequal h/p coordinate, a satisfying assignment for the displayed parent, an invalid resolution step, or a frozen-source mismatch refutes the positive certificate.",
            "repair_or_next_discriminator": "Propagate this exact compatible label into the separate collision-to-cover obligation: determine whether it creates a genuinely new cover requirement rather than only a label collision, with that cover evaluator frozen before access.",
            "proof_and_source_evidence": "Five-step hand derivation, explicit 64/66-bit canonical words, three-step resolution certificate, and all 33 coordinate equalities. Separate exact decoding, hostile worlds, and a 256-assignment truth table corroborate but do not supply proof authority.",
        },
        "reusable_mathematical_lessons": [
            {
                "lesson": "A phase change can turn a former separator into a constructive semantic resource: aligned header bits may force a useful unit clause rather than merely cease to conflict.",
                "authority": "PROVED_IN_EXACT_C053_WITNESS_SCOPE",
                "validation": "A transfer must map the exact bits to legal target tokens and close the semantic obligation independently.",
            },
            {
                "lesson": "For an existential compatibility proposition over a frozen finite phase, one full formula-bound witness decides the phase without classifying every parameter pair.",
                "authority": "LOGICAL_QUANTIFIER_LESSON",
                "validation": "The witness must belong to the frozen universe and satisfy every conjunct; it cannot be selected from an expanded post-result universe.",
            },
            {
                "lesson": "Free coordinates before the equal split and forced coordinates after it can be designed jointly: the free prefix supplies one clause while the shared suffix supplies the other clauses and pad.",
                "authority": "PROVED_IN_EXACT_C053_WITNESS_SCOPE",
                "validation": "Display the split map and verify every cross-boundary token and padding coordinate.",
            },
        ],
        "framework_feedback_boundary": "This is mathematical search experience, not framework-evolution evidence or an automatically promoted ResearchTool.",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    review = seal({
        "schema_version": "1.0.0",
        "review_id": "PNP-C053-K32-CLEAN-PHASE-SAME-CONTEXT-REVIEW-20260812",
        "positive_certificate_artifact_hash": positive["artifact_hash"],
        "check_artifact_hash": check["artifact_hash"],
        "role_reviews": {
            "domain_theory": "Both words are canonical in their exact support cells; the parent is UNSAT by a three-step resolution refutation.",
            "analogy_method_transfer": "The parser-phase analogy suggested inspecting cross-boundary fields but supplies no authority; the exact bit map supplies the result.",
            "adversarial_falsification": "All 33 bits, the parent pad, variable ranges, hostile false positives, incomplete coverage, source mutation, and conflicting packets fail closed.",
            "formal_methods": "The resolution certificate is short and independently checkable; the truth table is only corroboration. A future formal proof would still require statement binding.",
            "novelty_research_value": "This closes only the finite compatibility atom and opens the collision-to-cover obligation; no novelty or lower-bound claim follows.",
        },
        "strongest_objection": "Could the displayed UNSAT fact be an artifact of computation? No: C1 gives NOT x2, C0 then gives NOT x5, C2 gives x5, yielding the empty clause by resolution.",
        "blocking_concerns": [],
        "verdict": "EXACT_C053_POSITIVE_WITNESS_SURVIVES_SAME_CONTEXT_REVIEW",
        "review_boundary": "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
    })
    e10 = seal({
        "event_id": "O9d12a2a1b-C053-K32-CLEAN-PHASE-E10", "atom_id": "O9d12a2a1b-C053-K32-CLEAN-PHASE-COMPATIBILITY",
        "event_type": "FALSIFIER_RUN", "timestamp": "2026-08-12T17:52:00Z",
        "state_summary": "All nine frozen hostile/conformance/integration worlds pass and the separately rederived checker agrees on the exact positive witness.",
        "action_summary": "Check the hand certificate, source bindings, branch propagation, false positives, and exact corroboration.",
        "evidence_pointers": [str(CHECK.relative_to(ROOT))],
        "outputs": [check["artifact_hash"], "PUBLIC_WORLDS_PASS", BRANCH],
        "previous_event_hash": PREVIOUS_EVENT_HASH,
        "residuals": ["record exact bounded result", "collision-to-cover implication remains open", "root open"],
        "next_steps": ["record only the source-bound compatibility result and mathematical lesson"],
    })
    e11 = seal({
        "event_id": "O9d12a2a1b-C053-K32-CLEAN-PHASE-E11", "atom_id": "O9d12a2a1b-C053-K32-CLEAN-PHASE-COMPATIBILITY",
        "event_type": "RESULT_RECORDED", "timestamp": "2026-08-12T17:52:01Z",
        "state_summary": "The exact 32-pair existential is positive via the (8,5) formula-bound UNSAT witness; no root or cover claim follows.",
        "action_summary": "Record the positive branch, seven-field lesson, scope, and next mathematical residual.",
        "evidence_pointers": [str(POSITIVE.relative_to(ROOT)), str(LESSON.relative_to(ROOT)), str(REVIEW.relative_to(ROOT))],
        "outputs": [positive["artifact_hash"], lesson["artifact_hash"], BRANCH, "OPEN_NO_SOLUTION_CERTIFICATE"],
        "previous_event_hash": e10["artifact_hash"],
        "residuals": ["collision does not establish a new cover requirement", "other 31 pairs unclassified", "root open"],
        "next_steps": ["freeze a separate collision-to-cover discriminator before evaluating any cover effect"],
    })
    receipt = seal({
        "schema_version": "1.0.0",
        "result_id": "PNP-C053-K32-CLEAN-PHASE-RESULT-20260812",
        "application_base_sha": BASE_SHA,
        "authorization_artifact_hash": AUTHORIZATION_HASH,
        "result_branch": BRANCH,
        "exact_mathematical_result": positive["exact_result"],
        "positive_certificate_artifact_hash": positive["artifact_hash"],
        "independent_check_artifact_hash": check["artifact_hash"],
        "lesson_artifact_hash": lesson["artifact_hash"],
        "same_context_review_artifact_hash": review["artifact_hash"],
        "implementation_hashes": {"candidate": digest(DISCRIMINATOR.read_bytes()), "independent_checker": digest(CHECKER.read_bytes())},
        "public_trace_deltas": [e10, e11],
        "mathematical_credit": ["explicit formula-bound 33-bit compatibility witness", "three-step hand resolution refutation of the parent formula"],
        "zero_credit": ["Git", "CI", "schemas", "hashes", "chronology", "repository activity", "computation as proof", "independent peer review"],
        "open_residual": "Whether this compatible label forces any new cover requirement remains unevaluated and requires a separately frozen discriminator.",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    return positive, check, lesson, review, receipt


def write() -> tuple[dict, ...]:
    documents = build()
    for path, document in zip((POSITIVE, CHECK, LESSON, REVIEW, RECEIPT), documents):
        path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return documents


if __name__ == "__main__":
    write()
