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
FINAL_VALIDATION = (
    BASE / "05_oracles/NS_B1a_C001_FINAL_HEAD_INTEGRATION_VALIDATION_20260811.json"
)
POSTMERGE_VALIDATION = (
    BASE / "05_oracles/NS_B1a_C001_PR51_POSTMERGE_INVARIANCE_20260811.json"
)
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


def _git_bytes(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=check,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def _normalized_repository(value: str) -> str:
    value = value.strip().removesuffix(".git").removesuffix("/")
    if value.startswith("git@github.com:"):
        value = "https://github.com/" + value.removeprefix("git@github.com:")
    return value


def _final_provenance_errors(
    receipt: dict, *, live_subject_commit: str | None = None
) -> tuple[str, ...]:
    errors: list[str] = []
    origins = {
        _normalized_repository(value)
        for value in _git("remote", "get-url", "--all", "origin").stdout.splitlines()
    }
    if _normalized_repository(receipt["source_repository"]) not in origins:
        errors.append("origin mismatch")

    commit_subjects = {
        "source PR base": receipt["source_pull_request"]["base"],
        "source PR head": receipt["source_pull_request"]["head"],
        "source PR merge": receipt["source_pull_request"]["merge"],
        "repair source": receipt["repair_source"],
        "prior integration": receipt["prior_integration_commit"],
        "current main": receipt["current_main"],
        "integration": receipt["integration_commit"],
    }
    available: dict[str, bool] = {}
    for role, subject in commit_subjects.items():
        commit = subject["commit"]
        available[role] = (
            _git("cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode == 0
        )
        if not available[role]:
            errors.append(f"missing commit: {role}")
            continue
        if _git("rev-parse", f"{commit}^{{tree}}").stdout.strip() != subject["tree"]:
            errors.append(f"tree mismatch: {role}")
        if "parents" in subject:
            observed_parents = _git(
                "show", "-s", "--format=%P", commit
            ).stdout.split()
            if observed_parents != subject["parents"]:
                errors.append(f"parent mismatch: {role}")

    integration = receipt["integration_commit"]
    if available.get("integration"):
        parents = _git("show", "-s", "--format=%P", integration["commit"]).stdout.split()
        if parents != integration["parents"]:
            errors.append("integration parent mismatch")
    if available.get("repair source") and available.get("current main"):
        observed_base = _git(
            "merge-base",
            receipt["repair_source"]["commit"],
            receipt["current_main"]["commit"],
        ).stdout.strip()
        if observed_base != receipt["merge_base"]:
            errors.append("merge-base mismatch")

    for requirement in receipt["ancestry_requirements"]:
        ancestor = requirement["ancestor"]
        descendant = requirement["descendant"]
        if _git("cat-file", "-e", f"{ancestor}^{{commit}}", check=False).returncode != 0:
            errors.append(f'missing ancestry commit: {requirement["role"]}')
        elif _git(
            "merge-base", "--is-ancestor", ancestor, descendant, check=False
        ).returncode != 0:
            errors.append(f'ancestry mismatch: {requirement["role"]}')

    expected_byte_mode = "GIT_SHOW_NO_TEXTCONV_NO_EXT_DIFF_BINARY_STDOUT"
    for binding in receipt["historical_bindings"]:
        role = binding["role"]
        commit = binding["commit"]
        path = binding["source_path"]
        if binding["byte_mode"] != expected_byte_mode:
            errors.append(f"byte mode mismatch: {role}")
        if _git("cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode != 0:
            errors.append(f"missing historical commit: {role}")
            continue
        if _git("rev-parse", f"{commit}^{{tree}}").stdout.strip() != binding["tree"]:
            errors.append(f"historical tree mismatch: {role}")
        source_object = f"{commit}:{path}"
        if _git("cat-file", "-e", source_object, check=False).returncode != 0:
            errors.append(f"missing historical path: {role}")
            continue
        if _git("rev-parse", source_object).stdout.strip() != binding["git_blob_sha"]:
            errors.append(f"historical blob mismatch: {role}")
        raw = _git_bytes("show", "--no-textconv", "--no-ext-diff", source_object).stdout
        observed_raw_hash = "sha256:" + hashlib.sha256(raw).hexdigest()
        if observed_raw_hash != binding["raw_sha256"]:
            errors.append(f"historical raw hash mismatch: {role}")
        snapshot = ROOT / binding["preserved_snapshot_path"]
        if not snapshot.is_file():
            errors.append(f"missing preserved snapshot: {role}")
        else:
            snapshot_raw = snapshot.read_bytes()
            if snapshot_raw != raw:
                errors.append(f"preserved snapshot mismatch: {role}")
            if "sha256:" + hashlib.sha256(snapshot_raw).hexdigest() != binding[
                "preserved_snapshot_raw_sha256"
            ]:
                errors.append(f"preserved snapshot hash mismatch: {role}")

    for role, subject in receipt["live_subjects"].items():
        path = ROOT / subject["path"]
        if live_subject_commit is None:
            if not path.is_file():
                errors.append(f"missing live subject: {role}")
                continue
            raw_bytes = path.read_bytes()
        else:
            source_object = f'{live_subject_commit}:{subject["path"]}'
            probe = _git_bytes("cat-file", "-e", source_object, check=False)
            if probe.returncode != 0:
                errors.append(f"missing historical live subject: {role}")
                continue
            raw_bytes = _git_bytes(
                "show", "--no-textconv", "--no-ext-diff", source_object
            ).stdout
        if "sha256:" + hashlib.sha256(raw_bytes).hexdigest() != subject["raw_sha256"]:
            errors.append(f"live raw hash mismatch: {role}")
        if subject["semantic_hash_kind"] == "SELF_HASH":
            value = json.loads(raw_bytes.decode("utf-8"))
            try:
                _assert_self_hash(value)
            except AssertionError:
                errors.append(f"live self-hash mismatch: {role}")
            if value["artifact_hash"] != subject["semantic_hash"]:
                errors.append(f"live semantic hash mismatch: {role}")
        elif subject["semantic_hash_kind"] == "NESTED_EXPERIENCE_SELF_HASH":
            value = json.loads(raw_bytes.decode("utf-8"))["experience"]
            try:
                _assert_self_hash(value)
            except AssertionError:
                errors.append(f"live self-hash mismatch: {role}")
            if value["artifact_hash"] != subject["semantic_hash"]:
                errors.append(f"live semantic hash mismatch: {role}")
        elif subject["semantic_hash_kind"] == "FINAL_TRACE_EVENT_HASH":
            value = json.loads(raw_bytes.decode("utf-8"))["entries"][-1][
                "artifact_hash"
            ]
            if value != subject["semantic_hash"]:
                errors.append(f"live semantic hash mismatch: {role}")
        elif subject["semantic_hash_kind"] != "RAW_ONLY":
            errors.append(f"unknown semantic hash kind: {role}")
    return tuple(errors)


def _postmerge_invariance_errors(receipt: dict) -> tuple[str, ...]:
    errors: list[str] = []
    available: dict[str, bool] = {}
    for role in ("integration_base", "repaired_pr_head", "post_merge"):
        subject = receipt[role]
        commit = subject["commit"]
        available[role] = (
            _git("cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode == 0
        )
        if not available[role]:
            errors.append(f"missing commit: {role}")
            continue
        if _git("rev-parse", f"{commit}^{{tree}}").stdout.strip() != subject["tree"]:
            errors.append(f"tree mismatch: {role}")
        if "parents" in subject:
            parents = _git("show", "-s", "--format=%P", commit).stdout.split()
            if parents != subject["parents"]:
                errors.append(f"parent mismatch: {role}")

    for requirement in receipt["ancestry_requirements"]:
        if _git(
            "merge-base",
            "--is-ancestor",
            requirement["ancestor"],
            requirement["descendant"],
            check=False,
        ).returncode != 0:
            errors.append(f'ancestry mismatch: {requirement["role"]}')

    current_main = _git("rev-parse", "origin/main").stdout.strip()
    if _git(
        "merge-base",
        "--is-ancestor",
        receipt["post_merge"]["commit"],
        current_main,
        check=False,
    ).returncode != 0:
        errors.append("live main does not descend from registered post-merge commit")

    corrective = receipt["corrective_test_source"]
    corrective_commit = corrective["commit"]
    corrective_path = corrective["path"]
    if _git(
        "cat-file", "-e", f"{corrective_commit}^{{commit}}", check=False
    ).returncode != 0:
        errors.append("missing corrective test source commit")
    else:
        if _git("rev-parse", f"{corrective_commit}^{{tree}}").stdout.strip() != corrective[
            "tree"
        ]:
            errors.append("corrective test source tree mismatch")
        source_object = f"{corrective_commit}:{corrective_path}"
        if _git("cat-file", "-e", source_object, check=False).returncode != 0:
            errors.append("missing corrective test source path")
        else:
            if _git("rev-parse", source_object).stdout.strip() != corrective["git_blob_sha"]:
                errors.append("corrective test source blob mismatch")
            raw = _git_bytes(
                "show", "--no-textconv", "--no-ext-diff", source_object
            ).stdout
            if "sha256:" + hashlib.sha256(raw).hexdigest() != corrective["raw_sha256"]:
                errors.append("corrective test source raw hash mismatch")

    prior = receipt["historical_receipt"]
    prior_path = ROOT / prior["path"]
    if not prior_path.is_file():
        errors.append("missing historical receipt")
    else:
        if _raw_sha256(prior_path) != prior["raw_sha256"]:
            errors.append("historical receipt raw hash mismatch")
        value = _load(prior_path)
        if value["artifact_hash"] != prior["artifact_hash"]:
            errors.append("historical receipt artifact hash mismatch")
        if value["current_main"]["commit"] != receipt["integration_base"]["commit"]:
            errors.append("historical receipt integration-base mismatch")

    context = receipt["attribute_context"]
    snapshot_path = context["snapshot_path"]
    if available["integration_base"]:
        registered_attr = _git(
            f'--attr-source={receipt["integration_base"]["commit"]}',
            "check-attr",
            "whitespace",
            "--",
            snapshot_path,
        ).stdout.strip()
        if not registered_attr.endswith(context["integration_base_attribute"]):
            errors.append("integration-base attribute mismatch")
    if available["post_merge"]:
        postmerge_attr = _git(
            f'--attr-source={receipt["post_merge"]["commit"]}',
            "check-attr",
            "whitespace",
            "--",
            snapshot_path,
        ).stdout.strip()
        if not postmerge_attr.endswith(context["post_merge_attribute"]):
            errors.append("post-merge attribute mismatch")
    return tuple(errors)


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


def test_final_integration_validation_is_self_hashed_and_exactly_scoped() -> None:
    receipt = _load(FINAL_VALIDATION)
    postmerge = _load(POSTMERGE_VALIDATION)
    _assert_self_hash(receipt)
    assert receipt["current_main"]["commit"] == postmerge["integration_base"]["commit"]
    assert postmerge["historical_receipt"]["artifact_hash"] == receipt["artifact_hash"]
    assert receipt["framework_pin"] == (
        "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
    )
    assert receipt["validation"]["focused_passed"] == 10
    assert receipt["validation"]["full_passed"] == 217
    assert receipt["validation"]["diff_check_result"] == (
        "CLEAN_IN_EXACT_HEAD_WORKTREE_CONTEXT"
    )
    assert receipt["authority"] == (
        "FINAL_HEAD_INTEGRATION_VALIDATION / RETROSPECTIVE_ANALYTIC_CALIBRATION / "
        "SEARCH_CONTROL_ONLY / NO_NAVIER_STOKES_ROOT_EVIDENCE / ROOT_AUTHORITY_NONE"
    )


def test_final_integration_git_provenance_is_executable_and_complete() -> None:
    postmerge = _load(POSTMERGE_VALIDATION)
    assert _final_provenance_errors(
        _load(FINAL_VALIDATION),
        live_subject_commit=postmerge["repaired_pr_head"]["commit"],
    ) == ()


def test_final_integration_git_provenance_planted_worlds_fail_closed() -> None:
    receipt = _load(FINAL_VALIDATION)
    source_commit = _load(POSTMERGE_VALIDATION)["repaired_pr_head"]["commit"]

    missing = copy.deepcopy(receipt)
    missing["repair_source"]["commit"] = "0" * 40
    assert "missing commit: repair source" in _final_provenance_errors(
        missing, live_subject_commit=source_commit
    )

    forged_tree = copy.deepcopy(receipt)
    forged_tree["current_main"]["tree"] = "f" * 40
    assert "tree mismatch: current main" in _final_provenance_errors(
        forged_tree, live_subject_commit=source_commit
    )

    missing_path = copy.deepcopy(receipt)
    missing_path["historical_bindings"][0]["source_path"] += ".missing"
    assert "missing historical path: original result" in _final_provenance_errors(
        missing_path, live_subject_commit=source_commit
    )

    forged_blob = copy.deepcopy(receipt)
    forged_blob["historical_bindings"][0]["git_blob_sha"] = "f" * 40
    assert "historical blob mismatch: original result" in _final_provenance_errors(
        forged_blob, live_subject_commit=source_commit
    )

    forged_raw = copy.deepcopy(receipt)
    forged_raw["historical_bindings"][1]["raw_sha256"] = "sha256:" + "f" * 64
    assert "historical raw hash mismatch: original trace" in _final_provenance_errors(
        forged_raw, live_subject_commit=source_commit
    )

    forged_origin = copy.deepcopy(receipt)
    forged_origin["source_repository"] = "https://github.com/example/not-rakl-math"
    assert "origin mismatch" in _final_provenance_errors(
        forged_origin, live_subject_commit=source_commit
    )

    broken_ancestry = copy.deepcopy(receipt)
    broken_ancestry["ancestry_requirements"][0]["descendant"] = receipt[
        "source_pull_request"
    ]["base"]["commit"]
    assert "ancestry mismatch: repair source reaches integration" in (
        _final_provenance_errors(
            broken_ancestry, live_subject_commit=source_commit
        )
    )


def test_whitespace_policy_preserves_only_the_immutable_snapshot_exception() -> None:
    snapshot_path = (
        "research/real_math/millennium/navier_stokes/04_candidates/negative_history/"
        "NS_B1a_C001_PR19_RESULT_SNAPSHOT_9B6B8AE.md"
    )
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8").splitlines()
    exemptions = [line for line in attributes if "whitespace=" in line]
    assert exemptions == [
        f"{snapshot_path} whitespace=-trailing-space"
    ]

    postmerge = _load(POSTMERGE_VALIDATION)
    integration_base = postmerge["integration_base"]["commit"]
    repaired_pr_head = postmerge["repaired_pr_head"]["commit"]
    post_merge = postmerge["post_merge"]["commit"]

    default_attr = _git("check-attr", "whitespace", "--", snapshot_path).stdout.strip()
    current_main_attr = _git(
        "--attr-source=origin/main", "check-attr", "whitespace", "--", snapshot_path
    ).stdout.strip()
    base_attr = _git(
        f"--attr-source={integration_base}",
        "check-attr",
        "whitespace",
        "--",
        snapshot_path,
    ).stdout.strip()
    assert default_attr.endswith("whitespace: -trailing-space")
    assert current_main_attr.endswith("whitespace: -trailing-space")
    assert base_attr.endswith("whitespace: unspecified")

    assert _git("diff", "--check", "origin/main...HEAD", check=False).returncode == 0
    base_context = _git(
        f"--attr-source={integration_base}",
        "diff",
        "--check",
        f"{integration_base}...{repaired_pr_head}",
        check=False,
    )
    assert base_context.returncode != 0
    assert base_context.stdout.count(f"{snapshot_path}:") == 3
    postmerge_context = _git(
        f"--attr-source={post_merge}",
        "diff",
        "--check",
        f"{integration_base}...{repaired_pr_head}",
        check=False,
    )
    assert postmerge_context.returncode == 0

    receipt_context = _load(FINAL_VALIDATION)["validation"]["diff_check_context"]
    assert receipt_context["default_exact_head_worktree_result"] == "CLEAN"
    assert receipt_context["explicit_head_attribute_source_result"] == "CLEAN"
    assert receipt_context["explicit_base_attribute_source_result"] == (
        "EXPECTED_CONTEXTUAL_FAILURE_IMMUTABLE_SNAPSHOT_TRAILING_WHITESPACE"
    )
    assert receipt_context["context_free_clean_claim"] is False


def test_pr51_postmerge_receipt_binds_immutable_integration_semantics() -> None:
    receipt = _load(POSTMERGE_VALIDATION)
    _assert_self_hash(receipt)
    assert _postmerge_invariance_errors(receipt) == ()
    assert receipt["post_merge"]["parents"] == [
        receipt["integration_base"]["commit"],
        receipt["repaired_pr_head"]["commit"],
    ]
    assert receipt["validation"]["focused_passed"] == 12
    assert receipt["validation"]["full_passed"] == 219
    assert receipt["framework_pin"] == (
        "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
    )
    assert receipt["authority"].endswith(
        "NO_NAVIER_STOKES_ROOT_EVIDENCE / ROOT_AUTHORITY_NONE"
    )


def test_pr51_postmerge_planted_worlds_fail_closed() -> None:
    receipt = _load(POSTMERGE_VALIDATION)

    missing = copy.deepcopy(receipt)
    missing["integration_base"]["commit"] = "0" * 40
    assert "missing commit: integration_base" in _postmerge_invariance_errors(missing)

    forged_tree = copy.deepcopy(receipt)
    forged_tree["repaired_pr_head"]["tree"] = "f" * 40
    assert "tree mismatch: repaired_pr_head" in _postmerge_invariance_errors(
        forged_tree
    )

    forged_parents = copy.deepcopy(receipt)
    forged_parents["post_merge"]["parents"] = list(
        reversed(forged_parents["post_merge"]["parents"])
    )
    assert "parent mismatch: post_merge" in _postmerge_invariance_errors(
        forged_parents
    )

    broken_ancestry = copy.deepcopy(receipt)
    broken_ancestry["ancestry_requirements"][0]["descendant"] = receipt[
        "integration_base"
    ]["commit"]
    assert "ancestry mismatch: repaired head reaches merge" in (
        _postmerge_invariance_errors(broken_ancestry)
    )

    forged_receipt = copy.deepcopy(receipt)
    forged_receipt["historical_receipt"]["raw_sha256"] = "sha256:" + "f" * 64
    assert "historical receipt raw hash mismatch" in _postmerge_invariance_errors(
        forged_receipt
    )

    forged_test_blob = copy.deepcopy(receipt)
    forged_test_blob["corrective_test_source"]["git_blob_sha"] = "f" * 40
    assert "corrective test source blob mismatch" in _postmerge_invariance_errors(
        forged_test_blob
    )
