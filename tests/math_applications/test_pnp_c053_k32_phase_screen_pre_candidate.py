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
SCREEN = PNP / "03_routes/c053_k32_phase_screen.py"
FIXTURE = PNP / "09_trace/c053_k32_phase_screen_pre_candidate_fixture.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_source_bound_phase_screen_proves_k32_is_first_survivor_after_k31() -> None:
    screen = load_module("c053_k32_screen", SCREEN)
    report = screen.classify()
    assert report["bounded_k_values"] == [31, 32]
    assert report["k31"]["parameter_pair_count"] == 82
    assert report["k31"]["surviving_parameter_pair_count"] == 0
    assert report["k32"]["parameter_pair_count"] == 42148
    assert report["k32"]["endpoint_forced_conflict_count"] == 0
    assert report["k32"]["mapped_illegal_token_count"] == 17668
    assert report["k32"]["surviving_parameter_pair_count"] == 24480
    assert report["least_surviving_k"] == 32
    assert report["overlap_or_sat_accessed"] is False


def test_exact_k32_cell_phase_matrix_is_complete() -> None:
    screen = load_module("c053_k32_matrix", SCREEN)
    rows = screen.classify()["k32"]["cell_phase_matrix"]
    assert len(rows) == 6
    by_cells = {(row["parent_cell"], row["current_cell"]): row for row in rows}
    assert by_cells[((4, 3), (3, 4))]["surviving_parameter_pair_count"] == 32
    assert by_cells[((6, 2), (3, 4))]["surviving_parameter_pair_count"] == 128
    assert by_cells[((6, 2), (11, 1))]["surviving_parameter_pair_count"] == 24320
    assert by_cells[((1, 8), (3, 4))]["surviving_parameter_pair_count"] == 0
    assert by_cells[((1, 8), (11, 1))]["surviving_parameter_pair_count"] == 0
    assert by_cells[((4, 3), (11, 1))]["surviving_parameter_pair_count"] == 0


def test_prepended_h_zero_is_never_treated_as_a_parent_token_coordinate() -> None:
    screen = load_module("c053_k32_prepended_bit", SCREEN)
    synthetic_parent = {"m": 1, "header": 9, "width": 2}
    rows = screen.mapped_fixed_header_tokens(synthetic_parent, current_v=1, current_m=1, k=10)
    assert all(row["h_start"] >= 1 for row in rows)
    assert 0 not in {row["h_start"] for row in rows}


def test_documents_match_fixture_and_typed_v3_schemas() -> None:
    fixture = load_module("c053_k32_fixture", FIXTURE)
    documents = fixture.build_documents()
    assert set(documents) == set(fixture.PATHS)
    for name, relative in fixture.PATHS.items():
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
            load(ROOT / "framework/RAKL/schemas" / schema),
            format_checker=jsonschema.FormatChecker(),
        ).validate(documents[name])


def test_context_memory_and_external_ledger_authority_are_bounded() -> None:
    fixture = load_module("c053_k32_memory", FIXTURE)
    context = load(ROOT / fixture.PATHS["context"])
    memory = load(ROOT / fixture.PATHS["memory"])
    authority = load(ROOT / fixture.PATHS["authority_boundary"])
    assert "k=32" in context["object_context"]
    assert "F-PNP-C052-K31-ACTUAL-OVERLAP-EMPTY-BY-SYNTAX-DICHOTOMY" in memory["relevant_failure_ids"]
    assert authority["promotable_external_results"] == [
        "C037 exact finite strict-decrease replay",
        "U8 reconstructed full-union LP value 49/24",
    ]
    assert authority["missing_certificate_claims"]["C035/C036/C039/C040"] == "CANNOT_CHECK"
    assert authority["external_packet_root_authority"] == "NONE"


def test_learning_artifact_contains_only_seven_mathematical_fields() -> None:
    fixture = load_module("c053_k32_lesson", FIXTURE)
    lesson = load(ROOT / fixture.PATHS["mathematical_lesson"])
    fields = lesson["seven_field_mathematical_lesson"]
    assert set(fields) == {
        "attempted_implication",
        "exact_theorem_or_failure",
        "supported_and_competing_mathematical_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_mathematical_move",
        "proof_and_source_evidence",
    }
    text = json.dumps(fields).lower()
    for non_math in ("git", " ci ", "schema", "hash", "chronology", "workflow"):
        assert non_math not in text


def test_shortcut_review_uses_search_with_exact_mapping_not_topic_similarity() -> None:
    fixture = load_module("c053_k32_shortcut", FIXTURE)
    shortcut = load(ROOT / fixture.PATHS["shortcut_review"])
    assert shortcut["selected_mode"] == ShortcutMode.SEARCH.value
    assert shortcut["selected_episode_ids"] == ["E-PNP-C052-K31-FULL-WORD-SCREEN"]
    assert len(shortcut["direct_mapping_witnesses"]) == 1
    witness = shortcut["direct_mapping_witnesses"][0]
    assert witness["unmatched_source_preconditions"] == []
    assert any("k31" in item.lower() and "k32" in item.lower() for item in witness["disanalogies"])


def test_trace_and_discriminator_proposal_are_candidate_and_result_free() -> None:
    fixture = load_module("c053_k32_trace", FIXTURE)
    trace = load(ROOT / fixture.PATHS["trace"])["entries"]
    expected = [event.value for event in (
        ResearchTraceEventType.ATOMIZED,
        ResearchTraceEventType.CONTEXT_FROZEN,
        ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
        ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    )]
    assert [entry["event_type"] for entry in trace] == expected
    assert trace[0]["previous_event_hash"] == ""
    for previous, current in zip(trace, trace[1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    assert "CANDIDATE_PROPOSED" not in expected
    proposal = load(ROOT / fixture.PATHS["discriminator_proposal"])
    gate = load(ROOT / fixture.PATHS["gate"])
    assert proposal["candidate_identity"] is None
    assert proposal["evaluator_identity"] is None
    assert proposal["overlap_result_accessed"] is False
    assert gate["candidate_generation_in_this_round"] is False
    assert gate["overlap_or_sat_result_accessed"] is False
    assert gate["git_ci_schema_hash_mathematical_credit"] == 0


def test_roles_preserve_disagreement_and_same_context_boundary() -> None:
    fixture = load_module("c053_k32_roles", FIXTURE)
    expert = load(ROOT / fixture.PATHS["expert_review"])
    assert {row["role"] for row in expert["role_reviews"]} == {
        "domain_theory_lead",
        "analogy_method_transfer_lead",
        "adversarial_falsification_lead",
        "formal_methods_lead",
        "novelty_research_value_lead",
    }
    assert expert["blocking_concerns"] == []
    assert "NOT_INDEPENDENT_PEER_REVIEW" in expert["review_authority"]
    assert "partial survivor" in expert["disagreement"].lower()
