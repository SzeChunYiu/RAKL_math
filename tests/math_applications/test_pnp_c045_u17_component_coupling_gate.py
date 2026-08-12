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
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c045_u17_component_coupling_pre_candidate_fixture.py"

ARTIFACTS = {
    "atomization": PNP / "02_problem_dag/O9d12a2a1b_C045_ATOMIZATION_20260812.json",
    "context": PNP / "01_frontier/O9d12a2a1b_C045_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": PNP / "07_memory/O9d12a2a1b_C045_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": PNP / "07_memory/O9d12a2a1b_C045_FAILURE_SNAPSHOT_20260812.json",
    "memory": PNP / "07_memory/O9d12a2a1b_C045_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": PNP / "07_memory/O9d12a2a1b_C045_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": PNP / "08_reviews/O9d12a2a1b_C045_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": PNP / "08_reviews/O9d12a2a1b_C045_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": PNP / "09_trace/O9d12a2a1b_C045_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C045_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": PNP / "09_trace/O9d12a2a1b_C045_LATEST_RAKL_GATE_RECEIPT_20260812.json",
}


def _load_fixture():
    spec = importlib.util.spec_from_file_location("pnp_c045_pre_candidate_fixture", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from _walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_keys(child)


def test_c045_all_current_v3_pre_candidate_gates_pass_without_candidate() -> None:
    module = _load_fixture()
    plan, fiber, memory, transformation_memory, shortcut, trace, preservation = (
        module.build_current_gate_plan()
    )
    assert module.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert module.APPLICATION_BASE_SHA == "e768b7da7dc48739ccb581dea0eb2cfeb8a701e7"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert shortcut.selected_mode is ShortcutMode.SEARCH
    assert shortcut.selected_episode_ids == ("E-PNP-C044-EXACT-COMPONENT-COUPLING-GATE",)
    assert transformation_memory.snapshot_hash
    assert memory.selected_tool_ids == ("T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",)
    assert fiber.first_candidate_at is None
    assert preservation.root_claim_id == module.ATOM
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


def test_c045_artifacts_are_schema_valid_and_match_runtime_fixture() -> None:
    module = _load_fixture()
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
        "preservation": "root-coordinate-preservation-receipt-v1.schema.json",
        "trace": "math-research-trace.schema.json",
    }
    for name, schema_name in schema_names.items():
        schema = _load(ROOT / "framework/RAKL/schemas" / schema_name)
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(expected[name])


def test_c045_packet_is_result_blind_and_has_no_target_capability() -> None:
    module = _load_fixture()
    documents = module.build_documents()
    forbidden_keys = {
        "result",
        "observed_result",
        "target_outcome",
        "quotient_complement",
        "explicit_pairs",
        "target_cells",
        "witness_cells",
        "target_count",
        "cover_number",
    }
    assert not (forbidden_keys & set(_walk_keys(documents)))

    artifact_text = "\n".join(
        json.dumps(document, sort_keys=True) for document in documents.values()
    )
    assert "TARGET_OUTCOME_UNOBSERVED" in artifact_text
    assert "CANDIDATE_PROPOSED" not in artifact_text
    assert "rho(G17)=" not in artifact_text
    assert "rho(G_17)=" not in artifact_text

    fixture_text = FIXTURE.read_text(encoding="utf-8")
    for forbidden in (
        "C041_fx_sat_one_sided",
        "decode_formula",
        "is_satisfiable",
        "canonical_cover_oracle",
        "full_cover_oracle",
        "c043_first_row_split_gate",
        "c044_retrospective_quotient_multiplexing",
        "subprocess",
    ):
        assert forbidden not in fixture_text


def test_c045_freezes_branch_complete_incidence_gate_without_an_outcome() -> None:
    atomization = _load(ARTIFACTS["atomization"])
    assert atomization["target_extension"] == "U16_TO_U17_IMMEDIATE_SOURCE_EXTENSION"
    assert atomization["qoi"] == "EXACT_FULL_HISTORY_QUOTIENT_COMPONENT_INCIDENCE"
    assert atomization["allowed_result_branches"] == [
        "NO_NEW_SEMANTIC_CELL",
        "NO_CROSS_COMPONENT_COUPLING",
        "CROSS_COMPONENT_COUPLING_WITNESS",
        "OLD_TYPE_COLLISION_OR_SPLIT",
        "CANNOT_CHECK",
    ]
    assert atomization["candidate_generation_allowed"] is False
    assert atomization["target_output_accessed"] is False

    gate = _load(ARTIFACTS["gate"])
    assert gate["gate_verdicts"]["candidate_generation_allowed"] is True
    assert gate["gate_verdicts"]["licensed_action"] == (
        "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"
    )
    assert gate["chronology"]["candidate_identity"] is None
    assert gate["chronology"]["candidate_proposed"] is False
    assert gate["chronology"]["target_output_accessed"] is False
    assert gate["authority"]["grants_mathematical_result"] is False
    assert gate["authority"]["grants_p_vs_np_authority"] is False
