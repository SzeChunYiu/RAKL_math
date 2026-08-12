from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'research/real_math/millennium/riemann_hypothesis/09_trace/RAKL_CYCLE_METRICS_RH_ANA_003g_20260812_R8.json'

def h(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

def test_r8_cycle_metrics_are_content_bound_and_noninflationary():
    doc=json.loads(P.read_text())
    x=dict(doc); got=x.pop('artifact_hash')
    assert got=='sha256:'+h(x)
    assert doc['schema']=='RAKL_CYCLE_METRICS'
    assert doc['framework']['method_version']=='3.0.0'
    assert doc['framework']['candidate_subject_rakl_main_sha']=='5dc0627f039e8f3e1cdcb7e05cd7603860afc554'
    assert doc['rakl_math']['cycle_base_sha']=='320db4230608c5e39eb475b8239507b08ee10f9c'
    assert doc['rakl_math']['mathematical_result_head_sha']=='357f3cf12ba1d51f290ea026b05e66a39e252ab2'
    assert doc['active_atom']['fibre_snapshot_hash']=='sha256:c8a33c085f9b1a1497f4c2f7568b7fa1acc83aa447764d34aa99110c62d239ed'
    assert doc['memory_retrieval']['selected_count']==12
    assert doc['memory_retrieval']['rejected_count']==5
    assert doc['retained_semantic_novelty_counts']=={'KNOWLEDGE':1,'OPERATOR':0,'EXPERIENCE_PATTERN':1,'OBSTRUCTION':1,'RELATION':1,'PATH':1,'META_METHOD':0}
    assert all(v==0 for v in doc['protected_canonical_novelty_counts'].values())
    assert doc['gate_provenance_ci']['root_contract']=='OPEN_NO_SOLUTION_CERTIFICATE'
    assert doc['gate_provenance_ci']['promotion']=='INELIGIBLE'
    assert doc['rakl_changed_action_relative_pre_memory_pre_gate_preference']['changed'] is True
