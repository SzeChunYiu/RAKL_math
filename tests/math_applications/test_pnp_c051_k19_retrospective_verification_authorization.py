from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/p_vs_np/09_trace/c051_k19_retrospective_verification_authorization_fixture.py"
RECORD = ROOT / "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C051_K19_RETROSPECTIVE_VERIFICATION_AUTHORIZATION_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c051_k19_retrospective_auth", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def test_authorization_matches_fixture_and_preserves_contamination() -> None:
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    assert record == module().build()
    chronology = record["chronology"]
    assert chronology["verification_executed_in_this_round"] is False
    assert chronology["parallel_uncommitted_result_shaped_artifacts_observed_before_authorization"] is True
    assert chronology["result_value_inspected_for_this_authorization"] is False
    assert chronology["prospective_result_credit_permanently_forfeited"] is True
    assert record["mathematical_credit"] == 0
    assert record["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_authorization_binds_exact_merged_candidates_and_evaluator() -> None:
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    assert {row["candidate_id"] for row in record["candidate_bindings"]} == {
        "C051-K19-TARGET-BLIND-SYNCHRONIZED-DISCRIMINATOR-v1",
        "C051-K19-RETROSPECTIVE-SUPPORT-DISCRIMINATOR-v1",
    }
    assert record["evaluator_binding"]["raw_sha256"] == "sha256:0b21232a509ecd525e000840d490c4294f23ea7f053b117ff746f87fe13f72cc"
    assert any("retrospective verification" in action for action in record["licensed_after_public_merge"])
