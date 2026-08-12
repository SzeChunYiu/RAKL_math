from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"
CANDIDATE = BASE / "04_candidates/YM_S1A1_C001_DENSE_COMMON_RATE_SPECTRAL_EXCLUSION_20260811.md"
REVIEW = BASE / "08_reviews/YM-S1A1-C001_RESULT_REVIEW_20260811.md"
TRACE = BASE / "09_trace/YM-S1A1-C001_RESULT_TRACE_20260811.json"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _moment(diagonal: tuple[float, ...], vector: tuple[float, ...], n: int) -> float:
    return sum((x * x) * (lam**n) for lam, x in zip(diagonal, vector, strict=True))


def test_hidden_state_world_requires_density_repair() -> None:
    diagonal = (0.5, 0.25)
    tested = (0.0, 1.0)
    for n in (4, 16, 64):
        rate = _moment(diagonal, tested, n) ** (1.0 / n)
        assert abs(rate - 0.25) < 1e-12
    assert max(diagonal) == 0.5
    text = CANDIDATE.read_text(encoding="utf-8")
    assert "D=span{e_2}" in text
    assert "not dense" in text
    assert "F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE" in text


def test_dense_spanning_world_recovers_slowest_rate() -> None:
    diagonal = (0.5, 0.25)
    e1 = (1.0, 0.0)
    e2 = (0.0, 1.0)
    for n in (4, 16, 64):
        assert abs(_moment(diagonal, e1, n) ** (1.0 / n) - 0.5) < 1e-12
        assert abs(_moment(diagonal, e2, n) ** (1.0 / n) - 0.25) < 1e-12
    assert max(diagonal) == 0.5


def test_candidate_scope_blocks_root_overclaim() -> None:
    candidate = CANDIDATE.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    assert "SUPPORTED_ABSTRACT_LEMMA / TARGET_BINDING_OPEN" in candidate
    assert "No root promotion is permitted" in candidate
    assert "G5" in candidate and "G6" in candidate and "G7" in candidate
    assert "same-theory OS source binding" in review
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in review


def test_result_trace_continues_pre_candidate_hash_chain() -> None:
    trace = json.loads(TRACE.read_text(encoding="utf-8"))
    assert trace["predecessor_trace_id"].startswith("TRACE-YM-S1A1-PRE-CANDIDATE")
    previous = trace["predecessor_event_hash"]
    assert previous == "sha256:7c93020929cde30bcc7ed92a5300f7e938064655cc24033ce0fe602c12b1edaf"
    event_types = []
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        payload = copy.deepcopy(event)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        previous = artifact_hash
        event_types.append(event["event_type"])
    assert event_types == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]
