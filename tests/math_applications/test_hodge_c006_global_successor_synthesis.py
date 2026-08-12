from __future__ import annotations
import copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
M=ROOT/'research/real_math/millennium/cross_problem/07_memory'
OLD_L=M/'GLOBAL_MATH_ONLY_SATURATION_LEDGER_PNP_C049_SUCCESSOR_20260812.json'
NEW_L=M/'GLOBAL_MATH_ONLY_SATURATION_LEDGER_HODGE_C006_SUCCESSOR_20260812.json'
OLD_A=M/'GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_PNP_C049_SUCCESSOR_20260812.json'
NEW_A=M/'GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_HODGE_C006_SUCCESSOR_20260812.json'
MERGED='bc55996ef611c93fcc85162f5a2dfe5450cef8b1'
def load(p): return json.loads(p.read_text())
def canon(d):
 x=copy.deepcopy(d);x['artifact_hash']=''
 return 'sha256:'+hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def items(d): return {i['item_id']:i for lane in d['lanes'] for i in lane['credited_items']}
def test_successors_preserve_exact_predecessors_and_hashes():
 ol,nl,oa,na=map(load,(OLD_L,NEW_L,OLD_A,NEW_A))
 assert nl['successor_lineage']['predecessor_raw_sha256']==hashlib.sha256(OLD_L.read_bytes()).hexdigest()
 assert na['successor_lineage']['predecessor_raw_sha256']==hashlib.sha256(OLD_A.read_bytes()).hexdigest()
 assert nl['successor_lineage']['predecessor_artifact_hash']==ol['artifact_hash']
 assert na['successor_lineage']['predecessor_artifact_hash']==oa['artifact_hash']
 assert nl['authority_universe']['repository_sha']==na['authority_universe']['repository_sha']==MERGED
 assert nl['artifact_hash']==canon(nl);assert na['artifact_hash']==canon(na)
def test_exactly_one_math_unit_and_zero_software_credit():
 old,new=load(OLD_L),load(NEW_L);oi,ni=items(old),items(new)
 ident='MATH-HODGE-C006-RAMIFICATION-POINTWISE-DIFFERENTIAL-NONIMPLICATION'
 assert set(ni)-set(oi)=={ident};assert all(ni[k]==v for k,v in oi.items())
 i=ni[ident];assert i['credit_type']=='EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE';assert i['credit_units']==1
 assert 'Q[u] -> Q[t]' in i['exact_claim'] and 'd pi_0=0' in i['exact_claim']
 assert new['totals']['mathematical_credit_units']==43
 assert new['totals']['mathematical_credit_units_by_lane']['hodge_conjecture']==4
 assert new['totals']['mathematical_credit_units_by_type']['EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE']==16
 boundary=' '.join(i['non_implications']).lower()
 for term in ('git','ci','tests','schemas','hashes','chronology','telemetry'): assert term in boundary
 assert all((ROOT/p).is_file() for p in i['evidence_pointers'])
def test_atlas_records_supported_cause_competitors_scope_falsifier_and_repair():
 old,new=load(OLD_A),load(NEW_A);ob={x['id']:x for x in old['failure_mechanisms']};nb={x['id']:x for x in new['failure_mechanisms']}
 ident='FM-HODGE-C006-RAMIFICATION-FIRST-ORDER-INVISIBILITY'
 assert set(nb)-set(ob)=={ident};assert all(nb[k]==v for k,v in ob.items())
 x=nb[ident];assert x['root_cause_status']=='VERIFIED_SCOPED_EXPLICIT_COUNTEREXAMPLE'
 assert x['supported_causes'] and len(x['competing_causes'])==3
 assert 't -> t^2' in x['falsifier'];assert 'direct image geometry' in x['repair']
 assert any('not an actual Hodge-incidence' in s for s in x['scope'])
 assert all((ROOT/p).is_file() for p in x['evidence'])
