from __future__ import annotations
import importlib.util,json
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[2]; P=ROOT/'research/real_math/millennium/p_vs_np'
F=P/'09_trace/c051_k19_retrospective_candidate_fixture.py'; E=P/'05_falsification/c051_k19_inert_evaluator.py'
def mod(name,path):
 s=importlib.util.spec_from_file_location(name,path); assert s and s.loader; m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def test_documents_match_and_target_stays_unevaluated():
 m=mod('c051candidate',F); docs=m.documents()
 for n,d in docs.items(): assert json.loads((ROOT/m.PATHS[n]).read_text())==d
 c=docs['candidate']; assert c['preexposed_support_input']['mathematical_credit']==0
 assert c['target_access']=={'shared_bits_compared':False,'field_offsets_derived':False,'parent_formula_constructed':False,'unsat_evaluated':False,'intersection_determined':False}
 assert c['discriminator']['predicted_result'] is None
 assert docs['authorization']['shared_bit_or_unsat_evaluation_authorized'] is False
 assert c['root_state']=='OPEN_NO_SOLUTION_CERTIFICATE'
def test_support_regimes_are_exact_bounded_arithmetic():
 m=mod('c051arithmetic',F)
 assert [(v,k) for v in range(1,32) for k in range(1,10) if m.enc(v,k)==38]==[(1,4)]
 assert [(v,k) for v in range(1,32) for k in range(1,10) if m.enc(v,k)==40]==[(4,2),(5,2),(6,2),(7,2)]
def test_evaluator_is_inert():
 m=mod('c051inert',E)
 with pytest.raises(m.TargetEvaluationNotAuthorized): m.evaluate_target()
