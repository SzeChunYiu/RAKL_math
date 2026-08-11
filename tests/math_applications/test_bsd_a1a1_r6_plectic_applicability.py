import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"
M = BSD / "07_memory"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_r6_receipts_are_scoped_and_non_promoting():
    src = load(BSD / "00_sources" / "BSD_A1a1_R6_PLECTIC_APPLICABILITY_SOURCE_RECEIPT_20260811.json")
    ep = load(M / "BSD_A1a1_R6_CURRENT_V3_TASK_EPISODE_SHADOW_20260811.taskepisode")
    obs = load(M / "BSD_A1a1_R6_INTRINSIC_ENTRY_OBSTRUCTION_SHADOW_20260811.json")
    metrics = load(M / "BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R6.json")
    assert src["derived_scope_result"]["scope"].startswith("AUDITED_FORNEA")
    assert ep["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert ep["outcome"] == "PARTIAL_SUCCESS"
    assert obs["promotion_status"] == "PROPOSAL_SHADOW_NOT_PROTECTED"
    assert metrics["retained_semantic_novelty"]["OBSTRUCTION"] == 0
    assert metrics["application"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["outcome"]["candidate_generated"] is False
    assert metrics["gates"]["independent_mathematical_review_credit"] == 0
