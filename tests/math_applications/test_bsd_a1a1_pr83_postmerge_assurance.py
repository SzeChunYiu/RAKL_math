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
BASE = "50c703f3f0c518bba1b48fb17e51b03d53ed02c3"
PR_HEAD = "7ead1aff9b517e6537aff9269130374246eb2761"
PR_TREE = "356ca0204743fb23c946959f5348f762d69fdfb0"
MERGE = "8bc7a9cf17adf347e5be13ab61a08a690dda895e"
FRAMEWORK_COMMIT = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
FRAMEWORK_TREE = "b0f14dc300e20eb74a69f946e06343af1683ca16"
SOURCE_COMMIT = "434436b1a08f46bc7df6b75c4aa342476dc0799f"
TRACE_COMMIT = "0e337640c4e5d3cb6fddfa3c1d01cfc7705bccae"
FINAL_SUCCESSOR_COMMIT = "89ad0b01854bcd622a4cdb6001694b442869ffb6"
CORRECTION = BSD / "08_reviews/BSD_A1a1_PR83_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"
SOURCE_RECEIPT = BSD / "00_sources/BSD_A1a1_CURRENT_2026_SOURCE_RECEIPT_V1_20260811.json"
SOURCE_SNAPSHOT = BSD / "00_sources/BSD_A1a1_ARXIV_SOURCE_SNAPSHOT_20260811.xml"
EPISODE = BSD / "07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_CANONICAL_RETROSPECTIVE_V2_20260811.json"
FAILURES = BSD / "07_memory/BSD_A1a1_FAILURE_EXPERIENCE_LATTICE_V3_RETROSPECTIVE_20260811.json"
TRACE = BSD / "09_trace/BSD_A1a1_RESEARCH_TRACE_RETROSPECTIVE_SUCCESSOR_20260811.json"
PRETRACE = BSD / "09_trace/BSD_A1a1_PRE_CANDIDATE_TRACE_20260811.json"
METRICS_R2 = BSD / "07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R2.json"
METRICS_R3 = BSD / "07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R3_RETROSPECTIVE_SUCCESSOR.json"
SHADOW_EPISODE = BSD / "07_memory/BSD_A1a1_CURRENT_2026_TASK_EPISODE_SHADOW.json"
SHADOW_FAILURE = BSD / "07_memory/BSD_A1a1_CURRENT_2026_FAILURE_SHADOW.json"
OLD_LATTICE = BSD / "07_memory/BSD_A1a1_FAILURE_EXPERIENCE_LATTICE_20260811.json"


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


def _canonical_hash(value: dict, *, remove: bool = False) -> str:
    payload = copy.deepcopy(value)
    if remove:
        payload.pop("artifact_hash", None)
    else:
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


def _framework_validator_at(commit: str, schema_name: str) -> jsonschema.Draft202012Validator:
    raw = _git(
        "-C", str(FRAMEWORK), "show", f"{commit}:schemas/{schema_name}", binary=True
    )
    assert isinstance(raw, bytes)
    schema = json.loads(raw)
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


