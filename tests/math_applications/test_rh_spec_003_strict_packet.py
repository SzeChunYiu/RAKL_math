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
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _git_blob_hash(path: Path) -> str:
    payload = path.read_bytes()
    framed = b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload
    return "gitblob-sha1:" + hashlib.sha1(framed).hexdigest()


def _fiber(raw: dict) -> MathContextFiber:
    return MathContextFiber(
        atom_id=raw["atom_id"], object_context=raw["object_context"],
        structural_coordinates=tuple(raw["structural_coordinates"]),
        equivalent_formulations=tuple(raw["equivalent_formulations"]),
        solved_analogues=tuple(raw.get("solved_analogues", ())), near_solved_analogues=tuple(raw.get("near_solved_analogues", ())),
        method_transfers=tuple(MethodTransfer(source_context=i["source_context"], method=i["method"], shared_structure=tuple(i["shared_structure"]), required_assumptions=tuple(i["required_assumptions"]), disanalogies=tuple(i["disanalogies"]), repair_question=i["repair_question"], source_anchors=tuple(i["source_anchors"])) for i in raw["method_transfers"]),
        explicit_disanalogies=tuple(raw["explicit_disanalogies"]), source_anchors=tuple(raw["source_anchors"]), analogy_scan_status=raw["analogy_scan_status"],
        cross_domain_analogies=tuple(CrossDomainAnalogy(source_kind=i["source_kind"], source_situation=i["source_situation"], common_abstraction=tuple(i["common_abstraction"]), source_to_target_mapping=tuple(i["source_to_target_mapping"]), shared_constraints=tuple(i["shared_constraints"]), disanalogies=tuple(i["disanalogies"]), proposed_principle=i["proposed_principle"], validation_obligation=i["validation_obligation"], provenance_note=i["provenance_note"]) for i in raw.get("cross_domain_analogies", ())),
        analogy_scan_notes=raw.get("analogy_scan_notes", ""), frozen_at=raw["frozen_at"], first_candidate_at=raw.get("first_candidate_at"), packet_hash=raw["packet_hash"],
    )


