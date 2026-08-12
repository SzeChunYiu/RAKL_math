from __future__ import annotations

from datetime import datetime
from hashlib import sha256
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"
PRE = NS / "09_trace/NS-B2a1a3_PRE_CANDIDATE_PACKET_20260812.json"
EXP = NS / "07_memory/NS-B2a1a3_EXPERIENCE_DELTA_20260812.json"
RESULT = NS / "01_frontier/NS-B2a1a3_ONE_SCALE_LOG_WEIGHT_OBSTRUCTION_20260812.md"
METRICS = NS / "10_case_study/NS-B2a1a3_RAKL_CASE_METRICS_20260812.json"


def _hash(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + sha256(encoded).hexdigest()


def _dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def test_frozen_fibre_and_hash_chain_are_content_bound() -> None:
    packet = json.loads(PRE.read_text())
    assert packet["framework"]["method_version"] == "3.0.0"
    assert packet["application"]["base_sha"] == "21d22075fa250e4ded412fd292b7942b87503266"
    assert _hash(packet["fibre_snapshot"]) == packet["fibre_snapshot_hash"]
    entries = packet["research_trace"]["entries"]
    assert [e["event_type"] for e in entries][-1] == "NEXT_STEP_PROPOSED"
    for i, entry in enumerate(entries):
        assert entry["previous_event_hash"] == ("" if i == 0 else entries[i - 1]["artifact_hash"])
        body = dict(entry)
        observed = body.pop("artifact_hash")
        assert _hash(body) == observed
    assert all(_dt(entries[i]["timestamp"]) < _dt(entries[i + 1]["timestamp"]) for i in range(len(entries) - 1))


def test_radius_outgrows_fixed_finite_log_gain_on_registered_calibration() -> None:
    # Calibration only, not proof: the proof in the result file is the logarithmic asymptotic.
    for gamma in (0.5, 1.0, 2.0):
        for beta in (2.0, 9.0 / 4.0, 25.0 / 12.0, 3.0):
            logs = []
            for k in (10, 20, 50):
                L = float(k * k)
                h = float(k)
                logs.append((L - h) - beta * gamma * math.log(L / h))
            assert logs[0] < logs[1] < logs[2]
            assert logs[-1] > 100.0


def test_episode_diagnosis_obstruction_lesson_remain_distinct_and_shadow_only() -> None:
    doc = json.loads(EXP.read_text())
    assert doc["episode"]["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert doc["episode"]["episode_id"] == "E-NS-B2a1a3-R1"
    assert doc["diagnosis"]["id"] == "D-NS-B2a1a3-R1"
    assert doc["obstruction"]["id"] == "O-NS-B2a1a3-RADIUS-VS-LOG-WEIGHT"
    assert doc["lesson"]["lesson_id"] == "L-NS-B2a1a3-RESTORE-GEOMETRIC-SCALE-FIRST"
    assert doc["lesson"]["authority"] == "CANDIDATE"
    assert doc["authority"] == "PROPOSAL_SHADOW_ONLY"


def test_case_metrics_have_explicit_seven_axis_vector_and_open_root() -> None:
    doc = json.loads(METRICS.read_text())
    m = doc["RAKL_CYCLE_METRICS"]
    assert set(m["retained_semantic_novelty"]) == {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD"
    }
    assert m["retained_semantic_novelty"]["OPERATOR"] == 0
    assert m["retained_semantic_novelty"]["META_METHOD"] == 0
    assert m["gates"]["root_promotion"] == "BLOCKED_OPEN"
    assert m["authority"] == "PROPOSAL_SHADOW_ONLY"
    text = RESULT.read_text()
    assert "A diverging upper bound is not a lower bound" in text
    assert "NS0 = OPEN_NO_SOLUTION_CERTIFICATE" in text
