from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c052_k31_overlap_result_fixture.py"
DISCRIMINATOR = PNP / "04_candidates/c052_k31_overlap_discriminator.py"
PATHS = [
    PNP / "04_candidates/O9d12a2a1b_C052_K31_OVERLAP_NEGATIVE_CERTIFICATE_20260812.json",
    PNP / "05_falsification/O9d12a2a1b_C052_K31_OVERLAP_INDEPENDENT_CHECK_RESULT_20260812.json",
    PNP / "07_memory/O9d12a2a1b_C052_K31_OVERLAP_FAILURE_EXPERIENCE_20260812.json",
    PNP / "07_memory/O9d12a2a1b_C052_K31_OVERLAP_MATHEMATICAL_LESSON_20260812.json",
    PNP / "08_reviews/O9d12a2a1b_C052_K31_OVERLAP_SAME_CONTEXT_REVIEW_20260812.json",
    PNP / "09_trace/O9d12a2a1b_C052_K31_OVERLAP_RESULT_RECEIPT_20260812.json",
]


def module():
    spec = importlib.util.spec_from_file_location("k31_result", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def discriminator_module():
    spec = importlib.util.spec_from_file_location("k31_discriminator", DISCRIMINATOR)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_result_documents_match_authorized_execution_fixture() -> None:
    assert [load(path) for path in PATHS] == list(module().build())


def test_negative_certificate_proves_exact_two_case_separator() -> None:
    negative = load(PATHS[0])
    assert negative["branch"] == "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE"
    assert all(negative["negative_obligations"].values())
    assert negative["negative_obligations"]["N4"] == negative["symbolic_separator_valid"]
    assert negative["negative_obligations"]["N5"] == negative["all_public_prefix_rows_separated"]
    assert negative["parent_cell"]["padding"] == 1
    assert len(negative["current_cells"]) == 3
    assert negative["public_unique_prefixes_checked_with_multiplicity_by_v"] == 82928
    assert all(row["all_prefixes_separated"] for row in negative["public_enumeration_rows"])
    proof = " ".join(negative["symbolic_proof"])
    assert "h[31]=0" in proof and "p[7:10]=100" in proof and "variable zero is illegal" in proof


def test_frontend_rederives_frozen_source_binding_and_fails_closed_on_mutation() -> None:
    discriminator = discriminator_module()
    result = discriminator.evaluate_public_k31()
    assert result["source_binding_valid"] is True
    assert result["branch"] == "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE"
    mutated = discriminator.evaluate_public_k31(source_overrides={"c041_grammar": b"mutated"})
    assert mutated["source_binding_valid"] is False
    assert mutated["branch"] == "CANNOT_CHECK"


def test_full_frontend_propagation_world_covers_all_three_frozen_branches() -> None:
    check = load(PATHS[1])
    world = check["world_results"]["K31-FRONTEND-KERNEL-BRANCH-PROPAGATION-v1"]
    assert world == {
        "CANNOT_CHECK": "CANNOT_CHECK",
        "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE": "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE",
        "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE": "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE",
    }


def test_independent_worlds_and_integration_pass_without_hidden_native() -> None:
    check = load(PATHS[1])
    assert check["candidate_branch"] == check["independent_branch"] == "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE"
    assert check["worlds_all_pass"] is True
    assert check["integration_all_pass"] is True
    assert check["independently_rederived_source_binding_valid"] is True
    assert check["hidden_or_native_executed"] is False
    assert check["authority"] == "INDEPENDENTLY_IMPLEMENTED_SAME_CONTEXT_CHECK_NOT_INDEPENDENT_PEER_REVIEW"


def test_failure_and_seven_field_math_lesson_preserve_scope() -> None:
    failure = load(PATHS[2])
    lesson = load(PATHS[3])
    fields = lesson["seven_field_mathematical_lesson"]
    assert len(fields) == 7
    assert failure["verified_impossibility_scope"] == "H_31 intersection P_32 only"
    assert failure["mathematical_classification"] == "SCOPED_STRUCTURAL_LEMMA_AND_FAILED_LOCAL_TO_GLOBAL_IMPLICATION"
    assert failure["warning_not_blacklist"].startswith("Future k")
    assert "full-word canonical boundary/token legality" in fields["supported_and_competing_causes"]
    assert "widen obstruction fingerprints" in lesson["framework_feedback_boundary"]
    assert len(lesson["reusable_mathematical_lessons"]) == 7
    assert all(item["authority"] in {"PROVED_IN_EXACT_K31_SCOPE", "SEARCH_HEURISTIC"} for item in lesson["reusable_mathematical_lessons"])


def test_review_and_receipt_never_escalate_root_or_review_authority() -> None:
    review = load(PATHS[4])
    receipt = load(PATHS[5])
    assert review["blocking_concerns"] == []
    assert review["review_boundary"] == "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW"
    assert receipt["hidden_or_native_executed"] is False
    assert receipt["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert [event["event_type"] for event in receipt["public_trace_deltas"]] == ["FALSIFIER_RUN", "RESULT_RECORDED"]
    assert receipt["public_trace_deltas"][1]["previous_event_hash"] == receipt["public_trace_deltas"][0]["artifact_hash"]
