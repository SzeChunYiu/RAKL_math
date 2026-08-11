from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from rakl.math_context import ContextGateVerdict, CrossDomainAnalogy, MathContextFiber, MethodTransfer, audit_math_context_fiber
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview, ResearchMemoryVerdict, audit_research_memory_review
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_h4d1b_context_memory_and_trace_pass_current_framework_gates() -> None:
    raw = _load("01_frontier/H4d1b_CONTEXT_FIBER_20260811.json")
    for_hash = copy.deepcopy(raw)
    for_hash["packet_hash"] = ""
    assert raw["packet_hash"] == _canonical_hash(for_hash)
    fiber = MathContextFiber(
        atom_id=raw["atom_id"], object_context=raw["object_context"],
        structural_coordinates=tuple(raw["structural_coordinates"]), equivalent_formulations=tuple(raw["equivalent_formulations"]),
        solved_analogues=tuple(raw.get("solved_analogues", ())), near_solved_analogues=tuple(raw.get("near_solved_analogues", ())),
        method_transfers=tuple(MethodTransfer(source_context=x["source_context"], method=x["method"], shared_structure=tuple(x["shared_structure"]), required_assumptions=tuple(x["required_assumptions"]), disanalogies=tuple(x["disanalogies"]), repair_question=x["repair_question"], source_anchors=tuple(x["source_anchors"])) for x in raw["method_transfers"]),
        explicit_disanalogies=tuple(raw["explicit_disanalogies"]), source_anchors=tuple(raw["source_anchors"]), analogy_scan_status=raw["analogy_scan_status"],
        cross_domain_analogies=tuple(CrossDomainAnalogy(source_kind=x["source_kind"], source_situation=x["source_situation"], common_abstraction=tuple(x["common_abstraction"]), source_to_target_mapping=tuple(x["source_to_target_mapping"]), shared_constraints=tuple(x["shared_constraints"]), disanalogies=tuple(x["disanalogies"]), proposed_principle=x["proposed_principle"], validation_obligation=x["validation_obligation"], provenance_note=x["provenance_note"]) for x in raw.get("cross_domain_analogies", ())),
        analogy_scan_notes=raw.get("analogy_scan_notes", ""), frozen_at=raw["frozen_at"], first_candidate_at=raw.get("first_candidate_at"), packet_hash=raw["packet_hash"],
    )
    assert audit_math_context_fiber(fiber).verdict is ContextGateVerdict.PASS

    tools = _load("07_memory/H4d1b_RESEARCH_TOOL_INVENTORY_20260811.json")
    failures = _load("07_memory/H4d1b_FAILURE_MEMORY_SNAPSHOT_20260811.json")
    memory_raw = _load("07_memory/H4d1b_RESEARCH_MEMORY_REVIEW_20260811.json")
    assert memory_raw["tool_inventory_snapshot_hash"] == _canonical_hash(tools)
    assert memory_raw["failure_lattice_snapshot_hash"] == _canonical_hash(failures)
    memory_for_hash = copy.deepcopy(memory_raw)
    memory_for_hash["artifact_hash"] = ""
    assert memory_raw["artifact_hash"] == _canonical_hash(memory_for_hash)
    memory = ResearchMemoryReview(
        target_atom_id=memory_raw["target_atom_id"], target_context_hash=memory_raw["target_context_hash"],
        tool_inventory_snapshot_hash=memory_raw["tool_inventory_snapshot_hash"], failure_lattice_snapshot_hash=memory_raw["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(memory_raw["tool_query_status"]), failure_query_status=MemoryQueryStatus(memory_raw["failure_query_status"]),
        candidate_method_families=tuple(memory_raw["candidate_method_families"]), relevant_tool_ids=tuple(memory_raw.get("relevant_tool_ids", ())),
        relevant_failure_ids=tuple(memory_raw.get("relevant_failure_ids", ())), selected_tool_ids=tuple(memory_raw.get("selected_tool_ids", ())),
        tool_applicability_notes=tuple(memory_raw.get("tool_applicability_notes", ())), failure_reuse_notes=tuple(memory_raw.get("failure_reuse_notes", ())),
        unresolved_warnings=tuple(memory_raw.get("unresolved_warnings", ())), evidence_pointers=tuple(memory_raw["evidence_pointers"]), artifact_hash=memory_raw["artifact_hash"],
    )
    assert audit_research_memory_review(memory, atom_id=fiber.atom_id, context_hash=fiber.packet_hash).verdict is ResearchMemoryVerdict.PASS

    trace_raw = _load("09_trace/H4d1b_PRE_CANDIDATE_TRACE_20260811.json")
    entries = []
    previous = ""
    for x in trace_raw["entries"]:
        assert x["previous_event_hash"] == previous
        payload = copy.deepcopy(x)
        observed = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert observed == _canonical_hash(payload)
        previous = observed
        entries.append(ResearchTraceEntry(event_id=x["event_id"], atom_id=x["atom_id"], event_type=ResearchTraceEventType(x["event_type"]), timestamp=x["timestamp"], state_summary=x["state_summary"], action_summary=x["action_summary"], evidence_pointers=tuple(x["evidence_pointers"]), alternatives_considered=tuple(x.get("alternatives_considered", ())), decision_rationale=x.get("decision_rationale", ""), outputs=tuple(x.get("outputs", ())), uncertainties=tuple(x.get("uncertainties", ())), residuals=tuple(x.get("residuals", ())), next_steps=tuple(x.get("next_steps", ())), artifact_hash=x["artifact_hash"], previous_event_hash=x.get("previous_event_hash", "")))
    trace = MathResearchTrace(trace_id=trace_raw["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(trace, atom_id=fiber.atom_id, context_packet_hash=fiber.packet_hash).verdict is TraceGateVerdict.PASS


def test_h4d1b_packet_keeps_first_order_and_formal_authority_separate() -> None:
    raw = _load("01_frontier/H4d1b_CONTEXT_FIBER_20260811.json")
    joined = " ".join(raw["structural_coordinates"] + raw["explicit_disanalogies"])
    assert "first-order" in joined
    assert "formal" in joined
    assert "all-order" in joined
    assert "initial algebraicity" in joined
