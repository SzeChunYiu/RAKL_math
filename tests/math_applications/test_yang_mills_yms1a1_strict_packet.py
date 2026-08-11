from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from rakl.math_context import (
    ContextGateVerdict,
    CrossDomainAnalogy,
    MathContextFiber,
    MethodTransfer,
    audit_math_context_fiber,
)
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import (
    MemoryQueryStatus,
    ResearchMemoryReview,
    ResearchMemoryVerdict,
    audit_research_memory_review,
)
from rakl.semantic_shortcut import REQUIRED_SHORTCUT_ACTIONS, ShortcutReviewVerdict
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_yms1a1_fresh_packet_passes_current_pre_candidate_gates() -> None:
    context_raw = _load("01_frontier/YM-S1A1_CONTEXT_FIBER_20260811.json")
    context_for_hash = copy.deepcopy(context_raw)
    context_for_hash["packet_hash"] = ""
    assert context_raw["packet_hash"] == _canonical_hash(context_for_hash)

    fiber = MathContextFiber(
        atom_id=context_raw["atom_id"],
        object_context=context_raw["object_context"],
        structural_coordinates=tuple(context_raw["structural_coordinates"]),
        equivalent_formulations=tuple(context_raw["equivalent_formulations"]),
        solved_analogues=tuple(context_raw.get("solved_analogues", ())),
        near_solved_analogues=tuple(context_raw.get("near_solved_analogues", ())),
        method_transfers=tuple(
            MethodTransfer(
                source_context=item["source_context"],
                method=item["method"],
                shared_structure=tuple(item["shared_structure"]),
                required_assumptions=tuple(item["required_assumptions"]),
                disanalogies=tuple(item["disanalogies"]),
                repair_question=item["repair_question"],
                source_anchors=tuple(item["source_anchors"]),
            )
            for item in context_raw["method_transfers"]
        ),
        explicit_disanalogies=tuple(context_raw["explicit_disanalogies"]),
        source_anchors=tuple(context_raw["source_anchors"]),
        analogy_scan_status=context_raw["analogy_scan_status"],
        cross_domain_analogies=tuple(
            CrossDomainAnalogy(
                source_kind=item["source_kind"],
                source_situation=item["source_situation"],
                common_abstraction=tuple(item["common_abstraction"]),
                source_to_target_mapping=tuple(item["source_to_target_mapping"]),
                shared_constraints=tuple(item["shared_constraints"]),
                disanalogies=tuple(item["disanalogies"]),
                proposed_principle=item["proposed_principle"],
                validation_obligation=item["validation_obligation"],
                provenance_note=item["provenance_note"],
            )
            for item in context_raw.get("cross_domain_analogies", ())
        ),
        analogy_scan_notes=context_raw.get("analogy_scan_notes", ""),
        frozen_at=context_raw["frozen_at"],
        first_candidate_at=context_raw.get("first_candidate_at"),
        packet_hash=context_raw["packet_hash"],
    )
    assert audit_math_context_fiber(fiber).verdict is ContextGateVerdict.PASS

    tools_raw = _load("07_memory/YM-S1A1_RESEARCH_TOOL_INVENTORY_20260811.json")
    failures_raw = _load("07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_20260811.json")
    memory_raw = _load("07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_20260811.json")

    assert memory_raw["tool_inventory_snapshot_hash"] == _canonical_hash(tools_raw)
    assert memory_raw["failure_lattice_snapshot_hash"] == _canonical_hash(failures_raw)
    assert [item["failure_id"] for item in failures_raw["experiences"]] == [
        "F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE"
    ]

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
    assert memory.failure_query_status is MemoryQueryStatus.MATCHES_FOUND
    assert (
        audit_research_memory_review(
            memory, atom_id=fiber.atom_id, context_hash=fiber.packet_hash
        ).verdict
        is ResearchMemoryVerdict.PASS
    )

    trace_raw = _load("09_trace/YM-S1A1_PRE_CANDIDATE_TRACE_20260811.json")
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
        entry.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED
        for entry in entries
    )
    trace_obj = MathResearchTrace(trace_id=trace_raw["trace_id"], entries=tuple(entries))
    assert (
        audit_pre_candidate_trace(
            trace_obj, atom_id=fiber.atom_id, context_packet_hash=fiber.packet_hash
        ).verdict
        is TraceGateVerdict.FAIL
    )

    plan = plan_math_research(
        signature=ProblemSignature(
            objects=(
                "positive self-adjoint Yang-Mills transfer matrix",
                "dense/cyclic gauge-invariant source states",
                "common Euclidean-time covariance exponent",
                "full excited transfer spectrum",
            ),
            relations=(
                "spectral measure / moment asymptotics",
                "OS Euclidean-time reconstruction",
                "source density",
                "strong-coupling correlation decay",
            ),
            domain="lattice gauge theory / operator theory",
            goal_type="close fixed-cutoff source-completeness-to-full-gap logical bridge",
        ),
        record=MathResearchRecord(claim_id=fiber.atom_id),
        context_fiber=fiber,
        memory_review=memory,
        research_trace=trace_obj,
    )
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.CANNOT_CHECK
    assert plan.trace_gate.verdict is TraceGateVerdict.CANNOT_CHECK
    assert plan.candidate_generation_allowed is False
    assert plan.pre_candidate_actions == REQUIRED_SHORTCUT_ACTIONS


