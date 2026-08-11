from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_h4d1a_same_detector_route_pruning_trace_is_hash_chained() -> None:
    trace = json.loads(
        (BASE / "09_trace/H4d1a_CALIBRATION_TRACE_CONTINUATION_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    assert trace["parent_final_event_hash"] == "sha256:4035a5ee15fc2f1faa1d925f57648ba0cb76301219aa8bc913836f7063b7651f"
    previous = trace["parent_final_event_hash"]
    assert [entry["event_type"] for entry in trace["entries"]] == [
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = copy.deepcopy(entry)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        previous = artifact_hash
    assert previous == "sha256:ad45384089660f2a605dbebd045fa2d896d4729c07e91fe14e8eda4f2477949d"


def test_h4d1a_no_go_is_scoped_and_preserves_root_boundary() -> None:
    result = (
        BASE / "03_routes/H4d1a_BRANCH_DETECTOR_COMPATIBILITY_NOGO_20260811.md"
    ).read_text(encoding="utf-8")
    assert "B_{T,1} subseteq ker(sigma)" in result
    assert "injective  =>  B_{T,1} = 0" in result
    assert "FIRST_ORDER_SAME_DETECTOR_PROPER_NONZERO_NOGO" in result
    assert "does not address root initial algebraicity" in result


def test_h4d1a_failure_delta_registers_scoped_impossibility_only() -> None:
    delta = json.loads(
        (BASE / "07_memory/H4d1a_FAILURE_EXPERIENCE_DELTA_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    assert len(delta["experiences"]) == 1
    failure = delta["experiences"][0]
    assert failure["failure_id"] == "F-H4D1A-SAME-DETECTOR-BRANCH-NOGO"
    assert failure["diagnosis_status"] == "VERIFIED_IMPOSSIBILITY"
    assert any("first-order" in scope for scope in failure["scope_conditions"])
    assert any("different independently justified detector" in scope for scope in failure["scope_conditions"])
    payload = copy.deepcopy(failure)
    artifact_hash = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert artifact_hash == _canonical_hash(payload)
