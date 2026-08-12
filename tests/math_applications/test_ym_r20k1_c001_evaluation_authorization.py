from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
AUTHORIZATION = YM / "09_trace/YM-S1a2i_K1_C001_POST_FREEZE_EVALUATION_AUTHORIZATION_20260812.json"
CANDIDATE = YM / "04_candidates/YM-S1a2i_K1_C001_SCALAR_MARGIN_CANDIDATE_FREEZE_20260812.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_authorization_is_bound_to_the_merged_candidate_and_still_result_blind() -> None:
    authorization = _load(AUTHORIZATION)
    candidate = _load(CANDIDATE)

    assert authorization["candidate_id"] == candidate["candidate_id"]
    assert authorization["candidate_core_sha256"] == candidate["candidate_identity"]["canonical_core_sha256"]
    assert authorization["candidate_artifact_hash"] == candidate["artifact_hash"]
    assert authorization["candidate_freeze_merge"] == "eea2fe72f0c06de3612589be0103d0fff5812a87"
    assert authorization["evaluation_may_begin_only_after_this_authorization_is_merged"] is True
    assert authorization["result_state"] == "UNEVALUATED"
    assert authorization["result_accessed"] is False
    assert authorization["mathematical_result_credit"] is False
    assert authorization["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_authorization_preserves_source_first_order_and_exact_result_branches() -> None:
    authorization = _load(AUTHORIZATION)

    assert authorization["authorized_order"] == [
        "O1-SOURCE-UNIFORMITY",
        "O4-NORM-AND-SCALE-SCOPE",
        "O2-BASE-LOWER-BOUND",
        "O3-SCALAR-EXISTENCE",
        "O5-NEXT-RADIUS-COMPOSITION",
        "FROZEN-FALSIFIER",
        "RESULT-CLASSIFICATION",
    ]
    assert authorization["fail_closed_stop_rules"] == {
        "missing_source_constant_or_uniformity": "SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT",
        "unproved_same_norm_or_scale_scope": "SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT",
        "unavailable_source_evidence": "CANNOT_CHECK",
        "scalar_or_composition_counterexample": "SCALAR_EXISTENCE_OR_COMPOSITION_REFUTED",
    }
    assert authorization["allowed_result_branches"] == [
        "CONDITIONAL_UNIFORM_SCALAR_SLACK_PROVED",
        "SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT",
        "SCALAR_EXISTENCE_OR_COMPOSITION_REFUTED",
        "CANNOT_CHECK",
    ]


def test_authorization_hash_is_recomputed_with_empty_artifact_hash_seal() -> None:
    authorization = _load(AUTHORIZATION)
    claimed = authorization["artifact_hash"].removeprefix("sha256:")
    payload = dict(authorization)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert hashlib.sha256(raw).hexdigest() == claimed

