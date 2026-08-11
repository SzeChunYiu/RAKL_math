from __future__ import annotations

import json
from pathlib import Path

from rakl.math_context import (
    CrossDomainAnalogy,
    MathContextFiber,
    MethodTransfer,
    audit_math_context_fiber,
    ContextGateVerdict,
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
    return json.loads(path.read_text())

def test_ns_b1a1_strict_pre_candidate_gates():
    c = _load(NS / "01_frontier/NS-B1a1_CONTEXT_FIBER_20260811.json")
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
    fiber = MathContextFiber(
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
    assert audit_math_context_fiber(fiber).verdict is ContextGateVerdict.PASS

    m = _load(NS / "07_memory/NS-B1a1_RESEARCH_MEMORY_REVIEW_20260811.json")
    review = ResearchMemoryReview(
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
    assert audit_research_memory_review(
        review, atom_id=fiber.atom_id, context_hash=fiber.packet_hash
    ).verdict is ResearchMemoryVerdict.PASS

    t = _load(NS / "09_trace/NS-B1a1_TRACE_20260811.json")
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
    trace = MathResearchTrace(trace_id=t["trace_id"], entries=entries)
    assert audit_pre_candidate_trace(
        trace, atom_id=fiber.atom_id, context_packet_hash=fiber.packet_hash
    ).verdict is TraceGateVerdict.PASS
    assert ResearchTraceEventType.CANDIDATE_PROPOSED not in {x.event_type for x in entries}

def test_local_energy_absolute_scale_currency_is_critical_not_decaying():
    # Dimension exponents for T/R after using A,C,D definitions:
    # T2: R^-1 * R^-2 * (R^2 time) * (R A) = R^0 A
    quadratic_power = -1 - 2 + 2 + 1
    # T3: R^-1(normalize) * R^-1(cutoff grad) * R^2 C
    cubic_power = -1 - 1 + 2
    # Tp: R^-1(normalize) * R^-1(grad) *
    #     (R^2 D)^(2/3) * (R^2 C)^(1/3)
    pressure_power = -1 - 1 + (2 * 2 / 3) + (2 * 1 / 3)
    assert quadratic_power == 0
    assert cubic_power == 0
    assert pressure_power == 0

def test_failure_scope_does_not_blacklist_signed_or_rigidity_routes():
    f = _load(NS / "07_memory/NS-B1a1_FAILURE_EXPERIENCE_DELTA_20260811.json")
    scope = " ".join(f["experience"]["scope_conditions"])
    diagnoses = " ".join(f["experience"]["competing_diagnoses"])
    assert "absolute termwise estimates only" in scope
    assert "signed local-energy increment" in diagnoses
    assert "minimal-element almost-periodicity" in diagnoses
