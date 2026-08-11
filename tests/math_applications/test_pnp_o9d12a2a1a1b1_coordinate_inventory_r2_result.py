from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
RESULT_PATH = BASE / "01_frontier/O9d12a2a1a1b1_COORDINATE_INVENTORY_R2_RESULT_20260811.json"
LEDGER_PATH = BASE / "07_memory/O9d12a2a1a1b1_COORDINATE_INVENTORY_R2_MATHEMATICAL_EXPERIENCE_20260811.json"
TRACE_PATH = BASE / "09_trace/O9d12a2a1a1b1_COORDINATE_INVENTORY_R2_RESULT_TRACE_20260811.json"
REVIEW_PATH = BASE / "08_reviews/O9d12a2a1a1b1_COORDINATE_INVENTORY_R2_HOSTILE_MATH_REVIEW_20260811.json"
PRE_ACTION_PATH = BASE / "09_trace/O9d12a2a1a1b1_COORDINATE_INVENTORY_R2_PRE_ACTION_20260811.json"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _raw_sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _canonical_hash(document: dict[str, object]) -> str:
    payload = dict(document)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _event_hash(event: dict[str, object]) -> str:
    payload = dict(event)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_r2_result_is_bound_to_frozen_pre_action_and_hashes_are_canonical() -> None:
    result = _load(RESULT_PATH)
    ledger = _load(LEDGER_PATH)
    trace = _load(TRACE_PATH)
    review = _load(REVIEW_PATH)
    pre_action = _load(PRE_ACTION_PATH)

    for document in (result, ledger, trace, review):
        assert document["artifact_hash"] == _canonical_hash(document)

    binding = result["pre_action_binding"]
    assert binding["raw_sha256"] == _raw_sha256(PRE_ACTION_PATH)
    assert binding["canonical_sha256"] == "sha256:" + pre_action["receipt_canonical_sha256"]
    assert binding["application_commit"] == pre_action["application_commit"]
    assert binding["framework_commit"] == pre_action["framework_commit"]
    assert binding["frozen_before_result"] is True


def test_all_seven_rows_have_mathematical_difference_witnesses_and_rate_audits() -> None:
    result = _load(RESULT_PATH)
    rows = result["coordinate_rows"]
    assert len(rows) == 7
    assert {row["row_id"] for row in rows} == {
        "R2-C01-ECCC-T24-D-CAP",
        "R2-C02-ECCC-T30-D-CYCLIC",
        "R2-C03-ECCC-T37-DESCRIPTION",
        "R2-C04-RAZ89-WIG93-PAIRED-PROGRAMS",
        "R2-C05-ECCC-T45-SEMIULTRAFILTER",
        "R2-C06-WIG95-BRANCHING-RESTRICTION",
        "R2-C07-NM95-LOOP-APPROXIMATION",
    }
    for row in rows:
        assert row["source_anchors"]
        assert row["domain_and_quantifiers"]
        assert row["construction_side"]["status"]
        assert "sufficient_for_omega_log_N" in row["implication_composition"]
        witness = row["difference_witness"]
        assert witness["source_to_target_map"]
        assert witness["preserved_conditions"]
        assert witness["changed_or_broken_conditions"]
        assert witness["implication_direction"]
        assert witness["cheapest_falsifier_or_repair_test"]
        assert row["verdict"]

    t24 = next(row for row in rows if row["row_id"] == "R2-C01-ECCC-T24-D-CAP")
    assert t24["target_side"]["status"] == "PASS_EXPLICIT_RESTRICTED_MONOTONE_TARGET_WITH_ANCESTRY_GAP"
    assert t24["implication_composition"]["sufficient_for_omega_log_N"] is True
    description = next(row for row in rows if row["row_id"] == "R2-C03-ECCC-T37-DESCRIPTION")
    assert description["coordinate"]["distinct_from_frozen_root_quantities"] == "NOT_A_TARGET_COORDINATE_AS_STATED"
    branch = next(row for row in rows if row["row_id"] == "R2-C06-WIG95-BRANCHING-RESTRICTION")
    assert "rho_full<=rho_branch" in branch["implication_composition"]["scale_calculation"]
    ultra = next(row for row in rows if row["row_id"] == "R2-C05-ECCC-T45-SEMIULTRAFILTER")
    assert ultra["construction_side"]["statement"] == "rho_ultra(A,B) <= rho(A,B) <= m"


