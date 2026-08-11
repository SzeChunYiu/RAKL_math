from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"


def _json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_r9_frozen_fibre_and_exact_taskepisode_shadow_are_bound() -> None:
    fibre = _json(BSD / "01_frontier/BSD_A1a1_R9_HIGHER_RANK_ES_CONTEXT_FIBRE_20260812.json")
    wrapper = _json(BSD / "07_memory/BSD_A1a1_R9_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode")
    episode = wrapper["taskepisode"]

    assert fibre["atom_id"] == "BSD-A1a1-THETA-ORDER-COMPARISON"
    assert fibre["packet_hash"] == "sha256:add723b4c6bed16e57583a6ec0f890f269d360d872765a0c0a7a2d7ee367e956"
    assert episode["fibre_snapshot_hash"] == fibre["packet_hash"].removeprefix("sha256:")
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert episode["artifact_hash"] == "c273ca5bf2bd6cad146f7e01176cf86f0e46351cb31cdf5eb3c270fee60ec998"
    assert wrapper["authority"] == "PROPOSAL_SHADOW_NO_SCIENTIFIC_AUTHORITY"


def test_r9_episode_diagnosis_failure_obstruction_are_distinct_and_nonpromoted() -> None:
    diagnosis = _json(BSD / "07_memory/BSD_A1a1_R9_DIAGNOSIS_SHADOW_20260812.json")
    failure = _json(BSD / "07_memory/BSD_A1a1_R9_BASIC_RANK_BASE_CHANGE_FAILURE_SHADOW_20260812.json")
    obstruction = _json(BSD / "07_memory/BSD_A1a1_R9_BASIC_RANK_BASE_CHANGE_OBSTRUCTION_SHADOW_20260812.json")

    assert diagnosis["artifact_type"] == "DIAGNOSIS_PROPOSAL_SHADOW"
    assert failure["artifact_type"] == "FAILURE_EXPERIENCE_PROPOSAL_SHADOW"
    assert obstruction["artifact_type"] == "OBSTRUCTION_PROPOSAL_SHADOW"
    assert diagnosis["episode_pointer"] == failure["episode_pointer"] == obstruction["episode_pointer"]
    assert diagnosis["local_mathematical_failure"] is False
    assert diagnosis["local_to_global_gluing_failure"] is True
    assert failure["retained_as_learning"] is False
    assert obstruction["retained_novelty_OBSTRUCTION"] == 0
    assert obstruction["promotion_status"] == "PROPOSAL_SHADOW_ONLY"


def test_r9_source_scope_keeps_basic_rank_distinct_from_analytic_rank() -> None:
    source = _json(BSD / "00_sources/BSD_A1a1_R9_HIGHER_RANK_ES_SOURCE_RECEIPT_20260812.json")
    fibre = _json(BSD / "01_frontier/BSD_A1a1_R9_HIGHER_RANK_ES_CONTEXT_FIBRE_20260812.json")

    claims = source["primary_source"]["claims_bound"]
    assert any("K=Q, r_T=1" in claim for claim in claims)
    assert any("r_T=2" in claim and "imaginary quadratic" in claim for claim in claims)
    assert any("Heegner point main conjecture" in claim for claim in claims)
    assert any("Conjecture 1.6" in claim and "complex leading-term" in claim for claim in claims)
    assert source["derived_scope_result"]["local_to_global_gluing_failure"] is True
    assert fibre["memory_routing"]["cross_millennium_query"].startswith("NOT_INVOKED")


def test_r9_trace_continues_merged_r7_and_quarantines_unmerged_r8() -> None:
    trace = _json(BSD / "09_trace/BSD_A1a1_R9_RESULT_TRACE_DELTA_20260812.json")

    assert trace["base_last_event_id"] == "BSD-A1a1-E26-R7-REVIEW"
    assert trace["base_last_event_hash"] == "sha256:be71bb36fdb30705154c45e1f6873bfb7fd7b401972e66ecf2c701a6ff18cac8"
    assert "R8 PR #181 was unmerged" in trace["off_chain_history_note"]
    previous = trace["base_last_event_hash"]
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        assert entry["artifact_hash"].startswith("sha256:")
        previous = entry["artifact_hash"]
    assert trace["authority"] == "PUBLIC_DECISION_TRACE_DELTA_NO_ROOT_AUTHORITY"


def test_r9_case_study_preserves_root_boundary_and_no_raw_growth_learning() -> None:
    case = (BSD / "07_memory/RAKL_METHOD_CASE_STUDY_BSD_A1a1_HIGHER_RANK_ES_20260812_R9.md").read_text(encoding="utf-8")

    assert "local-to-global/gluing failure, not a local mathematical failure" in case
    assert "KNOWLEDGE=1" in case
    assert "OBSTRUCTION=0" in case
    assert "raw repository growth is not counted as learning" in case
    assert "CANNOT_MEASURE" in case
