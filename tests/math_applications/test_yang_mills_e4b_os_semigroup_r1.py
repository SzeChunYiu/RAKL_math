import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FIBRE = YM / "01_frontier/YM-E4b_CONTEXT_FIBER_20260811_R1.json"
EPISODE = YM / "07_memory/YM-E4b_V3_TASK_EPISODE_20260811_R1.json"
TRACE = YM / "09_trace/YM-E4b_RESEARCH_TRACE_20260811_R1.json"
SOURCE = YM / "03_sources/YM_E4b_OS_SEMIGROUP_VARYING_HILBERT_AUDIT_20260811_R1.md"
CASE = YM / "10_case_study/YM-E4b_RAKL_METHOD_CASE_STUDY_20260811_R1.md"


def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def test_fibre_snapshot_hash_is_content_bound():
    obj = json.loads(FIBRE.read_text())
    got = obj.pop("fibre_snapshot_hash")
    assert got == "sha256:" + hashlib.sha256(_canon(obj)).hexdigest()


def test_task_episode_artifact_hash_is_content_bound():
    obj = json.loads(EPISODE.read_text())
    got = obj.pop("artifact_hash")
    assert got == hashlib.sha256(_canon(obj)).hexdigest()
    assert len(got) == 64 and got == got.lower()


def test_trace_is_hash_chained():
    obj = json.loads(TRACE.read_text())
    prev = "0" * 64
    for event in obj["events"]:
        assert event["prev_hash"] == prev
        got = event["event_hash"]
        payload = dict(event)
        payload.pop("event_hash")
        assert got == hashlib.sha256(_canon(payload)).hexdigest()
        prev = got
    assert obj["terminal_hash"] == prev


def test_nonzero_positive_energy_makes_os_semigroup_nonisometric():
    # Regression witness only; the proof in the source audit uses the spectral theorem.
    t = 1.0
    positive_energy = 1.0
    squared_norm_factor = math.exp(-2.0 * t * positive_energy)
    assert 0.0 < squared_norm_factor < 1.0


def test_local_result_does_not_escalate_root_authority():
    source = SOURCE.read_text()
    case = CASE.read_text()
    assert "PARTIAL_LOCAL_RESULT" in source
    assert "changing-Hilbert-space OS identification certificate is still missing" in source
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in source
    assert "OPERATOR = 0" in case
    assert "OBSTRUCTION = 0" in case
    assert "META_METHOD = 0" in case
    assert "No protected lesson/tool/framework/root promotion is attempted" in case
