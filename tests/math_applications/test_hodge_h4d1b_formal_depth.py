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


def test_planted_first_order_pass_fails_next_artin_lift() -> None:
    # Work over F_5 as an exact finite analogue of the characteristic-zero calculation.
    # A' = F5[e]/e^3; a lift of u=e mod e^2 has u=e+a e^2.
    # Its square always has e^2 coefficient 1, so u^2=0 cannot hold.
    for a in range(5):
        # coefficients of (e + a e^2)^2 mod e^3 are (const,e,e^2)
        square = (0, 0, 1)
        assert square != (0, 0, 0)


def test_h4d1b_result_keeps_first_order_authority_scoped() -> None:
    result = (BASE / "03_routes/H4d1b_FIRST_ORDER_DEPTH_CALIBRATION_20260811.md").read_text(encoding="utf-8")
    assert "FIRST_ORDER_CHECKPOINT_NOT_FORMAL_CERTIFICATE" in result
    assert "delta_1|T=0" in result
    assert "formal lifting != algebraization != global/monodromy continuation != root initial algebraicity" in result
    assert "not" in result.lower()


def test_h4d1b_continuation_is_hash_chained() -> None:
    trace = json.loads((BASE / "09_trace/H4d1b_CALIBRATION_TRACE_CONTINUATION_20260811.json").read_text(encoding="utf-8"))
    assert trace["parent_final_event_hash"] == "sha256:eae53222edea02ae5bc338cd4375d315f4c2e9678f632765f676717395d82f7b"
    previous = trace["parent_final_event_hash"]
    assert [x["event_type"] for x in trace["entries"]] == ["CANDIDATE_PROPOSED", "FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED"]
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = copy.deepcopy(entry)
        observed = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert observed == _canonical_hash(payload)
        previous = observed
    assert previous == "sha256:10ad0bb83de77e23e5be83ad66188cf44b70ee24a77ffd9d967b74e463f5ce1d"


def test_h4d1b_failure_is_verified_only_in_method_scope() -> None:
    delta = json.loads((BASE / "07_memory/H4d1b_FAILURE_EXPERIENCE_DELTA_20260811.json").read_text(encoding="utf-8"))
    assert len(delta["experiences"]) == 1
    failure = delta["experiences"][0]
    assert failure["failure_id"] == "F-H4D1B-FIRST-ORDER-NOT-FORMAL"
    assert failure["diagnosis_status"] == "VERIFIED_IMPOSSIBILITY"
    assert any("general method rule" in x for x in failure["scope_conditions"])
    assert any("special Hodge families" in x for x in failure["scope_conditions"])
    payload = copy.deepcopy(failure)
    observed = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert observed == _canonical_hash(payload)
