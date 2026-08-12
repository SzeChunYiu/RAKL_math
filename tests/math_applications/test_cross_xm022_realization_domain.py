import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/cross_problem"
FIBRE = BASE / "01_frontier/XM022_NS_HODGE_REALIZATION_DOMAIN_CONTEXT_FIBRE_20260812.json"
CANDIDATE = BASE / "04_candidates/XM022_NS_HODGE_REALIZATION_DOMAIN_AUTHORITY_CALIBRATION_20260812.json"
EPISODE = BASE / "07_memory/XM022_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
BOUNDARY = BASE / "07_memory/XM022_DIAGNOSIS_FAILURE_LESSON_20260812.json"
TRACE = BASE / "09_trace/XM022_HASH_CHAINED_TRACE_20260812.json"


def load(path):
    return json.loads(path.read_text())


def canonical_hash(obj):
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def test_xm022_frozen_subjects_and_hash_binding():
    fibre = load(FIBRE)
    candidate = load(CANDIDATE)
    episode = load(EPISODE)
    assert fibre["framework"]["main_sha"] == "1b866dc5aafc7e952f4de5acaa75bd3f7b71048e"
    assert fibre["framework"]["method_version"] == "3.0.0"
    assert fibre["application"]["base_main_sha"] == "3871283cfe5040801b174e25b045e05ee0228cc2"
    assert canonical_hash(fibre) == "sha256:59e095475e9660da1f7eb4575e3ccae72fdd9abd3a65aa64d6f6c988d8184766"
    assert candidate["fibre_snapshot_hash"] == canonical_hash(fibre)
    assert canonical_hash(candidate) == "sha256:81c7412e8cd500a538bd3f1426744509a773bd5f261ba4932aea0ee8873f0feb"
    assert episode["candidate_artifact_hash"] == canonical_hash(candidate)
    assert canonical_hash(episode) == "sha256:9544d7e3c6716638265502a4cff36ed1d4ce25c01588f335131d04e25a63a72e"


def test_current_v3_realization_domain_scope_is_fail_closed():
    candidate = load(CANDIDATE)
    audit = candidate["current_v3_operational_gate_audit"]
    src = audit["source_scoped_witness"]
    tgt = audit["target_scoped_witness"]
    assert src["realization_domain"] == "TARGET_DOMAIN"
    assert src["expected_and_observed_gate_verdict"] == "ACCEPTED_TARGET_DOMAIN"
    assert src["may_certify_target_obligation_weakening"] is True
    assert "does not certify" in src["scope_limit"]
    assert tgt["realization_domain"] == "AMBIENT_REPRESENTATION"
    assert tgt["expected_and_observed_gate_verdict"] == "REPRESENTATION_ONLY"
    assert tgt["may_certify_target_obligation_weakening"] is False
    assert audit["literal_cross_problem_authority_transfer"]["verdict"] == "BLOCKED_NO_TARGET_REALIZATION_WITNESS"


def test_episode_diagnosis_failure_lesson_are_separate_and_nonpromoting():
    boundary = load(BOUNDARY)
    ids = {
        boundary["episode"]["id"],
        boundary["diagnosis"]["id"],
        boundary["failure"]["id"],
        boundary["lesson"]["id"],
    }
    assert len(ids) == 4
    assert boundary["obstruction"]["new_id"] is None
    assert boundary["lesson"]["authority"] == "PROPOSAL_ONLY_NOT_ADMITTED"
    assert boundary["failure"]["not_a_blacklist"]


def test_trace_hash_chain():
    trace = load(TRACE)
    previous = "GENESIS"
    for event in trace["events"]:
        assert event["previous_event_hash"] == previous
        material = {k: v for k, v in event.items() if k != "event_hash"}
        assert event["event_hash"] == canonical_hash(material)
        previous = event["event_hash"]
    assert trace["final_hash"] == previous


def test_no_root_or_independent_review_authority():
    candidate = load(CANDIDATE)
    episode = load(EPISODE)
    assert candidate["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert candidate["outcome"]["root_status"] == "ALL_SIX_OPEN_NO_SOLUTION_CERTIFICATE"
    assert candidate["expert_cell"]["independence"] == "SAME_CONTEXT_ONLY_0_OF_3_INDEPENDENT_MATHEMATICAL_REVIEW"
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["independent_mathematical_review_credit"] == "0/3"
