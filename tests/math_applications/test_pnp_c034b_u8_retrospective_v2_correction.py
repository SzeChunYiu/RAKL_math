from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
V1_RECEIPT = PNP / "05_falsification/C034B_U8_RETROSPECTIVE_REPLAY_RECEIPT_20260811.json"
V1_REPLAY = PNP / "05_falsification/c034b_u8_retrospective_replay.py"
V1_SCHEMA = ROOT / "schemas/pnp-c034b-u8-retrospective-replay.schema.json"
V1_TEST = ROOT / "tests/math_applications/test_pnp_c034b_u8_retrospective_replay.py"
V1_REVIEW = PNP / "08_reviews/C034B_U8_RETROSPECTIVE_HOSTILE_REVIEW_20260811.md"
V2_REPLAY = PNP / "05_falsification/c034b_u8_retrospective_v2_correction.py"
V2_RECEIPT = PNP / "05_falsification/C034B_U8_RETROSPECTIVE_REPLAY_V2_CORRECTION_20260811.json"
V2_SCHEMA = ROOT / "schemas/pnp-c034b-u8-retrospective-v2-correction.schema.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _module():
    spec = importlib.util.spec_from_file_location("c034b_u8_v2", V2_REPLAY)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _git(*arguments: str, binary: bool = False) -> str | bytes:
    run = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        text=not binary,
    )
    return run.stdout if binary else run.stdout.strip()


