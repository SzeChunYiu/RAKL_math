from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = BASE / "09_trace/c052_identity_freeze_fixture.py"
CLASSIFIER = BASE / "04_candidates/O9d12a2a1b_C052_TARGET_BLIND_CLASSIFIER_IDENTITY_20260812.json"
FALSIFIER = BASE / "05_falsification/O9d12a2a1b_C052_INDEPENDENT_HOSTILE_FALSIFIER_IDENTITY_20260812.json"
FREEZE = BASE / "09_trace/O9d12a2a1b_C052_CLASSIFIER_FALSIFIER_IDENTITY_FREEZE_20260812.json"
REVALIDATION = BASE / "09_trace/O9d12a2a1b_C052_FRAMEWORK_REVALIDATION_EA607C8_20260812.json"
TRACE = BASE / "09_trace/O9d12a2a1b_C052_CLASSIFIER_IDENTITY_FREEZE_TRACE_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_identity_freeze", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def raw_sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def test_c052_identity_artifacts_match_serializer_and_remain_inert() -> None:
    classifier, falsifier, revalidation, trace, freeze = module().build()
    assert load(CLASSIFIER) == classifier
    assert load(FALSIFIER) == falsifier
    assert load(REVALIDATION) == revalidation
    assert load(TRACE) == trace
    assert load(FREEZE) == freeze
    assert classifier["status"] == falsifier["status"] == "FROZEN_NOT_EXECUTED"
    assert classifier["identity_kind"] == "INERT_DATA_ONLY_CLASSIFIER_SPECIFICATION"
    assert falsifier["identity_kind"] == "INERT_DATA_ONLY_FALSIFIER_SPECIFICATION"
    assert freeze["chronology"] == {
        "classifier_executed": False,
        "decoder_sat_overlap_accessed": False,
        "falsifier_executed": False,
        "hostile_cell_materialized": False,
        "new_k_enumerated": False,
        "result_accessed": False,
        "target_k_selected": False,
    }
    assert trace["entries"][-1]["event_type"] == "CANDIDATE_PROPOSED"
    assert trace["entries"][-1]["timestamp"] == "2026-08-12T12:31:24Z"
    assert trace["entries"][-1]["previous_event_hash"] == trace["entries"][-2]["artifact_hash"]
    assert trace["entries"][-1]["outputs"][-1] == "ZERO_MATHEMATICAL_RESULT_CREDIT"


def test_c052_identities_are_distinct_and_bound_to_actual_bytes() -> None:
    freeze = load(FREEZE)
    assert freeze["identities"]["classifier"]["raw_sha256"] == raw_sha(CLASSIFIER)
    assert freeze["identities"]["falsifier"]["raw_sha256"] == raw_sha(FALSIFIER)
    assert raw_sha(CLASSIFIER) != raw_sha(FALSIFIER)
    assert freeze["identities"]["distinct_raw_identities"] is True
    hostile = bytearray(CLASSIFIER.read_bytes())
    hostile[-2] = ord(" ")
    assert "sha256:" + hashlib.sha256(hostile).hexdigest() != freeze["identities"]["classifier"]["raw_sha256"]


def test_c052_classifier_is_total_over_exact_four_branches() -> None:
    classifier = load(CLASSIFIER)
    assert list(classifier["total_result_algebra"]["branches"]) == [
        "CANNOT_CHECK",
        "ESCAPE_ADMISSIBLE",
        "FORCED_CONFLICT",
        "UNRESOLVED",
    ]
    assert classifier["total_result_algebra"]["exactly_one_branch_required"] is True
    algebra = classifier["total_result_algebra"]
    assert algebra["partition_rule"].startswith("First validate the input")
    assert "no supported-cell semantic branch is reached" in algebra["branches"]["CANNOT_CHECK"]
    assert algebra["branches"]["UNRESOLVED"].startswith("The input and support proof are valid")
    domain = classifier["domain"]
    assert "h[0]=1 is prepended; c[0]=x[k]=h[1]" in domain["derived_equalities"]
    assert any("every legal literal variable index" in item for item in domain["quantifiers"])
    assert "choose padding rather than derive it" in domain["forbidden_domain_shortcuts"]


