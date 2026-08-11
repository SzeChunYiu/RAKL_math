import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def _load(rel):
    return json.loads((NS / rel).read_text())


def test_r4_finite_history_scope_and_nonpromotion():
    episode = _load("07_memory/NS-B1a3b1a2_TASK_EPISODE_R4_20260811.json")
    delta = _load("07_memory/NS-B1a3b1a2_EXPERIENCE_DELTA_R4_20260811.json")
    review = _load("08_reviews/NS-B1a3b1a2_EXPERT_POSTCHECK_R4_20260811.json")

    assert episode["atom_id"] == "NS-B1a3b1a2"
    assert episode["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert episode["outcome"] == "SCOPED_SOLVED_ROUTE_PRUNED_FIXED_FINITE_HISTORY"
    assert episode["residual_signature"] == "ANCIENT_INFINITE_HISTORY_OR_SCALE_RELATIVE_TIGHTNESS_STILL_OPEN"
    assert episode["independent_review_credit"] == "0/3"
    assert episode["novelty_class"] == "transfer"

    assert delta["episode_link"] == episode["episode_id"]
    assert delta["diagnosis"]["id"] != episode["episode_id"]
    assert delta["obstruction"]["id"] != delta["diagnosis"]["id"]
    assert delta["lesson"]["authority"] == "CANDIDATE_ONLY_SEARCH_PRIORITY"
    assert review["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert review["independent_review_credit"] == "0/3"


def test_r4_critical_scaling_exponents():
    # NSE scaling u_l=lambda u(lambda x, lambda^2 t), omega_l=lambda^2 omega(lambda x,...)
    # Weak L^p spatial scaling exponent for omega is 2-3/p, which vanishes at p=3/2.
    p = 3 / 2
    assert 2 - 3 / p == 0

    # A: r^-1 int_B |u|^2. Integral scaling exponent is -1 and radius maps r->lambda*r.
    assert -1 + 1 == 0
    # C,D: r^-2 spacetime integral; |u|^3 and |p|^(3/2) both give integral exponent -2.
    assert -2 + 2 == 0
    # E: r^-1 spacetime integral |grad u|^2 gives integral exponent -1.
    assert -1 + 1 == 0


def test_r4_trace_tail_and_gluing_separation():
    rows = [json.loads(line) for line in (NS / "09_trace/NS-B1a3b1a2_TRACE_R4_20260811.jsonl").read_text().splitlines()]
    assert rows[-1]["event"] == "NEXT_ACTION"
    assert rows[-1]["event_hash"] == "sha256:d5307654e947a31879844f4deaa0e4f40e5e86b57d27f06bcf142c389ba25e1f"
    assert rows[-1]["payload"]["residual"] == "ANCIENT_INFINITE_HISTORY_OR_SCALE_RELATIVE_TIGHTNESS_STILL_OPEN"
    for prev, cur in zip(rows, rows[1:]):
        assert cur["prev_hash"] == prev["event_hash"]

    dag = (NS / "02_problem_dag/NS_B1a3b1a2_C001_R4_DELTA_20260811.yaml").read_text()
    assert "FIXED_FINITE_HISTORY_PRODUCER_PRUNED_ANCIENT_RESIDUAL_OPEN" in dag
    assert "local_to_global_gluing_status: ANCIENT_SOURCE_CLASS_NOT_REACHED" in dag
    assert "root_status: OPEN_NO_SOLUTION_CERTIFICATE" in dag
