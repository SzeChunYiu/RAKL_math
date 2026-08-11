from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

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
YM = ROOT / "research/real_math/millennium/yang_mills"
FRAMEWORK_SCHEMAS = ROOT / "framework/RAKL/schemas"
CONTEXT = YM / "01_frontier/YM-S1A1_C001C1_FUTURE_CORRECTION_CONTEXT_FIBER_20260811.json"
OLD_LATTICE = YM / "07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_20260811.json"
LATTICE = YM / "07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_QZERO_SUCCESSOR_20260811.json"
MEMORY = YM / "07_memory/YM-S1A1_C001C1_FUTURE_CORRECTION_RESEARCH_MEMORY_REVIEW_20260811.json"
RECEIPT = YM / "08_reviews/YM-S1A1_C001_V2_STRICT_CHRONOLOGY_INVALIDATION_RECEIPT_20260811.json"
TRACE = YM / "09_trace/YM-S1A1_C001C1_FUTURE_CORRECTION_PRE_CANDIDATE_TRACE_20260811.json"
OLD_CORRECTION_TRACE = YM / "09_trace/YM-S1A1_C001_V2_CORRECTION_TRACE_20260811.json"
V1 = YM / "04_candidates/YM-S1A1_C001_DENSE_SOURCE_COMMON_RATE_SPECTRAL_EXCLUSION_20260811.md"
V2 = YM / "04_candidates/YM-S1A1_C001_V2_DENSE_SOURCE_COMMON_RATE_SPECTRAL_EXCLUSION_20260811.md"
TOOL_INVENTORY = YM / "07_memory/YM-S1A1_RESEARCH_TOOL_INVENTORY_20260811.json"

V1_SHA = "sha256:a8b6081ac1333468fc05fa98ad2d456f89d2ea934250517af265f803e8408f9b"
V2_SHA = "sha256:7cd5b6cf8070aa792c3793e55f332f139953897180ec792f2f893113df680bf9"
QZERO_FAILURE = "F-YM-S1A1-C001-QZERO-LOGARITHM-DOMAIN"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _self_hash(value: dict, field: str = "artifact_hash") -> str:
    payload = copy.deepcopy(value)
    observed = payload[field]
    payload[field] = ""
    assert observed == _canonical_hash(payload)
    return observed


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _validate(instance: dict, schema_path: Path) -> None:
    schema = _load(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(instance)


def test_qzero_failure_lattice_successor_is_schema_valid_and_versioned() -> None:
    old = _load(OLD_LATTICE)
    lattice = _load(LATTICE)
    _validate(lattice, FRAMEWORK_SCHEMAS / "failure-experience-lattice.schema.json")

    assert lattice["experiences"][0] == old["experiences"][0]
    failure = next(item for item in lattice["experiences"] if item["failure_id"] == QZERO_FAILURE)
    _self_hash(failure)
    assert failure["candidate_id"] == "YM-S1A1-C001-DENSE-SOURCE-COMMON-RATE-SPECTRAL-EXCLUSION"
    assert failure["research_trace_event_id"] == "YM-S1A1-E014"
    assert {"trace-event:YM-S1A1-E013", "trace-event:YM-S1A1-E014"} <= set(
        failure["evidence_pointers"]
    )
    assert failure["diagnosis_status"] == "SUPPORTED"
    assert "abstract q=0 spectral exclusion itself is not refuted" in failure["failure_mode"]

    links = [item for item in lattice["links"] if item["source_id"] == QZERO_FAILURE]
    assert len(links) == 1
    assert links[0]["relation"] == "RESOLVED_BY"
    assert links[0]["target_id"] == "YM-S1A1-C001-V2-DENSE-SOURCE-COMMON-RATE-SPECTRAL-EXCLUSION"


def test_historical_v1_v2_and_correction_trace_are_immutable_and_noncrediting() -> None:
    receipt = _load(RECEIPT)
    _validate(receipt, ROOT / "schemas/retrospective-correction-chronology-receipt.schema.json")
    _self_hash(receipt)

    bindings = receipt["historical_bindings"]
    assert _file_hash(V1) == V1_SHA == bindings["v1"]["file_sha256"]
    assert _file_hash(V2) == V2_SHA == bindings["v2"]["file_sha256"]
    assert _file_hash(OLD_CORRECTION_TRACE) == bindings["correction_trace"]["file_sha256"]

    old_trace = _load(OLD_CORRECTION_TRACE)
    types = [entry["event_type"] for entry in old_trace["entries"]]
    assert types[:3] == ["REVIEWED", "RESIDUAL_OPENED", "CANDIDATE_PROPOSED"]
    assert "EXPERIENCE_MEMORY_REVIEW" not in types[:3]

    audit = receipt["chronology_audit"]
    assert audit["strict_trace_valid_for_v2_successor_discovery"] is False
    assert audit["historical_trace_bytes_preserved"] is True
    classification = receipt["classification"]
    assert classification["v2_correction"] == "RETROSPECTIVE_EXTERNAL_REVIEW_CORRECTION"
    assert classification["strict_successor_discovery_credit"] == "NONE"
    assert classification["future_gate_effect"] == "FUTURE_CANDIDATES_ONLY"
    assert classification["independent_review"] is False
    assert classification["root_authority"] == "NONE"


def test_fresh_child_context_and_dual_memory_are_exact_and_pass_current_gates() -> None:
    context_raw = _load(CONTEXT)
    _validate(context_raw, FRAMEWORK_SCHEMAS / "math-context-fiber.schema.json")
    context_payload = copy.deepcopy(context_raw)
    context_payload["packet_hash"] = ""
    assert context_raw["packet_hash"] == _canonical_hash(context_payload)

    context = MathContextFiber(
        atom_id=context_raw["atom_id"],
        object_context=context_raw["object_context"],
        structural_coordinates=tuple(context_raw["structural_coordinates"]),
        equivalent_formulations=tuple(context_raw["equivalent_formulations"]),
        solved_analogues=tuple(context_raw["solved_analogues"]),
        near_solved_analogues=tuple(context_raw["near_solved_analogues"]),
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
            for item in context_raw["cross_domain_analogies"]
        ),
        analogy_scan_notes=context_raw["analogy_scan_notes"],
        frozen_at=context_raw["frozen_at"],
        first_candidate_at=context_raw["first_candidate_at"],
        packet_hash=context_raw["packet_hash"],
    )
    assert audit_math_context_fiber(context).verdict is ContextGateVerdict.PASS

    memory_raw = _load(MEMORY)
    _validate(memory_raw, FRAMEWORK_SCHEMAS / "research-memory-review.schema.json")
    _self_hash(memory_raw)
    assert memory_raw["tool_inventory_snapshot_hash"] == _canonical_hash(_load(TOOL_INVENTORY))
    assert memory_raw["failure_lattice_snapshot_hash"] == _canonical_hash(_load(LATTICE))
    assert set(memory_raw["relevant_failure_ids"]) == {
        "F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE",
        QZERO_FAILURE,
    }

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
    assert (
        audit_research_memory_review(
            memory, atom_id=context.atom_id, context_hash=context.packet_hash
        ).verdict
        is ResearchMemoryVerdict.PASS
    )


