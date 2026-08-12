from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
METRICS = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/RAKL_CYCLE_METRICS_RH_ANA_003_ABEL_001_20260812_R10.json"


def test_r10_metrics_bind_current_framework_subject_and_result_head() -> None:
    metrics = json.loads(METRICS.read_text())
    assert metrics["schema"] == "RAKL_CYCLE_METRICS"
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["framework"]["current_rakl_main_sha"] == "182f0eff233b8608bc38c4869f52a5bb15e7e5fd"
    assert metrics["framework"]["candidate_subject_sha"] == "d594e6864f49ecf6dac394173082fbf0174b422e"
    assert metrics["rakl_math"]["cycle_base_sha"] == "6016dd6a87d87b18d8f5498e2537b043a8468c04"
    assert metrics["rakl_math"]["mathematical_result_head_sha"] == "ac726bc1ce555e957a8d2aeea91827bb68193f55"
    assert metrics["active_atom"]["fibre_snapshot_hash"] == "sha256:1cefd235555778753fb0731e783ff94cd9b888b941813a5dc00b11e302362f2f"
    assert metrics["retained_semantic_novelty_counts"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert all(value == 0 for value in metrics["protected_canonical_novelty_counts"].values())
    assert metrics["rakl_changed_action_relative_pre_memory_pre_gate_preference"]["changed"] is True
    assert metrics["gate_provenance_ci"]["root_contract"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["promotion"] == "INELIGIBLE"
