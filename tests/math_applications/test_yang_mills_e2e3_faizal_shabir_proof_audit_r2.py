from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"
METRICS = YM / "10_case_study" / "YM-E2E3_RAKL_CYCLE_METRICS_20260811.json"
EPISODE = YM / "10_case_study" / "YM-E2E3_V3_TASK_EPISODE_20260811.json"
AUDIT = YM / "03_sources" / "YM-E2E3_FAIZAL_SHABIR_PROOF_AUDIT_R2_20260811.md"
CASE = YM / "10_case_study" / "YM-E2E3_RAKL_METHOD_CASE_STUDY_20260811.md"


def _canonical_hash_without_artifact_hash(payload: dict[str, object]) -> str:
    material = dict(payload)
    material.pop("artifact_hash", None)
    raw = json.dumps(
        material,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def test_source_audit_keeps_exact_defects_and_scope() -> None:
    text = AUDIT.read_text(encoding="utf-8")
    assert "e^{a_{k+1}\\Delta_k}\\le e^{a_{k+1}}" in text
    assert "2Cr+Cr^2\\le0" in text
    assert "Cr(2+r)>0" in text
    assert "#92 `YM-E2b`" in text
    assert "#93 `YM-E3a`" in text
    assert "proof defect, not an impossibility theorem" in text
    assert "does **not** establish that no corrected weak-coupling construction exists" in text


def test_cycle_metrics_bind_current_framework_and_explicit_novelty_vector() -> None:
    data = json.loads(METRICS.read_text(encoding="utf-8"))
    assert data["rakl"]["git_sha"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert data["rakl_math"]["base_sha"] == "6557b1b25fa839fe71aba8047c958d5da892edd8"
    assert data["rakl_math"]["framework_pin_sha"] == data["rakl"]["git_sha"]
    assert data["outcome"] == "PARTIAL_SUCCESS"
    assert data["retained_semantic_novelty"] == {
        "KNOWLEDGE": 2,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 2,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
        "classification_boundary": (
            "internal v3 metrology; overlapping axes are not summed into a scalar "
            "learning score and have not received external novelty audit"
        ),
    }
    assert data["gate_provenance_ci"]["source_audit_chronology"].startswith("RETROSPECTIVE")
    assert data["gate_provenance_ci"]["mathematical_candidate_generated"] is False
    assert data["gate_provenance_ci"]["root_authority"] == "NONE"
    assert data["artifact_hash"] == "sha256:" + _canonical_hash_without_artifact_hash(data)


def test_task_episode_is_shadow_only_and_separates_diagnosis_from_authority() -> None:
    data = json.loads(EPISODE.read_text(encoding="utf-8"))
    assert data["outcome"] == "PARTIAL_SUCCESS"
    assert data["shadow_extensions"]["candidate_gate"].startswith("NO_NEW_MATHEMATICAL_CANDIDATE")
    assert data["shadow_extensions"]["novelty_class"]["class"] == "UNRESOLVED"
    diagnoses = data["shadow_extensions"]["diagnoses"]
    assert len(diagnoses) == 2
    assert all("non_escalation" in item for item in diagnoses)
    assert data["artifact_hash"] == "sha256:" + _canonical_hash_without_artifact_hash(data)


def test_method_case_study_marks_same_context_review_and_no_framework_promotion() -> None:
    text = CASE.read_text(encoding="utf-8")
    assert "same-context analytical passes" in text
    assert "no independent-review credit" in text
    assert "no framework issue is opened from this cycle" in text
    assert "no theorem authority was created" in text
