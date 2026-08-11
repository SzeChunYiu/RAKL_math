import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1c1a1_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260811_R8.json"
FIBRE = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1c1a1_FIBRE_RECEIPT_20260811_R8.json"
AUDIT = ROOT / "research/real_math/millennium/yang_mills/00_sources/YM-S1c1a1_SECTION9_TERMINAL_ANCHOR_AUDIT_20260811_R8.md"


def test_constant_offset_equal_increment_hostile_control():
    a = [2.0 ** (-j) for j in range(1, 12)]
    tail = [sum(a[k:]) for k in range(len(a))]
    A = [1.0 + x for x in tail]
    B = tail
    # On every interval available in the finite calibration, the increments agree.
    dA = [A[k] - A[k + 1] for k in range(len(A) - 1)]
    dB = [B[k] - B[k + 1] for k in range(len(B) - 1)]
    assert dA == dB
    assert all(abs((A[k] - B[k]) - 1.0) < 1e-12 for k in range(len(A)))


def test_r8_receipt_authority_and_seven_axis_metrology():
    data = json.loads(CASE.read_text())
    assert data["authority"] == "PROPOSAL_SHADOW_MEASUREMENT_ONLY_ROOT_AUTHORITY_NONE"
    assert data["TaskEpisode"]["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert data["RAKL_CYCLE_METRICS"]["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    expected = {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 1,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert data["RAKL_CYCLE_METRICS"]["retained_semantic_novelty"] == expected
    assert all(v == 0 for v in data["RAKL_CYCLE_METRICS"]["protected_retained_semantic_novelty"].values())
    assert data["RAKL_METHOD_CASE_STUDY"]["solved_subproblem_novelty_class"]["class"] == "RAKL_TRIVIAL"
    assert data["RAKL_CYCLE_METRICS"]["independent_mathematical_reviews"] == 0


def test_task_episode_content_hash_matches_current_v3_shape():
    data = json.loads(CASE.read_text())
    episode = dict(data["TaskEpisode"])
    claimed = episode.pop("artifact_hash")
    payload = json.dumps(episode, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert hashlib.sha256(payload).hexdigest() == claimed


def test_fibre_and_source_audit_bind_terminal_anchor_residual():
    fibre = json.loads(FIBRE.read_text())
    text = AUDIT.read_text()
    assert fibre["fibre_snapshot_hash"] == "72b95bbc806d50a55d0e2fb34aec7600f3e0b98442edba2738f861c587f49f14"
    assert fibre["chronology"]["r8_specific_durable_receipt"] == "PERSISTED_AFTER_SOURCE_OBSERVATION"
    assert "limsup_{K->infinity}|S_K^A-S_K^B|" in text
    assert "Theorem 9.4 is conditional uniqueness" in text
    assert "#171" in text
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in text