def _git_object_exists(specification: str) -> bool:
    return subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "-e", specification],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def test_v2_is_deterministic_strict_self_hashed_and_preserves_v1_bytes() -> None:
    module = _module()
    observed = module.build_receipt()
    assert observed == _load(V2_RECEIPT)
    schema = _load(V2_SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(observed)
    assert observed["artifact_hash"] == _canonical_hash(observed)
    assert observed["correction_implementation"]["raw_sha256"] == (
        "sha256:" + hashlib.sha256(V2_REPLAY.read_bytes()).hexdigest()
    )
    assert observed["correction_schema"]["raw_sha256"] == (
        "sha256:" + hashlib.sha256(V2_SCHEMA.read_bytes()).hexdigest()
    )

    bindings = observed["superseded_v1_bindings"]
    expected = {
        V1_RECEIPT: bindings["receipt"],
        V1_REPLAY: bindings["implementation"],
        V1_SCHEMA: bindings["schema"],
        V1_TEST: bindings["test"],
        V1_REVIEW: bindings["review"],
    }
    for path, binding in expected.items():
        raw = path.read_bytes()
        assert binding["path"] == str(path.relative_to(ROOT))
        assert binding["raw_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
        assert _git("show", f'{binding["commit"]}:{binding["path"]}', binary=True) == raw
        assert _git("rev-parse", f'{binding["commit"]}:{binding["path"]}') == binding["git_blob_sha"]
    assert bindings["receipt"]["artifact_hash"] == _load(V1_RECEIPT)["artifact_hash"]
    assert observed["supersession"]["historical_bytes_preserved"] is True
    assert observed["supersession"]["v1_review_preserved_as_failed_history"] is True


def test_v2_chronology_and_git_source_bindings_are_executable() -> None:
    module = _module()
    receipt = _load(V2_RECEIPT)
    result = module.audit_git_bindings(receipt)
    assert result == {"verdict": "PASS", "checked_relations": 14}
    assert receipt["validation_worlds"]["git_binding_pass"] == result

    chronology = receipt["chronology_correction"]
    bad_recorded_at = datetime.fromisoformat(chronology["v1_recorded_at"])
    v1_commit_time = datetime.fromisoformat(chronology["v1_result_commit_time"])
    assert int((bad_recorded_at - v1_commit_time).total_seconds()) == 8078
    assert chronology["v1_chronology_verdict"] == "INVALID_FUTURE_RELATIVE_TO_CONTAINING_COMMIT"
    assert chronology["v2_chronology_verdict"] == "REALIZABLE_AFTER_INTEGRATED_BASE"
    assert datetime.fromisoformat(receipt["recorded_at"]) > datetime.fromisoformat(
        chronology["integrated_base_commit_time"]
    )

    receipt_path = str(V2_RECEIPT.relative_to(ROOT))
    if _git_object_exists(f"HEAD:{receipt_path}"):
        introduction = _git("log", "--diff-filter=A", "--format=%H", "--", receipt_path).splitlines()[0]
        introduced_at = datetime.fromisoformat(_git("show", "-s", "--format=%cI", introduction))
        assert datetime.fromisoformat(receipt["recorded_at"]) <= introduced_at


def test_v2_pass_fail_cannot_check_and_external_authority_boundaries() -> None:
    receipt = _load(V2_RECEIPT)
    worlds = receipt["validation_worlds"]
    assert worlds["finite_replay_pass"]["verdict"] == "PASS"
    assert worlds["finite_replay_pass"]["exact_optimum"] == "49/24"
    assert worlds["planted_fail"]["verdict"] == "FAIL"
    assert worlds["structural_cannot_check"] == {
        "verdict": "CANNOT_CHECK",
        "reason": "MISSING_GIT_BINDING_FIELDS",
    }
    assert receipt["claim_update"] == {
        "v1_receipt_status": "SUPERSEDED_BY_V2_CORRECTION_FAILED_HISTORY_RETAINED",
        "reconstructed_finite_lp_status": "RETROSPECTIVE_EXACT_REPLAY_PASS_SOURCE_AND_CHRONOLOGY_BOUND",
        "reported_external_certificate_status": "STILL_MISSING_NOT_REPRODUCED",
        "reported_external_support_counts_status": "UNVERIFIED_21_PRIMAL_24_DUAL",
        "root_status": "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE",
    }
    assert all(value is False for value in receipt["authority_contract"].values())


def test_v2_hostile_hash_authority_chronology_and_binding_mutations_fail_closed() -> None:
    module = _module()
    receipt = _load(V2_RECEIPT)
    schema = _load(V2_SCHEMA)
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )

    schema_mutations = []
    for path in (
        ("artifact_hash",),
        ("source_binding", "source_raw_sha256"),
        ("source_binding", "application_base_commit"),
    ):
        original = receipt
        for key in path:
            original = original[key]
        assert isinstance(original, str)
        for hostile_value in (7, original + "\n", original + "\r\n"):
            mutated = copy.deepcopy(receipt)
            target = mutated
            for key in path[:-1]:
                target = target[key]
            target[path[-1]] = hostile_value
            schema_mutations.append(mutated)
    authority = copy.deepcopy(receipt)
    authority["authority_contract"]["grants_p_vs_np_root_authority"] = True
    schema_mutations.append(authority)
    external = copy.deepcopy(receipt)
    external["claim_update"]["reported_external_certificate_status"] = "VERIFIED"
    schema_mutations.append(external)
    chronology = copy.deepcopy(receipt)
    chronology["chronology_correction"]["v1_chronology_verdict"] = "PASS"
    schema_mutations.append(chronology)
    for mutation in schema_mutations:
        assert list(validator.iter_errors(mutation))

    wrong_raw = copy.deepcopy(receipt)
    wrong_raw["source_binding"]["source_raw_sha256"] = "sha256:" + "0" * 64
    assert module.audit_git_bindings(wrong_raw)["verdict"] == "FAIL"
    wrong_blob = copy.deepcopy(receipt)
    wrong_blob["source_binding"]["assessment_git_blob_sha"] = "0" * 40
    assert module.audit_git_bindings(wrong_blob)["verdict"] == "FAIL"
    missing = copy.deepcopy(receipt)
    del missing["source_binding"]["application_base_commit"]
    assert module.audit_git_bindings(missing) == {
        "verdict": "CANNOT_CHECK",
        "reason": "MISSING_GIT_BINDING_FIELDS",
    }
