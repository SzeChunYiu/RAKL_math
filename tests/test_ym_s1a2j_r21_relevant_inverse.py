import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACE = ROOT / "research/real_math/millennium/yang_mills/09_trace/YM-S1a2j_TRACE_CURRENT_SCHEMA_20260812_R21.json"
CORRECTION = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1a2j_R21_CHRONOLOGY_HASH_CORRECTION_20260812.json"


def test_nonnormal_expanding_eigenvalues_do_not_force_inverse_contraction():
    # A_M=[[2,M],[0,2]].  Both eigenvalues are exactly 2.  Applying A_M^{-1}
    # to e_2 gives (-M/4, 1/2), hence a rigorous lower bound on the inverse norm.
    M = 4.0
    inverse_norm_lower_bound = math.sqrt((M / 4.0) ** 2 + 0.5**2)
    assert inverse_norm_lower_bound > 1.0


def test_one_dimensional_relevant_block_is_a_real_exception():
    # If the target relevant block is actually one-dimensional and invariant,
    # |a|>=lambda_rel>1 does imply ||a^{-1}||<=1/lambda_rel<1.
    lambda_rel = 1.1
    assert 1.0 / lambda_rel < 1.0


def test_current_schema_shadow_trace_is_hash_chained_and_pre_candidate_ordered():
    data = json.loads(TRACE.read_text())
    entries = data["entries"]
    required = [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert [entry["event_type"] for entry in entries[:8]] == required
    assert entries[0]["previous_event_hash"] == ""
    for previous, current in zip(entries, entries[1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]


def test_chronology_hash_mismatch_is_fail_closed_not_silently_repaired():
    correction = json.loads(CORRECTION.read_text())
    assert correction["match"] is False
    assert correction["strict_binding_verdict"] == "RETROSPECTIVE_BINDING_REFUTED"
    assert correction["chronology_status"] == "RETROSPECTIVE_ONLY"
    assert correction["raw_repository_growth_learning_credit"] == 0
