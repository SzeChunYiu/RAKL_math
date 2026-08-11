from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAPPING = ROOT / "research/real_math/millennium/cross_problem/07_memory/XM006_TRANSFER_MAPPING_20260811.json"
AUDIT = ROOT / "research/real_math/millennium/cross_problem/04_candidates/XM006_DIAGONAL_UNIFORMITY_AUDIT_20260811.md"
METRICS = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_CYCLE_METRICS_XM006_20260811_R1.json"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_xm006_is_retrospective_and_non_escalating() -> None:
    mapping = _load(MAPPING)
    assert mapping["status"].startswith("RETROSPECTIVE_TRANSFER_MAPPING")
    assert "NO_PRE_ACTION_OR_PRE_CANDIDATE_CREDIT" in mapping["status"]
    assert mapping["authority"].startswith("RETROSPECTIVE_TRANSFER_CALIBRATION")
    assert "NO_YANG_MILLS_THEOREM" in mapping["authority"]
    assert mapping["framework_authority"]["main_sha"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert mapping["source_atom"]["failure_id"] == "F-NS-B1a1-SCALE-NEUTRAL-LOCAL-ENERGY-LEDGER"
    assert mapping["source_atom"]["process_authority"] == "RETROSPECTIVE_METHOD_EVIDENCE_ONLY_PENDING_ISSUE_134_SUCCESSOR"


def test_pointwise_common_rate_does_not_imply_diagonal_rate() -> None:
    q = 0.5

    def m(n: int, k: int) -> float:
        return q ** max(n - k, 0)

    for k in (1, 2, 5, 10):
        # Exact family identity for the fixed-source tail.
        for n in (k + 1, k + 7, k + 50):
            assert m(n, k) == q ** (n - k)
        # The nth-root rate approaches the same q for every fixed k.
        n = 100_000
        fixed_root = math.exp(math.log(m(n, k)) / n)
        assert abs(fixed_root - q) < 1e-4

    # A moving source can defeat the pointwise conclusion completely.
    for n in (1, 2, 5, 10, 100, 1000):
        assert m(n, n) == 1.0
        assert m(n, n) ** (1.0 / n) == 1.0
        assert max(m(n, k) for k in range(1, n + 2)) == 1.0


def test_prefactor_growth_is_the_exact_missing_uniformity_coordinate() -> None:
    q = 0.4
    # For k=n, C_k=q^{-k}, so C_k^(1/n)=q^{-1} and the effective rate is 1.
    for n in (2, 5, 20):
        c = q ** (-n)
        effective_rate = q * c ** (1.0 / n)
        assert math.isclose(effective_rate, 1.0, rel_tol=1e-12, abs_tol=1e-12)

    # A subexponential prefactor exp(sqrt(n)) has nth-root factor -> 1.
    for n in (10_000, 40_000):
        factor = math.exp(math.sqrt(n) / n)
        assert factor < 1.02
        assert q * factor < 1.0


def test_metrics_cover_all_seven_axes_and_do_not_count_raw_growth() -> None:
    metrics = _load(METRICS)
    axes = metrics["retained_semantic_novelty"]
    assert set(axes) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert axes == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 1,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["framework_learning"]["promoted_new_lesson_count"] == 0
    assert metrics["framework_learning"]["promoted_new_tool_count"] == 0
    assert metrics["framework_learning"]["promoted_new_meta_method_count"] == 0
    assert all(metrics["raw_growth_not_learning"].values())
    assert metrics["rakl_action_counterfactual"]["status"] == "CANNOT_MEASURE"
    assert metrics["gate_provenance_ci"]["xm006_chronology"] == "RETROSPECTIVE_ONLY"


def test_metrics_self_hash_and_scientific_subject_binding() -> None:
    metrics = _load(METRICS)
    stored = metrics.pop("artifact_hash")
    canonical = json.dumps(metrics, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    assert stored == "sha256:" + hashlib.sha256(canonical).hexdigest()
    assert metrics["application"]["scientific_subject_sha"] == "499932240c81009b2ae05c5576face37289dc981"


def test_audit_preserves_scope_and_names_primary_target_source() -> None:
    text = AUDIT.read_text(encoding="utf-8")
    assert "Shen, Rongchan Zhu, Xiangchan Zhu" in text
    assert "10.1007/s00220-022-04609-1" in text
    assert "not** a claim that the Shen–Zhu–Zhu source prefactor actually grows" in text
    assert "Issue #124 already owns root-coordinate preservation" in text
    assert "Root authority: unchanged" in text
