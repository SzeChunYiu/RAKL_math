"""Append-only correction for the C051 support-selection chronology.

This record corrects authority only.  It earns zero mathematical credit and
must not erase the valid mathematical context, memory, or unevaluated QoI.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

BASE = Path('research/real_math/millennium/p_vs_np')
OUTPUT = BASE / '09_trace/O9d12a2a1b_C051_SUPPORT_CONTAMINATION_CORRECTION_20260812.json'
SOURCE_GATE = BASE / '09_trace/O9d12a2a1b_C051_PRE_CANDIDATE_GATE_RECEIPT_20260812.json'
SOURCE_GATE_BLOB = '179f99f607a6659c3ff3222ac441ef04f961b510'
APPLICATION_MAIN_AT_AUDIT = 'f3275302b2198bbd15d551d57adce85c5762c013'


def _hash(value: object) -> str:
    raw=json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    return 'sha256:'+hashlib.sha256(raw).hexdigest()


def build_document() -> dict:
    document = {
        'schema_version':'1.0.0',
        'correction_id':'PNP-C051-SUPPORT-CONTAMINATION-CORRECTION-20260812',
        'atom_id':'O9d12a2a1b-C051',
        'recorded_at':'2026-08-12T09:40:59Z',
        'application_main_at_audit':APPLICATION_MAIN_AT_AUDIT,
        'supersedes_authority_fields_only':{
            'artifact':str(SOURCE_GATE),
            'git_blob':SOURCE_GATE_BLOB,
            'fields':['chronology.untouched_target_result_accessed','chronology.target_state','gate_verdicts.candidate_generation_allowed','application_authority.candidate_construction_authorized','application_authority.licensed_actions'],
        },
        'observed_pre_freeze_event':{
            'operation':'evaluated the exact canonical half-length formula over bounded (width,m) pairs and printed supported consecutive k values',
            'observed_k19_support_content':['k=19 parent half-length support includes (variable bit-length=1,m=4)','k=20 current half-length support includes (variable bit-length=3,m=2)'],
            'event_preceded_c051_context_freeze':True,
            'private_same_session_observation':True,
            'shared_bit_result_accessed':False,
            'canonical_parse_result_accessed':False,
            'unsat_result_accessed':False,
            'intersection_result_accessed':False,
        },
        'corrected_authority':{
            'strict_context_first_discovery_status':'RETROSPECTIVE_ONLY_SUPPORT_SELECTION_CONTAMINATION',
            'candidate_generation_allowed_under_original_strict_gate':False,
            'licensed_action':'FREEZE_RETROSPECTIVE_K19_DISCRIMINATOR_BEFORE_ANY_SHARED_BIT_OR_UNSAT_EVALUATION',
            'k19_support_selection_authority':'PREEXPOSED_SAME_SESSION_ZERO_DISCOVERY_CREDIT',
            'remaining_unevaluated_mathematics':['exact shared-coordinate compatibility of H_19 and P_20','canonical parent and current parses beyond support parameters','parent UNSAT condition','H_19 intersection P_20'],
            'root_state':'OPEN_NO_SOLUTION_CERTIFICATE',
        },
        'failure_diagnosis':{
            'attempted_implication':'A green strict pre-candidate packet implied k=19 had remained target-blind.',
            'exact_failure':'The same session had already computed and printed the k=19/k=20 support parameter regimes before the recorded context freeze.',
            'supported_cause':'The workflow tracked decoder/shared-bit result access but failed to classify support-spectrum calculation as target mathematical result access.',
            'competing_causes':['Git movement did not cause the error','schema validation did not cause the error','the mathematical support formula was not itself false'],
            'scope':'C051 strict discovery authority for k=19 support selection only; no claim that shared bits, UNSAT, or the intersection were evaluated.',
            'falsifier':'Evidence that the bounded support calculation occurred after the C051 context freeze, or that its output omitted the k=19/k=20 regimes, would refute this diagnosis.',
            'mathematical_repair':'Treat k=19 support as known input; prospectively freeze the exact shared-coordinate discriminator before deriving any common bit or UNSAT consequence. Do not count the repair as mathematics.',
            'proof_and_source_evidence':['same-session command receipt: bounded formula output contained (19,[(1,4)],[(3,2)])','C041 exact encoder source fixes the length formula'],
        },
        'credit':{'mathematical':0,'process_assurance':0,'new_lesson':0},
        'preservation':['do not rewrite or delete the original packet','preserve the valid context fiber and protected DifferenceWitness','mark every k=19 successor retrospective for support selection','do not call same-session correction independent review'],
        'artifact_hash':'',
    }
    document['artifact_hash']=_hash(document)
    return document

if __name__=='__main__':
    OUTPUT.write_text(json.dumps(build_document(),indent=2,sort_keys=True)+'\n')
