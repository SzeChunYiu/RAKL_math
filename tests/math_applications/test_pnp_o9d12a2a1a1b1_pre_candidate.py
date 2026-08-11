from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import jsonschema

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
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
FRAMEWORK_SCHEMAS = ROOT / "framework/RAKL/schemas"
ATOM = "O9d12a2a1a1b1"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _self_hash(raw: dict, field: str) -> str:
    payload = copy.deepcopy(raw)
    expected = payload[field]
    payload[field] = ""
    assert expected == _canonical_hash(payload)
    return expected


def test_o9d12a2a1a1b1_strict_pre_candidate_packet_passes_current_gates() -> None:
    context_raw = _load(f"01_frontier/{ATOM}_MATH_CONTEXT_FIBER_20260811.json")
    jsonschema.validate(
        context_raw,
        json.loads((FRAMEWORK_SCHEMAS / "math-context-fiber.schema.json").read_text()),
    )
    context_hash = _self_hash(context_raw, "packet_hash")
    assert context_raw["atom_id"] == ATOM
    assert context_raw["first_candidate_at"] is None
    assert context_raw["analogy_scan_status"] == "NO_SAFE_BRIDGE_FOUND"
    assert context_raw["cross_domain_analogies"] == []
    assert "coding" in context_raw["analogy_scan_notes"]
    assert len(context_raw["method_transfers"]) == 3
    assert all(item["repair_question"] for item in context_raw["method_transfers"])

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
        analogy_scan_notes=context_raw["analogy_scan_notes"],
        frozen_at=context_raw["frozen_at"],
        first_candidate_at=context_raw["first_candidate_at"],
        packet_hash=context_raw["packet_hash"],
    )
    assert audit_math_context_fiber(fiber).verdict is ContextGateVerdict.PASS

    tools_raw = _load(f"07_memory/{ATOM}_TOOL_SNAPSHOT_20260811.json")
    failures_raw = _load(f"07_memory/{ATOM}_FAILURE_SNAPSHOT_20260811.json")
    memory_raw = _load(f"07_memory/{ATOM}_RESEARCH_MEMORY_REVIEW_20260811.json")
    jsonschema.validate(
        memory_raw,
        json.loads((FRAMEWORK_SCHEMAS / "research-memory-review.schema.json").read_text()),
    )
    assert {item["tool_id"] for item in tools_raw["tools"]} == {
        "T-PNP-UPPER-FIRST",
        "T-PNP-EXTREMAL-CALIBRATION",
        "T-PNP-FRACTIONAL-SEMIFILTER-PACKING",
        "T-PNP-GNEQ-JOINT-SIGNATURE-CALIBRATION",
    }
    assert {item["failure_id"] for item in failures_raw["experiences"]} == {
        "F-C010-MULTIPLEXING",
        "F-C021-CHEAP-ADJACENCY",
        "F-C023-SCALAR-COLLAPSE",
        "F-C024-FRACTIONAL-INTEGRALITY-GAP",
        "F-C025-FIRST-ORDER-CANONICAL-COLLAPSE",
        "F-O9D12A2A1A1-PARTITION-CLOSURE-COLLAPSE",
        "F-O9D12A2A1A1B-FIXED-LAMBDA-GLOBAL-STATE-FACTORIZATION",
    }
    assert memory_raw["tool_inventory_snapshot_hash"] == _canonical_hash(tools_raw)
    assert memory_raw["failure_lattice_snapshot_hash"] == _canonical_hash(failures_raw)
    memory_hash = _self_hash(memory_raw, "artifact_hash")
    assert "T-PNP-FRACTIONAL-SEMIFILTER-PACKING" not in memory_raw["selected_tool_ids"]
    assert any("no DifferenceWitness" in note for note in memory_raw["failure_reuse_notes"])

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
        memory, atom_id=ATOM, context_hash=context_hash
    ).verdict is ResearchMemoryVerdict.PASS

    review_raw = _load(
        f"08_reviews/SAME_CONTEXT_EXPERT_REVIEW_{ATOM}_PRE_CANDIDATE_20260811.json"
    )
    _self_hash(review_raw, "artifact_hash")
    assert review_raw["review_type"] == "ROLE_SEPARATED_SAME_CONTEXT_INTERNAL_REVIEW"
    assert review_raw["independent_peer_review"] is False
    assert review_raw["candidate_reviewed"] is None
    assert {role["role"] for role in review_raw["roles"]} == {
        "domain_theory_lead",
        "analogy_method_transfer_lead",
        "adversarial_falsification_lead",
        "formal_methods_lead",
        "novelty_research_value_lead",
    }

    trace_raw = _load(f"09_trace/{ATOM}_PRE_CANDIDATE_TRACE_20260811.json")
    jsonschema.validate(
        trace_raw,
        json.loads((FRAMEWORK_SCHEMAS / "math-research-trace.schema.json").read_text()),
    )
    previous = ""
    entries: list[ResearchTraceEntry] = []
    for raw in trace_raw["entries"]:
        assert raw["previous_event_hash"] == previous
        payload = copy.deepcopy(raw)
        expected = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert expected == _canonical_hash(payload)
        previous = expected
        entries.append(
            ResearchTraceEntry(
                event_id=raw["event_id"],
                atom_id=raw["atom_id"],
                event_type=ResearchTraceEventType(raw["event_type"]),
                timestamp=raw["timestamp"],
                state_summary=raw["state_summary"],
                action_summary=raw["action_summary"],
                evidence_pointers=tuple(raw["evidence_pointers"]),
                alternatives_considered=tuple(raw["alternatives_considered"]),
                decision_rationale=raw["decision_rationale"],
                outputs=tuple(raw["outputs"]),
                uncertainties=tuple(raw["uncertainties"]),
                residuals=tuple(raw["residuals"]),
                next_steps=tuple(raw["next_steps"]),
                artifact_hash=raw["artifact_hash"],
                previous_event_hash=raw["previous_event_hash"],
            )
        )
    assert [entry.event_type.value for entry in entries] == [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert all(entry.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED for entry in entries)
    trace = MathResearchTrace(trace_id=trace_raw["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(
        trace, atom_id=ATOM, context_packet_hash=context_hash
    ).verdict is TraceGateVerdict.PASS

    plan = plan_math_research(
        signature=ProblemSignature(
            objects=(
                "non-trivial set A in Gamma",
                "generator family B",
                "semi-filters over U=A^c",
                "shared integral t-pair family Lambda",
                "cover graph",
                "cyclic intersection system",
            ),
            relations=(
                "above-w generator incidence",
                "pair preservation",
                "integral coverage of all above-A semi-filters",
                "Theorem-24 inclusion recurrence",
                "Theorem-30 exact cyclic characterization",
                "cheap-target and multiplexing controls",
            ),
            domain="complexity theory / set-theoretic fusion / P versus NP",
            goal_type="freeze the source-native shared-t-rule accounting interface before any lower-bound quantity or target evaluation",
        ),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=fiber,
        memory_review=memory,
        research_trace=trace,
    )
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert trace.entries[-1].outputs == (
        "next_action:SOURCE_NATIVE_T_RULE_THEOREM_INVENTORY",
        "candidate_identity:none",
        "root_authority:none",
    )
    assert memory.target_context_hash == context_hash
    assert memory.artifact_hash == memory_hash

    receipt_path = ROOT / "receipts/pnp-o9d12a2a1a1b1-pre-candidate-gate-20260811.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    jsonschema.validate(
        receipt,
        json.loads(
            (
                ROOT
                / "schemas/pnp-o9d12a2a1a1b1-pre-candidate-gate.schema.json"
            ).read_text(encoding="utf-8")
        ),
        format_checker=jsonschema.FormatChecker(),
    )
    _self_hash(receipt, "artifact_hash")
    assert receipt["source_binding"]["framework_pin"] == (
        "9027cc6beab7e935d714bbdf8e902b89b50caaa8"
    )
    assert receipt["runtime_gate"]["plan_math_research"] == {
        "candidate_generation_allowed": True,
        "pre_candidate_actions": [],
        "candidate_paths_used": False,
        "candidate_identity": None,
    }
    assert receipt["authority_contract"] == {
        "candidate_proposed": False,
        "mathematical_result": False,
        "proof_authority": False,
        "novelty_authority": False,
        "independent_peer_review": False,
        "p_vs_np_authority": False,
        "framework_promotion_authority": False,
    }
    for artifact in receipt["artifacts"]:
        assert hashlib.sha256((ROOT / artifact["path"]).read_bytes()).hexdigest() == artifact[
            "sha256"
        ]
