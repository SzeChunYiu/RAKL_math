import json
from pathlib import Path


ROOT = Path("research/real_math/millennium/yang_mills")
FIBRE = ROOT / "10_case_study/YM-E3a2_FIBRE_RECEIPT_20260811_R6.json"
CASE = ROOT / "10_case_study/YM-E3a2_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260811_R6.json"
AUDIT = ROOT / "00_sources/YM-E3a2_BGM_SEILER_FRD_SOURCE_SCOPE_AUDIT_20260811_R6.md"


def test_source_scope_packet_keeps_proposal_authority_and_root_open():
    fibre = json.loads(FIBRE.read_text())
    case = json.loads(CASE.read_text())
    audit = AUDIT.read_text()

    assert fibre["authority"] == "PROPOSAL_SHADOW_FROZEN_CONTEXT_ROOT_AUTHORITY_NONE"
    assert case["authority"] == "PROPOSAL_SHADOW_MEASUREMENT_ONLY_ROOT_AUTHORITY_NONE"
    assert case["RAKL_CYCLE_METRICS"]["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert "ROOT_AUTHORITY_NONE" in audit


def test_fibre_and_episode_bind_same_atom_and_hash():
    fibre = json.loads(FIBRE.read_text())
    case = json.loads(CASE.read_text())

    assert fibre["active_atom"] == case["RAKL_METHOD_CASE_STUDY"]["atom"] == "YM-E3a2"
    assert fibre["fibre_snapshot_hash"] == case["TASK_EPISODE_SHADOW"]["input_fibre_hash"]
    assert fibre["fibre_snapshot_hash"] == case["RAKL_CYCLE_METRICS"]["fibre_snapshot_hash"]


def test_semantic_novelty_does_not_count_repository_growth_or_mint_obstruction():
    case = json.loads(CASE.read_text())
    metrics = case["RAKL_CYCLE_METRICS"]
    novelty = metrics["retained_semantic_novelty"]

    assert metrics["raw_repository_growth_counts_as_learning"] is False
    assert novelty["KNOWLEDGE"] == 1
    assert novelty["OPERATOR"] == 0
    assert novelty["EXPERIENCE_PATTERN"] == 0
    assert novelty["OBSTRUCTION"] == 0
    assert novelty["RELATION"] == 1
    assert novelty["PATH"] == 1
    assert novelty["META_METHOD"] == 0
    assert metrics["new_ids"]["obstruction_ids"] == []
    assert metrics["new_ids"]["lesson_ids"] == []


def test_source_audit_preserves_difference_witness_and_missing_source_block():
    audit = AUDIT.read_text()

    assert "FRD_COVARIANCE_INGREDIENT_CONFIRMED" in audit
    assert "SAME_THEORY_YM_NONLINEAR_CONTRACTION_NOT_ESTABLISHED_BY_THIS_SOURCE" in audit
    assert "BLOCKED/UNKNOWN" in audit
    assert "DifferenceWitness" in audit
    assert "Do not spend another cycle treating BGM Theorem 1.1" in audit
