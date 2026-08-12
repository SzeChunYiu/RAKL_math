from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/cross_problem/poincare_transfer"
CANDIDATE = BASE / "04_candidates/XM_PC_NS_001_C001_ENSTROPHY_SIGN_FALSIFIER_FREEZE_20260812.json"
EVALUATOR = BASE / "05_falsification/XM_PC_NS_001_C001_EVALUATOR_FREEZE_20260812.json"
TRACE = BASE / "09_trace/XM_PC_NS_001_C001_CANDIDATE_FREEZE_TRACE_20260812.json"
PRETRACE = BASE / "09_trace/XM_PC_NS_001_PRE_CANDIDATE_TRACE_20260812.json"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _candidate_hash(candidate: dict) -> str:
    payload = dict(candidate)
    payload.pop("candidate_canonical_sha256")
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def test_candidate_identity_and_evaluator_are_frozen_without_result() -> None:
    candidate = _load(CANDIDATE)
    evaluator = _load(EVALUATOR)
    assert _candidate_hash(candidate) == candidate["candidate_canonical_sha256"]
    assert evaluator["candidate_canonical_sha256"] == candidate["candidate_canonical_sha256"]
    assert evaluator["execution_status"] == "NOT_EXECUTED"
    assert evaluator["result"] is None
    assert candidate["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert candidate["independent_review_credit"] == 0


def test_candidate_is_exactly_the_licensed_action_and_has_all_branches() -> None:
    gate = _load(BASE / "09_trace/XM_PC_NS_001_PRE_CANDIDATE_GATE_RECEIPT_20260812.json")
    candidate = _load(CANDIDATE)
    assert gate["gate_verdicts"]["licensed_action"] == "FREEZE_ONE_EXPLICIT_3D_NS_ENSTROPHY_SIGN_FALSIFIER"
    assert candidate["candidate_type"] == "EXACT_MATHEMATICAL_TRANSFER_FALSIFIER"
    assert {row["verdict"] for row in candidate["preregistered_result_branches"]} == {
        "POSITIVE_DERIVATIVE_REFUTES_BARE_ENSTROPHY_MONOTONICITY",
        "FROZEN_FIELD_DOES_NOT_REFUTE_MONOTONICITY",
        "CANNOT_CHECK",
    }


def test_candidate_trace_continues_merged_pre_candidate_hash_chain() -> None:
    pretrace = _load(PRETRACE)
    trace = _load(TRACE)
    assert trace["entries"][0]["previous_event_hash"] == pretrace["entries"][-1]["artifact_hash"]
    assert trace["entries"][1]["previous_event_hash"] == trace["entries"][0]["artifact_hash"]
    assert [row["event_type"] for row in trace["entries"]] == ["CANDIDATE_PROPOSED", "FORMALIZED"]
    serialized = json.dumps(trace, sort_keys=True)
    assert "EVALUATOR_NOT_EXECUTED" in serialized
    assert "POSITIVE_DERIVATIVE_OBSERVED" not in serialized


def test_candidate_field_is_syntactically_fixed_and_not_abc_beltrami() -> None:
    candidate = _load(CANDIDATE)
    assert candidate["frozen_field"]["amplitude"] == "A=100 nu"
    assert candidate["frozen_field"]["base_field"] == [
        "v_1(x,y,z)=cos(y)+cos(x+y)",
        "v_2(x,y,z)=cos(x)-cos(x+y)",
        "v_3(x,y,z)=cos(x+y)",
    ]
    assert "ABC" not in json.dumps(candidate)
