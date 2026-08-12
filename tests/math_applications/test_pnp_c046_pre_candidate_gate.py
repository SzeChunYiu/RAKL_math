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
FIXTURE = PNP / "09_trace/c046_canonical_collision_pre_candidate_fixture.py"
VERIFIER = PNP / "09_trace/verify_c046_pre_candidate_packet.py"

ARTIFACTS = {
    "atomization": PNP / "02_problem_dag/O9d12a2a1b_C046_ATOMIZATION_20260812.json",
    "context": PNP / "01_frontier/O9d12a2a1b_C046_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": PNP / "07_memory/O9d12a2a1b_C046_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": PNP / "07_memory/O9d12a2a1b_C046_FAILURE_SNAPSHOT_20260812.json",
    "memory": PNP / "07_memory/O9d12a2a1b_C046_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": PNP / "07_memory/O9d12a2a1b_C046_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": PNP / "08_reviews/O9d12a2a1b_C046_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": PNP / "08_reviews/O9d12a2a1b_C046_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": PNP / "09_trace/O9d12a2a1b_C046_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C046_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": PNP / "09_trace/O9d12a2a1b_C046_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}


def _load_module(name: str, path: Path):
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


def test_c046_v3_pre_candidate_gates_license_only_a_separation_lemma_freeze() -> None:
    module = _load_module("pnp_c046_pre_candidate_fixture", FIXTURE)
    plan, fiber, memory, transformation_memory, shortcut, trace, preservation = (
        module.build_current_gate_plan()
    )
    assert module.APPLICATION_BASE_SHA == "ac8c0745be8aed791a446fd55fcf5154cac01962"
    assert module.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert shortcut.selected_mode is ShortcutMode.SEARCH
    assert shortcut.selected_episode_ids == (
        "E-PNP-C046-PARTITION-INVARIANT-BEFORE-TARGET-SCAN",
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


def test_c046_documents_match_fixture_and_current_framework_schemas() -> None:
    module = _load_module("pnp_c046_pre_candidate_fixture_docs", FIXTURE)
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


def test_c046_gate_is_target_blind_and_mathematics_first() -> None:
    module = _load_module("pnp_c046_pre_candidate_fixture_blind", FIXTURE)
    documents = module.build_documents()
    serialized = json.dumps(documents, sort_keys=True)
    assert "TARGET_RESULT_UNACCESSED" in serialized
    assert "CANDIDATE_PROPOSED" not in serialized
    assert "NO_QUALIFYING_CANONICAL_TARGET" not in serialized

    atom = documents["atomization"]
    assert atom["qoi"] == "LEAST_CANONICAL_UNSAT_PREFIX_ROW_COLLISION_OR_NONE"
    assert atom["allowed_result_branches"] == [
        "FINITE_LEAST_COLLISION_LEVEL",
        "NO_COLLISION_IN_FROZEN_ONE_SIDED_FAMILY",
        "CANNOT_CHECK",
    ]
    assert atom["target_result_accessed"] is False

    gate = documents["gate"]
    assert gate["gate_verdicts"]["licensed_action"] == (
        "FREEZE_HIGH_HALF_SEPARATION_LEMMA_CANDIDATE_ONLY"
    )
    assert gate["application_authority"]["target_evaluator_execution_authorized"] is False
    assert gate["chronology"]["candidate_identity"] is None
    assert gate["chronology"]["target_result_accessed"] is False
    assert gate["authority"]["mathematical_saturation_credit"] is False
    assert gate["authority"]["mathematical_result_credit"] is False

    # The assurance implementation itself cannot import or execute the decoder.
    source = FIXTURE.read_text(encoding="utf-8") + VERIFIER.read_text(encoding="utf-8")
    for forbidden in (
        "from C041_fx_sat_one_sided",
        "import C041_fx_sat_one_sided",
        "decode_formula",
        "is_satisfiable",
        "materialize_complement",
        "importlib",
        "subprocess",
    ):
        assert forbidden not in source


def test_c046_expert_and_memory_reviews_preserve_authority_boundaries() -> None:
    expert = _load(ARTIFACTS["expert_review"])
    assert expert["review_authority"] == (
        "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW"
    )
    assert {row["role"] for row in expert["role_reviews"]} == {
        "domain_theory_lead",
        "analogy_method_transfer_lead",
        "adversarial_falsification_lead",
        "formal_methods_lead",
        "novelty_research_value_lead",
    }
    memory = _load(ARTIFACTS["memory"])
    assert memory["selected_tool_ids"] == [
        "T-PNP-PARTITION-INVARIANT-FEASIBILITY-FIRST"
    ]
    assert "F-C045-U17-PROJECTION-DISJOINT" in memory["relevant_failure_ids"]
    assert "F-C043-FIRST-ROW-SPLIT-TYPE-CEILING" in memory["relevant_failure_ids"]


def test_c046_full_document_verifier_passes_and_rejects_stale_hash(tmp_path: Path) -> None:
    verifier = _load_module("pnp_c046_pre_candidate_verifier", VERIFIER)
    assert verifier.audit_packet(ROOT) == ()
    verifier.verify_packet(ROOT)

    for name, source_path in ARTIFACTS.items():
        target = tmp_path / source_path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source_path.read_bytes())
    context = _load(tmp_path / ARTIFACTS["context"].relative_to(ROOT))
    context["structural_coordinates"].append("HOSTILE_STALE_HASH_MUTATION")
    (tmp_path / ARTIFACTS["context"].relative_to(ROOT)).write_text(
        json.dumps(context, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    errors = verifier.audit_packet(tmp_path)
    assert any("context: full-document digest mismatch" in error for error in errors)
