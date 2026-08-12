from __future__ import annotations

from dataclasses import replace
import importlib.util
import json
import math
from pathlib import Path
import sys

import jsonschema
import pytest
from rakl.failure_lattice import reconstruct_failure_lattice
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_research_trace,
)


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"
FALSIFIER = NS / "05_falsification/ns_b2a1a2_escaping_bump_falsifier.py"
TRACE_BUILDER = NS / "09_trace/build_ns_b2a1a2_final_trace.py"
RECEIPT = NS / "05_falsification/NS-B2a1a2_C001_ESCAPING_BUMP_RECEIPT_20260812.json"
FAILURE = NS / "07_memory/NS-B2a1a2_C001_FAILURE_EXPERIENCE_CANONICAL_20260812.json"
FINAL_TRACE = NS / "09_trace/NS-B2a1a2_FINAL_TRACE_20260812.json"


def _module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _trace(raw: dict) -> MathResearchTrace:
    return MathResearchTrace(
        trace_id=raw["trace_id"],
        entries=tuple(
            ResearchTraceEntry(
                event_id=e["event_id"], atom_id=e["atom_id"],
                event_type=ResearchTraceEventType(e["event_type"]),
                timestamp=e["timestamp"], state_summary=e["state_summary"],
                action_summary=e["action_summary"], evidence_pointers=tuple(e["evidence_pointers"]),
                alternatives_considered=tuple(e.get("alternatives_considered", [])),
                decision_rationale=e.get("decision_rationale", ""), outputs=tuple(e.get("outputs", [])),
                uncertainties=tuple(e.get("uncertainties", [])), residuals=tuple(e.get("residuals", [])),
                next_steps=tuple(e.get("next_steps", [])), artifact_hash=e["artifact_hash"],
                previous_event_hash=e.get("previous_event_hash", ""),
            ) for e in raw["entries"]
        ),
    )


def test_b2a1a2_exact_mesoscopic_and_mass_identities() -> None:
    module = _module(FALSIFIER, "ns_b2a1a2_falsifier")
    assert module.statement_hash() == module.CANDIDATE_STATEMENT_SHA256
    rows = [module.calibration_row(k, gamma=1.25) for k in range(4, 13)]
    for row in rows:
        assert module.verify_row(row) == ()
        assert math.isclose(row.h / row.L, 1 / row.k)
        assert math.isclose(row.physical_radius, math.exp(1 - row.k))
        assert math.isclose(row.F, row.k**1.25)
        assert math.isclose(row.normalized_A, row.F**-2)
        assert math.isclose(row.absolute_l2_mass, row.a / row.F**2)
    assert all(y < x for x, y in zip([r.normalized_A for r in rows], [r.normalized_A for r in rows][1:]))
    assert all(y > x for x, y in zip([r.absolute_l2_mass for r in rows], [r.absolute_l2_mass for r in rows][1:]))


def test_b2a1a2_receipt_matches_frozen_executable_falsifier() -> None:
    module = _module(FALSIFIER, "ns_b2a1a2_falsifier_receipt")
    expected = module.run_falsifier(max_k=12, gamma=1.0)
    assert _load(RECEIPT) == expected
    assert expected["verdict"] == "BARE_TRANSFER_REFUTED"
    assert expected["failures"] == []
    assert expected["checks"]["field_claimed_to_solve_navier_stokes_or_euler"] is False
    assert expected["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_b2a1a2_hostile_support_and_parameter_mutations_fail_closed() -> None:
    module = _module(FALSIFIER, "ns_b2a1a2_falsifier_hostile")
    row = module.calibration_row(6)
    assert "support_not_outside_fixed_ball" in module.verify_row(row, fixed_radius=row.center_radius)
    assert "moving_ball_misses_support" in module.verify_row(replace(row, a=row.center_radius))
    with pytest.raises(ValueError):
        module.calibration_row(1)
    with pytest.raises(ValueError):
        module.calibration_row(4, gamma=0)
    with pytest.raises(ValueError):
        module.calibration_row(4, psi_l2_squared=0)
    assert module.validate_template_and_authority(
        divergence_l2=1.0,
        support_radius=2.0,
        claimed_pde_solution=True,
        claimed_root_authority=True,
    ) == (
        "template_not_divergence_free",
        "template_support_not_in_unit_ball",
        "false_pde_solution_claim",
        "false_root_authority_claim",
    )


def test_b2a1a2_kinematic_and_polarity_boundaries_are_explicit() -> None:
    result = (NS / "04_candidates/NS-B2a1a2_C001_ESCAPING_BUMP_RESULT_20260812.md").read_text()
    review = _load(NS / "08_reviews/NS-B2a1a2_C001_SAME_CONTEXT_REVIEW_20260812.json")
    saturation = _load(NS / "10_case_study/NS-B2a1a2_C001_MATHEMATICAL_SATURATION_RECEIPT_20260812.json")
    assert "not** asserted to solve" in result
    assert "if and only if" in result
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in result
    assert review["independent_review"] is False
    assert review["authority"] == "SAME_CONTEXT_REVIEW_NOT_INDEPENDENT"
    assert saturation["mathematical_credit"] == {
        "explicit_divergence_free_translated_bump_counterexample": True,
        "sharp_uniform_intermediate_annulus_tail_condition": True,
        "software_schema_hash_chronology_ci_pr_credit": 0,
    }
    assert saturation["framework_feedback"]["status"] == "PROPOSAL_ONLY_APPLICATION_FEEDBACK"
    assert saturation["root_authority"] == "NONE"


def test_b2a1a2_failure_is_schema_valid_and_runtime_reconstructable() -> None:
    document = _load(FAILURE)
    schema = _load(ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json")
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(document)
    lattice = reconstruct_failure_lattice(document)
    assert lattice.experiences[0].failure_id == "F-NS-B2a1a2-FIXED-TO-MOVING-RADIUS-ESCAPE"
    assert lattice.experiences[0].diagnosis_status.value == "SUPPORTED"


def test_b2a1a2_final_trace_is_exact_append_and_hash_chained() -> None:
    builder = _module(TRACE_BUILDER, "ns_b2a1a2_final_trace_builder")
    expected = builder.build_trace()
    actual = _load(FINAL_TRACE)
    assert actual == expected
    trace = _trace(actual)
    assert audit_research_trace(trace).verdict is TraceGateVerdict.PASS
    assert [e.event_type for e in trace.entries[-6:]] == [
        ResearchTraceEventType.CANDIDATE_PROPOSED,
        ResearchTraceEventType.FALSIFIER_RUN,
        ResearchTraceEventType.RESULT_RECORDED,
        ResearchTraceEventType.RESIDUAL_OPENED,
        ResearchTraceEventType.REVIEWED,
        ResearchTraceEventType.PROMOTED,
    ]
    assert trace.entries[-1].residuals == ("NS0_OPEN_NO_SOLUTION_CERTIFICATE",)
