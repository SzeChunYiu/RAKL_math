from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRACE = (
    ROOT
    / "research/real_math/millennium/p_vs_np/09_trace"
    / "O9d12a2a1a_C025_TRACE_CONTINUATION_20260811.json"
)
PARENT = (
    ROOT
    / "research/real_math/millennium/p_vs_np/09_trace"
    / "O9d12a2a1a_PRE_CANDIDATE_TRACE_MIGRATION_REPAIRED_20260811.json"
)


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_c025_trace_continues_exact_repaired_parent_chain() -> None:
    parent = json.loads(PARENT.read_text(encoding="utf-8"))
    continuation = json.loads(TRACE.read_text(encoding="utf-8"))
    parent_terminal_hash = parent["entries"][-1]["artifact_hash"]
    assert continuation["parent_terminal_hash"] == parent_terminal_hash

    previous = parent_terminal_hash
    types = []
    for entry in continuation["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = copy.deepcopy(entry)
        payload["artifact_hash"] = ""
        assert entry["artifact_hash"] == _canonical_hash(payload)
        previous = entry["artifact_hash"]
        types.append(entry["event_type"])

    assert types == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
    ]
