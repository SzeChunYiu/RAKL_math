from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
ORACLE_DIR = ROOT / "research" / "real_math" / "millennium" / "p_vs_np" / "05_falsification"
EVALUATOR = ORACLE_DIR / "disjoint_cover_gap_census.py"


def _load_evaluator():
    sys.path.insert(0, str(ORACLE_DIR))
    try:
        spec = importlib.util.spec_from_file_location("pnp_c026_disjoint_cover_gap_census", EVALUATOR)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)


def test_c026_frozen_sample_and_exact_null_reproduce() -> None:
    module = _load_evaluator()
    result = module.run_census()

    assert result["sample_set_id"] == "C026-FRESH-M5-20260811-v1"
    assert result["sample_manifest_sha256"] == (
        "47b3502c6075d99027c609fbecbc1a637d6650a6c2ba3462cc825fb28337a831"
    )
    assert result["graph_count"] == 64
    assert result["c008_negative_control"] == {"rho": 2, "rho_disj": 2}
    assert result["strict_gap_count"] == 0
    assert result["first_strict_gap"] is None
    assert result["distribution"] == {"1->1": 20, "2->2": 44}
    assert result["output_sha256"] == (
        "024a0e9b1be6335ad3a35aedfb5bd4e425ee3e4445288ab6049fc2b11d8ad301"
    )
    assert all(row["rho_disj"] >= row["rho"] for row in result["rows"])
    assert all(not row["strict_gap"] for row in result["rows"])
