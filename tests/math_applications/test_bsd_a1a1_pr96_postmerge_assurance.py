from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"
FRAMEWORK = ROOT / "framework/RAKL"
BASE = "6557b1b25fa839fe71aba8047c958d5da892edd8"
PR_HEAD = "43729e13a5df5628e1e3dd07ba7500289a88e476"
MERGE = "9bb808752a4cf456f537c2e1d81253ef2883c109"
FRAMEWORK_COMMIT = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"

SOURCE_SNAPSHOT = BSD / "00_sources/BSD_A1a1_PLECTIC_ARXIV_SOURCE_SNAPSHOT_20260811.xml"
SOURCE_RECEIPT = BSD / "00_sources/BSD_A1a1_PLECTIC_SOURCE_RECEIPT_V1_20260811.json"
EPISODE = BSD / "07_memory/BSD_A1a1_PLECTIC_TASK_EPISODE_CANONICAL_RETROSPECTIVE_20260811.json"
FAILURES = BSD / "07_memory/BSD_A1a1_PLECTIC_FAILURE_EXPERIENCE_LATTICE_RETROSPECTIVE_20260811.json"
TRACE = BSD / "09_trace/BSD_A1a1_PLECTIC_RESEARCH_TRACE_RETROSPECTIVE_SUCCESSOR_20260811.json"
PRETRACE = BSD / "09_trace/BSD_A1a1_PRE_CANDIDATE_TRACE_20260811.json"
CORRECTION = BSD / "08_reviews/BSD_A1a1_PR96_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"
ORIGINAL_EPISODE = BSD / "07_memory/BSD_A1a1_PLECTIC_TASK_EPISODE_SHADOW_20260811_R3.json"
ORIGINAL_FAILURE = BSD / "07_memory/BSD_A1a1_PLECTIC_FAILURE_SHADOW_20260811_R3.json"
ORIGINAL_TRACE_DELTA = BSD / "09_trace/BSD_A1a1_PLECTIC_RESEARCH_TRACE_DELTA_20260811_R3.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _git(*arguments: str, binary: bool = False) -> str | bytes:
    run = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        text=not binary,
    )
    return run.stdout if binary else run.stdout.strip()


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _validator(schema_path: Path) -> jsonschema.Draft202012Validator:
    schema = _load(schema_path)
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )


def _parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
    return parsed


def _framework_import_path() -> None:
    source = str(FRAMEWORK / "src")
    if source not in sys.path:
        sys.path.insert(0, source)


