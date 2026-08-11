"""Assurance checks for the finite C042 mathematical receipts.

Passing these tests gives no proof, asymptotic, circuit, novelty, review-
independence, or P-versus-NP authority.  The mathematical content lives in the
explicit analytic arguments and witnesses that these checks reproduce.
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
GATE_PATH = PNP / "05_falsification/c042_activation_quotient_gate.py"
RECEIPT_PATH = PNP / "05_falsification/C042_ACTIVATION_QUOTIENT_RECEIPT_20260812.json"
WITNESS_PATH = PNP / "05_falsification/C042_QUOTIENT_PAIR_WITNESS_RECEIPT_20260812.json"
FAILURE_PATH = PNP / "07_memory/O9d12a2a1b_C042_ACTIVATION_QUOTIENT_FAILURE_DELTA_20260812.json"
ENCODING_REVIEW_PATH = PNP / "08_reviews/O9d12a2a1b_C042_ENCODING_THRESHOLD_HOSTILE_REVIEW_20260812.json"
QUOTIENT_REVIEW_PATH = PNP / "08_reviews/O9d12a2a1b_C042_STRUCTURAL_QUOTIENT_HOSTILE_REVIEW_20260812.json"
TRACE_PATH = PNP / "09_trace/O9d12a2a1b_C042_FINAL_TRACE_20260812.json"
FEEDBACK_PATH = PNP / "10_feedback/C042_SEMANTIC_ACTIVATION_GATE_FEEDBACK_20260812.json"


def _load_gate():
    spec = importlib.util.spec_from_file_location("c042_activation_result", GATE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _encoded_pairs(instance: dict) -> list[tuple[int, int]]:
    return [
        (pair["e_mask"], pair["h_mask"])
        for pair in instance["cover_pairs"]
    ]


def test_receipt_reproduces_exact_threshold_words_pairs_and_types() -> None:
    gate = _load_gate()
    receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    assert gate.build_receipt() == receipt

    thresholds = receipt["frozen_threshold_claims"]
    assert thresholds == {
        "magic_prefix_first_parent_level": 4,
        "canonical_syntax_first_parent_level": 8,
        "canonical_unsat_first_parent_level": 12,
        "canonical_unsat_equality_parameters": {"v": 1, "m": 2},
    }
    for level in receipt["levels_2_through_12"][:-1]:
        assert level["canonical_magic_unsat_words"] == []
        assert level["cross_unsat_pairs"] == [[0, 0]]

    level_12 = receipt["levels_2_through_12"][-1]
    assert level_12["canonical_magic_unsat_words"] == [
        "111001011010010101111111",
        "111001011010111111010101",
    ]
    assert level_12["cross_unsat_pairs"] == [
        [0, 0],
        [3674, 1407],
        [3674, 4053],
    ]

    g9 = receipt["first_syntax_child"]
    g13 = receipt["first_unsat_capable_child"]
    assert (g9["row_type_count"], g9["column_type_count"]) == (4, 4)
    assert (g13["row_type_count"], g13["column_type_count"]) == (5, 5)
    assert g9["quotient_complement"] == [[0, 0], [1, 2], [2, 1], [2, 2]]
    assert g13["quotient_complement"] == [
        [0, 0], [1, 2], [2, 1], [2, 2], [4, 4]
    ]
    assert g9["quotient_exact_full_cover_number"] == 2
    assert g13["quotient_exact_full_cover_number"] == 2
    assert receipt["scope"]["grants_p_vs_np_authority"] is False
    assert receipt["scope"]["computation_is_proof"] is False


def test_explicit_pair_families_cover_every_relevant_semifilter_and_one_does_not() -> None:
    gate = _load_gate()
    oracle = gate.oracle
    witness = json.loads(WITNESS_PATH.read_text(encoding="utf-8"))
    assert witness["artifact_hash"] == _canonical_hash(witness)

    for instance in witness["instances"]:
        side = instance["side"]
        complement = {tuple(edge) for edge in instance["ordered_complement"]}
        filters = oracle._relevant_semifilters(side, complement)
        pairs = _encoded_pairs(instance)
        assert len(filters) == instance["relevant_semifilter_count"]
        assert all(
            any(oracle.pair_covers_semifilter(filt, e, h) for e, h in pairs)
            for filt in filters
        )
        assert all(
            not all(oracle.pair_covers_semifilter(filt, e, h) for filt in filters)
            for e, h in pairs
        )
        assert instance["exact_full_cover_number"] == 2


def test_three_explicit_relevant_semifilters_rule_out_any_single_pair() -> None:
    gate = _load_gate()
    oracle = gate.oracle
    for side, complement in [
        (4, {(0, 0), (1, 2), (2, 1), (2, 2)}),
        (5, {(0, 0), (1, 2), (2, 1), (2, 2), (4, 4)}),
    ]:
        filters = set(oracle._relevant_semifilters(side, complement))
        # Ordered complement names a,b,c,..., so singleton masks are 1,2,4.
        obstruction_filters = {(1, 2), (1, 4), (2, 4)}
        assert obstruction_filters <= filters
        assert not any(
            all(oracle.pair_covers_semifilter(filt, e, h) for filt in obstruction_filters)
            for e in range(1 << len(complement))
            for h in range(1 << len(complement))
        )


def test_math_failure_reviews_feedback_and_trace_preserve_scope() -> None:
    failure = json.loads(FAILURE_PATH.read_text(encoding="utf-8"))
    failure_schema = json.loads(
        (ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        failure_schema, format_checker=jsonschema.FormatChecker()
    ).validate(failure)
    assert failure["links"] == []
    for experience in failure["experiences"]:
        assert experience["artifact_hash"] == _canonical_hash(experience)
        assert experience["candidate_id"] == "C042-ACTIVATION-QUOTIENT-GATE-v1"

    encoding_review = json.loads(ENCODING_REVIEW_PATH.read_text(encoding="utf-8"))
    quotient_review = json.loads(QUOTIENT_REVIEW_PATH.read_text(encoding="utf-8"))
    for review in (encoding_review, quotient_review):
        assert review["artifact_hash"] == _canonical_hash(review)
        assert review["authority"]["independent_peer_review"] is False
    assert quotient_review["conclusion"] == [
        "rho(Q9)=2",
        "rho(Q13)=2",
        "rho(G9)<=2 by C013 lift",
        "rho(G13)<=2 by C013 lift",
    ]

    feedback = json.loads(FEEDBACK_PATH.read_text(encoding="utf-8"))
    assert feedback["artifact_hash"] == _canonical_hash(feedback)
    assert feedback["mathematical_saturation_credit"] is True
    assert feedback["software_assurance_saturation_credit"] is False
    zero_credit = feedback["saturation_credit_policy"]["assurance_only_zero_credit"]
    assert "CI" in zero_credit and "schemas" in zero_credit and "observed runtime" in zero_credit

    trace = json.loads(TRACE_PATH.read_text(encoding="utf-8"))
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
    assert "root_authority:none" in trace["entries"][-1]["outputs"]
    assert all(entry["event_type"] != "PROMOTED" for entry in trace["entries"])
