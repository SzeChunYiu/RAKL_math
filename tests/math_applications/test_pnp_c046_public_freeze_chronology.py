from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / (
    "research/real_math/millennium/p_vs_np/09_trace/"
    "O9d12a2a1b_C046_PUBLIC_FREEZE_CHRONOLOGY_20260812.json"
)


def _load() -> dict:
    value = json.loads(RECEIPT.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(document: dict) -> str:
    subject = copy.deepcopy(document)
    subject["artifact_hash"] = ""
    raw = json.dumps(
        subject, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_c046_public_freeze_binds_exact_remote_chronology_without_evaluation() -> None:
    receipt = _load()
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    assert receipt["application_base_commit"] == "ac8c0745be8aed791a446fd55fcf5154cac01962"
    assert receipt["pre_candidate_freeze"] == {
        "commit": "538d689390fb60d30cba31863c1b73cc1716036e",
        "committed_at": "2026-08-12T02:16:58Z",
        "publicly_visible_in_pr": 244,
    }
    assert receipt["candidate_freeze"] == {
        "commit": "c76177457d6c75189b7cc80a3ccc012cb9f1e655",
        "committed_at": "2026-08-12T02:21:02Z",
        "parent": "538d689390fb60d30cba31863c1b73cc1716036e",
        "publicly_visible_in_pr": 244,
    }
    assert receipt["pull_request"] == {
        "number": 244,
        "url": "https://github.com/SzeChunYiu/RAKL_math/pull/244",
        "created_at": "2026-08-12T02:23:07Z",
        "state_at_observation": "OPEN",
        "head_ref": "research/pnp-c046-canonical-collision-freeze-20260812",
        "head_sha_at_observation": "c76177457d6c75189b7cc80a3ccc012cb9f1e655",
        "base_ref": "main",
    }
    assert receipt["chronology_verdict"] == (
        "PRE_CANDIDATE_PARENT_PRECEDES_CANDIDATE; BOTH_PUBLIC_BEFORE_ANY_EVALUATION"
    )
    assert receipt["target_boundary"] == {
        "target_decoder_imported_or_executed": False,
        "candidate_evaluator_imported_or_executed": False,
        "later_target_enumerated": False,
        "later_target_result_accessed": False,
        "finite_collision_level_selected": False,
    }
    assert receipt["authority"] == {
        "assurance_only": True,
        "mathematical_saturation_credit": False,
        "mathematical_result_credit": False,
        "theorem_truth": False,
        "independent_review": False,
        "p_vs_np_authority": False,
        "root_status": "OPEN",
    }
