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
    FailureLink,
    FailureRelation,
    add_failure_experience,
    add_failure_link,
)
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
PR_BASE = "60bd1c0e86313a3b2228a83d0a273a36c7d5cc14"
PR_HEAD = "3ccdcc51aa312af8b8288ff7cf6f4a681966d1fd"
PR_HEAD_TREE = "0f50d7d987a82bf01ea9542336976c479604beaf"
INTEGRATION_BASE = "0fddc66a70a1f89b5aada81b63678fd66da589eb"
INTEGRATION_MERGE = "f44e7b59373cbe6885d551b12b1e29898f381133"
FRAMEWORK = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
HISTORICAL_EXPERIENCE_RUNTIME_BLOB = "4d7044bd4825c2d058c6a95ee63cea703c3234f3"
CONTEXT_HASH = "sha256:0c2a46839a95a7af6cfa2cff1a8257432ec397865e10515c84f8004719818ad7"

CORRECTION = PNP / "10_case_study/O9d12a2a1a1_PR49_SUCCESSOR_ASSURANCE_CORRECTION_20260811.json"
EPISODE = PNP / "10_case_study/O9d12a2a1a1_TASK_EPISODE_RUNTIME_HASH_SUCCESSOR_20260811.json"
TRACE = PNP / "09_trace/O9d12a2a1a1_TRACE_COMBINED_CANONICAL_20260811.json"
LATTICE = PNP / "07_memory/O9d12a2a1a1_FAILURE_LATTICE_CANONICAL_20260811.json"
SCHEMA = ROOT / "schemas/pnp-pr49-successor-assurance-correction.schema.json"

CONTEXT = PNP / "01_frontier/O9d12a2a1a1_CONTEXT_FIBER_20260811.json"
TOOLS = PNP / "07_memory/O9d12a2a1a1_RESEARCH_TOOL_INVENTORY_20260811.json"
PARENT_LATTICE = PNP / "07_memory/O9d12a2a1a1_FAILURE_EXPERIENCE_LATTICE_20260811.json"
MEMORY = PNP / "07_memory/O9d12a2a1a1_RESEARCH_MEMORY_REVIEW_20260811.json"
PRETRACE = PNP / "09_trace/O9d12a2a1a1_PRE_CANDIDATE_TRACE_20260811.json"
CONTINUATION = PNP / "09_trace/O9d12a2a1a1_INTERFACE_AUDIT_TRACE_CONTINUATION_20260811.json"
INVALID_DELTA = PNP / "07_memory/O9d12a2a1a1_INTERFACE_AUDIT_FAILURE_DELTA_20260811.json"


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


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
    return parsed


