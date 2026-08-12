from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FIXTURE = YM / "09_trace/ym_k1_d001_c001_candidate_freeze_fixture.py"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def fixture():
    return load(FIXTURE, "ym_k1_d001_c001_freeze")


def test_documents_regenerate_from_exact_merged_pr401_main() -> None:
    m = fixture()
    docs = m.build_documents()
    assert m.PARENT_MAIN_SHA == "4c9e987483c06b56e8a060ca58ac3b98e365941f"
    assert m.FRAMEWORK_SHA == "d21592b0ff8da988deabb923fd549891ff8ad9f0"
    assert set(docs) == set(m.PATHS)
    for name, path in m.PATHS.items():
        assert json.loads(path.read_text()) == docs[name], name


def test_candidate_identity_binds_two_stage_protocol_before_result_access() -> None:
    m = fixture()
    docs = m.build_documents()
    candidate = docs["candidate"]
    assert candidate["candidate_id"] == "YM-S1a2i-K1-D001-C001-TWO-STAGE-SOURCE-BRIDGE"
    assert candidate["candidate_kind"] == "SOURCE_APPLICABILITY_DISCRIMINATOR_PROTOCOL_NOT_A_PROOF_LEMMA"
    assert candidate["candidate_identity"]["canonical_core_sha256"] == m._sha(m.candidate_core(m.parent_bindings()))
    assert candidate["target_access"] == {
        "source_proof_accessed_or_executed": False,
        "constants_derived": False,
        "g_star_selected": False,
        "stage_a_evaluated": False,
        "stage_b_evaluated": False,
        "planted_worlds_executed": False,
        "result_accessed": False,
    }
    assert candidate["authority"]["mathematical_result_credit"] is False
    assert candidate["authority"]["strict_proof_candidate_authority"] is False
    assert candidate["authority"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_stage_a_precedes_stage_b_and_freezes_exact_predicates() -> None:
    candidate = fixture().build_documents()["candidate"]
    protocol = candidate["two_stage_discriminator"]
    assert protocol["stage_order"] == [
        "STAGE_A_SOURCE_DOMAIN_COMPATIBILITY",
        "STAGE_B_EXACT_FLOW_MARGIN",
    ]
    a, b = protocol["stage_a"], protocol["stage_b"]
    assert a["chosen_graph_radius"] == "c_K=4*C_force/(1-rho)"
    assert a["pass_predicate"].endswith("c_K<=C_dom")
    assert "may not be split" in a["no_reinterpretation_rule"]
    assert b["entry_condition"] == "STAGE_A_SOURCE_DOMAIN_COMPATIBILITY=PASS only"
    assert b["lower_flow_factor"] == "L(g)=1-b_0*g^2-C_beta*g^4"
    assert b["required_predicates"] == [
        "L(g)>=0 for every 0<g<=g_star",
        "L(g)^2>=rho+(C_force/c_K)*g^2 for every 0<g<=g_star",
    ]
    assert "no value is selected" in b["frozen_interval"]


def test_exact_four_branches_and_precedence_are_frozen() -> None:
    candidate = fixture().build_documents()["candidate"]
    assert set(candidate["allowed_result_branches"]) == {
        "APPLICABLE_BRIDGE",
        "STRONGER_PREMISE_MISMATCH_A",
        "FLOW_MARGIN_FAIL_B",
        "CANNOT_CHECK",
    }
    precedence = " ".join(candidate["branch_precedence"])
    assert "Stage A cannot be checked" in precedence
    assert "Stage A is checked and fails" in precedence
    assert "Stage A passes and Stage B fails" in precedence
    assert "both stages pass" in precedence


def test_inert_worlds_include_conflated_c_and_factor_two_traps_without_values() -> None:
    docs = fixture().build_documents()
    manifest = docs["falsifier"]
    worlds = {row["world_id"]: row for row in manifest["planted_worlds"]}
    assert {key: row["expected_branch"] for key, row in worlds.items()} == {
        "WORLD-A-B-PASS-SEPARATE-CONSTANTS-EXACT-MARGIN": "APPLICABLE_BRIDGE",
        "WORLD-A-FAIL-CONFLATED-C-TRAP": "STRONGER_PREMISE_MISMATCH_A",
        "WORLD-B-FAIL-FACTOR-TWO-TRAP": "FLOW_MARGIN_FAIL_B",
        "WORLD-CANNOT-CHECK-UPSTREAM-CONSTANTS": "CANNOT_CHECK",
    }
    assert "4C/(1-rho)>C" in " ".join(worlds["WORLD-A-FAIL-CONFLATED-C-TRAP"]["structural_payload"])
    assert "1+rho>1" in " ".join(worlds["WORLD-B-FAIL-FACTOR-TWO-TRAP"]["structural_payload"])
    assert all(row["world_kind"].endswith("NO_VALUES") for row in worlds.values())
    assert manifest["world_payload_policy"].startswith("Structural predicate specifications only")
    assert manifest["current_round_execution_authorized"] is False
    assert manifest["source_proof_execution_authorized"] is False


def test_freeze_has_no_authorization_or_evaluator_implementation() -> None:
    m = fixture()
    docs = m.build_documents()
    manifest = docs["falsifier"]
    assert manifest["evaluator_identity"] is None
    assert manifest["evaluator_path"] is None
    assert manifest["evaluator_implementation_present"] is False
    assert manifest["future_authorization_status"].startswith("NOT_CREATED")
    assert "authorization" not in docs
    assert not (YM / "09_trace/YM-S1a2i_K1_D001_C001_EVALUATION_AUTHORIZATION_20260812.json").exists()
    assert not (YM / "05_oracles/ym_k1_d001_c001_inert_falsifier.py").exists()


def test_pr401_packet_and_exact_wilson_source_identities_are_content_bound() -> None:
    m = fixture()
    candidate = m.build_documents()["candidate"]
    source = candidate["source_identity"]
    assert source["zenodo_version_doi"] == "10.5281/zenodo.19393832"
    assert source["zenodo_concept_doi"] == "10.5281/zenodo.19393831"
    assert source["pdf_sha256"] == "08013e1ce75c8b2be79c62ba61f70e30024b9bb427c465ceab7ee9266236690d"
    assert source["tex_sha256"] == "ef936e502e84b0cafabc594c9705c16c9c1df29dc95f2a6a679b6b446c526c18"
    bindings = candidate["parent_packet_binding"]
    assert bindings["pr"] == 401
    assert bindings["merge_commit"] == m.PARENT_MAIN_SHA
    for binding in bindings["inputs"].values():
        raw = (ROOT / binding["path"]).read_bytes()
        assert binding["raw_sha256"] == hashlib.sha256(raw).hexdigest()
        document = json.loads(raw)
        assert binding["canonical_sha256"] == m._sha(document)
        blob = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", f"{m.PARENT_MAIN_SHA}:{binding['path']}"],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        ).stdout.strip()
        assert binding["git_blob"] == blob


def test_trace_appends_candidate_only_and_remains_hash_chained() -> None:
    m = fixture()
    docs = m.build_documents()
    pre = json.loads((ROOT / m.PRE_TRACE).read_text())
    trace = docs["trace"]
    assert trace["entries"][:-1] == pre["entries"]
    assert trace["entries"][-1]["event_type"] == "CANDIDATE_PROPOSED"
    assert trace["entries"][-1]["outputs"][-2:] == [
        "FROZEN_UNEVALUATED",
        "ZERO_MATHEMATICAL_RESULT_CREDIT",
    ]
    assert all(entry["event_type"] not in {"FALSIFIER_RUN", "RESULT_RECORDED", "PROOF_CHECKED"} for entry in trace["entries"])
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        unsigned = dict(entry)
        actual = unsigned["artifact_hash"]
        unsigned["artifact_hash"] = ""
        assert actual == m._sha(unsigned)
        previous = actual


def test_receipt_defers_authorization_and_evaluation_to_post_merge_round() -> None:
    docs = fixture().build_documents()
    receipt = docs["receipt"]
    assert "authorization" not in docs
    assert receipt["chronology"]["application_parent_commit"] == "4c9e987483c06b56e8a060ca58ac3b98e365941f"
    assert receipt["chronology"]["evaluation_authorization_created"] is False
    assert receipt["chronology"]["evaluator_implementation_present"] is False
    assert receipt["chronology"]["source_proof_executed"] is False
    assert receipt["chronology"]["falsifier_executed"] is False
    assert receipt["chronology"]["g_star_selected"] is False
    assert receipt["chronology"]["result_accessed"] is False
    assert receipt["authority"]["mathematical_result_credit"] is False
    assert receipt["authority"]["target_truth"] is False
    assert receipt["authority"]["independent_review"] is False
    assert "SEPARATE POST-MERGE ROUND" in receipt["allowed_next_action"]
