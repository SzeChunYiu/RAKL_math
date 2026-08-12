import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIBRE = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1c1a_FIBRE_RECEIPT_20260811_R7.json"
METRICS = ROOT / "research/real_math/millennium/yang_mills/10_case_study/YM-S1c1a_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260811_R7.json"
AUDIT = ROOT / "research/real_math/millennium/yang_mills/00_sources/YM-S1c1a_AF_IR_GLUING_SOURCE_AUDIT_20260811_R7.md"


def test_frozen_fibre_is_shadow_and_root_open():
    data = json.loads(FIBRE.read_text())
    assert data["active_atom"] == "YM-S1c1a"
    assert data["root"]["state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert data["authority"] == "PROPOSAL_SHADOW_FROZEN_CONTEXT_ROOT_AUTHORITY_NONE"
    assert len(data["fibre_snapshot_hash"]) == 64
    assert data["framework"]["method_version"] == "3.0.0"


def test_case_study_has_mandatory_v3_telemetry_and_zero_retained_novelty():
    data = json.loads(METRICS.read_text())
    metrics = data["RAKL_CYCLE_METRICS"]
    case = data["RAKL_METHOD_CASE_STUDY"]
    assert metrics["active_atom"] == "YM-S1c1a"
    assert metrics["outcome"].startswith("PARTIAL_SUCCESS_SOURCE_ROUTE_REFINED")
    assert set(metrics["retained_semantic_novelty"]) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert all(v == 0 for v in metrics["retained_semantic_novelty"].values())
    assert data["TaskEpisode"]["authority"] == "PROPOSAL_SHADOW_NO_PROMOTION_AUTHORITY"
    assert case["failure_categories"]["gluing"] is True
    assert metrics["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["independent_mathematical_reviews"] == 0


def test_source_audit_preserves_scoped_claims_and_hostile_controls():
    text = AUDIT.read_text()
    assert "ALTERNATIVE_SMALL_G_BARE_ENTRY_LANE_PRESENT_IN_SOURCE" in text
    assert "DISPLAYED_AF_IR_DIFFERENCE_BOUNDS_DO_NOT_ESTABLISH_SUMMABILITY" in text
    assert "THEOREM_10_8_WRITTEN_RECURSION_GIVES_BOUNDEDNESS_NOT_EQUALITY" in text
    assert "does **not** prove that the actual inter-trajectory difference" in text
    assert "Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`" in text


def test_hostile_control_math_is_exact():
    # Finite-horizon witnesses to the generic inference failures.  This is not a
    # Yang--Mills proof and not a numerical substitute for one.
    eps = [0.0] * 32
    d = [1.0]
    for e in eps:
        d.append(d[-1] + e)
    assert all(x == 1.0 for x in d)  # summable defects do not force D_k -> 0

    theta = 0.5
    x = 0.0
    xs = []
    for k in range(1, 200):
        x = theta * x + 1.0 / k
        xs.append(x)
    assert all(xs[k - 1] >= 1.0 / k for k in range(1, 200))
    # Equality forcing has harmonic lower bound, so the abstract recurrence
    # shape cannot license an l1 conclusion.
