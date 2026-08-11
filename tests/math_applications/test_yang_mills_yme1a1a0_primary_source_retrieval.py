from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_primary_source_retrieval_extends_actual_block_trace() -> None:
    parent = _load(YM / "09_trace" / "YM_E1a1a_ACTUAL_BLOCK_SOURCE_TRACE_20260811.json")
    extension = _load(YM / "09_trace" / "YM_E1a1a0_PRIMARY_SOURCE_RETRIEVAL_TRACE_20260811.json")

    terminal = parent["entries"][-1]
    assert terminal["event_id"] == "YM-E1a1a-E008"
    assert extension["predecessor_event_id"] == terminal["event_id"]
    assert extension["predecessor_event_hash"] == terminal["artifact_hash"]

    result, residual = extension["entries"]
    assert result["event_id"] == "YM-E1a1a-E009"
    assert result["previous_event_hash"] == terminal["artifact_hash"]
    assert result["artifact_hash"] == "sha256:843ed45fded234322ba610216bf7627d137ba705ec2b57034e076d2f973f485a"
    assert "candidate_generation:BLOCKED" in result["outputs"]
    assert "B1_B2_B3:UNKNOWN" in result["outputs"]

    assert residual["event_id"] == "YM-E1a1a-E010"
    assert residual["previous_event_hash"] == result["artifact_hash"]
    assert residual["artifact_hash"] == "sha256:0d66962c0b3edfbbd526525e2c266124e555959964a06ddaa5b14ac3a85b2404"
    assert "failure_experience:NO_NEW_ENTRY" in residual["outputs"]
    assert "mathematical_candidate:NO" in residual["outputs"]


def test_primary_source_retrieval_fails_closed_without_b1_b3() -> None:
    text = (
        YM
        / "03_sources"
        / "YM_E1a1a0_PRIMARY_SOURCE_RETRIEVAL_20260811.md"
    ).read_text(encoding="utf-8")

    assert "DOI `10.1007/BF01211042`" in text
    assert "HUTMP-83-B147" in text
    assert "`B1_FINE_COARSE_GEOMETRY` | `UNKNOWN`" in text
    assert "`B2_GAUGE_AVERAGING_MAP` | `UNKNOWN`" in text
    assert "`B3_REGULARITY_DOMAIN` | `UNKNOWN`" in text
    assert "NO_MATHEMATICAL_CANDIDATE" in text
    assert "NO_FAILURE_EXPERIENCE" in text
    assert "ROOT_AUTHORITY_NONE" in text
