from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C047_ORIENTATION_ONLY_SEPARATION_LEMMA_FREEZE_20260812.json"
CERTIFICATE = PNP / "04_candidates/O9d12a2a1b_C047_ORIENTATION_ONLY_SEPARATION_PROOF_CERTIFICATE_FREEZE_20260812.json"
AUTHORIZATION = PNP / "09_trace/O9d12a2a1b_C047_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json"
CHRONOLOGY = PNP / "09_trace/O9d12a2a1b_C047_PUBLIC_FREEZE_CHRONOLOGY_20260812.json"
EVALUATOR = PNP / "05_falsification/c047_orientation_feasibility_evaluator.py"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _digest(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_c047_certificate_is_exactly_bound_to_public_candidate() -> None:
    candidate = _load(CANDIDATE)
    certificate = _load(CERTIFICATE)
    assert certificate["candidate_id"] == candidate["candidate_id"]
    assert certificate["candidate_artifact_hash"] == candidate["artifact_hash"]
    assert certificate["source_identity"]["candidate_public_freeze_commit"] == "e033df7a4f0276abb218027451754695679ec288"
    assert certificate["source_identity"]["candidate_raw_sha256"] == hashlib.sha256(CANDIDATE.read_bytes()).hexdigest()
    subject = dict(certificate)
    subject["artifact_hash"] = ""
    assert certificate["artifact_hash"] == _digest(subject)


def test_c047_hand_derivation_covers_all_frozen_obligations_and_cases() -> None:
    certificate = _load(CERTIFICATE)
    assert {item["obligation_id"] for item in certificate["obligations"]} == {
        "DEFINE_ORIENTATION_ONLY_FAMILIES",
        "EXHAUSTIVE_ROW_SUPPORT_TRICHOTOMY",
        "DECODER_BRANCH_TO_FRESH_ROW_FORMS",
        "BINARY_HEADER_DISJOINTNESS",
        "MIRROR_AND_TWO_SIDED_CONCLUSION",
    }
    assert all(item["status"] == "PROVED" for item in certificate["obligations"])
    proof = " ".join(step["derivation"] for step in certificate["proof_steps"])
    assert "all-zero" in proof
    assert "1111" in proof and "1110" in proof
    assert "TWO_SIDED" in proof
    assert certificate["scope_boundary"]["literal_matrix_transpose"] is False


def test_c047_authorization_binds_exact_certificate_and_evaluator() -> None:
    certificate = _load(CERTIFICATE)
    authorization = _load(AUTHORIZATION)
    assert authorization["certificate_artifact_hash"] == certificate["artifact_hash"]
    assert authorization["evaluator_raw_sha256"] == hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    assert authorization["token"] == "C047-ORIENTATION-PROOF-CHECK-AUTHORIZED-AFTER-PUBLIC-FREEZE"
    subject = dict(authorization)
    subject["artifact_hash"] = ""
    assert authorization["artifact_hash"] == _digest(subject)


def test_c047_chronology_precedes_proof_and_preserves_target_blindness() -> None:
    chronology = _load(CHRONOLOGY)
    assert chronology["pre_candidate_public_at"] < chronology["candidate_evaluator_public_at"] < chronology["proof_certificate_frozen_at"]
    assert chronology["later_target_result_accessed"] is False
    assert chronology["finite_target_enumerated"] is False
    assert chronology["assurance_only_zero_math_credit"] is True


def test_c047_certificate_preserves_authority_boundary() -> None:
    certificate = _load(CERTIFICATE)
    assert certificate["authority"] == {
        "same_context_hand_derivation": True,
        "theorem_truth": False,
        "formal_proof": False,
        "independent_review": False,
        "novelty": False,
        "cover_or_circuit_lower_bound": False,
        "p_vs_np_authority": False,
        "root_status": "OPEN",
    }
    assert certificate["target_access"]["later_target_result_accessed"] is False
