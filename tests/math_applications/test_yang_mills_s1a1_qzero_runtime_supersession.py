from __future__ import annotations

import copy
import hashlib
import json
from datetime import datetime
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker

from rakl.failure_lattice import (
    FailureDiagnosisStatus,
    FailureExperience,
    FailureExperienceLattice,
    FailureLink,
    FailureRelation,
    add_failure_experience,
    add_failure_link,
)
from rakl.research_memory import (
    MemoryQueryStatus,
    ResearchMemoryReview,
    ResearchMemoryVerdict,
    audit_research_memory_review,
)
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
INVALID_LATTICE = YM / "07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_QZERO_SUCCESSOR_20260811.json"
INVALID_MEMORY = YM / "07_memory/YM-S1A1_C001C1_FUTURE_CORRECTION_RESEARCH_MEMORY_REVIEW_20260811.json"
INVALID_TRACE = YM / "09_trace/YM-S1A1_C001C1_FUTURE_CORRECTION_PRE_CANDIDATE_TRACE_20260811.json"

LATTICE = YM / "07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_QZERO_RUNTIME_CONFORMANT_V2_20260811.json"
MEMORY = YM / "07_memory/YM-S1A1_C001C1_RUNTIME_CONFORMANT_V2_RESEARCH_MEMORY_REVIEW_20260811.json"
TRACE = YM / "09_trace/YM-S1A1_C001C1_RUNTIME_CONFORMANT_V2_PRE_CANDIDATE_TRACE_20260811.json"
RECEIPT = YM / "08_reviews/YM-S1A1_QZERO_FAILURE_LATTICE_RUNTIME_SUPERSESSION_RECEIPT_20260811.json"
RECEIPT_SCHEMA = ROOT / "schemas/failure-lattice-runtime-supersession-receipt.schema.json"

INVALID_BYTES = {
    INVALID_LATTICE: "sha256:59a1060dfb3ce759d2f4fdc9e0b511f9a1cfb36ebf2ac2951cc3e5193a645af4",
    INVALID_MEMORY: "sha256:2ad0a35442024e28987fcc91ae17c6777ded8884261094288fe5581111004138",
    INVALID_TRACE: "sha256:2e4c5a63c1d904296790b598d645e5b02bd3edd61a2f3b30edcc6d2bbdc10517",
}


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _assert_self_hash(value: dict, field: str = "artifact_hash") -> str:
    payload = copy.deepcopy(value)
    observed = payload[field]
    payload[field] = ""
    assert observed == _canonical_hash(payload)
    return observed


