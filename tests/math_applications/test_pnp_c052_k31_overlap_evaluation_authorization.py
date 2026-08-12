from __future__ import annotations

import importlib.util
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c052_k31_overlap_evaluation_authorization_fixture.py"
AUTHORIZATION = PNP / "09_trace/O9d12a2a1b_C052_K31_OVERLAP_EVALUATION_AUTHORIZATION_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_k31_eval_auth", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_authorization_matches_fixture_and_exact_public_identities() -> None:
    authorization = load(AUTHORIZATION)
    assert authorization == module().build()
    assert authorization["application_base_sha"] == "c8c8501105ed952dc9773f7e93dfd5418eb1c80c"
    assert authorization["exact_identity_bindings"] == module().BINDINGS
    assert authorization["candidate_id"] == module().CANDIDATE_ID
    assert authorization["falsifier_id"] == module().FALSIFIER_ID


def test_authorization_is_result_blind_and_only_licenses_post_merge_work() -> None:
    authorization = load(AUTHORIZATION)
    chronology = authorization["chronology"]
    assert datetime.fromisoformat(chronology["candidate_freeze_public_merged_at_utc"].replace("Z", "+00:00")) < datetime.fromisoformat(authorization["frozen_at_utc"].replace("Z", "+00:00"))
    assert chronology["implementation_and_execution_may_begin_only_after_this_authorization_is_publicly_merged"] is True
    assert chronology["implementation_exists_in_this_round"] is False
    assert chronology["validation_world_materialized_in_this_round"] is False
    assert chronology["formula_label_or_certificate_constructed_in_this_round"] is False
    assert chronology["SAT_UNSAT_or_overlap_executed_in_this_round"] is False
    assert chronology["result_or_branch_accessed_in_this_round"] is False
    assert authorization["result_state"] == "UNEVALUATED"


def test_public_validation_order_and_fail_closed_actual_k31_gate_are_exact() -> None:
    authorization = load(AUTHORIZATION)
    scope = authorization["authorized_public_scope_after_merge"]
    assert scope["public_validation_worlds_in_order"] == [
        "K31-PLANTED-POSITIVE-CERTIFICATE-KERNEL-v1",
        "K31-PLANTED-NEGATIVE-CERTIFICATE-KERNEL-v1",
        "K31-MALFORMED-CERTIFICATE-CANNOT-CHECK-v1",
        "K31-MARGINAL-ONLY-FALSE-POSITIVE-v1",
        "K31-SOURCE-BINDING-MISMATCH-v1",
        "K31-FRONTEND-KERNEL-BRANCH-PROPAGATION-v1",
    ]
    assert scope["actual_public_k31_evaluation"].startswith("only after every public")
    assert scope["actual_result_branches"] == [
        "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE",
        "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE",
        "CANNOT_CHECK",
    ]
    assert authorization["fail_closed_stop_rules"]["any_public_validation_world_fails"] == "STOP_CANNOT_CHECK_NO_ACTUAL_K31_EVALUATION"


def test_hidden_native_and_root_authority_are_forbidden() -> None:
    authorization = load(AUTHORIZATION)
    boundary = authorization["public_only_boundary"]
    assert boundary == {
        "all_validation_inputs_and_receipts_must_be_public": True,
        "hidden_worlds_allowed": False,
        "native_parametric_expansion_allowed": False,
        "target_k": 31,
    }
    assert any("hidden-world" in item for item in authorization["forbidden"])
    assert any("beyond public k31" in item for item in authorization["forbidden"])
    assert any("root promotion" in item for item in authorization["forbidden"])
    assert authorization["credit"] == {
        "independent_review": 0,
        "mathematical_result": 0,
        "mathematical_saturation": 0,
        "software_process": 0,
    }
    assert authorization["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
