"""Assurance-only checks for the pre-output C043 candidate freeze."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
STATEMENT = PNP / "04_candidates/C043_FIRST_ROW_SPLIT_FREEZE_20260812.md"
EVALUATOR = PNP / "05_falsification/c043_first_row_split_gate.py"
PRE_TRACE = PNP / "09_trace/O9d12a2a1b_C043_PRE_CANDIDATE_TRACE_20260812.json"
FREEZE = PNP / "09_trace/O9d12a2a1b_C043_CANDIDATE_FREEZE_20260812.json"
CANDIDATE_TRACE = PNP / "09_trace/O9d12a2a1b_C043_CANDIDATE_TRACE_20260812.json"
LATEST_GATE = PNP / "09_trace/O9d12a2a1b_C043_LATEST_RAKL_GATE_RECEIPT_20260812.json"


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _load_evaluator_without_running_gate():
    spec = importlib.util.spec_from_file_location("c043_candidate_freeze", EVALUATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_latest_framework_pre_candidate_gate_passed_before_candidate() -> None:
    gate = json.loads(LATEST_GATE.read_text(encoding="utf-8"))
    assert gate["framework_commit"] == "439a176b109f5f3fe14386c96617207f9a2447ee"
    assert gate["gate_verdicts"] == {
        "context": "PASS",
        "dual_memory": "PASS",
        "obstruction_transformation": "PASS",
        "trace": "PASS",
        "selected_mode": "SEARCH",
        "candidate_route_ready": True,
        "candidate_generation_allowed": True,
    }
    assert gate["chronology"]["candidate_identity"] is None
    assert gate["chronology"]["candidate_proposed"] is False
    assert gate["chronology"]["native_output_accessed"] is False
    assert gate["artifact_hash"] == _canonical_hash(gate)


def test_freeze_binds_exact_statement_evaluator_and_unknown_output() -> None:
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    pre = json.loads(PRE_TRACE.read_text(encoding="utf-8"))
    assert freeze["pre_candidate_commit"] == "d71926073aa3be6da3f6351efe46dafdcd9b02a7"
    assert freeze["statement"]["sha256"] == hashlib.sha256(STATEMENT.read_bytes()).hexdigest()
    assert freeze["evaluator"]["sha256"] == hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    assert freeze["evaluator"]["runs_full_cover_LP"] is False
    assert freeze["chronology"]["pre_candidate_trace_last_hash"] == pre["entries"][-1]["artifact_hash"]
    assert freeze["chronology"]["native_output_accessed"] is False
    assert freeze["artifact_hash"] == _canonical_hash(freeze)


def test_candidate_trace_appends_one_proposal_after_all_eight_gate_events() -> None:
    pre = json.loads(PRE_TRACE.read_text(encoding="utf-8"))
    trace = json.loads(CANDIDATE_TRACE.read_text(encoding="utf-8"))
    assert trace["entries"][:8] == pre["entries"]
    assert [entry["event_type"] for entry in trace["entries"]] == [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW",
        "NEXT_STEP_PROPOSED",
        "CANDIDATE_PROPOSED",
    ]
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        assert entry["artifact_hash"] == _canonical_hash(entry)
        previous = entry["artifact_hash"]
    assert "native_output_accessed:false" in trace["entries"][-1]["outputs"]
    assert "root_authority:none" in trace["entries"][-1]["outputs"]


def test_only_non_native_length_helpers_are_loaded_before_commit() -> None:
    evaluator = _load_evaluator_without_running_gate()
    assert evaluator.parameter_pairs_for_length(26) == (
        (4, 1), (5, 1), (6, 1), (7, 1)
    )
    assert evaluator.parameter_pairs_for_length(28) == ()
    assert evaluator.parameter_pairs_for_length(30) == ((1, 3),)
