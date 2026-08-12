import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"


def _load(rel):
    return json.loads((BASE / rel).read_text())


def test_c008_fibre_binds_current_framework_and_application_base():
    fibre = _load("01_frontier/H4d1c_C008_PRE_VERIFICATION_FIBRE_20260812.json")
    assert fibre["framework"]["method_version"] == "3.0.0"
    assert fibre["framework"]["main_sha"] == "8db3343dfb764c9a139f9ba76f6f44c76eaf86de"
    assert fibre["application"]["base_main_sha"] == "02c5fb7764116cf075d8dd5efd7b6fe835275ab9"
    assert fibre["application"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert fibre["chronology"]["status"] == "RETROSPECTIVE_HYPOTHESIS_SEED_PROSPECTIVE_VERIFICATION_ONLY"


def test_c008_keeps_episode_diagnosis_obstruction_and_lesson_distinct():
    episode = json.loads((BASE / "07_memory/H4d1c_C008_TASK_EPISODE_SHADOW_20260812.jsonl").read_text())
    diagnosis = _load("07_memory/H4d1c_C008_DIAGNOSIS_20260812.json")
    obstruction = _load("07_memory/H4d1c_C008_OBSTRUCTION_20260812.json")
    lesson = _load("07_memory/H4d1c_C008_CANDIDATE_LESSON_20260812.json")
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert diagnosis["episode_id"] == episode["episode_id"]
    assert obstruction["derived_from_episode_id"] == episode["episode_id"]
    assert lesson["supporting_episode_ids"] == [episode["episode_id"]]
    assert diagnosis["diagnosis_id"] != obstruction["obstruction_id"] != lesson["lesson_id"]


def test_c008_root_and_review_gates_remain_closed():
    review = _load("08_reviews/H4d1c_C008_EXPERT_CELL_REVIEW_20260812.json")
    failure = _load("07_memory/H4d1c_C008_PROCESS_FAILURE_20260812.json")
    assert review["independent_reviews"] == 0
    assert review["required_for_root"] == 3
    assert failure["mathematical_failure"] is False
    assert failure["category"] == "META_POLICY_CHRONOLOGY"
