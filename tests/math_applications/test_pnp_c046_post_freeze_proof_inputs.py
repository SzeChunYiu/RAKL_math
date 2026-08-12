from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CERTIFICATE = PNP / "04_candidates/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_PROOF_CERTIFICATE_FREEZE_20260812.json"
AUTHORIZATION = PNP / "09_trace/O9d12a2a1b_C046_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json"
EVALUATOR = PNP / "05_falsification/c046_high_half_separation_evaluator.py"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_LEMMA_FREEZE_20260812.json"

PUBLIC_FREEZE_HEAD = "68a0d8bcd4a13a351bb10738dc36ede1a97204e8"
CANDIDATE_FREEZE_COMMIT = "c76177457d6c75189b7cc80a3ccc012cb9f1e655"
EVALUATOR_RAW_SHA256 = "c45fd7a7e8fc05f61ef653a07c3882c1c33fbf878a98391646c8db0338a65193"
REQUIRED_TOKEN = "C046-SEPARATION-PROOF-CHECK-AUTHORIZED-AFTER-PUBLIC-FREEZE"
REQUIRED_OBLIGATIONS = {
    "BASE_U3_ROW_PROJECTION",
    "INDUCTIVE_SUPPORT_QUADRANT_CONTAINMENT",
    "MAGIC_LEADING_BIT_PREFIX_CONTAINMENT",
    "DISJOINT_HALF_INTERVAL_CONCLUSION",
}


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(document: dict) -> str:
    payload = dict(document)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_c046_proof_certificate_freezes_all_four_exact_obligations() -> None:
    certificate = _load(CERTIFICATE)
    assert certificate["candidate_id"] == "C046-HIGH-HALF-SEPARATION-LEMMA-v1"
    assert certificate["status"] == "FROZEN_HAND_DERIVATION_AWAITING_EVALUATOR"
    assert {record["obligation_id"] for record in certificate["obligations"]} == REQUIRED_OBLIGATIONS
    assert all(record["status"] == "PROVED" for record in certificate["obligations"])
    assert all(record["evidence_pointer"] for record in certificate["obligations"])
    assert certificate["source_identity"]["candidate_freeze_commit"] == CANDIDATE_FREEZE_COMMIT
    assert certificate["source_identity"]["public_freeze_head"] == PUBLIC_FREEZE_HEAD
    assert certificate["source_identity"]["evaluator_raw_sha256"] == EVALUATOR_RAW_SHA256
    assert certificate["source_identity"]["candidate_artifact_hash"] == _load(CANDIDATE)["artifact_hash"]
    assert certificate["target_access"] == {
        "target_decoder_imported_or_executed": False,
        "later_target_enumerated": False,
        "later_target_result_accessed": False,
        "finite_collision_level_selected": False,
        "evaluator_imported_or_executed_at_certificate_freeze": False,
    }
    assert certificate["authority"]["theorem_truth"] is False
    assert certificate["authority"]["independent_review"] is False
    assert certificate["artifact_hash"] == _canonical_hash(certificate)


def test_c046_authorization_is_later_than_public_remote_freeze_and_narrow() -> None:
    certificate = _load(CERTIFICATE)
    authorization = _load(AUTHORIZATION)
    assert authorization["token"] == REQUIRED_TOKEN
    assert authorization["candidate_id"] == certificate["candidate_id"]
    assert authorization["certificate_artifact_hash"] == certificate["artifact_hash"]
    assert authorization["evaluator_raw_sha256"] == hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    assert authorization["evaluator_raw_sha256"] == EVALUATOR_RAW_SHA256
    exposure = authorization["prior_public_freeze_exposure"]
    assert exposure["pull_request"] == 244
    assert exposure["remote_head_sha"] == PUBLIC_FREEZE_HEAD
    assert exposure["candidate_freeze_commit"] == CANDIDATE_FREEZE_COMMIT
    assert exposure["observed_at"] < authorization["authorized_at"]
    assert authorization["scope"] == {
        "exact_certificate_only": True,
        "exact_evaluator_only": True,
        "proof_obligation_evaluator_execution_authorized": True,
        "target_decoder_access_authorized": False,
        "later_target_enumeration_authorized": False,
        "finite_target_scan_authorized": False,
    }
    assert authorization["artifact_hash"] == _canonical_hash(authorization)
