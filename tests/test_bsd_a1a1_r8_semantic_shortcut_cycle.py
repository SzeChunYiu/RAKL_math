import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"
M = BSD / "07_memory"
S = BSD / "00_sources" / "BSD_A1a1_R8_SOURCE_FAMILY_AUDIT_20260812.json"
EP = M / "BSD_A1a1_R8_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
DIAG = M / "BSD_A1a1_R8_DIAGNOSIS_SHADOW_20260812.json"
FAIL = M / "BSD_A1a1_R8_SOURCE_FAMILY_FAILURE_SHADOW_20260812.json"
REVIEW = M / "BSD_A1a1_R8_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json"
METRICS = M / "BSD_A1a1_RAKL_CYCLE_METRICS_20260812_R8.json"
TRACE = BSD / "09_trace" / "BSD_A1a1_R8_RESULT_TRACE_DELTA_20260812.json"
CASE = M / "RAKL_METHOD_CASE_STUDY_BSD_A1a1_SEMANTIC_SHORTCUT_20260812_R8.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(obj):
    payload = dict(obj)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_r8_packet_exists_and_metrics_hash_is_valid():
    for path in [S, EP, DIAG, FAIL, REVIEW, METRICS, TRACE, CASE]:
        assert path.exists(), path
    metrics = load(METRICS)
    assert metrics["artifact_hash"] == canonical_hash(metrics)


def test_semantic_shortcut_is_fail_closed_without_lift_authority():
    review_packet = load(REVIEW)
    review = review_packet["review"]
    memory = review_packet["transformation_memory"]
    expected_memory_payload = {
        "memory_id": memory["memory_id"],
        "source_universe": memory["source_universe"],
        "episodes": memory["episodes"],
        "evidence_pointers": memory["evidence_pointers"],
    }
    encoded = json.dumps(expected_memory_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert memory["snapshot_hash"] == hashlib.sha256(encoded).hexdigest()
    assert memory["episodes"] == []
    assert review["direct_search_status"] == "NO_VIABLE_MATCH"
    assert review["selected_mode"] == "CANNOT_CHECK"
    assert review["exhaustion_witness"] is None
    assert review["missing_transformation_specification"] is None
    assert review_packet["audit_expectation"]["candidate_route_ready"] is False
    assert "no cross-problem coverage receipt" in " ".join(review["unresolved_warnings"])


def test_episode_diagnosis_failure_and_obstruction_remain_distinct():
    episode = load(EP)
    diagnosis = load(DIAG)
    failure = load(FAIL)
    assert episode["episode_id"] == "EP-BSD-A1A1-SEMANTIC-SHORTCUT-SOURCE-FAMILY-20260812-R8"
    assert diagnosis["episode_id"] == episode["episode_id"]
    assert failure["episode_id"] == episode["episode_id"]
    assert failure["diagnosis_id"] == diagnosis["diagnosis_id"]
    assert diagnosis["existing_obstruction_reused"] == "BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE"
    assert diagnosis["new_obstruction_promoted"] is False
    assert failure["mathematical_status"] == "OPEN_RELATION_NOT_IMPOSSIBILITY"
    assert failure["local_mathematical_failure"] is False
    assert failure["gluing_failure"] is True


def test_source_family_audit_does_not_reverse_premises():
    source = load(S)
    assert source["coverage_claim"] == "BOUNDED_ONLY_NOT_COMPLETE"
    assert source["candidate_generated"] is False
    assert source["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert len(source["sources"]) == 4
    assert all(item["route_verdict"].startswith("REJECT_AS_") or item["route_verdict"].startswith("RETAIN_AS_") for item in source["sources"])
    assert any(item["id"] == "arXiv:2312.09301" and "Main Conjecture" in item["verified_claim"] for item in source["sources"])
    assert any(item["id"] == "arXiv:2409.11966" and "p-localization" in item["verified_claim"] for item in source["sources"])


def test_metrics_cover_all_seven_axes_and_no_authority_promotion():
    metrics = load(METRICS)
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert set(metrics["saturation_axes"]) == set(metrics["retained_semantic_novelty"])
    assert metrics["raw_repository_growth_is_learning"] is False
    assert metrics["outcome"]["candidate_generated"] is False
    assert metrics["gates"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gates"]["independent_mathematical_review_credit"] == 0
    assert metrics["gates"]["scientific_authority_promotion"] == "NOT_INVOKED"
    assert metrics["gates"]["lift_gate"] == "BLOCKED_NO_CROSS_PROBLEM_COVERAGE_RECEIPT"
    assert metrics["rakl_action_effect"]["changed_observable_pre_memory_pre_gate_preference"].startswith("CANNOT_MEASURE")


def test_trace_extends_r7_hash_chain_and_stays_open():
    trace = load(TRACE)
    assert trace["base_last_event_id"] == "BSD-A1a1-E26-R7-REVIEW"
    assert trace["base_last_event_hash"] == "sha256:be71bb36fdb30705154c45e1f6873bfb7fd7b401972e66ecf2c701a6ff18cac8"
    previous = trace["base_last_event_hash"]
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        previous = entry["artifact_hash"]
    assert trace["entries"][-1]["outputs"] == [
        "ROOT_STATE_OPEN_NO_SOLUTION_CERTIFICATE",
        "CANDIDATE_GENERATED_FALSE",
        "RETAINED_NOVELTY_K1_E1_R1",
    ]
