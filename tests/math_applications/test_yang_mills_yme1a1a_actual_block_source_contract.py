from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_actual_block_source_gate_extends_canonical_trace_and_blocks_candidate() -> None:
    parent = _load(YM / "09_trace" / "YM_E1a1a_PRE_CANDIDATE_TRACE_20260811.json")
    extension = _load(YM / "09_trace" / "YM_E1a1a_ACTUAL_BLOCK_SOURCE_TRACE_20260811.json")

    terminal = parent["entries"][-1]
    assert terminal["event_id"] == "YM-E1a1a-E007"
    assert extension["predecessor_event_id"] == terminal["event_id"]
    assert extension["predecessor_event_hash"] == terminal["artifact_hash"]

    event = extension["entries"][0]
    assert event["event_id"] == "YM-E1a1a-E008"
    assert event["previous_event_hash"] == terminal["artifact_hash"]
    assert "candidate_generation:BLOCKED" in event["outputs"]
    assert "missing_primary_binding:DOI:10.1007/BF01211042" in event["outputs"]
    assert event["artifact_hash"] == "sha256:bcab2fc322c2f8410b7214e006c4dc5e7ec5ab5b72f7229f4f78bd22ed77939f"


def test_actual_block_contract_is_fail_closed_and_contains_no_candidate() -> None:
    text = (
        YM
        / "03_sources"
        / "YM_E1a1a_ACTUAL_BLOCK_SOURCE_CONTRACT_20260811.md"
    ).read_text(encoding="utf-8")

    assert "DOI `10.1007/BF01211042`" in text
    assert "CANDIDATE_BLOCKED" in text
    assert "NO_MATHEMATICAL_CANDIDATE" in text
    assert "ROOT_AUTHORITY_NONE" in text
    assert "YM-E1a1a0" in text
    for field in range(12):
        assert f"B{field}_" in text
    assert "Candidate generation is enabled only if `B0`–`B11` have no `UNKNOWN`" in text
