from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from rakl.math_context import ContextGateVerdict, CrossDomainAnalogy, MathContextFiber, MethodTransfer, audit_math_context_fiber
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview, ResearchMemoryVerdict, audit_research_memory_review
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_yme1a1a_packet_passes_current_pre_candidate_gates_without_candidate() -> None:
    context_raw = _load("01_frontier/YM_E1a1a_CONTEXT_FIBER_20260811.json")
    context_for_hash = copy.deepcopy(context_raw)
    context_for_hash["packet_hash"] = ""
    assert context_raw["packet_hash"] == _canonical_hash(context_for_hash)
    assert context_raw["first_candidate_at"] is None

    fiber = MathContextFiber(
        atom_id=context_raw["atom_id"],
        object_context=context_raw["object_context"],
        structural_coordinates=tuple(context_raw["structural_coordinates"]),
        equivalent_formulations=tuple(context_raw["equivalent_formulations"]),
        solved_analogues=tuple(context_raw.get("solved_analogues", ())),
        near_solved_analogues=tuple(context_raw.get("near_solved_analogues", ())),
        method_transfers=tuple(
            MethodTransfer(
                source_context=i["source_context"],
                method=i["method"],
                shared_structure=tuple(i["shared_structure"]),
                required_assumptions=tuple(i["required_assumptions"]),
                disanalogies=tuple(i["disanalogies"]),
                repair_question=i["repair_question"],
                source_anchors=tuple(i["source_anchors"]),
            )
            for i in context_raw["method_transfers"]
        ),
        explicit_disanalogies=tuple(context_raw["explicit_disanalogies"]),
        source_anchors=tuple(context_raw["source_anchors"]),
        analogy_scan_status=context_raw["analogy_scan_status"],
        cross_domain_analogies=tuple(
            CrossDomainAnalogy(
                source_kind=i["source_kind"],
                source_situation=i["source_situation"],
                common_abstraction=tuple(i["common_abstraction"]),
                source_to_target_mapping=tuple(i["source_to_target_mapping"]),
                shared_constraints=tuple(i["shared_constraints"]),
                disanalogies=tuple(i["disanalogies"]),
                proposed_principle=i["proposed_principle"],
                validation_obligation=i["validation_obligation"],
                provenance_note=i["provenance_note"],
            )
            for i in context_raw.get("cross_domain_analogies", ())
        ),
        analogy_scan_notes=context_raw.get("analogy_scan_notes", ""),
        frozen_at=context_raw["frozen_at"],
        first_candidate_at=context_raw.get("first_candidate_at"),
        packet_hash=context_raw["packet_hash"],
    )
    assert audit_math_context_fiber(fiber).verdict is ContextGateVerdict.PASS

    tools_raw = _load("07_memory/YM_E1a1a_RESEARCH_TOOL_INVENTORY_20260811.json")
    failures_raw = _load("07_memory/YM_E1a1a_FAILURE_EXPERIENCE_LATTICE_20260811.json")
    memory_raw = _load("07_memory/YM_E1a1a_RESEARCH_MEMORY_REVIEW_20260811.json")
    assert memory_raw["tool_inventory_snapshot_hash"] == _canonical_hash(tools_raw)
    assert memory_raw["failure_lattice_snapshot_hash"] == _canonical_hash(failures_raw)
    assert memory_raw["relevant_failure_ids"] == [
        "F-YM-E1A1-FINITE-LOOP-GEOMETRY-CLOSURE",
        "F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE",
    ]
    for failure in failures_raw["experiences"]:
        copied = copy.deepcopy(failure)
        artifact_hash = copied["artifact_hash"]
        copied["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(copied)

    memory_for_hash = copy.deepcopy(memory_raw)
    memory_for_hash["artifact_hash"] = ""
    assert memory_raw["artifact_hash"] == _canonical_hash(memory_for_hash)
    memory = ResearchMemoryReview(
        target_atom_id=memory_raw["target_atom_id"],
        target_context_hash=memory_raw["target_context_hash"],
        tool_inventory_snapshot_hash=memory_raw["tool_inventory_snapshot_hash"],
        failure_lattice_snapshot_hash=memory_raw["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(memory_raw["tool_query_status"]),
        failure_query_status=MemoryQueryStatus(memory_raw["failure_query_status"]),
        candidate_method_families=tuple(memory_raw["candidate_method_families"]),
        relevant_tool_ids=tuple(memory_raw.get("relevant_tool_ids", ())),
        relevant_failure_ids=tuple(memory_raw.get("relevant_failure_ids", ())),
        selected_tool_ids=tuple(memory_raw.get("selected_tool_ids", ())),
        tool_applicability_notes=tuple(memory_raw.get("tool_applicability_notes", ())),
        failure_reuse_notes=tuple(memory_raw.get("failure_reuse_notes", ())),
        unresolved_warnings=tuple(memory_raw.get("unresolved_warnings", ())),
        evidence_pointers=tuple(memory_raw.get("evidence_pointers", ())),
        artifact_hash=memory_raw["artifact_hash"],
    )
    assert audit_research_memory_review(
        memory, atom_id=fiber.atom_id, context_hash=fiber.packet_hash
    ).verdict is ResearchMemoryVerdict.PASS

    trace_raw = _load("09_trace/YM_E1a1a_PRE_CANDIDATE_TRACE_20260811.json")
    previous = ""
    entries = []
    for raw in trace_raw["entries"]:
        assert raw["previous_event_hash"] == previous
        payload = copy.deepcopy(raw)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        previous = artifact_hash
        entries.append(
            ResearchTraceEntry(
                event_id=raw["event_id"],
                atom_id=raw["atom_id"],
                event_type=ResearchTraceEventType(raw["event_type"]),
                timestamp=raw["timestamp"],
                state_summary=raw["state_summary"],
                action_summary=raw["action_summary"],
                evidence_pointers=tuple(raw["evidence_pointers"]),
                alternatives_considered=tuple(raw.get("alternatives_considered", ())),
                decision_rationale=raw.get("decision_rationale", ""),
                outputs=tuple(raw.get("outputs", ())),
                uncertainties=tuple(raw.get("uncertainties", ())),
                residuals=tuple(raw.get("residuals", ())),
                next_steps=tuple(raw.get("next_steps", ())),
                artifact_hash=raw["artifact_hash"],
                previous_event_hash=raw.get("previous_event_hash", ""),
            )
        )
    assert all(
        e.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED for e in entries
    )
    trace = MathResearchTrace(trace_id=trace_raw["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(
        trace, atom_id=fiber.atom_id, context_packet_hash=fiber.packet_hash
    ).verdict is TraceGateVerdict.PASS

    plan = plan_math_research(
        signature=ProblemSignature(
            objects=(
                "one actual weak-coupling Balaban-style 4D pure Yang-Mills RG block",
                "buffered gauge-invariant source mark",
                "graded localized marked polymer/loop state",
            ),
            relations=(
                "background-field RG blocking",
                "source differentiation",
                "operator and geometry mixing",
                "polymer localization",
                "reflection-buffer transport",
                "g_k/L-dependent norm control",
                "small/large-field compatibility",
            ),
            domain="constructive quantum field theory / lattice Yang-Mills renormalization group",
            goal_type="classify one-step graded marked closure or leakage before multiscale iteration",
        ),
        record=MathResearchRecord(claim_id=fiber.atom_id),
        context_fiber=fiber,
        memory_review=memory,
        research_trace=trace,
    )
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed
    assert plan.pre_candidate_actions == ()


def test_yme1a1a_preserves_parent_scope_and_does_not_claim_root_authority() -> None:
    source = (BASE / "03_sources/YM_E1a1a_BALABAN_WEAK_COUPLING_SOURCE_AUDIT_20260811.md").read_text(encoding="utf-8")
    review = (BASE / "08_reviews/YM_E1a1a_PRE_CANDIDATE_REVIEW_20260811.md").read_text(encoding="utf-8")
    context_text = (BASE / "01_frontier/YM_E1a1a_CONTEXT_FIBER_20260811.json").read_text(encoding="utf-8")
    assert "not a weak-coupling Balaban impossibility theorem" in context_text
    assert "NO_CANDIDATE" in source
    assert "ROOT_AUTHORITY_NONE" in source
    assert "NO_CANDIDATE" in review
    assert "ROOT_AUTHORITY_NONE" in review