def test_pr96_git_provenance_and_all_original_bytes_are_immutable() -> None:
    correction = _load(CORRECTION)
    assert correction["application_repository"] == {
        "url": "https://github.com/SzeChunYiu/RAKL_math.git",
        "pre_pr_base_commit": BASE,
        "pr_head_commit": PR_HEAD,
        "merge_commit": MERGE,
        "merge_parents": [BASE, PR_HEAD],
    }
    assert _git("show", "-s", "--format=%P", MERGE).split() == [BASE, PR_HEAD]
    changed = set(_git("diff", "--name-only", BASE, PR_HEAD).splitlines())
    bindings = correction["preserved_pr96_artifacts"]
    assert len(bindings) == 8
    assert {item["path"] for item in bindings} == changed
    for item in bindings:
        raw = _git("show", f'{MERGE}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert (ROOT / item["path"]).read_bytes() == raw
        assert item["git_blob_sha"] == _git("rev-parse", f'{MERGE}:{item["path"]}')
        assert item["content_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()


def test_exact_bd1_framework_schema_and_runtime_bindings_are_loaded() -> None:
    correction = _load(CORRECTION)
    authority = correction["framework_authority"]
    assert authority["commit"] == FRAMEWORK_COMMIT
    assert authority["application_gitlink"] == FRAMEWORK_COMMIT
    assert _git("rev-parse", "HEAD:framework/RAKL") == FRAMEWORK_COMMIT
    assert _git("-C", str(FRAMEWORK), "rev-parse", "HEAD") == FRAMEWORK_COMMIT
    for item in authority["schema_bindings"] + authority["runtime_bindings"]:
        assert item["git_blob_sha"] == _git(
            "-C", str(FRAMEWORK), "rev-parse", f'HEAD:{item["path"]}'
        )


def test_exact_versioned_plectic_sources_are_content_bound() -> None:
    receipt = _load(SOURCE_RECEIPT)
    _validator(ROOT / "schemas/bsd-a1a1-pr96-plectic-source-receipt.schema.json").validate(receipt)
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    raw = SOURCE_SNAPSHOT.read_bytes()
    assert receipt["retrieval"]["snapshot_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
    assert receipt["retrieval"]["snapshot_size_bytes"] == len(raw)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    xml = ET.fromstring(raw)
    versioned = {
        entry.findtext("a:id", namespaces=ns).rsplit("/", 1)[-1]
        for entry in xml.findall("a:entry", ns)
    }
    assert versioned == {"2603.28327v2", "2311.03100v2", "2202.12573v2"}
    assert {item["versioned_id"] for item in receipt["sources"]} == versioned
    assert all(item["pdf_sha256"].startswith("sha256:") for item in receipt["sources"])
    assert all(item["pdf_size_bytes"] > 0 for item in receipt["sources"])
    assert all(item["claim_check"]["status"] == "SUPPORTED_AT_RECORDED_SCOPE" for item in receipt["sources"])


def test_original_pr96_schema_hash_and_git_chronology_defects_are_preserved() -> None:
    correction = _load(CORRECTION)
    recorded = {item["subject"]: item for item in correction["schema_runtime_audit"]["findings"]}
    cases = [
        (ORIGINAL_EPISODE, "task-episode.schema.json"),
        (ORIGINAL_FAILURE, "failure-experience-lattice.schema.json"),
        (ORIGINAL_TRACE_DELTA, "math-research-trace.schema.json"),
    ]
    for path, schema_name in cases:
        errors = sorted(
            _validator(FRAMEWORK / "schemas" / schema_name).iter_errors(_load(path)),
            key=lambda error: (list(map(str, error.absolute_path)), error.message),
        )
        subject = str(path.relative_to(ROOT))
        assert recorded[subject]["error_count"] == len(errors) > 0
        assert recorded[subject]["schema_path"] == "schemas/" + schema_name

    original_delta = _load(ORIGINAL_TRACE_DELTA)
    mismatch = correction["schema_runtime_audit"]["original_trace_hash_mismatches"]
    assert [item["event_id"] for item in mismatch] == ["BSD-A1a1-E08", "BSD-A1a1-E09"]
    for recorded_hash, event in zip(mismatch, original_delta["entries"], strict=True):
        assert recorded_hash["claimed"] == event["artifact_hash"]
        assert recorded_hash["blank_field_canonical"] == _canonical_hash(event)
        assert recorded_hash["claimed"] != recorded_hash["blank_field_canonical"]

    for item in correction["chronology_audit"]:
        assert _parse_time(item["bound_commit_time"]) > _parse_time(item["claimed_timestamp"])
        assert item["bound_commit_time"] == _git("show", "-s", "--format=%cI", item["bound_commit"])


def test_canonical_retrospective_episode_passes_schema_runtime_and_hash_checks() -> None:
    episode = _load(EPISODE)
    _validator(FRAMEWORK / "schemas/task-episode.schema.json").validate(episode)
    assert episode["artifact_hash"] == _canonical_hash(episode)
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert "NO_STRICT_DISCOVERY_CREDIT" in episode["action_trace"]
    _framework_import_path()
    from rakl.experience_substrate import EpisodeOutcome, TaskEpisode, validate_episode

    runtime = TaskEpisode(
        episode_id=episode["episode_id"], task_id=episode["task_id"], atom_id=episode["atom_id"],
        context_hash=episode["context_hash"], problem_signature=tuple(episode["problem_signature"]),
        fibre_snapshot_hash=episode["fibre_snapshot_hash"], operator_ids=tuple(episode["operator_ids"]),
        action_trace=tuple(episode["action_trace"]), observation_ids=tuple(episode["observation_ids"]),
        verification_ids=tuple(episode["verification_ids"]), outcome=EpisodeOutcome(episode["outcome"]),
        residual_signature=tuple(episode["residual_signature"]), evidence_pointers=tuple(episode["evidence_pointers"]),
        artifact_hash=episode["artifact_hash"], timestamp=episode["timestamp"], cost=episode["cost"],
    )
    assert validate_episode(runtime) == ()


def test_canonical_failure_lattice_passes_schema_runtime_and_trace_binding() -> None:
    lattice = _load(FAILURES)
    trace = _load(TRACE)
    _validator(FRAMEWORK / "schemas/failure-experience-lattice.schema.json").validate(lattice)
    event_ids = {item["event_id"] for item in trace["entries"]}
    new_failure = lattice["experiences"][-1]
    assert new_failure["diagnosis_status"] == "OBSERVED_ONLY"
    assert new_failure["candidate_id"] == "NO_CANDIDATE_RETROSPECTIVE_SOURCE_AUDIT"
    assert new_failure["research_trace_event_id"] in event_ids
    assert new_failure["artifact_hash"] == _canonical_hash(new_failure)

    _framework_import_path()
    from rakl.failure_lattice import FailureDiagnosisStatus, FailureExperience, validate_failure_experience
    runtime = FailureExperience(
        failure_id=new_failure["failure_id"], atom_id=new_failure["atom_id"], candidate_id=new_failure["candidate_id"],
        context_packet_hash=new_failure["context_packet_hash"], research_trace_event_id=new_failure["research_trace_event_id"],
        method_family=new_failure["method_family"], failure_mode=new_failure["failure_mode"],
        residual_signature=tuple(new_failure["residual_signature"]), broken_assumptions=tuple(new_failure["broken_assumptions"]),
        scope_conditions=tuple(new_failure["scope_conditions"]), competing_diagnoses=tuple(new_failure["competing_diagnoses"]),
        selected_diagnosis=new_failure["selected_diagnosis"], diagnosis_status=FailureDiagnosisStatus(new_failure["diagnosis_status"]),
        evidence_pointers=tuple(new_failure["evidence_pointers"]), falsifier_or_attempt=new_failure["falsifier_or_attempt"],
        observed_result=new_failure["observed_result"], artifact_hash=new_failure["artifact_hash"], timestamp=new_failure["timestamp"],
        local_repair_attempts=tuple(new_failure["local_repair_attempts"]),
    )
    assert validate_failure_experience(runtime) == ()


def test_canonical_trace_copies_pretrace_and_appends_retrospective_events_only() -> None:
    trace = _load(TRACE)
    original = _load(PRETRACE)
    _validator(FRAMEWORK / "schemas/math-research-trace.schema.json").validate(trace)
    assert trace["entries"][:7] == original["entries"]
    assert [item["event_type"] for item in trace["entries"][7:]] == ["RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"]
    assert not any(item["event_type"] == "CANDIDATE_PROPOSED" for item in trace["entries"])
    previous = ""
    for item in trace["entries"]:
        assert item["artifact_hash"] == _canonical_hash(item)
        assert item.get("previous_event_hash", "") == previous
        previous = item["artifact_hash"]

    _framework_import_path()
    from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict, audit_research_trace
    entries = tuple(ResearchTraceEntry(
        event_id=item["event_id"], atom_id=item["atom_id"], event_type=ResearchTraceEventType(item["event_type"]),
        timestamp=item["timestamp"], state_summary=item["state_summary"], action_summary=item["action_summary"],
        evidence_pointers=tuple(item["evidence_pointers"]), alternatives_considered=tuple(item.get("alternatives_considered", [])),
        decision_rationale=item.get("decision_rationale", ""), outputs=tuple(item.get("outputs", [])),
        uncertainties=tuple(item.get("uncertainties", [])), residuals=tuple(item.get("residuals", [])),
        next_steps=tuple(item.get("next_steps", [])), artifact_hash=item["artifact_hash"],
        previous_event_hash=item.get("previous_event_hash", ""),
    ) for item in trace["entries"])
    assert audit_research_trace(MathResearchTrace(trace["trace_id"], entries)).verdict is TraceGateVerdict.PASS


def test_correction_is_schema_valid_git_bound_and_fails_closed_on_authority() -> None:
    correction = _load(CORRECTION)
    schema = _validator(ROOT / "schemas/bsd-a1a1-pr96-postmerge-assurance-correction.schema.json")
    schema.validate(correction)
    assert correction["artifact_hash"] == _canonical_hash(correction)
    assert correction["correction"] == {
        "classification": "RETROSPECTIVE_SOURCE_BOUND_ROUTE_EVIDENCE",
        "strict_discovery_credit": "NO_STRICT_DISCOVERY_CREDIT",
        "root_authority": "ROOT_AUTHORITY_NONE",
        "originals_preserved": True,
        "repairs_original_chronology": False,
        "mathematical_candidate_generated": False,
        "next_candidate_gate": "FRESH_CONTEXT_MEMORY_TRACE_AND_DISCRIMINATOR_REQUIRED",
    }
    assert all(value is False for key, value in correction["authority_contract"].items() if key != "effective_authority")
    for field in [key for key in correction["authority_contract"] if key != "effective_authority"]:
        hostile = copy.deepcopy(correction)
        hostile["authority_contract"][field] = True
        with pytest.raises(jsonschema.ValidationError):
            schema.validate(hostile)
    for item in correction["successors"]:
        raw = _git("show", f'{item["source_commit"]}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert raw == (ROOT / item["path"]).read_bytes()
        assert item["git_blob_sha"] == _git("rev-parse", f'{item["source_commit"]}:{item["path"]}')
        assert item["raw_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()


def test_branch_changes_no_paper_or_manuscript_paths() -> None:
    base = _git("merge-base", "HEAD", "origin/main")
    changed = _git("diff", "--name-only", base, "HEAD").splitlines()
    forbidden = [
        path for path in changed
        if path.startswith(("paper/", "papers/", "publication/")) or path.endswith(".tex")
    ]
    assert forbidden == []
