from __future__ import annotations

import copy
import hashlib
import json
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FRAMEWORK_SCHEMAS = ROOT / "framework/RAKL/schemas"
CONTEXT = YM / "01_frontier/YM-S1A1_C001C1_FUTURE_CORRECTION_CONTEXT_FIBER_20260811.json"
MEMORY = YM / "07_memory/YM-S1A1_C001C1_RUNTIME_CONFORMANT_V2_RESEARCH_MEMORY_REVIEW_20260811.json"
LATTICE = YM / "07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_QZERO_RUNTIME_CONFORMANT_V2_20260811.json"
OLD_TRACE = YM / "09_trace/YM-S1A1_C001C1_RUNTIME_CONFORMANT_V2_PRE_CANDIDATE_TRACE_20260811.json"
OLD_RECEIPT = YM / "08_reviews/YM-S1A1_QZERO_FAILURE_LATTICE_RUNTIME_SUPERSESSION_RECEIPT_20260811.json"
TRACE = YM / "09_trace/YM-S1A1_C001C1_MEMORY_BINDING_CONFORMANT_V3_PRE_CANDIDATE_TRACE_20260811.json"
RECEIPT = YM / "08_reviews/YM-S1A1_QZERO_TRACE_MEMORY_BINDING_SUPERSESSION_RECEIPT_20260811.json"
RECEIPT_SCHEMA = ROOT / "schemas/trace-memory-binding-supersession-receipt.schema.json"

OLD_TRACE_SHA = "sha256:fa26819e97cf202b5a74df4b9a1b47fcd40066a5b99d3e4e186d7ccbde482d03"
OLD_RECEIPT_SHA = "sha256:48cf825004ab08baff84982525496b4815c246e19a1d6462e114170f8d044ade"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _self_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    observed = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert observed == _canonical_hash(payload)
    return observed


def _validate(value: dict, schema_path: Path) -> None:
    schema = _load(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(value)


def _entry(raw: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
        event_id=raw["event_id"], atom_id=raw["atom_id"],
        event_type=ResearchTraceEventType(raw["event_type"]), timestamp=raw["timestamp"],
        state_summary=raw["state_summary"], action_summary=raw["action_summary"],
        evidence_pointers=tuple(raw["evidence_pointers"]),
        alternatives_considered=tuple(raw["alternatives_considered"]),
        decision_rationale=raw["decision_rationale"], outputs=tuple(raw["outputs"]),
        uncertainties=tuple(raw["uncertainties"]), residuals=tuple(raw["residuals"]),
        next_steps=tuple(raw["next_steps"]), artifact_hash=raw["artifact_hash"],
        previous_event_hash=raw["previous_event_hash"],
    )


def test_f081_trace_and_receipt_bytes_are_preserved_and_stale_binding_is_explicit() -> None:
    assert _file_hash(OLD_TRACE) == OLD_TRACE_SHA
    assert _file_hash(OLD_RECEIPT) == OLD_RECEIPT_SHA
    memory = _load(MEMORY)
    predecessor_e006 = _load(OLD_TRACE)["entries"][5]
    assert memory["artifact_hash"] in predecessor_e006["evidence_pointers"]
    assert memory["artifact_hash"] not in predecessor_e006["outputs"]
    assert "sha256:dccaacdd5c2c37fa4dfd6869ce9811c8e4f1a18676128ccc1fbd4ace1b34f1fe" in predecessor_e006["outputs"]


def test_v3_trace_binds_exact_memory_and_failure_snapshot_in_evidence_and_outputs() -> None:
    context = _load(CONTEXT)
    memory = _load(MEMORY)
    trace_raw = _load(TRACE)
    _validate(trace_raw, FRAMEWORK_SCHEMAS / "math-research-trace.schema.json")

    previous = ""
    entries = []
    for raw in trace_raw["entries"]:
        assert raw["previous_event_hash"] == previous
        previous = _self_hash(raw)
        entries.append(_entry(raw))

    assert [entry.event_type for entry in entries] == [
        ResearchTraceEventType.ATOMIZED,
        ResearchTraceEventType.CONTEXT_FROZEN,
        ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    ]
    e006 = entries[5]
    exact_bindings = {memory["artifact_hash"], memory["failure_lattice_snapshot_hash"]}
    assert exact_bindings <= set(e006.evidence_pointers)
    assert exact_bindings <= set(e006.outputs)
    assert "sha256:dccaacdd5c2c37fa4dfd6869ce9811c8e4f1a18676128ccc1fbd4ace1b34f1fe" not in e006.outputs
    assert all(entry.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED for entry in entries)
    assert "NO_CANDIDATE_EMITTED" in entries[-1].outputs

    trace = MathResearchTrace(trace_id=trace_raw["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(
        trace, atom_id=context["atom_id"], context_packet_hash=context["packet_hash"]
    ).verdict is TraceGateVerdict.FAIL


def test_later_receipt_supersedes_only_future_trace_use_and_binds_exact_files() -> None:
    receipt = _load(RECEIPT)
    trace = _load(TRACE)
    memory = _load(MEMORY)
    _validate(receipt, RECEIPT_SCHEMA)
    _self_hash(receipt)

    assert receipt["finding_classification"] == "QUARANTINED_APPLICATION_FEEDBACK_HYPOTHESIS"
    assert receipt["predecessor_trace"]["file_sha256"] == OLD_TRACE_SHA
    assert receipt["predecessor_trace"]["semantic_binding_result"] == "FAIL"
    assert receipt["successor_trace"]["file_sha256"] == _file_hash(TRACE)
    assert receipt["successor_trace"]["final_event_hash"] == trace["entries"][-1]["artifact_hash"]
    assert receipt["exact_memory_bindings"]["memory_artifact_hash"] == memory["artifact_hash"]
    assert receipt["exact_memory_bindings"]["failure_lattice_snapshot_hash"] == memory["failure_lattice_snapshot_hash"]
    assert receipt["authority"]["mathematical_truth_effect"] == "NONE"
    assert receipt["authority"]["independent_review"] is False

    receipt_time = datetime.fromisoformat(receipt["recorded_at"])
    final_trace_time = datetime.fromisoformat(trace["entries"][-1]["timestamp"])
    assert receipt_time > final_trace_time
    forbidden = str(RECEIPT.relative_to(ROOT))
    assert all(forbidden not in entry["evidence_pointers"] for entry in trace["entries"])
