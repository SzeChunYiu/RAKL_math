from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c046_high_half_separation_result_fixture.py"
RESULT = PNP / "05_falsification/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_PROOF_CHECK_RESULT_20260812.json"
TRACE = PNP / "09_trace/O9d12a2a1b_C046_POST_FREEZE_RESULT_TRACE_20260812.json"

PUBLIC_INPUT_FREEZE_COMMIT = "ae9c196d3f879ba6b1140af0878a416cf16df6c0"
PUBLIC_INPUT_OBSERVED_AT = "2026-08-12T02:29:52Z"


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_c046_result_matches_exact_post_public_freeze_fixture() -> None:
    fixture = _module("pnp_c046_result_fixture", FIXTURE)
    expected = fixture.build_documents(ROOT)
    assert _load(RESULT) == expected["result"]
    assert _load(TRACE) == expected["trace"]

    result = expected["result"]
    exposure = result["chronology"]["public_proof_input_freeze"]
    assert exposure["remote_head_sha"] == PUBLIC_INPUT_FREEZE_COMMIT
    assert exposure["observed_at"] == PUBLIC_INPUT_OBSERVED_AT
    assert exposure["observed_at"] < result["execution"]["executed_at"]
    assert result["evaluator_output"] == {
        "verdict": "PASS",
        "candidate_id": "C046-HIGH-HALF-SEPARATION-LEMMA-v1",
    }
    assert result["execution"]["raw_output_sha256"] == "e0e536c9c6a5460f4bd36069f9455fe3ff87b548ab44ffd9c63cb03f1d3dd23a"


def test_c046_result_preserves_target_and_authority_boundaries() -> None:
    result = _load(RESULT)
    assert result["status"] == "PASS_SAME_CONTEXT_CERTIFICATE_RECORD_CHECK"
    assert result["target_access"] == {
        "proof_obligation_evaluator_imported_and_executed": True,
        "target_decoder_imported_or_executed": False,
        "later_target_enumerated": False,
        "later_target_result_accessed": False,
        "finite_collision_level_selected": False,
    }
    assert result["interpretation"]["formal_proof_checked"] is False
    assert result["interpretation"]["semantic_derivation_independently_checked"] is False
    assert result["authority"] == {
        "same_context_hand_derivation_record_check": True,
        "theorem_truth": False,
        "formal_proof": False,
        "independent_review": False,
        "novelty": False,
        "cover_or_circuit_lower_bound": False,
        "p_vs_np_authority": False,
        "root_status": "OPEN",
    }


def test_c046_frozen_evaluator_retains_pass_fail_and_cannot_check_branches() -> None:
    fixture = _module("pnp_c046_result_fixture_branches", FIXTURE)
    certificate = _load(fixture.CERTIFICATE_PATH)
    authorization = _load(fixture.AUTHORIZATION_PATH)
    evaluator = fixture.load_exact_evaluator(ROOT)

    assert evaluator.evaluate_certificate(certificate, {}) == {
        "verdict": "CANNOT_CHECK",
        "reason": "SEPARATE_POST_FREEZE_AUTHORIZATION_REQUIRED",
    }
    refuted = json.loads(json.dumps(certificate))
    refuted["obligations"][0]["status"] = "REFUTED"
    assert evaluator.evaluate_certificate(refuted, authorization) == {
        "verdict": "FAIL",
        "falsified_obligation": "BASE_U3_ROW_PROJECTION",
    }
    assert evaluator.evaluate_certificate(certificate, authorization)["verdict"] == "PASS"


def test_c046_result_trace_appends_falsifier_and_result_events_hash_chained() -> None:
    trace = _load(TRACE)
    assert [entry["event_type"] for entry in trace["entries"][-2:]] == [
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
    ]
    assert len(trace["entries"]) == 11
    for previous, current in zip(trace["entries"], trace["entries"][1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    final = trace["entries"][-1]
    assert "PASS_SAME_CONTEXT_CERTIFICATE_RECORD_CHECK" in final["outputs"]
    assert "TARGET_RESULT_UNACCESSED" in final["outputs"]
