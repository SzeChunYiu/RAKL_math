from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.framework_candidate_freeze import CandidateFreezeRevalidationVerdict
from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace
from rakl.root_coordinate_preservation import PreservationGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict

ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003j_pre_candidate_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("rh_ana003j_pre", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_current_gate_is_fail_closed_before_any_candidate() -> None:
    module = _module()
    plan, fiber, memory, tm, shortcut, trace, _ = module.build_current_gate_plan()
    assert module.APPLICATION_BASE_SHA == "b7ca6ac51fa8319b559e95402c47959c626f284a"
    assert module.FRAMEWORK_SEMANTICS_SHA == "2834760f4ae96684654a2080f5f36b24dc1d1ef7"
    assert module.FRAMEWORK_CURRENT_SHA == "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
    assert module.FRAMEWORK_PIN_SHA == "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.CANNOT_CHECK
    assert plan.trace_gate.verdict is TraceGateVerdict.CANNOT_CHECK
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.framework_subject_gate.verdict is CandidateFreezeRevalidationVerdict.ACKNOWLEDGED_NON_METHOD_DRIFT
    assert plan.candidate_generation_allowed is False
    assert shortcut.selected_mode is ShortcutMode.CANNOT_CHECK
    assert shortcut.exhaustion_witness is None
    assert shortcut.missing_transformation_specification is None
    assert fiber.first_candidate_at is None
    assert tm.snapshot_hash == shortcut.episode_memory_snapshot_hash
    assert audit_pre_candidate_trace(
        trace,
        atom_id=module.ATOM,
        context_packet_hash=fiber.packet_hash,
        obstruction_transformation_review_hash=shortcut.artifact_hash,
    ).verdict is TraceGateVerdict.PASS


def test_documents_match_fixture_and_pinned_schemas() -> None:
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
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(expected[name])


def test_exact_quantifier_normal_forms_and_seven_axes_are_frozen() -> None:
    docs = _module().build_documents()
    atom = docs["atomization"]
    discriminator = docs["quantifier_discriminator"]
    assert "forall n forall epsilon>0 exists M(n,epsilon) forall Y>=M" in atom["source_quantifier_normal_form"]
    assert atom["target_quantifier_normal_form"] == "exists N forall n>=N: E(n,Y_n)<=epsilon_n"
    assert "M(n,epsilon_n)<=Y_n" in atom["missing_bridge_normal_form"]
    assert "C is one fixed real constant >0" in atom["parameter_scope"]
    assert "epsilon=(epsilon_n) is not frozen" in atom["parameter_scope"]
    assert discriminator["epsilon_sequence_identity"] is None
    assert discriminator["epsilon_sequence_status"] == "TO_BE_FROZEN_BEFORE_RESULT_EVALUATION"
    assert len(discriminator["quantifier_axes"]) == 7
    joined = " ".join(discriminator["quantifier_axes"])
    for term in ("fixed n", "diagonal", "threshold", "modulus", "internal prefix", "natural order", "Li/RH"):
        assert term in joined


def test_quantifier_table_is_complete_and_branches_unselected() -> None:
    docs = _module().build_documents()
    source = docs["source_packet"]
    discriminator = docs["quantifier_discriminator"]
    required = set(discriminator["required_table_fields"])
    assert len(source["source_target_quantifier_table"]) == 3
    assert all(required <= set(row) for row in source["source_target_quantifier_table"])
    allowed = {
        "UNIFORM_MODULUS_AND_DIAGONAL_COMPATIBILITY_PROVED",
        "POINTWISE_ONLY_NO_DIAGONAL_TRANSFER",
        "ENDPOINT_ONLY_NO_INTERNAL_PREFIX_TRANSFER",
        "CANNOT_CHECK",
    }
    assert set(source["allowed_future_result_branches"]) == allowed
    assert set(discriminator["allowed_future_result_branches"]) == allowed
    assert source["selected_result_branch"] is None
    assert discriminator["selected_result_branch"] is None
    assert discriminator["cheapest_hostile_world_to_execute_later"]["status"] == "FROZEN_NOT_EVALUATED"


def test_live_fail_closed_quantifier_semantics_are_mirrored_without_theorem_credit() -> None:
    docs = _module().build_documents()
    live = docs["quantifier_discriminator"]["live_framework_quantifier_semantics"]
    assert live == {
        "framework_semantics_sha": "2834760f4ae96684654a2080f5f36b24dc1d1ef7",
        "observed_live_main_sha": "62e97d545f93ff604b2db47a7c8d41a59a1c5286",
        "source_scope_alignment": "MISALIGNED",
        "substitution_permission": "UNKNOWN_UNTIL_MODULUS_AND_COMPARISON_ARE_PROVED",
        "required_scope_witness": "UNKNOWN",
        "faithful_pre_result_status": "FAIL_CLOSED_UNKNOWN",
        "conditional_status_forbidden_without_explicit_bridge": True,
        "authority": "ROUTING_GLUING_ONLY_NOT_THEOREM",
    }
    assert docs["framework_observation"]["application_pin_lacks_live_quantifier_compatibility_surface"] is True
    assert docs["gate"]["authority"]["mathematical_result_credit"] is False


def test_c002_reuse_is_mathematical_and_strictly_scoped() -> None:
    docs = _module().build_documents()
    tool = docs["tool_snapshot"]["tools"][0]
    assert tool["tool_id"] == "T-RH-C002-FIXED-N-NATURAL-ORDER-ABEL-IDENTITY"
    assert "fixed-n natural-order identity" in tool["applicable_effect"]
    joined = " ".join(tool["non_guarantees"])
    for term in ("M(n,epsilon)", "diagonal", "n-uniform", "all-prefix", "Li or RH"):
        assert term in joined
    notes = " ".join(docs["memory"]["tool_applicability_notes"])
    assert "inner statement obtained after fixing n" in notes
    assert "software replay" in notes


def test_required_failure_history_and_seven_math_roles_are_bound() -> None:
    docs = _module().build_documents()
    expected_failures = {
        "F-RH-ANA-003e-MOVING-PREFIX-POLYBOUND-NOT-WEAKER",
        "F-RH-ANA-003f-STRICT-CUT-SUFFIX-GLUE",
        "F-RH-ANA-003f-PATH-WITNESS-NOT-ARITHMETIC",
        "F-RH-ANA-003g-COMPLEMENT-FIRST-WEAKENING-FAIL",
        "R9-STRICT-PREFIX-ARITHMETIC-ATTAINABILITY-OBSTRUCTION",
    }
    assert set(docs["memory"]["relevant_failure_ids"]) == expected_failures
    assert {x["failure_id"] for x in docs["failure_snapshot"]["failures"]} == expected_failures
    mathematical_failure_fields = {
        "attempted_mathematical_implication",
        "exact_mathematical_failure",
        "supported_mathematical_cause",
        "competing_mathematical_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_discriminator",
        "proof_or_source_evidence",
    }
    for failure in docs["failure_snapshot"]["failures"]:
        assert mathematical_failure_fields <= set(failure)
        assert failure["competing_mathematical_causes"]
        assert failure["proof_or_source_evidence"]
        assert failure["process_assurance_mathematical_credit"] == 0
    review = docs["expert_review"]
    assert review["independent_review_credit"] == 0
    assert review["process_assurance_mathematical_credit"] == 0
    assert {x["role"] for x in review["role_reviews"]} == {
        "analytic_number_theory_domain_lead",
        "uniform_asymptotics_lead",
        "summation_gluing_lead",
        "quantifier_formal_logic_lead",
        "adversarial_falsification_lead",
        "formal_methods_dependency_lead",
        "novelty_research_value_lead",
    }
    assert "may depend arbitrarily on n" in review["strongest_objection"]


def test_current_lesson_boundary_is_mathematical_not_software_credit() -> None:
    lesson = _module().build_documents()["quantifier_discriminator"]["mathematical_lesson_boundary"]
    assert "lim_{Y->infinity}" in lesson["attempted_mathematical_implication"]
    assert "M(n,epsilon_n)<=Y_n" in lesson["exact_mathematical_state"]
    assert lesson["supported_mathematical_cause"]
    assert lesson["competing_mathematical_causes"]
    assert "Laguerre/Abel" in lesson["repair_or_next_mathematical_action"]
    assert lesson["proof_or_source_evidence"]
    assert lesson["evaluated_result"] is False
    assert lesson["process_assurance_mathematical_credit"] == 0


def test_trace_order_hash_chain_and_discriminator_chronology() -> None:
    docs = _module().build_documents()
    entries = docs["trace"]["entries"]
    assert [e["event_type"] for e in entries] == [
        x.value for x in (
            ResearchTraceEventType.ATOMIZED,
            ResearchTraceEventType.CONTEXT_FROZEN,
            ResearchTraceEventType.ANALOGY_SCAN,
            ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
            ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
            ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
            ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
            ResearchTraceEventType.NEXT_STEP_PROPOSED,
        )
    ]
    assert entries[0]["previous_event_hash"] == ""
    for prior, current in zip(entries, entries[1:]):
        assert current["previous_event_hash"] == prior["artifact_hash"]
    discriminator = docs["quantifier_discriminator"]
    assert discriminator["pre_candidate_trace_last_event_hash"] == entries[-1]["artifact_hash"]
    assert discriminator["frozen_at"] > entries[-1]["timestamp"]


def test_packet_contains_no_candidate_result_or_evaluator() -> None:
    module = _module()
    docs = module.build_documents()
    events = {entry["event_type"] for entry in docs["trace"]["entries"]}
    assert ResearchTraceEventType.CANDIDATE_PROPOSED.value not in events
    assert ResearchTraceEventType.RESULT_RECORDED.value not in events
    assert docs["atomization"]["candidate_generation_allowed"] is False
    assert docs["gate"]["chronology"]["candidate_identity"] is None
    assert docs["gate"]["chronology"]["evaluator_executed"] is False
    assert docs["quantifier_discriminator"]["evaluator_capability"] is False
    assert docs["quantifier_discriminator"]["evaluated_result"] is False
    assert not list((RH / "04_candidates").glob("*ANA_003j*"))
    assert not list((RH / "05_oracles").glob("*ANA_003j*"))
    text = FIXTURE.read_text(encoding="utf-8")
    for forbidden in ("sympy", "mpmath", "subprocess", "scipy", "candidate_result", "proof_candidate"):
        assert forbidden not in text


def test_parent_ana003i_artifacts_are_not_mutated_by_generator(tmp_path: Path) -> None:
    module = _module()
    parents = sorted(RH.glob("**/*ANA_003i*")) + [RH / "09_trace/rh_ana003i_pre_candidate_fixture.py"]
    before = {path.relative_to(ROOT).as_posix(): _sha(path) for path in parents if path.is_file()}
    module.write_documents(tmp_path)
    after = {path.relative_to(ROOT).as_posix(): _sha(path) for path in parents if path.is_file()}
    assert before == after
    generated_files = [path for path in tmp_path.rglob("*") if path.is_file()]
    assert generated_files
    assert all("ANA_003j" in str(path) or "ana003j" in str(path) for path in generated_files)
