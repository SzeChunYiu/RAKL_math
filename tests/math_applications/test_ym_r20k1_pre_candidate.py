from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from rakl.math_context import ContextGateVerdict
from rakl.pre_scratch_fibre_freeze import HookMaterializationStatus
from rakl.quantifier_compatibility import GluingConsumer, WitnessAuditVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import ResearchTraceEventType, TraceGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FIXTURE = YM / "09_trace/ym_r20k1_pre_candidate_fixture.py"


def module():
    spec = importlib.util.spec_from_file_location("ym_r20k1_pre", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_strict_runtime_gates_pass_but_candidate_waits_for_public_durability() -> None:
    m = module()
    plan, context, memory, _, shortcut, _, _, trace, _ = m.build_plan()
    assert m.APPLICATION_BASE_SHA == "b7ca6ac51fa8319b559e95402c47959c626f284a"
    assert m.FRAMEWORK_SHA == "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed is True
    assert context.first_candidate_at is None
    assert memory.selected_tool_ids == ()
    assert shortcut.selected_mode is ShortcutMode.JUMP
    assert [entry.event_type for entry in trace.entries] == [
        ResearchTraceEventType.ATOMIZED,
        ResearchTraceEventType.CONTEXT_FROZEN,
        ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
        ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    ]
    gate = m.build_documents()["gate"]
    assert gate["operational_candidate_materialization_allowed"] is False
    assert gate["pre_scratch_durability"]["status"] == "BUILT_NOT_PERSISTED_PENDING_PUBLIC_MAIN_MERGE"
    assert gate["future_material_result_contract"]["current_status"] == "NO_RESULT_NO_LESSON"
    assert gate["future_material_result_contract"]["mathematical_credit_only"] is True


def test_documents_are_regenerated_and_result_blind() -> None:
    m = module()
    documents = m.build_documents()
    assert set(documents) == set(m.PATHS)
    for name, path in m.PATHS.items():
        assert json.loads(path.read_text()) == documents[name], name
    text = json.dumps(documents, sort_keys=True)
    atom = documents["atomization"]
    assert atom["candidate_identity"] is None
    assert atom["candidate_proposed"] is False
    assert atom["result_accessed"] is False
    assert documents["selection"]["selected_atom"] == "YM-S1a2i-K1"
    assert documents["selection"]["mathematical_credit"] == 0
    for forbidden in (
        "observed_result",
        "explicit_threshold",
        "proof_certificate",
        "mass_gap_proved",
    ):
        assert forbidden not in text


def test_hook_receipt_and_trace_are_content_bound() -> None:
    m = module()
    docs = m.build_documents()
    hook, receipt, trace = docs["hook"], docs["pre_action"], docs["trace"]
    assert hook["materialization_status"] == HookMaterializationStatus.BUILT_NOT_PERSISTED.value
    assert hook["durable_receipt_pointer"] is None
    assert hook["reasons"] == ["receipt_built_without_durable_persistence_acknowledgement"]
    assert hook["receipt_canonical_sha256"] == receipt["receipt_canonical_sha256"]
    assert receipt["framework_commit"] == m.FRAMEWORK_SHA
    assert receipt["application_commit"] == m.APPLICATION_BASE_SHA
    assert receipt["atom_id"] == m.ATOM
    assert receipt["allowed_outcome_branches"] == [
        "SUCCESS", "PARTIAL_SUCCESS", "FAILURE", "BLOCKED", "UNKNOWN"
    ]
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        previous = entry["artifact_hash"]
    quantifier = m.build_quantifier(m.build_context())
    audit = m.audit_quantifier_compatibility(
        quantifier,
        expected_atom_id=m.ATOM,
        consumer=GluingConsumer.REVIEW,
        claimed_witness_hash=quantifier.witness_canonical_sha256,
    )
    assert audit.verdict is WitnessAuditVerdict.FAIL_CLOSED_UNKNOWN
    assert audit.grants_gluing_authority is False
    assert audit.grants_theorem_authority is False
    assert set(quantifier.unknown_fields) >= {
        "sequence_limit_scope",
        "norm_quantifier_scope",
        "required_scope_witness",
    }
