from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re

import jsonschema

from rakl.failure_lattice import reconstruct_failure_lattice
from rakl.math_context import ContextGateVerdict, MathContextFiber, MethodTransfer, audit_math_context_fiber
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview, ResearchMemoryVerdict, audit_research_memory_review
from rakl.research_tool_inventory import ResearchTool, ResearchToolAuthority, validate_research_tool
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
SCHEMAS = ROOT / "framework/RAKL/schemas"
ATOM = "O9d12a2a1a1b1"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def canonical_hash(value: object, field: str | None = None) -> str:
    payload = copy.deepcopy(value)
    if field is not None:
        assert isinstance(payload, dict)
        payload[field] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def parsed(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def test_v2_gate_is_prospective_schema_valid_runtime_reconstructed_and_candidate_free() -> None:
    correction = load(ROOT / "receipts/pnp-o9d12a2a1a1b1-v0-hostile-failure-20260811.json")
    assert correction["artifact_hash"] == canonical_hash(correction, "artifact_hash")
    for binding in correction["failed_packet_bindings"]:
        assert hashlib.sha256((ROOT / binding["path"]).read_bytes()).hexdigest() == binding["raw_sha256"]
    assert correction["failed_status"] == "REJECTED_PRE_CANDIDATE_AUTHORIZATION"
    assert correction["authority_contract"]["candidate_generation_allowed"] is False

    v0_context = load(BASE / "01_frontier/O9d12a2a1a1b1_MATH_CONTEXT_FIBER_20260811.json")
    v0_trace = load(BASE / "09_trace/O9d12a2a1a1b1_PRE_CANDIDATE_TRACE_20260811.json")
    v0_review = load(BASE / "08_reviews/SAME_CONTEXT_EXPERT_REVIEW_O9d12a2a1a1b1_PRE_CANDIDATE_20260811.json")
    v0_memory = load(BASE / "07_memory/O9d12a2a1a1b1_RESEARCH_MEMORY_REVIEW_20260811.json")
    assert parsed(v0_context["frozen_at"]) < parsed(v0_trace["entries"][0]["timestamp"])
    assert v0_review["memory_review_hash"] == v0_memory["artifact_hash"]
    assert v0_trace["entries"][4]["event_type"] == "EXPERT_CONTEXT_REVIEW"
    assert v0_trace["entries"][5]["event_type"] == "EXPERIENCE_MEMORY_REVIEW"

    atomization = load(BASE / "02_problem_dag/O9d12a2a1a1b1_ATOMIZATION_V2_20260811.json")
    assert atomization["artifact_hash"] == canonical_hash(atomization, "artifact_hash")
    assert atomization["candidate_identity"] is None

    context_raw = load(BASE / "01_frontier/O9d12a2a1a1b1_MATH_CONTEXT_FIBER_V2_20260811.json")
    jsonschema.Draft202012Validator(
        load(SCHEMAS / "math-context-fiber.schema.json"),
        format_checker=jsonschema.FormatChecker(),
    ).validate(context_raw)
    assert context_raw["packet_hash"] == canonical_hash(context_raw, "packet_hash")
    assert parsed(atomization["atomized_at"]) < parsed(context_raw["frozen_at"])
    assert context_raw["first_candidate_at"] is None
    assert context_raw["analogy_scan_status"] == "NO_SAFE_BRIDGE_FOUND"
    assert context_raw["cross_domain_analogies"] == []
    retrospective = context_raw["method_transfers"][2]
    assert retrospective["method"].startswith("Retrospective source method only:")
    assert "Choose a source-defined family" not in retrospective["method"]

    fiber = MathContextFiber(
        atom_id=context_raw["atom_id"], object_context=context_raw["object_context"],
        structural_coordinates=tuple(context_raw["structural_coordinates"]),
        equivalent_formulations=tuple(context_raw["equivalent_formulations"]),
        solved_analogues=tuple(context_raw["solved_analogues"]),
        near_solved_analogues=tuple(context_raw["near_solved_analogues"]),
        method_transfers=tuple(MethodTransfer(
            source_context=item["source_context"], method=item["method"],
            shared_structure=tuple(item["shared_structure"]), required_assumptions=tuple(item["required_assumptions"]),
            disanalogies=tuple(item["disanalogies"]), repair_question=item["repair_question"], source_anchors=tuple(item["source_anchors"]),
        ) for item in context_raw["method_transfers"]),
        explicit_disanalogies=tuple(context_raw["explicit_disanalogies"]), source_anchors=tuple(context_raw["source_anchors"]),
        analogy_scan_status=context_raw["analogy_scan_status"], cross_domain_analogies=(), analogy_scan_notes=context_raw["analogy_scan_notes"],
        frozen_at=context_raw["frozen_at"], first_candidate_at=None, packet_hash=context_raw["packet_hash"],
    )
    assert audit_math_context_fiber(fiber).verdict is ContextGateVerdict.PASS

    tools_raw = load(BASE / "07_memory/O9d12a2a1a1b1_TOOL_SNAPSHOT_V2_20260811.json")
    failures_raw = load(BASE / "07_memory/O9d12a2a1a1b1_FAILURE_SNAPSHOT_V2_20260811.json")
    jsonschema.Draft202012Validator(load(SCHEMAS / "research-tool-inventory.schema.json")).validate(tools_raw)
    jsonschema.Draft202012Validator(
        load(SCHEMAS / "failure-experience-lattice.schema.json"),
        format_checker=jsonschema.FormatChecker(),
    ).validate(failures_raw)
    assert len(reconstruct_failure_lattice(failures_raw).experiences) == 6
    for item in tools_raw["tools"]:
        tool = ResearchTool(
            tool_id=item["tool_id"], name=item["name"], kind=item["kind"], abstraction=item["abstraction"],
            source_atom_id=item["source_atom_id"], source_candidate_id=item["source_candidate_id"], source_result_ids=tuple(item["source_result_ids"]),
            source_context_hash=item["source_context_hash"], authority=ResearchToolAuthority(item["authority"]), preconditions=tuple(item["preconditions"]),
            structural_signature=tuple(item["structural_signature"]), operation=item["operation"], guaranteed_effects=tuple(item["guaranteed_effects"]),
            non_guarantees=tuple(item["non_guarantees"]), validation_obligations=tuple(item["validation_obligations"]), evidence_pointers=tuple(item["evidence_pointers"]),
            known_failure_ids=tuple(item.get("known_failure_ids", ())), successful_reuse_ids=tuple(item.get("successful_reuse_ids", ())),
            proof_backing=tuple(item.get("proof_backing", ())), artifact_hash=item["artifact_hash"],
        )
        assert validate_research_tool(tool) == ()
    warning = load(BASE / "07_memory/O9d12a2a1a1b1_NONCANONICAL_PARENT_WARNING_V2_20260811.json")
    assert warning["artifact_hash"] == canonical_hash(warning, "artifact_hash")
    assert hashlib.sha256((ROOT / warning["source_path"]).read_bytes()).hexdigest() == warning["source_raw_sha256"]
    assert warning["authority"]["canonical_failure_memory"] is False

    review = load(BASE / "08_reviews/SAME_CONTEXT_EXPERT_REVIEW_O9d12a2a1a1b1_PRE_CANDIDATE_V2_20260811.json")
    assert review["artifact_hash"] == canonical_hash(review, "artifact_hash")
    assert "memory_review_hash" not in review
    assert review["child_memory_state_at_review"] == "NOT_YET_FROZEN"
    assert parsed(context_raw["frozen_at"]) < parsed(review["reviewed_at"])

    memory_raw = load(BASE / "07_memory/O9d12a2a1a1b1_RESEARCH_MEMORY_REVIEW_V2_20260811.json")
    freeze = load(BASE / "07_memory/O9d12a2a1a1b1_MEMORY_FREEZE_V2_20260811.json")
    jsonschema.Draft202012Validator(load(SCHEMAS / "research-memory-review.schema.json")).validate(memory_raw)
    assert memory_raw["artifact_hash"] == canonical_hash(memory_raw, "artifact_hash")
    assert freeze["artifact_hash"] == canonical_hash(freeze, "artifact_hash")
    assert parsed(review["reviewed_at"]) < parsed(freeze["frozen_at"])
    assert memory_raw["tool_inventory_snapshot_hash"] == canonical_hash(tools_raw)
    assert memory_raw["failure_lattice_snapshot_hash"] == canonical_hash(failures_raw)
    assert warning["legacy_failure_id"] not in memory_raw["relevant_failure_ids"]
    memory = ResearchMemoryReview(
        target_atom_id=memory_raw["target_atom_id"], target_context_hash=memory_raw["target_context_hash"],
        tool_inventory_snapshot_hash=memory_raw["tool_inventory_snapshot_hash"], failure_lattice_snapshot_hash=memory_raw["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(memory_raw["tool_query_status"]), failure_query_status=MemoryQueryStatus(memory_raw["failure_query_status"]),
        candidate_method_families=tuple(memory_raw["candidate_method_families"]), relevant_tool_ids=tuple(memory_raw["relevant_tool_ids"]),
        relevant_failure_ids=tuple(memory_raw["relevant_failure_ids"]), selected_tool_ids=tuple(memory_raw["selected_tool_ids"]),
        tool_applicability_notes=tuple(memory_raw["tool_applicability_notes"]), failure_reuse_notes=tuple(memory_raw["failure_reuse_notes"]),
        unresolved_warnings=tuple(memory_raw["unresolved_warnings"]), evidence_pointers=tuple(memory_raw["evidence_pointers"]), artifact_hash=memory_raw["artifact_hash"],
    )
    assert audit_research_memory_review(memory, atom_id=ATOM, context_hash=fiber.packet_hash).verdict is ResearchMemoryVerdict.PASS

    trace_raw = load(BASE / "09_trace/O9d12a2a1a1b1_PRE_CANDIDATE_TRACE_V2_20260811.json")
    jsonschema.Draft202012Validator(
        load(SCHEMAS / "math-research-trace.schema.json"), format_checker=jsonschema.FormatChecker()
    ).validate(trace_raw)
    previous = ""
    entries = []
    for raw in trace_raw["entries"]:
        assert raw["previous_event_hash"] == previous
        assert raw["artifact_hash"] == canonical_hash(raw, "artifact_hash")
        previous = raw["artifact_hash"]
        entries.append(ResearchTraceEntry(
            event_id=raw["event_id"], atom_id=raw["atom_id"], event_type=ResearchTraceEventType(raw["event_type"]), timestamp=raw["timestamp"],
            state_summary=raw["state_summary"], action_summary=raw["action_summary"], evidence_pointers=tuple(raw["evidence_pointers"]),
            alternatives_considered=tuple(raw["alternatives_considered"]), decision_rationale=raw["decision_rationale"], outputs=tuple(raw["outputs"]),
            uncertainties=tuple(raw["uncertainties"]), residuals=tuple(raw["residuals"]), next_steps=tuple(raw["next_steps"]),
            artifact_hash=raw["artifact_hash"], previous_event_hash=raw["previous_event_hash"],
        ))
    assert [e.event_type.value for e in entries] == ["ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW", "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW", "NEXT_STEP_PROPOSED"]
    assert entries[0].timestamp == atomization["atomized_at"]
    assert entries[1].timestamp == context_raw["frozen_at"]
    assert entries[4].timestamp == review["reviewed_at"]
    assert entries[5].timestamp == freeze["frozen_at"]
    assert all(parsed(entries[i].timestamp) <= parsed(entries[i + 1].timestamp) for i in range(6))
    assert all(e.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED for e in entries)
    trace = MathResearchTrace(trace_id=trace_raw["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(trace, atom_id=ATOM, context_packet_hash=fiber.packet_hash).verdict is TraceGateVerdict.PASS

    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("non-trivial A in Gamma", "generator family B", "semi-filters over U=A^c", "shared integral t-pair family Lambda", "cover graph", "cyclic intersection system"),
            relations=("above-w incidence", "pair preservation", "integral coverage", "Theorem-24 recurrence", "Theorem-30 equivalence", "cheap-target and multiplexing controls"),
            domain="complexity theory / set-theoretic fusion / P versus NP",
            goal_type="freeze a source-native shared-t-rule theorem inventory action before any mathematical candidate",
        ),
        record=MathResearchRecord(claim_id=ATOM), context_fiber=fiber, memory_review=memory, research_trace=trace,
    )
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert entries[-1].outputs == ("next_action:SOURCE_NATIVE_T_RULE_THEOREM_INVENTORY", "candidate_identity:none", "root_authority:none")

    synthesis = (
        BASE / "01_frontier/O9d12a2a1a1b1_SOURCE_AND_TRANSFER_PACKET_V2_20260811.md"
    ).read_text(encoding="utf-8")
    match = re.search(r"V2 synthesized after trace:\*\* `([^`]+)`", synthesis)
    assert match is not None
    assert parsed(entries[-1].timestamp) < parsed(match.group(1))


def test_v2_receipt_is_exact_hardened_and_rejects_hash_and_duplicate_mutations() -> None:
    receipt_path = ROOT / "receipts/pnp-o9d12a2a1a1b1-pre-candidate-gate-v2-20260811.json"
    schema_path = ROOT / "schemas/pnp-o9d12a2a1a1b1-pre-candidate-gate-v2.schema.json"
    receipt = load(receipt_path)
    schema = load(schema_path)
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    validator.validate(receipt)
    assert receipt["artifact_hash"] == canonical_hash(receipt, "artifact_hash")
    assert receipt["freshness_check"] == {
        "checked_at": "2026-08-11T15:48:08Z",
        "branch_moved": False,
        "local_base_sha": "5a8c6bb2f297a536e1b0d1c8b0aa8e66cd1e3720",
        "origin_main_sha": "5a8c6bb2f297a536e1b0d1c8b0aa8e66cd1e3720",
        "left_count": 0,
        "right_count": 0,
    }
    assert len({item["path"] for item in receipt["artifacts"]}) == 11
    assert len({item["kind"] for item in receipt["artifacts"]}) == 11
    for item in receipt["artifacts"]:
        assert hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() == item[
            "sha256"
        ]

    hash_paths: list[tuple[object, ...]] = [
        ("source_binding", "application_base_sha"),
        ("source_binding", "framework_pin"),
        ("source_binding", "primary_source_pdf_sha256"),
        ("freshness_check", "local_base_sha"),
        ("freshness_check", "origin_main_sha"),
        ("supersession", "v0_correction_hash"),
        ("runtime_gate", "context_packet_hash"),
        ("runtime_gate", "memory_review_hash"),
        ("runtime_gate", "expert_review_hash"),
        ("runtime_gate", "trace_terminal_hash"),
        ("artifact_hash",),
    ] + [("artifacts", index, "sha256") for index in range(11)]

    def get_at(document: dict, path: tuple[object, ...]) -> object:
        value: object = document
        for key in path:
            value = value[key]  # type: ignore[index]
        return value

    def set_at(document: dict, path: tuple[object, ...], value: object) -> None:
        target: object = document
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]

    for path in hash_paths:
        original = get_at(receipt, path)
        assert isinstance(original, str)
        for mutation in (123, "", original[:-1], original + "0", original + "\n", original + "\r\n", original.upper()):
            hostile = copy.deepcopy(receipt)
            set_at(hostile, path, mutation)
            assert list(validator.iter_errors(hostile)), (path, mutation)

    duplicate_artifact = copy.deepcopy(receipt)
    duplicate_artifact["artifacts"][1] = copy.deepcopy(duplicate_artifact["artifacts"][0])
    assert list(validator.iter_errors(duplicate_artifact))
    missing_artifact = copy.deepcopy(receipt)
    missing_artifact["artifacts"].pop()
    assert list(validator.iter_errors(missing_artifact))
    duplicate_run = copy.deepcopy(receipt)
    duplicate_run["test_runs"][1] = copy.deepcopy(duplicate_run["test_runs"][0])
    assert list(validator.iter_errors(duplicate_run))
    missing_run = copy.deepcopy(receipt)
    missing_run["test_runs"].pop()
    assert list(validator.iter_errors(missing_run))
