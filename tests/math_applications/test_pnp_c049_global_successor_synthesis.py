import json,hashlib,copy
from pathlib import Path
R=Path(__file__).resolve().parents[2];M=R/'research/real_math/millennium/cross_problem/07_memory';O=M/'GLOBAL_MATH_ONLY_SATURATION_LEDGER_BSD_R9_SUCCESSOR_20260812.json';N=M/'GLOBAL_MATH_ONLY_SATURATION_LEDGER_PNP_C049_SUCCESSOR_20260812.json';A=M/'GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_PNP_C049_SUCCESSOR_20260812.json'
def load(p):return json.loads(p.read_text())
def items(d):return {i['item_id']:i for l in d['lanes'] for i in l['credited_items']}
def test_exactly_one_unit_preserves_predecessor():
 o,n=load(O),load(N);oi,ni=items(o),items(n);assert set(ni)-set(oi)=={'MATH-PNP-C049-K12-FIRST-ADMISSIBLE-FIXED-BIT-SEPARATION'};assert all(ni[k]==v for k,v in oi.items());assert n['totals']['mathematical_credit_units']==o['totals']['mathematical_credit_units']+1;assert n['totals']['mathematical_credit_units_by_lane']['p_vs_np']==16;assert n['totals']['mathematical_credit_units_by_type']['PROOF_OR_LEMMA']==14
def test_scope_and_distinct_cause():
 n,a=load(N),load(A);i=items(n)['MATH-PNP-C049-K12-FIRST-ADMISSIBLE-FIXED-BIT-SEPARATION'];assert 'k=12 only' in i['scope'];assert any('No conclusion for k>12' in x for x in i['non_implications']);c=a['failure_mechanisms'][-1];assert c['id']=='FM-PNP-C049-FIRST-ADMISSIBLE-FIELD-ALIGNMENT-CONFLICT';assert c['root_cause_status']=='SUPPORTED_BOUNDED_K12_EXACT_SEPARATION';assert 'k=12 only' in c['scope']
