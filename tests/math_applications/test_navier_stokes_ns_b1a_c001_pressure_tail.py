from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"
RESULT = BASE / "01_frontier/NS-B1a_C001_PRESSURE_TAIL_LOCALIZATION_20260811.md"
PROVENANCE = (
    BASE
    / "04_candidates/negative_history/NS_B1a_C001_PR19_CHRONOLOGY_AUDIT_20260811.json"
)
RESULT_SNAPSHOT = (
    BASE
    / "04_candidates/negative_history/NS_B1a_C001_PR19_RESULT_SNAPSHOT_9B6B8AE.md"
)
TRACE_SNAPSHOT = (
    BASE
    / "04_candidates/negative_history/NS_B1a_C001_PR19_TRACE_SNAPSHOT_070B5CC.json"
)
TRACE = BASE / "09_trace/NS-B1a_C001_TRACE_CONTINUATION_20260811.json"
PARENT_TRACE = BASE / "09_trace/NS-B1a_PRE_CANDIDATE_TRACE_20260811.json"
FAILURES = BASE / "07_memory/NS-B1a_C001_FAILURE_EXPERIENCE_DELTA_20260811.json"
ASSURANCE_FAILURES = (
    BASE / "07_memory/NS_B1a_C001_PR19_ASSURANCE_FAILURE_DELTA_20260811.json"
)
REVIEW = BASE / "08_reviews/SAME_CONTEXT_REVIEW_NS-B1a_C001_RESULT_20260811.md"
VALIDATION = BASE / "05_oracles/NS_B1a_C001_RETROSPECTIVE_VALIDATION_20260811.json"
FRAMEWORK = ROOT / "framework/RAKL"
RETROSPECTIVE_AUTHORITY = (
    "RETROSPECTIVE_ANALYTIC_CALIBRATION / SEARCH_CONTROL_ONLY / "
    "NO_NAVIER_STOKES_ROOT_EVIDENCE / ROOT_AUTHORITY_NONE"
)


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _raw_sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _assert_self_hash(value: dict) -> None:
    expected = value["artifact_hash"]
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    assert expected == _canonical_hash(payload)


def _git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def _normalized_repository(value: str) -> str:
    value = value.strip().removesuffix(".git").removesuffix("/")
    if value.startswith("git@github.com:"):
        value = "https://github.com/" + value.removeprefix("git@github.com:")
    return value


def test_pressure_tail_dyadic_constants_remain_exact_but_search_control_only() -> None:
    pressure_geometric_sum = Fraction(1, 1) / (1 - Fraction(1, 4))
    gradient_geometric_sum = Fraction(1, 1) / (1 - Fraction(1, 8))
    assert 2 * pressure_geometric_sum == Fraction(8, 3)
    assert 2 * gradient_geometric_sum == Fraction(16, 7)

    text = RESULT.read_text(encoding="utf-8")
    assert RETROSPECTIVE_AUTHORITY in text
    assert "analytic shell calculation" in text
    assert "does **not** construct a Navier–Stokes sparse-tail solution" in text
    assert "No repository-visible exact evaluator or candidate identity predates" in text
    assert "were frozen before this candidate" not in text
    assert "Why this candidate is allowed now" not in text
    assert "VERIFIED_LOCAL_ANALYTIC_STEP" not in text


def test_pr19_chronology_receipt_is_self_hashed_and_preserves_exact_snapshots() -> None:
    receipt = _load(PROVENANCE)
    _assert_self_hash(receipt)
    assert receipt["source_pull_request"] == 19
    assert receipt["source_merge_commit"] == (
        "0ad7991d8b4f05792d6d43b6e36128ef4b7eada9"
    )
    assert receipt["preserved_source_identity"]["original_result_commit"] == (
        "9b6b8ae4c84fc3c1b579b4db8e3fe6726b6244c0"
    )
    assert receipt["preserved_source_identity"]["original_trace_commit"] == (
        "070b5cc620368862aa3b10414af7c986ce341601"
    )
    assert receipt["chronology_observation"]["exact_candidate_before_result"] is False
    assert "NO_BACKFILLED_PREREGISTRATION" in receipt["disposition"]
    assert receipt["authority"] == (
        "CHRONOLOGY_AUDIT / NEGATIVE_HISTORY / "
        "NO_NAVIER_STOKES_ROOT_EVIDENCE / ROOT_AUTHORITY_NONE"
    )

    snapshots = {item["snapshot_role"]: item for item in receipt["historical_snapshots"]}
    assert snapshots["ORIGINAL_RESULT_AND_CANDIDATE_SAME_FILE"]["raw_file_sha256"] == (
        _raw_sha256(RESULT_SNAPSHOT)
    )
    assert snapshots["LATER_BACKFILLED_TRACE"]["raw_file_sha256"] == (
        _raw_sha256(TRACE_SNAPSHOT)
    )
    assert snapshots["ORIGINAL_RESULT_AND_CANDIDATE_SAME_FILE"]["source_git_blob"] == (
        _git("hash-object", str(RESULT_SNAPSHOT)).stdout.strip()
    )
    assert snapshots["LATER_BACKFILLED_TRACE"]["source_git_blob"] == (
        _git("hash-object", str(TRACE_SNAPSHOT)).stdout.strip()
    )


