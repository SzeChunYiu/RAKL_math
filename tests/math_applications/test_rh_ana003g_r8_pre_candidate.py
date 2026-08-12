from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RH=ROOT/"research/real_math/millennium/riemann_hypothesis"

def load(rel: str):
    return json.loads((RH/rel).read_text())

def h(obj) -> str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def check_prefixed(rel: str):
    obj=load(rel); got=obj.pop("artifact_hash")
    assert got=="sha256:"+h(obj)

def test_r8_pre_candidate_packet_is_current_v3_frozen_and_hash_bound():
    fibre=load("01_frontier/RH_ANA_003g_CONTEXT_FIBER_20260812_R8.json")
    x=dict(fibre); got=x.pop("packet_hash")
    assert got=="sha256:"+h(x)
    assert fibre["framework_subject"]=={
        "method_version":"3.0.0",
        "rakl_main_sha":"43897d3afaf0038385102d5acc64793c05ec40f0",
        "application_pin":"43897d3afaf0038385102d5acc64793c05ec40f0",
    }
    assert fibre["application_subject"]["base_sha"]=="70a4c30e88e01f3923ab3efc4311a77c50b05bba"
    for rel in [
      "07_memory/RH_ANA_003g_RESEARCH_MEMORY_REVIEW_20260812_R8.json",
      "07_memory/RH_ANA_003g_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812_R8.json",
      "08_reviews/RH_ANA_003g_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812_R8.json",
      "08_reviews/RH_ANA_003g_EXPERT_CELL_PRE_CANDIDATE_20260812_R8.json",
      "09_trace/RH_ANA_003g_PRE_CANDIDATE_TRACE_20260812_R8.json",
    ]: check_prefixed(rel)
    review=load("08_reviews/RH_ANA_003g_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812_R8.json")
    assert review["selected_mode"]=="GLUE"
    assert review["lift_status"]=="NOT_AUTHORIZED"
    experts=load("08_reviews/RH_ANA_003g_EXPERT_CELL_PRE_CANDIDATE_20260812_R8.json")
    assert len(experts["roles"])==7 and experts["independent_review_credit"]==0
    memory=load("07_memory/RH_ANA_003g_RESEARCH_MEMORY_REVIEW_20260812_R8.json")
    assert memory["decision_policy"]["rakl_changed_action"] is True
    assert len(memory["selected_failure_ids"])+len(memory["selected_episode_or_motif_ids"])==8
    assert len(memory["rejected_ids"])==5

def test_r8_pre_candidate_trace_is_hash_chained_and_ends_before_candidate():
    trace=load("09_trace/RH_ANA_003g_PRE_CANDIDATE_TRACE_20260812_R8.json")
    prev="0"*64
    for event in trace["events"]:
        x=dict(event); got=x.pop("event_hash")
        assert x["prev_hash"]==prev
        assert got==h(x)
        prev=got
    assert trace["terminal_hash"]=="sha256:"+prev
    assert trace["events"][-1]["type"]=="NEXT_STEP_PROPOSED"
    assert trace["candidate_generated"] is False
