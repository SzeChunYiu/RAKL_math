import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def test_context_fibre_self_hash_and_shadow_authority():
    path = NS / "01_frontier" / "NS-B1a4_CONTEXT_FIBER_R1_20260812.json"
    data = json.loads(path.read_text())
    expected = data.pop("fibre_snapshot_hash")
    assert expected == "sha256:" + hashlib.sha256(canonical_bytes(data)).hexdigest()
    assert data["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert data["root_contract"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_pressure_zero_shear_strict_sign_margin():
    # f^2_t / f^2 = ((y-3)^2 - 2(1+t)) / (2(1+t)^2).
    # The worst point on |y|<=1 is y=1.  It stays strictly positive for t<1.
    for t in (0.0, 0.25, 0.5, 0.75, 0.999):
        s = 1.0 + t
        margin = ((1.0 - 3.0) ** 2 - 2.0 * s) / (2.0 * s * s)
        assert margin > 0.0


def test_trace_hash_chain():
    path = NS / "09_trace" / "NS-B1a4_TRACE_R1_20260812.jsonl"
    events = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    previous = "0" * 64
    for index, event in enumerate(events):
        assert event["index"] == index
        assert event["previous_hash"] == previous
        digest = event.pop("event_hash")
        assert hashlib.sha256(canonical_bytes(event)).hexdigest() == digest
        previous = digest
    assert previous == "ca8b653d4fc8771b64d84c4bb112bf2f0a8731e10dc5422dcd29355dfd8de3fe"


def test_task_episode_content_hash_and_nonpromotion():
    path = NS / "07_memory" / "NS-B1a4_TASK_EPISODE_R1_20260812.json"
    data = json.loads(path.read_text())
    digest = data.pop("artifact_hash")
    assert hashlib.sha256(canonical_bytes(data)).hexdigest() == digest
    assert digest == "7e45e0a0fdb01b9041334b3805d9d61d7f8440cd46b7c28aa478b9da26a4cbed"
    assert data["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert data["outcome"] == "PARTIAL_SUCCESS"
    assert "LOCAL_TO_GLOBAL_FINITE_I_ANCIENT_GLUE_UNRESOLVED" in data["residual_signature"]


def test_experience_delta_separates_episode_diagnosis_obstruction_and_gluing():
    path = NS / "07_memory" / "NS-B1a4_EXPERIENCE_DELTA_R1_20260812.json"
    data = json.loads(path.read_text())
    assert data["episode"]["id"].startswith("EP-")
    assert data["diagnosis"]["id"].startswith("DX-")
    assert data["obstruction"]["id"].startswith("O-")
    ids = {item["id"] for item in data["failures"]}
    assert "F-NS-B1a4-GENERIC-LEI-PRESSUREZERO-NO-MONOTONICITY" in ids
    assert "G-NS-B1a4-LOCAL-SHEAR-TO-FINITE-I-ANCIENT" in ids
    assert data["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