def test_future_only_trace_is_hash_chained_complete_and_emits_no_candidate() -> None:
    context_raw = _load(CONTEXT)
    memory_raw = _load(MEMORY)
    trace_raw = _load(TRACE)
    _validate(trace_raw, FRAMEWORK_SCHEMAS / "math-research-trace.schema.json")

    previous = ""
    entries = []
    for raw in trace_raw["entries"]:
        assert raw["previous_event_hash"] == previous
        payload = copy.deepcopy(raw)
        observed = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert observed == _canonical_hash(payload)
        previous = observed
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

    types = [entry.event_type for entry in entries]
    assert types == [
        ResearchTraceEventType.ATOMIZED,
        ResearchTraceEventType.CONTEXT_FROZEN,
        ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    ]
    assert ResearchTraceEventType.CANDIDATE_PROPOSED not in types
    assert "NO_V3_EMITTED" in entries[-1].outputs
    assert "RETROACTIVE_CREDIT_DENIED_V1_V2" in entries[-1].outputs

    trace = MathResearchTrace(trace_id=trace_raw["trace_id"], entries=tuple(entries))
    assert (
        audit_pre_candidate_trace(
            trace,
            atom_id=context_raw["atom_id"],
            context_packet_hash=context_raw["packet_hash"],
        ).verdict
        is TraceGateVerdict.FAIL
    )

    # The packet is a real prospective gate, but no candidate is emitted by this repair.
    context = MathContextFiber(
        atom_id=context_raw["atom_id"], object_context=context_raw["object_context"],
        structural_coordinates=tuple(context_raw["structural_coordinates"]),
        equivalent_formulations=tuple(context_raw["equivalent_formulations"]),
        solved_analogues=tuple(context_raw["solved_analogues"]),
        near_solved_analogues=tuple(context_raw["near_solved_analogues"]),
        method_transfers=tuple(MethodTransfer(
            source_context=x["source_context"], method=x["method"],
            shared_structure=tuple(x["shared_structure"]),
            required_assumptions=tuple(x["required_assumptions"]),
            disanalogies=tuple(x["disanalogies"]), repair_question=x["repair_question"],
            source_anchors=tuple(x["source_anchors"]),
        ) for x in context_raw["method_transfers"]),
        explicit_disanalogies=tuple(context_raw["explicit_disanalogies"]),
        source_anchors=tuple(context_raw["source_anchors"]),
        analogy_scan_status=context_raw["analogy_scan_status"],
        cross_domain_analogies=(), analogy_scan_notes=context_raw["analogy_scan_notes"],
        frozen_at=context_raw["frozen_at"], first_candidate_at=None,
        packet_hash=context_raw["packet_hash"],
    )
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
    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("immutable v1", "retrospective v2", "future successor"),
            relations=("supersession", "dual memory", "strict chronology"),
            domain="mathematical assurance / positive-operator statement governance",
            goal_type="gate only future candidate generation after q-zero failure learning",
        ),
        record=MathResearchRecord(claim_id=context.atom_id),
        context_fiber=context,
        memory_review=memory,
        research_trace=trace,
    )
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.CANNOT_CHECK
    assert plan.trace_gate.verdict is TraceGateVerdict.CANNOT_CHECK
    assert plan.candidate_generation_allowed is False
    assert plan.pre_candidate_actions == REQUIRED_SHORTCUT_ACTIONS
    assert all("CANDIDATE_PROPOSED" not in item for item in entries[-1].outputs)
