from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"


def test_ns_b1a2_pre_candidate_chronology_and_authority() -> None:
    context = json.loads((NS / "01_frontier/NS-B1a2_CONTEXT_FIBER_20260811.json").read_text())
    memory = json.loads((NS / "07_memory/NS-B1a2_RESEARCH_MEMORY_REVIEW_20260811.json").read_text())
    trace = json.loads((NS / "09_trace/NS-B1a2_PRE_CANDIDATE_TRACE_20260811.json").read_text())

    assert context["atom_id"] == "NS-B1a2"
    assert context["first_candidate_at"] is None
    assert memory["target_context_hash"] == context["packet_hash"]
    assert trace["context_packet_hash"] == context["packet_hash"]
    assert trace["memory_review_hash"] == memory["artifact_hash"]
    assert [event["event_type"] for event in trace["events"]] == [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    previous = None
    for event in trace["events"]:
        assert event["previous_event_hash"] == previous
        previous = event["artifact_hash"]
    assert trace["final_event_hash"] == previous
    assert trace["events"][-1]["payload"]["candidate_generation_allowed"] is True
    assert "NO_THEOREM_AUTHORITY" in trace["authority"]


def test_ns_b1a2_energy_count_has_divergent_scale_bound() -> None:
    E0 = 2.0
    M = 3.0
    gamma = 0.5
    bounds = []
    for lam in (0.5, 0.25, 0.125, 0.0625):
        count_bound = M * E0 / (gamma**3 * lam)
        bounds.append(count_bound)
        per_core_energy = gamma**3 * lam / M
        assert math.isclose(count_bound * per_core_energy, E0)
    assert bounds == sorted(bounds)
    assert math.isclose(bounds[-1] / bounds[-2], 2.0)


def test_ns_b1a2_packed_blob_scaling_is_energy_bounded_but_l3_diverges() -> None:
    # Scale identities for N(lambda)=c/lambda disjoint copies of
    # lambda^-1 phi((x-x_j)/lambda). Constants ||phi||_2^2 and ||phi||_3^3
    # are normalized to one because only the lambda exponents are tested.
    c = 0.25
    total_energies = []
    l3_cubed = []
    for lam in (0.25, 0.125, 0.0625, 0.03125):
        n = int(c / lam)
        total_energies.append(n * lam)
        l3_cubed.append(float(n))
    assert all(math.isclose(value, c) for value in total_energies)
    assert l3_cubed == sorted(l3_cubed)
    assert l3_cubed[-1] > l3_cubed[0]


def test_ns_b1a2_metrics_and_dag_fail_closed() -> None:
    metrics = json.loads((NS / "10_case_study/NS-B1a2_C001_RAKL_CYCLE_METRICS_20260811.json").read_text())
    dag_text = (NS / "02_problem_dag/open_obligations.yaml").read_text()
    failure = json.loads((NS / "07_memory/NS-B1a2_C001_FAILURE_EXPERIENCE_DELTA_20260811.json").read_text())

    assert metrics["authority"] == "PROPOSAL_SHADOW_TELEMETRY_ONLY"
    assert metrics["outcome"]["novel_structure_rank"] == 0
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 1,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["gates"]["independent_review"] is False
    assert metrics["gates"]["root_authority"] == "NONE"
    assert failure["experience"]["diagnosis_status"] == "SUPPORTED"
    assert failure["experience"]["failure_id"] == "F-NS-B1a2-KINETIC-ENERGY-NONQUANTIZATION"
    assert "status: OPEN_NO_SOLUTION_CERTIFICATE" in dag_text
    assert "id: NS-B1a3" in dag_text
    assert "status: OPEN_SIBLING_RESIDUAL" in dag_text
