from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"
CONTEXT = NS / "01_frontier" / "NS-B1a3_CONTEXT_FIBER_20260811.json"
MEMORY = NS / "07_memory" / "NS-B1a3_RESEARCH_MEMORY_REVIEW_20260811.json"
EXPERT = NS / "08_reviews" / "NS-B1a3_EXPERT_CONTEXT_REVIEW_20260811.md"
PRE_TRACE = NS / "09_trace" / "NS-B1a3_PRE_CANDIDATE_TRACE_20260811.json"
RESULT = NS / "01_frontier" / "NS-B1a3_C001_I_PROFILE_MAX_DECOUPLING_20260811.md"
RESULT_REVIEW = NS / "08_reviews" / "NS-B1a3_C001_RESULT_REVIEW_20260811.md"
CONT_TRACE = NS / "09_trace" / "NS-B1a3_C001_TRACE_CONTINUATION_20260811.json"
FAILURE = NS / "07_memory" / "NS-B1a3_C001_FAILURE_EXPERIENCE_DELTA_20260811.json"
EPISODE = NS / "10_case_study" / "NS-B1a3_C001_V3_TASK_EPISODE_20260811.json"
METRICS = NS / "10_case_study" / "NS-B1a3_C001_RAKL_CYCLE_METRICS_20260811.json"
DAG = NS / "02_problem_dag" / "open_obligations.yaml"

PRE_CANDIDATE_SHA = "a5998e1849fe643148f2d3ecf1f4cad9c5e6e334"
RESULT_REL = "research/real_math/millennium/navier_stokes/01_frontier/NS-B1a3_C001_I_PROFILE_MAX_DECOUPLING_20260811.md"


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _event_hash(event: dict[str, object]) -> str:
    unsigned = dict(event)
    unsigned.pop("artifact_hash", None)
    payload = json.dumps(unsigned, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def test_ns_b1a3_pre_candidate_packet_is_complete_and_hash_chained() -> None:
    context = _load(CONTEXT)
    memory = _load(MEMORY)
    trace = _load(PRE_TRACE)

    assert context["atom_id"] == "NS-B1a3"
    assert context["first_candidate_at"] is None
    assert context["framework_binding"]["pin_status"] == "FRESH_EXACT_CURRENT_MAIN"
    assert memory["target_context_hash"] == context["packet_hash"]
    assert memory["fibre_snapshot_hash"] == context["fibre_snapshot_hash"]
    assert "F-NS-B1a2-KINETIC-ENERGY-NONQUANTIZATION" in memory["failure_query"]["relevant_failure_ids"]

    expected = [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert [event["event_type"] for event in trace["events"]] == expected
    previous = None
    for event in trace["events"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _event_hash(event)
        previous = event["artifact_hash"]
    assert trace["final_event_hash"] == previous
    assert trace["events"][-1]["payload"]["candidate_generation_allowed"] is True
    assert EXPERT.exists()


def test_ns_b1a3_git_chronology_proves_result_postdates_pre_candidate_freeze() -> None:
    subprocess.run(["git", "cat-file", "-e", f"{PRE_CANDIDATE_SHA}:research/real_math/millennium/navier_stokes/09_trace/NS-B1a3_PRE_CANDIDATE_TRACE_20260811.json"], cwd=ROOT, check=True)
    absent = subprocess.run(["git", "cat-file", "-e", f"{PRE_CANDIDATE_SHA}:{RESULT_REL}"], cwd=ROOT, check=False, capture_output=True)
    assert absent.returncode != 0
    assert RESULT.exists()


def test_ns_b1a3_result_is_scoped_and_failure_is_not_global_impossibility() -> None:
    text = RESULT.read_text(encoding="utf-8")
    assert "max-decoupled" in text
    assert "not Navier–Stokes solutions" in text
    assert "does **not** show" in text
    assert "NO_PROFILE_DECOMPOSITION_IMPOSSIBILITY" in text

    failure = _load(FAILURE)
    assert failure["failure_id"] == "F-NS-B1a3-I-MAX-DECOUPLING-NONADDITIVE-CURRENCY"
    assert failure["diagnosis_status"] == "SUPPORTED"
    assert "no claim about actual Navier-Stokes superposition or ancient solutions" in failure["scope_conditions"]

    review = RESULT_REVIEW.read_text(encoding="utf-8")
    assert "SCOPED_RESULT_ACCEPTED" in review
    assert "not prove failure of a profile decomposition" in review


def test_ns_b1a3_trace_episode_and_metrics_preserve_authority_and_metrology() -> None:
    pre = _load(PRE_TRACE)
    cont = _load(CONT_TRACE)
    assert cont["pre_candidate_final_event_hash"] == pre["final_event_hash"]
    previous = pre["final_event_hash"]
    for event in cont["events"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _event_hash(event)
        previous = event["artifact_hash"]
    assert cont["final_event_hash"] == previous

    episode = _load(EPISODE)
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["cost"] == 0.0
    assert "not interpreted as zero actual use" in episode["cost_note"]

    metrics = _load(METRICS)
    assert metrics["framework"]["application_framework_pin_sha"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert metrics["framework"]["pin_status"] == "FRESH_EXACT_CURRENT_MAIN"
    assert metrics["state"]["pre_state_fingerprint"]["value"] == "CANNOT_MEASURE"
    assert metrics["rakl_action_attribution"]["did_rakl_change_action"] == "OBSERVED_ROUTING_CHANGE_NOT_CAUSAL_ATTRIBUTION"
    assert set(metrics["retained_semantic_novelty"]) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }


def test_ns_b1a3_dag_opens_pde_specific_no_dichotomy_child_without_root_promotion() -> None:
    dag = yaml.safe_load(DAG.read_text(encoding="utf-8"))
    assert dag["root"]["status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    b1a = dag["atoms"]["NS-B1"]["open_children"]["NS-B1a"]
    assert b1a["completed_children"]["NS-B1a3"]["failure_memory"] == "F-NS-B1a3-I-MAX-DECOUPLING-NONADDITIVE-CURRENCY"
    assert b1a["next_child"]["id"] == "NS-B1a4"
    assert b1a["next_child"]["status"] == "CONTEXT_REQUIRED_BEFORE_CANDIDATE"
    assert any("max-decoupling" in rule for rule in dag["nonpromotion_rules"])


def test_ns_b1a3_large_separation_bound_decays() -> None:
    # Deterministic algebraic regression for the both-support cylinder bound.
    def upper(L: float, R: float, m2: float, m3: float, mg: float) -> float:
        return 2 * (m2 + mg) / (L - 2 * R) + 4 * m3 / (L - 2 * R) ** 2

    values = [upper(L, 2.0, 3.0, 5.0, 7.0) for L in (10.0, 20.0, 100.0, 1000.0)]
    assert values == sorted(values, reverse=True)
    assert values[-1] < 0.021