def _validate(value: dict, schema_path: Path) -> None:
    schema = _load(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(value)


def _experience(raw: dict) -> FailureExperience:
    return FailureExperience(
        failure_id=raw["failure_id"],
        atom_id=raw["atom_id"],
        candidate_id=raw["candidate_id"],
        context_packet_hash=raw["context_packet_hash"],
        research_trace_event_id=raw["research_trace_event_id"],
        method_family=raw["method_family"],
        failure_mode=raw["failure_mode"],
        residual_signature=tuple(raw["residual_signature"]),
        broken_assumptions=tuple(raw.get("broken_assumptions", [])),
        scope_conditions=tuple(raw["scope_conditions"]),
        competing_diagnoses=tuple(raw["competing_diagnoses"]),
        selected_diagnosis=raw["selected_diagnosis"],
        diagnosis_status=FailureDiagnosisStatus(raw["diagnosis_status"]),
        evidence_pointers=tuple(raw["evidence_pointers"]),
        falsifier_or_attempt=raw["falsifier_or_attempt"],
        observed_result=raw["observed_result"],
        local_repair_attempts=tuple(raw.get("local_repair_attempts", [])),
        timestamp=raw["timestamp"],
        artifact_hash=raw["artifact_hash"],
    )


def _link(raw: dict) -> FailureLink:
    return FailureLink(
        source_id=raw["source_id"],
        target_id=raw["target_id"],
        relation=FailureRelation(raw["relation"]),
        rationale=raw["rationale"],
        evidence_pointers=tuple(raw.get("evidence_pointers", [])),
    )


def test_pushed_invalid_derivatives_are_immutable_and_old_runtime_link_is_rejected() -> None:
    for path, expected in INVALID_BYTES.items():
        assert _file_hash(path) == expected

    predecessor = _load(INVALID_LATTICE)
    _validate(predecessor, FRAMEWORK_SCHEMAS / "failure-experience-lattice.schema.json")
    lattice = FailureExperienceLattice()
    for raw in predecessor["experiences"]:
        lattice = add_failure_experience(lattice, _experience(raw))

    with pytest.raises(
        ValueError, match="failure links require existing source and target experiences"
    ):
        add_failure_link(lattice, _link(predecessor["links"][0]))


def test_runtime_conformant_lattice_rebuilds_only_through_public_runtime_apis() -> None:
    raw = _load(LATTICE)
    predecessor = _load(INVALID_LATTICE)
    _validate(raw, FRAMEWORK_SCHEMAS / "failure-experience-lattice.schema.json")
    assert raw["experiences"] == predecessor["experiences"]

    lattice = FailureExperienceLattice()
    for item in raw["experiences"]:
        _assert_self_hash(item)
        lattice = add_failure_experience(lattice, _experience(item))
    for item in raw["links"]:
        lattice = add_failure_link(lattice, _link(item))

    assert tuple(item.failure_id for item in lattice.experiences) == tuple(
        item["failure_id"] for item in raw["experiences"]
    )
    assert raw["links"] == []
    assert lattice.links == ()


def test_supersession_receipt_is_self_hashed_and_quarantines_application_feedback() -> None:
    receipt = _load(RECEIPT)
    _validate(receipt, RECEIPT_SCHEMA)
    _assert_self_hash(receipt)

    assert receipt["finding_classification"] == "QUARANTINED_APPLICATION_FEEDBACK_HYPOTHESIS"
    assert receipt["runtime_reproduction"]["predecessor_result"] == "REJECTED"
    assert receipt["runtime_reproduction"]["successor_result"] == "ACCEPTED"
    assert receipt["authority"]["framework_promotion"] == "NONE"
    assert receipt["authority"]["independent_review"] is False
    assert receipt["candidate_resolution"]["recorded_only_in_correction_receipt"] is True
    assert receipt["candidate_resolution"]["failure_to_candidate_link_present"] is False

    predecessor = receipt["predecessor"]
    assert predecessor["file_sha256"] == INVALID_BYTES[INVALID_LATTICE]
    assert predecessor["schema_result"] == "PASS"
    assert predecessor["runtime_result"] == "FAIL"
    successor = receipt["successor"]
    assert successor["file_sha256"] == _file_hash(LATTICE)
    assert successor["failure_lattice_snapshot_hash"] == _canonical_hash(_load(LATTICE))
    for binding in receipt["superseded_derivatives"]:
        assert binding["successor_file_sha256"] == _file_hash(ROOT / binding["successor_path"])


def test_corrected_memory_and_future_only_trace_pass_exact_gates_without_candidate() -> None:
    context = _load(CONTEXT)
    memory_raw = _load(MEMORY)
    lattice_raw = _load(LATTICE)
    trace_raw = _load(TRACE)
    _validate(memory_raw, FRAMEWORK_SCHEMAS / "research-memory-review.schema.json")
    _validate(trace_raw, FRAMEWORK_SCHEMAS / "math-research-trace.schema.json")
    _assert_self_hash(memory_raw)
    assert memory_raw["failure_lattice_snapshot_hash"] == _canonical_hash(lattice_raw)

    memory = ResearchMemoryReview(
        target_atom_id=memory_raw["target_atom_id"],
        target_context_hash=memory_raw["target_context_hash"],
        tool_inventory_snapshot_hash=memory_raw["tool_inventory_snapshot_hash"],
        failure_lattice_snapshot_hash=memory_raw["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(memory_raw["tool_query_status"]),
        failure_query_status=MemoryQueryStatus(memory_raw["failure_query_status"]),
        candidate_method_families=tuple(memory_raw["candidate_method_families"]),
        relevant_tool_ids=tuple(memory_raw["relevant_tool_ids"]),
        relevant_failure_ids=tuple(memory_raw["relevant_failure_ids"]),
        selected_tool_ids=tuple(memory_raw["selected_tool_ids"]),
        tool_applicability_notes=tuple(memory_raw["tool_applicability_notes"]),
        failure_reuse_notes=tuple(memory_raw["failure_reuse_notes"]),
        unresolved_warnings=tuple(memory_raw["unresolved_warnings"]),
        evidence_pointers=tuple(memory_raw["evidence_pointers"]),
        artifact_hash=memory_raw["artifact_hash"],
    )
    assert audit_research_memory_review(
        memory, atom_id=context["atom_id"], context_hash=context["packet_hash"]
    ).verdict is ResearchMemoryVerdict.PASS

    previous = ""
    entries: list[ResearchTraceEntry] = []
    for raw in trace_raw["entries"]:
        assert raw["previous_event_hash"] == previous
        previous = _assert_self_hash(raw)
        entries.append(
            ResearchTraceEntry(
                event_id=raw["event_id"], atom_id=raw["atom_id"],
                event_type=ResearchTraceEventType(raw["event_type"]),
                timestamp=raw["timestamp"], state_summary=raw["state_summary"],
                action_summary=raw["action_summary"],
                evidence_pointers=tuple(raw["evidence_pointers"]),
                alternatives_considered=tuple(raw["alternatives_considered"]),
                decision_rationale=raw["decision_rationale"], outputs=tuple(raw["outputs"]),
                uncertainties=tuple(raw["uncertainties"]), residuals=tuple(raw["residuals"]),
                next_steps=tuple(raw["next_steps"]), artifact_hash=raw["artifact_hash"],
                previous_event_hash=raw["previous_event_hash"],
            )
        )

    expected = [
        ResearchTraceEventType.ATOMIZED,
        ResearchTraceEventType.CONTEXT_FROZEN,
        ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    ]
    assert [entry.event_type for entry in entries] == expected
    assert all(entry.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED for entry in entries)
    expert_outputs = entries[4].outputs
    for role in (
        "DOMAIN_THEORY_LEAD:",
        "ANALOGY_METHOD_TRANSFER_LEAD:",
        "ADVERSARIAL_FALSIFICATION_LEAD:",
        "FORMAL_METHODS_LEAD:",
        "NOVELTY_RESEARCH_VALUE_LEAD:",
        "STRONGEST_OBJECTION:",
    ):
        assert any(output.startswith(role) for output in expert_outputs)
    assert "NO_CANDIDATE_EMITTED" in entries[-1].outputs

    receipt = _load(RECEIPT)
    receipt_time = datetime.fromisoformat(receipt["recorded_at"])
    final_trace_time = datetime.fromisoformat(entries[-1].timestamp)
    memory_freeze_event = entries[5]
    memory_freeze_time = datetime.fromisoformat(memory_freeze_event.timestamp)
    assert receipt_time > final_trace_time > memory_freeze_time
    assert str(MEMORY.relative_to(ROOT)) in memory_freeze_event.evidence_pointers
    assert memory_raw["artifact_hash"] in memory_freeze_event.evidence_pointers
    forbidden = str(RECEIPT.relative_to(ROOT))
    assert forbidden not in memory_raw["evidence_pointers"]
    assert all(forbidden not in entry.evidence_pointers for entry in entries)

    trace = MathResearchTrace(trace_id=trace_raw["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(
        trace, atom_id=context["atom_id"], context_packet_hash=context["packet_hash"]
    ).verdict is TraceGateVerdict.FAIL
