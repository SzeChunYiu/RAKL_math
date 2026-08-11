import hashlib
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"

PRE = BSD / "07_memory" / "BSD_A1a1_R5_PREACTION_FIBRE_RECEIPT_20260811.json"
SOURCE = BSD / "00_sources" / "BSD_A1a1_R5_KOLYVAGIN_SELMER_SOURCE_RECEIPT_20260811.json"
EPISODE = BSD / "07_memory" / "BSD_A1a1_R5_TASK_EPISODE_SHADOW_20260811.json"
FAILURE = BSD / "07_memory" / "BSD_A1a1_R5_DIRECT_COMPLEX_CARRIER_FAILURE_SHADOW_20260811.json"
DIAGNOSIS = BSD / "07_memory" / "BSD_A1a1_R5_SELMER_CARRIER_DIAGNOSIS_SHADOW_20260811.json"
OBSTRUCTION = BSD / "07_memory" / "BSD_A1a1_R5_SELMER_TO_MW_SHA_OBSTRUCTION_SHADOW_20260811.json"
METRICS = BSD / "07_memory" / "BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R5.json"
TRACE = BSD / "09_trace" / "BSD_A1a1_R5_KOLYVAGIN_SELMER_TRACE_DELTA_20260811.json"


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_hash(payload) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def _hash_without_artifact_hash(obj) -> str:
    payload = dict(obj)
    payload.pop("artifact_hash", None)
    return "sha256:" + _canonical_hash(payload)


def test_r5_preaction_is_prospectively_bound_and_self_hashed():
    pre = _load(PRE)
    payload = dict(pre)
    claimed = payload.pop("receipt_canonical_sha256")
    assert claimed == _canonical_hash(payload)
    assert pre["schema_version"] == "pre-action-fibre-receipt-v1"
    assert pre["framework_commit"] == "3df0000e71e7f3f8a61925bf9a8176e72d5143de"
    assert pre["application_commit"] == "812addd25a7f34d3c6272143e21d5d7db34539aa"
    assert pre["fibre_snapshot_hash"] == "732dee783ffc2d72b6fa83ec84f15adb450b4afd242ada32c5ec9bbc6b03f19a"

    episode = _load(EPISODE)
    pre_time = datetime.fromisoformat(pre["frozen_at_utc"].replace("Z", "+00:00"))
    episode_time = datetime.fromisoformat(episode["timestamp"].replace("Z", "+00:00"))
    assert pre_time < episode_time
    assert f"pre_action_receipt:{claimed}" in episode["evidence_pointers"]
    assert episode["operator_ids"] == pre["operator_ids"]


def test_r5_task_episode_matches_current_v3_content_hash_shape():
    episode = _load(EPISODE)
    payload = dict(episode)
    claimed = payload.pop("artifact_hash")
    assert claimed == _canonical_hash(payload)
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["cost"] == 7.0
    assert episode["residual_signature"]


def test_r5_source_failure_diagnosis_obstruction_are_distinct_and_hashed():
    for path in (SOURCE, FAILURE, DIAGNOSIS, OBSTRUCTION):
        data = _load(path)
        assert data["artifact_hash"] == _hash_without_artifact_hash(data)

    failure = _load(FAILURE)
    diagnosis = _load(DIAGNOSIS)
    obstruction = _load(OBSTRUCTION)
    assert failure["failure_id"] == "F-BSD-A1A1-DIRECT-COMPLEX-CARRIER-MISS-R5"
    assert diagnosis["diagnosis_id"] == "D-BSD-A1A1-SELMER-CARRIER-FAITHFULNESS-R5"
    assert obstruction["obstruction_id"] == "O-BSD-A1A1-SELMER-TO-MW-SHA-FAITHFULNESS-R5"
    assert obstruction["obstruction_kind"] == "LOCAL_TO_GLOBAL_ROOT_FAITHFULNESS_GLUING"
    assert obstruction["lesson_promotion"] == "NONE"


def test_r5_trace_extends_canonical_r3_head_and_is_hash_chained():
    trace = _load(TRACE)
    assert trace["base_last_event_id"] == "BSD-A1a1-E09"
    previous = trace["base_last_event_hash"]
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _hash_without_artifact_hash(event)
        previous = event["artifact_hash"]
    assert trace["entries"][-1]["outputs"][-1] == "root_state:OPEN_NO_SOLUTION_CERTIFICATE"


def test_r5_metrics_preserve_zeroes_and_root_gate():
    metrics = _load(METRICS)
    assert metrics["artifact_hash"] == _hash_without_artifact_hash(metrics)
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["active_atom"]["fibre_snapshot_hash"] == "sha256:732dee783ffc2d72b6fa83ec84f15adb450b4afd242ada32c5ec9bbc6b03f19a"
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 1,
        "RELATION": 1,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert set(metrics["saturation_axes"]) >= {
        "retrieval_novelty",
        "tool_output_novelty",
        "counterexample_pressure",
        "decomposition_yield",
        "expert_review_novelty",
        "method_novelty",
        "transfer_novelty",
    }
    assert metrics["new_objects"]["lesson_ids"] == []
    assert metrics["new_objects"]["tool_ids"] == []
    assert metrics["gate_provenance_ci"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["mathematical_candidate_generated"] is False
    assert metrics["gate_provenance_ci"]["same_context_review_independent"] is False
    assert metrics["raw_growth_not_learning"]["files_created_not_counted_as_learning"] is True
