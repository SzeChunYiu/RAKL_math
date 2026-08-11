from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError
from rakl.experience_substrate import EpisodeOutcome, TaskEpisode, validate_episode
from rakl.failure_lattice import (
    FailureDiagnosisStatus,
    FailureExperience,
    FailureExperienceLattice,
    add_failure_experience,
)
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"
BASE = "2ddb51359292fd9638116b488ffff9a04397446b"
PR_HEAD = "08fd327f0e211b2e807363c9f8c31cba50bd6497"
MERGE = "48d1153c3b5fa749b1a6fd84212befb9e39daabe"
MERGE_TREE = "dc467172b96b06a9108d45879bf7f272665fa224"
FRAMEWORK = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
HISTORICAL_EXPERIENCE_RUNTIME_BLOB = "4d7044bd4825c2d058c6a95ee63cea703c3234f3"

CORRECTION = NS / "10_case_study/NS-B1a2_C001_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"
EPISODE = NS / "10_case_study/NS-B1a2_C001_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_V2_20260811.json"
TRACE = NS / "09_trace/NS-B1a2_C001_TRACE_COMBINED_CANONICAL_20260811.json"
LATTICE = NS / "07_memory/NS-B1a2_C001_FAILURE_LATTICE_CANONICAL_20260811.json"
SCHEMA = ROOT / "schemas/ns-b1a2-postmerge-assurance-correction.schema.json"
ORIGINAL_CONTEXT = NS / "01_frontier/NS-B1a2_CONTEXT_FIBER_20260811.json"
ORIGINAL_MEMORY = NS / "07_memory/NS-B1a2_RESEARCH_MEMORY_REVIEW_20260811.json"
ORIGINAL_PRETRACE = NS / "09_trace/NS-B1a2_PRE_CANDIDATE_TRACE_20260811.json"
ORIGINAL_CONTINUATION = NS / "09_trace/NS-B1a2_C001_TRACE_CONTINUATION_20260811.json"
ORIGINAL_EPISODE = NS / "10_case_study/NS-B1a2_C001_V3_TASK_EPISODE_20260811.json"
ORIGINAL_FAILURE = NS / "07_memory/NS-B1a2_C001_FAILURE_EXPERIENCE_DELTA_20260811.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _git(*args: str, binary: bool = False) -> str | bytes:
    completed = subprocess.run(
        ["git", "-C", str(ROOT), *args], check=True, capture_output=True,
        text=not binary,
    )
    return completed.stdout if binary else completed.stdout.strip()


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _validate(value: dict, schema: Path) -> None:
    raw = _load(schema)
    Draft202012Validator.check_schema(raw)
    Draft202012Validator(raw, format_checker=FormatChecker()).validate(value)


def _framework_schema_at(commit: str, schema_name: str) -> dict:
    raw = _git(
        "-C", str(ROOT / "framework/RAKL"), "show", f"{commit}:schemas/{schema_name}"
    )
    assert isinstance(raw, str)
    value = json.loads(raw)
    assert isinstance(value, dict)
    return value


def _parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
    return parsed


