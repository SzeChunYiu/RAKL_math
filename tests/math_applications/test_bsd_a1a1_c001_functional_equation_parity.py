from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _leading_inversion_sign(r: int) -> int:
    # T |-> (1+T)^(-1)-1 = -T + O(T^2), hence on J^r/J^(r+1).
    return -1 if r % 2 else 1


def test_functional_equation_sign_plus_forces_even_augmentation_order() -> None:
    for r in range(1, 12):
        equation_can_hold = _leading_inversion_sign(r) == 1
        assert equation_can_hold is (r % 2 == 0)


def test_hostile_sign_minus_one_reverses_parity() -> None:
    for r in range(1, 12):
        equation_can_hold = _leading_inversion_sign(r) == -1
        assert equation_can_hold is (r % 2 == 1)


def test_candidate_and_trace_preserve_scope_and_hash_chain() -> None:
    candidate = (BASE / "04_candidates/BSD_A1a1_C001_FUNCTIONAL_EQUATION_PARITY_20260811.md").read_text(encoding="utf-8")
    assert "does **not** prove `ord_J Theta_{f/K}=2`" in candidate
    assert "p>3" in candidate
    assert "Theta=0" in candidate
    assert "BSD-A1a1b-HIGHER-EVEN-ORDER-EXCLUSION" in candidate

    prior = json.loads((BASE / "09_trace/BSD_A1a1_PRE_CANDIDATE_TRACE_20260811.json").read_text(encoding="utf-8"))
    continuation = json.loads((BASE / "09_trace/BSD_A1a1_C001_TRACE_CONTINUATION_20260811.json").read_text(encoding="utf-8"))
    previous = prior["entries"][-1]["artifact_hash"]
    assert [e["event_type"] for e in continuation["entries"]] == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]
    for entry in continuation["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = dict(entry)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        previous = artifact_hash
