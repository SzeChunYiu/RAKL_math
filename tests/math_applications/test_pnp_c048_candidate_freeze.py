from __future__ import annotations
import hashlib,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PNP=ROOT/'research/real_math/millennium/p_vs_np'
FIXTURE=PNP/'09_trace/c048_literal_transpose_candidate_fixture.py'; EVALUATOR=PNP/'05_falsification/c048_literal_transpose_transfer_evaluator.py'
ART={"candidate":PNP/'04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_TRANSFER_CONDITION_FREEZE_20260812.json',"manifest":PNP/'05_falsification/O9d12a2a1b_C048_LITERAL_TRANSPOSE_TRANSFER_EVALUATOR_FREEZE_20260812.json',"authorization":PNP/'09_trace/O9d12a2a1b_C048_EVALUATION_AUTHORIZATION_20260812.json',"trace":PNP/'09_trace/O9d12a2a1b_C048_CANDIDATE_FREEZE_TRACE_20260812.json',"feedback":PNP/'10_feedback/C048_TRANSPOSE_TWO_INTERFACE_APPLICATION_FEEDBACK_PROPOSAL_20260812.json',"receipt":PNP/'09_trace/O9d12a2a1b_C048_CANDIDATE_FREEZE_RECEIPT_20260812.json'}
def mod():
 s=importlib.util.spec_from_file_location('c048cand',FIXTURE);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def load(p): return json.loads(p.read_text())
def test_documents_match_public_gate_parent():
 m=mod(); assert m.PRE_CANDIDATE_FREEZE_SHA=='f765a0cb27d4602eb41bc4a38887696c6a954707'; assert {n:load(p) for n,p in ART.items()}==m.build_documents()
def test_candidate_separates_collision_from_reduction_faithfulness():
 c=load(ART['candidate']); s=c['statement']; assert '(M+c,r) in G^T' in s['part_A_reduction_faithfulness']; assert 'intersects P_(k+1)' in s['part_C_collision_condition']; assert 'failed repair' in s['part_D_repair_verdict_rule']; assert c['non_guarantees'][0]=='no claim that the overlap language is nonempty at any level'; assert c['credit_boundary']['assurance_only_zero_credit']==['Git/branch/PR chronology','CI/tests','schemas/hashes/serialization','runtime/evaluator wiring']
def test_inert_freeze_has_no_result_capability():
 m=load(ART['manifest']);a=load(ART['authorization']); assert m['status']=='FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED'; assert m['evaluator']['raw_sha256']==hashlib.sha256(EVALUATOR.read_bytes()).hexdigest(); assert a['current_task_evaluator_execution_authorized'] is False; src=EVALUATOR.read_text(); assert all(x not in src for x in ('C041_fx_sat_one_sided','decode_formula','is_satisfiable','materialize_complement','subprocess'))
def test_trace_has_candidate_only_and_feedback_is_proposal_only():
 t=load(ART['trace']); assert len(t['entries'])==9 and t['entries'][-1]['event_type']=='CANDIDATE_PROPOSED'; assert 'RESULT_RECORDED' not in json.dumps(t); f=load(ART['feedback']); assert f['status']=='APPLICATION_FEEDBACK_PROPOSAL_ONLY_NOT_PROMOTED' and f['credit']['software_process_credit']==0
