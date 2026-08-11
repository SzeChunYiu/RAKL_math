import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAPPING = ROOT / "research/real_math/millennium/cross_problem/07_memory/XM009_JET_FAITHFULNESS_TRANSFER_MAPPING_20260811.json"
CASE = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_METHOD_CASE_STUDY_20260811_R5.md"
CANDIDATE = ROOT / "research/real_math/millennium/cross_problem/04_candidates/XM009_JET_FAITHFULNESS_HODGE_BSD_AUDIT_20260811.md"


def _order(coefficients):
    for index, coefficient in enumerate(coefficients):
        if coefficient != 0:
            return index
    return None


def test_xm009_mapping_is_shadow_and_root_closed():
    data = json.loads(MAPPING.read_text(encoding="utf-8"))
    assert data["authority"] == "PROPOSAL_SHADOW_SEARCH_CONTROL_ONLY"
    assert data["framework"]["method_version"] == "3.0.0"
    assert data["framework"]["git_sha"] == "3299072b410ac9136548dfd103e846fc7656c31e"
    assert data["application"]["base_sha"] == "812addd25a7f34d3c6272143e21d5d7db34539aa"
    assert data["application"]["execution_pin"] == "787c7e00af2a5877ccb715bc807ec14f52974e9c"
    assert data["verification"]["root_gate"] == "BLOCKED"
    assert data["verification"]["independent_mathematical_reviews"] == "0/3"


def test_xm009_transfer_contract_and_difference_witness_are_explicit():
    data = json.loads(MAPPING.read_text(encoding="utf-8"))
    transfer = data["transfer"]
    assert transfer["source_atom"].startswith("H4d1b")
    assert "COMPLEX_S_DERIVATIVE_ORDER_TWO" in transfer["target_atom"]
    assert transfer["predicted_principle"] == "JET_FAITHFULNESS_BEFORE_ORDER_TRANSFER"
    assert len(transfer["enabling_assumptions"]) >= 5
    assert len(transfer["disanalogies"]) >= 4
    assert "Only truncation/coordinate-faithfulness logic transfers" in transfer["difference_witness"]
    assert len(transfer["cheapest_falsifier"]) == 3


def test_xm009_memory_routing_changed_and_rejections_are_typed():
    data = json.loads(MAPPING.read_text(encoding="utf-8"))
    memory = data["memory_review"]
    policy = data["decision_policy"]
    assert len(memory["retrieved_ids"]) == 8
    assert len(memory["selected_ids"]) == 4
    assert len(memory["rejected_or_deferred_ids"]) == 3
    assert memory["missed_relevant_ids"].startswith("CANNOT_MEASURE")
    assert policy["rakl_changed_observable_action_preference"] is True
    assert policy["pre_memory_preference"] != policy["post_memory_pre_gate_preference"]


def test_xm009_episode_diagnosis_lesson_are_separate():
    data = json.loads(MAPPING.read_text(encoding="utf-8"))
    separation = data["episode_diagnosis_lesson_separation"]
    ids = {
        separation["episode_id"],
        separation["diagnosis_id"],
        separation["observed_failure_id"],
        separation["proposal_lesson_id"],
        separation["positive_motif_id"],
    }
    assert len(ids) == 5
    assert separation["lesson_authority"] == "PROPOSAL_SHADOW_ONLY"
    assert separation["obstruction_authority"] == "OBSERVED_ONLY_SEARCH_CONTROL"


def test_xm009_all_seven_saturation_axes_are_present():
    data = json.loads(MAPPING.read_text(encoding="utf-8"))
    expected = {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert set(data["saturation"]["axes"]) == expected
    novelty = data["saturation"]["retained_semantic_novelty"]
    assert set(novelty) == expected
    assert novelty == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }


def test_jet_faithfulness_hostile_and_positive_controls():
    # f(T)=T^2 has exact order two.
    assert _order([0, 0, 1]) == 2
    # f(T)+epsilon*T with epsilon=1 has order one.
    assert _order([0, 1, 1]) == 1
    # f(phi(U)) for f(T)=T^2 and phi(U)=U^2 is U^4.
    assert _order([0, 0, 0, 0, 1]) == 4
    # For phi(U)=2U+U^2, phi(U)^2=4U^2+4U^3+U^4 keeps order two.
    assert _order([0, 0, 4, 4, 1]) == 2


def test_case_study_preserves_local_vs_gluing_and_no_framework_promotion():
    case = CASE.read_text(encoding="utf-8")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    assert "local-to-global" in case.lower()
    assert "canonical materialized `RAKLV3State.state_fingerprint()` coverage" in case
    assert "NO_NEW_CHALLENGER_THIS_ROUND" in case
    assert "No RAKL issue is opened from this cycle" in case
    assert "No Millennium root status changes" in candidate
