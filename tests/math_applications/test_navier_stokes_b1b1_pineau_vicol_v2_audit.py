from __future__ import annotations

import json
from pathlib import Path

from rakl.math_context import (
    ContextGateVerdict,
    CrossDomainAnalogy,
    MathContextFiber,
    MethodTransfer,
    audit_math_context_fiber,
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
NS = ROOT / "research/real_math/millennium/navier_stokes"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _context() -> MathContextFiber:
    c = _load(NS / "01_frontier/NS-B1b1_CONTEXT_FIBER_20260811.json")
    transfers = tuple(
        MethodTransfer(
            source_context=x["source_context"],
            method=x["method"],
            shared_structure=tuple(x["shared_structure"]),
            required_assumptions=tuple(x["required_assumptions"]),
            disanalogies=tuple(x["disanalogies"]),
            repair_question=x["repair_question"],
            source_anchors=tuple(x["source_anchors"]),
        )
        for x in c["method_transfers"]
    )
    analogies = tuple(
        CrossDomainAnalogy(
            source_kind=x["source_kind"],
            source_situation=x["source_situation"],
            common_abstraction=tuple(x["common_abstraction"]),
            source_to_target_mapping=tuple(x["source_to_target_mapping"]),
            shared_constraints=tuple(x["shared_constraints"]),
            disanalogies=tuple(x["disanalogies"]),
            proposed_principle=x["proposed_principle"],
            validation_obligation=x["validation_obligation"],
            provenance_note=x["provenance_note"],
        )
        for x in c["cross_domain_analogies"]
    )
    return MathContextFiber(
        atom_id=c["atom_id"],
        object_context=c["object_context"],
        structural_coordinates=tuple(c["structural_coordinates"]),
        equivalent_formulations=tuple(c["equivalent_formulations"]),
        solved_analogues=tuple(c["solved_analogues"]),
        near_solved_analogues=tuple(c["near_solved_analogues"]),
        method_transfers=transfers,
        explicit_disanalogies=tuple(c["explicit_disanalogies"]),
        source_anchors=tuple(c["source_anchors"]),
        analogy_scan_status=c["analogy_scan_status"],
        cross_domain_analogies=analogies,
        analogy_scan_notes=c["analogy_scan_notes"],
        frozen_at=c["frozen_at"],
        first_candidate_at=c["first_candidate_at"],
        packet_hash=c["packet_hash"],
    )


def _memory() -> ResearchMemoryReview:
    m = _load(NS / "07_memory/NS-B1b1_RESEARCH_MEMORY_REVIEW_20260811.json")
    return ResearchMemoryReview(
        target_atom_id=m["target_atom_id"],
        target_context_hash=m["target_context_hash"],
        tool_inventory_snapshot_hash=m["tool_inventory_snapshot_hash"],
        failure_lattice_snapshot_hash=m["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(m["tool_query_status"]),
        failure_query_status=MemoryQueryStatus(m["failure_query_status"]),
        candidate_method_families=tuple(m["candidate_method_families"]),
        relevant_tool_ids=tuple(m["relevant_tool_ids"]),
        relevant_failure_ids=tuple(m["relevant_failure_ids"]),
        selected_tool_ids=tuple(m["selected_tool_ids"]),
        tool_applicability_notes=tuple(m["tool_applicability_notes"]),
        failure_reuse_notes=tuple(m["failure_reuse_notes"]),
        unresolved_warnings=tuple(m["unresolved_warnings"]),
        evidence_pointers=tuple(m["evidence_pointers"]),
        artifact_hash=m["artifact_hash"],
    )


def _trace() -> MathResearchTrace:
    t = _load(NS / "09_trace/NS-B1b1_TRACE_20260811.json")
    entries = tuple(
        ResearchTraceEntry(
            event_id=x["event_id"],
            atom_id=x["atom_id"],
            event_type=ResearchTraceEventType(x["event_type"]),
            timestamp=x["timestamp"],
            state_summary=x["state_summary"],
            action_summary=x["action_summary"],
            evidence_pointers=tuple(x["evidence_pointers"]),
            alternatives_considered=tuple(x["alternatives_considered"]),
            decision_rationale=x["decision_rationale"],
            outputs=tuple(x["outputs"]),
            uncertainties=tuple(x["uncertainties"]),
            residuals=tuple(x["residuals"]),
            next_steps=tuple(x["next_steps"]),
            artifact_hash=x["artifact_hash"],
            previous_event_hash=x["previous_event_hash"],
        )
        for x in t["entries"]
    )
    return MathResearchTrace(trace_id=t["trace_id"], entries=entries)


def test_ns_b1b1_pre_candidate_gates_are_closed_before_source_discriminator():
    context = _context()
    assert audit_math_context_fiber(context).verdict is ContextGateVerdict.PASS

    memory = _memory()
    assert audit_research_memory_review(
        memory, atom_id=context.atom_id, context_hash=context.packet_hash
    ).verdict is ResearchMemoryVerdict.PASS

    trace = _trace()
    assert audit_pre_candidate_trace(
        trace, atom_id=context.atom_id, context_packet_hash=context.packet_hash
    ).verdict is TraceGateVerdict.PASS
    assert ResearchTraceEventType.CANDIDATE_PROPOSED not in {
        entry.event_type for entry in trace.entries
    }


def test_pineau_vicol_v2_source_boundary_and_residual_are_explicit():
    audit = (
        NS
        / "01_frontier/NS-B1b1_PINEAU_VICOL_V2_SCENARIO_TRANSFER_AUDIT_20260811.md"
    ).read_text(encoding="utf-8")
    for marker in (
        "arXiv:2607.09619v2",
        "Theorem 1.4",
        "Theorem 1.7",
        "Theorem 1.9",
        "Remark 1.11",
        "TRANSFER_BLOCKED_SCOPED",
        "ROOT_AUTHORITY_NONE",
        "Stage A",
        "Stage B",
        "strong `L^3_loc`",
        "weak `L^(3/2)_loc`",
    ):
        assert marker in audit

    assert "none of Theorems 1.4, 1.7, or 1.9 can presently be applied" in audit
    assert "NS-B1b1a" in audit


def test_direct_transfer_failure_is_scoped_and_does_not_blacklist_repairs():
    f = _load(NS / "07_memory/NS-B1b1_FAILURE_EXPERIENCE_DELTA_20260811.json")
    experience = f["experience"]
    scope = " ".join(experience["scope_conditions"])
    diagnoses = " ".join(experience["competing_diagnoses"])

    assert "direct, unmodified application" in scope
    assert "finite A,C,D,E" in diagnoses
    assert "near-stationary slice" in diagnoses
    assert experience["diagnosis_status"] == "SUPPORTED"
    assert experience["candidate_id"] is None
