import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "real_math" / "millennium" / "cross_problem"


def load(rel):
    return json.loads((BASE / rel).read_text())


def test_xm012_shadow_episode_and_hash_contract():
    p = BASE / "07_memory" / "XM012_CURRENT_V3_TASK_EPISODE_SHADOW_20260811.taskepisode"
    ep = json.loads(p.read_text())
    assert ep["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert ep["outcome"] == "PARTIAL_SUCCESS"
    assert "RH-ANA-003a-TRIANGULAR_RENORMALIZATION_UNIFORMITY" in ep["residual_signature"]
    content = {k: ep[k] for k in (
        "episode_id", "task_id", "atom_id", "context_hash", "problem_signature",
        "fibre_snapshot_hash", "operator_ids", "action_trace", "observation_ids",
        "verification_ids", "outcome", "residual_signature", "evidence_pointers",
        "timestamp", "cost", "storage_admission",
    )}
    raw = json.dumps(content, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert hashlib.sha256(raw).hexdigest() == ep["artifact_hash"]


def test_xm012_transfer_has_required_difference_witness_and_rejects_overtransfer():
    r = load("01_frontier/XM012_ENDPOINT_ANCHOR_OVERTRANSFER_FALSIFIER_20260811.json")
    t = r["transfer"]
    for k in (
        "source_atom", "target_atom", "common_abstraction", "enabling_assumptions",
        "disanalogies", "predicted_principle", "cheapest_falsifier", "difference_witness",
    ):
        assert t[k]
    assert t["difference_witness"]["verdict"].startswith("The offset pair is not two admissible worlds")
    assert r["episode_outcome"]["target_residual_unchanged"] == "RH-ANA-003a-TRIANGULAR_RENORMALIZATION_UNIFORMITY"
    assert r["episode_outcome"]["root_certificates"] == 0


def test_xm012_episode_diagnosis_lesson_are_distinct_and_unpromoted():
    m = load("07_memory/XM012_DIAGNOSIS_FAILURE_LESSON_SHADOW_20260811.json")
    ids = {
        m["episode_reference"]["episode_id"],
        m["diagnosis"]["diagnosis_id"],
        m["failure"]["failure_id"],
        m["candidate_lesson"]["lesson_id"],
        m["motif"]["motif_id"],
    }
    assert len(ids) == 5
    assert m["obstruction"]["new_obstruction_id"] is None
    assert not m["candidate_lesson"]["retained_as_protected_learning"]


def test_xm012_current_work_coverage_fails_closed():
    c = load("09_trace/XM012_CURRENT_WORK_COVERAGE_OBSERVATION_20260811.json")
    assert c["coverage_semantics"] == "SAMPLED_SUBSET"
    assert c["current_work_binding_status"] == "CURRENT_WORK_NOT_BOUND"
    assert c["observed_open_counts"]["issues"] == 32
    assert c["observed_open_counts"]["pull_requests"] == 58
    assert all(not v for v in c["authority"].values())


def test_xm012_metrics_count_semantic_novelty_not_repository_growth():
    m = load("09_trace/RAKL_CYCLE_METRICS_XM012_20260811.json")
    assert m["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert m["raw_repository_growth_is_learning"] is False
    assert m["gates"]["independent_mathematical_review_credit"] == 0
    assert m["gates"]["scientific_authority_promotion"] == "NOT_INVOKED"


def test_xm012_case_study_preserves_six_lane_measurement_gaps():
    c = load("10_study_pattern/RAKL_METHOD_CASE_STUDY_XM012_20260811.json")
    assert len(c["lane_summaries"]) == 6
    pnp = next(x for x in c["lane_summaries"] if x["lane"] == "P_vs_NP")
    rh = next(x for x in c["lane_summaries"] if x["lane"] == "Riemann_Hypothesis")
    assert str(pnp["retained_semantic_novelty"]).startswith("CANNOT_MEASURE")
    assert str(rh["retained_semantic_novelty"]).startswith("CANNOT_MEASURE")
    assert c["framework_improvement_hypothesis"]["issue_opened"] is False
