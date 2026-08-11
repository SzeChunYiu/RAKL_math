from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"
EPISODE = YM / "09_trace" / "YM-E2_FS_GAP_BUDGET_TASK_EPISODE_20260811.json"
FAILURE = YM / "07_memory" / "YM-E2_FS_GAP_BUDGET_FAILURE_DELTA_20260811.json"
AUDIT = YM / "03_sources" / "YM-E2_FAIZAL_SHABIR_GAP_BUDGET_AUDIT_20260811.md"


def test_summability_does_not_imply_positive_residual_margin() -> None:
    delta0 = 1.0
    eps = (0.6, 0.6)
    assert sum(eps) < float("inf")
    assert delta0 - sum(eps) <= 0.0


def test_shadow_episode_cannot_mint_authority() -> None:
    episode = json.loads(EPISODE.read_text())
    assert episode["chronology_status"] == (
        "RETROSPECTIVE_RESULT_NOT_ELIGIBLE_FOR_PRE_CANDIDATE_CREDIT"
    )
    contract = episode["authority_contract"]
    assert contract["grants_tool_authority"] is False
    assert contract["grants_proof_authority"] is False
    assert contract["grants_gluing_authority"] is False
    assert contract["grants_theorem_authority"] is False
    assert contract["grants_framework_authority"] is False
    assert contract["grants_review_independence"] is False


def test_failure_scope_is_source_route_only() -> None:
    failure = json.loads(FAILURE.read_text())
    assert failure["status"] == "OBSERVED_ONLY"
    assert failure["diagnosis_authority"] == "SUPPORTED_SOURCE_ROUTE_DIAGNOSTIC"
    assert failure["authority_contract"]["grants_theorem_authority"] is False
    assert failure["authority_contract"]["grants_root_authority"] is False


def test_audit_names_exact_repair_obligation() -> None:
    text = AUDIT.read_text()
    assert "sum_k epsilon_k < delta_0" in text
    assert "C/(1-theta) < delta_0" in text
    assert "No RAKL framework mutation is authorized by this single episode." in text
