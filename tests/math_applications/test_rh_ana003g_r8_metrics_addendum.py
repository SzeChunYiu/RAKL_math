from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'research/real_math/millennium/riemann_hypothesis/09_trace/RAKL_CYCLE_METRICS_ADDENDUM_RH_ANA_003g_20260812_R8.json'

def h(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

def test_r8_metrics_addendum_is_content_bound_and_fail_closed():
    doc=json.loads(P.read_text())
    x=dict(doc); got=x.pop('artifact_hash')
    assert got=='sha256:'+h(x)
    assert doc['base_metrics_artifact_hash']=='sha256:3ded325299ed299eca0e780f996b643c89ffe09ded12024905b734a6445cac5b'
    assert doc['late_observations']['result_subject_focused_ci']['conclusion']=='success'
    assert doc['late_observations']['result_subject_full_application_ci']['conclusion']=='failure'
    assert doc['late_observations']['successor_issue']['issue_number']==324
    assert doc['root_status']=='OPEN_NO_SOLUTION_CERTIFICATE'
