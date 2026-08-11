from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_rh_spec_003_context_defect_is_append_only_and_candidate_blocking() -> None:
    frozen = json.loads((BASE / "01_frontier/RH_SPEC_003_CONTEXT_FIBER_20260811.json").read_text(encoding="utf-8"))
    assert frozen["packet_hash"] == "sha256:90a186d8e391a32b0aaa061f3c9cd42ad009633caa0232f190562e894769d529"
    assert frozen["first_candidate_at"] is None
    assert any("weak-L1 endpoint" in item for item in frozen["near_solved_analogues"])

    parent = json.loads((BASE / "09_trace/RH_SPEC_003_OPEN_TRACE_20260811.json").read_text(encoding="utf-8"))
    parent_hash = parent["entries"][-1]["artifact_hash"]
    assert parent_hash == "sha256:c8265e1d45f5bc05f51f2c3dc9ce664f711ec856955a936e31eb5d634dbb87a2"
    assert all(entry["event_type"] != "CANDIDATE_PROPOSED" for entry in parent["entries"])

    continuation = json.loads((BASE / "09_trace/RH_SPEC_003_CONTEXT_DEFECT_TRACE_CONTINUATION_20260811.json").read_text(encoding="utf-8"))
    assert continuation["parent_event_hash"] == parent_hash
    previous = parent_hash
    for entry in continuation["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = copy.deepcopy(entry)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        previous = artifact_hash
    assert [entry["event_type"] for entry in continuation["entries"]] == ["FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED"]
    assert all(entry["event_type"] != "CANDIDATE_PROPOSED" for entry in continuation["entries"])
    assert "CANDIDATE_GENERATION_BLOCKED" in continuation["entries"][-1]["outputs"]


def test_rh_spec_003_retrospective_endpoint_scope_is_locked() -> None:
    result = (BASE / "04_candidates/negative_history/RH_SPEC_003_WEAK_L1_ENDPOINT_CONTEXT_DEFECT_20260811.md").read_text(encoding="utf-8")
    for required in (
        "RETROSPECTIVE_ANALYTIC_CALIBRATION",
        "nu_n ~ n / (C log n)",
        "A_alpha in S_p  <=>  alpha*p > 1",
        "A_alpha notin S_{1/alpha, infinity}",
        "beta >= alpha",
        "beta > 2 alpha",
        "s_n(B_{1,1}) ~ C/n",
        "no prime-power trace formula",
        "cannot now be backfilled as a preregistered `RH-SPEC-003` candidate",
    ):
        assert required in result

    delta = json.loads((BASE / "07_memory/RH_SPEC_003_CONTEXT_DEFECT_FAILURE_EXPERIENCE_DELTA_20260811.json").read_text(encoding="utf-8"))
    payload = copy.deepcopy(delta)
    artifact_hash = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert artifact_hash == _canonical_hash(payload)
    assert {item["failure_id"] for item in delta["failures"]} == {
        "F-RH-SPEC-003-WEAK-L1-ENDPOINT",
        "F-RH-SPEC-003-FOCUSED-CURRENT-FRAMEWORK-CI-COVERAGE",
    }
    assert all(item["difference_witness_required"] for item in delta["failures"])


def test_focused_rh_workflow_covers_spec003_assurance_files() -> None:
    workflow = (ROOT / ".github/workflows/rh-spectral-assurance.yml").read_text(encoding="utf-8")
    assert "tests/math_applications/test_rh_spec_003_strict_packet.py" in workflow
    assert "tests/math_applications/test_rh_spec_003_endpoint_erratum.py" in workflow
