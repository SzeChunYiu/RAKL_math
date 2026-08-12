import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"


def _load(relative):
    return json.loads((YM / relative).read_text())


def test_r14_packet_authority_and_fibre_binding():
    fibre = _load("10_case_study/YM-S1a2d_PRE_CANDIDATE_FIBRE_MEMORY_20260812_R14.json")
    packet = _load("10_case_study/YM-S1a2d_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260812_R14.json")
    episode = packet["TaskEpisode"]
    expected = "sha256:a5d653721edaffb1358834e5c4d6f6f0bf848328ff9ffa5e86e1e9db1358bf79"
    assert fibre["atom"]["issue"] == "#253"
    assert fibre["fibre_hash"] == expected
    assert episode["fibre_hash"] == expected
    assert "PROPOSAL_SHADOW" in episode["authority"]


def test_r14_protected_novelty_and_reviews_remain_zero():
    metrics = _load("10_case_study/YM-S1a2d_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260812_R14.json")["RAKL_CYCLE_METRICS"]
    assert all(value == 0 for value in metrics["retained_semantic_novelty"]["protected_authoritative"].values())
    assert metrics["gate_provenance_ci"]["protected_authority_transition"] == "NONE"
    assert metrics["gate_provenance_ci"]["independent_mathematical_reviews"] == "0/3"


def test_r14_trace_links_and_residual():
    trace = _load("09_trace/YM-S1a2d_RESEARCH_TRACE_20260812_R14.json")
    events = trace["events"]
    assert events[0]["previous_event_hash"] == ""
    for left, right in zip(events, events[1:]):
        assert right["previous_event_hash"] == left["event_hash"]
    assert trace["trace_final_hash"] == events[-1]["event_hash"]
    packet = _load("10_case_study/YM-S1a2d_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260812_R14.json")
    assert packet["TaskEpisode"]["residual_after"] == "RES-YM-S1a2d-INFINITE-VOLUME-OS-NULL-QUOTIENT-ONE-STEP-TRANSFER-REALIZATION-PLUS-DENSITY-AUTHORITY-AND-CONTINUUM-UNBOUND"


def test_r14_candidate_marks_operator_and_root_boundaries():
    text = (YM / "04_candidates/YM-S1a2d_C001_OS_REFLECTED_CORRELATION_COMMON_RATE_20260812_R14.md").read_text()
    assert "NO_OPERATOR_REALIZATION" in text
    assert "It is not yet a statement about powers of an infinite-volume physical transfer operator" in text
    assert "Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`" in text
