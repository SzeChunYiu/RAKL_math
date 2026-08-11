import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/real_math/millennium/cross_problem/07_memory/XM011_CURRENT_WORK_COVERAGE_PACKET_20260811_R7.json"
METRICS = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_CYCLE_METRICS_XM011_20260811_R7.json"
CASE_STUDY = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_METHOD_CASE_STUDY_XM011_20260811_R7.md"


def load(path: Path):
    return json.loads(path.read_text())


def test_xm011_episode_is_shadow_only_and_transfer_is_typed():
    packet = load(PACKET)
    assert packet["authority"].startswith("PROPOSAL_SHADOW_ONLY")
    episode = packet["task_episode"]
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert packet["transfer"]["source_atom"].startswith("H4d1c")
    assert packet["transfer"]["target_atom"].startswith("RH-ANA-003")
    witness = packet["transfer"]["difference_witness"]
    assert "#118" in witness and "#147" in witness
    assert "coverage failure only" in witness
    assert packet["failure"]["class"] == ["retrieval", "decomposition", "meta-policy"]
    assert "math" in packet["failure"]["not_class"]


def test_xm011_trace_is_hash_linked_without_promoting_authority():
    packet = load(PACKET)
    trace = packet["trace"]
    previous = trace["genesis_hash"]
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"].startswith("sha256:")
        previous = event["artifact_hash"]
    assert trace["final_event_hash"] == previous
    assert packet["obstruction"]["retained_novelty_counted"] is False
    assert packet["lesson"]["authority"] == "CANDIDATE_PROPOSAL_ONLY"
    assert packet["motif"]["authority"] == "PROPOSAL_SHADOW_ONLY"


def test_xm011_metrics_are_conservative_and_complete_on_seven_axes():
    receipt = load(METRICS)["RAKL_CYCLE_METRICS"]
    novelty = receipt["retained_semantic_novelty"]
    assert {k: novelty[k] for k in ("KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD")} == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    aggregate = receipt["cross_lane_aggregates"]["retained_novelty_lower_bound_five_comparable_lanes"]
    assert aggregate == {
        "KNOWLEDGE": 4,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 3,
        "OBSTRUCTION": 3,
        "RELATION": 5,
        "PATH": 4,
        "META_METHOD": 0,
    }
    assert receipt["cross_lane_aggregates"]["confirmed_repeated_current_work_coverage_failure_occurrences"] == 2
    assert str(receipt["cross_lane_aggregates"]["repeated_failure_rate"]).startswith("CANNOT_MEASURE")
    assert str(receipt["lane_summaries"]["PNP_PR152"]["fibre_hash"]).startswith("CANNOT_MEASURE")
    assert receipt["gate_provenance_ci"]["all_six_millennium_roots"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert receipt["gate_provenance_ci"]["independent_mathematical_reviews"] == "0/3"


def test_xm011_case_study_preserves_failure_and_gluing_separation():
    text = CASE_STUDY.read_text()
    assert "retrieval/decomposition/meta-policy" in text
    assert "not math" in text
    assert "zero independent-review credit" in text
    assert "local-success/global-gluing-failure" in text
    assert "RAKL#239" in text