def test_git_provenance_fails_closed_on_origin_commit_path_blob_and_ancestry() -> None:
    receipt = _load(PROVENANCE)
    origins = {
        _normalized_repository(value)
        for value in _git("remote", "get-url", "--all", "origin").stdout.splitlines()
    }
    assert _normalized_repository(receipt["source_repository"]) in origins
    assert _git(
        "merge-base", "--is-ancestor", receipt["source_merge_commit"], "HEAD", check=False
    ).returncode == 0
    assert _git(
        "merge-base",
        "--is-ancestor",
        receipt["source_head"],
        receipt["source_merge_commit"],
        check=False,
    ).returncode == 0
    merge_parents = _git("show", "-s", "--format=%P", receipt["source_merge_commit"]).stdout.split()
    assert merge_parents == [receipt["source_merge_first_parent"], receipt["source_head"]]

    for artifact in receipt["source_artifacts"]:
        source_object = f'{artifact["source_commit"]}:{artifact["path"]}'
        assert _git("cat-file", "-e", source_object, check=False).returncode == 0
        assert _git("rev-parse", source_object).stdout.strip() == artifact["source_git_blob"]
        assert (
            "sha256:"
            + hashlib.sha256(_git("show", source_object).stdout.encode("utf-8")).hexdigest()
            == artifact["raw_file_sha256"]
        )
        if artifact["first_pr19_commit"] is not None:
            introduced = _git(
                "log", "--follow", "--diff-filter=A", "--format=%H", "--", artifact["path"]
            ).stdout.splitlines()
            assert introduced == [artifact["first_pr19_commit"]]

    result_commit = receipt["preserved_source_identity"]["original_result_commit"]
    result_path = receipt["preserved_source_identity"]["original_result_path"]
    parent = _git("rev-parse", f"{result_commit}^").stdout.strip()
    assert _git("cat-file", "-e", f"{parent}:{result_path}", check=False).returncode != 0
    assert _git(
        "grep", "-n", "NS-B1a-C001", parent, "--", "research/real_math/millennium/navier_stokes",
        check=False,
    ).returncode != 0
    assert _git(
        "merge-base",
        "--is-ancestor",
        result_commit,
        receipt["preserved_source_identity"]["original_trace_commit"],
        check=False,
    ).returncode == 0


def test_failure_delta_is_hash_bound_schema_valid_and_retrospectively_scoped() -> None:
    delta = _load(FAILURES)
    experience = delta["experience"]
    payload = copy.deepcopy(experience)
    artifact_hash = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert artifact_hash == _canonical_hash(payload)
    assert experience["diagnosis_status"] == "SUPPORTED"
    assert experience["research_trace_event_id"] == "NS-B1a-E08R"
    assert any("retrospective" in value.lower() for value in experience["scope_conditions"])
    assert "SEARCH_CONTROL_ONLY" in experience["observed_result"]

    schema = _load(FRAMEWORK / "schemas/failure-experience-lattice.schema.json")
    jsonschema.Draft202012Validator(schema).validate(
        {"experiences": [experience], "links": delta["links"]}
    )

    assurance = _load(ASSURANCE_FAILURES)
    chronology = assurance["experience"]
    _assert_self_hash(chronology)
    assert chronology["failure_id"] == "F-NS-B1a-C001-PR19-CHRONOLOGY"
    assert chronology["diagnosis_status"] == "SUPPORTED"
    assert "exact temporal cause remains unverified" in chronology["selected_diagnosis"]
    assert "NO_BACKFILLED_PREREGISTRATION" in chronology["observed_result"]
    jsonschema.Draft202012Validator(schema).validate(
        {"experiences": [chronology], "links": assurance["links"]}
    )


def test_replacement_trace_records_retrospective_result_without_candidate_authority() -> None:
    parent = _load(PARENT_TRACE)
    continuation = _load(TRACE)
    assert continuation["trace_id"] == parent["trace_id"]
    assert continuation["parent_final_event_hash"] == parent["entries"][-1]["artifact_hash"]
    assert continuation["source_trace_superseded"]["source_pr"] == 19
    assert continuation["source_trace_superseded"]["chronology_audit_hash"] == (
        _load(PROVENANCE)["artifact_hash"]
    )
    previous = parent["entries"][-1]["artifact_hash"]
    event_types = []
    for entry in continuation["entries"]:
        _assert_self_hash(entry)
        assert entry["previous_event_hash"] == previous
        previous = entry["artifact_hash"]
        event_types.append(entry["event_type"])
    assert event_types == [
        "RESULT_RECORDED",
        "EXPERIENCE_MEMORY_REVIEW",
        "RESIDUAL_OPENED",
        "REVIEWED",
    ]
    assert "CANDIDATE_PROPOSED" not in event_types
    assert "FALSIFIER_RUN" not in event_types
    assert "PROMOTED" not in event_types


def test_review_dag_readme_and_validation_preserve_the_authority_boundary() -> None:
    review = REVIEW.read_text(encoding="utf-8")
    assert "not independent review or peer review" in review
    assert "repository chronology fails closed" in review.lower()
    assert "RETROSPECTIVE_ANALYTIC_CALIBRATION" in review
    assert "valid pre-candidate packet before `C001`" not in review

    dag = (BASE / "02_problem_dag/open_obligations.yaml").read_text(encoding="utf-8")
    readme = (BASE / "README.md").read_text(encoding="utf-8")
    assert "RETROSPECTIVE_ANALYTIC_SHELL_CALIBRATION" in dag
    assert "VERIFIED_LOCAL_PRESSURE_TAIL_CALIBRATION" not in dag
    assert "retrospective analytic shell calculation" in readme
    assert "first strict child candidate" not in readme

    validation = _load(VALIDATION)
    _assert_self_hash(validation)
    assert validation["subjects"]["chronology_audit_hash"] == _load(PROVENANCE)["artifact_hash"]
    assert validation["focused_result"]["exit_code"] == 0
    assert validation["full_result"]["exit_code"] == 0
    assert validation["authority"] == (
        "EXACT_LOCAL_VALIDATION_RECEIPT / NO_NAVIER_STOKES_ROOT_EVIDENCE / "
        "ROOT_AUTHORITY_NONE"
    )
