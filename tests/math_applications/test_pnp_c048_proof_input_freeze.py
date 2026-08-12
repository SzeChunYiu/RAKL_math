import importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'research/real_math/millennium/p_vs_np';F=B/'09_trace/c048_literal_transpose_proof_input_fixture.py';A={'certificate':B/'04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_PROOF_CERTIFICATE_FREEZE_20260812.json','authorization':B/'09_trace/O9d12a2a1b_C048_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json','chronology':B/'09_trace/O9d12a2a1b_C048_PUBLIC_FREEZE_CHRONOLOGY_20260812.json'}
def load(p):return json.loads(p.read_text())
def module():s=importlib.util.spec_from_file_location('c048inputs',F);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def test_exact_docs_and_math_scope():
 m=module();assert {n:load(p) for n,p in A.items()}==m.build_documents();c=load(A['certificate']);assert [x['status'] for x in c['obligations']]==['PROVED']*5;assert c['mathematical_verdict_if_records_validate']['overall_repair'].startswith('NOT_YET_ESTABLISHED');assert c['credit']['software_process']==0
def test_publication_precedes_execution_and_forbids_target():
 a=load(A['authorization']);ch=load(A['chronology']);assert a['proof_check_authorized'] is True and a['target_enumeration_authorized'] is False;assert ch['status']=='TO_BE_PUBLISHED_BEFORE_EVALUATOR_EXECUTION';assert ch['target_access']=={'decoder_executed':False,'evaluator_executed':False,'target_enumerated':False}
