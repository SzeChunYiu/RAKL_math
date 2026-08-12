"""Retrospective-support, target-blind C051 k=19 discriminator freeze."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
BASE='research/real_math/millennium/p_vs_np'
ATOM='O9d12a2a1b-C051'; CANDIDATE='C051-K19-RETROSPECTIVE-SUPPORT-DISCRIMINATOR-v1'
APP_BASE='f55355f003a25e13a8a24c65c92d525f0c8e430b'; FRAMEWORK='9da0f4d331e9ae61f1309b3a006d7a3c67fa217c'
FROZEN_AT='2026-08-12T09:48:30Z'
PATHS={
'candidate':f'{BASE}/04_candidates/O9d12a2a1b_C051_K19_RETROSPECTIVE_DISCRIMINATOR_FREEZE_20260812.json',
'evaluator_manifest':f'{BASE}/05_falsification/O9d12a2a1b_C051_K19_INERT_EVALUATOR_FREEZE_20260812.json',
'authorization':f'{BASE}/09_trace/O9d12a2a1b_C051_K19_RETROSPECTIVE_EVALUATION_AUTHORIZATION_20260812.json',
'receipt':f'{BASE}/09_trace/O9d12a2a1b_C051_K19_RETROSPECTIVE_CANDIDATE_FREEZE_RECEIPT_20260812.json'}
EVALUATOR=f'{BASE}/05_falsification/c051_k19_inert_evaluator.py'
CORRECTION=f'{BASE}/09_trace/O9d12a2a1b_C051_SUPPORT_CONTAMINATION_CORRECTION_20260812.json'

def h(v): return 'sha256:'+hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def seal(v):
 d=dict(v); d['artifact_hash']=''; d['artifact_hash']=h(d); return d
def raw(v,m): return 8+(2*v.bit_length()-1)+(2*m.bit_length()-1)+3*m*(1+v.bit_length())
def enc(v,m):
 r=raw(v,m); return r+r%2

def candidate():
 core={
 'schema_version':'1.0.0','atom_id':ATOM,'candidate_id':CANDIDATE,'frozen_at':FROZEN_AT,
 'authority':'RETROSPECTIVE_ONLY_FOR_SUPPORT_SELECTION__PROSPECTIVE_FOR_SHARED_BITS_AND_UNSAT',
 'object':'Exact classification of H_19 intersection P_20 under the unchanged C041 grammar and C048 swapped reduction.',
 'qoi':'EXACT_H19_INTERSECTION_P20_CLASSIFICATION',
 'preexposed_support_input':{
  'mathematical_credit':0,
  'parent_length_38_regime':{'v':1,'m':4,'raw_length':38,'encoded_length':38,'padding':False},
  'current_length_40_regime':{'v_values':[4,5,6,7],'m':2,'raw_length':40,'encoded_length':40,'padding':False},
  'status':'KNOWN_BEFORE_CONTEXT_FREEZE_NOT_STRICT_DISCOVERY'},
 'support_derivation_to_be_checked_not_discovered':{
  'length_formula':'R(v,m)=8+(2 bit_length(v)-1)+(2 bit_length(m)-1)+3m(1+bit_length(v)); E=R+(R mod 2)',
  'parent_exhaustion':'E(v,m)=38 iff (v,m)=(1,4) among positive canonical parameters.',
  'current_exhaustion':'E(v,m)=40 iff m=2 and bit_length(v)=3, hence v in {4,5,6,7}.',
 },
 'discriminator':{
  'predicted_result':None,
  'operation_order':['derive exact field offsets for the sole length-38 parent regime','derive exact field offsets for all four length-40 current regimes','compare h=1||suffix_19(x) with prefix_20(y) coordinate by coordinate','if any forced mismatch covers all branches, return SCOPED_OVERLAP_IMPOSSIBILITY','otherwise require explicit canonical x,y and independently prove x UNSAT before returning EXACT_OVERLAP_WITNESS'],
  'positive_certificate':'canonical length-38 x=r||c with Dec(x) UNSAT; canonical length-40 y; prefix_20(y)=1||c exactly; C048 swapped reduction retained.',
  'negative_certificate':'exhaust the one parent and four current parameter regimes and prove a forced unequal coordinate or contradiction in every product branch.',
  'allowed_results':['EXACT_OVERLAP_WITNESS','SCOPED_OVERLAP_IMPOSSIBILITY','BOUNDED_NO_MATCH_ONLY','CANNOT_CHECK'],
 },
 'proof_obligations':['PARENT_LENGTH_38_PARAMETER_EXHAUSTION','CURRENT_LENGTH_40_PARAMETER_EXHAUSTION','EXACT_PARENT_AND_CURRENT_FIELD_OFFSETS','ALL_20_SHARED_COORDINATES_ACCOUNTED_FOR','PARENT_UNSAT_PROVED_IF_SYNTAX_SURVIVES','C048_SWAPPED_REDUCTION_PRESERVED','K19_SCOPE_ONLY'],
 'falsifiers':{
  'support':['a positive (v,m) outside the frozen regimes with encoded length 38 or 40','incorrect raw or padded length arithmetic'],
  'impossibility':['one canonical length-38 UNSAT x and canonical length-40 y with prefix_20(y)=1||suffix_19(x)','one omitted grammar-product branch'],
  'positive':['one unequal shared bit','noncanonical parse','one satisfying assignment of the claimed UNSAT parent']},
 'target_access':{'shared_bits_compared':False,'field_offsets_derived':False,'parent_formula_constructed':False,'unsat_evaluated':False,'intersection_determined':False},
 'result_firewall':{'allowed_now':['freeze these exact regimes, obligations, falsifiers, and inert evaluator'],'forbidden_now':['derive any shared coordinate','construct or solve a parent formula','state or predict the intersection result','claim strict discovery for support selection']},
 'root_state':'OPEN_NO_SOLUTION_CERTIFICATE',
 'credit':{'candidate_freeze_result_credit':0,'support_selection_discovery_credit':0,'assurance_credit':0},
 'source_binding':{'application_base':APP_BASE,'live_framework_main':FRAMEWORK,'correction':CORRECTION},
 }
 identity={'candidate_id':CANDIDATE,'candidate_core_sha256':h(core)}
 return seal({**core,'candidate_identity':identity})

def documents():
 c=candidate()
 manifest=seal({'schema_version':'1.0.0','candidate_id':CANDIDATE,'evaluator':EVALUATOR,'evaluator_sha256':'sha256:'+hashlib.sha256(Path(EVALUATOR).read_bytes()).hexdigest(),'capabilities':[],'inert':True,'target_evaluation_authorized':False})
 authorization=seal({'schema_version':'1.0.0','candidate_id':CANDIDATE,'candidate_artifact_hash':c['artifact_hash'],'candidate_core_sha256':c['candidate_identity']['candidate_core_sha256'],'support_selection_authority':'RETROSPECTIVE_ONLY','shared_bit_or_unsat_evaluation_authorized':False,'licensed_next_action':'PUBLIC_SUCCESSOR_MAY_IMPLEMENT_EXACT_FROZEN_DISCRIMINATOR','root_state':'OPEN_NO_SOLUTION_CERTIFICATE'})
 receipt=seal({'schema_version':'1.0.0','receipt_id':'PNP-C051-K19-RETROSPECTIVE-CANDIDATE-FREEZE-20260812','application_base':APP_BASE,'framework_main':FRAMEWORK,'candidate_id':CANDIDATE,'bindings':{'candidate':h(c),'evaluator_manifest':h(manifest),'authorization':h(authorization),'correction':CORRECTION},'verdict':'RETROSPECTIVE_SUPPORT_INPUT__TARGET_DISCRIMINATOR_FROZEN__EVALUATION_NOT_AUTHORIZED','mathematical_result':False,'assurance_zero_credit':True})
 return {'candidate':c,'evaluator_manifest':manifest,'authorization':authorization,'receipt':receipt}
if __name__=='__main__':
 for n,d in documents().items(): Path(PATHS[n]).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
