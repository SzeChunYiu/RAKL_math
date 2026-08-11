from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"
FIXTURE = ROOT / "tests/fixtures/framework_bd1a2768/schemas"
BASE = "49edbefcb3bd4bab24b154ac509ed933e8d817dc"
PR_HEAD = "4da857235fc4cf84da0537403af15a97ba33e024"
MERGE = "8a608f340d47b4b6ae612275b0595faf6b804432"
MERGE_TREE = "57c2282124eeb58e90198491472f118d140e7b40"
FRAMEWORK_MAIN = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
FRAMEWORK_TREE = "b0f14dc300e20eb74a69f946e06343af1683ca16"
FRAMEWORK_SCHEMA_BLOBS = {
    "math-context-fiber.schema.json": "b24aa8db49aa4548fbd9eccd132b5bbd37230529",
    "research-memory-review.schema.json": "22f50c6c49e537d9e27999adb17fb7a60ad28827",
    "math-research-trace.schema.json": "700e9fd81fe7cf6e7ee956fcef05fd2006ff310d",
    "failure-experience-lattice.schema.json": "c007e33ec016bfab91d8688880bc18ce2192b031",
    "task-episode.schema.json": "076f38181b7a896ab1d740f5b6ad160e4fb2cd1c",
}
CORRECTION = NS / "10_case_study/NS-B1a1_C001_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"
CANONICAL_EPISODE = NS / "10_case_study/NS-B1a1_C001_TASK_EPISODE_CANONICAL_20260811.json"
TELEMETRY = NS / "10_case_study/NS-B1a1_C001_PROPOSAL_TELEMETRY_AUTHORITY_20260811.json"
FAILURE_LATTICE = NS / "07_memory/NS-B1a1_C001_FAILURE_LATTICE_CANONICAL_20260811.json"
ORIGINAL_CONTEXT = NS / "01_frontier/NS-B1a1_CONTEXT_FIBER_20260811.json"
ORIGINAL_MEMORY = NS / "07_memory/NS-B1a1_RESEARCH_MEMORY_REVIEW_20260811.json"
ORIGINAL_PRETRACE = NS / "09_trace/NS-B1a1_PRE_CANDIDATE_TRACE_20260811.json"
ORIGINAL_CONTINUATION = NS / "09_trace/NS-B1a1_C001_TRACE_CONTINUATION_20260811.json"
ORIGINAL_TASK = NS / "10_case_study/NS-B1a1_C001_V3_TASK_EPISODE_20260811.json"
ORIGINAL_FAILURE = NS / "07_memory/NS-B1a1_C001_FAILURE_EXPERIENCE_DELTA_20260811.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _git(*arguments: str, binary: bool = False) -> str | bytes:
    completed = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        capture_output=True,
        text=not binary,
    )
    return completed.stdout if binary else completed.stdout.strip()


