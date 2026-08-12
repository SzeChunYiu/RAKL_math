from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FIXTURE = YM / "09_trace/ym_k1_d001_c001_evaluation_authorization_fixture.py"


def module():
    spec = importlib.util.spec_from_file_location("ym_k1_d001_c001_auth", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_authorization_regenerates_from_exact_post_pr405_main() -> None:
    m = module()
    document = m.build_document()
    assert m.PARENT_MAIN_SHA == "46000411f3edc7b96eba3ddb201e45f2b6d690ce"
    assert json.loads(m.OUTPUT.read_text()) == document
    assert document["current_round_execution_state"]["authorization_publication_pending"] is True
    assert all(value is False for key, value in document["current_round_execution_state"].items() if key != "authorization_publication_pending")


def test_candidate_falsifier_and_receipt_identities_are_exactly_aligned() -> None:
    m = module()
    document = m.build_document()
    checks = document["identity_checks"]
    assert checks["candidate_id_alignment"] is True
    assert checks["candidate_core_alignment"] is True
    assert checks["falsifier_core_alignment"] is True
    for binding in document["public_freeze_binding"].values():
        raw = (ROOT / binding["path"]).read_bytes()
        assert binding["raw_sha256"] == hashlib.sha256(raw).hexdigest()
        blob = subprocess.run(["git", "-C", str(ROOT), "rev-parse", f"{m.PARENT_MAIN_SHA}:{binding['path']}"], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()
        assert binding["git_blob"] == blob


def test_authorization_is_future_effective_and_stage_ordered() -> None:
    document = module().build_document()
    future = document["authorized_only_after_this_authorization_is_merged"]
    assert all(future.values())
    order = " ".join(document["stage_order_and_fail_close"])
    assert "Stage A must run first" in order
    assert "Stage B is unauthorized unless Stage A" in order
    assert "g_star" in order and "before Stage B target evaluation" in order
    assert document["authority"]["licenses_future_scoped_evaluation_after_merge"] is True
    assert document["authority"]["grants_target_truth"] is False
    assert document["authority"]["grants_mathematical_result_credit"] is False


def test_public_wilson_source_boundary_and_broader_claim_bans_are_explicit() -> None:
    document = module().build_document()
    source = document["authorized_evidence_boundary"]["public_primary_source"]
    assert source["zenodo_version_doi"] == "10.5281/zenodo.19393832"
    assert source["zenodo_concept_doi"] == "10.5281/zenodo.19393831"
    assert source["pdf_sha256"] == "08013e1ce75c8b2be79c62ba61f70e30024b9bb427c465ceab7ee9266236690d"
    assert source["tex_sha256"] == "ef936e502e84b0cafabc594c9705c16c9c1df29dc95f2a6a679b6b446c526c18"
    banned = set(document["explicitly_unauthorized"])
    assert "CLAIMING_REFUTATION_OF_YANG_MILLS_OR_THE_FULL_SOURCE" in banned
    assert "CLAIMING_FULL_GRAPH_TRANSFORM_OR_STABLE_MANIFOLD_CLOSURE" in banned
    assert "CLAIMING_CONTINUUM_CONSTRUCTION_OS_RECONSTRUCTION_OR_MASS_GAP" in banned
    assert "EVALUATION_BEFORE_THIS_AUTHORIZATION_IS_MERGED_TO_MAIN" in banned


def test_artifact_hash_covers_full_authorization() -> None:
    m = module()
    document = m.build_document()
    unsigned = dict(document)
    actual = unsigned["artifact_hash"]
    unsigned["artifact_hash"] = ""
    assert actual == m._sha(unsigned)