def test_c052_regressions_and_hostile_escape_world_are_mandatory_but_unrun() -> None:
    classifier = load(CLASSIFIER)
    falsifier = load(FALSIFIER)
    freeze = load(FREEZE)
    assert [world["world_id"] for world in classifier["mandatory_regression_worlds"]] == [
        "C050-k15-bounded-regression",
        "C051-k19-bounded-regression",
    ]
    assert all(world["expected_branch"] == "FORCED_CONFLICT" for world in classifier["mandatory_regression_worlds"])
    assert classifier["hostile_world_contract"]["expected_branch_if_certificate_valid"] == "ESCAPE_ADMISSIBLE"
    assert classifier["hostile_world_contract"]["materialization_and_execution_status"] == "NOT_MATERIALIZED_NOT_EXECUTED"
    assert falsifier["hostile_supported_escape_cell"]["cell_value_status"] == "WITHHELD_UNMATERIALIZED_UNTIL_SEPARATE_EXECUTION_AUTHORIZATION"
    assert falsifier["independence_boundary"]["specification_identity_distinct_from_classifier"] is True
    assert falsifier["independence_boundary"]["falsifier_implementation_status"].startswith("ABSENT")
    assert falsifier["independence_boundary"]["classifier_import_allowed"] is False
    assert freeze["mandatory_validation_worlds"] == [
        "C050-k15-bounded-regression",
        "C051-k19-bounded-regression",
        "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1",
    ]


def test_c052_freeze_has_zero_mathematical_credit_and_root_remains_open() -> None:
    freeze = load(FREEZE)
    assert freeze["frozen_result_branches"] == [
        "FORCED_CONFLICT",
        "ESCAPE_ADMISSIBLE",
        "UNRESOLVED",
        "CANNOT_CHECK",
    ]
    assert freeze["mathematical_state"] == {
        "candidate_is_a_theorem": False,
        "lesson_created": False,
        "mathematical_result_created": False,
        "root": "OPEN_NO_SOLUTION_CERTIFICATE",
    }
    assert freeze["credit"] == {
        "mathematical_result_units": 0,
        "same_context_review_independence": 0,
        "software_git_ci_hash_schema_chronology": 0,
    }
    assert "not independent peer review" in freeze["review_boundary"]


def test_c052_identity_freeze_framework_revalidation_is_preserved_historically() -> None:
    observation = load(REVALIDATION)
    expected = "ea607c8cd8e4fd308ea9a4e024d8c93ff87f5fda"
    assert observation["observed_current_main_sha"] == expected
    assert observation["identity_creation_authorized"] is True
    assert observation["classifier_or_falsifier_execution_authorized"] is False
    assert observation["new_k_enumeration_or_selection_authorized"] is False
    assert observation["decoder_sat_overlap_access_authorized"] is False
    assert observation["mathematical_result_credit"] == 0


def test_c052_fixture_source_has_no_classifier_or_evaluator_execution_surface() -> None:
    source = FIXTURE.read_text(encoding="utf-8")
    forbidden_definitions = ["def classify(", "def evaluate(", "def enumerate(", "decode_formula", "is_satisfiable", "materialize_complement"]
    assert not any(token in source for token in forbidden_definitions)


def test_c052_postfreeze_framework_revalidation_preserves_exact_inert_identities() -> None:
    path = BASE / "09_trace/O9d12a2a1b_C052_POSTFREEZE_FRAMEWORK_REVALIDATION_6756EBE_20260812.json"
    observation = load(path)
    assert observation["observed_current_main_sha"] == "6756ebec40b90f327d879410539f5146e188f34d"
    assert observation["classifier_raw_sha256"] == raw_sha(CLASSIFIER)
    assert observation["falsifier_raw_sha256"] == raw_sha(FALSIFIER)
    assert observation["identity_hashes_recomputed_unchanged"] is True
    assert observation["classifier_or_falsifier_execution_authorized"] is False
    assert observation["hostile_cell_materialization_authorized"] is False
    assert observation["new_k_enumeration_or_selection_authorized"] is False
    assert observation["decoder_sat_overlap_access_authorized"] is False
    assert observation["mathematical_result_credit"] == 0
    assert observation["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
