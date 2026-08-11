from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"


def test_ym_s1c1_retrospective_v3_authority_boundary() -> None:
    episode = json.loads(
        (YM / "07_memory" / "YM_S1C1_V3_TASK_EPISODE_20260811.json").read_text()
    )
    failure = json.loads(
        (YM / "07_memory" / "YM_S1C1_FAILURE_EXPERIENCE_DELTA_20260811.json").read_text()
    )
    saturation = json.loads(
        (YM / "07_memory" / "YM_S1C1_SATURATION_VECTOR_20260811.json").read_text()
    )
    fibre = json.loads(
        (YM / "01_frontier" / "YM_S1C1_PROBLEM_FIBRE_SNAPSHOT_20260811.json").read_text()
    )
    source = (
        YM / "03_sources" / "YM_S1C1_FAIZAL_SHABIR_AF_ENTRY_AUDIT_20260811.md"
    ).read_text()
    case_study = (
        YM / "08_reviews" / "RAKL_METHOD_CASE_STUDY_YM_S1C1_20260811.md"
    ).read_text()
    child = (YM / "02_problem_dag" / "YM_S1C1a_delta.yaml").read_text()

    assert episode["episode_id"] == "EP-YM-S1C1-AF-BARE-COUPLING-AUDIT-20260811"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["residual_signature"]
    assert episode["authority"]["status"] == "PROPOSAL_SHADOW"
    assert episode["authority"]["allowed_effect"] == "SEARCH_PRIORITY_ONLY"
    assert episode["authority"]["grants_theorem_authority"] is False
    assert episode["authority"]["grants_gluing_authority"] is False
    assert episode["authority"]["chronology"] == "RETROSPECTIVE"

    assert failure["failure_id"] == "F-YM-S1C1-FIXED-REFERENCE-BARE-COUPLING-ESCAPE"
    assert failure["diagnosis_status"] == "OBSERVED_ONLY"
    assert "does not claim nonexistence" in " ".join(failure["scope_conditions"])

    assert set(saturation["axes"]) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert saturation["absolute_completeness"] is False

    assert fibre["snapshot_hash"] == "sha256:27075442496d85c19f6bee4ac90345dd1c4b851e00f6aa70306a037fd6c1cb9c"
    assert fibre["authority"] == "PROPOSAL_SHADOW_SEARCH_PRIORITY_ONLY"
    assert "bare_coupling_coordinate" in fibre["contents"]["active_interface_keys"]
    assert fibre["contents"]["retrieved_but_rejected"]

    assert "beta_K -> beta_* < infinity" in source
    assert "BARE_COUPLING_ESCAPE_NOT_ESTABLISHED_BY_THEOREM_5_4" in source
    assert "does **not** show that no asymptotically-free trajectory exists" in source
    assert "FRESH_SOURCE_COLLISION_GATE" in case_study
    assert "candidate_generation_gate:" in child
    assert "allowed: false" in child
