from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"

def load(rel: str):
    return json.loads((RH / rel).read_text())

def h(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def check_prefixed(rel: str):
    obj=load(rel); got=obj.pop("artifact_hash")
    assert got=="sha256:"+h(obj)

def test_r7_candidate_hashes_and_authority_are_scoped():
    for rel in [
        "04_candidates/RH_ANA_003f_INTERIOR_EXCURSION_GLUING_DICHOTOMY_20260812_R7.json",
        "07_memory/RH_ANA_003f_DIAGNOSIS_20260812_R7.json",
        "07_memory/RH_ANA_003f_OBSTRUCTION_20260812_R7.json",
        "07_memory/RH_ANA_003f_LESSON_20260812_R7.json",
        "07_memory/RH_ANA_003f_FAILURES_20260812_R7.json",
        "08_reviews/RH_ANA_003f_EXPERT_CELL_RESULT_20260812_R7.json",
        "09_trace/RH_ANA_003f_RESULT_TRACE_20260812_R7.json",
        "10_case_study/RAKL_METHOD_CASE_STUDY_RH_ANA_003f_20260812_R7.json",
    ]:
        check_prefixed(rel)
    c=load("04_candidates/RH_ANA_003f_INTERIOR_EXCURSION_GLUING_DICHOTOMY_20260812_R7.json")
    assert c["outcome"]=="PARTIAL_SUCCESS_ROUTE_DICHOTOMY_AND_GLUING_OBSTRUCTION"
    assert "NO_RH_THEOREM" in c["authority"]
    r=load("08_reviews/RH_ANA_003f_EXPERT_CELL_RESULT_20260812_R7.json")
    assert r["independent_review_credit"]==0
    assert r["consensus"].endswith("NO_ROOT_PROMOTION")

def test_r7_task_episode_uses_v3_content_hash_contract():
    ep=load("07_memory/RH_ANA_003f_TASK_EPISODE_RESULT_20260812_R7.json")
    got=ep.pop("artifact_hash")
    assert got==h(ep)
    assert ep["storage_admission"]=="PROPOSAL_SHADOW_STORED"
    assert ep["outcome"]=="PARTIAL_SUCCESS"
    assert "ROOT_REMAINS_OPEN" in ep["residual_signature"]

def q_of(path: list[float], y: int) -> float:
    return max([0.0] + [max(-path[m], 0.0) for m in range(0, y+1)])

def g_of(path: list[float], y: int, x: int) -> float:
    return max([0.0] + [max(path[y]-path[m], 0.0) for m in range(y, x+1)])

def test_r7_strict_cut_gluing_inequality_on_hostile_finite_paths():
    paths=[
        [0.0, 2.0, -1.0, 3.0, -7.0],
        [0.0, -2.0, -1.0, -4.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, -100.0],
        [0.0, 5.0, 4.0, 3.0, 2.0],
    ]
    for path in paths:
        y=2; x=len(path)-1
        q=q_of(path,y); g=g_of(path,y,x)
        assert path[x] >= -q-g
        q_end=q_of(path,x)
        assert max(-path[x],0.0) <= q_end

def test_r7_ambient_differencewitness_is_not_mislabeled_arithmetic():
    a=[0.0,0.0,0.0,0.0]
    b=[0.0,0.0,0.0,-1000.0]
    assert q_of(a,2)==q_of(b,2)==0.0
    assert a[-1]!=b[-1]
    c=load("04_candidates/RH_ANA_003f_INTERIOR_EXCURSION_GLUING_DICHOTOMY_20260812_R7.json")
    assert c["difference_witness"]["type"]=="STRUCTURAL_PATH_SPACE_NOT_TARGET_ARITHMETIC"
    assert "not claimed to be realizable" in c["difference_witness"]["does_not_establish"]

def test_r7_result_trace_is_hash_chained_after_pretrace():
    tr=load("09_trace/RH_ANA_003f_RESULT_TRACE_20260812_R7.json")
    prev=tr["pre_trace_terminal_hash"].removeprefix("sha256:")
    for event in tr["events"]:
        x=dict(event); got=x.pop("event_hash")
        assert x["prev_hash"]==prev
        assert got==h(x)
        prev=got
    assert tr["terminal_hash"]=="sha256:"+prev
    assert tr["events"][-1]["type"]=="ROOT_GATE_CHECK"
    assert tr["events"][-1]["payload"]["root_state"]=="OPEN_NO_SOLUTION_CERTIFICATE"
