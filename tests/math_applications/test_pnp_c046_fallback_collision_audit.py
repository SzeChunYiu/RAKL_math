from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECODER = ROOT / "research/real_math/millennium/p_vs_np/04_candidates/C041_fx_sat_one_sided.py"

spec = spec_from_file_location("pnp_c041_frozen_decoder_for_c046", DECODER)
assert spec is not None and spec.loader is not None
fx = module_from_spec(spec)
spec.loader.exec_module(fx)


def test_all_zero_fallback_creates_g17_row_collision():
    word = fx.cross_word(16, 0, 0)
    assert word == "0" * 32
    formula = fx.decode_formula(word)
    assert formula.decoder_branch == "ALL_ZERO_SHORT_CONTRADICTION"
    assert not fx.is_satisfiable(formula)
    assert fx.complement_contains(17, 0, 1 << 16)
    assert fx.complement_contains(16, 0, 0)


def test_fallback_row_collision_is_uniform_for_small_exact_levels():
    for parent_level in range(2, 8):
        assert fx.cross_word(parent_level, 0, 0) == "0" * (2 * parent_level)
        assert fx.complement_contains(parent_level + 1, 0, 1 << parent_level)
        assert fx.complement_contains(parent_level, 0, 0)
