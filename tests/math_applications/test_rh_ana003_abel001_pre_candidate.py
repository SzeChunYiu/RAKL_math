from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.framework_candidate_freeze import CandidateFreezeRevalidationVerdict
from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import ResearchTraceEventType, TraceGateVerdict
from rakl.root_coordinate_preservation import PreservationGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003_abel001_pre_candidate_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("rh_abel001_pre", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_strict_v3_gate_licenses_only_candidate_freeze() -> None:
    module = _module()
    plan, fiber, memory, tm, shortcut, trace, _ = module.build_current_gate_plan()
    assert module.APPLICATION_BASE_SHA == "58de5548d337d4ea3c83b5fcde6ed5c6aee3f2e0"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.framework_subject_gate.verdict is CandidateFreezeRevalidationVerdict.CURRENT_UNCHANGED
    assert plan.candidate_generation_allowed is True
    assert shortcut.selected_mode is ShortcutMode.SEARCH
    assert shortcut.selected_episode_ids == ("E-CLASSICAL-FINITE-ABEL-SUMMATION",)
    assert fiber.first_candidate_at is None
    assert tm.snapshot_hash == shortcut.episode_memory_snapshot_hash
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


def test_documents_match_fixture_and_v3_schemas() -> None:
    module = _module()
    expected = module.build_documents()
    assert set(expected) == set(module.PATHS)
    for name, relative in module.PATHS.items():
        assert _load(ROOT / relative) == expected[name]
    schemas = {
        "context": "math-context-fiber.schema.json",
        "memory": "research-memory-review.schema.json",
        "transformation_memory": "obstruction-transformation-memory.schema.json",
        "shortcut_review": "obstruction-transformation-review.schema.json",
        "preservation": "root-coordinate-preservation-receipt-v1.schema.json",
        "trace": "math-research-trace.schema.json",
    }
    for name, schema_name in schemas.items():
        schema = _load(ROOT / "framework/RAKL/schemas" / schema_name)
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(expected[name])


def test_packet_is_mathematics_first_and_result_inert() -> None:
    module = _module()
    documents = module.build_documents()
    atom = documents["atomization"]
    source = documents["source_packet"]
    gate = documents["gate"]
    assert atom["qoi"] == "FIXED_N_NATURAL_ORDER_ABEL_IDENTITY_TRUTH_STATUS"
    assert atom["candidate_proposed"] is False
    assert atom["target_result_accessed"] is False
    assert source["sources"][0]["theorem"] == "Theorem 1.5"
    assert source["sources"][0]["equation_1_3"] == "Delta(x)=|psi(x)-x|/x"
    assert "unmerged PR316" in source["excluded_authority"]
    assert gate["gate_verdicts"]["licensed_action"] == (
        "FREEZE_FIXED_N_ABEL_CANDIDATE_PROOF_INPUTS_AND_INERT_EVALUATOR_ONLY"
    )
    assert gate["chronology"] == {
        "candidate_identity": None,
        "candidate_proposed": False,
        "target_result_accessed": False,
        "evaluator_executed": False,
    }
    assert gate["authority"]["mathematical_result_credit"] is False
    assert gate["authority"]["grants_li_or_rh_authority"] is False


def test_pre_candidate_source_has_no_evaluator_or_candidate_result_capability() -> None:
    text = FIXTURE.read_text(encoding="utf-8")
    for forbidden in (
        "sympy",
        "mpmath",
        "subprocess",
        "scipy",
        "candidate_result",
    ):
        assert forbidden not in text
