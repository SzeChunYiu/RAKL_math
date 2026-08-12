from __future__ import annotations
import hashlib, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RH=ROOT/"research/real_math/millennium/riemann_hypothesis"

def load(rel: str): return json.loads((RH/rel).read_text())
def h(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def check_prefixed(rel: str):
    obj=load(rel); got=obj.pop("artifact_hash"); assert got=="sha256:"+h(obj)

def test_r8_result_artifacts_are_content_bound_and_shadow_scoped():
    for rel in [
      "04_candidates/RH_ANA_003g_KV_ABSOLUTE_MAJORANT_FIXED_SCALE_DICHOTOMY_20260812_R8.json",
      "07_memory/RH_ANA_003g_DIAGNOSIS_20260812_R8.json",
      "07_memory/RH_ANA_003g_OBSTRUCTION_20260812_R8.json",
      "07_memory/RH_ANA_003g_LESSON_20260812_R8.json",
      "07_memory/RH_ANA_003g_FAILURES_20260812_R8.json",
      "08_reviews/RH_ANA_003g_EXPERT_CELL_RESULT_20260812_R8.json",
      "09_trace/RH_ANA_003g_RESULT_TRACE_20260812_R8.json",
      "09_trace/RH_ANA_003g_RAKL_METHOD_CASE_STUDY_20260812_R8.json",
    ]: check_prefixed(rel)
    ep=load("07_memory/RH_ANA_003g_TASK_EPISODE_RESULT_20260812_R8.json")
    got=ep.pop("artifact_hash"); assert got==h(ep)
    assert ep["outcome"]=="PARTIAL_SUCCESS"
    assert ep["storage_admission"]=="PROPOSAL_SHADOW_STORED"

def test_r8_fixed_c_phase_diagram_and_scope_guards():
    c=load("04_candidates/RH_ANA_003g_KV_ABSOLUTE_MAJORANT_FIXED_SCALE_DICHOTOMY_20260812_R8.json")
    assert c["outcome"]=="MATERIAL_ROUTE_PRUNING_PARTIAL_SUCCESS"
    assert "NO_RH_THEOREM" in c["authority"]
    d=1.0
    cstar=25.0*(2.0/d)**10
    def coeff(C): return 2.0*math.sqrt(C)-d*C**0.6/(5.0**0.2)
    assert coeff(cstar*0.5)>0
    assert coeff(cstar*2.0)<0
    assert abs(coeff(cstar)) < 1e-9*max(1.0,2.0*math.sqrt(cstar))
    assert c["phase_diagram"]["critical_or_n_dependent_transition"].startswith("UNRESOLVED")
    fs=load("07_memory/RH_ANA_003g_FAILURES_20260812_R8.json")
    ids={x["failure_id"] for x in fs["failures"]}
    assert "F-RH-ANA-003g-SUBCRITICAL-ABSOLUTE-MAJORANT-VACUOUS" in ids
    assert "F-RH-ANA-003g-SUPERCRITICAL-COMPLEMENT-ROOTLOAD-TRANSFER" in ids
    assert fs["repeated_process_failure_links"][0]["prior"]=="F-RH-ANA-003e-PRE-CANDIDATE-SNAPSHOT-HASH-MISMATCH"

def test_r8_result_trace_continues_pre_trace_and_root_stays_open():
    pre=load("09_trace/RH_ANA_003g_PRE_CANDIDATE_TRACE_20260812_R8.json")
    tr=load("09_trace/RH_ANA_003g_RESULT_TRACE_20260812_R8.json")
    prev=pre["terminal_hash"].split(":",1)[1]
    assert tr["parent_terminal_hash"]==pre["terminal_hash"]
    for event in tr["events"]:
        x=dict(event); got=x.pop("event_hash")
        assert x["prev_hash"]==prev
        assert got==h(x); prev=got
    assert tr["terminal_hash"]=="sha256:"+prev
    assert tr["events"][-1]["type"]=="ROOT_GATE_CHECK"
    assert tr["events"][-1]["payload"]["promotion"]=="INELIGIBLE"
    review=load("08_reviews/RH_ANA_003g_EXPERT_CELL_RESULT_20260812_R8.json")
    assert review["independent_review_credit"]==0
