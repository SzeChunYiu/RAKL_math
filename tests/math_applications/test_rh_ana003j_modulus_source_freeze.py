from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003j_modulus_source_freeze_fixture.py"
RECORD = RH / "09_trace/RH_ANA_003j_MODULUS_SOURCE_DISCRIMINATOR_FREEZE_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("rh_ana003j_modulus_source_freeze", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_record_exactly_matches_result_blind_fixture() -> None:
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    assert record == module().build()
    assert record["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert record["future_result_lesson_contract"]["current_status"] == "NO_RESULT_NO_LESSON"
    assert len(record["future_result_lesson_contract"]["required_seven_fields"]) == 7
    assert record["authority"]["mathematical_result_credit"] is False
    assert record["authority"]["mathematical_lesson_credit"] is False


def test_concrete_source_discriminator_and_fail_closed_target_are_frozen() -> None:
    record = module().build()
    target = record["authoritative_target_identity_audit"]
    discriminator = record["frozen_future_discriminator_identity"]
    assert target["cutoff_family_form"] == "Y_n=exp(C n^(5/3) log^2(n+e))"
    assert target["cutoff_constant_identity"] is None
    assert target["epsilon_sequence_identity"] is None
    assert target["comparison_status"].startswith("FORBIDDEN_UNTIL")
    assert discriminator["discriminator_id"] == "RH-ANA-003j-D001-C002-EXPLICIT-BOUNDARY-TAIL-MODULUS-SOURCE-AUDIT"
    assert discriminator["required_output_object"]["remainder_envelope"].startswith("B(n,Y)")
    assert len(discriminator["required_output_object"]["constant_ledger"]) == 6
    assert discriminator["selected_result_branch"] is None
    assert discriminator["source_result_access_authorized_after_public_freeze"] is True
    assert record["chronology_and_firewall"]["source_audit_executed"] is False
    assert record["chronology_and_firewall"]["comparison_M_n_epsilon_n_le_Y_n_attempted"] is False


def test_allowed_branches_distinguish_explicit_modulus_from_qualitative_decay() -> None:
    record = module().build()
    branches = record["frozen_future_discriminator_identity"]["allowed_result_branches"]
    assert branches == [
        "EXPLICIT_SOURCE_DERIVED_MODULUS_MATERIALIZED",
        "QUALITATIVE_OR_INEFFECTIVE_SOURCE_ONLY_NO_EXPLICIT_MODULUS",
        "ACQUIRED_SOURCE_SCOPE_INSUFFICIENT_FOR_ONE_OR_MORE_REQUIRED_CONSTANTS",
        "SOURCE_STATEMENT_OR_NORMALIZATION_MISMATCH",
        "CANNOT_CHECK_EXACT_SOURCE_SCOPE",
    ]
    rule = record["predeclared_branch_rules"]["EXPLICIT_SOURCE_DERIVED_MODULUS_MATERIALIZED"]
    assert "does not authorize M(n,epsilon_n)<=Y_n" in rule
    assert len(record["falsifiers"]) == 5


def test_all_parent_bindings_match_bytes_and_observed_framework_drift_is_scoped() -> None:
    fixture = module()
    record = fixture.build()
    for binding in record["chronology_and_firewall"]["parent_bindings"].values():
        assert fixture.raw_sha256(ROOT / binding["path"]) == binding["raw_sha256"]
    assert record["framework_authority"]["intervening_paths"] == [
        "research/empirical_10_of_10_v1/PAPER3/DOWNSTREAM/ROUTING_REGISTRATION_V1.md",
        "research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/ROBUSTNESS_REGISTRATION_V1.md",
    ]
    assert record["framework_authority"]["classification"] == "PAPER3_REGISTRATION_ONLY_NO_MATHEMATICAL_GATE_CHANGE"
    assert record["framework_authority"]["grants_mathematical_authority"] is False
    assert record["framework_authority"]["application_gitlink_edited"] is False
