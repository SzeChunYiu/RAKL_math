from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import ResearchTraceEventType, TraceGateVerdict
from rakl.root_coordinate_preservation import PreservationGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/cross_problem/poincare_transfer/09_trace/pc_ns001_pre_candidate_fixture.py"


def _module(name: str):
    spec = importlib.util.spec_from_file_location(name, FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_pc_ns001_strict_gate_licenses_only_one_transfer_falsifier() -> None:
    module = _module("pc_ns001_gate")
    plan, fiber, memory, transformation_memory, shortcut, trace, _ = module.build_current_gate_plan()
    assert module.APPLICATION_BASE_SHA == "ec8a9eb5eeedaaf1d3f497a8688384256a2079e0"
    assert module.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.candidate_generation_allowed is True
    assert shortcut.selected_mode is ShortcutMode.JUMP
    assert shortcut.selected_episode_ids == (
        "E-PC-ENTROPY-NONCOLLAPSE-CANONICAL-SURGERY-EXTINCTION",
    )
    assert fiber.first_candidate_at is None
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
    assert transformation_memory.snapshot_hash == shortcut.episode_memory_snapshot_hash
    assert memory.selected_tool_ids == ("T-XM-ROOT-BRIDGE-STABILITY-AUDIT",)


def test_pc_ns001_documents_match_fixture_and_framework_schemas() -> None:
    module = _module("pc_ns001_docs")
    expected = module.build_documents()
    for name, document in expected.items():
        path = ROOT / module.PATHS[name]
        assert path.is_file(), path
        assert _load(path) == document

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


def test_poincare_chain_is_composite_source_success_not_monotonicity_only() -> None:
    module = _module("pc_ns001_chain")
    documents = module.build_documents()
    receipt = documents["source_receipt"]
    assert [row["arxiv_id"] for row in receipt["sources"]] == [
        "math/0211159v1",
        "math/0303109v1",
        "math/0307245v1",
    ]
    assert all(len(row["pdf_sha256"]) == 64 for row in receipt["sources"])
    chain = documents["success_chain"]
    assert [row["step_id"] for row in chain["transformation_chain"]] == [
        "PC-T1-ENTROPY",
        "PC-T2-NONCOLLAPSE",
        "PC-T3-CANONICAL-NEIGHBORHOODS",
        "PC-T4-SURGERY-CONTINUATION",
        "PC-T5-FINITE-EXTINCTION",
    ]
    assert chain["target_transfer_authority"] == "NONE"
    assert any("T1 does not imply T3" in item for item in chain["composition_obligations"])
    assert any("T3 does not imply T5" in item for item in chain["composition_obligations"])


def test_pre_candidate_packet_contains_no_target_field_or_result() -> None:
    module = _module("pc_ns001_blind")
    documents = module.build_documents()
    serialized = json.dumps(documents, sort_keys=True)
    assert "TARGET_FIELD_NOT_FROZEN" in serialized
    assert "CANDIDATE_PROPOSED" not in serialized
    assert "POSITIVE_DERIVATIVE_OBSERVED" not in serialized
    atom = documents["atomization"]
    assert atom["candidate_proposed"] is False
    assert atom["target_field_frozen"] is False
    assert atom["target_algebra_executed"] is False
    gate = documents["gate"]
    assert gate["gate_verdicts"]["licensed_action"] == (
        "FREEZE_ONE_EXPLICIT_3D_NS_ENSTROPHY_SIGN_FALSIFIER"
    )
    assert gate["authority"]["navier_stokes_root_status"] == (
        "OPEN_NO_SOLUTION_CERTIFICATE"
    )
    assert gate["authority"]["independent_review_credit"] == 0


def test_full_document_integrity_is_content_bound() -> None:
    module = _module("pc_ns001_integrity")
    documents = module.build_documents()
    bindings = documents["gate"]["full_document_integrity"]["inputs"]
    for name, binding in bindings.items():
        assert binding["path"] == module.PATHS[name]
        assert binding["canonical_sha256"] == module._hash(documents[name])
