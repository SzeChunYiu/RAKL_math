import importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'research/real_math/millennium/p_vs_np';F=B/'09_trace/c048_literal_transpose_result_fixture.py';A={'result':B/'05_falsification/O9d12a2a1b_C048_LITERAL_TRANSPOSE_PROOF_CHECK_RESULT_20260812.json','saturation':B/'10_case_study/C048_LITERAL_TRANSPOSE_MATHEMATICAL_SATURATION_RECEIPT_20260812.json','episode':B/'10_case_study/C048_LITERAL_TRANSPOSE_TASK_EPISODE_20260812.json','trace':B/'09_trace/O9d12a2a1b_C048_POST_FREEZE_RESULT_TRACE_20260812.json'}
def load(p):return json.loads(p.read_text())
def module():s=importlib.util.spec_from_file_location('c048res',F);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def test_exact_result_documents():assert {n:load(p) for n,p in A.items()}==module().build_documents()
def test_math_credit_is_narrow_and_software_zero():
 r=load(A['result']);s=load(A['saturation']);assert r['evaluator_output']['verdict']=='PASS';assert r['exact_mathematical_result']['overall_repair'].startswith('NOT_ESTABLISHED');assert r['interpretation']['software_assurance_mathematical_credit']==0;assert s['mathematical_credit']['ci_schema_hash_chronology_runtime']==0;assert s['mathematical_credit']['collision_iff_overlap_transfer_condition'] is True;assert s['lesson_authority'].startswith('PROPOSAL_ONLY')
def test_trace_records_result_and_open_residual():
 t=load(A['trace']);assert [x['event_type'] for x in t['entries'][-3:]]==['FALSIFIER_RUN','RESULT_RECORDED','RESIDUAL_OPENED'];assert t['entries'][-2]['outputs']==['SCOPED_TRANSFER_LEMMA','OVERLAP_OPEN','ROOT_OPEN']
