import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"


def load_json(relative: str):
    return json.loads((BSD / relative).read_text(encoding="utf-8"))


def canonical_event_hash(event):
    payload = dict(event)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_r9_required_artifacts_exist_and_root_stays_open():
    required = [
        "00_sources/BSD_A1a1_R9_CM_KATZ_ORDER_SOURCE_AUDIT_20260812.json",
        "07_memory/BSD_A1a1_R9_CM_KATZ_ORDER_TASK_EPISODE_SHADOW_20260812.taskepisode",
        "07_memory/BSD_A1a1_R9_CM_KATZ_ORDER_DIAGNOSIS_SHADOW_20260812.json",
        "07_memory/BSD_A1a1_R9_COMPLEX_TO_KATZ_ORDER_FAILURE_SHADOW_20260812.json",
        "07_memory/RAKL_METHOD_CASE_STUDY_BSD_A1a1_CM_KATZ_ORDER_20260812_R9.md",
        "07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260812_R9.json",
        "08_reviews/BSD_A1a1_R9_CM_KATZ_ORDER_PROSPECTIVE_EXPERT_REVIEW_20260812.md",
        "09_trace/BSD_A1a1_R9_CM_KATZ_ORDER_TRACE_DELTA_20260812.json",
    ]
    for relative in required:
        assert (BSD / relative).is_file(), relative

    audit = load_json(required[0])
    episode = load_json(required[1])
    metrics = load_json(required[5])
    assert audit["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert "PROPOSAL_SHADOW" in episode["authority"]
    assert metrics["gates"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["outcome"]["mathematical_candidate_generated"] is False
    assert metrics["outcome"]["root_certificate_generated"] is False


def test_r9_source_audit_does_not_reverse_castella_theorem_c():
    audit = load_json("00_sources/BSD_A1a1_R9_CM_KATZ_ORDER_SOURCE_AUDIT_20260812.json")
    scope = audit["source_scope"]
    assert "ord_{s=1} L_p(s) = 2" in scope["additional_theorem_C_hypotheses"]
    assert "ord_{s=1} L_p^*(s) = 1" in scope["additional_theorem_C_hypotheses"]
    assert audit["bounded_route_cell"]["root_facing_status"] == "MISSING"
    assert audit["bounded_route_cell"]["generic_scope_status"] == "SPECIAL_CM_CELL_ONLY"
    falsifiers = " ".join(audit["falsifiers"])
    assert "p-adic BSD" in falsifiers
    assert "complex" in falsifiers and "p-adic" in falsifiers


def test_r9_episode_diagnosis_failure_obstruction_are_distinct():
    episode = load_json("07_memory/BSD_A1a1_R9_CM_KATZ_ORDER_TASK_EPISODE_SHADOW_20260812.taskepisode")
    diagnosis = load_json("07_memory/BSD_A1a1_R9_CM_KATZ_ORDER_DIAGNOSIS_SHADOW_20260812.json")
    failure = load_json("07_memory/BSD_A1a1_R9_COMPLEX_TO_KATZ_ORDER_FAILURE_SHADOW_20260812.json")
    assert episode["episode_id"] == diagnosis["source_episode_ref"] == failure["source_episode_ref"]
    assert "episode_id" not in diagnosis
    assert "episode_id" not in failure
    assert diagnosis["diagnosis_id"] == failure["diagnosis_id"]
    assert diagnosis["existing_obstruction_reused"] == "BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE"
    assert failure["existing_obstruction"] == "BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE"
    assert "no new protected obstruction" in failure["not_claimed"]


def test_r9_metrics_have_exact_seven_axes_and_zero_unearned_growth():
    metrics = load_json("07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260812_R9.json")
    novelty = metrics["retained_semantic_novelty"]
    assert set(novelty) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert novelty == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert metrics["raw_repository_growth_is_learning"] is False
    assert metrics["new_ids"]["lessons"] == []
    assert metrics["new_ids"]["obstructions"] == []
    assert metrics["new_ids"]["tools"] == []
    assert metrics["new_ids"]["motifs"] == []
    assert metrics["gates"]["independent_mathematical_review_credit"] == 0


def test_r9_metrics_bind_exact_framework_and_fibre():
    metrics = load_json("07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260812_R9.json")
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["framework"]["exact_current_main_sha_at_cycle_sample"] == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert metrics["application"]["base_sha"] == "ac8c0745be8aed791a446fd55fcf5154cac01962"
    assert metrics["active_atom"]["fibre_snapshot_hash"] == "sha256:1169325f3cc17acc2094488809bc13ebba796a54aa51bcbc132690c98e1987c9"
    assert metrics["state_fingerprints"]["raw_repository_growth_is_learning"] is False


def test_r9_hash_chain_extends_r8_postdrift_tip():
    trace = load_json("09_trace/BSD_A1a1_R9_CM_KATZ_ORDER_TRACE_DELTA_20260812.json")
    entries = trace["entries"]
    assert trace["base_last_event_id"] == "BSD-A1a1-E31-R8-BOUNDED-LIFT-SPEC"
    assert entries[0]["previous_event_hash"] == trace["base_last_event_hash"]
    assert entries[1]["previous_event_hash"] == entries[0]["artifact_hash"]
    for event in entries:
        assert canonical_event_hash(event) == event["artifact_hash"]


def test_r9_same_context_review_is_not_independent_review():
    review = (BSD / "08_reviews/BSD_A1a1_R9_CM_KATZ_ORDER_PROSPECTIVE_EXPERT_REVIEW_20260812.md").read_text(encoding="utf-8")
    assert "Independent mathematical review credit is **0/3**" in review
    assert "seven-role same-context expert cell" in review
    assert "OPEN_NO_SOLUTION_CERTIFICATE" not in review or "no root" in review.lower()
