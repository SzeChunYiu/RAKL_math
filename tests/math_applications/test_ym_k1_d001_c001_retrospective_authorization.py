from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FIXTURE = YM / "09_trace/ym_k1_d001_c001_retrospective_authorization_fixture.py"


def module():
    spec = importlib.util.spec_from_file_location("ym_k1_d001_c001_retro_auth", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_authorization_binds_exact_merged_evaluator_and_freeze() -> None:
    f = module()
    document = f.build_document()
    assert json.loads(f.OUTPUT.read_text()) == document
    assert document["authorization_base_sha"] == "0c556fc68cbf4b4d25555437ba4fc26b8128c858"
    assert document["evaluator_identity_merge_sha"] == "ff21299ae77dde937e00c5739de3c526a30736d5"
    assert document["evaluator_binding"]["application_commit"] == document["evaluator_identity_merge_sha"]
    assert document["freeze_binding"]["application_commit"] == document["evaluator_identity_merge_sha"]
    assert document["evaluator_binding"]["raw_sha256"] == "4d096d89f2fdb038e9f26507caaf8393cb6b00cfab60ced6d5b9cfc41c7bc514"
    assert all(document["identity_checks"].values())


def test_round_is_authorization_only_and_stage_b_is_forbidden() -> None:
    document = module().build_document()
    assert all(value is False for value in document["current_round_state"].values())
    assert "ENTERING_STAGE_B" in document["explicitly_unauthorized"]
    assert "SELECTING_G_STAR" in document["explicitly_unauthorized"]
    assert document["authority"]["grants_current_mathematical_result_credit"] is False


def test_future_run_must_remain_retrospective_and_non_strict() -> None:
    document = module().build_document()
    assert document["mandatory_labels"]["run_type"] == "RETROSPECTIVE_REPRODUCTION_NOT_PROSPECTIVE_DISCOVERY"
    assert document["mandatory_labels"]["strict_rakl_discovery_chronology"] is False
    assert document["authority"]["grants_strict_discovery_authority"] is False


def test_artifact_hash_is_exact() -> None:
    f = module()
    document = f.build_document()
    actual = document["artifact_hash"]
    unsigned = dict(document)
    unsigned["artifact_hash"] = ""
    assert actual == "sha256:" + hashlib.sha256(f.canonical(unsigned)).hexdigest()
