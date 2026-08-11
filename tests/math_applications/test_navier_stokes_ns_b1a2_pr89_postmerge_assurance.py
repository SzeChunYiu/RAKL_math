from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker
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

CORRECTION = NS / "10_case_study/NS-B1a2_C001_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"
EPISODE = NS / "10_case_study/NS-B1a2_C001_TASK_EPISODE_CANONICAL_20260811.json"
TRACE = NS / "09_trace/NS-B1a2_C001_TRACE_COMBINED_CANONICAL_20260811.json"
LATTICE = NS / "07_memory/NS-B1a2_C001_FAILURE_LATTICE_CANONICAL_20260811.json"
SCHEMA = ROOT / "schemas/ns-b1a2-postmerge-assurance-correction.schema.json"


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


def test_pr89_original_merge_bytes_are_immutable() -> None:
    receipt = _load(CORRECTION)
    assert _git("show", "-s", "--format=%P", MERGE).split() == [BASE, PR_HEAD]
    assert _git("rev-parse", f"{MERGE}^{{tree}}") == MERGE_TREE
    paths = _git("diff", "--name-only", BASE, MERGE).splitlines()
    assert len(paths) == 13
    assert {item["path"] for item in receipt["preserved_artifacts"]} == set(paths)
    for item in receipt["preserved_artifacts"]:
        historical = _git("show", f"{MERGE}:{item['path']}", binary=True)
        assert historical == (ROOT / item["path"]).read_bytes()
        assert _git("rev-parse", f"{MERGE}:{item['path']}") == item["git_blob_sha"]
        assert "sha256:" + hashlib.sha256(historical).hexdigest() == item["content_sha256"]


def test_successors_use_exact_v3_schemas_and_runtime_shapes() -> None:
    correction = _load(CORRECTION)
    episode = _load(EPISODE)
    trace = _load(TRACE)
    lattice = _load(LATTICE)
    _validate(correction, SCHEMA)
    _validate(episode, ROOT / "framework/RAKL/schemas/task-episode.schema.json")
    _validate(trace, ROOT / "framework/RAKL/schemas/math-research-trace.schema.json")
    _validate(lattice, ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json")
    assert correction["artifact_hash"] == _canonical_hash(correction)
    assert episode["artifact_hash"] == _canonical_hash(episode)
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
    assert validate_episode(episode_object) == ()

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
    assert all(item["future_offset_seconds"] > 0 for item in receipt["chronology_audit"])