def _memory(raw: dict) -> ResearchMemoryReview:
    return ResearchMemoryReview(
        target_atom_id=raw["target_atom_id"], target_context_hash=raw["target_context_hash"],
        tool_inventory_snapshot_hash=raw["tool_inventory_snapshot_hash"], failure_lattice_snapshot_hash=raw["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(raw["tool_query_status"]), failure_query_status=MemoryQueryStatus(raw["failure_query_status"]),
        candidate_method_families=tuple(raw["candidate_method_families"]), relevant_tool_ids=tuple(raw.get("relevant_tool_ids", ())),
        relevant_failure_ids=tuple(raw.get("relevant_failure_ids", ())), selected_tool_ids=tuple(raw.get("selected_tool_ids", ())),
        tool_applicability_notes=tuple(raw.get("tool_applicability_notes", ())), failure_reuse_notes=tuple(raw.get("failure_reuse_notes", ())),
        unresolved_warnings=tuple(raw.get("unresolved_warnings", ())), evidence_pointers=tuple(raw.get("evidence_pointers", ())), artifact_hash=raw["artifact_hash"],
    )


def _trace(raw: dict) -> MathResearchTrace:
    previous = ""
    entries = []
    for item in raw["entries"]:
        payload = copy.deepcopy(item)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        assert item["previous_event_hash"] == previous
        previous = artifact_hash
        entries.append(ResearchTraceEntry(event_id=item["event_id"], atom_id=item["atom_id"], event_type=ResearchTraceEventType(item["event_type"]), timestamp=item["timestamp"], state_summary=item["state_summary"], action_summary=item["action_summary"], evidence_pointers=tuple(item["evidence_pointers"]), alternatives_considered=tuple(item.get("alternatives_considered", ())), decision_rationale=item.get("decision_rationale", ""), outputs=tuple(item.get("outputs", ())), uncertainties=tuple(item.get("uncertainties", ())), residuals=tuple(item.get("residuals", ())), next_steps=tuple(item.get("next_steps", ())), artifact_hash=item["artifact_hash"], previous_event_hash=item.get("previous_event_hash", "")))
    return MathResearchTrace(trace_id=raw["trace_id"], entries=tuple(entries))


def test_rh_spec_003_strict_pre_candidate_packet_passes() -> None:
    context_raw = _load("01_frontier/RH_SPEC_003_CONTEXT_FIBER_20260811.json")
    context_for_hash = copy.deepcopy(context_raw); context_for_hash["packet_hash"] = ""
    assert context_raw["packet_hash"] == _canonical_hash(context_for_hash)
    assert context_raw["first_candidate_at"] is None
    fiber = _fiber(context_raw)
    assert audit_math_context_fiber(fiber).verdict is ContextGateVerdict.PASS

    memory_raw = _load("07_memory/RH_SPEC_003_RESEARCH_MEMORY_REVIEW_20260811.json")
    assert memory_raw["tool_inventory_snapshot_hash"] == _git_blob_hash(BASE / "07_memory/RH_SPEC_002_POSTCAL_RESEARCH_TOOL_INVENTORY_20260811.json")
    assert memory_raw["failure_lattice_snapshot_hash"] == _git_blob_hash(BASE / "07_memory/RH_SPEC_002_POSTCAL_FAILURE_EXPERIENCE_LATTICE_20260811.json")
    memory_for_hash = copy.deepcopy(memory_raw); memory_for_hash["artifact_hash"] = ""
    assert memory_raw["artifact_hash"] == _canonical_hash(memory_for_hash)
    assert memory_raw["selected_tool_ids"] == []
    memory = _memory(memory_raw)
    assert audit_research_memory_review(memory, atom_id=fiber.atom_id, context_hash=fiber.packet_hash).verdict is ResearchMemoryVerdict.PASS

    trace = _trace(_load("09_trace/RH_SPEC_003_OPEN_TRACE_20260811.json"))
    assert audit_pre_candidate_trace(trace, atom_id=fiber.atom_id, context_packet_hash=fiber.packet_hash).verdict is TraceGateVerdict.PASS
    assert all(e.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED for e in trace.entries)

    precontext = (BASE / "01_frontier/RH_SPEC_003_TRACE_CLASS_THRESHOLD_PRECONTEXT_20260811.md").read_text(encoding="utf-8")
    review = (BASE / "08_reviews/SAME_CONTEXT_REVIEW_RH_SPEC_003_PRE_CANDIDATE_20260811.md").read_text(encoding="utf-8")
    for required in ("Exact RH binding and success contract", "A0 — spectral bridge assumptions", "A5 — exemptions and non-circularity", "Domain", "Self-adjointness", "Positivity", "Trace legitimacy", "Prime matching", "Multiplicity", "Completeness", "Non-circularity", "Limits/interchanges", "Representation"):
        assert required in precontext
    for role in ("Operator theorist", "Analytic number theorist", "Trace-formula / dynamical specialist", "de Branges / canonical-systems specialist", "de Bruijn–Newman / random-matrix specialist", "Adversarial verifier"):
        assert role in review

    plan = plan_math_research(
        signature=ProblemSignature(objects=("hypothetical exact compact-resolvent self-adjoint HP operator H", "Riemann zero counting multiset with multiplicity", "(I+H^2)^(-alpha/2)", "ordinary versus regularized/distributional trace"), relations=("spectral completeness and multiplicity matching", "von Mangoldt counting transfer", "Stieltjes/dyadic summability", "Schatten S_p membership", "trace-legitimacy exclusion"), domain="analytic number theory / self-adjoint operator theory / Schatten ideals / trace formulas", goal_type="freeze an exact necessary trace-class threshold filter before any Hilbert-Pólya candidate theorem"),
        record=MathResearchRecord(claim_id=fiber.atom_id), context_fiber=fiber, memory_review=memory, research_trace=trace,
    )
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed
    assert plan.pre_candidate_actions == ()