def _canonical_hash(value: dict, key: str = "artifact_hash", *, remove: bool = False) -> str:
    unhashed = copy.deepcopy(value)
    if remove:
        unhashed.pop(key, None)
    else:
        unhashed[key] = ""
    raw = json.dumps(
        unhashed,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _validator(schema: dict) -> Draft202012Validator:
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _fixture_validator(name: str) -> Draft202012Validator:
    path = FIXTURE / name
    assert _git("hash-object", str(path)) == FRAMEWORK_SCHEMA_BLOBS[name]
    return _validator(_load(path))


def _parse_time(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(normalized)
    assert parsed.tzinfo is not None
    return parsed


def test_pr81_merge_provenance_and_all_eleven_original_bytes_are_immutable() -> None:
    receipt = _load(CORRECTION)
    assert _git("rev-parse", f"{MERGE}^{{tree}}") == MERGE_TREE
    assert _git("show", "-s", "--format=%P", MERGE).split() == [BASE, PR_HEAD]
    assert _git("rev-parse", f"{PR_HEAD}^{{tree}}") == MERGE_TREE
    assert receipt["application_repository"] == {
        "url": "https://github.com/SzeChunYiu/RAKL_math.git",
        "pre_pr_base_commit": BASE,
        "pr_head_commit": PR_HEAD,
        "pr_head_tree": MERGE_TREE,
        "merge_commit": MERGE,
        "merge_tree": MERGE_TREE,
        "merge_parents": [BASE, PR_HEAD],
    }

    bindings = receipt["preserved_artifacts"]
    assert len(bindings) == 11
    assert {item["path"] for item in bindings} == set(
        _git("diff", "--name-only", BASE, PR_HEAD).splitlines()
    )
    for item in bindings:
        path = item["path"]
        source = _git("show", f"{MERGE}:{path}", binary=True)
        assert isinstance(source, bytes)
        assert (ROOT / path).read_bytes() == source
        assert _git("rev-parse", f"{MERGE}:{path}") == item["git_blob_sha"]
        assert "sha256:" + hashlib.sha256(source).hexdigest() == item["content_sha256"]
        assert _git("merge-base", "--is-ancestor", item["introduced_commit"], PR_HEAD) == ""
        assert _git("show", "-s", "--format=%cI", item["introduced_commit"]) == item[
            "introduced_commit_time"
        ]


def test_current_v3_schema_snapshot_is_exact_and_reproduces_all_original_failures() -> None:
    receipt = _load(CORRECTION)
    framework = receipt["framework_authority"]
    assert framework["current_main_commit"] == FRAMEWORK_MAIN
    assert framework["current_main_tree"] == FRAMEWORK_TREE
    assert {Path(item["path"]).name: item["git_blob_sha"] for item in framework["schema_bindings"]} == FRAMEWORK_SCHEMA_BLOBS

    cases = [
        (ORIGINAL_CONTEXT, "math-context-fiber.schema.json", 14),
        (ORIGINAL_MEMORY, "research-memory-review.schema.json", 5),
        (ORIGINAL_PRETRACE, "math-research-trace.schema.json", 2),
        (ORIGINAL_CONTINUATION, "math-research-trace.schema.json", 2),
        (ORIGINAL_TASK, "task-episode.schema.json", 1),
        (ORIGINAL_FAILURE, "failure-experience-lattice.schema.json", 2),
    ]
    recorded_findings = {
        item["subject"]: item for item in receipt["schema_audit"]["findings"]
    }
    for document_path, schema_name, expected_count in cases:
        errors = sorted(
            _fixture_validator(schema_name).iter_errors(_load(document_path)),
            key=lambda error: (
                list(map(str, error.absolute_path)),
                error.message,
            ),
        )
        assert len(errors) == expected_count
        subject = str(document_path.relative_to(ROOT))
        assert recorded_findings[subject] == {
            "subject": subject,
            "schema_path": "schemas/" + schema_name,
            "error_count": expected_count,
            "violations": [
                (
                    "/" + "/".join(map(str, error.absolute_path))
                    if error.absolute_path
                    else "/"
                )
                + ": "
                + error.message
                for error in errors
            ],
        }

    assert {key: value for key, value in receipt["schema_audit"].items() if key != "findings"} == {
        "context_error_count": 14,
        "memory_error_count": 5,
        "pretrace_error_count": 2,
        "continuation_error_count": 2,
        "task_episode_error_count": 1,
        "failure_lattice_error_count": 2,
        "strict_process_verdict": "INVALID_NO_RETROACTIVE_REPAIR",
    }


def test_historical_remove_key_hash_audit_detects_e07_and_pretrace_document_defects() -> None:
    receipt = _load(CORRECTION)
    recorded = {item["subject"]: item for item in receipt["hash_audit"]["findings"]}
    computed: dict[str, tuple[str, str]] = {}

    for path, key in (
        (ORIGINAL_CONTEXT, "packet_hash"),
        (ORIGINAL_MEMORY, "artifact_hash"),
        (ORIGINAL_TASK, "artifact_hash"),
    ):
        document = _load(path)
        computed[str(path.relative_to(ROOT))] = (document[key], _canonical_hash(document, key, remove=True))
    for path in (ORIGINAL_PRETRACE, ORIGINAL_CONTINUATION):
        document = _load(path)
        for event in document["events"]:
            computed[event["event_id"]] = (
                event["artifact_hash"],
                _canonical_hash(event, remove=True),
            )
        subject = str(path.relative_to(ROOT)) + "::trace_hash"
        computed[subject] = (
            document["trace_hash"],
            _canonical_hash(document, "trace_hash", remove=True),
        )

    assert set(recorded) == set(computed)
    for subject, (stored, reproduced) in computed.items():
        assert recorded[subject] == {
            "subject": subject,
            "stored_hash": stored,
            "computed_remove_key_hash": reproduced,
            "matches_remove_key": stored == reproduced,
        }
    assert {subject for subject, item in recorded.items() if not item["matches_remove_key"]} == {
        "NS-B1a1-E07",
        "research/real_math/millennium/navier_stokes/09_trace/NS-B1a1_PRE_CANDIDATE_TRACE_20260811.json::trace_hash",
    }

    pretrace = _load(ORIGINAL_PRETRACE)
    continuation = _load(ORIGINAL_CONTINUATION)
    e07 = pretrace["events"][-1]
    assert continuation["starts_after_event_hash"] == e07["artifact_hash"]
    assert continuation["starts_after_event_hash"] != _canonical_hash(e07, remove=True)
    assert receipt["hash_audit"]["successor_rule"] == (
        "CANONICAL_JSON_SHA256_WITH_ARTIFACT_HASH_BLANK"
    )


def test_git_chronology_detects_all_three_future_dated_original_records() -> None:
    receipt = _load(CORRECTION)
    assert len(receipt["chronology_audit"]) == 3
    for finding in receipt["chronology_audit"]:
        commit_time = _parse_time(_git("show", "-s", "--format=%cI", finding["introducing_commit"]))
        claimed = _parse_time(finding["claimed_timestamp"])
        assert claimed > commit_time
        assert int((claimed - commit_time).total_seconds()) == finding["future_offset_seconds"]
        assert _git("merge-base", "--is-ancestor", finding["introducing_commit"], PR_HEAD) == ""


def test_successors_are_schema_valid_blank_field_hashed_and_non_backfilling() -> None:
    correction = _load(CORRECTION)
    telemetry = _load(TELEMETRY)
    episode = _load(CANONICAL_EPISODE)
    failures = _load(FAILURE_LATTICE)

    correction_validator = _validator(
        _load(ROOT / "schemas/postmerge-assurance-correction-receipt.schema.json")
    )
    telemetry_validator = _validator(
        _load(ROOT / "schemas/proposal-telemetry-authority-receipt.schema.json")
    )
    correction_validator.validate(correction)
    telemetry_validator.validate(telemetry)
    _fixture_validator("task-episode.schema.json").validate(episode)
    _fixture_validator("failure-experience-lattice.schema.json").validate(failures)

    assert correction["artifact_hash"] == _canonical_hash(correction)
    assert telemetry["artifact_hash"] == _canonical_hash(telemetry)
    assert episode["artifact_hash"] == _canonical_hash(episode)
    assert len(failures["experiences"]) == 1
    assert failures["experiences"][0]["artifact_hash"] == _canonical_hash(
        failures["experiences"][0]
    )
    assert failures["links"] == []

    original = _load(ORIGINAL_TASK)
    assert telemetry["telemetry_payload"] == original["shadow_extensions"]
    assert "shadow_extensions" not in episode
    assert correction["correction"] == {
        "classification": "RETROSPECTIVE_ROUTE_PRUNING",
        "strict_discovery_credit": "NO_STRICT_DISCOVERY_CREDIT",
        "root_authority": "ROOT_AUTHORITY_NONE",
        "originals_preserved": True,
        "repairs_original_chronology": False,
        "prospective_child_atom": "NS-B1a2",
    }


@pytest.mark.parametrize(
    ("target", "field", "value"),
    [
        ("correction", "grants_strict_discovery_credit", True),
        ("correction", "grants_root_authority", True),
        ("correction", "may_backfill_chronology", True),
        ("telemetry", "grants_theorem_authority", True),
        ("telemetry", "grants_framework_authority", True),
        ("telemetry", "grants_review_independence", True),
        ("telemetry", "may_suppress_failure_warning", True),
    ],
)
def test_hostile_authority_mutations_are_rejected(target: str, field: str, value: object) -> None:
    if target == "correction":
        document = _load(CORRECTION)
        validator = _validator(
            _load(ROOT / "schemas/postmerge-assurance-correction-receipt.schema.json")
        )
    else:
        document = _load(TELEMETRY)
        validator = _validator(
            _load(ROOT / "schemas/proposal-telemetry-authority-receipt.schema.json")
        )
    document["authority_contract"][field] = value
    with pytest.raises(ValidationError):
        validator.validate(document)


def test_hostile_failure_to_atom_link_is_rejected_by_runtime() -> None:
    framework_source = ROOT / "framework/RAKL/src"
    if str(framework_source) not in sys.path:
        sys.path.insert(0, str(framework_source))
    from rakl.failure_lattice import (  # noqa: PLC0415
        FailureDiagnosisStatus,
        FailureExperience,
        FailureExperienceLattice,
        FailureLink,
        FailureRelation,
        add_failure_link,
    )

    item = _load(FAILURE_LATTICE)["experiences"][0]
    experience = FailureExperience(
        failure_id=item["failure_id"],
        atom_id=item["atom_id"],
        candidate_id=item["candidate_id"],
        context_packet_hash=item["context_packet_hash"],
        research_trace_event_id=item["research_trace_event_id"],
        method_family=item["method_family"],
        failure_mode=item["failure_mode"],
        residual_signature=tuple(item["residual_signature"]),
        broken_assumptions=tuple(item["broken_assumptions"]),
        scope_conditions=tuple(item["scope_conditions"]),
        competing_diagnoses=tuple(item["competing_diagnoses"]),
        selected_diagnosis=item["selected_diagnosis"],
        diagnosis_status=FailureDiagnosisStatus(item["diagnosis_status"]),
        evidence_pointers=tuple(item["evidence_pointers"]),
        falsifier_or_attempt=item["falsifier_or_attempt"],
        observed_result=item["observed_result"],
        artifact_hash=item["artifact_hash"],
        timestamp=item["timestamp"],
        local_repair_attempts=tuple(item["local_repair_attempts"]),
    )
    lattice = FailureExperienceLattice(experiences=(experience,), links=())
    invalid = FailureLink(
        source_id=experience.failure_id,
        target_id="NS-B1a2",
        relation=FailureRelation.MOTIVATES_META_ATOM,
        rationale="An atom is not a registered failure endpoint.",
    )
    with pytest.raises(ValueError, match="existing source and target experiences"):
        add_failure_link(lattice, invalid)


def test_positive_memory_fibre_and_scope_evidence_remains_reproducible() -> None:
    memory = _load(ORIGINAL_MEMORY)
    bindings = memory["fibre_contents_actually_consulted"]
    assert len(bindings) == 9
    for binding in bindings:
        path, blob = binding.rsplit("@blob:", 1)
        assert _git("rev-parse", f"{BASE}:{path}") == blob
    raw = json.dumps(
        bindings,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    assert memory["fibre_snapshot_hash"] == "sha256:" + hashlib.sha256(raw).hexdigest()

    correction = _load(CORRECTION)
    assert any("physical cutoff terms are O(R)" in item for item in correction["positive_evidence_preserved"])
    assert any("no Navier-Stokes theorem" in item for item in correction["positive_evidence_preserved"])
