from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[2]
CROSS = ROOT / "research/real_math/millennium/cross_problem"
FRAMEWORK = ROOT / "framework/RAKL"
PR_BASE = "49edbefcb3bd4bab24b154ac509ed933e8d817dc"
PR_HEAD = "260f971b72a1caa9d186fa00e29b0878b5b6a01c"
PR_HEAD_TREE = "0e023e12da5e3a9fd55d4093c1eabff4af53b413"
INTEGRATION = "7d2869f742872ca6fd5f8d48764f36c76a935523"
PRE_INTEGRATION_MAIN = "0fddc66a70a1f89b5aada81b63678fd66da589eb"
FRAMEWORK_COMMIT = "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
FRAMEWORK_TREE = "b0f14dc300e20eb74a69f946e06343af1683ca16"
SOURCE_COMMIT = "e5c8402901c36a294062ea50f2f0346a1ed886db"
SUCCESSOR_COMMIT = "bb0d4fea646a727a1174a7fa9abcaa01bb81d845"
ASSURANCE = CROSS / "08_reviews/XM005_PR71_OPEN_HEAD_RETROSPECTIVE_ASSURANCE_20260811.json"
SOURCE = CROSS / "00_sources/XM005_EXACT_SOURCE_VERSION_RECEIPT_20260811.json"
SOURCE_XML = CROSS / "00_sources/XM005_ARXIV_SOURCE_SNAPSHOT_20260811.xml"
EPISODE = CROSS / "07_memory/XM005_RETROSPECTIVE_TASK_EPISODE_20260811.json"
FAILURES = CROSS / "07_memory/XM005_RETROSPECTIVE_FAILURE_EXPERIENCE_LATTICE_20260811.json"
TRACE = CROSS / "09_trace/XM005_RETROSPECTIVE_RESEARCH_TRACE_20260811.json"
HISTORICAL_EPISODE = CROSS / "07_memory/XM005_METHOD_TASK_EPISODE_PROPOSAL_20260811.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _git(*args: str, binary: bool = False) -> str | bytes:
    run = subprocess.run(["git", "-C", str(ROOT), *args], check=True, stdout=subprocess.PIPE, text=not binary)
    return run.stdout if binary else run.stdout.strip()


def _hash(value: dict, *, remove: bool = False) -> str:
    payload = copy.deepcopy(value)
    if remove:
        payload.pop("artifact_hash", None)
    else:
        payload["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def _validator(path: Path) -> jsonschema.Draft202012Validator:
    schema = _load(path)
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())


def _framework_validator_at(commit: str, schema_name: str) -> jsonschema.Draft202012Validator:
    raw = _git("-C", str(FRAMEWORK), "show", f"{commit}:schemas/{schema_name}", binary=True)
    assert isinstance(raw, bytes)
    schema = json.loads(raw)
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())


def _time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
    return parsed


def _framework_path() -> None:
    value = str(FRAMEWORK / "src")
    if value not in sys.path:
        sys.path.insert(0, value)


def _historical_episode_content_bytes(value: dict) -> bytes:
    """Reproduce the exact TaskEpisode identity contract at ``FRAMEWORK_COMMIT``."""

    fields = (
        "episode_id", "task_id", "atom_id", "context_hash",
        "problem_signature", "fibre_snapshot_hash", "operator_ids",
        "action_trace", "observation_ids", "verification_ids", "outcome",
        "residual_signature", "evidence_pointers", "timestamp", "cost",
    )
    payload = {field: value[field] for field in fields}
    return json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def _assert_current_schema_rejects_historical_episode(value: dict) -> None:
    errors = list(_validator(FRAMEWORK / "schemas/task-episode.schema.json").iter_errors(value))
    assert "storage_admission" not in value
    assert any(
        error.validator == "required"
        and error.message == "'storage_admission' is a required property"
        for error in errors
    )


def _application_episode_assurance_reasons(value: dict) -> tuple[str, ...]:
    """Close bd1's length-gated TaskEpisode digest-verification bypass."""

    claimed = value.get("artifact_hash")
    if not isinstance(claimed, str) or re.fullmatch(r"[0-9a-f]{64}", claimed) is None:
        return ("application:episode_artifact_hash_not_raw_64_hex",)
    reasons: list[str] = []
    if hashlib.sha256(_historical_episode_content_bytes(value)).hexdigest() != claimed:
        reasons.append("application:episode_artifact_hash_mismatch")
    return tuple(reasons)


