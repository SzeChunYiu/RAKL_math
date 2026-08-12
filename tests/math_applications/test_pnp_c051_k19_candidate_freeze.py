from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c051_k19_candidate_freeze_fixture.py"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C051_K19_ALIGNMENT_DISCRIMINATOR_FREEZE_20260812.json"
EVALUATOR = PNP / "05_falsification/c051_k19_alignment_evaluator.py"


def module():
    spec = importlib.util.spec_from_file_location("c051_k19_candidate_freeze", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_candidate_document_matches_prospective_fixture() -> None:
    observed = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    assert observed == module().build()
    assert observed["chronology"] == {
        "evaluator_executed": False,
        "frozen_at": "2026-08-12T09:44:24Z",
        "generic_target_result_accessed": True,
        "quarantined_families": ["k=13"],
        "result_artifact": None,
        "target_state": "K13_QUARANTINED_PROCESS_CONTAMINATION__K19_TARGET_RESULT_UNACCESSED",
        "untouched_k19_target_result_accessed": False,
    }
    assert observed["candidate_identity"]["candidate_id"] == "C051-K19-TARGET-BLIND-SYNCHRONIZED-DISCRIMINATOR-v1"
    assert observed["candidate"]["parent_length_classification"]["claim"].endswith("v=1,m=4.")
    assert observed["candidate"]["current_length_classification"]["claim"].endswith("4<=v<=7,m=2.")
    assert observed["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_freeze_contains_no_evaluated_result_or_result_receipt() -> None:
    observed = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    serialized = json.dumps(observed, sort_keys=True)
    assert "parent_signs" not in serialized
    assert "shared_label" not in serialized
    assert not (PNP / "05_falsification/O9d12a2a1b_C051_K19_RESULT_20260812.json").exists()
    assert EVALUATOR.exists()


def test_assurance_surfaces_receive_zero_mathematical_credit() -> None:
    boundary = json.loads(CANDIDATE.read_text(encoding="utf-8"))["mathematical_credit_boundary"]
    assert {"tests", "CI", "Git", "hashes", "schemas", "chronology"} <= set(boundary["no_credit_now"])
    assert boundary["future_result_requires_direct_mathematical_certificate"] is True
