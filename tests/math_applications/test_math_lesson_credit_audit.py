from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AUDIT = (
    ROOT
    / "research/real_math/millennium/cross_problem/10_case_study/"
    "MATH_LESSON_CREDIT_AUDIT_20260812.json"
)
LATEST_LEDGER = (
    ROOT
    / "research/real_math/millennium/cross_problem/07_memory/"
    "GLOBAL_MATH_ONLY_SATURATION_LEDGER_BSD_R15_SUCCESSOR_20260812.json"
)
BASE = "cd8ca21bf0cb4b493a374d619d0f3ea5008cf018"
FRAMEWORK = "7d67a18a96499f5df7bf58bc6b1356d1ce1cafbf"
EXPECTED_PATHS = {
    "research/meta/application_feedback/round1/lessons/exact_framework_pin_runner.json",
    "research/meta/application_feedback/round1/lessons/framework_split_dangling_tests.json",
    "research/meta/application_feedback/round1/lessons/migrated_test_root.json",
    "research/meta/application_feedback/round1/lessons/o9_source_trace_hash.json",
    "research/real_math/millennium/cross_problem/10_study_pattern/LESSON_PROPOSAL_EXAMPLE_20260811.json",
    "research/real_math/millennium/cross_problem/10_study_pattern/LESSON_PROPOSAL.schema.json",
}
SEVEN_FIELDS = {
    "attempted_mathematical_implication",
    "exact_result_or_failure",
    "supported_and_competing_causes",
    "scope",
    "mathematical_falsifier",
    "repair_or_next_discriminator",
    "proof_or_source_evidence",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_audit_is_content_bound_and_exactly_scoped() -> None:
    audit = load(AUDIT)
    assert audit["artifact_hash"] == canonical_hash(audit)
    authority = audit["authority_universe"]
    assert authority["application_base_sha"] == BASE
    assert authority["live_framework_main_observed_sha"] == FRAMEWORK
    assert authority["review_authority"] == (
        "SAME_CONTEXT_ADDITIVE_CLASSIFICATION_AUDIT_NOT_INDEPENDENT_REVIEW"
    )
    assert {item["path"] for item in audit["audited_artifacts"]} == EXPECTED_PATHS
    assert all((ROOT / path).is_file() for path in EXPECTED_PATHS)


def test_six_software_or_process_lessons_are_explicit_zero_credit() -> None:
    audit = load(AUDIT)
    assert len(audit["audited_artifacts"]) == 6
    for item in audit["audited_artifacts"]:
        assert item["classification"] == "NO_MATHEMATICAL_LESSON"
        assert item["mathematical_credit"] is False
        assert item["credit_units"] == 0
        assert SEVEN_FIELDS <= item.keys()
        assert item["attempted_mathematical_implication"] is None
        assert "NOT_APPLICABLE" in item["supported_and_competing_causes"]
        assert item["proof_or_source_evidence"]

    result = audit["audit_result"]
    assert result == {
        "artifacts_examined": 6,
        "cannot_check": 0,
        "classification": (
            "SIX_RETAINED_LESSON_LABELS_RECLASSIFIED_"
            "NO_MATHEMATICAL_LESSON_ZERO_CREDIT"
        ),
        "framework_method_evolution_claim": False,
        "mathematical_result_generated": False,
        "no_mathematical_lesson": 6,
        "positive_mathematical_credit": 0,
        "software_only_artifact_was_positive_in_checked_ledger": False,
    }


def test_source_content_supports_nonmathematical_classification() -> None:
    feedback = ROOT / "research/meta/application_feedback/round1/lessons"
    runner = load(feedback / "exact_framework_pin_runner.json")
    assert runner["proof_backing"] == []
    assert "does not prove any mathematical statement" in runner["non_guarantees"]
    assert runner["candidate_framework_delta"]["status"] == "UNVALIDATED_PROPOSAL"

    split = load(feedback / "framework_split_dangling_tests.json")
    assert split["method_family"] == "framework-application-repository-split"
    assert split["candidate_framework_delta"]["status"] == "UNVALIDATED_PROPOSAL"

    migrated = load(feedback / "migrated_test_root.json")
    assert migrated["method_family"] == "repository-tree-migration"
    assert "FileNotFoundError" in migrated["residual_signature"]

    trace_hash = load(feedback / "o9_source_trace_hash.json")
    assert "no mathematical candidate was evaluated" in trace_hash["scope_conditions"]
    assert trace_hash["candidate_framework_delta"]["status"] == "UNVALIDATED_PROPOSAL"

    study = load(
        ROOT
        / "research/real_math/millennium/cross_problem/10_study_pattern/"
        "LESSON_PROPOSAL_EXAMPLE_20260811.json"
    )
    assert study["status"] == "PROPOSAL_ONLY"
    assert "does not prove, formalize, glue, or certify mathematics" in study["boundaries"]
    contract = study["authority_contract"]
    assert contract["grants_proof_authority"] is False
    assert contract["grants_theorem_authority"] is False

    schema = load(
        ROOT
        / "research/real_math/millennium/cross_problem/10_study_pattern/"
        "LESSON_PROPOSAL.schema.json"
    )
    assert "search-priority advisory" in schema["description"]
    assert schema["properties"]["status"]["const"] == "PROPOSAL_ONLY"


def test_exact_frozen_predecessor_ledger_grants_no_credit_to_audited_items() -> None:
    audit, ledger = load(AUDIT), load(LATEST_LEDGER)
    checked = audit["ledger_cross_check"]
    assert checked["artifact_hash"] == ledger["artifact_hash"]
    assert checked["authority_repository_sha"] == ledger["base_repository_sha"]
    assert checked["authority_repository_sha"] == ledger["authority_universe"]["repository_sha"]
    assert "not current portfolio coverage" in checked["scope_boundary"]
    assert checked["result"] == (
        "NO_POSITIVE_MATHEMATICAL_CREDIT_FOUND_FOR_THE_SIX_AUDITED_ARTIFACTS"
    )
    credited_pointers = {
        pointer
        for lane in ledger["lanes"]
        for item in lane["credited_items"]
        for pointer in item["evidence_pointers"]
    }
    assert EXPECTED_PATHS.isdisjoint(credited_pointers)
    exclusions = " ".join(
        pointer
        for item in ledger["excluded_provenance"]
        for pointer in item["evidence_pointers"]
    )
    assert "LESSON_PROPOSAL_EXAMPLE_20260811.json" in exclusions
    assert any(
        "application feedback" in item["reason"].lower()
        and item["mathematical_credit"] is False
        and item["credit_units"] == 0
        for item in ledger["excluded_provenance"]
    )


def test_math_lesson_policy_fails_closed_and_roots_remain_open() -> None:
    audit = load(AUDIT)
    contract = audit["classification_contract"]
    assert set(contract["required_seven_fields_for_any_material_mathematical_lesson"]) == SEVEN_FIELDS
    assert "CANNOT_CHECK with zero credit" in contract["fail_closed_rule"]
    assert contract["computation_is_proof"] is False
    assert contract["same_context_review_is_independent_review"] is False
    roots = audit["root_statuses"]
    assert all(
        status == "OPEN_NO_SOLUTION_CERTIFICATE"
        for problem, status in roots.items()
        if problem != "poincare_conjecture"
    )
    assert roots["poincare_conjecture"] == (
        "SOLVED_EXTERNALLY_NO_NEW_APPLICATION_SOLUTION_CLAIM"
    )
