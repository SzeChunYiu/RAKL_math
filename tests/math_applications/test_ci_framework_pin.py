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


def test_rh_strict_ci_binds_the_checked_out_application_subject() -> None:
    workflow = RH_WORKFLOW.read_text(encoding="utf-8")
    subject_expression = (
        "${{ github.event_name == 'pull_request' && "
        "github.event.pull_request.head.sha || github.sha }}"
    )

    assert f"ref: {subject_expression}" in workflow
    assert f"EXPECTED_APPLICATION_SHA: {subject_expression}" in workflow
    assert 'test "$(git rev-parse HEAD)" = "$EXPECTED_APPLICATION_SHA"' in workflow
    assert 'RAKL_MATH_SUBJECT_SHA=$EXPECTED_APPLICATION_SHA' in workflow


def test_rh_strict_ci_pins_external_actions_to_verified_commits() -> None:
    workflow = RH_WORKFLOW.read_text(encoding="utf-8")

    assert "actions/checkout@11d5960a326750d5838078e36cf38b85af677262" in workflow
    assert "actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065" in workflow
    assert "actions/checkout@v4" not in workflow
    assert "actions/setup-python@v5" not in workflow
