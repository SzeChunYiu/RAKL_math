from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
from datetime import datetime

import jsonschema
from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import ResearchTraceEventType, TraceGateVerdict
from rakl.root_coordinate_preservation import PreservationGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c050_later_k_pre_candidate_fixture.py"
VERIFIER = PNP / "09_trace/verify_c050_pre_candidate_packet.py"
ARTIFACTS = {
    "atomization": PNP / "02_problem_dag/O9d12a2a1b_C050_ATOMIZATION_20260812.json",
    "context": PNP / "01_frontier/O9d12a2a1b_C050_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": PNP / "07_memory/O9d12a2a1b_C050_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": PNP / "07_memory/O9d12a2a1b_C050_FAILURE_SNAPSHOT_20260812.json",
    "memory": PNP / "07_memory/O9d12a2a1b_C050_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": PNP / "07_memory/O9d12a2a1b_C050_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": PNP / "08_reviews/O9d12a2a1b_C050_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": PNP / "08_reviews/O9d12a2a1b_C050_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": PNP / "09_trace/O9d12a2a1b_C050_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C050_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": PNP / "09_trace/O9d12a2a1b_C050_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_c050_strict_v3_gate_licenses_only_exact_later_k_discriminator() -> None:
    module = _module("pnp_c050_pre", FIXTURE)
    plan, fiber, memory, transformation_memory, shortcut, trace, preservation = module.build_current_gate_plan()
    assert module.APPLICATION_BASE_SHA == "5dd7c0d5084dfb0dd3cd3a1619badd30b532b975"
    assert module.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.candidate_generation_allowed is True
    assert shortcut.selected_mode is ShortcutMode.SEARCH
    assert shortcut.selected_episode_ids == ("E-PNP-C050-SYNCHRONIZED-CODE-LANGUAGE-INTERSECTION",)
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


def test_c050_documents_match_fixture_and_framework_schemas() -> None:
    module = _module("pnp_c050_pre_docs", FIXTURE)
    expected = module.build_documents()
    assert set(expected) == set(ARTIFACTS)
    for name, path in ARTIFACTS.items():
        assert _load(path) == expected[name]
    schemas = {
        "context": "math-context-fiber.schema.json",
        "memory": "research-memory-review.schema.json",
        "transformation_memory": "obstruction-transformation-memory.schema.json",
        "shortcut_review": "obstruction-transformation-review.schema.json",
        "preservation": "root-coordinate-preservation-receipt-v1.schema.json",
        "trace": "math-research-trace.schema.json",
    }
    for name, schema in schemas.items():
        jsonschema.Draft202012Validator(
            _load(ROOT / "framework/RAKL/schemas" / schema),
            format_checker=jsonschema.FormatChecker(),
        ).validate(expected[name])


def test_c050_gate_is_result_capability_free_and_mathematics_first() -> None:
    atom = _load(ARTIFACTS["atomization"])
    gate = _load(ARTIFACTS["gate"])
    assert atom["qoi"] == "LATER_K_FIELD_ALIGNMENT_OVERLAP_NONEMPTINESS_OR_IMPOSSIBILITY"
    assert atom["target_result_accessed"] is False
    assert gate["gate_verdicts"]["licensed_action"] == "FREEZE_FIRST_LATER_K_ALIGNMENT_DISCRIMINATOR_ONLY"
    assert gate["chronology"]["candidate_identity"] is None
    assert gate["authority"]["mathematical_saturation_credit"] is False
    source = FIXTURE.read_text(encoding="utf-8") + VERIFIER.read_text(encoding="utf-8")
    for forbidden in (
        "from C041_fx_sat_one_sided",
        "import C041_fx_sat_one_sided",
        "decode_formula",
        "is_satisfiable",
        "materialize_complement",
        "subprocess",
    ):
        assert forbidden not in source


def test_c050_memory_and_expert_roles_preserve_scope() -> None:
    memory = _load(ARTIFACTS["memory"])
    expert = _load(ARTIFACTS["expert_review"])
    assert memory["selected_tool_ids"] == ["T-PNP-C049-K12-FIXED-BIT-SEPARATION"]
    assert "F-PNP-C047-ORIENTATION-ONLY-INTERFACE-MISALIGNMENT" in memory["relevant_failure_ids"]
    assert {row["role"] for row in expert["role_reviews"]} == {
        "domain_theory_lead",
        "analogy_method_transfer_lead",
        "adversarial_falsification_lead",
        "formal_methods_lead",
        "novelty_research_value_lead",
    }
    assert "NOT_INDEPENDENT_PEER_REVIEW" in expert["review_authority"]
    assert "UNSAT" in expert["strongest_objection"]


def test_c050_trace_events_do_not_predate_atom_or_context_freeze() -> None:
    atom = _load(ARTIFACTS["atomization"])
    context = _load(ARTIFACTS["context"])
    trace = _load(ARTIFACTS["trace"])
    chronology_floor = max(
        datetime.fromisoformat(atom["recorded_at"].replace("Z", "+00:00")),
        datetime.fromisoformat(context["frozen_at"].replace("Z", "+00:00")),
    )
    assert all(
        datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
        > chronology_floor
        for entry in trace["entries"]
    )


def test_c050_full_document_verifier_detects_stale_context(tmp_path: Path) -> None:
    verifier = _module("pnp_c050_pre_verify", VERIFIER)
    assert verifier.audit_packet(ROOT) == ()
    for name, path in ARTIFACTS.items():
        target = tmp_path / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())
    context_path = tmp_path / ARTIFACTS["context"].relative_to(ROOT)
    context = _load(context_path)
    context["structural_coordinates"].append("HOSTILE_MUTATION")
    context_path.write_text(json.dumps(context, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert any("context: full-document digest mismatch" in error for error in verifier.audit_packet(tmp_path))
