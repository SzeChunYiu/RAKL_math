from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c052_k31_overlap_candidate_freeze_fixture.py"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C052_K31_OVERLAP_DISCRIMINATOR_IDENTITY_20260812.json"
FALSIFIER = PNP / "05_falsification/O9d12a2a1b_C052_K31_OVERLAP_FALSIFIER_IDENTITY_20260812.json"
RECEIPT = PNP / "09_trace/O9d12a2a1b_C052_K31_OVERLAP_CANDIDATE_FREEZE_RECEIPT_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_k31_candidate_freeze", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_documents_match_result_blind_fixture_and_exact_base() -> None:
    candidate, falsifier, receipt = module().build()
    assert [load(path) for path in (CANDIDATE, FALSIFIER, RECEIPT)] == [candidate, falsifier, receipt]
    assert candidate["application_base_sha"] == "8b05d8248c68b7fe80e42cb202f0129d55df751e"
    assert candidate["source_bindings"] == module().SOURCE_BINDINGS
    assert falsifier["candidate_artifact_hash"] == candidate["artifact_hash"]
    assert receipt["candidate_artifact_hash"] == candidate["artifact_hash"]
    assert receipt["falsifier_artifact_hash"] == falsifier["artifact_hash"]


def test_exact_target_blind_branch_contract_and_certificates_are_frozen() -> None:
    candidate = load(CANDIDATE)
    assert candidate["allowed_branches"] == [
        "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE",
        "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE",
        "CANNOT_CHECK",
    ]
    assert len(candidate["positive_certificate_obligations"]) == 7
    assert len(candidate["negative_certificate_obligations"]) == 6
    assert any("UNSAT" in item for item in candidate["positive_certificate_obligations"])
    assert any("byte-for-byte h=p" in item for item in candidate["positive_certificate_obligations"])
    assert any("proof of completeness" in item for item in candidate["negative_certificate_obligations"])
    assert candidate["target_blindness"] == {
        "overlap_label_or_branch_included": False,
        "public_marginal_witnesses_used_as_overlap_candidates": False,
        "same branch rules apply before any certificate content is accessed": True,
        "target_result_used_to_choose_identity": False,
    }


def test_falsifier_freezes_all_required_unmaterialized_worlds_and_integration() -> None:
    falsifier = load(FALSIFIER)
    worlds = {row["world_id"]: row for row in falsifier["future_worlds"]}
    assert set(worlds) == {
        "K31-PLANTED-POSITIVE-CERTIFICATE-KERNEL-v1",
        "K31-PLANTED-NEGATIVE-CERTIFICATE-KERNEL-v1",
        "K31-MALFORMED-CERTIFICATE-CANNOT-CHECK-v1",
        "K31-MARGINAL-ONLY-FALSE-POSITIVE-v1",
        "K31-SOURCE-BINDING-MISMATCH-v1",
        "K31-FRONTEND-KERNEL-BRANCH-PROPAGATION-v1",
    }
    assert all(row["materialized"] is False for row in worlds.values())
    assert worlds["K31-MARGINAL-ONLY-FALSE-POSITIVE-v1"]["expected_branch"] == "CANNOT_CHECK"
    assert worlds["K31-SOURCE-BINDING-MISMATCH-v1"]["layer"] == "integration"
    assert worlds["K31-FRONTEND-KERNEL-BRANCH-PROPAGATION-v1"]["layer"] == "integration"
    assert falsifier["implementation"] is None
    assert falsifier["evaluation_authorized"] is False


def test_freeze_contains_no_result_implementation_or_evaluation_authority() -> None:
    candidate = load(CANDIDATE)
    falsifier = load(FALSIFIER)
    receipt = load(RECEIPT)
    assert candidate["implementation"] is None
    assert candidate["evaluation_authorized"] is False
    assert candidate["result_state"] == "UNEVALUATED"
    assert falsifier["result_accessed"] is False
    assert receipt["next_authorized_action"] == "PR_REVIEW_MERGE_ONLY"
    assert receipt["credit"] == {
        "Git_CI_trace": 0,
        "independent_review": 0,
        "mathematical_result": 0,
        "mathematical_saturation": 0,
    }
    assert all(value is False for key, value in receipt["chronology_firewall"].items() if not key.endswith("identity_frozen"))
    source = FIXTURE.read_text(encoding="utf-8")
    for forbidden in ("from C041_fx_sat_one_sided", "import C041_fx_sat_one_sided", "decode_formula", "is_satisfiable", "subprocess"):
        assert forbidden not in source


def test_candidate_trace_delta_extends_pre_candidate_tip_without_result() -> None:
    receipt = load(RECEIPT)
    delta = receipt["trace_delta"]
    assert delta["event_type"] == "CANDIDATE_PROPOSED"
    assert delta["previous_event_hash"] == module().PREVIOUS_EVENT_HASH
    assert delta["outputs"][-1] == "ZERO_RESULT_OR_MATHEMATICAL_CREDIT"
    assert "RESULT_RECORDED" not in json.dumps(receipt)
    assert receipt["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
