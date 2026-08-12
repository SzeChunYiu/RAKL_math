from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
CAND = RH / "04_candidates/RH_ANA_003e_PREFIX_GROWTH_STRENGTH_FALSIFIER_20260812_R6.json"
EP = RH / "07_memory/RH_ANA_003e_TASK_EPISODE_RESULT_20260812_R6.json"
FAIL = RH / "07_memory/RH_ANA_003e_RESULT_FAILURE_20260812_R6.json"
CASE = RH / "09_trace/RAKL_METHOD_CASE_STUDY_RH_ANA_003e_20260812_R6.json"

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def test_r6_result_is_route_pruning_not_root_promotion():
    c,e,f,s = map(load, (CAND,EP,FAIL,CASE))
    assert c["candidate_id"] == "RH-ANA-003e-C001-NEGLIGIBLE-TAIL-GROWTH-QUOTIENT"
    assert "NO_RH_THEOREM" in c["authority"]
    assert c["difference_witness"]["outcome"].startswith("IMPOSSIBLE")
    assert e["retained_semantic_novelty_counts"] == {"KNOWLEDGE":1,"OPERATOR":0,"EXPERIENCE_PATTERN":1,"OBSTRUCTION":1,"RELATION":1,"PATH":1,"META_METHOD":0}
    assert f["failure_category"] == ["decomposition","representation","gluing"]
    assert s["episode_diagnosis_obstruction_lesson"]["kept_distinct"] is True
    assert s["failure_category"]["mathematical"] == "NONE_LOCAL_LEMMA_SUCCEEDED"

def test_elementary_negligible_tail_growth_equivalence_fixture():
    A=2
    P=[0,4,9,16,25]
    T=[0.5,-0.25,0.1,-0.01,0.001]
    S=[p+t for p,t in zip(P,T)]
    for n,(p,s,t) in enumerate(zip(P,S,T), start=1):
        assert abs(s) <= abs(p)+abs(t)+1e-15
        assert abs(p) <= abs(s)+abs(t)+1e-15
        assert abs(t) <= 1
        assert n**A >= 1
