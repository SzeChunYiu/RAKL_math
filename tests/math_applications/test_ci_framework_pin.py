from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RH_WORKFLOW = ROOT / ".github/workflows/rh-spectral-assurance.yml"


def test_rh_strict_ci_uses_the_exact_application_framework_pin() -> None:
    workflow = RH_WORKFLOW.read_text(encoding="utf-8")

    assert "submodules: recursive" in workflow
    assert "git rev-parse HEAD:framework/RAKL" in workflow
    assert "git -C framework/RAKL rev-parse HEAD" in workflow
    assert "tools/run_application_tests.py --framework framework/RAKL" in workflow
    assert "git clone --depth 1 https://github.com/SzeChunYiu/RAKL.git" not in workflow
    assert "/tmp/rakl-framework" not in workflow
