"""Assurance checks for the exact C041 mathematical result receipt."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
RECEIPT_PATH = PNP / "05_falsification/C041_FX_SAT_EXACT_GATE_RECEIPT_20260812.json"
FAILURE_PATH = PNP / "07_memory/O9d12a2a1b_C041_ZERO_AUGMENTATION_FAILURE_DELTA_20260812.json"
TRACE_PATH = PNP / "09_trace/O9d12a2a1b_C041_RESULT_TRACE_20260812.json"
FINAL_TRACE_PATH = PNP / "09_trace/O9d12a2a1b_C041_FINAL_TRACE_20260812.json"
SPARSE_FAILURE_PATH = PNP / "07_memory/O9d12a2a1b_C041_SPARSE_WITNESS_FAILURE_DELTA_20260812.json"
BRIDGE_REVIEW_PATH = PNP / "08_reviews/O9d12a2a1b_C041_FX_SAT_BRIDGE_PROOF_REVIEW_20260812.json"
ZERO_REVIEW_PATH = PNP / "08_reviews/O9d12a2a1b_C041_FX_SAT_ZERO_HOSTILE_REVIEW_20260812.json"


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _q(numerator: int, denominator: int = 1) -> dict[str, int]:
    return {"numerator": numerator, "denominator": denominator}


def test_exact_receipt_proves_seed_equality_and_fixed_mass_zero_only() -> None:
    receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    assert receipt["freeze_commit"] == "4627ae32e2d3660a86cc12d327592577adc25e5f"
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    assert receipt["added_complement"] == [[0, 4]]

    seed = receipt["seed_exact_recheck"]
    assert seed["relevant_semifilter_families_equal"] is True
    assert seed["original_relevant_semifilter_count"] == 19
    assert seed["square_seed_relevant_semifilter_count"] == 19
    assert seed["primal_total"] == seed["dual_total"] == _q(3, 2)
    assert seed["exact_optimum"] == _q(3, 2)

    gate = receipt["finite_gate"]
    assert gate["status"] == "FAIL"
    assert gate["mathematical_outcome"] == "FAIL_ZERO_AUGMENTATION"
    assert gate["summary"] == {
        "positive_parent_support": 3,
        "relevant_cylinder_lifts": 3,
        "irrelevant_cylinder_lifts": 0,
    }
    assert gate["maximum_lifted_pair_load"] == _q(1)
    residual = gate["residual_augmentation"]
    assert residual["exact_optimum"] == _q(0)
    assert residual["primal_total"] == residual["dual_total"] == _q(0)
    assert residual["complete_child_filter_count"] == 787
    assert residual["augmentation_support"] == []
    assert residual["cover_certificate_support"] == [
        {"e_mask": 3, "h_mask": 28, "weight": _q(1)},
        {"e_mask": 5, "h_mask": 26, "weight": _q(1)},
    ]
    assert receipt["scope"]["magic_coded_sat_slice_evaluated"] is False
    assert receipt["scope"]["grants_p_vs_np_authority"] is False


def test_failure_delta_is_math_only_scoped_and_schema_valid() -> None:
    failure = json.loads(FAILURE_PATH.read_text(encoding="utf-8"))
    schema = json.loads(
        (ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(schema).validate(failure)
    experience = failure["experiences"][0]
    assert experience["failure_id"] == (
        "F-C041-FX-SAT-FIRST-STEP-ZERO-AUGMENTATION"
    )
    assert experience["artifact_hash"] == _canonical_hash(experience)
    assert "the exact lifted parent dual weights are retained" in experience[
        "scope_conditions"
    ]
    assert any(
        "delta_2^*=0" in signature
        for signature in experience["residual_signature"]
    )


def test_result_trace_records_result_and_residual_without_root_promotion() -> None:
    trace = json.loads(TRACE_PATH.read_text(encoding="utf-8"))
    schema = json.loads(
        (ROOT / "framework/RAKL/schemas/math-research-trace.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(trace)
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        previous = entry["artifact_hash"]
    assert [entry["event_type"] for entry in trace["entries"][-3:]] == [
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]
    assert "root_authority:none" in trace["entries"][-1]["outputs"]
    assert all(entry["event_type"] != "PROMOTED" for entry in trace["entries"])


def test_sparse_failure_is_preserved_and_reviews_resolve_only_the_bridge() -> None:
    schema = json.loads(
        (ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json").read_text(
            encoding="utf-8"
        )
    )
    sparse_failure = json.loads(SPARSE_FAILURE_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(sparse_failure)
    experience = sparse_failure["experiences"][0]
    assert experience["failure_id"] == (
        "F-C041-DECLARED-VARIABLE-WITNESS-BLOWUP"
    )
    assert experience["artifact_hash"] == _canonical_hash(experience)

    bridge = json.loads(BRIDGE_REVIEW_PATH.read_text(encoding="utf-8"))
    zero = json.loads(ZERO_REVIEW_PATH.read_text(encoding="utf-8"))
    assert bridge["artifact_hash"] == _canonical_hash(bridge)
    assert zero["artifact_hash"] == _canonical_hash(zero)
    addendum = bridge["repair_addendum_20260812"]
    assert addendum["final_blocker_status"]["remaining_bridge_blockers"] == []
    assert addendum["final_blocker_status"]["candidate_changed"] is False
    assert zero["authority_contract"]["grants_reoptimized_child_optimum"] is False
    assert zero["authority_contract"]["grants_p_vs_np_root_authority"] is False


def test_final_trace_records_same_context_review_without_promotion() -> None:
    trace = json.loads(FINAL_TRACE_PATH.read_text(encoding="utf-8"))
    schema = json.loads(
        (ROOT / "framework/RAKL/schemas/math-research-trace.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(trace)
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        previous = entry["artifact_hash"]
    last = trace["entries"][-1]
    assert last["event_type"] == "REVIEWED"
    assert "sparse_bridge:ACCEPTED" in last["outputs"]
    assert "review_independence:false" in last["outputs"]
    assert "root_authority:none" in last["outputs"]
    assert all(entry["event_type"] != "PROMOTED" for entry in trace["entries"])
