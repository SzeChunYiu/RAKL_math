from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/rh_ana003j_d001_jy_pre_candidate_fixture.py"
PATHS = {
    "source": ROOT / "research/real_math/millennium/riemann_hypothesis/01_frontier/RH_ANA_003j_D001_JY_SOURCE_ASSIMILATION_PACKET_20260812.json",
    "context": ROOT / "research/real_math/millennium/riemann_hypothesis/01_frontier/RH_ANA_003j_D001_JY_MATH_CONTEXT_FIBER_20260812.json",
    "failure": ROOT / "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_003j_D001_JY_PRIOR_FAILURE_ASSIMILATION_20260812.json",
    "memory": ROOT / "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_003j_D001_JY_RESEARCH_MEMORY_REVIEW_20260812.json",
    "expert": ROOT / "research/real_math/millennium/riemann_hypothesis/08_reviews/RH_ANA_003j_D001_JY_EXPERT_SOURCE_ASSIMILATION_REVIEW_20260812.json",
    "shortcut": ROOT / "research/real_math/millennium/riemann_hypothesis/08_reviews/RH_ANA_003j_D001_JY_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "trace": ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/RH_ANA_003j_D001_JY_PRE_CANDIDATE_TRACE_20260812.json",
}


def fixture():
    spec = importlib.util.spec_from_file_location("rh_jy_fixture", FIXTURE)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(value: dict, schema_name: str) -> None:
    schema = load(ROOT / "framework/RAKL/schemas" / schema_name)
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(value)


def test_fixture_reproduces_all_frozen_artifacts_and_hashes() -> None:
    module = fixture()
    expected = module.build_all()
    assert set(expected) == {str(path.relative_to(ROOT)) for path in PATHS.values()}
    for relative, value in expected.items():
        assert load(ROOT / relative) == value
    assert expected[module.SOURCE_PACKET]["artifact_hash"] == module.canonical_hash(expected[module.SOURCE_PACKET])
    assert expected[module.CONTEXT]["packet_hash"] == module.canonical_hash(expected[module.CONTEXT], "packet_hash")
    for relative in (module.FAILURE_ASSIMILATION, module.MEMORY, module.EXPERT, module.SHORTCUT):
        assert expected[relative]["artifact_hash"] == module.canonical_hash(expected[relative])
    previous = ""
    for event in expected[module.TRACE]["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == module.canonical_hash(event)
        previous = event["artifact_hash"]


def test_framework_schemas_accept_context_memory_shortcut_and_trace() -> None:
    validate(load(PATHS["context"]), "math-context-fiber.schema.json")
    validate(load(PATHS["memory"]), "research-memory-review.schema.json")
    validate(load(PATHS["shortcut"]), "obstruction-transformation-review.schema.json")
    validate(load(PATHS["trace"]), "math-research-trace.schema.json")


def test_primary_source_and_exact_normalization_are_bound() -> None:
    source = load(PATHS["source"])
    primary = source["primary_source"]
    assert primary["arxiv"] == "2204.01980v2 [math.NT]"
    assert primary["pdf_sha256"] == "565993a6def48b237a68a92acba604f2c42f99165e0e71e390f8e21a313b74b2"
    assert "Theorem 1.1" in primary["exact_anchors"][0]
    assert "equation (1.3)" in primary["exact_anchors"][1]
    assert "Table 1" in primary["exact_anchors"][2]
    assert primary["exposed_constants"] == {
        "amplitude": 9.39,
        "log_power": 1.515,
        "sqrt_log_decay": 0.8274,
        "x_threshold": 2,
    }
    normalization = source["normalization_binding"]
    assert normalization["application_delta"] == "Delta(x)=|psi(x)-x|/x"
    assert normalization["application_cumulative_source"] == "A(x)=floor(x)-psi(x)"
    assert normalization["normalization_status"] == "EXACTLY_COMPATIBLE_AFTER_FLOOR_ERROR_ONE"


def test_simple_domination_constant_is_safe_and_optimizer_has_no_extra_two() -> None:
    source = load(PATHS["source"])
    simple = source["prospective_candidate_families"]["simple_domination_cross_check_family"]
    assert simple["chosen_constants"] == {
        "effective_amplitude": 172,
        "sqrt_log_decay": 0.4,
        "x_threshold": 2,
    }
    decay_gap = 0.8274 - 0.4
    optimizer = 3.03 / decay_gap
    exact_supremum = 9.39 * (optimizer**3.03) * math.exp(-decay_gap * optimizer)
    assert 171.43 < exact_supremum < 172
    assert "3.03 already equals 2*1.515" in simple["optimizer_guard"]


def test_direct_integral_and_monotonicity_family_are_pre_candidate_only() -> None:
    source = load(PATHS["source"])
    families = source["prospective_candidate_families"]
    direct = families["preferred_direct_jy_family"]
    assert "2j+5.03" in direct["integral_identity"]
    assert "18.78" in direct["envelope_formula"]
    assert "2(n-1+1.515)/0.8274" in direct["monotonicity_floor_proposal"]
    assert families["candidate_identity"] is None
    assert families["candidate_generation_allowed"] is False
    assert families["selected_result_branch"] is None
    firewall = source["frozen_firewall"]
    assert firewall == {
        "M_values_calculated": False,
        "numerical_remainder_tests_run": False,
        "epsilon_sequence_identity": None,
        "diagonal_cutoff_constant_identity": None,
        "diagonal_comparison_attempted": False,
        "candidate_id": None,
    }


def test_bellotti_negative_history_and_invalid_mixed_transfers_are_preserved() -> None:
    source = load(PATHS["source"])
    bellotti = source["source_branch_classification"]["bellotti_v1"]
    assert bellotti["status"] == "EFFECTIVE_BUT_CONSTANT_AND_THRESHOLD_UNEXPOSED_IN_ACQUIRED_TEXT"
    assert bellotti["ineffectivity_claimed"] is False
    invalid = " ".join(source["invalid_mixed_source_transfers"])
    assert "exp(55A_0)" in invalid
    assert "Bellotti's Vinogradov--Korobov decay" in invalid
    assert "Dropping the factor (log x)^1.515" in invalid
    failure = load(PATHS["failure"])
    fields = failure["seven_field_assimilation"]
    assert set(fields) == {
        "attempted_mathematical_implication",
        "exact_result_or_failure",
        "supported_and_competing_mathematical_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_discriminator",
        "proof_or_source_evidence",
    }
    assert failure["append_only_disposition"].startswith("PRESERVE_PRIOR_BYTES")
    assert failure["authority"]["bellotti_ineffectivity_claimed"] is False


def test_trace_is_exact_pre_candidate_order_and_zero_software_credit() -> None:
    source, trace = load(PATHS["source"]), load(PATHS["trace"])
    assert [event["event_type"] for event in trace["entries"]] == [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert all("NO_CANDIDATE_IDENTITY" in event["outputs"] for event in trace["entries"])
    assert all("SOFTWARE_CREDIT_ZERO" in event["outputs"] for event in trace["entries"])
    authority = source["authority"]
    assert authority["software_or_governance_credit_units"] == 0
    assert authority["mathematical_result_generated"] is False
    assert authority["root_solution_authority"] is False
    review = load(PATHS["expert"])
    assert review["review_authority"] == "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT_REVIEW"
    shortcut = load(PATHS["shortcut"])
    assert shortcut["selected_mode"] == "SEARCH"
    assert shortcut["direct_search_status"] == "MATCHES_FOUND"
    assert shortcut["jump_search_status"] == "NOT_RUN"
    assert shortcut["glue_search_status"] == "NOT_RUN"
