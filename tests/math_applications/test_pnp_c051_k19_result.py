from __future__ import annotations
import importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; P=ROOT/'research/real_math/millennium/p_vs_np'; F=P/'09_trace/c051_k19_result_fixture.py'; C041=P/'04_candidates/C041_fx_sat_one_sided.py'
def mod(name,path):
 s=importlib.util.spec_from_file_location(name,path);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
def test_result_documents_match_fixture_and_seven_fields():
 m=mod('c051result',F);docs=m.documents()
 for n,d in docs.items(): assert json.loads((ROOT/m.PATHS[n]).read_text())==d
 seven=docs['lesson']['seven_field_math_lesson']; assert set(seven)=={'attempted_implication','exact_result_or_failure','supported_and_competing_causes','scope','falsifier','mathematical_repair','proof_and_source_evidence'}
 assert docs['result']['theorem']=='H_19 intersection P_20 = emptyset'; assert docs['dag']['root_state']=='OPEN_NO_SOLUTION_CERTIFICATE'
def test_exact_length_regimes_and_bit3_separation():
 c=mod('c041_c051',C041)
 pairs38=[];pairs40=[]
 for v in range(1,64):
  for m in range(1,16):
   f=c.Formula3CNF(v,tuple((((1,False),(1,False),(1,False))) for _ in range(m)),'TEST')
   n=len(c.encode_formula(f))
   if n==38:pairs38.append((v,m))
   if n==40:pairs40.append((v,m))
 assert pairs38==[(1,4)];assert pairs40==[(4,2),(5,2),(6,2),(7,2)]
 z=(1,False);nz=(1,True);x=c.encode_formula(c.Formula3CNF(1,((z,z,z),(nz,nz,nz),(z,z,z),(z,z,z)),'TEST'))
 assert x=='11100101100100010101111111010101010101'; assert not c.is_satisfiable(c.decode_formula(x))
 h='1'+x[19:];assert h[3]=='1'
 for v in range(4,8):
  f=c.Formula3CNF(v,(((1,False),(1,False),(1,False)),((1,False),(1,False),(1,False))),'TEST');p=c.encode_formula(f)[:20];assert p[3]=='0';assert h!=p
def test_trace_is_hash_chained():
 m=mod('c051trace',F);t=m.documents()['trace'];prev=''
 for e in t['entries']:
  assert e['previous_event_hash']==prev; core=dict(e);ah=core.pop('artifact_hash');assert m.h(core)==ah;prev=ah
