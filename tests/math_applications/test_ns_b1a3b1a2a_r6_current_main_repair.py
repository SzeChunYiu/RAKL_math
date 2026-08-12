from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"
SOURCE = NS / "00_sources/NS_B1a3b1a2a_R6_ANCIENT_SMOOTHING_CAPACITY_SOURCE_RECEIPT_20260812.json"
LESSON = NS / "07_memory/NS_B1a3b1a2a_R6_SCOPED_MATHEMATICAL_LESSON_20260812.json"
BASE_SHA = "58de5548d337d4ea3c83b5fcde6ed5c6aee3f2e0"
FRAMEWORK_SHA = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
UNIT_ID = "MATH-NS-B1A3B1A2A-R6-ANCIENT-SMOOTHING-TO-FIXED-TIME-CAPACITY"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _contains_key(value: object, forbidden: str) -> bool:
    if isinstance(value, dict):
        return forbidden in value or any(_contains_key(item, forbidden) for item in value.values())
    if isinstance(value, list):
        return any(_contains_key(item, forbidden) for item in value)
    return False


def test_r6_repair_is_exactly_one_scoped_proof_unit_on_current_authority() -> None:
    lesson = _load(LESSON)
    assert lesson["unit_id"] == UNIT_ID
    assert lesson["mathematical_unit_count"] == 1
    assert lesson["credit_type"] == "PROOF_OR_LEMMA"
    assert lesson["transfer_condition_separate_credit_units"] == 0
    assert lesson["application"]["base_sha"] == BASE_SHA
    assert lesson["framework"]["rakl_main_sha"] == FRAMEWORK_SHA
    assert lesson["application"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert lesson["independent_mathematical_review_credit"] == "0/3"


def test_r6_derivative_and_capacity_quantifiers_constants_are_explicit() -> None:
    result = _load(LESSON)["scoped_result"]
    assert result["derivative_estimate"]["quantifiers"] == "for every k,l in Z_ge_0"
    assert result["derivative_estimate"]["bound"] == (
        "||nabla^k partial_t^l u||_infinity <= C_{k,l} M^(k+2l+1)"
    )
    assert result["temporal_vorticity_constant"] == (
        "K:=||partial_t omega||_infinity <= C_omega M^4"
    )
    capacity = result["fixed_time_capacity"]
    assert capacity["quantifiers"] == (
        "for every t<0, x0 in R^3, lambda>0, and R>0"
    )
    assert capacity["delta_when_K_positive"] == "min(R^2,lambda/(2K))"
    assert capacity["delta_when_K_zero"] == "R^2"
    assert capacity["all_radius_bound"] == (
        "|S_lambda(t) intersect B(x0,R)| <= 8 I R/(lambda^2 delta)"
    )
    assert capacity["large_radius_condition"] == "K>0 and R^2>=lambda/(2K)"
    assert capacity["large_radius_bound"] == (
        "|S_lambda(t) intersect B(x0,R)| <= 16 I K R lambda^(-3) <= C I M^4 R lambda^(-3)"
    )
    assert capacity["K_zero_consequence"] == (
        "|S_lambda(t) intersect B(x0,R)| <= 8 I/(lambda^2 R), hence omega=0"
    )


def test_r6_lesson_has_exactly_seven_ordered_math_fields() -> None:
    fields = _load(LESSON)["seven_field_math_lesson"]
    assert list(fields) == [
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "falsifier",
        "mathematical_repair",
        "proof_and_source_evidence",
    ]
    assert "unbounded observation-radius factor" in fields["exact_result_or_failure"]
    assert "not uniformly weaker" in fields["supported_and_competing_causes"]
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in fields["scope"]


def test_r6_sources_bind_knss_restart_and_albritton_barker_ledger() -> None:
    source = _load(SOURCE)
    assert source["unit_id"] == UNIT_ID
    by_role = {entry["role"]: entry for entry in source["sources"]}
    assert by_role["BOUNDED_MILD_SMOOTHING"]["arxiv"] == "0709.3599"
    assert by_role["BOUNDED_MILD_SMOOTHING"]["locator"] == "Section 4, Proposition 4.1"
    assert by_role["ANCIENT_MILD_RESTART_CLASS"]["locator"] == "Section 6, ancient mild solution definition"
    assert by_role["FINITE_I_DISSIPATION_LEDGER"]["arxiv"] == "1811.00502v2"
    assert by_role["FINITE_I_DISSIPATION_LEDGER"]["locator"] == "equations (1.1)-(1.5)"
    assert source["direct_calculation"]["curl_bound"] == "|curl u|^2 <= 2|nabla u|^2"


def test_r6_packet_witness_and_pending_overlap_receive_no_extra_credit() -> None:
    lesson = _load(LESSON)
    witness = lesson["attached_representation_witness"]
    assert witness["realization_domain"] == "AMBIENT_REPRESENTATION"
    assert witness["separate_credit_units"] == 0
    assert witness["not_claimed"] == [
        "Navier-Stokes solution",
        "suitable local-energy solution",
        "Albritton-Barker blow-up limit",
        "PDE impossibility theorem",
    ]
    overlaps = lesson["pending_overlap_disposition"]
    assert overlaps["pr310"]["state"] == "OPEN_DRAFT_PENDING_NOT_MERGED"
    assert overlaps["pr310"]["separate_r6_credit_units"] == 0
    assert overlaps["r7"]["state"] == "PENDING_BRANCH_NOT_MERGED"
    assert overlaps["r7"]["separate_r6_credit_units"] == 0
    assert lesson["deduplication"]["global_failure_cause_added"] is False
    assert lesson["deduplication"]["global_ledger_updated"] is False


def test_r6_generic_containers_do_not_claim_taskepisode_identity_or_candidate_status() -> None:
    for path in (SOURCE, LESSON):
        value = _load(path)
        for forbidden in ("episode_id", "task_id", "storage_admission"):
            assert not _contains_key(value, forbidden)
    candidate = NS / "04_candidates/NS-B1a3b1a2a_R6_ANCIENT_SMOOTHING_LINEAR_PACKET_CAPACITY_20260812.md"
    assert not candidate.exists()
    cross = ROOT / "research/real_math/millennium/cross_problem/07_memory"
    assert not (cross / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_NS_R6_SUCCESSOR_20260812.json").exists()