def test_pr71_is_open_historical_head_not_a_fake_merge_and_all_bytes_are_preserved() -> None:
    receipt = _load(ASSURANCE)
    historical = receipt["historical_pr71"]
    assert historical["state_observed"] == "OPEN"
    assert historical["merge_commit"] is None
    assert historical["base_commit"] == PR_BASE
    assert historical["head_commit"] == PR_HEAD
    assert historical["head_tree"] == PR_HEAD_TREE == _git("rev-parse", f"{PR_HEAD}^{{tree}}")
    assert historical["remote_branch_rewritten"] is False

    changed = set(_git("diff", "--name-only", PR_BASE, PR_HEAD).splitlines())
    bindings = receipt["preserved_pr71_artifacts"]
    assert len(bindings) == 6
    assert {item["path"] for item in bindings} == changed
    for item in bindings:
        raw = _git("show", f'{PR_HEAD}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert raw == (ROOT / item["path"]).read_bytes()
        assert item["git_blob_sha"] == _git("rev-parse", f'{PR_HEAD}:{item["path"]}')
        assert item["raw_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
        assert item["first_commit_time"] == _git("show", "-s", "--format=%cI", item["first_commit"])
        assert item["final_byte_commit_time"] == _git("show", "-s", "--format=%cI", item["final_byte_commit"])

    integration = receipt["current_main_integration"]
    assert integration["integration_merge_commit"] == INTEGRATION
    assert integration["integration_merge_parents"] == [PRE_INTEGRATION_MAIN, PR_HEAD]
    assert _git("show", "-s", "--format=%P", INTEGRATION).split() == [PRE_INTEGRATION_MAIN, PR_HEAD]
    assert integration["effect"] == "IMPORT_PR71_HEAD_BYTES_WITHOUT_CLAIMING_PR71_WAS_MERGED"


def test_candidate_before_context_memory_trace_and_source_chronology_is_exact() -> None:
    audit = _load(ASSURANCE)["chronology_audit"]
    candidate = _time(_git("show", "-s", "--format=%cI", audit["candidate_commit"]))
    assert candidate == _time(audit["candidate_commit_time"])
    for commit, field in [
        ("d1c48059f1c3c041b665ca1d0a4c2ac711334a22", "candidate_precedes_method_case_study_seconds"),
        ("7afa24dd50c10d2c2dc0703a7fcfc2bb0f2c21a2", "candidate_precedes_episode_proposal_seconds"),
        ("0c59960d31c1d752005476507ef6dbdb80938e48", "candidate_precedes_source_receipt_seconds"),
        (PR_HEAD, "candidate_precedes_final_source_correction_seconds"),
    ]:
        later = _time(_git("show", "-s", "--format=%cI", commit))
        assert int((later - candidate).total_seconds()) == audit[field]
    assert [audit["candidate_precedes_method_case_study_seconds"], audit["candidate_precedes_episode_proposal_seconds"], audit["candidate_precedes_source_receipt_seconds"], audit["candidate_precedes_final_source_correction_seconds"]] == [68, 139, 312, 746]
    initial = _time(audit["episode_initial_commit_time"])
    claimed = _time(audit["episode_claimed_recorded_at"])
    assert int((claimed - initial).total_seconds()) == audit["episode_initial_future_offset_seconds"] == 173
    assert audit["context_fiber_status"] == "MISSING"
    assert audit["dual_memory_review_status"] == "MISSING"
    assert audit["pre_candidate_trace_status"] == "MISSING"


def test_historical_episode_is_only_local_proposal_and_fails_canonical_task_schema() -> None:
    original = _load(HISTORICAL_EPISODE)
    local_schema = _validator(CROSS / "10_study_pattern/EXPERIENCE_EPISODE_PROPOSAL.schema.json")
    local_schema.validate(original)
    assert original["artifact_hash"] == _hash(original)
    historical = _framework_validator_at(FRAMEWORK_COMMIT, "task-episode.schema.json")
    errors = sorted(historical.iter_errors(original), key=lambda error: (list(map(str, error.absolute_path)), error.message))
    finding = _load(ASSURANCE)["schema_audit"]["canonical_task_schema_finding"]
    assert len(errors) == finding["error_count"] == 10
    assert finding["violations"] == [(("/" + "/".join(map(str, e.absolute_path))) if e.absolute_path else "/") + ": " + e.message for e in errors]
    assert _load(ASSURANCE)["schema_audit"]["strict_discovery_verdict"] == "FAIL_NO_RETROACTIVE_REPAIR"


def test_exact_source_versions_metadata_hashes_and_locators_are_bound() -> None:
    receipt = _load(SOURCE)
    _validator(ROOT / "schemas/xm005-source-version-receipt.schema.json").validate(receipt)
    assert receipt["artifact_hash"] == _hash(receipt)
    raw = SOURCE_XML.read_bytes()
    assert receipt["retrieval"]["snapshot_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
    assert receipt["retrieval"]["snapshot_size_bytes"] == len(raw)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    xml = ET.fromstring(raw)
    versions = {item.findtext("a:id", namespaces=ns).rsplit("/", 1)[-1] for item in xml.findall("a:entry", ns)}
    assert versions == {"2606.29468v1", "2008.09345v1", "2201.08232v4"}
    assert {item["versioned_id"] for item in receipt["sources"]} == versions
    assert all(item["source_check"]["status"] == "SUPPORTED_BY_VERSIONED_PDF_LOCATOR" for item in receipt["sources"])
    assert {item["versioned_id"]: item["source_check"]["pdf_page"] for item in receipt["sources"]} == {"2008.09345v1": 4, "2201.08232v4": 1, "2606.29468v1": 9}
    assert receipt["chronology_correction"]["official_version"] == "2008.09345v1"
    assert receipt["chronology_correction"]["official_published"] == "2020-08-21T07:36:26Z"
    assert all(len(item["pdf_sha256"]) == 71 and item["pdf_size_bytes"] > 0 for item in receipt["sources"])


def test_exact_bd1_framework_schema_and_runtime_blobs_are_pinned() -> None:
    framework = _load(ASSURANCE)["framework_authority"]
    assert framework["commit"] == FRAMEWORK_COMMIT
    assert framework["tree"] == FRAMEWORK_TREE
    assert framework["application_gitlink"] == FRAMEWORK_COMMIT
    for item in framework["schema_bindings"] + framework["runtime_bindings"]:
        assert _git("-C", str(FRAMEWORK), "rev-parse", f'{FRAMEWORK_COMMIT}:{item["path"]}') == item["git_blob_sha"]


def test_canonical_retrospective_episode_hash_schema_runtime_and_manifest_are_exact() -> None:
    episode = _load(EPISODE)
    _framework_validator_at(FRAMEWORK_COMMIT, "task-episode.schema.json").validate(episode)
    assert re.fullmatch(r"[0-9a-f]{64}", episode["artifact_hash"])
    assert _application_episode_assurance_reasons(episode) == ()
    assert hashlib.sha256(_historical_episode_content_bytes(episode)).hexdigest() == episode["artifact_hash"]
    _assert_current_schema_rejects_historical_episode(episode)
    manifest = _load(ASSURANCE)["historical_evidence_manifest"]
    encoded = []
    for item in manifest["entries"]:
        assert item["git_blob_sha"] == _git("rev-parse", f'{item["source_commit"]}:{item["path"]}')
        encoded.append(f'{item["path"]}@git:{item["source_commit"]}@blob:{item["git_blob_sha"]}')
    observed = "sha256:" + hashlib.sha256(json.dumps(encoded, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert observed == manifest["artifact_hash"] == episode["fibre_snapshot_hash"]

@pytest.mark.parametrize(
    ("mutation", "expected_reason"),
    [
        ("WRONG_LENGTH", "application:episode_artifact_hash_not_raw_64_hex"),
        ("SHA256_PREFIXED", "application:episode_artifact_hash_not_raw_64_hex"),
        ("CONTENT_MUTATION", "application:episode_artifact_hash_mismatch"),
    ],
)
def test_task_episode_application_assurance_rejects_hash_bypass_and_mutation(
    mutation: str, expected_reason: str
) -> None:
    hostile = copy.deepcopy(_load(EPISODE))
    if mutation == "WRONG_LENGTH":
        hostile["artifact_hash"] = hostile["artifact_hash"][:-1]
    elif mutation == "SHA256_PREFIXED":
        hostile["artifact_hash"] = "sha256:" + hostile["artifact_hash"]
    else:
        hostile["action_trace"].append("planted post-hash mutation")
    assert expected_reason in _application_episode_assurance_reasons(hostile)


def test_failure_lattice_is_scoped_runtime_valid_and_not_a_blacklist() -> None:
    lattice = _load(FAILURES)
    _validator(FRAMEWORK / "schemas/failure-experience-lattice.schema.json").validate(lattice)
    assert len(lattice["experiences"]) == 1
    assert lattice["links"] == []
    item = lattice["experiences"][0]
    assert item["artifact_hash"] == _hash(item)
    assert item["diagnosis_status"] == "SUPPORTED"
    assert "does not refute" in " ".join(item["scope_conditions"])
    assert "does not blacklist" in " ".join(item["scope_conditions"])

    _framework_path()
    from rakl.failure_lattice import FailureDiagnosisStatus, FailureExperience, validate_failure_experience
    runtime = FailureExperience(item["failure_id"], item["atom_id"], item["candidate_id"], item["context_packet_hash"], item["research_trace_event_id"], item["method_family"], item["failure_mode"], tuple(item["residual_signature"]), tuple(item["broken_assumptions"]), tuple(item["scope_conditions"]), tuple(item["competing_diagnoses"]), item["selected_diagnosis"], FailureDiagnosisStatus(item["diagnosis_status"]), tuple(item["evidence_pointers"]), item["falsifier_or_attempt"], item["observed_result"], item["artifact_hash"], item["timestamp"], tuple(item["local_repair_attempts"]))
    assert validate_failure_experience(runtime) == ()


def test_retrospective_trace_passes_integrity_but_prospective_candidate_gate_fails_closed() -> None:
    trace = _load(TRACE)
    _validator(FRAMEWORK / "schemas/math-research-trace.schema.json").validate(trace)
    assert [item["event_type"] for item in trace["entries"]] == ["RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"]
    assert not any(item["event_type"] == "CANDIDATE_PROPOSED" for item in trace["entries"])
    previous = ""
    for item in trace["entries"]:
        assert item["artifact_hash"] == _hash(item)
        assert item["previous_event_hash"] == previous
        previous = item["artifact_hash"]

    _framework_path()
    from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace, audit_research_trace
    entries = tuple(ResearchTraceEntry(item["event_id"], item["atom_id"], ResearchTraceEventType(item["event_type"]), item["timestamp"], item["state_summary"], item["action_summary"], tuple(item["evidence_pointers"]), tuple(item.get("alternatives_considered", [])), item.get("decision_rationale", ""), tuple(item.get("outputs", [])), tuple(item.get("uncertainties", [])), tuple(item.get("residuals", [])), tuple(item.get("next_steps", [])), item["artifact_hash"], item.get("previous_event_hash", "")) for item in trace["entries"])
    runtime = MathResearchTrace(trace["trace_id"], entries)
    assert audit_research_trace(runtime).verdict is TraceGateVerdict.PASS
    pre = audit_pre_candidate_trace(runtime, atom_id="XM-MOVING-CORE-RIGIDITY-005", context_packet_hash="sha256:97140726c846578b96a5b31d484d94520691c618918a0d6ddba1d38b36011737")
    assert pre.verdict is TraceGateVerdict.FAIL
    assert set(pre.reasons) == {f"required_trace_event_missing:{name}" for name in ["ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW", "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW", "NEXT_STEP_PROPOSED"]}
    gate = _load(ASSURANCE)["prospective_gate"]
    assert gate["status"] == "CLOSED"
    assert gate["candidate_generation_allowed"] is False


def test_assurance_successors_are_git_bound_and_authority_mutations_fail_closed() -> None:
    receipt = _load(ASSURANCE)
    schema = _validator(ROOT / "schemas/xm005-pr71-retrospective-assurance.schema.json")
    schema.validate(receipt)
    assert receipt["artifact_hash"] == _hash(receipt)
    for item in [receipt["source_version_binding"]] + receipt["successors"]:
        raw = _git("show", f'{item["source_commit"]}:{item["path"]}', binary=True)
        assert isinstance(raw, bytes)
        assert raw == (ROOT / item["path"]).read_bytes()
        assert item["git_blob_sha"] == _git("rev-parse", f'{item["source_commit"]}:{item["path"]}')
        assert item["raw_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
    assert receipt["pr71_disposition"]["close_now"] is False
    assert receipt["pr71_disposition"]["close_after_successor_review_and_merge"] is True

    for field in [key for key in receipt["authority_contract"] if key != "effective_authority"]:
        hostile = copy.deepcopy(receipt)
        hostile["authority_contract"][field] = not hostile["authority_contract"][field]
        with pytest.raises(jsonschema.ValidationError):
            schema.validate(hostile)
    hostile_gate = copy.deepcopy(receipt)
    hostile_gate["prospective_gate"]["candidate_generation_allowed"] = True
    with pytest.raises(jsonschema.ValidationError):
        schema.validate(hostile_gate)
    hostile_episode_binding = copy.deepcopy(receipt)
    hostile_episode_binding["successors"][0]["artifact_hash"] = "sha256:" + hostile_episode_binding["successors"][0]["artifact_hash"]
    with pytest.raises(jsonschema.ValidationError):
        schema.validate(hostile_episode_binding)