def test_pr83_git_provenance_and_all_seven_original_bytes_are_immutable() -> None:
    receipt = _load(CORRECTION)
    app = receipt["application_repository"]
    assert app == {
        "url": "https://github.com/SzeChunYiu/RAKL_math.git",
        "pre_pr_base_commit": BASE,
        "pr_head_commit": PR_HEAD,
        "pr_head_tree": PR_TREE,
        "merge_commit": MERGE,
        "merge_tree": PR_TREE,
        "merge_parents": [BASE, PR_HEAD],
    }
    assert _git("rev-parse", f"{PR_HEAD}^{{tree}}") == PR_TREE
    assert _git("rev-parse", f"{MERGE}^{{tree}}") == PR_TREE
    assert _git("show", "-s", "--format=%P", MERGE).split() == [BASE, PR_HEAD]

    changed = set(_git("diff", "--name-only", BASE, PR_HEAD).splitlines())
    bindings = receipt["preserved_pr83_artifacts"]
    assert len(bindings) == 7
    assert {item["path"] for item in bindings} == changed
    for item in bindings:
        raw = _git("show", f'{MERGE}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert (ROOT / item["path"]).read_bytes() == raw
        assert _git("rev-parse", f'{MERGE}:{item["path"]}') == item["git_blob_sha"]
        assert "sha256:" + hashlib.sha256(raw).hexdigest() == item["content_sha256"]
        assert _git("show", "-s", "--format=%cI", item["introduced_commit"]) == item["introduced_commit_time"]
        assert _git("merge-base", "--is-ancestor", item["introduced_commit"], PR_HEAD) == ""


def test_exact_bd1_framework_schema_and_runtime_bindings_are_loaded() -> None:
    receipt = _load(CORRECTION)["framework_authority"]
    assert receipt["commit"] == FRAMEWORK_COMMIT
    assert receipt["tree"] == FRAMEWORK_TREE
    assert receipt["application_gitlink"] == FRAMEWORK_COMMIT
    assert _git("-C", str(FRAMEWORK), "rev-parse", f"{FRAMEWORK_COMMIT}^{{tree}}") == FRAMEWORK_TREE
    for item in receipt["schema_bindings"] + receipt["runtime_bindings"]:
        assert _git("-C", str(FRAMEWORK), "rev-parse", f'{FRAMEWORK_COMMIT}:{item["path"]}') == item["git_blob_sha"]


def test_original_shadows_fail_current_schemas_exactly_and_remain_retrospective() -> None:
    correction = _load(CORRECTION)
    cases = [
        (SHADOW_EPISODE, "task-episode.schema.json", 9),
        (SHADOW_FAILURE, "failure-experience-lattice.schema.json", 3),
    ]
    recorded = {
        item["subject"]: item
        for item in correction["schema_runtime_audit"]["findings"]
    }
    for path, schema_name, expected in cases:
        errors = sorted(
            _framework_validator_at(FRAMEWORK_COMMIT, schema_name).iter_errors(_load(path)),
            key=lambda error: (list(map(str, error.absolute_path)), error.message),
        )
        assert len(errors) == expected
        subject = str(path.relative_to(ROOT))
        assert recorded[subject] == {
            "subject": subject,
            "schema_path": "schemas/" + schema_name,
            "error_count": expected,
            "violations": [
                (("/" + "/".join(map(str, error.absolute_path))) if error.absolute_path else "/")
                + ": "
                + error.message
                for error in errors
            ],
        }
    assert _load(SHADOW_EPISODE)["artifact_hash"] == _canonical_hash(
        _load(SHADOW_EPISODE), remove=True
    )
    assert _load(SHADOW_FAILURE)["artifact_hash"] == _canonical_hash(
        _load(SHADOW_FAILURE), remove=True
    )
    assert correction["correction"]["strict_discovery_credit"] == "NO_STRICT_DISCOVERY_CREDIT"
    assert correction["correction"]["mathematical_candidate_generated"] is False


def test_all_original_future_bindings_and_metrics_successor_chronology_are_exact() -> None:
    correction = _load(CORRECTION)
    assert [item["future_offset_seconds"] for item in correction["chronology_audit"]] == [659, 695, 588, 724]
    for item in correction["chronology_audit"]:
        claimed = _parse_time(item["claimed_timestamp"])
        bound = _parse_time(_git("show", "-s", "--format=%cI", item["bound_commit"]))
        assert bound > claimed
        assert int((bound - claimed).total_seconds()) == item["future_offset_seconds"]
        assert item["bound_commit_time"] == _git("show", "-s", "--format=%cI", item["bound_commit"])

    r2 = _load(METRICS_R2)
    r3 = _load(METRICS_R3)
    _validator(ROOT / "schemas/bsd-a1a1-metrics-chronology-successor.schema.json").validate(r3)
    assert r3["artifact_hash"] == _canonical_hash(r3)
    prior = r3["supersedes"]
    raw = _git("show", f'{prior["source_commit"]}:{prior["path"]}', binary=True)
    assert isinstance(raw, bytes)
    assert raw == METRICS_R2.read_bytes()
    assert prior["git_blob_sha"] == _git("rev-parse", f'{prior["source_commit"]}:{prior["path"]}')
    assert prior["raw_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
    assert prior["artifact_hash"] == r2["artifact_hash"]
    times = r3["corrected_chronology"]
    assert _parse_time(times["recorded_at_utc"]) > _parse_time(times["source_receipt_commit_time"]) > _parse_time(times["pr83_merge_commit_time"]) > _parse_time(times["scientific_subject_commit_time"])
    assert r3["measurement_status"] == "RETAINED_UNCHANGED_NOT_REMEASURED"


def test_exact_versioned_source_receipt_and_snapshot_are_content_bound() -> None:
    receipt = _load(SOURCE_RECEIPT)
    _validator(ROOT / "schemas/bsd-a1a1-current-source-receipt.schema.json").validate(receipt)
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    raw = SOURCE_SNAPSHOT.read_bytes()
    assert receipt["retrieval"]["snapshot_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
    assert receipt["retrieval"]["snapshot_size_bytes"] == len(raw)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    xml = ET.fromstring(raw)
    versioned = {entry.findtext("a:id", namespaces=ns).rsplit("/", 1)[-1] for entry in xml.findall("a:entry", ns)}
    assert versioned == {"2608.06879v1", "2603.22483v2", "1809.09066v4", "2203.12161v7"}
    assert {item["versioned_id"] for item in receipt["sources"]} == versioned
    assert all(item["claim_check"]["status"] == "SUPPORTED_BY_VERSIONED_ARXIV_METADATA" for item in receipt["sources"])
    assert all(len(item["pdf_sha256"]) == 71 and item["pdf_size_bytes"] > 0 for item in receipt["sources"])
    bound = _load(CORRECTION)["source_version_binding"]
    source_raw = _git("show", f'{bound["source_commit"]}:{bound["path"]}', binary=True)
    assert isinstance(source_raw, bytes)
    assert source_raw == SOURCE_RECEIPT.read_bytes()
    assert bound["git_blob_sha"] == _git("rev-parse", f'{bound["source_commit"]}:{bound["path"]}')
    assert bound["raw_sha256"] == "sha256:" + hashlib.sha256(source_raw).hexdigest()
    assert bound["versions"] == sorted(versioned)


def test_canonical_episode_hash_schema_runtime_and_fibre_manifest_are_exact() -> None:
    episode = _load(EPISODE)
    _framework_validator_at(FRAMEWORK_COMMIT, "task-episode.schema.json").validate(episode)
    # Runtime bd1 does not verify prefixed hashes, so this explicit content check is mandatory.
    assert episode["artifact_hash"] == _canonical_hash(episode)
    correction = _load(CORRECTION)
    manifest = correction["fibre_snapshot_manifest"]
    encoded = []
    for item in manifest["entries"]:
        assert item["git_blob_sha"] == _git("rev-parse", f'{item["source_commit"]}:{item["path"]}')
        encoded.append(f'{item["path"]}@git:{item["source_commit"]}@blob:{item["git_blob_sha"]}')
    observed = "sha256:" + hashlib.sha256(
        json.dumps(encoded, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert observed == manifest["artifact_hash"] == episode["fibre_snapshot_hash"]

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
    assert validate_episode(runtime) == ("episode:artifact_hash_invalid",)


def test_failure_lattice_hash_schema_runtime_and_typed_warning_scope_are_exact() -> None:
    lattice = _load(FAILURES)
    _validator(FRAMEWORK / "schemas/failure-experience-lattice.schema.json").validate(lattice)
    assert lattice["experiences"][0] == _load(OLD_LATTICE)["experiences"][0]
    assert lattice["experiences"][1]["artifact_hash"] == _canonical_hash(lattice["experiences"][1])
    assert lattice["experiences"][1]["diagnosis_status"] == "OBSERVED_ONLY"
    assert lattice["experiences"][1]["candidate_id"] == "NO_CANDIDATE_RETROSPECTIVE_SOURCE_AUDIT"
    assert len(lattice["links"]) == 1
    link = lattice["links"][0]
    assert link["relation"] == "TRANSFER_WARNING_FOR"
    assert "no causal equivalence" in link["rationale"]
    assert "no causal equivalence" in link["rationale"] and "theorem transfer" in link["rationale"]

    _framework_import_path()
    from rakl.failure_lattice import FailureDiagnosisStatus, FailureExperience, FailureExperienceLattice, FailureLink, FailureRelation, add_failure_link, validate_failure_experience
    experiences = []
    for item in lattice["experiences"]:
        value = FailureExperience(
            failure_id=item["failure_id"], atom_id=item["atom_id"], candidate_id=item["candidate_id"],
            context_packet_hash=item["context_packet_hash"], research_trace_event_id=item["research_trace_event_id"],
            method_family=item["method_family"], failure_mode=item["failure_mode"],
            residual_signature=tuple(item["residual_signature"]), broken_assumptions=tuple(item.get("broken_assumptions", [])),
            scope_conditions=tuple(item["scope_conditions"]), competing_diagnoses=tuple(item["competing_diagnoses"]),
            selected_diagnosis=item["selected_diagnosis"], diagnosis_status=FailureDiagnosisStatus(item["diagnosis_status"]),
            evidence_pointers=tuple(item["evidence_pointers"]), falsifier_or_attempt=item["falsifier_or_attempt"],
            observed_result=item["observed_result"], artifact_hash=item["artifact_hash"], timestamp=item["timestamp"],
            local_repair_attempts=tuple(item.get("local_repair_attempts", [])),
        )
        assert validate_failure_experience(value) == ()
        experiences.append(value)
    runtime = FailureExperienceLattice(tuple(experiences), ())
    runtime = add_failure_link(runtime, FailureLink(link["source_id"], link["target_id"], FailureRelation(link["relation"]), link["rationale"], tuple(link["evidence_pointers"])))
    assert len(runtime.links) == 1


def test_trace_copies_strict_pretrace_then_appends_only_retrospective_events() -> None:
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
    from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace, audit_research_trace
    entries = tuple(ResearchTraceEntry(
        event_id=item["event_id"], atom_id=item["atom_id"], event_type=ResearchTraceEventType(item["event_type"]),
        timestamp=item["timestamp"], state_summary=item["state_summary"], action_summary=item["action_summary"],
        evidence_pointers=tuple(item["evidence_pointers"]), alternatives_considered=tuple(item.get("alternatives_considered", [])),
        decision_rationale=item.get("decision_rationale", ""), outputs=tuple(item.get("outputs", [])),
        uncertainties=tuple(item.get("uncertainties", [])), residuals=tuple(item.get("residuals", [])),
        next_steps=tuple(item.get("next_steps", [])), artifact_hash=item["artifact_hash"],
        previous_event_hash=item.get("previous_event_hash", ""),
    ) for item in trace["entries"])
    runtime = MathResearchTrace(trace["trace_id"], entries)
    assert audit_research_trace(runtime).verdict is TraceGateVerdict.PASS
    assert audit_pre_candidate_trace(runtime, atom_id="BSD-A1a1-THETA-ORDER-COMPARISON", context_packet_hash="sha256:385d587cb9ab74512adc3fed98e00df9a804c37fd327539c2cea449a97b5417d").verdict is TraceGateVerdict.FAIL


def test_correction_successors_are_exactly_git_bound_and_authority_fails_closed() -> None:
    correction = _load(CORRECTION)
    schema = _validator(ROOT / "schemas/bsd-a1a1-postmerge-assurance-correction.schema.json")
    schema.validate(correction)
    assert correction["artifact_hash"] == _canonical_hash(correction)
    assert correction["schema_runtime_audit"]["candidate_event_count"] == 0
    for item in correction["successors"]:
        raw = _git("show", f'{item["source_commit"]}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert raw == (ROOT / item["path"]).read_bytes()
        assert item["git_blob_sha"] == _git("rev-parse", f'{item["source_commit"]}:{item["path"]}')
        assert item["raw_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
    assert {key: value for key, value in correction["authority_contract"].items() if key != "effective_authority"} == {
        "grants_strict_discovery_credit": False, "grants_proof_authority": False,
        "grants_root_authority": False, "grants_theorem_authority": False,
        "grants_novelty_authority": False, "grants_framework_authority": False,
        "grants_review_independence": False, "may_backfill_chronology": False,
        "may_suppress_failure_warning": False,
    }

    for field in ["grants_strict_discovery_credit", "grants_root_authority", "grants_theorem_authority", "grants_novelty_authority", "grants_framework_authority", "grants_review_independence", "may_backfill_chronology", "may_suppress_failure_warning"]:
        hostile = copy.deepcopy(correction)
        hostile["authority_contract"][field] = True
        with pytest.raises(jsonschema.ValidationError):
            schema.validate(hostile)
