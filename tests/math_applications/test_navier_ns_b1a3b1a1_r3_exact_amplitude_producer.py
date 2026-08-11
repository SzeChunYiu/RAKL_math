import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"
FIBRE = NS / "01_frontier" / "NS-B1a3b1a1_CONTEXT_FIBER_R3_20260811.json"
DAG = NS / "01_frontier" / "problem_dag_delta_NS-B1a3b1a1_R3_20260811.json"
EPISODE = NS / "07_memory" / "NS-B1a3b1a1_TASK_EPISODE_R3_20260811.json"
EXPERIENCE = NS / "07_memory" / "NS-B1a3b1a1_EXPERIENCE_DELTA_R3_20260811.json"
TRACE = NS / "09_trace" / "NS-B1a3b1a1_RESULT_TRACE_R3_20260811.json"
CASE = NS / "10_case_study" / "NS-B1a3b1a1_C001_R3_RAKL_METHOD_CASE_STUDY_20260811.json"
METRICS = NS / "10_case_study" / "NS-B1a3b1a1_C001_R3_RAKL_CYCLE_METRICS_20260811.json"
RESULT = NS / "04_candidates" / "NS-B1a3b1a1_C001_R3_EXACT_NSE_HIGH_FREQUENCY_PRODUCER_20260811.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def episode_content_hash(ep):
    payload = {
        "episode_id": ep["episode_id"],
        "task_id": ep["task_id"],
        "atom_id": ep["atom_id"],
        "context_hash": ep["context_hash"],
        "problem_signature": ep["problem_signature"],
        "fibre_snapshot_hash": ep["fibre_snapshot_hash"],
        "operator_ids": ep["operator_ids"],
        "action_trace": ep["action_trace"],
        "observation_ids": ep["observation_ids"],
        "verification_ids": ep["verification_ids"],
        "outcome": ep["outcome"],
        "residual_signature": ep["residual_signature"],
        "evidence_pointers": ep["evidence_pointers"],
        "timestamp": ep["timestamp"],
        "cost": ep["cost"],
        "storage_admission": ep["storage_admission"],
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def test_r3_shadow_episode_and_root_authority_are_fail_closed():
    for path in [FIBRE, DAG, EPISODE, EXPERIENCE, TRACE, CASE, METRICS, RESULT]:
        assert path.exists(), path
    episode = load(EPISODE)
    metrics = load(METRICS)
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["artifact_hash"] == episode_content_hash(episode)
    assert metrics["outcome"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["root_promotion_gate"] == "BLOCKED"
    assert metrics["gate_provenance_ci"]["genuinely_isolated_mathematical_reviews"] == "0/3"


def test_episode_diagnosis_obstruction_lesson_are_distinct():
    ex = load(EXPERIENCE)
    ids = {
        ex["episode_ref"]["episode_id"],
        ex["diagnosis"]["diagnosis_id"],
        ex["failure_experience"]["failure_id"],
        ex["obstruction"]["obstruction_id"],
        ex["lesson_candidate"]["lesson_id"],
    }
    assert len(ids) == 5
    assert ex["lesson_candidate"]["authority"] == "CANDIDATE"
    assert len(ex["gluing_failures_separate"]) == 3


def test_same_slab_route_pruned_but_history_child_stays_open():
    dag = load(DAG)
    assert dag["nodes"]["NS-B1a3b1a1"]["resolution"] == "ROUTE_PRUNED_BY_EXACT_NSE_COUNTERFAMILY"
    assert dag["nodes"]["NS-B1a3b1a2"]["status"] == "OPEN"
    assert dag["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    text = RESULT.read_text(encoding="utf-8")
    assert "Pure scaling rejected" in text
    assert "does not enter the Albritton–Barker singular/ancient source family" in text


def test_metrology_has_all_seven_axes_and_no_repo_growth_learning():
    metrics = load(METRICS)
    axes = metrics["retained_semantic_novelty"]
    assert set(axes) == {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION",
        "RELATION", "PATH", "META_METHOD",
    }
    assert metrics["raw_repository_growth_counted_as_learning"] is False
    assert metrics["decision_policy"]["rakl_changed_observable_action_preference"] is True
    assert metrics["outcome"]["novelty_class"] == "representation"


def test_trace_continues_preaction_chain_and_records_positive_time_check():
    trace = load(TRACE)
    assert trace["continues_from"] == "sha256:f5954682d63fe66d88bea70bf90b50b0772377e06cfaf70fc74c011d114041c8"
    assert trace["final_hash"] == "sha256:ab63c88d5d9f58bfe6e12d257b8ebe86ae40283583cc0a61b6561c2a0798de88"
    kinds = [event["kind"] for event in trace["events"]]
    assert "POSITIVE_TIME_VERIFICATION" in kinds
    assert "FINITE_I_VERIFICATION" in kinds
