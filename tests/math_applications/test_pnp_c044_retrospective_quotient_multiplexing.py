"""Assurance checks for the retrospective C044 finite upper proof.

The Q16 outcome was exposed before a strict candidate freeze.  These checks
must preserve that chronology and cannot create strict discovery, proof,
review-independence, exact-lower-bound, circuit, or P-versus-NP authority.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.failure_lattice import reconstruct_failure_lattice


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
SCRIPT = PNP / "05_falsification/c044_retrospective_quotient_multiplexing.py"
RECEIPT = PNP / "05_falsification/C044_RETROSPECTIVE_Q16_MULTIPLEXING_RECEIPT_20260812.json"
RESULT = PNP / "04_candidates/C044_RETROSPECTIVE_Q16_MULTIPLEXING_RESULT_20260812.md"
FAILURE = PNP / "07_memory/O9d12a2a1b_C044_HETEROGENEOUS_MULTIPLEXING_FAILURE_DELTA_20260812.json"
TOOL = PNP / "07_memory/O9d12a2a1b_C044_RESEARCH_TOOL_PROPOSAL_DELTA_20260812.json"
PROOF_REVIEW = PNP / "08_reviews/O9d12a2a1b_C044_MULTIPLEXING_PROOF_HOSTILE_REVIEW_20260812.json"
LOWER_REVIEW = PNP / "08_reviews/O9d12a2a1b_C044_CANONICAL_LOWER_AUTHORITY_REVIEW_20260812.json"
TRACE = PNP / "09_trace/O9d12a2a1b_C044_RETROSPECTIVE_FINAL_TRACE_20260812.json"
MATH_FEEDBACK = PNP / "10_feedback/C044_COMPONENT_COUPLING_GATE_FEEDBACK_20260812.json"
LEAK_FEEDBACK = PNP / "10_feedback/C044_PARALLEL_RESULT_LEAKAGE_FEEDBACK_20260812.json"


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _load_script():
    spec = importlib.util.spec_from_file_location("c044_retrospective_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_receipt_reproduces_explicit_three_pair_upper_witness() -> None:
    module = _load_script()
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    assert receipt["artifact_hash"] == "sha256:0f726e5d6c59a26d66d68b239c17ac672e4bfb2dc7acf86c0e5d41ab698097c0"
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    assert module.build_receipt() == receipt
    assert receipt["quotient"]["complement_edge_count"] == 10
    assert receipt["quotient"]["cross_component_complement_edges"] == []
    assert receipt["quotient"]["empty_fibre_labels"] == [3]
    assert len(receipt["explicit_pairs"]) == 3
    assert all(row["disjoint"] and row["partitions_complement"] for row in receipt["explicit_pairs"])
    cover = receipt["generator_separation"]
    assert cover["relevant_graph_edge_count"] == 39
    assert cover["all_relevant_graph_edges_separated"] is True
    assert all(row["separating_pair_indices"] for row in cover["coverage"])
    assert cover["proved_upper_bound"] == "rho(Q16)<=sigma(Q16)<=3"
    assert cover["lifted_upper_bound"] == "rho(G16)<=rho(Q16)<=3"


def test_lower_value_and_discovery_chronology_fail_closed() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    chronology = receipt["chronology"]
    assert chronology == {
        "strict_pre_candidate_gate_run": False,
        "candidate_evaluator_frozen_before_output": False,
        "result_exposed_before_candidate_freeze": True,
        "strict_rakl_discovery_authority": False,
        "truth_check_may_proceed_retrospectively": True,
    }
    support = receipt["canonical_exhaustive_support"]
    assert support == {
        "canonical_graph_edges": 39,
        "distinct_maximal_pair_masks": 63,
        "minimum_pairs": 3,
        "authority": "RETROSPECTIVE_COMPUTATIONAL_CORROBORATION_NOT_PROOF",
    }
    scope = receipt["scope"]
    assert scope["proves_explicit_upper_bound_only"] is True
    assert scope["grants_exact_quotient_value"] is False
    assert scope["computation_is_proof"] is False
    assert scope["grants_p_vs_np_authority"] is False
    result = RESULT.read_text(encoding="utf-8")
    assert "does **not** receive strict context-first RAKL discovery authority" in result
    assert "no exact lower" in result and "bound is promoted" in result
    assert "rho(G_{16})\\le\\rho(Q_{16})\\le3" in result


def test_failure_reviews_tool_and_feedback_separate_math_from_assurance() -> None:
    failure = json.loads(FAILURE.read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(failure)
    assert len(failure["experiences"]) == 1
    assert failure["links"] == []
    lattice = reconstruct_failure_lattice(failure)
    assert len(lattice.experiences) == 1 and lattice.links == ()
    exp = failure["experiences"][0]
    assert exp["failure_id"] == "F-C044-HETEROGENEOUS-BLOCK-MULTIPLEXING"
    assert exp["artifact_hash"] == _canonical_hash(exp)
    assert any("rho(Q16)<=3" in item for item in exp["residual_signature"])

    proof = json.loads(PROOF_REVIEW.read_text(encoding="utf-8"))
    lower = json.loads(LOWER_REVIEW.read_text(encoding="utf-8"))
    for review in [proof, lower]:
        assert review["artifact_hash"] == _canonical_hash(review)
        assert review["authority"]["independent_peer_review"] is False
        assert review["authority"]["strict_rakl_discovery"] is False
        assert review["authority"]["grants_p_vs_np_authority"] is False
    assert proof["authority"]["grants_exact_quotient_value"] is False
    assert lower["authority"]["grants_canonical_lower_bound_theorem"] is False

    tool = json.loads(TOOL.read_text(encoding="utf-8"))
    assert tool["artifact_hash"] == _canonical_hash(tool)
    assert tool["authority"] == "HEURISTIC_PROPOSAL_PENDING_FRESH_REUSE_ASSURANCE"
    assert tool["validation_obligations"] == [
        "prove the full complement decomposition rather than infer it from samples",
        "check all local generator fibres and pair disjointness",
        "check all cross-component active edge orientations",
    ]
    assert all("framework promotion" not in item for item in tool["validation_obligations"])
    assert "t>=1" in tool["abstraction"]
    assert any("row projections" in item and "column projections" in item for item in tool["preconditions"])

    math_feedback = json.loads(MATH_FEEDBACK.read_text(encoding="utf-8"))
    leak_feedback = json.loads(LEAK_FEEDBACK.read_text(encoding="utf-8"))
    assert math_feedback["artifact_hash"] == _canonical_hash(math_feedback)
    assert math_feedback["mathematical_saturation_credit"] is True
    transfer = math_feedback["proposed_reusable_method_delta"]["transfer_condition"]
    assert "t>=1" in transfer and "row and column projections" in transfer
    assert math_feedback["strict_rakl_discovery_credit"] is False
    assert leak_feedback["artifact_hash"] == _canonical_hash(leak_feedback)
    assert leak_feedback["mathematical_saturation_credit"] is False
    assert leak_feedback["software_assurance_saturation_credit"] is False


def test_retrospective_trace_is_hash_chained_without_promotion() -> None:
    trace = json.loads(TRACE.read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "framework/RAKL/schemas/math-research-trace.schema.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(trace)
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        assert entry["artifact_hash"] == _canonical_hash(entry)
        previous = entry["artifact_hash"]
    assert [entry["event_type"] for entry in trace["entries"]] == [
        "RESULT_RECORDED", "FALSIFIER_RUN", "RESIDUAL_OPENED", "REVIEWED"
    ]
    outputs = trace["entries"][-1]["outputs"]
    assert "strict_rakl_discovery:false" in outputs
    assert "canonical_lower_theorem:NOT_PROMOTED" in outputs
    assert "review_independence:false" in outputs
    assert "root_authority:none" in outputs
    assert all(entry["event_type"] != "PROMOTED" for entry in trace["entries"])
