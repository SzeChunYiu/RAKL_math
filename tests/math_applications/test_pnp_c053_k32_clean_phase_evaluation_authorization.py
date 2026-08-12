from __future__ import annotations

import importlib.util
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c053_k32_clean_phase_evaluation_authorization_fixture.py"
AUTHORIZATION = PNP / "09_trace/O9d12a2a1b_C053_K32_CLEAN_PHASE_EVALUATION_AUTHORIZATION_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c053_k32_eval_auth", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_authorization_matches_fixture_and_merged_candidate_identities() -> None:
    authorization = load(AUTHORIZATION)
    fixture = module()
    assert authorization == fixture.build()
    assert authorization["application_base_sha"] == "04d8ca7af5c007d3d5f93dd9f47b411a07e95822"
    assert authorization["candidate_merge_sha"] == "461393f748af13ae9500f368aefbefc0da90f715"
    assert authorization["exact_identity_bindings"] == fixture.BINDINGS


def test_authorization_checkpoint_is_result_blind_and_post_merge() -> None:
    authorization = load(AUTHORIZATION)
    chronology = authorization["chronology"]
    merged = datetime.fromisoformat(chronology["candidate_freeze_public_merged_at_utc"].replace("Z", "+00:00"))
    frozen = datetime.fromisoformat(authorization["frozen_at_utc"].replace("Z", "+00:00"))
    assert merged < frozen
    assert chronology["authorization_frozen_after_candidate_merge"] is True
    assert all(value is False for key, value in chronology.items() if key.endswith("_checkpoint") and key != "implementation_and_execution_may_begin_only_after_this_authorization_is_committed_as_a_separate_checkpoint")
    assert authorization["result_state"] == "UNEVALUATED"


def test_hand_first_world_order_and_fail_closed_contract_are_exact() -> None:
    authorization = load(AUTHORIZATION)
    scope = authorization["authorized_scope_after_checkpoint"]
    assert scope["public_validation_worlds_in_order"] == [
        "C053-CLEAN-PHASE-PLANTED-POSITIVE-v1",
        "C053-CLEAN-PHASE-PLANTED-NEGATIVE-v1",
        "C053-CLEAN-PHASE-SYNTAX-SURVIVAL-ONLY-v1",
        "C053-CLEAN-PHASE-PARTIAL-EQUALITY-v1",
        "C053-CLEAN-PHASE-SAT-PARENT-FALSE-POSITIVE-v1",
        "C053-CLEAN-PHASE-INCOMPLETE-PAIR-COVERAGE-v1",
        "C053-CLEAN-PHASE-SOURCE-MISMATCH-v1",
        "C053-CLEAN-PHASE-CONFLICTING-CERTIFICATES-v1",
        "C053-CLEAN-PHASE-FRONTEND-BRANCH-PROPAGATION-v1",
    ]
    assert scope["actual_32_pair_evaluation"].startswith("only after the hand certificate")
    assert authorization["fail_closed_stop_rules"]["any_public_validation_world_fails"] == "STOP_CANNOT_CHECK_NO_ACTUAL_C053_EVALUATION"


def test_scope_preserves_exact_pair_set_and_open_root() -> None:
    authorization = load(AUTHORIZATION)
    boundary = authorization["public_only_boundary"]
    assert boundary["target_k"] == 32
    assert boundary["parameter_pair_count"] == 32
    assert boundary["hidden_worlds_allowed"] is False
    assert boundary["native_parametric_expansion_allowed"] is False
    assert any("exact 32 frozen" in item for item in authorization["forbidden"])
    assert any("P-versus-NP" in item for item in authorization["forbidden"])
    assert authorization["credit"]["Git_CI_schema_hash_chronology"] == 0
    assert authorization["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
