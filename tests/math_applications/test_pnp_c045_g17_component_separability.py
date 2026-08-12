from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/'research/real_math/millennium/p_vs_np/05_falsification/c045_g17_component_separability.py'
spec=spec_from_file_location('c045',PATH); mod=module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod)

def test_c045_finite_calibration():
    out=mod.verify()
    assert out['unsat_word_count']==10
    assert out['new_edge_count']==10
    assert out['local_uncovered_active_cells']==0
    assert out['status']=='CALIBRATION_MATCH'
