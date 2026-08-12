from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CROSS = ROOT / "research/real_math/millennium/cross_problem"
TRANSFER = CROSS / "01_frontier/XM017_COVER_VS_SPECTRAL_AGGREGATION_DIFFERENCEWITNESS_20260812.json"
EPISODE = CROSS / "07_memory/XM017_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
TRACE = CROSS / "09_trace/XM017_HASH_CHAINED_TRACE_20260812.json"
METRICS = CROSS / "10_study_pattern/RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM017_20260812.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_transfer_differencewitness_is_scoped_and_content_bound() -> None:
    value = _load(TRANSFER)
    expected = value["canonical_content_hash"]
    unhashed = copy.deepcopy(value)
    unhashed["canonical_content_hash"] = ""
    assert expected == _hash(unhashed)
    assert value["source"]["atom"] == "O9d12a2a1b-C044"
    assert value["target"]["atom"] == "YM-S1a2"
    assert value["outcome"].startswith("PARTIAL_SUCCESS_")
    assert value["local_mathematical_failure"] is False
    assert value["local_to_global_gluing_failure"] is True
    assert "no continuum/root authority" in value["target"]["scope"]


def test_shadow_task_episode_is_not_canonical_admission() -> None:
    wrapper = _load(EPISODE)
    assert wrapper["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert "NO_CANONICAL_ADMISSION" in wrapper["authority"]
    episode = wrapper["episode"]
    expected = episode["artifact_hash"]
    unhashed = copy.deepcopy(episode)
    unhashed["artifact_hash"] = ""
    assert expected == _hash(unhashed)
    assert episode["fibre_snapshot_hash"] == "sha256:9d6f66a6ae952e51f501dfeea204ce24ddd895efcf8ffbe5960d874b505941c0"


def test_trace_is_hash_chained_and_terminal_hash_matches() -> None:
    trace = _load(TRACE)
    previous = "GENESIS"
    for event in trace["entries"]:
        assert event["prev_hash"] == previous
        expected = event["event_hash"]
        unhashed = copy.deepcopy(event)
        unhashed.pop("event_hash")
        assert expected == _hash(unhashed)
        previous = expected
    assert previous == trace["terminal_hash"]


def test_metrology_counts_semantic_axes_not_repository_growth() -> None:
    value = _load(METRICS)
    metrics = value["RAKL_CYCLE_METRICS"]
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["framework"]["git_sha"] == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert metrics["raw_repository_growth_counts_as_learning"] is False
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert all(v == 0 for v in metrics["protected_retained_semantic_novelty"].values())
    assert metrics["gate_provenance_ci"]["scientific_authority_promotion"] == "NOT_INVOKED"
    assert metrics["gate_provenance_ci"]["root_status"] == "ALL_SIX_OPEN_NO_SOLUTION_CERTIFICATE"
