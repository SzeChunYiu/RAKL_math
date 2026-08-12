from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "research/real_math/millennium/cross_problem/10_case_study/MATH_FAILURE_MEMORY_COVERAGE_AUDIT_20260812.json"
LEGACY = "F-O9D12A2A1A1B-FIXED-LAMBDA-GLOBAL-STATE-FACTORIZATION"


def load() -> dict:
    return json.loads(AUDIT.read_text(encoding="utf-8"))


def semantic(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(semantic(payload)).hexdigest()


def test_coverage_population_and_exact_gap_are_frozen() -> None:
    audit = load()
    coverage = audit["coverage"]
    assert coverage["failure_experiences_scanned"] == 91
    assert coverage["files_scanned_with_experiences"] == 43
    assert coverage["canonical_schema_complete_experiences"] == 89
    assert coverage["canonical_schema_gap_experiences"] == 2
    assert coverage["seven_field_math_complete_experiences"] == 90
    assert coverage["seven_field_math_gap_experiences"] == 1
    assert [row["failure_id"] for row in coverage["seven_field_math_gaps"]] == [LEGACY]
    assert audit["artifact_hash"] == artifact_hash(audit)


def test_seven_mathematical_lesson_coordinates_are_explicit() -> None:
    mapping = load()["seven_field_mapping"]
    assert set(mapping) == {
        "attempted_mathematical_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "mathematical_falsifier",
        "mathematical_repair",
        "proof_or_source_evidence",
    }
    assert "competing_diagnoses" in mapping["supported_and_competing_causes"]
    assert mapping["mathematical_falsifier"] == ["falsifier_or_attempt"]


def test_gap_is_diagnosed_without_promoting_its_mathematics() -> None:
    audit = load()
    diagnosis = audit["bounded_diagnosis"]
    assert diagnosis["status"] == "SUPPORTED_BOUNDED"
    assert len(diagnosis["competing_causes"]) >= 2
    assert "append-only" in diagnosis["falsifier"]
    assert "Preserve the legacy bytes" in diagnosis["repair"]
    assert audit["credit_boundary"]["mathematical_credit_units"] == 0


def test_existing_framework_owner_prevents_unearned_method_invention() -> None:
    audit = load()
    owner = audit["framework_owner_audit"]
    assert owner["verdict"] == "EXISTING_METHOD_SURFACE_APPLICATION_ROUTING_GAP"
    assert owner["new_method_surface_justified"] is False
    assert owner["fresh_assurance_required"] is True
    assert owner["promotion_state"] == "NO_FRAMEWORK_DELTA_PROPOSED_OR_PROMOTED"
    assert any("failure_lattice.py" in path for path in owner["existing_owners"])
    assert any("challenge_learning.py" in path for path in owner["existing_owners"])


def test_root_and_authority_boundaries_remain_fail_closed() -> None:
    audit = load()
    assert audit["authority_universe"]["pending_or_open_pr_material_counted"] is False
    assert audit["credit_boundary"]["framework_promotion"] is False
    assert audit["credit_boundary"]["independent_review"] is False
    assert audit["root_status"] == "ALL_UNSOLVED_ROOTS_OPEN_NO_SOLUTION_CERTIFICATE"
