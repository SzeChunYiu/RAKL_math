from __future__ import annotations

import hashlib
import json
from pathlib import Path

YM = Path("research/real_math/millennium/yang_mills")
CANDIDATE = YM / "04_candidates/YM-S1A1_C001_DENSE_SOURCE_COMMON_RATE_SPECTRAL_EXCLUSION_20260811.md"
EPISODE = YM / "07_memory/YM-S1A1_DENSE_SOURCE_TASK_EPISODE_20260811.json"
SAT = YM / "07_memory/YM-S1A1_SATURATION_VECTOR_SHADOW_20260811.json"
TRACE = YM / "09_trace/YM-S1A1_POST_CANDIDATE_TRACE_20260811.json"
CHILD = YM / "02_problem_dag/YM-S1A2.yaml"

EXPECTED_CONTEXT = "sha256:082ddb6131aa0316cbdd17248d762af6bc036caed877a2acce42087f1c940e3a"
EXPECTED_CANDIDATE_SHA256 = "a8b6081ac1333468fc05fa98ad2d456f89d2ea934250517af265f803e8408f9b"
PREVIOUS_E007_HASH = "sha256:7c93020929cde30bcc7ed92a5300f7e938064655cc24033ce0fe602c12b1edaf"


def _canonical_hash(value: dict[str, object]) -> str:
    return "sha256:" + hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def test_candidate_is_exactly_bound_and_scoped() -> None:
    data = CANDIDATE.read_bytes()
    assert hashlib.sha256(data).hexdigest() == EXPECTED_CANDIDATE_SHA256
    text = data.decode("utf-8")
    assert "dense in `H_exc`" in text
    assert "one **common** asymptotic transfer ratio `q<1`" in text
    assert "Spec(T|H_exc) subset [0,q]" in text
    assert "YM-S1a2 — OS/SZZ SAME-THEORY BINDING" in text
    assert "PROVISIONAL_RAKL_TRIVIAL" in text
    assert "ROOT_AUTHORITY_NONE" in text


def test_known_answer_worlds_guard_density_and_uniform_rate() -> None:
    # Old hidden-state world: q=1/4 is visible only on e2, while e1 has ratio 1/2.
    true_excited_ratios = (0.5, 0.25)
    restricted_source_ratios = (0.25,)
    assert max(restricted_source_ratios) < max(true_excited_ratios)

    # Enlarged complete source world recovers the exact slowest ratio.
    complete_source_ratios = (0.5, 0.25)
    assert max(complete_source_ratios) == max(true_excited_ratios) == 0.5

    # Dense sourcewise rates can approach one, so individual q_k<1 is not a gap.
    q_k = tuple(1.0 - 1.0 / (k + 1) for k in range(1, 10000))
    assert all(q < 1.0 for q in q_k)
    assert q_k[-1] > 0.9998  # finite witness of the registered q_k -> 1 construction


def test_v3_episode_separates_local_success_from_gluing_residual() -> None:
    episode = json.loads(EPISODE.read_text(encoding="utf-8"))
    assert episode["context_hash"] == EXPECTED_CONTEXT
    assert episode["fibre_snapshot_hash"] == EXPECTED_CONTEXT
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["proposal_shadow"] is True
    assert episode["novelty_classification"] == "PROVISIONAL_RAKL_TRIVIAL"
    assert any(item.startswith("LOCAL_MATH_CLOSED:") for item in episode["residual_signature"])
    assert sum(item.startswith("GLUING_OPEN:") for item in episode["residual_signature"]) == 2

    unsigned = dict(episode)
    observed = unsigned.pop("artifact_hash")
    assert observed == _canonical_hash(unsigned)


def test_seven_axis_saturation_is_shadow_and_reopened() -> None:
    sat = json.loads(SAT.read_text(encoding="utf-8"))
    assert sat["proposal_shadow"] is True
    assert sat["bounded_saturated"] is False
    assert sat["retained_novelty"]["OPERATOR"] == 0
    assert sat["retained_novelty"]["META_METHOD"] == 0
    assert set(sat["reopened_axes"]) == {"RELATION", "PATH", "KNOWLEDGE"}

    unsigned = dict(sat)
    observed = unsigned.pop("artifact_hash")
    assert observed == _canonical_hash(unsigned)


def test_post_candidate_trace_continues_pre_candidate_hash_chain() -> None:
    trace = json.loads(TRACE.read_text(encoding="utf-8"))
    entries = trace["entries"]
    assert entries[0]["previous_event_hash"] == PREVIOUS_E007_HASH
    previous = PREVIOUS_E007_HASH
    for event in entries:
        assert event["previous_event_hash"] == previous
        unsigned = dict(event)
        observed = unsigned.pop("artifact_hash")
        assert observed == _canonical_hash(unsigned)
        previous = observed
    assert [event["event_type"] for event in entries] == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
        "REVIEWED",
    ]


def test_new_target_binding_child_fails_closed_before_candidate() -> None:
    text = CHILD.read_text(encoding="utf-8")
    assert "atom_id: YM-S1a2" in text
    assert "status: CONTEXT_REQUIRED" in text
    assert "allowed: false" in text
    assert "G5 RG transport" in text
    assert "G6 physical lattice-spacing scaling" in text
    assert "G7 continuum spectral identification" in text
    assert "ROOT_AUTHORITY_NONE" in text
