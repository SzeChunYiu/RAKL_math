from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
CLASSIFIER = BASE / "04_candidates/O9d12a2a1b_C052_TARGET_BLIND_CLASSIFIER_IDENTITY_20260812.json"
FALSIFIER = BASE / "05_falsification/O9d12a2a1b_C052_INDEPENDENT_HOSTILE_FALSIFIER_IDENTITY_20260812.json"
AUTHORIZATION = BASE / "09_trace/O9d12a2a1b_C052_EVALUATION_AUTHORIZATION_20260812.json"
REVALIDATION = BASE / "09_trace/O9d12a2a1b_C052_FRAMEWORK_REVALIDATION_7A95860_20260812.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def raw_sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def test_c052_evaluation_authorization_binds_public_identity_bytes() -> None:
    authorization = load(AUTHORIZATION)
    assert authorization["identity_public_merge"] == "3ebde341484e6781796229d3b2328def257deae0"
    assert authorization["identities"] == {
        "classifier_raw_sha256": raw_sha(CLASSIFIER),
        "falsifier_raw_sha256": raw_sha(FALSIFIER),
    }
    assert authorization["chronology_at_freeze"] == {
        "classifier_implementation_exists": False,
        "falsifier_implementation_exists": False,
        "hostile_cell_materialized": False,
        "regressions_executed": False,
        "native_parametric_evaluation_executed": False,
        "decoder_sat_overlap_executed": False,
    }


def test_c052_authorization_freezes_hostile_selection_and_execution_order() -> None:
    authorization = load(AUTHORIZATION)
    hostile = authorization["hostile_world_selection"]
    assert hostile["selection_rule_id"] == (
        "INDEPENDENT-SYMBOLIC-SUPPORT-SOLVER-WITH-NO-FORCED-MAGIC-CONFLICT-v1"
    )
    assert hostile["ordering"] == "LEXICOGRAPHIC_ASCENDING"
    assert hostile["bounded_domain"] == {
        "k": [8, 128],
        "a": [1, 8],
        "m": [2, 32],
        "a_plus": [1, 8],
        "m_plus": [1, 32],
    }
    assert hostile["native_target_status"] == "CONTROLLED_HOSTILE_WORLD_NOT_A_NATIVE_TARGET"
    assert authorization["mandatory_execution_order"][:3] == [
        "C050-k15-bounded-regression",
        "C051-k19-bounded-regression",
        "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1",
    ]
    assert authorization["native_parametric_evaluation_gate"] == (
        "BLOCKED_UNLESS_ALL_THREE_CONTROLLED_WORLDS_PASS"
    )
    assert authorization["forbidden_capabilities"] == [
        "decoder import or execution",
        "SAT or UNSAT execution",
        "overlap comparison",
        "native target-k selection before controlled-world pass",
    ]


def test_c052_latest_framework_revalidation_is_non_authorizing_mathematically() -> None:
    observation = load(REVALIDATION)
    assert observation["observed_current_main_sha"] == "7a95860924f73c02113d11d3837ea22eefa8cc44"
    assert observation["protected_mathematical_gate_files_changed"] == []
    assert observation["new_modules_wired_into_c052_gate"] is False
    assert observation["mathematical_result_credit"] == 0
    assert observation["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"

