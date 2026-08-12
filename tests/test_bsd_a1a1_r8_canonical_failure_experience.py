from __future__ import annotations

import hashlib
import json
from pathlib import Path

import jsonschema
from rakl.failure_lattice import (
    FailureDiagnosisStatus,
    reconstruct_failure_lattice,
)
from rakl.schema_reference_constraints import check_reference_constraints


ROOT = Path(__file__).resolve().parents[1]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"
MEMORY = BSD / "07_memory"
FAILURE = MEMORY / "BSD_A1a1_R8_CANONICAL_FAILURE_EXPERIENCE_DELTA_20260812.json"
EPISODE = MEMORY / "BSD_A1a1_R8_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
COVERAGE = MEMORY / "BSD_A1a1_R8_CROSS_PROBLEM_COVERAGE_RECEIPT_20260812.json"
LIFT_REVIEW = MEMORY / "BSD_A1a1_R8_POSTDRIFT_OBSTRUCTION_TRANSFORMATION_LIFT_REVIEW_20260812.json"
TRACE = BSD / "09_trace/BSD_A1a1_R8_RESULT_TRACE_DELTA_20260812.json"
SCHEMA = ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def experience_hash(experience: dict) -> str:
    payload = dict(experience)
    payload["artifact_hash"] = ""
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def test_r8_canonical_failure_delta_is_schema_and_runtime_valid() -> None:
    document = load(FAILURE)
    schema = load(SCHEMA)
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(document)
    assert check_reference_constraints(document, schema) == ()

    lattice = reconstruct_failure_lattice(document)
    assert len(lattice.experiences) == 1
    assert lattice.links == ()
    experience = lattice.experiences[0]
    assert experience.failure_id == (
        "F-BSD-A1A1-R8-SOURCE-FAMILY-REIMPORTS-ARITHMETIC-ENTRY"
    )
    assert experience.atom_id == "BSD-A1a1-THETA-ORDER-COMPARISON"
    assert experience.diagnosis_status is FailureDiagnosisStatus.SUPPORTED
    assert "NO_SUPPORTED_CAUSAL_DIAGNOSIS" in experience.selected_diagnosis


def test_r8_canonical_failure_is_content_hashed_and_bound_to_exact_context_trace() -> None:
    document = load(FAILURE)
    experience = document["experiences"][0]
    episode = load(EPISODE)
    trace = load(TRACE)

    assert experience["artifact_hash"] == experience_hash(experience)
    assert experience["context_packet_hash"] == episode["fibre_snapshot_hash"]
    matching_events = [
        entry
        for entry in trace["entries"]
        if entry["event_id"] == experience["research_trace_event_id"]
    ]
    assert len(matching_events) == 1
    assert (
        experience["failure_id"]
        in matching_events[0]["outputs"]
    )


def test_r8_canonical_failure_preserves_bounded_math_diagnosis() -> None:
    experience = load(FAILURE)["experiences"][0]
    source = load(
        BSD / "00_sources/BSD_A1a1_R8_SOURCE_FAMILY_AUDIT_20260812.json"
    )
    diagnosis = load(MEMORY / "BSD_A1a1_R8_DIAGNOSIS_SHADOW_20260812.json")
    shadow = load(MEMORY / "BSD_A1a1_R8_SOURCE_FAMILY_FAILURE_SHADOW_20260812.json")
    assert source["active_atom"] == experience["atom_id"]
    assert source["coverage_claim"] == "BOUNDED_ONLY_NOT_COMPLETE"
    assert {item["id"] for item in source["sources"]} == {
        "arXiv:2312.09301",
        "arXiv:2203.12161",
        "arXiv:2409.11966",
        "arXiv:1809.09066",
    }
    assert diagnosis["diagnosis_id"] == (
        "D-BSD-A1A1-R8-SOURCE-FAMILIES-REENTER-A1A2"
    )
    assert shadow["failure_id"] == experience["failure_id"]
    assert len(experience["competing_diagnoses"]) >= 5
    assert any(
        "bounded source audit" in item and "missing theorem" in item
        for item in experience["competing_diagnoses"]
    )
    assert any(
        "genuine" in item and "obstruction" in item
        for item in experience["competing_diagnoses"]
    )
    assert len(experience["broken_assumptions"]) >= 6
    assert any("same E/Q" in item for item in experience["scope_conditions"])
    assert any(
        "not a literature-wide" in item for item in experience["scope_conditions"]
    )
    assert "strictly weaker" in experience["falsifier_or_attempt"]
    assert "same E/Q" in experience["falsifier_or_attempt"]


def test_r8_canonical_failure_evidence_paths_exist_and_relations_are_narrative_only() -> None:
    document = load(FAILURE)
    experience = document["experiences"][0]
    assert document["links"] == []
    for pointer in experience["evidence_pointers"]:
        assert pointer.startswith("research/real_math/millennium/")
        assert (ROOT / pointer).is_file(), pointer

    prior_ids = (
        "F-BSD-A1A1-R5-AUXILIARY-K-EXACT-SCOPE-GAP",
        "F-BSD-A1A1-R6-AUXILIARY-K-CANNOT-SUPPLY-INTRINSIC-ENTRY",
        "F-BSD-A1A1-R7-ANALYTIC-TO-TRANSVERSE-LOCALIZATION",
    )
    combined_text = " ".join(
        experience["competing_diagnoses"]
        + experience["local_repair_attempts"]
        + experience["evidence_pointers"]
    )
    assert all(item in combined_text for item in prior_ids)


def test_r8_stale_coverage_residual_is_superseded_without_math_credit() -> None:
    experience = load(FAILURE)["experiences"][0]
    coverage = load(COVERAGE)
    lift_review = load(LIFT_REVIEW)

    assert "SEMANTIC_SHORTCUT_CROSS_PROBLEM_COVERAGE_UNAVAILABLE_FOR_LIFT" not in (
        experience["residual_signature"]
    )
    assert coverage["coverage_id"] == (
        "CPCR-BSD-A1A1-R8-CURRENT-MAIN-TYPED-MEMORY-20260812"
    )
    assert lift_review["selected_mode"] == "LIFT"
    assert lift_review["missing_transformation_specification"]["spec_id"] == (
        "MTS-BSD-A1A2-R8-COMPLEX-TO-ARITHMETIC-ENTRY-20260812"
    )
    repairs = " ".join(experience["local_repair_attempts"])
    scope = " ".join(experience["scope_conditions"])
    assert "ASSURANCE_ONLY_SUPERSESSION" in repairs
    assert "MISSING_TRANSFORMATION_SPEC_FROZEN_NO_MATHEMATICAL_CANDIDATE" in repairs
    assert "Git/CI/schema/hash/chronology" in scope
    assert "zero mathematical saturation, result, and root credit" in scope


def test_r8_retained_lesson_is_math_only_and_bounded() -> None:
    experience = load(FAILURE)["experiences"][0]
    lessons = [
        item.removeprefix("MATH_ONLY_LESSON: ")
        for item in experience["local_repair_attempts"]
        if item.startswith("MATH_ONLY_LESSON: ")
    ]
    assert lessons == [
        "A change of arithmetic carrier does not close the complex-rank-to-arithmetic bridge when it merely relocates the required nonvanishing or localization into a hypothesis. Credit a route only when a same-curve theorem derives a root-faithful arithmetic witness from exact complex analytic rank two under hypotheses strictly weaker than that witness; keep subsequent BSD leading-term gluing as a separate obligation."
    ]
    assert not any(
        word in lessons[0].lower()
        for word in ("git", "ci", "schema", "hash", "software", "framework")
    )
