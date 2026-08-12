from __future__ import annotations

import hashlib
import importlib.util
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c052_v21_offwindow_evaluation_authorization_fixture.py"
AUTHORIZATION = PNP / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_EVALUATION_AUTHORIZATION_20260812.json"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C052_V21_OFFWINDOW_UNSAT_ANCHOR_LEMMA_FREEZE_20260812.json"
FALSIFIER = PNP / "05_falsification/O9d12a2a1b_C052_V21_OFFWINDOW_LEMMA_FALSIFIER_MANIFEST_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_offwindow_auth", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def raw_sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def test_authorization_matches_result_blind_fixture_and_merged_sources() -> None:
    authorization = load(AUTHORIZATION)
    assert authorization == module().build()
    assert authorization["application_base_commit"] == "329a69493762fc7df086c45e8d194486bcb53ef3"
    assert authorization["source_bindings"]["candidate"]["raw_sha256"] == raw_sha(CANDIDATE)
    assert authorization["source_bindings"]["falsifier"]["raw_sha256"] == raw_sha(FALSIFIER)
    chronology = authorization["chronology"]
    assert datetime.fromisoformat(chronology["candidate_freeze_public_merged_at_utc"].replace("Z", "+00:00")) < datetime.fromisoformat(chronology["authorization_frozen_at_utc"].replace("Z", "+00:00"))
    assert chronology["evaluation_may_begin_only_after_authorization_public_merge"] is True
    assert chronology["proof_or_falsifier_executed_in_this_round"] is False
    assert chronology["formula_witness_constructed_in_this_round"] is False
    assert chronology["k31_regression_executed_in_this_round"] is False
    assert chronology["result_or_label_accessed_in_this_round"] is False


def test_authorization_preserves_exact_O1_O13_and_marginal_scope() -> None:
    authorization = load(AUTHORIZATION)
    candidate = load(CANDIDATE)
    obligations = authorization["authorized_after_public_merge"]["proof_obligations_in_exact_order"]
    assert obligations == candidate["proof_obligations_for_future_authorized_check"]
    assert [item.split("_", 1)[0] for item in obligations] == [f"O{i}" for i in range(1, 14)]
    assert authorization["marginal_not_independent_caveat"] == candidate["marginal_not_independent_caveat"]
    assert "all 2^7 window patterns occur" in authorization["marginal_not_independent_caveat"]["not_asserted"]


def test_k31_is_authorized_only_as_public_regression_and_sensitive_lanes_are_forbidden() -> None:
    authorization = load(AUTHORIZATION)
    k31 = authorization["authorized_after_public_merge"]["public_k31_regression"]
    assert k31["authorized"] is True
    assert k31["public_only_not_hidden_validation"] is True
    assert k31["expected_parent_cell"]["k"] == 31
    assert k31["required_current_encoded_length"] == 64
    assert k31["must_discharge_obligations"] == ["O10", "O11", "O12"]
    assert k31["consumed_k20_not_reused_as_hidden_validation"] is True
    assert authorization["forbidden_capabilities"][:3] == [
        "overlap comparison or execution",
        "native parametric target selection or execution",
        "hidden-world materialization, label access, or execution",
    ]


def test_authorization_has_no_result_or_mathematical_credit_and_seal_is_exact() -> None:
    authorization = load(AUTHORIZATION)
    assert authorization["result_state"] == "UNEVALUATED"
    assert authorization["credit"] == {
        "independent_review": 0,
        "mathematical_result": 0,
        "mathematical_saturation": 0,
        "software_process": 0,
    }
    assert authorization["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    claimed = authorization["artifact_hash"]
    payload = dict(authorization)
    payload.pop("artifact_hash")
    expected = "sha256:" + hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    assert claimed == expected
