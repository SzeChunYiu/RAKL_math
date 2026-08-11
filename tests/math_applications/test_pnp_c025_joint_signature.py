from __future__ import annotations

from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = (
    ROOT
    / "research/real_math/millennium/p_vs_np/05_falsification"
    / "joint_signature_calibration.py"
)
SPEC = importlib.util.spec_from_file_location("joint_signature_calibration", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_power_of_two_gneq_signature_calibration() -> None:
    for n in range(1, 9):
        result = MODULE.standard_power_of_two_calibration(n)
        assert result["N"] == 2**n
        assert result["width"] == n
        assert result["distinct_signature_count"] == 2**n
        assert result["covers_all_canonical_gneq_filters"] is True
        assert result["capacity_lower_bound"] == n


def test_injectivity_is_exact_canonical_separation_condition() -> None:
    assert MODULE.covers_gneq_canonical_by_signatures([(0, 0), (0, 1), (1, 0)])
    assert not MODULE.covers_gneq_canonical_by_signatures([(0, 0), (0, 1), (0, 0)])


def test_binary_capacity_floor() -> None:
    expected = {
        1: 0,
        2: 1,
        3: 2,
        4: 2,
        5: 3,
        8: 3,
        9: 4,
        16: 4,
        17: 5,
    }
    for count, width in expected.items():
        assert MODULE.minimum_binary_signature_width(count) == width


def test_candidate_scope_is_fail_closed() -> None:
    text = (
        ROOT
        / "research/real_math/millennium/p_vs_np/04_candidates/negative_history"
        / "C025_joint_signature_canonical_scope.md"
    ).read_text(encoding="utf-8")
    assert "NO NOVELTY CLAIM" in text
    assert "REJECTED AS TOO BROAD" in text
    assert "No use of this normalization outside the `G_NEQ` canonical family is licensed here." in text
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in text
