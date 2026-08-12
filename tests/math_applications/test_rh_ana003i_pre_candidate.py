from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.framework_candidate_freeze import CandidateFreezeRevalidationVerdict
from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import (
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)
from rakl.root_coordinate_preservation import PreservationGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003i_pre_candidate_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("rh_ana003i_pre", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_current_gate_is_fail_closed_before_any_candidate() -> None:
    module = _module()
    plan, fiber, memory, tm, shortcut, trace, _ = module.build_current_gate_plan()
    assert module.APPLICATION_BASE_SHA == "c5ebefad369a737f458ea1528cb6bfa9989b7265"
    assert module.FRAMEWORK_CURRENT_SHA == "e58b3b338c896487c37dfe2069c022e73cf9a974"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.CANNOT_CHECK
    assert plan.trace_gate.verdict is TraceGateVerdict.CANNOT_CHECK
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.framework_subject_gate.verdict is CandidateFreezeRevalidationVerdict.CURRENT_UNCHANGED
    assert plan.candidate_generation_allowed is False
    assert shortcut.selected_mode is ShortcutMode.CANNOT_CHECK
    assert shortcut.exhaustion_witness is None
    assert shortcut.missing_transformation_specification is None
    assert fiber.first_candidate_at is None
    assert tm.snapshot_hash == shortcut.episode_memory_snapshot_hash
    direct_trace = audit_pre_candidate_trace(
        trace,
        atom_id=module.ATOM,
        context_packet_hash=fiber.packet_hash,
        obstruction_transformation_review_hash=shortcut.artifact_hash,
    )
    assert direct_trace.verdict is TraceGateVerdict.PASS


def test_documents_match_fixture_and_current_schemas() -> None:
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


def test_object_qoi_scale_and_first_discriminator_are_exact() -> None:
    module = _module()
    docs = module.build_documents()
    atom = docs["atomization"]
    context = docs["context"]
    assert "x_{n,m}" in atom["object"]
    assert "Y_n=exp(C n^(5/3) log^2(n+e))" in atom["object"]
    assert "source-bound non-extremal internal-family class" in atom["qoi"]
    assert len(atom["first_discriminator"]) == 6
    joined = " ".join(atom["first_discriminator"])
    for required in (
        "R_n(Y_n)",
        "S_n",
        "D_n(Y_n)",
        "endpoint/running-extremum",
        "ambient signed-path",
        "reordering or regrouping",
        "strictly weaker",
        "mollifier/resonance",
    ):
        assert required in joined
    assert "natural integer order" in " ".join(context["structural_coordinates"])


def test_source_authority_separates_primary_current_and_shadow_evidence() -> None:
    module = _module()
    source = module.build_documents()["source_packet"]
    ids = {item["id"] for item in source["primary_sources"]}
    assert {
        "COFFEY-0706.0343v2",
        "LI-1997",
        "BOMBIERI-LAGARIAS-1999",
        "VOROS-math0506326v2",
        "BELLOTTI-2508.02041v1",
        "DUNSTER-GIL-SEGURA-1705.01190v1",
        "CONREY-ETAL-2508.11108",
    } <= ids
    assert {item["id"] for item in source["shadow_evidence"]} == {"PR316-R9", "PR320-R8"}
    assert all("proposal-only" in item["scope"] for item in source["shadow_evidence"])
    conrey = next(item for item in source["primary_sources"] if item["id"] == "CONREY-ETAL-2508.11108")
    assert conrey["access_status"] == "DEFERRED_ALTERNATE_ROUTE_NOT_VERIFIED_THIS_ROUND"


def test_all_required_negative_history_is_bound() -> None:
    module = _module()
    docs = module.build_documents()
    expected = {
        "F-RH-ANA-003g-COMPLEMENT-FIRST-WEAKENING-FAIL",
        "F-RH-ANA-003g-AMBIENT-WITNESS-CURRENT-V3-REPRESENTATION-ONLY",
        "F-RH-ANA-003f-STRICT-CUT-SUFFIX-GLUE",
        "F-RH-ANA-003f-PATH-WITNESS-NOT-ARITHMETIC",
        "F-RH-ANA-003e-MOVING-PREFIX-POLYBOUND-NOT-WEAKER",
        "F-RH-ANA-003c-UNWITNESSED-WINDOW-GLUE",
        "R9-STRICT-PREFIX-ARITHMETIC-ATTAINABILITY-OBSTRUCTION",
    }
    assert set(docs["memory"]["relevant_failure_ids"]) == expected
    assert {item["failure_id"] for item in docs["failure_snapshot"]["failures"]} == expected


def test_seven_roles_and_complete_trace_have_zero_independent_credit() -> None:
    module = _module()
    docs = module.build_documents()
    review = docs["expert_review"]
    assert len(review["role_reviews"]) == 7
    assert review["independent_review_credit"] == 0
    assert {item["role"] for item in review["role_reviews"]} == {
        "analytic_number_theory_domain_lead",
        "laguerre_uniform_asymptotics_lead",
        "summation_gluing_lead",
        "target_domain_transfer_applicability_lead",
        "adversarial_falsification_lead",
        "formal_methods_dependency_lead",
        "novelty_research_value_lead",
    }
    assert [entry["event_type"] for entry in docs["trace"]["entries"]] == [
        item.value
        for item in (
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


def test_packet_contains_no_candidate_or_result_event() -> None:
    module = _module()
    docs = module.build_documents()
    events = {entry["event_type"] for entry in docs["trace"]["entries"]}
    assert ResearchTraceEventType.CANDIDATE_PROPOSED.value not in events
    assert ResearchTraceEventType.RESULT_RECORDED.value not in events
    assert docs["atomization"]["candidate_generation_allowed"] is False
    assert docs["atomization"]["candidate_proposed"] is False
    assert docs["gate"]["chronology"]["candidate_identity"] is None
    assert docs["gate"]["gate_verdicts"]["candidate_generation_allowed"] is False
    assert docs["gate"]["gate_verdicts"]["lift_authorized"] is False
    assert docs["gate"]["authority"]["mathematical_result_credit"] is False
    packet_text = "\n".join(
        json.dumps(document, sort_keys=True, ensure_ascii=False)
        for document in docs.values()
    )
    assert "CANDIDATE_PROPOSED" not in packet_text
    assert "RESULT_RECORDED" not in packet_text
    assert "H" + "_n" not in packet_text


def test_fixture_has_no_evaluator_or_candidate_capability() -> None:
    text = FIXTURE.read_text(encoding="utf-8")
    for forbidden in (
        "sympy",
        "mpmath",
        "subprocess",
        "scipy",
        "candidate_result",
        "proof_candidate",
    ):
        assert forbidden not in text