def test_missing_primary_ancestry_forces_blocked_no_candidate_and_no_root_authority() -> None:
    result = _load(RESULT_PATH)
    overall = result["overall_result"]
    assert overall == {
        "outcome_branch": "BLOCKED",
        "verdict": "CANNOT_CHECK_REQUIRED_PRIMARY_ANCESTRY_AND_NO_ADMISSIBLE_MATCH_IN_INSPECTED_ROWS",
        "candidate_generation_allowed": False,
        "candidate_generated": False,
        "inspected_row_admissible_match_count": 0,
        "exhaustive_no_match_claimed": False,
        "root_status": "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE",
    }
    assert set(result["source_completeness_cut"]["missing_primary_sources"]) == {
        "KARCHMER-1993",
        "WIGDERSON-1995",
        "NAKAYAMA-MARUOKA-1995",
    }
    assert result["source_completeness_cut"]["bounded_no_match_allowed"] is False
    sources = {row["source_id"]: row for row in result["source_universe"]}
    assert sources["RAZBOROV-1989"]["raw_sha256"].endswith("a829725a0b7a70d78ed9ba8cf26fd15d58c7a12270443610c2391f5768b40706")
    assert sources["WIGDERSON-1993"]["raw_sha256"].endswith("69893dfc288a89c2b7243b11ec0851ed73cbdda004e0046257bdbe439082e1d7")
    assert all(value is False for value in result["authority_contract"].values())


def test_mathematical_experience_excludes_operational_checks() -> None:
    ledger = _load(LEDGER_PATH)
    required = set(ledger["admission_rule"]["required_fields"])
    assert {
        "typed_mathematical_statement_or_failure",
        "quantifiers_or_scope",
        "mathematical_evidence",
        "broken_assumptions",
        "falsifier_or_next_discriminator",
        "non_guarantees",
        "local_vs_gluing_status",
    } <= required
    forbidden_phrases = (
        "CI passed",
        "CI failed",
        "Git branch moved",
        "HTTP 404",
        "schema passed",
        "test count",
        "token usage",
    )
    for experience in ledger["experiences"]:
        for field in (
            "typed_mathematical_statement_or_failure",
            "bounded_diagnosis",
            "falsifier_or_next_discriminator",
            "local_vs_gluing_status",
        ):
            text = experience[field]
            assert not any(phrase in text for phrase in forbidden_phrases)
        assert experience["mathematical_evidence"]
        assert experience["non_guarantees"]

    assert ledger["evidence_completeness_block"]["classification"] == (
        "SOURCE_GOVERNANCE_ASSURANCE_NOT_MATHEMATICAL_LESSON"
    )
    assert ledger["framework_feedback"]["new_framework_delta_warranted"] is False
    assert all(value is False for value in ledger["authority_contract"].values())


def test_result_trace_is_hash_chained_and_review_is_internal_only() -> None:
    trace = _load(TRACE_PATH)
    previous = trace["pre_action_predecessor"]["canonical_hash"]
    for event in trace["events"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _event_hash(event)
        previous = event["artifact_hash"]

    review = _load(REVIEW_PATH)
    assert review["review_authority"] == (
        "SAME_CONTEXT_INTERNAL_HOSTILE_MATHEMATICAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW"
    )
    assert review["verdict"] == "NO_BLOCKER_FOR_NARROW_BLOCKED_RESULT"
    assert review["candidate_generated"] is False
    assert review["root_status"] == "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE"
    assert review["lesson_boundary_audit"]["operational_items_in_mathematical_lessons"] is False
    assert review["lesson_boundary_audit"]["framework_change_promoted"] is False
    assert all(value is False for value in review["authority_contract"].values())

    bindings = {entry["path"]: entry for entry in review["reviewed_artifacts"]}
    for path in (RESULT_PATH, LEDGER_PATH, TRACE_PATH):
        relative = str(path.relative_to(ROOT))
        assert bindings[relative]["raw_sha256"] == _raw_sha256(path)
        assert bindings[relative]["artifact_hash"] == _load(path)["artifact_hash"]
