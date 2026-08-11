import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"


def _load(rel):
    return json.loads((BSD / rel).read_text())


def test_r8_fibre_and_source_scope_are_proposal_only():
    fibre = _load("01_frontier/BSD_A1a1_R8_CURRENT_RANK2_CLAIM_PARITY_CONTEXT_FIBRE_20260812.json")
    src = _load("00_sources/BSD_A1a1_R8_CURRENT_RANK2_CLAIM_PARITY_SOURCE_RECEIPT_20260812.json")
    assert fibre["packet_hash"] == "sha256:6d2e1fc36ff8863db99e826fc5f6f9609a1b5c8733968dfb1fa88207e5cb8b2e"
    assert fibre["application_snapshot"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert "NO_ROOT_AUTHORITY" in fibre["authority"]
    assert src["source_bound_result"]["status"] == "CLAIM_ROUTE_REFUTED_AT_FOUNDATIONAL_SIGN_PARTITION"
    assert "does not refute BSD" in src["source_bound_result"]["scope"]


def test_r8_episode_diagnosis_failure_obstruction_are_distinct():
    ep = _load("07_memory/BSD_A1a1_R8_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode")
    d = _load("07_memory/BSD_A1a1_R8_DIAGNOSIS_SHADOW_20260812.json")
    f = _load("07_memory/BSD_A1a1_R8_ROOT_NUMBER_PARITY_FAILURE_SHADOW_20260812.json")
    o = _load("07_memory/BSD_A1a1_R8_CURRENT_CLAIM_OBSTRUCTION_SHADOW_20260812.json")
    assert ep["episode_id"].startswith("EP-")
    assert d["id"].startswith("D-") and d["episode_id"] == ep["episode_id"]
    assert f["id"].startswith("F-") and f["diagnosis_id"] == d["id"]
    assert o["id"].startswith("O-") and o["failure_id"] == f["id"]
    assert len({ep["episode_id"], d["id"], f["id"], o["id"]}) == 4


def test_r8_trace_hash_chain_is_recomputable():
    trace = _load("09_trace/BSD_A1a1_R8_RESULT_TRACE_DELTA_20260812.json")
    prev = trace["base_last_event_hash"]
    for event in trace["entries"]:
        assert event["previous_event_hash"] == prev
        artifact_hash = event["artifact_hash"]
        body = dict(event)
        body.pop("artifact_hash")
        actual = "sha256:" + hashlib.sha256(
            json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        assert actual == artifact_hash
        prev = artifact_hash


def test_r8_method_case_study_has_all_seven_axes_and_no_independent_credit():
    text = (BSD / "07_memory/RAKL_METHOD_CASE_STUDY_BSD_A1a1_CURRENT_RANK2_CLAIM_PARITY_20260812_R8.md").read_text()
    for axis in ["KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD"]:
        assert axis in text
    review = (BSD / "08_reviews/BSD_A1a1_R8_PROSPECTIVE_EXPERT_REVIEW_20260812.md").read_text()
    assert "independent_mathematical_review_credit = 0" in review
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in review