def test_yms1a1_difference_witness_preserves_old_hidden_state_failure() -> None:
    memory_raw = _load("07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_20260811.json")
    notes = "\n".join(memory_raw["failure_reuse_notes"])
    assert "DifferenceWitness" in notes
    assert "old three-state falsifier" in notes
    assert "density hypothesis" in notes


def test_yms1a1_trace_binds_the_exact_live_memory_review() -> None:
    memory = _load("07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_20260811.json")
    trace = _load("09_trace/YM-S1A1_PRE_CANDIDATE_TRACE_20260811.json")
    legacy = _load(
        "09_trace/YM-S1A1_PRE_CANDIDATE_TRACE_MEMORY_HASH_INVALID_20260811.json"
    )

    memory_event = next(
        event for event in trace["entries"] if event["event_id"] == "YM-S1A1-E006"
    )
    next_step = next(
        event for event in trace["entries"] if event["event_id"] == "YM-S1A1-E007"
    )
    assert memory["artifact_hash"] in memory_event["evidence_pointers"]
    assert memory["artifact_hash"] in memory_event["outputs"]
    assert memory["artifact_hash"] in next_step["evidence_pointers"]
    assert trace["trace_id"] != legacy["trace_id"]
    assert any(
        "sha256:9e8e0176a607b4ac63d1231d4b936f9751a0b3e77d1b50bc353eafde98b53279"
        in event["evidence_pointers"] + event["outputs"]
        for event in legacy["entries"]
    )


def test_yms1a1_packet_has_role_separation_and_live_evidence_paths() -> None:
    review_path = BASE / "08_reviews/YM-S1A1_PRE_CANDIDATE_REVIEW_20260811.md"
    review = review_path.read_text(encoding="utf-8")
    assert "## 6. Formal-methods lead" in review
    assert "## 7. Novelty / prior-art lead" in review
    assert "## 8. Analogy / method-transfer lead" in review

    trace = _load("09_trace/YM-S1A1_PRE_CANDIDATE_TRACE_20260811.json")
    review_event = next(
        event for event in trace["entries"] if event["event_id"] == "YM-S1A1-E005"
    )
    review_hash = "sha256:" + hashlib.sha256(review_path.read_bytes()).hexdigest()
    assert "Eight role-separated" in review_event["state_summary"]
    assert review_hash in review_event["evidence_pointers"]
    assert review_hash in review_event["outputs"]
    next_step = next(
        event for event in trace["entries"] if event["event_id"] == "YM-S1A1-E007"
    )
    assert len(next_step["evidence_pointers"]) == len(
        set(next_step["evidence_pointers"])
    )

    failures = _load("07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_20260811.json")
    for experience in failures["experiences"]:
        for pointer in experience["evidence_pointers"]:
            if pointer.startswith("tests/"):
                assert (ROOT / pointer).is_file(), pointer
