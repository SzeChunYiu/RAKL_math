from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FIXTURE = YM / "09_trace/ym_k1_d001_c001_evaluator_freeze_fixture.py"


def module():
    spec = importlib.util.spec_from_file_location("ym_k1_d001_c001_evaluator_freeze", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_evaluator_identity_and_planted_worlds_are_exact() -> None:
    f = module()
    document = f.build_document()
    assert json.loads(f.OUTPUT.read_text()) == document
    evaluator = f.EVALUATOR.read_bytes()
    assert document["evaluator_identity"]["raw_sha256"] == hashlib.sha256(evaluator).hexdigest()
    assert document["all_planted_worlds_match"] is True
    assert document["parent_main_sha"] == "aa6386126229bdfcae57fcf10a5b46ee8e91b83b"
    assert {row["observed_branch"] for row in document["planted_world_receipt"]} == {
        "APPLICABLE_BRIDGE",
        "STRONGER_PREMISE_MISMATCH_A",
        "FLOW_MARGIN_FAIL_B",
        "CANNOT_CHECK",
    }


def test_round_contains_no_target_result_and_grants_no_execution_authority() -> None:
    document = module().build_document()
    assert document["current_round_state"]["scope"] == "THIS_PUBLISHED_EVALUATOR_FREEZE_ROUND_ONLY"
    assert all(value is False for key, value in document["current_round_state"].items() if key != "scope")
    assert document["authority"]["evaluator_identity_frozen"] is True
    assert document["authority"]["licenses_target_execution"] is False
    assert document["authority"]["grants_mathematical_result_credit"] is False


def test_prior_chronology_failure_is_explicit_and_future_run_is_retrospective() -> None:
    chronology = module().build_document()["chronology_boundary"]
    assert chronology["prior_local_unpublished_result_commit"] == "25c0271d6a0f379cad4dab3c2a4be56d732f5a00"
    assert chronology["prior_local_result_access_preceded_public_evaluator_byte_freeze"] is True
    assert chronology["prior_local_source_audit_executed"] is True
    assert chronology["strict_rakl_discovery_chronology_for_prior_generation"] is False
    assert chronology["future_reproduction_must_be_labeled_retrospective_not_prospective_discovery"] is True


def test_conflated_c_branch_was_prospectively_frozen_before_local_result_access() -> None:
    binding = module().build_document()["prospective_specification_binding"]
    assert binding["candidate_core_sha256"] == "sha256:fb50ccd8ca6079c7827d812fc6d3b2cf5136cc2196ed0fb3aba9da525bdfb71e"
    assert binding["declarative_falsifier_core_sha256"] == "sha256:a0d1f2c25d7c836a047b670cc536f919497b0a7f967e3e77b4d82da22875abb5"
    assert binding["contamination_assessment"] == "GENERIC_BRANCH_LOGIC_PREEXISTED_RESULT_ACCESS; TARGET_EVIDENCE_AND_CLASSIFICATION_NOT_EMBEDDED"
    assert "c_K=4C/(1-rho)>C" in binding["prospectively_frozen_conflated_c_branch"]


def test_artifact_hash_covers_full_freeze() -> None:
    f = module()
    document = f.build_document()
    actual = document["artifact_hash"]
    unsigned = dict(document)
    unsigned["artifact_hash"] = ""
    assert actual == f.sha(unsigned)
