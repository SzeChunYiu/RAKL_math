from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.research_trace import ResearchTraceEventType
from rakl.semantic_shortcut import ShortcutMode


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c052_k31_overlap_pre_candidate_fixture.py"


def module():
    spec = importlib.util.spec_from_file_location("c052_k31_overlap_pre", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_documents_match_fixture_and_typed_schemas() -> None:
    m = module()
    documents = m.build_documents()
    assert set(documents) == set(m.PATHS)
    for name, relative in m.PATHS.items():
        assert load(ROOT / relative) == documents[name]
    schemas = {
        "context": "math-context-fiber.schema.json",
        "memory": "research-memory-review.schema.json",
        "transformation_memory": "obstruction-transformation-memory.schema.json",
        "shortcut_review": "obstruction-transformation-review.schema.json",
        "trace": "math-research-trace.schema.json",
    }
    for name, schema in schemas.items():
        jsonschema.Draft202012Validator(
            load(ROOT / "framework/RAKL/schemas" / schema), format_checker=jsonschema.FormatChecker()
        ).validate(documents[name])


def test_exact_object_support_cells_and_source_identities_are_frozen() -> None:
    m = module()
    context = load(ROOT / m.PATHS["context"])
    firewall = load(ROOT / m.PATHS["firewall"])
    assert "H_31 ∩ P_32" in context["object_context"]
    assert firewall["parent_support_cell"] == m.PARENT_CELL
    assert firewall["exhaustive_current_support_cells"] == m.CURRENT_CELLS
    assert firewall["parent_support_cell"]["k"] == 31
    assert {row["a"] for row in firewall["exhaustive_current_support_cells"]} == {1, 4, 6}
    assert firewall["source_bindings"] == m.SOURCE_BINDINGS


def test_memory_review_uses_math_success_and_failures_without_extrapolation() -> None:
    m = module()
    memory = load(ROOT / m.PATHS["memory"])
    assert memory["selected_tool_ids"] == ["T-PNP-C048-EXACT-OVERLAP-TRANSFER-CONDITION"]
    assert "F-PNP-C050-K15-FIXED-VARIABLE-BIT-VERSUS-MAGIC" in memory["relevant_failure_ids"]
    assert any("cannot be extrapolated" in note for note in memory["failure_reuse_notes"])
    assert any("marginal witnesses" in warning for warning in memory["unresolved_warnings"])


def test_roles_shortcut_and_plan_fail_closed_before_candidate() -> None:
    m = module()
    expert = load(ROOT / m.PATHS["expert_review"])
    shortcut = load(ROOT / m.PATHS["shortcut_review"])
    assert {row["role"] for row in expert["role_reviews"]} == {
        "domain_theory_lead", "analogy_method_transfer_lead", "adversarial_falsification_lead",
        "formal_methods_lead", "novelty_research_value_lead",
    }
    assert "NOT_INDEPENDENT_PEER_REVIEW" in expert["review_authority"]
    assert shortcut["selected_mode"] == ShortcutMode.CANNOT_CHECK.value
    assert m.build_plan().candidate_generation_allowed is False


def test_certificates_are_candidate_independent_and_result_firewall_is_closed() -> None:
    m = module()
    firewall = load(ROOT / m.PATHS["firewall"])
    chronology = firewall["chronology_firewall"]
    assert len(firewall["candidate_independent_positive_certificate_requirements"]) == 5
    assert len(firewall["candidate_independent_negative_certificate_requirements"]) == 5
    assert all(value is False for value in chronology.values())
    assert firewall["allowed_future_branches"] == [
        "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE", "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE", "CANNOT_CHECK"
    ]
    source = FIXTURE.read_text(encoding="utf-8")
    for forbidden in ("from C041_fx_sat_one_sided", "import C041_fx_sat_one_sided", "decode_formula", "is_satisfiable", "subprocess"):
        assert forbidden not in source


def test_trace_is_strictly_ordered_hash_chained_and_candidate_free() -> None:
    m = module()
    entries = load(ROOT / m.PATHS["trace"])["entries"]
    context = load(ROOT / m.PATHS["context"])
    memory = load(ROOT / m.PATHS["memory"])
    shortcut = load(ROOT / m.PATHS["shortcut_review"])
    assert [entry["event_type"] for entry in entries] == [event.value for event in (
        ResearchTraceEventType.ATOMIZED, ResearchTraceEventType.CONTEXT_FROZEN, ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW, ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW, ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    )]
    assert [entry["timestamp"] for entry in entries] == sorted(entry["timestamp"] for entry in entries)
    assert len({entry["timestamp"] for entry in entries}) == len(entries)
    assert entries[0]["previous_event_hash"] == ""
    for previous, current in zip(entries, entries[1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    assert context["packet_hash"] in entries[1]["outputs"]
    assert context["packet_hash"] in entries[2]["outputs"]
    assert context["packet_hash"] in entries[3]["outputs"]
    assert memory["artifact_hash"] in entries[5]["outputs"]
    assert shortcut["artifact_hash"] in entries[6]["outputs"]
    assert shortcut["episode_memory_snapshot_hash"] in entries[6]["outputs"]
    assert "CANDIDATE_PROPOSED" not in [entry["event_type"] for entry in entries]
    gate = load(ROOT / m.PATHS["gate"])
    assert gate["candidate_generation_in_this_round"] is False
    assert gate["overlap_result_accessed"] is False
    assert gate["git_ci_trace_mathematical_credit"] == 0
