from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c053_k32_clean_phase_result_fixture.py"
DISCRIMINATOR = PNP / "04_candidates/c053_k32_clean_phase_discriminator.py"
CHECKER = PNP / "05_falsification/c053_k32_clean_phase_independent_checker.py"
PATHS = [
    PNP / "04_candidates/O9d12a2a1b_C053_K32_CLEAN_PHASE_POSITIVE_CERTIFICATE_20260812.json",
    PNP / "05_falsification/O9d12a2a1b_C053_K32_CLEAN_PHASE_INDEPENDENT_CHECK_RESULT_20260812.json",
    PNP / "07_memory/O9d12a2a1b_C053_K32_CLEAN_PHASE_MATHEMATICAL_LESSON_20260812.json",
    PNP / "08_reviews/O9d12a2a1b_C053_K32_CLEAN_PHASE_SAME_CONTEXT_REVIEW_20260812.json",
    PNP / "09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_RESULT_RECEIPT_20260812.json",
]
BRANCH = "COMPATIBLE_WITH_EXACT_FORMULA_BOUND_UNSAT_WITNESS"


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_result_documents_match_authorized_fixture() -> None:
    assert [load(path) for path in PATHS] == list(module("c053_result_fixture", FIXTURE).build())


def test_hand_certificate_is_exact_canonical_formula_bound_witness() -> None:
    certificate = load(PATHS[0])
    assert certificate["branch"] == BRANCH
    assert certificate["chosen_frozen_pair"] == {"parent_v": 8, "current_v": 5}
    assert len(certificate["frozen_pair_universe"]) == 32
    assert certificate["parent_formula"]["canonical_word_x"] == "1110010100010000110001000010101011001010010100100001000010001010"
    assert certificate["current_formula"]["canonical_word_y"] == "111001010010100100001000010001010000010001000100010001000100010001"
    assert certificate["label_h"] == certificate["current_prefix_p"] == "111001010010100100001000010001010"
    assert len(certificate["all_33_coordinate_equalities"]) == 33
    assert all(row["h"] == row["p"] for row in certificate["all_33_coordinate_equalities"])
    assert all(certificate["positive_obligations"].values())


def test_three_step_resolution_is_proof_and_computation_is_only_corroboration() -> None:
    certificate = load(PATHS[0])
    assert [step["resolvent"] for step in certificate["resolution_certificate"]] == ["NOT x5", "x5", "EMPTY"]
    assert certificate["proof_authority"] == "HAND_RESOLUTION_AND_EXPLICIT_CANONICAL_WORD_EQUALITY"
    assert certificate["computational_corroboration"] == {
        "authority": "CORROBORATION_ONLY",
        "satisfying_assignments": 0,
        "truth_table_assignments_checked": 256,
    }
    discriminator = module("c053_discriminator", DISCRIMINATOR)
    witness = discriminator.build_hand_witness()
    assert witness["resolution_proof_valid"] is True
    assert witness["truth_table_satisfying_assignment_count"] == 0
    assert discriminator.parse_canonical(witness["x"])["literals"] == tuple(lit for clause in witness["parent_clauses"] for lit in clause)


def test_source_binding_fails_closed_and_all_nine_worlds_pass() -> None:
    discriminator = module("c053_discriminator_source", DISCRIMINATOR)
    actual = discriminator.evaluate()
    assert actual["branch"] == BRANCH
    mutated = discriminator.frontend(positive=actual["witness"], overrides={"c041": b"mutated"})
    assert mutated["branch"] == "CANNOT_CHECK"
    check = load(PATHS[1])
    assert check["candidate_branch"] == check["independent_branch"] == BRANCH
    assert check["worlds_all_pass"] is True
    assert len(check["world_results"]) == 9
    for world in (
        "C053-CLEAN-PHASE-SYNTAX-SURVIVAL-ONLY-v1",
        "C053-CLEAN-PHASE-PARTIAL-EQUALITY-v1",
        "C053-CLEAN-PHASE-SAT-PARENT-FALSE-POSITIVE-v1",
        "C053-CLEAN-PHASE-INCOMPLETE-PAIR-COVERAGE-v1",
        "C053-CLEAN-PHASE-SOURCE-MISMATCH-v1",
        "C053-CLEAN-PHASE-CONFLICTING-CERTIFICATES-v1",
    ):
        assert check["world_results"][world] == "CANNOT_CHECK"


def test_seven_field_lesson_preserves_exact_scope_and_next_residual() -> None:
    lesson = load(PATHS[2])
    fields = lesson["seven_field_mathematical_lesson"]
    assert len(fields) == 7
    assert "constructive cross-boundary token alignment" in fields["supported_and_competing_causes"]
    assert "does not classify the other 31 pairs" in fields["scope"]
    assert "collision-to-cover obligation" in fields["repair_or_next_discriminator"]
    assert lesson["framework_feedback_boundary"].endswith("automatically promoted ResearchTool.")
    assert lesson["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_review_receipt_trace_and_zero_credit_never_escalate_root() -> None:
    review = load(PATHS[3])
    receipt = load(PATHS[4])
    assert review["blocking_concerns"] == []
    assert review["review_boundary"] == "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW"
    assert receipt["application_base_sha"] == "31cc68929a947311b9abfcc7b397c83b8ec30d3f"
    assert receipt["authorization_artifact_hash"] == "sha256:078ed4be2cf0f4da62f8960d7cb19519b73a2ac797f219ba8f5dd7f6d48dd299"
    assert receipt["result_branch"] == BRANCH
    assert [event["event_type"] for event in receipt["public_trace_deltas"]] == ["FALSIFIER_RUN", "RESULT_RECORDED"]
    assert receipt["public_trace_deltas"][1]["previous_event_hash"] == receipt["public_trace_deltas"][0]["artifact_hash"]
    assert receipt["zero_credit"][:6] == ["Git", "CI", "schemas", "hashes", "chronology", "repository activity"]
    assert "cover requirement remains unevaluated" in receipt["open_residual"]
    assert receipt["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
