from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "real_math" / "millennium" / "cross_problem"


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_sha256(payload: object) -> str:
    raw = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def test_xm016_task_episode_is_current_v3_shadow_and_content_bound():
    episode = _load(
        BASE
        / "07_memory"
        / "XM016_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
    )
    artifact_hash = episode.pop("artifact_hash")

    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["episode_id"] == "EP-XM016-PNP-HODGE-AGGREGATION-LAW-DW-20260812"
    assert episode["atom_id"] == "XM016-PNP-C043-TO-HODGE-H4d1c-AGGREGATION-LAW"
    assert episode["fibre_snapshot_hash"] == (
        "sha256:f4ecc79e5d5d77ab9681cf6a9d72432d6f52355906a8e1c69e2c90bdcf821a0e"
    )
    assert _canonical_sha256(episode) == artifact_hash


def test_xm016_differencewitness_falsifies_twin_overtransfer():
    transfer = _load(
        BASE
        / "01_frontier"
        / "XM016_AGGREGATION_LAW_DIFFERENCEWITNESS_20260812.json"
    )

    witness = transfer["DifferenceWitness"]
    assert witness["id"] == "DW-XM016-QUOTIENT-VS-SIGNED-CANCELLATION"
    assert transfer["cheapest_falsifier"]["result"] == "FALSIFIED"
    assert "equal" in witness["source_relation"]
    assert "signed" in witness["target_relation"]
    assert "aggregation law" in witness["nonpreserved_coordinates"]

    h1 = 1
    h2 = -1
    assert h1 != h2
    assert h1 + h2 == 0
    assert transfer["outcome"] == (
        "PARTIAL_SUCCESS_SUCCESSFUL_OVERTRANSFER_FALSIFICATION_STRUCTURAL_FAMILY_SPLIT"
    )


def test_xm016_episode_diagnosis_failure_lesson_are_distinct_and_nonpromoted():
    memory = _load(
        BASE / "07_memory" / "XM016_DIAGNOSIS_AND_LESSON_SHADOW_20260812.json"
    )

    ids = {
        memory["episode"]["id"],
        memory["diagnosis"]["id"],
        memory["failure"]["id"],
        memory["proposed_lesson"]["id"],
        memory["proposed_motif"]["id"],
    }
    assert len(ids) == 5
    assert memory["proposed_lesson"]["authority"] == "PROPOSAL_ONLY_NOT_PROMOTED"
    assert memory["proposed_lesson"]["counts_as_learning"] is False
    assert memory["proposed_motif"]["counts_as_learning"] is False
    assert memory["failure"]["warning_not_blacklist"] is True


def test_xm016_trace_is_hash_chained():
    trace = _load(BASE / "09_trace" / "XM016_HASH_CHAINED_TRACE_20260812.json")

    previous = "GENESIS"
    for entry in trace["entries"]:
        assert entry["previous_hash"] == previous
        digest_payload = {key: value for key, value in entry.items() if key != "entry_hash"}
        assert _canonical_sha256(digest_payload) == entry["entry_hash"]
        previous = entry["entry_hash"]

    assert trace["terminal_hash"] == previous


def test_xm016_metrics_are_conservative_and_exclude_noncomparable_pnp():
    packet = _load(
        BASE
        / "10_study_pattern"
        / "RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM016_20260812.json"
    )
    metrics = packet["RAKL_CYCLE_METRICS"]

    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["framework"]["git_sha"] == (
        "43897d3afaf0038385102d5acc64793c05ec40f0"
    )
    assert metrics["rakl_math"]["base_sha"] == (
        "e768b7da7dc48739ccb581dea0eb2cfeb8a701e7"
    )

    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["protected_retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
    }

    aggregate = metrics["cross_lane_aggregates"]
    assert aggregate["comparable_latest_lane_count"] == 5
    assert "P_vs_NP" in aggregate["excluded_lanes"]
    assert aggregate["latest_declared_retained_novelty_lower_bound"] == {
        "KNOWLEDGE": 3,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 3,
        "OBSTRUCTION": 3,
        "RELATION": 4,
        "PATH": 3,
        "META_METHOD": 0,
    }
    assert aggregate["latest_sampled_episode_record_presence"] == {
        "P_vs_NP": 0,
        "Riemann_Hypothesis": 1,
        "Navier_Stokes": 1,
        "Yang_Mills": 1,
        "Hodge": 1,
        "Birch_Swinnerton_Dyer": 1,
    }
    assert metrics["raw_repository_growth_counts_as_learning"] is False


def test_xm016_authority_and_framework_hypothesis_remain_proposal_only():
    packet = _load(
        BASE
        / "10_study_pattern"
        / "RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM016_20260812.json"
    )
    study = packet["RAKL_METHOD_CASE_STUDY"]
    metrics = packet["RAKL_CYCLE_METRICS"]

    hypothesis = study["framework_improvement_hypothesis"]
    assert hypothesis["framework_issue_opened"] is False
    assert metrics["gate_status"]["canonical_inventory"] == "NOT_INVOKED"
    assert metrics["gate_status"]["scientific_authority_promotion"] == "NOT_INVOKED"
    assert metrics["gate_status"]["root_authority"] == "NONE"
    assert metrics["gate_status"]["independent_mathematical_reviews"] == "0/3"
    assert study["repeated_process_failures"]["PNP_TELEMETRY_COMPARABILITY"][
        "classification"
    ] == "application/meta-policy, not framework defect"
