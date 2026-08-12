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

def test_r7_pre_candidate_packet_is_frozen_and_fail_closed():
    fibre=load("01_frontier/RH_ANA_003f_CONTEXT_FIBER_20260812_R7.json")
    x=dict(fibre); got=x.pop("packet_hash")
    assert got=="sha256:"+h(x)
    assert fibre["framework_subject"]=={"method_version":"3.0.0","rakl_main_sha":"43897d3afaf0038385102d5acc64793c05ec40f0","application_pin":"43897d3afaf0038385102d5acc64793c05ec40f0"}
    assert fibre["application_subject"]["base_sha"]=="ec8a9eb5eeedaaf1d3f497a8688384256a2079e0"
    for rel in [
      "07_memory/RH_ANA_003f_RESEARCH_MEMORY_REVIEW_20260812_R7.json",
      "07_memory/RH_ANA_003f_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812_R7.json",
      "08_reviews/RH_ANA_003f_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812_R7.json",
      "08_reviews/RH_ANA_003f_EXPERT_CELL_PRE_CANDIDATE_20260812_R7.json",
      "09_trace/RH_ANA_003f_PRE_CANDIDATE_TRACE_20260812_R7.json",
    ]: prefixed(load(rel))
    review=load("08_reviews/RH_ANA_003f_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812_R7.json")
    assert review["selected_mode"]=="GLUE"
    assert review["lift_status"]=="NOT_AUTHORIZED"
    experts=load("08_reviews/RH_ANA_003f_EXPERT_CELL_PRE_CANDIDATE_20260812_R7.json")
    assert len(experts["roles"])==7 and experts["independent_review_credit"]==0
    trace=load("09_trace/RH_ANA_003f_PRE_CANDIDATE_TRACE_20260812_R7.json")
    prev="0"*64
    for event in trace["events"]:
        x=dict(event); got=x.pop("event_hash")
        assert x["prev_hash"]==prev
        assert got==h(x)
        prev=got
    assert trace["terminal_hash"]=="sha256:"+prev
    assert trace["events"][-1]["type"]=="NEXT_STEP_PROPOSED"
    assert trace["candidate_generated"] is False
