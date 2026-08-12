import importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'research/real_math/millennium/p_vs_np';F=B/'09_trace/c049_k12_result_fixture.py';A={'result':B/'05_falsification/O9d12a2a1b_C049_K12_PROOF_CHECK_RESULT_20260812.json','diagnosis':B/'07_memory/O9d12a2a1b_C049_K12_OVERLAP_DIAGNOSIS_20260812.json','saturation':B/'10_case_study/C049_K12_OVERLAP_MATHEMATICAL_SATURATION_RECEIPT_20260812.json','episode':B/'10_case_study/C049_K12_OVERLAP_TASK_EPISODE_20260812.json','trace':B/'09_trace/O9d12a2a1b_C049_POST_FREEZE_RESULT_TRACE_20260812.json'}
def load(p):return json.loads(p.read_text())
def mod():s=importlib.util.spec_from_file_location('r49x',F);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def test_exact_docs():assert {n:load(p) for n,p in A.items()}==mod().build_documents()
def test_result_is_pass_but_strictly_k12():
 r=load(A['result']);s=load(A['saturation']);assert r['evaluator_output']['verdict']=='PASS';assert r['exact_mathematical_result']['lemma']=='H_12 intersection P_13 is empty.';assert r['exact_mathematical_result']['scope_consequence'].endswith('no conclusion for k>12');assert r['credit']['software_process']==0 and s['mathematical_credit']['ci_schema_hash_chronology_runtime']==0;assert s['lesson_authority'].startswith('PROPOSAL_ONLY')
def test_diagnosis_and_trace_preserve_open_residual():
 d=load(A['diagnosis']);t=load(A['trace']);assert d['cause']['status']=='SUPPORTED_BOUNDED';assert 'k=12 only' in d['scope'];assert [x['event_type'] for x in t['entries'][-3:]]==['FALSIFIER_RUN','RESULT_RECORDED','RESIDUAL_OPENED'];assert t['entries'][-2]['outputs']==['H12_INTERSECTION_P13_EMPTY','K_GT_12_OPEN','ROOT_OPEN']
