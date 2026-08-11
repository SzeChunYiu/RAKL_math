from __future__ import annotations

import importlib.util
import math
from pathlib import Path


MODULE_PATH = (
    Path(__file__).parents[2]
    / "research"
    / "real_math"
    / "millennium"
    / "p_vs_np"
    / "05_falsification"
    / "closure_cascade_falsifier.py"
)
SPEC = importlib.util.spec_from_file_location("pnp_c026_closure_cascade", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
c026 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c026)


def test_c026_parametric_cascade_regression() -> None:
    for m in range(3, 10):
        row = c026.check_cascade(m)
        assert row["predictions_pass"] is True
        assert row["before_cardinality"] == m + 1
        assert row["after_cardinality"] == 2**m
        assert row["before_contains_empty"] is False
        assert row["after_contains_empty"] is True
        assert row["before_fired_count"] == 0
        assert row["after_fired_count"] == m - 1


def test_c026_log_volume_marginal_is_unbounded_on_family() -> None:
    deltas = []
    for m in range(3, 20):
        row = c026.check_cascade(m)
        deltas.append(
            math.log2(int(row["after_cardinality"]))
            - math.log2(int(row["before_cardinality"]))
        )
    assert deltas[-1] > deltas[0]
    assert deltas[-1] > 10


def test_c026_scope_is_not_graph_specific() -> None:
    receipt = c026.regression_receipt(3, 6)
    assert receipt["all_predictions_pass"] is True
    assert receipt["scope"] == "generic finite source-compatible discrete spaces only"
    assert "NO_GRAPH_SPECIFIC_OR_ROOT_AUTHORITY" in str(receipt["authority"])
