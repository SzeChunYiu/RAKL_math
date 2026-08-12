from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import TraceGateVerdict
from rakl.semantic_shortcut import ShortcutReviewVerdict, ShortcutMode

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/p_vs_np/09_trace/c043_current_v3_pre_candidate_fixture.py"


def _load_fixture():
    spec = importlib.util.spec_from_file_location("pnp_c043_current_v3_fixture", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_c043_current_v3_pre_candidate_gates_pass_prospectively() -> None:
    module = _load_fixture()
    plan, fiber, memory_review, transformation_memory, shortcut_review, trace = module.build_current_gate_plan()
    assert module.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert module.APPLICATION_BASE_SHA == "9074c257e4fd3179c56ffdedc859efc972cd1c88"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert shortcut_review.selected_mode is ShortcutMode.SEARCH
    assert transformation_memory.snapshot_hash
    assert memory_review.artifact_hash
    assert fiber.first_candidate_at is None
    assert len(trace.entries) == 8
