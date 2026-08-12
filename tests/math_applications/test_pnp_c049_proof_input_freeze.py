import importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'research/real_math/millennium/p_vs_np';F=B/'09_trace/c049_k12_proof_input_fixture.py';A={'certificate':B/'04_candidates/O9d12a2a1b_C049_K12_PROOF_CERTIFICATE_FREEZE_20260812.json','authorization':B/'09_trace/O9d12a2a1b_C049_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json','chronology':B/'09_trace/O9d12a2a1b_C049_PUBLIC_FREEZE_CHRONOLOGY_20260812.json'}
def load(p):return json.loads(p.read_text())
def mod():s=importlib.util.spec_from_file_location('pii',F);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def test_documents_exact():assert {n:load(p) for n,p in A.items()}==mod().build_documents()
def test_scope_and_authorization():
 c=load(A['certificate']);a=load(A['authorization']);ch=load(A['chronology']);assert c['scoped_conclusion_if_records_validate'].endswith('no conclusion for any k>12.');assert [x['status'] for x in c['obligations']]==['PROVED']*6;assert c['credit']['software_process']==0;assert a['proof_check_authorized'] is True and a['decoder_access_authorized'] is False;assert ch['status']=='TO_BE_PUBLISHED_BEFORE_EVALUATOR_EXECUTION' and ch['scope']=='k=12 only'
