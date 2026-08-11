from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
CONTEXT_HASH = "sha256:300b787769442af040d944e0b52db106881844a9238c021e8804c7f382660742"
PARENT_EVENT_HASH = "sha256:21ec0a2e7a06b9d3cdc45f385b2a3d5bdd7113ec2441de6d1e664e66f31eb6f3"


def _canonical_hash(payload: dict) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _hash_without_artifact(payload: dict) -> str:
    data = dict(payload)
    data.pop("artifact_hash")
    return _canonical_hash(data)


def test_faithfulness_matrix_is_route_local_and_candidate_free() -> None:
    text = (
        RH
        / "01_frontier/RH_ANA_002_LI_NORM_FAITHFULNESS_MATRIX_20260811.md"
    ).read_text(encoding="utf-8")
    assert "NO_STRICTLY_WEAKER_BRIDGE_EXPOSED_IN_AUDITED_SUZUKI_SOURCE" in text
    assert "NO_MATHEMATICAL_CANDIDATE" in text
    assert "ROOT_AUTHORITY_NONE" in text
    assert "does **not** mean that no new theorem" in text
    assert "Proposition 3.2" in text and "RH_CONDITIONAL" in text
    assert "Theorem 1.1" in text and "RH_EQUIVALENT" in text
    assert "Section 4.1" in text and "SOURCE_OPEN" in text


def test_v3_task_episode_is_content_bound() -> None:
    path = RH / "07_memory/RH_ANA_002_SUZUKI_FAITHFULNESS_TASK_EPISODE_20260811.json"
    episode = json.loads(path.read_text(encoding="utf-8"))
    assert episode["atom_id"] == "RH-ANA-002"
    assert episode["context_hash"] == CONTEXT_HASH
    assert episode["fibre_snapshot_hash"] == CONTEXT_HASH
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["residual_signature"]
    assert episode["operator_ids"] == ["T-XM-ROOT-BRIDGE-STABILITY-AUDIT"]
    assert episode["artifact_hash"] == _hash_without_artifact(episode)


def test_failure_observation_preserves_competing_diagnoses_without_overpromotion() -> None:
    path = RH / "07_memory/RH_ANA_002_POSTAUDIT_FAILURE_EXPERIENCE_LATTICE_20260811.json"
    lattice = json.loads(path.read_text(encoding="utf-8"))
    assert len(lattice["experiences"]) == 1
    failure = lattice["experiences"][0]
    assert failure["failure_id"] == "F-RH-ANA-002-SUZUKI-NORM-NO-WEAKER-BRIDGE"
    assert failure["context_packet_hash"] == CONTEXT_HASH
    assert failure["diagnosis_status"] == "OBSERVED_ONLY"
    assert failure["selected_diagnosis"] == ""
    assert len(failure["competing_diagnoses"]) >= 3
    assert failure["artifact_hash"] == _hash_without_artifact(failure)
    assert any("does not claim" in scope for scope in failure["scope_conditions"])


def test_postaudit_trace_is_externally_anchored_and_internally_hash_chained() -> None:
    path = RH / "09_trace/RH_ANA_002_POSTAUDIT_TRACE_CONTINUATION_20260811.json"
    trace = json.loads(path.read_text(encoding="utf-8"))
    assert trace["parent_trace_id"] == "TRACE-RH-ANA-002-STRICT-20260811"
    assert trace["parent_event_id"] == "RH-ANA-002-E07"
    assert trace["parent_event_hash"] == PARENT_EVENT_HASH
    assert len(trace["entries"]) == 2
    e08, e09 = trace["entries"]
    assert e08["event_type"] == "RESULT_RECORDED"
    assert e08["previous_event_hash"] == PARENT_EVENT_HASH
    assert e08["artifact_hash"] == _hash_without_artifact(e08)
    assert e09["event_type"] == "RESIDUAL_OPENED"
    assert e09["previous_event_hash"] == e08["artifact_hash"]
    assert e09["artifact_hash"] == _hash_without_artifact(e09)
    assert "child_atom:RH-ANA-003" in e09["outputs"]


def test_next_child_is_context_required_and_contains_no_candidate_authority() -> None:
    text = (RH / "02_problem_dag/RH_ANA_003.yaml").read_text(encoding="utf-8")
    assert "atom_id: RH-ANA-003" in text
    assert "parent_atom_id: RH-ANA-002" in text
    assert "status: CONTEXT_REQUIRED" in text
    assert "root_authority: NONE" in text
    assert "allowed: false" in text
    assert "NO_MATHEMATICAL_CANDIDATE" in text
    assert "finite prime truncation" in text