def _historical_episode_content_bytes(episode: TaskEpisode) -> bytes:
    """Exact TaskEpisode identity payload used by the recorded bd1a276 runtime."""

    return json.dumps(
        {
            "episode_id": episode.episode_id,
            "task_id": episode.task_id,
            "atom_id": episode.atom_id,
            "context_hash": episode.context_hash,
            "problem_signature": list(episode.problem_signature),
            "fibre_snapshot_hash": episode.fibre_snapshot_hash,
            "operator_ids": list(episode.operator_ids),
            "action_trace": list(episode.action_trace),
            "observation_ids": list(episode.observation_ids),
            "verification_ids": list(episode.verification_ids),
            "outcome": episode.outcome.value,
            "residual_signature": list(episode.residual_signature),
            "evidence_pointers": list(episode.evidence_pointers),
            "timestamp": episode.timestamp,
            "cost": episode.cost,
        },
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _historical_validate_episode(episode: TaskEpisode) -> tuple[str, ...]:
    """Reproduce validate_episode at the immutable recorded framework commit."""

    reasons: list[str] = []
    for name in (
        "episode_id", "task_id", "atom_id", "context_hash",
        "fibre_snapshot_hash", "artifact_hash",
    ):
        if not getattr(episode, name):
            reasons.append(f"episode:{name}_missing")
    try:
        _parse_time(episode.timestamp)
    except (AssertionError, ValueError):
        reasons.append("episode:timestamp_missing_or_invalid")
    if not episode.problem_signature:
        reasons.append("episode:problem_signature_missing")
    if not episode.action_trace:
        reasons.append("episode:action_trace_missing")
    if not episode.evidence_pointers:
        reasons.append("episode:evidence_pointers_missing")
    if (
        episode.outcome
        in {EpisodeOutcome.FAILURE, EpisodeOutcome.PARTIAL_SUCCESS, EpisodeOutcome.BLOCKED}
        and not episode.residual_signature
    ):
        reasons.append("episode:residual_signature_required_for_non_success")
    if len(episode.artifact_hash) == 64 and hashlib.sha256(
        _historical_episode_content_bytes(episode)
    ).hexdigest() != episode.artifact_hash:
        reasons.append("episode:artifact_hash_mismatch")
    return tuple(reasons)


def test_pr89_original_merge_bytes_are_immutable() -> None:
    receipt = _load(CORRECTION)
    assert _git("show", "-s", "--format=%P", MERGE).split() == [BASE, PR_HEAD]
    assert _git("rev-parse", f"{MERGE}^{{tree}}") == MERGE_TREE
    paths = _git("diff", "--name-only", BASE, MERGE).splitlines()
    assert len(paths) == 13
    added_paths = set(_git("diff", "--diff-filter=A", "--name-only", BASE, MERGE).splitlines())
    assert {item["path"] for item in receipt["preserved_artifacts"]} == set(paths)
    for item in receipt["preserved_artifacts"]:
        historical = _git("show", f"{MERGE}:{item['path']}", binary=True)
        # Added evidence objects remain immutable at their live paths.  The
        # problem DAG is an intentionally evolving state file; its PR89 bytes
        # remain content-bound at MERGE without freezing all later DAG updates.
        if item["path"] in added_paths:
            assert historical == (ROOT / item["path"]).read_bytes()
        else:
            assert item["path"] == (
                "research/real_math/millennium/navier_stokes/02_problem_dag/"
                "open_obligations.yaml"
            )
        assert _git("rev-parse", f"{MERGE}:{item['path']}") == item["git_blob_sha"]
        assert "sha256:" + hashlib.sha256(historical).hexdigest() == item["content_sha256"]


def test_successors_use_exact_v3_schemas_and_runtime_shapes() -> None:
    correction = _load(CORRECTION)
    episode = _load(EPISODE)
    trace = _load(TRACE)
    lattice = _load(LATTICE)
    _validate(correction, SCHEMA)
    recorded_episode_schema = _framework_schema_at(FRAMEWORK, "task-episode.schema.json")
    recorded_trace_schema = _framework_schema_at(FRAMEWORK, "math-research-trace.schema.json")
    recorded_lattice_schema = _framework_schema_at(
        FRAMEWORK, "failure-experience-lattice.schema.json"
    )
    Draft202012Validator(recorded_episode_schema, format_checker=FormatChecker()).validate(episode)
    Draft202012Validator(recorded_trace_schema, format_checker=FormatChecker()).validate(trace)
    Draft202012Validator(recorded_lattice_schema, format_checker=FormatChecker()).validate(lattice)
    assert _git(
        "-C", str(ROOT / "framework/RAKL"), "rev-parse",
        f"{FRAMEWORK}:src/rakl/experience_substrate.py",
    ) == HISTORICAL_EXPERIENCE_RUNTIME_BLOB
    assert correction["artifact_hash"] == _canonical_hash(correction)
    assert all(item["artifact_hash"] == _canonical_hash(item) for item in lattice["experiences"])
    assert correction["framework_authority"]["current_main_commit"] == FRAMEWORK
    assert correction["correction"]["strict_discovery_credit"] == "NO_STRICT_DISCOVERY_CREDIT"
    assert correction["correction"]["repairs_original_chronology"] is False
    assert correction["prospective_gate"]["atom_id"] == "NS-B1a3"
    assert correction["prospective_gate"]["candidate_generation_allowed"] is False
    assert correction["authority_contract"] == {
        "effective_authority": "RETROSPECTIVE_ROUTE_PRUNING_ONLY",
        "grants_strict_discovery_credit": False,
        "grants_proof_authority": False,
        "grants_root_authority": False,
        "grants_theorem_authority": False,
        "grants_novelty_authority": False,
        "grants_framework_authority": False,
        "grants_review_independence": False,
        "may_backfill_chronology": False,
    }

    trace_object = MathResearchTrace(
        trace_id=trace["trace_id"],
        entries=tuple(
            ResearchTraceEntry(
                event_id=item["event_id"], atom_id=item["atom_id"],
                event_type=ResearchTraceEventType(item["event_type"]),
                timestamp=item["timestamp"], state_summary=item["state_summary"],
                action_summary=item["action_summary"],
                evidence_pointers=tuple(item["evidence_pointers"]),
                alternatives_considered=tuple(item.get("alternatives_considered", [])),
                decision_rationale=item.get("decision_rationale", ""),
                outputs=tuple(item.get("outputs", [])),
                uncertainties=tuple(item.get("uncertainties", [])),
                residuals=tuple(item.get("residuals", [])),
                next_steps=tuple(item.get("next_steps", [])),
                artifact_hash=item["artifact_hash"],
                previous_event_hash=item.get("previous_event_hash", ""),
            )
            for item in trace["entries"]
        ),
    )
    assert audit_pre_candidate_trace(
        trace_object, atom_id="NS-B1a2",
        context_packet_hash="sha256:6a7c8981dcb27f9b06b93e32901b33445d54978f236edeb51a921de5ae93f2bc",
    ).verdict is TraceGateVerdict.PASS

    episode_object = TaskEpisode(
        episode_id=episode["episode_id"], task_id=episode["task_id"],
        atom_id=episode["atom_id"], context_hash=episode["context_hash"],
        problem_signature=tuple(episode["problem_signature"]),
        fibre_snapshot_hash=episode["fibre_snapshot_hash"],
        operator_ids=tuple(episode["operator_ids"]),
        action_trace=tuple(episode["action_trace"]),
        observation_ids=tuple(episode["observation_ids"]),
        verification_ids=tuple(episode["verification_ids"]),
        outcome=EpisodeOutcome(episode["outcome"]),
        residual_signature=tuple(episode["residual_signature"]),
        evidence_pointers=tuple(episode["evidence_pointers"]),
        artifact_hash=episode["artifact_hash"], timestamp=episode["timestamp"],
        cost=episode["cost"],
    )
    assert episode["artifact_hash"] == hashlib.sha256(
        _historical_episode_content_bytes(episode_object)
    ).hexdigest()
    assert _historical_validate_episode(episode_object) == ()
    # Prospective b724b75 storage admission remains fail closed: historical
    # bytes are not silently reinterpreted as a current canonical episode.
    live_errors = list(Draft202012Validator(
        _load(ROOT / "framework/RAKL/schemas/task-episode.schema.json")
    ).iter_errors(episode))
    assert [error.message for error in live_errors] == [
        "'storage_admission' is a required property"
    ]
    assert validate_episode(episode_object) == ("episode:artifact_hash_mismatch",)

    state = FailureExperienceLattice()
    for item in lattice["experiences"]:
        state = add_failure_experience(
            state,
            FailureExperience(
                failure_id=item["failure_id"], atom_id=item["atom_id"],
                candidate_id=item["candidate_id"],
                context_packet_hash=item["context_packet_hash"],
                research_trace_event_id=item["research_trace_event_id"],
                method_family=item["method_family"], failure_mode=item["failure_mode"],
                residual_signature=tuple(item["residual_signature"]),
                broken_assumptions=tuple(item.get("broken_assumptions", [])),
                scope_conditions=tuple(item["scope_conditions"]),
                competing_diagnoses=tuple(item["competing_diagnoses"]),
                selected_diagnosis=item["selected_diagnosis"],
                diagnosis_status=FailureDiagnosisStatus(item["diagnosis_status"]),
                evidence_pointers=tuple(item["evidence_pointers"]),
                falsifier_or_attempt=item["falsifier_or_attempt"],
                observed_result=item["observed_result"],
                artifact_hash=item["artifact_hash"], timestamp=item["timestamp"],
                local_repair_attempts=tuple(item.get("local_repair_attempts", [])),
            ),
        )
    assert [item.failure_id for item in state.experiences] == [
        "F-NS-B1a2-KINETIC-ENERGY-NONQUANTIZATION"
    ]
    assert state.links == ()

    previous = ""
    for item in trace["entries"]:
        assert item["previous_event_hash"] == previous
        assert item["artifact_hash"] == _canonical_hash(item)
        previous = item["artifact_hash"]


def test_original_schema_defects_reproduce_against_exact_bd1a276() -> None:
    receipt = _load(CORRECTION)
    cases = [
        (ORIGINAL_CONTEXT, "math-context-fiber.schema.json", "context"),
        (ORIGINAL_MEMORY, "research-memory-review.schema.json", "memory_review"),
        (ORIGINAL_PRETRACE, "math-research-trace.schema.json", "pretrace"),
        (ORIGINAL_CONTINUATION, "math-research-trace.schema.json", "continuation"),
        (ORIGINAL_EPISODE, "task-episode.schema.json", "task_episode"),
        (ORIGINAL_FAILURE, "failure-experience-lattice.schema.json", "failure_lattice"),
    ]
    recorded = {item["subject"]: item for item in receipt["schema_audit"]["findings"]}
    for path, schema_name, label in cases:
        schema = _framework_schema_at(FRAMEWORK, schema_name)
        errors = sorted(
            Draft202012Validator(schema).iter_errors(_load(path)),
            key=lambda error: (list(map(str, error.absolute_path)), error.message),
        )
        subject = str(path.relative_to(ROOT))
        assert len(errors) == receipt["schema_audit"]["error_counts"][label]
        assert recorded[subject]["violations"] == [
            (("/" + "/".join(map(str, error.absolute_path))) if error.absolute_path else "/")
            + ": " + error.message
            for error in errors
        ]


def test_combined_trace_preserves_historical_event_identity_without_backfilling() -> None:
    pre = _load(ORIGINAL_PRETRACE)["events"]
    continuation = _load(ORIGINAL_CONTINUATION)["events"]
    canonical = _load(TRACE)["entries"]
    original = pre + continuation
    assert len(canonical) == len(original) == 11
    assert [item["event_id"] for item in canonical] == [item["event_id"] for item in original]
    assert [item["event_type"] for item in canonical] == [item["event_type"] for item in original]
    assert [item["timestamp"] for item in canonical] == [item["timestamp"] for item in original]
    assert all("Retrospective canonical rendering" in item["state_summary"] for item in canonical)
    assert _load(CORRECTION)["correction"]["repairs_original_chronology"] is False


def test_historical_schema_and_git_chronology_fail_closed() -> None:
    receipt = _load(CORRECTION)
    assert receipt["schema_audit"]["error_counts"] == {
        "context": 15,
        "memory_review": 5,
        "pretrace": 2,
        "continuation": 2,
        "task_episode": 1,
        "failure_lattice": 2,
    }
    assert receipt["schema_audit"]["strict_process_verdict"] == "INVALID_NO_RETROACTIVE_REPAIR"
    assert {item["subject"] for item in receipt["chronology_audit"]} == {
        "research/real_math/millennium/navier_stokes/09_trace/NS-B1a2_C001_TRACE_CONTINUATION_20260811.json::NS-B1a2-E09",
        "research/real_math/millennium/navier_stokes/09_trace/NS-B1a2_C001_TRACE_CONTINUATION_20260811.json::NS-B1a2-E10",
        "research/real_math/millennium/navier_stokes/09_trace/NS-B1a2_C001_TRACE_CONTINUATION_20260811.json::NS-B1a2-E11",
        "research/real_math/millennium/navier_stokes/07_memory/NS-B1a2_C001_FAILURE_EXPERIENCE_DELTA_20260811.json::F-NS-B1a2-KINETIC-ENERGY-NONQUANTIZATION",
        "research/real_math/millennium/navier_stokes/10_case_study/NS-B1a2_C001_V3_TASK_EPISODE_20260811.json",
    }
    for item in receipt["chronology_audit"]:
        commit_time = _parse_time(_git("show", "-s", "--format=%cI", item["introducing_commit"]))
        claimed = _parse_time(item["claimed_timestamp"])
        assert claimed > commit_time
        assert int((claimed - commit_time).total_seconds()) == item["future_offset_seconds"]


@pytest.mark.parametrize(
    ("section", "field", "value"),
    [
        ("authority_contract", "grants_strict_discovery_credit", True),
        ("authority_contract", "grants_root_authority", True),
        ("authority_contract", "grants_theorem_authority", True),
        ("authority_contract", "grants_review_independence", True),
        ("authority_contract", "may_backfill_chronology", True),
        ("prospective_gate", "candidate_generation_allowed", True),
    ],
)
def test_hostile_authority_escalation_is_rejected(
    section: str, field: str, value: object
) -> None:
    forged = copy.deepcopy(_load(CORRECTION))
    forged[section][field] = value
    schema = _load(SCHEMA)
    with pytest.raises(ValidationError):
        Draft202012Validator(schema).validate(forged)


def test_ns_b1a3_has_no_candidate_before_fresh_v3_packet() -> None:
    candidate_dir = NS / "04_candidates"
    candidates = list(candidate_dir.glob("*NS-B1a3*")) if candidate_dir.exists() else []
    assert candidates == []
