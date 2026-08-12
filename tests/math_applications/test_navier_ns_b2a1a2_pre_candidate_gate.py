from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import ResearchTraceEventType, TraceGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"
FIXTURE = NS / "09_trace/ns_b2a1a2_pre_candidate_fixture.py"
ARTIFACTS = {
    "atomization": NS / "02_problem_dag/NS_B2A1A2_DELTA_20260812.json",
    "context": NS / "01_frontier/NS-B2a1a2_CONTEXT_FIBER_20260812.json",
    "memory": NS / "07_memory/NS-B2a1a2_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": NS / "07_memory/NS-B2a1a2_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": NS / "08_reviews/NS-B2a1a2_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": NS / "08_reviews/NS-B2a1a2_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "trace": NS / "09_trace/NS-B2a1a2_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": NS / "09_trace/NS-B2a1a2_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}


def _module():
    spec = importlib.util.spec_from_file_location("ns_b2a1a2_pre_candidate", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_b2a1a2_all_pre_candidate_gates_pass_before_canonical_candidate() -> None:
    module = _module()
    plan, context, memory, transformation_memory, shortcut, _, trace = module.build_plan()
    assert module.APPLICATION_BASE_SHA == "ac8c0745be8aed791a446fd55fcf5154cac01962"
    assert module.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert context.first_candidate_at is None
    assert shortcut.selected_mode is ShortcutMode.SEARCH
    assert shortcut.selected_episode_ids == (
        "OTEP-NS-B1a2-DIVERGENCE-FREE-SCALE-CALIBRATION",
    )
    assert transformation_memory.snapshot_hash
    assert memory.selected_tool_ids == ()
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


def test_b2a1a2_documents_match_fixture_and_framework_schemas() -> None:
    module = _module()
    expected = module.build_documents()
    assert set(expected) == set(ARTIFACTS)
    for name, path in ARTIFACTS.items():
        assert path.is_file(), path
        assert _load(path) == expected[name]

    schema_names = {
        "context": "math-context-fiber.schema.json",
        "memory": "research-memory-review.schema.json",
        "transformation_memory": "obstruction-transformation-memory.schema.json",
        "shortcut_review": "obstruction-transformation-review.schema.json",
        "trace": "math-research-trace.schema.json",
    }
    for name, schema_name in schema_names.items():
        schema = _load(ROOT / "framework/RAKL/schemas" / schema_name)
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(expected[name])


def test_b2a1a2_pre_candidate_packet_is_result_blind_and_fail_closed() -> None:
    documents = _module().build_documents()
    text = json.dumps(documents, sort_keys=True)
    atomization = documents["atomization"]
    gate = documents["gate"]

    assert atomization["candidate_identity"] is None
    assert atomization["candidate_proposed"] is False
    assert atomization["candidate_generation_allowed"] is False
    assert atomization["inherited_direction_preexisted_gate"] is True
    assert atomization["strict_discovery_credit"] is False
    assert gate["gate_verdicts"]["candidate_generation_allowed"] is True
    assert gate["authority"]["mathematical_result_credit"] is False
    assert gate["authority"]["strict_discovery_credit"] is False
    assert gate["authority"]["navier_stokes_solution_authority"] is False
    assert gate["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    for forbidden in (
        "NS-B2a1a2-C001",
        "A(v_k,a_k)=",
        "escaping-bump counterexample",
        "observed_result",
        "candidate_statement",
    ):
        assert forbidden not in text

