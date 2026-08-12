from __future__ import annotations
import importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FIXTURE=ROOT/'research/real_math/millennium/p_vs_np/09_trace/c051_support_contamination_correction_fixture.py'
RECORD=ROOT/'research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C051_SUPPORT_CONTAMINATION_CORRECTION_20260812.json'

def module():
    spec=importlib.util.spec_from_file_location('c051_correction',FIXTURE); assert spec and spec.loader
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

def test_c051_correction_matches_fixture_and_fails_strict_gate_closed():
    doc=json.loads(RECORD.read_text())
    assert doc==module().build_document()
    assert doc['corrected_authority']['candidate_generation_allowed_under_original_strict_gate'] is False
    assert doc['corrected_authority']['strict_context_first_discovery_status'].startswith('RETROSPECTIVE_ONLY')
    assert doc['observed_pre_freeze_event']['intersection_result_accessed'] is False
    assert doc['credit']=={'mathematical':0,'process_assurance':0,'new_lesson':0}

def test_c051_correction_preserves_exact_open_mathematical_residual():
    doc=json.loads(RECORD.read_text())
    residual=doc['corrected_authority']['remaining_unevaluated_mathematics']
    assert 'exact shared-coordinate compatibility of H_19 and P_20' in residual
    assert 'H_19 intersection P_20' in residual
    assert doc['corrected_authority']['root_state']=='OPEN_NO_SOLUTION_CERTIFICATE'