def _validate(value: dict, schema_path: Path) -> None:
    schema = _load(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(value)


def _framework_schema_at(commit: str, schema_name: str) -> dict:
    raw = _git(
        "-C", str(ROOT / "framework/RAKL"), "show", f"{commit}:schemas/{schema_name}"
    )
    assert isinstance(raw, str)
    value = json.loads(raw)
    assert isinstance(value, dict)
    return value


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


def _trace_entry(item: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
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


def _failure(item: dict) -> FailureExperience:
    return FailureExperience(
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
        observed_result=item["observed_result"], artifact_hash=item["artifact_hash"],
        timestamp=item["timestamp"],
        local_repair_attempts=tuple(item.get("local_repair_attempts", [])),
    )


def test_pr49_history_is_integrated_without_rewriting_any_of_16_added_files() -> None:
    receipt = _load(CORRECTION)
    assert _git("rev-parse", f"{PR_HEAD}^{{tree}}") == PR_HEAD_TREE
    assert _git("show", "-s", "--format=%P", INTEGRATION_MERGE).split() == [
        INTEGRATION_BASE, PR_HEAD
    ]
    paths = _git("diff", "--diff-filter=A", "--name-only", PR_BASE, PR_HEAD).splitlines()
    assert len(paths) == 16
    assert {item["path"] for item in receipt["preserved_artifacts"]} == set(paths)
    for item in receipt["preserved_artifacts"]:
        historical = _git("show", f"{PR_HEAD}:{item['path']}", binary=True)
        assert historical == (ROOT / item["path"]).read_bytes()
        assert _git("rev-parse", f"{PR_HEAD}:{item['path']}") == item["git_blob_sha"]
        assert "sha256:" + hashlib.sha256(historical).hexdigest() == item["content_sha256"]


def test_historical_schema_defects_reproduce_exactly_against_bd1a276() -> None:
    receipt = _load(CORRECTION)
    cases = [
        (CONTEXT, "math-context-fiber.schema.json", "context"),
        (TOOLS, "research-tool-inventory.schema.json", "tool_inventory"),
        (PARENT_LATTICE, "failure-experience-lattice.schema.json", "failure_lattice"),
        (MEMORY, "research-memory-review.schema.json", "memory_review"),
        (PRETRACE, "math-research-trace.schema.json", "pretrace"),
        (CONTINUATION, "math-research-trace.schema.json", "continuation"),
        (INVALID_DELTA, "failure-experience-lattice.schema.json", "failure_delta"),
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
    assert receipt["schema_audit"]["error_counts"] == {
        "context": 0, "tool_inventory": 0, "failure_lattice": 0,
        "memory_review": 0, "pretrace": 0, "continuation": 1,
        "failure_delta": 4,
    }


def test_invalid_delta_and_standalone_continuation_remain_fail_closed() -> None:
    delta = _load(INVALID_DELTA)
    assert delta["new_experience"]["candidate_id"] == ""
    with pytest.raises(ValueError):
        FailureDiagnosisStatus(delta["new_experience"]["diagnosis_status"])
    standalone = _load(CONTINUATION)
    trace = MathResearchTrace(
        trace_id=standalone["trace_id"],
        entries=tuple(_trace_entry(item) for item in standalone["entries"]),
    )
    assert audit_pre_candidate_trace(
        trace, atom_id="O9d12a2a1a1", context_packet_hash=CONTEXT_HASH
    ).verdict is TraceGateVerdict.FAIL


def test_all_18_structured_pr49_timestamps_precede_file_introduction() -> None:
    receipt = _load(CORRECTION)
    introduced = {
        item["path"]: _parse_time(item["introduced_commit_time"])
        for item in receipt["preserved_artifacts"]
    }
    timestamp_keys = {
        "timestamp", "recorded_at", "frozen_at", "first_candidate_at",
        "created_at", "updated_at",
    }
    checked: list[tuple[str, str, str]] = []

    def walk(value: object, *, relative: str, pointer: str = "") -> None:
        if isinstance(value, dict):
            for key, item in value.items():
                child = f"{pointer}/{key}"
                if key in timestamp_keys and item is not None:
                    assert isinstance(item, str)
                    checked.append((relative, child, item))
                walk(item, relative=relative, pointer=child)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                walk(item, relative=relative, pointer=f"{pointer}/{index}")

    for path in (CONTEXT, TOOLS, PARENT_LATTICE, MEMORY, PRETRACE, CONTINUATION, INVALID_DELTA):
        relative = str(path.relative_to(ROOT))
        walk(_load(path), relative=relative)
    assert len(checked) == 18
    future = [
        (relative, pointer, timestamp)
        for relative, pointer, timestamp in checked
        if _parse_time(timestamp) > introduced[relative]
    ]
    assert future == []
    assert receipt["chronology_audit"] == {
        "checked_json_artifact_count": 7,
        "checked_timestamp_count": 18,
        "future_dated_claim_count": 0,
        "future_dated_claims": [],
        "verdict": "NO_FUTURE_DATED_STRUCTURED_PR49_CLAIMS_DETECTED",
    }


def test_canonical_combined_trace_is_exact_schema_valid_hash_chained_runtime() -> None:
    pre = _load(PRETRACE)
    continuation = _load(CONTINUATION)
    canonical = _load(TRACE)
    Draft202012Validator(
        _framework_schema_at(FRAMEWORK, "math-research-trace.schema.json"),
        format_checker=FormatChecker(),
    ).validate(canonical)
    assert canonical["entries"] == pre["entries"] + continuation["entries"]
    previous = ""
    entries = []
    for item in canonical["entries"]:
        assert item["previous_event_hash"] == previous
        assert item["artifact_hash"] == _canonical_hash(item)
        previous = item["artifact_hash"]
        entries.append(_trace_entry(item))
    trace = MathResearchTrace(trace_id=canonical["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(
        trace, atom_id="O9d12a2a1a1", context_packet_hash=CONTEXT_HASH
    ).verdict is TraceGateVerdict.PASS
    assert entries[-1].event_type is ResearchTraceEventType.RESIDUAL_OPENED


def test_canonical_failure_lattice_repairs_runtime_without_inventing_candidate() -> None:
    raw = _load(LATTICE)
    Draft202012Validator(
        _framework_schema_at(FRAMEWORK, "failure-experience-lattice.schema.json"),
        format_checker=FormatChecker(),
    ).validate(raw)
    parent = _load(PARENT_LATTICE)
    assert raw["experiences"][:-1] == parent["experiences"]
    new = raw["experiences"][-1]
    assert new["failure_id"] == "F-O9D12A2A1A1-PARTITION-CLOSURE-COLLAPSE"
    assert new["candidate_id"] == "NO_CANDIDATE_ROUTE_AUDIT"
    assert new["diagnosis_status"] == "SUPPORTED"
    assert new["research_trace_event_id"] == "O9d12a2a1a1-E09"
    state = FailureExperienceLattice()
    for item in raw["experiences"]:
        assert item["artifact_hash"] == _canonical_hash(item)
        state = add_failure_experience(state, _failure(item))
    for item in raw["links"]:
        state = add_failure_link(
            state,
            FailureLink(
                source_id=item["source_id"], target_id=item["target_id"],
                relation=FailureRelation(item["relation"]),
                rationale=item["rationale"],
                evidence_pointers=tuple(item.get("evidence_pointers", [])),
            ),
        )
    assert any(
        link.source_id == "F-O9D12A2A1A1-PARTITION-CLOSURE-COLLAPSE"
        and link.target_id == "F-C025-FIRST-ORDER-CANONICAL-COLLAPSE"
        and link.relation is FailureRelation.CONTEXT_SPECIALIZATION_OF
        for link in state.links
    )
    assert all(link.relation.value != "PRECEDES_CONTROL" for link in state.links)


def test_retrospective_episode_and_correction_narrow_authority_and_close_child() -> None:
    correction = _load(CORRECTION)
    episode = _load(EPISODE)
    _validate(correction, SCHEMA)
    recorded_episode_schema = _framework_schema_at(FRAMEWORK, "task-episode.schema.json")
    Draft202012Validator(
        recorded_episode_schema, format_checker=FormatChecker()
    ).validate(episode)
    assert _git(
        "-C", str(ROOT / "framework/RAKL"), "rev-parse",
        f"{FRAMEWORK}:src/rakl/experience_substrate.py",
    ) == HISTORICAL_EXPERIENCE_RUNTIME_BLOB
    assert correction["artifact_hash"] == _canonical_hash(correction)
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
    assert correction["correction"]["strict_discovery_credit"] == "NO_STRICT_DISCOVERY_CREDIT"
    assert correction["correction"]["repairs_original_chronology"] is False
    assert correction["prospective_gate"]["atom_id"] == "O9d12a2a1a1a"
    assert correction["prospective_gate"]["candidate_generation_allowed"] is False
    assert correction["authority_contract"] == {
        "effective_authority": "RETROSPECTIVE_SCOPED_ROUTE_PRUNING_ONLY",
        "grants_strict_discovery_credit": False,
        "grants_proof_authority": False,
        "grants_p_vs_np_root_authority": False,
        "grants_theorem_authority": False,
        "grants_novelty_authority": False,
        "grants_framework_authority": False,
        "grants_review_independence": False,
        "may_backfill_chronology": False,
    }
    assert correction["chronology_audit"]["future_dated_claim_count"] == 0
    candidate_dir = PNP / "04_candidates"
    candidates = list(candidate_dir.glob("*O9d12a2a1a1a*")) if candidate_dir.exists() else []
    assert candidates == []


@pytest.mark.parametrize(
    ("section", "field", "value"),
    [
        ("authority_contract", "grants_strict_discovery_credit", True),
        ("authority_contract", "grants_p_vs_np_root_authority", True),
        ("authority_contract", "grants_theorem_authority", True),
        ("authority_contract", "grants_review_independence", True),
        ("authority_contract", "may_backfill_chronology", True),
        ("prospective_gate", "candidate_generation_allowed", True),
    ],
)
def test_hostile_authority_escalation_is_schema_rejected(
    section: str, field: str, value: object
) -> None:
    forged = copy.deepcopy(_load(CORRECTION))
    forged[section][field] = value
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(SCHEMA)).validate(forged)


def test_successor_hash_bindings_are_exact() -> None:
    correction = _load(CORRECTION)
    for item in correction["successors"]:
        path = ROOT / item["path"]
        if item["hash_mode"] == "EMBEDDED_SELF_HASH":
            assert item["artifact_hash"] == _load(path)["artifact_hash"]
        else:
            assert item["hash_mode"] == "FILE_SHA256"
            assert item["artifact_hash"] == _file_hash(path)
