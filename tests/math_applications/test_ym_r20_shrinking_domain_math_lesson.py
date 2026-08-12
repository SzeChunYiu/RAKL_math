from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'research/real_math/millennium/yang_mills'
def load(rel): return json.loads((BASE/rel).read_text())
def test_r20_lesson_is_mathematical_and_scoped():
 d=load('07_memory/YM-S1a2i_R20_MATHEMATICAL_LESSON_20260812.json')
 assert len(d['exact_mathematical_result'])==4
 assert len(d['supported_causes'])==4
 assert len(d['competing_causes'])==3
 assert 'C_2' in ' '.join(d['exact_mathematical_result'])
 assert 'not a source-wide refutation' in d['scope']
 assert 'next-radius margin' in d['mathematical_falsifier']
 assert all((ROOT/p).exists() or p.startswith('Jonathan') for p in d['proof_or_source_evidence'])
def test_old_radius_does_not_imply_new_radius():
 g,gp,c,x=1,.5,1,.75
 assert gp<=g and x<=c*g*g and not x<=c*gp*gp
def test_relevant_margin_condition_is_exact():
 C2,cK=.75,2
 threshold=C2*(1+cK)/(1-C2)
 for c_lambda in (threshold,threshold+1):
  assert C2*c_lambda+C2*(1+cK)<=c_lambda
 C2=1.0
 assert not (C2*100+C2*(1+cK)<=100)
