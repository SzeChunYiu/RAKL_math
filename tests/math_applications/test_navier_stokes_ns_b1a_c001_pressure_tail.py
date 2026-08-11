from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import jsonschema

from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
    audit_research_trace,
)


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"
CONTEXT_HASH = "sha256:d0acf9ae066132883a893e669c09f5969f5e40281c558913b61c8ac0fcc2902d"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _entry(raw: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
        event_id=raw["event_id"],
        atom_id=raw["atom_id"],
        event_type=ResearchTraceEventType(raw["event_type"]),
        timestamp=raw["timestamp"],
        state_summary=raw["state_summary"],
        action_summary=raw["action_summary"],
        evidence_pointers=tuple(raw["evidence_pointers"]),
        alternatives_considered=tuple(raw.get("alternatives_considered", ())),
        decision_rationale=raw.get("decision_rationale", ""),
        outputs=tuple(raw.get("outputs", ())),
        uncertainties=tuple(raw.get("uncertainties", ())),
        residuals=tuple(raw.get("residuals", ())),
        next_steps=tuple(raw.get("next_steps", ())),
        artifact_hash=raw["artifact_hash"],
        previous_event_hash=raw.get("previous_event_hash", ""),
    )


def test_pressure_tail_dyadic_constants_are_exact() -> None:
    pressure_shell_ratio = Fraction(1, 4)
    gradient_shell_ratio = Fraction(1, 8)

    pressure_geometric_sum = Fraction(1, 1) / (1 - pressure_shell_ratio)
    gradient_geometric_sum = Fraction(1, 1) / (1 - gradient_shell_ratio)

    assert pressure_geometric_sum == Fraction(4, 3)
    assert gradient_geometric_sum == Fraction(8, 7)
    assert 2 * pressure_geometric_sum == Fraction(8, 3)
    assert 2 * gradient_geometric_sum == Fraction(16, 7)


def test_candidate_document_is_fail_closed_in_scope() -> None:
    text = (BASE / "01_frontier/NS-B1a_C001_PRESSURE_TAIL_LOCALIZATION_20260811.md").read_text(
        encoding="utf-8"
    )
    assert "raw pressure-divergence anti-replication mechanism" in text
    assert "does **not** construct a Navier–Stokes sparse-tail solution" in text
    assert "I<∞ -> L^3" in text
    assert "Type-II" in text
    assert "NO_NOVELTY_CLAIM" in text
    assert "NS-B1a1" in text


def test_failure_delta_is_hash_bound_and_schema_valid() -> None:
    delta = _load("07_memory/NS-B1a_C001_FAILURE_EXPERIENCE_DELTA_20260811.json")
    experience = delta["experience"]
    payload = copy.deepcopy(experience)
    artifact_hash = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert artifact_hash == _canonical_hash(payload)
    assert experience["diagnosis_status"] == "SUPPORTED"
    assert experience["research_trace_event_id"] == "NS-B1a-E10"
    assert experience["context_packet_hash"] == CONTEXT_HASH
    assert "instantaneous" in experience["selected_diagnosis"]
    assert any(link["relation"] == "MOTIVATES_META_ATOM" for link in delta["links"])

    schema = json.loads(
        (ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate({"experiences": [experience], "links": delta["links"]})


def test_trace_continuation_is_hash_chained_to_strict_pre_candidate_packet() -> None:
    base = _load("09_trace/NS-B1a_PRE_CANDIDATE_TRACE_20260811.json")
    continuation = _load("09_trace/NS-B1a_C001_TRACE_CONTINUATION_20260811.json")

    assert continuation["trace_id"] == base["trace_id"]
    assert continuation["entries"][0]["previous_event_hash"] == base["entries"][-1]["artifact_hash"]
    assert [entry["event_type"] for entry in continuation["entries"]] == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]

    previous = base["entries"][-1]["artifact_hash"]
    for raw in continuation["entries"]:
        assert raw["previous_event_hash"] == previous
        payload = copy.deepcopy(raw)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        previous = artifact_hash

    combined = MathResearchTrace(
        trace_id=base["trace_id"],
        entries=tuple(_entry(raw) for raw in base["entries"] + continuation["entries"]),
    )
    assert audit_research_trace(combined).verdict is TraceGateVerdict.PASS
    assert (
        audit_pre_candidate_trace(
            combined,
            atom_id="NS-B1a",
            context_packet_hash=CONTEXT_HASH,
        ).verdict
        is TraceGateVerdict.PASS
    )


def test_result_review_preserves_live_pressure_and_type_ii_routes() -> None:
    review = (BASE / "08_reviews/SAME_CONTEXT_REVIEW_NS-B1a_C001_RESULT_20260811.md").read_text(
        encoding="utf-8"
    )
    assert "Pressure is irrelevant" in review
    assert "Rejected" in review
    assert "temporal pressure-aware shell flux" in review
    assert "NO_NOVELTY_AUTHORITY" in review
