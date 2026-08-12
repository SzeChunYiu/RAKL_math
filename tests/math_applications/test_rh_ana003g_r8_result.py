from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RH=ROOT/"research/real_math/millennium/riemann_hypothesis"

def load(rel):
    return json.loads((RH/rel).read_text())

def h(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def prefixed(obj, field="artifact_hash"):
    x=dict(obj); got=x.pop(field)
    assert got=="sha256:"+h(x)

def positive_part(x):
    return max(x, 0)

def test_r8_result_packet_hashes_and_scope():
    for rel in [
        "04_candidates/RH_ANA_003g_EFFECTIVE_ENDPOINT_DICHOTOMY_20260812_R8.json",
        "07_memory/RH_ANA_003g_TASK_EPISODE_RESULT_20260812_R8.json",
        "07_memory/RH_ANA_003g_DIAGNOSIS_20260812_R8.json",
        "07_memory/RH_ANA_003g_OBSTRUCTION_20260812_R8.json",
        "07_memory/RH_ANA_003g_LESSON_20260812_R8.json",
        "07_memory/RH_ANA_003g_FAILURES_20260812_R8.json",
        "08_reviews/RH_ANA_003g_EXPERT_CELL_RESULT_20260812_R8.json",
        "09_trace/RH_ANA_003g_RESULT_TRACE_20260812_R8.json",
        "10_case_study/RAKL_METHOD_CASE_STUDY_RH_ANA_003g_20260812_R8.json",
    ]:
        prefixed(load(rel))

    cand=load("04_candidates/RH_ANA_003g_EFFECTIVE_ENDPOINT_DICHOTOMY_20260812_R8.json")
    assert cand["candidate_id"]=="RH-ANA-003g-C001-EFFECTIVE-ENDPOINT-DICHOTOMY"
    assert cand["framework_subject"]["rakl_main_sha"]=="5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
    assert cand["local_to_global"]["root_status"]=="OPEN_NO_SOLUTION_CERTIFICATE"
    assert cand["verification"]["independent_mathematical_reviews"]==0
    assert cand["current_v3_difference_witness_assessment"]["verdict"]=="REPRESENTATION_ONLY"
    assert cand["current_v3_difference_witness_assessment"]["may_certify_target_obligation_weakening"] is False

def test_effective_endpoint_inequality_on_adversarial_scalar_grid():
    # The proof is algebraic. This grid is regression/falsification support only.
    for r in range(-20,21):
        q0=positive_part(-r)
        for s in range(-20,21):
            d0=abs(s-r)
            for q_extra in (0,1,7):
                for d_extra in (0,2,9):
                    q=q0+q_extra
                    d=d0+d_extra
                    assert positive_part(-s) <= q+d

def test_result_trace_extends_pre_candidate_chain_and_preserves_episode_separation():
    pre=load("09_trace/RH_ANA_003g_PRE_CANDIDATE_TRACE_20260812_R8.json")
    res=load("09_trace/RH_ANA_003g_RESULT_TRACE_20260812_R8.json")
    assert res["extends_pre_candidate_terminal_hash"]==pre["terminal_hash"]
    prev=pre["terminal_hash"].split("sha256:",1)[1]
    for event in res["events"]:
        x=dict(event); got=x.pop("artifact_hash")
        assert x["previous_event_hash"]==prev
        assert got==h(x)
        prev=got
    assert res["terminal_hash"]=="sha256:"+prev
    ep=load("07_memory/RH_ANA_003g_TASK_EPISODE_RESULT_20260812_R8.json")
    diag=load("07_memory/RH_ANA_003g_DIAGNOSIS_20260812_R8.json")
    obs=load("07_memory/RH_ANA_003g_OBSTRUCTION_20260812_R8.json")
    lesson=load("07_memory/RH_ANA_003g_LESSON_20260812_R8.json")
    assert ep["episode_id"]=="EP-RH-ANA-003g-EFFECTIVE-ENDPOINT-DICHOTOMY-20260812-R8"
    assert diag["episode_id"]==ep["episode_id"]
    assert obs["episode_id"]==ep["episode_id"]
    assert lesson["episode_id"]==ep["episode_id"]
    assert lesson["counts_as_canonical_learning"] is False
