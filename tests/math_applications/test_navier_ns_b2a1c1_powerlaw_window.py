from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from rakl.experience_substrate import (
    EpisodeOutcome,
    EpisodeStorageAdmission,
    TaskEpisode,
    validate_episode,
)
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
    audit_research_trace,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"
CONTEXT_HASH = "sha256:663e72979a23265725349862397e5d8a7c2d94b75613ba062d504a7ea9a858b9"
REVIEW_HASH = "sha256:18916d9eccc7a00b890a723a97b1901c1da52994a17d6925842c81b9df7872a3"


def _load(rel: str):
    return json.loads((BASE / rel).read_text())


def _entry(x: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
        event_id=x["event_id"],
        atom_id=x["atom_id"],
        event_type=ResearchTraceEventType(x["event_type"]),
        timestamp=x["timestamp"],
        state_summary=x["state_summary"],
        action_summary=x["action_summary"],
        evidence_pointers=tuple(x["evidence_pointers"]),
        alternatives_considered=tuple(x["alternatives_considered"]),
        decision_rationale=x["decision_rationale"],
        outputs=tuple(x["outputs"]),
        uncertainties=tuple(x["uncertainties"]),
        residuals=tuple(x["residuals"]),
        next_steps=tuple(x["next_steps"]),
        artifact_hash=x["artifact_hash"],
        previous_event_hash=x["previous_event_hash"],
    )


def test_b2a1c1_r2_trace_passes_current_v3_gate_d() -> None:
    pre = _load("09_trace/NS-B2a1c1_PRE_CANDIDATE_TRACE_R2_20260812.json")
    result = _load("09_trace/NS-B2a1c1_RESULT_TRACE_R2_20260812.json")
    pre_trace = MathResearchTrace(pre["trace_id"], tuple(_entry(x) for x in pre["entries"]))
    assert audit_research_trace(pre_trace).verdict is TraceGateVerdict.PASS
    assert audit_pre_candidate_trace(
        pre_trace,
        atom_id="NS-B2a1c1",
        context_packet_hash=CONTEXT_HASH,
        obstruction_transformation_review_hash=REVIEW_HASH,
    ).verdict is TraceGateVerdict.PASS

    full_trace = MathResearchTrace(
        "TRACE-NS-B2a1c1-R2-FULL-20260812",
        tuple(_entry(x) for x in pre["entries"] + result["entries"]),
    )
    assert audit_research_trace(full_trace).verdict is TraceGateVerdict.PASS
    assert result["entries"][0]["previous_event_hash"] == pre["entries"][-1]["artifact_hash"]


def test_b2a1c1_task_episode_has_exact_v3_content_hash() -> None:
    x = _load("07_memory/NS-B2a1c1_TASK_EPISODE_R2_20260812.json")
    episode = TaskEpisode(
        episode_id=x["episode_id"], task_id=x["task_id"], atom_id=x["atom_id"],
        context_hash=x["context_hash"], problem_signature=tuple(x["problem_signature"]),
        fibre_snapshot_hash=x["fibre_snapshot_hash"], operator_ids=tuple(x["operator_ids"]),
        action_trace=tuple(x["action_trace"]), observation_ids=tuple(x["observation_ids"]),
        verification_ids=tuple(x["verification_ids"]), outcome=EpisodeOutcome(x["outcome"]),
        residual_signature=tuple(x["residual_signature"]), evidence_pointers=tuple(x["evidence_pointers"]),
        artifact_hash=x["artifact_hash"], timestamp=x["timestamp"], cost=x["cost"],
        storage_admission=EpisodeStorageAdmission(x["storage_admission"]),
    )
    assert validate_episode(episode) == ()
    assert episode.storage_admission is EpisodeStorageAdmission.PROPOSAL_SHADOW_STORED


def threshold(l1: Fraction) -> Fraction:
    return (Fraction(5) - 2 * l1) / (l1 + 1)


def exponent(alpha: Fraction, l1: Fraction) -> Fraction:
    return Fraction(2) - 3 * l1 / 2 - (alpha - 1) * (l1 + 1) / 2


def test_b2a1c1_exact_parameter_window_and_old_parameterization() -> None:
    for l1 in (Fraction(11, 10), Fraction(6, 5), Fraction(5, 4)):
        t = threshold(l1)
        assert Fraction(1) < t < Fraction(3, 2)
        assert exponent(t, l1) == 0
        assert exponent(Fraction(3, 2), l1) < 0
        assert exponent(Fraction(1), l1) > 0

        m_bound = (4 * l1 - 3) / (l1 + 1)
        assert Fraction(2) - t == m_bound
        m = (Fraction(1, 2) + m_bound) / 2
        alpha = Fraction(2) - m
        assert exponent(alpha, l1) < 0

    assert threshold(Fraction(5, 4)) == Fraction(10, 9)
    # Exact non-emptiness identity: 3/2 - threshold = 7(l1-1)/(2(l1+1)).
    for l1 in (Fraction(101, 100), Fraction(6, 5), Fraction(5, 4)):
        assert Fraction(3, 2) - threshold(l1) == 7 * (l1 - 1) / (2 * (l1 + 1))


def test_b2a1c1_keeps_local_and_gluing_failures_separate() -> None:
    delta = _load("02_problem_dag/NS_B2A1C1_DELTA_20260812.json")
    assert delta["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert delta["closed_edge"] == "GENERALIZED_F_PRODUCER -> SECTION4_4_4_PARAMETER_COMPATIBILITY"
    assert delta["separate_failures"]["local_to_global_gluing"].startswith("F-NS-B2a1c1")
    assert delta["separate_failures"]["process"].startswith("F-PROC-NS-B2a1c1")
