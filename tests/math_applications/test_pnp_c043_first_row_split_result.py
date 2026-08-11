"""Assurance checks for C043 finite mathematical receipts.

Passing these tests supplies no proof, optimum, recurrence, circuit, novelty,
review-independence, or P-versus-NP authority.  Mathematical authority comes
only from the explicit finite proofs and witnesses in the result artifact.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
GATE = PNP / "05_falsification/c043_first_row_split_gate.py"
RECEIPT = PNP / "05_falsification/C043_FIRST_ROW_SPLIT_RECEIPT_20260812.json"
RESULT = PNP / "04_candidates/C043_FIRST_ROW_SPLIT_RESULT_20260812.md"
FAILURE = PNP / "07_memory/O9d12a2a1b_C043_FIRST_ROW_SPLIT_FAILURE_DELTA_20260812.json"
TOOL_DELTA = PNP / "07_memory/O9d12a2a1b_C043_POST_RESULT_TOOL_REUSE_DELTA_20260812.json"
LENGTH_REVIEW = PNP / "08_reviews/O9d12a2a1b_C043_LENGTH_PNT_RESIDUAL_HOSTILE_REVIEW_20260812.json"
TYPE_REVIEW = PNP / "08_reviews/O9d12a2a1b_C043_ACCUMULATED_TWINS_POLARITY_HOSTILE_REVIEW_20260812.json"
TRACE = PNP / "09_trace/O9d12a2a1b_C043_FINAL_TRACE_20260812.json"
FEEDBACK = PNP / "10_feedback/C043_BIDIRECTIONAL_TWIN_GATE_FEEDBACK_20260812.json"


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _load_gate():
    spec = importlib.util.spec_from_file_location("c043_result", GATE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_receipt_is_exact_frozen_result_and_reproduces() -> None:
    gate = _load_gate()
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    assert receipt["artifact_hash"] == (
        "sha256:640122c54b0e7edc187405b232cbbf1bd28f3954f305d7609446f7d69ba697d2"
    )
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    assert gate.build_receipt() == receipt

    classes = receipt["length_classes"]
    assert [(row["word_length"], row["canonical_parameter_pairs"]) for row in classes] == [
        (26, [[4, 1], [5, 1], [6, 1], [7, 1]]),
        (28, []),
        (30, [[1, 3]]),
    ]
    assert [row["canonical_unsat_count"] for row in classes] == [0, 0, 42]
    assert receipt["scope"]["runs_full_cover_LP"] is False
    assert receipt["scope"]["computation_is_proof"] is False
    assert receipt["scope"]["grants_p_vs_np_authority"] is False


def test_exact_residual_and_suffix_neighborhood_classes() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    band = receipt["parent_15_new_band"]
    assert band["active_rows"] == [29402, 29403, 29406, 29407]
    residuals = {row["row"]: row["suffixes"] for row in band["row_residuals"]}
    assert [len(residuals[row]) for row in band["active_rows"]] == [17, 4, 4, 17]
    assert residuals[29403] == residuals[29406]
    assert 22015 in residuals[29402] and all(
        22015 not in residuals[row] for row in [29403, 29406, 29407]
    )
    assert 30037 in residuals[29407] and all(
        30037 not in residuals[row] for row in [29402, 29403, 29406]
    )
    assert all(21887 in residuals[row] for row in band["active_rows"])
    assert band["distinct_row_residual_count"] == 3

    column_classes = [
        (item["rows"], item["suffix_count"])
        for item in band["suffix_neighborhood_classes"]
    ]
    assert column_classes == [
        ([29402], 13),
        ([29402, 29403, 29406, 29407], 4),
        ([29407], 13),
    ]
    assert band["distinct_nonempty_column_neighborhood_count"] == 3


def test_accumulated_G16_types_and_upper_polarity_are_exactly_scoped() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    g16 = receipt["full_accumulated_G16"]
    assert g16["side"] == 65536
    assert g16["complement_edge_count"] == 62
    assert (g16["row_type_count"], g16["column_type_count"]) == (8, 8)
    assert g16["quotient_complement_edge_count"] == 10
    assert g16["type_class_rectangle_upper_bound"] == 8
    assert g16["rho_upper_bound_by_type_classes"] == 8
    assert receipt["scope"]["grants_quotient_cover_optimum"] is False
    assert receipt["scope"]["grants_uniform_type_growth"] is False
    assert receipt["scope"]["grants_recurrence"] is False

    result = RESULT.read_text(encoding="utf-8")
    assert "semantic multiplicity or multi-row support forces coercive cover growth" in result
    assert "This is an upper bound only" in result
    assert "assurance only and earn zero mathematical saturation credit" in result


def test_failure_reviews_tool_feedback_and_trace_preserve_math_assurance_split() -> None:
    failure = json.loads(FAILURE.read_text(encoding="utf-8"))
    failure_schema = json.loads(
        (ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        failure_schema, format_checker=jsonschema.FormatChecker()
    ).validate(failure)
    assert failure["links"] == []
    assert len(failure["experiences"]) == 1
    experience = failure["experiences"][0]
    assert experience["failure_id"] == "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING"
    assert experience["artifact_hash"] == _canonical_hash(experience)
    assert any("rho(G16)<=8" in item for item in experience["residual_signature"])

    for path in [LENGTH_REVIEW, TYPE_REVIEW]:
        review = json.loads(path.read_text(encoding="utf-8"))
        assert review["artifact_hash"] == _canonical_hash(review)
        assert review["authority"]["independent_peer_review"] is False
        assert review["authority"]["grants_p_vs_np_authority"] is False
    type_review = json.loads(TYPE_REVIEW.read_text(encoding="utf-8"))
    assert type_review["verdict"] == "ACCEPT_FINITE_UPPER_BOUND_ONLY"
    assert type_review["authority"]["grants_quotient_cover_optimum"] is False

    tool = json.loads(TOOL_DELTA.read_text(encoding="utf-8"))
    assert tool["artifact_hash"] == _canonical_hash(tool)
    assert tool["tool_id"] == "T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND"
    assert tool["reuse_status"] == "SUCCESSFUL_SCOPED_REUSE_WITHOUT_AUTHORITY_EXPANSION"
    assert tool["authority_after_reuse"] == "CONDITIONALLY_REUSABLE"

    feedback = json.loads(FEEDBACK.read_text(encoding="utf-8"))
    assert feedback["artifact_hash"] == _canonical_hash(feedback)
    assert feedback["mathematical_saturation_credit"] is True
    assert feedback["software_assurance_saturation_credit"] is False
    zero_credit = feedback["saturation_credit_policy"]["assurance_only_zero_credit"]
    assert "CI" in zero_credit and "schemas" in zero_credit and "hashes" in zero_credit

    trace = json.loads(TRACE.read_text(encoding="utf-8"))
    trace_schema = json.loads(
        (ROOT / "framework/RAKL/schemas/math-research-trace.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        trace_schema, format_checker=jsonschema.FormatChecker()
    ).validate(trace)
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        assert entry["artifact_hash"] == _canonical_hash(entry)
        previous = entry["artifact_hash"]
    assert [entry["event_type"] for entry in trace["entries"]] == [
        "FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"
    ]
    assert "review_independence:false" in trace["entries"][-1]["outputs"]
    assert "software_assurance_math_credit:false" in trace["entries"][-1]["outputs"]
    assert "root_authority:none" in trace["entries"][-1]["outputs"]
    assert all(entry["event_type"] != "PROMOTED" for entry in trace["entries"])
