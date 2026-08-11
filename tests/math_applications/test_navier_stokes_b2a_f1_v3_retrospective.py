import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def load(rel):
    return json.loads((NS / rel).read_text())


def test_b2a_v3_episode_is_retrospective_and_nonpromoting():
    ep = load("07_memory/NS_B2A_F1_TASK_EPISODE_20260811.json")
    failure = load("07_memory/NS_B2A_F1_FAILURE_EXPERIENCE_20260811.json")
    trace = load("09_trace/NS_B2A_F1_RETROSPECTIVE_TRACE_20260811.json")

    assert ep["episode_id"] == "EP-NS-B2a-F1-ABSOLUTE-FLUX-20260811"
    assert ep["outcome"] == "PARTIAL_SUCCESS"
    assert ep["residual_signature"]
    assert failure["diagnosis_status"] == "OBSERVED_ONLY"
    assert failure["selected_diagnosis"] == ""
    assert failure["authority_contract"]["allowed_effect"] == "SEARCH_PRIORITY_ONLY"
    assert not failure["authority_contract"]["grants_theorem_authority"]
    assert not failure["authority_contract"]["grants_proof_authority"]
    assert not failure["authority_contract"]["grants_tool_authority"]
    assert trace["status"] == "RETROSPECTIVE_NO_PRE_CANDIDATE_CREDIT"
    assert "CANDIDATE_PROPOSED" not in {e["type"] for e in trace["events"]}


def test_b2a_fibre_separates_relevance_from_authority():
    fibre = load("07_memory/NS_B2A_F1_RETROSPECTIVE_FIBRE_20260811.json")
    by_id = {item["id"]: item for item in fibre["consulted_items"]}

    assert fibre["status"] == "RETROSPECTIVE_SHADOW_ONLY"
    assert by_id["F-NS-B1a-C001-PRESSURE-SUMMABILITY"]["authority"] == "SUPPORTED_SCOPED_ON_MAIN"
    assert by_id["F-NS-B1a1-ABSOLUTE-LOCAL-ENERGY-SCALE-CURRENCY"]["authority"] == "NONCANONICAL_PENDING_ONLY"
    assert by_id["NS-BACKWARD-UNIQUENESS"]["role"] == "rejected"
    assert any("zero pre-candidate credit" in w for w in fibre["unresolved_warnings"])


def test_b2a_saturation_tracks_all_seven_axes_without_completeness():
    sat = load("07_memory/NS_B2A_F1_SATURATION_ROUND_20260811.json")
    assert set(sat["retained_novelty"]) == {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION",
        "RELATION", "PATH", "META_METHOD"
    }
    assert sat["bounded_saturation_claim"] is False
    assert sat["grants_absolute_completeness"] is False
    assert {"OBSTRUCTION", "PATH", "META_METHOD"} <= set(sat["residual_axes"])


def test_b2a_child_requires_fresh_context_and_result_is_scoped():
    result = (NS / "01_frontier" / "NS-B2a_F1_ABSOLUTE_CUTOFF_FLUX_CALIBRATION_20260811.md").read_text()
    child = (NS / "02_problem_dag" / "NS_B2A1_delta.yaml").read_text()

    assert "F-NS-B2a-F1-ABSOLUTE-CUTOFF-FLUX-NONDECAY" in result
    assert "does **not** show that the actual signed flux is nonzero" in result
    assert "candidate_generation_gate:" in child
    assert "allowed: false" in child
    assert "EULER_TAIL_TIGHTNESS_OR_SIGNED_FLUX" in child
