import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def test_r7_critical_scale_normalization_identity():
    # R = a * Omega^(-1/2), chi = K/Omega^2.
    for Omega, K, a in [(4.0, 16.0, 0.5), (9.0, 3.0, 2.0), (2.5, 40.0, 5.0)]:
        R = a / math.sqrt(Omega)
        chi = K / (Omega * Omega)
        lhs = Omega**2 * R**2 * min(R**2, Omega / K)
        rhs = a**2 * min(a**2, 1.0 / chi)
        assert math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)


def test_r7_shadow_authority_and_seven_axis_receipt():
    metrics_path = NS / "10_case_study" / "NS-B1a3b1a2b_R7_RAKL_CYCLE_METRICS_20260812.json"
    metrics = json.loads(metrics_path.read_text())
    assert metrics["gate_status"]["root_contract"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_status"]["independent_mathematical_reviews"] == "0/3"
    assert metrics["provenance"]["raw_repository_growth_counts_as_learning"] is False
    proposal = metrics["retained_semantic_novelty_proposal_shadow"]
    protected = metrics["retained_semantic_novelty_protected"]
    expected = {"KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD"}
    assert set(proposal) == expected
    assert set(protected) == expected
    assert all(value == 0 for value in protected.values())


def test_r7_episode_diagnosis_obstruction_are_distinct():
    episode = json.loads((NS / "07_memory" / "NS-B1a3b1a2b_R7_TASK_EPISODE_SHADOW_20260812.json").read_text())
    delta = json.loads((NS / "07_memory" / "NS-B1a3b1a2b_R7_EXPERIENCE_DELTA_20260812.json").read_text())
    assert episode["episode_id"] == "TE-NS-B1a3b1a2b-R7-20260812"
    assert delta["diagnosis"]["id"].startswith("D-")
    assert delta["failure"]["id"].startswith("F-")
    assert delta["obstruction"]["id"].startswith("O-")
    assert delta["candidate_lesson"]["id"].startswith("L-")
    assert len({episode["episode_id"], delta["diagnosis"]["id"], delta["failure"]["id"], delta["obstruction"]["id"], delta["candidate_lesson"]["id"]}) == 5


def test_r7_pre_candidate_trace_has_required_order_and_hash_tail():
    trace_path = NS / "09_trace" / "NS-B1a3b1a2b_R7_PRE_CANDIDATE_TRACE_20260812.jsonl"
    events = [json.loads(line) for line in trace_path.read_text().splitlines() if line.strip()]
    assert [event["event"] for event in events] == [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    for previous, current in zip(events, events[1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    assert events[-1]["artifact_hash"] == "sha256:5c5d884524bdd6c3076fa95092e066e8d4df849c89625824c1e7512eea445bde"
