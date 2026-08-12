from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"


def load(rel: str):
    return json.loads((RH / rel).read_text())


def h(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def test_r9_episode_and_case_study_are_content_bound_and_shadow_only():
    ep = load("07_memory/RH_ANA_003h_TASK_EPISODE_RESULT_20260812_R9.json")
    got = ep.pop("artifact_hash")
    assert got == h(ep)
    assert ep["outcome"] == "PARTIAL_SUCCESS"
    assert ep["storage_admission"] == "PROPOSAL_SHADOW_STORED"

    cs = load("09_trace/RH_ANA_003h_RAKL_METHOD_CASE_STUDY_20260812_R9.json")
    got = cs.pop("artifact_hash")
    assert got == "sha256:" + h(cs)
    assert cs["search_policy"]["rakl_changed_action"] is True
    assert cs["novelty_class"]["literature_novelty_claim"] == "NONE"


def test_r9_hash_chains_and_framework_drift_fail_closed():
    pre = load("09_trace/RH_ANA_003h_PRE_CANDIDATE_TRACE_20260812_R9.json")
    prev = "0" * 64
    for event in pre["entries"]:
        x = dict(event)
        got = x.pop("event_hash")
        assert x["prev_hash"] == prev
        assert got == h(x)
        prev = got
    assert pre["terminal_hash"] == prev

    result = load("09_trace/RH_ANA_003h_RESULT_TRACE_20260812_R9.json")
    prev = pre["terminal_hash"]
    for event in result["events"]:
        x = dict(event)
        got = x.pop("event_hash")
        assert x["prev_hash"] == prev
        assert got == h(x)
        prev = got
    assert result["terminal_hash"] == prev
    assert result["events"][-1]["payload"]["promotion"] == "INELIGIBLE"

    drift = load("09_trace/RH_ANA_003h_FRAMEWORK_DRIFT_REVALIDATION_20260812_R9.json")
    assert drift["verdict"] == "STALE_PROTECTED_SURFACE_CHANGED"
    assert drift["strict_discovery_effect"] == "FAIL_CLOSED_NOT_CURRENT_MAIN_DISCOVERY_COMPLIANT"


def test_r9_coefficient_balance_scale_and_scope_guard():
    c = load("04_candidates/RH_ANA_003h_EXACT_LAGUERRE_COEFFICIENT_SUBCRITICAL_TAIL_20260812_R9.json")
    assert c["outcome"] == "MATERIAL_REPRESENTATION_AND_CUTOFF_SCALE_IMPROVEMENT"
    assert "NO_RH_THEOREM" in c["authority"]
    assert c["novelty_class"]["primary"] == "representation"

    # The exact finite-degree majorant changes the balance coefficient from the
    # R8 n^3 log n scale to n log n at U=C n^(5/3) log^2 n.
    d = 1.0
    def kappa(C: float) -> float:
        return d * C ** (3.0 / 5.0) * (3.0 / 5.0) ** (1.0 / 5.0) - 2.0 / 3.0
    ccrit = ((2.0 / 3.0) / (d * (3.0 / 5.0) ** (1.0 / 5.0))) ** (5.0 / 3.0)
    assert kappa(ccrit * 0.5) < 0
    assert kappa(ccrit * 2.0) > 0
    assert abs(kappa(ccrit)) < 1e-12

    obs = load("07_memory/RH_ANA_003h_OBSTRUCTION_20260812_R9.json")
    assert obs["obstruction_id"] == "O-RH-ANA-003h-STRICT-PREFIX-ARITHMETIC-ATTAINABILITY"
    review = load("08_reviews/RH_ANA_003h_EXPERT_CELL_RESULT_20260812_R9.json")
    assert review["independent_review_credit"] == 0
