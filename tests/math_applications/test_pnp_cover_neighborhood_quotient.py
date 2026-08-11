from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "research/real_math/millennium/p_vs_np/05_falsification/cover_neighborhood_quotient_gneq.py"


def _module():
    spec = importlib.util.spec_from_file_location("cover_neighborhood_quotient_gneq", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_small_gneq_row_quotient_counts() -> None:
    m = _module()
    rows = {n: m.audit(n) for n in (2, 3, 4)}
    assert (rows[2].relevant_rows, rows[2].quotient_rows, rows[2].canonical_rows, rows[2].fixed_edge_rows) == (1, 1, 1, 1)
    assert (rows[3].relevant_rows, rows[3].quotient_rows, rows[3].canonical_rows, rows[3].fixed_edge_rows) == (4, 4, 3, 2)
    assert (rows[4].relevant_rows, rows[4].quotient_rows, rows[4].canonical_rows, rows[4].fixed_edge_rows) == (17, 17, 6, 5)


def test_singleton_pair_multiplexes_every_fixed_edge_row() -> None:
    m = _module()
    assert all(m.audit(n).singleton_pair_covers_fixed_edge for n in (2, 3, 4))


def test_complete_pair_neighborhood_is_injective_on_small_gneq_rows() -> None:
    m = _module()
    for n in (2, 3, 4):
        rows = m.relevant_gneq_semifilters(n)
        signatures = [m.pair_neighborhood(row, n) for row in rows]
        assert len(signatures) == len(set(signatures))
