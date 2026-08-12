from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "real_math" / "millennium" / "cross_problem"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text())


def test_xm021_shadow_episode_uses_current_raw_hash_contract() -> None:
    path = BASE / "07_memory" / "XM021_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
    episode = json.loads(path.read_text())
    expected = episode.pop("artifact_hash")
    payload = json.dumps(episode, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert hashlib.sha256(payload).hexdigest() == expected
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"


def test_xm021_outer_laguerre_ratio_falsifier_calibration() -> None:
    for n in range(2, 17):
        u = 2 * n * (n - 1)
        first = [k * (k + 1) / ((n - k) * u) for k in range(1, n)]
        assert max(first) <= 0.5
        if n >= 3:
            derivative = [k * (k + 2) / ((n - k - 1) * u) for k in range(1, n - 1)]
            assert max(derivative) < 0.5


def test_xm021_dyadic_growth_inequality_calibration() -> None:
    def f(u: float) -> float:
        return u ** (3.0 / 5.0) / math.log(u) ** (1.0 / 5.0)

    for u in (6.0, 12.0, 100.0, 10_000.0):
        assert f(2 * u) >= math.sqrt(2.0) * f(u)


def test_xm021_authority_and_metrology_boundaries() -> None:
    candidate = _load("04_candidates/XM021_RH_ANA_003h_OUTER_LAGUERRE_QUADRATIC_CUTOFF_20260812.json")
    metrics = _load("10_study_pattern/RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM021_20260812.json")
    assert candidate["outcome"] == "MATERIAL_ROUTE_REOPENING_PARTIAL_SUCCESS"
    assert "NO_RH_THEOREM" in candidate["authority"]
    assert candidate["local_to_global"]["gluing"] == "OPEN"
    assert metrics["RAKL_CYCLE_METRICS"]["retained_semantic_novelty_protected"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert metrics["RAKL_CYCLE_METRICS"]["rakl_changed_observable_action"] is True
