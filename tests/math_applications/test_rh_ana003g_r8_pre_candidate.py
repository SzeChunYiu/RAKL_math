from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RH=ROOT/"research/real_math/millennium/riemann_hypothesis"
FRAMEWORK=ROOT/"framework/RAKL/src"
sys.path.insert(0, str(FRAMEWORK))

def load(rel):
    return json.loads((RH/rel).read_text())

def h(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def prefixed(obj, field="artifact_hash"):
    x=dict(obj); got=x.pop(field)
    assert got=="sha256:"+h(x)

def test_r8_pre_candidate_packet_and_current_v3_realization_domain_gate():
    fibre=load("01_frontier/RH_ANA_003g_CONTEXT_FIBER_20260812_R8.json")
    x=dict(fibre); got=x.pop("packet_hash")
    assert got=="sha256:"+h(x)
    assert fibre["framework_subject"]["rakl_main_sha"]=="5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
    assert fibre["framework_subject"]["application_pin"]=="5dc0627f039e8f3e1cdcb7e05cd7603860afc554"

    for rel in [
        "07_memory/RH_ANA_003g_RESEARCH_MEMORY_REVIEW_20260812_R8.json",
        "07_memory/RH_ANA_003g_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812_R8.json",
        "08_reviews/RH_ANA_003g_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812_R8.json",
        "08_reviews/RH_ANA_003g_EXPERT_CELL_PRE_CANDIDATE_20260812_R8.json",
        "09_trace/RH_ANA_003g_CURRENT_WORK_RECONCILIATION_20260812_R8.json",
        "09_trace/RH_ANA_003g_PRE_CANDIDATE_TRACE_20260812_R8.json",
    ]:
        prefixed(load(rel))

    trace=load("09_trace/RH_ANA_003g_PRE_CANDIDATE_TRACE_20260812_R8.json")
    required=[
        "ATOMIZED","CONTEXT_FROZEN","ANALOGY_SCAN","METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW","EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW","NEXT_STEP_PROPOSED"
    ]
    assert [e["type"] for e in trace["events"]]==required
    prev="0"*64
    for event in trace["events"]:
        x=dict(event); got=x.pop("artifact_hash")
        assert x["previous_event_hash"]==prev
        assert got==h(x)
        prev=got
    assert trace["terminal_hash"]=="sha256:"+prev
    assert trace["candidate_generated"] is False

    from rakl.failure_lattice import (
        DifferenceWitness, RealizationDomain, ObligationStrengthVerdict,
        assess_obligation_strength_claim,
    )
    witness=DifferenceWitness(
        target_atom_id="RH-ANA-003g",
        target_context_hash=fibre["packet_hash"],
        method_family="strict-cut-running-negative-excursion",
        prior_failure_ids=("F-RH-ANA-003f-PATH-WITNESS-NOT-ARITHMETIC",),
        changed_structural_coordinates=("strict cut before endpoint",),
        restored_or_replaced_assumptions=("suffix left explicit",),
        prior_falsifier_escape_reason="Synthetic suffix proves ambient non-identification only.",
        cheapest_repeat_failure_test="Check target arithmetic realizability before claiming strict reduction.",
        evidence_pointers=("R7 candidate/failure bundle",),
        realization_domain=RealizationDomain.AMBIENT_REPRESENTATION,
    )
    assessment=assess_obligation_strength_claim(witness)
    assert assessment.verdict is ObligationStrengthVerdict.REPRESENTATION_ONLY
    assert assessment.may_certify_target_obligation_weakening is False

    review=load("08_reviews/RH_ANA_003g_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812_R8.json")
    assert review["selected_mode"]=="GLUE"
    assert review["lift"]["status"]=="NOT_AUTHORIZED"
    experts=load("08_reviews/RH_ANA_003g_EXPERT_CELL_PRE_CANDIDATE_20260812_R8.json")
    assert len(experts["roles"])==7
    assert experts["independent_review_credit"]==0

def test_r8_framework_candidate_freeze_is_operationally_current():
    receipt=load("09_trace/RH_ANA_003g_FRAMEWORK_CANDIDATE_FREEZE_20260812_R8.json")
    prefixed(receipt)
    from rakl.framework_candidate_freeze import (
        FrameworkSubjectFreezeBinding, FrameworkSubjectRevalidationObservation,
        CandidateFreezeRevalidationVerdict, audit_candidate_freeze_framework_subject,
    )
    bdoc=receipt["binding"]
    binding=FrameworkSubjectFreezeBinding(
        binding_id=bdoc["binding_id"],
        authoritative_framework_sha=bdoc["authoritative_framework_sha"],
        pre_candidate_packet_hash=bdoc["pre_candidate_packet_hash"],
        frozen_at_utc=bdoc["frozen_at_utc"],
        evidence_pointers=tuple(bdoc["evidence_pointers"]),
    )
    assert binding.binding_canonical_sha256==bdoc["binding_canonical_sha256"]
    obs=FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=receipt["observation"]["observed_current_main_sha"],
        intervening_diff=(),
        observation_evidence_pointers=tuple(receipt["observation"]["observation_evidence_pointers"]),
    )
    report=audit_candidate_freeze_framework_subject(binding, obs, required=True)
    assert report.verdict is CandidateFreezeRevalidationVerdict.CURRENT_UNCHANGED
    assert report.licenses_candidate_materialization is True
    assert report.grants_scientific_authority is False
