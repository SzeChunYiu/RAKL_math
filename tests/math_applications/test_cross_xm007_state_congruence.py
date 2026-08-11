from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAPPING = ROOT / "research/real_math/millennium/cross_problem/07_memory/XM007_STATE_CONGRUENCE_TRANSFER_MAPPING_20260811.json"
AUDIT = ROOT / "research/real_math/millennium/cross_problem/04_candidates/XM007_STATE_CONGRUENCE_HODGE_AUDIT_20260811.md"
METRICS = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_CYCLE_METRICS_CROSS_OBSERVER_20260811_R3.json"
CASE = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_METHOD_CASE_STUDY_20260811_R3.md"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _assert_self_hash(payload: dict[str, object]) -> None:
    stored = payload.pop("artifact_hash")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    assert stored == "sha256:" + hashlib.sha256(canonical).hexdigest()


def test_mapping_is_search_control_only_and_binds_exact_subjects() -> None:
    mapping = _load(MAPPING)
    assert mapping["transfer_id"] == "XM007"
    assert mapping["framework"]["main_sha"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert mapping["application"]["base_sha"] == "6557b1b25fa839fe71aba8047c958d5da892edd8"
    assert mapping["source_atom"]["source_pr"] == 78
    assert mapping["target_atom"]["target_pr"] == 77
    assert mapping["target_atom"]["canonicality"] == "OPEN_STACKED_TARGET_NOT_CURRENT_MAIN_AUTHORITY"
    assert "SEARCH_CONTROL_ONLY" in mapping["authority"]
    assert mapping["chronology"]["target_test"] == "PROSPECTIVE_SPECIFICATION_ONLY_NOT_EXECUTED"
    assert mapping["framework_feedback"]["new_issue_opened"] is False


def test_mapping_self_hash_is_canonical() -> None:
    _assert_self_hash(_load(MAPPING))


def test_equal_projected_state_different_outcome_falsifies_sufficiency() -> None:
    # Domain-neutral planted collision for the XM007 audit operation.
    states = [("coarse", 0), ("coarse", 1)]

    def coarse(state: tuple[str, int]) -> str:
        return state[0]

    def outcome(state: tuple[str, int]) -> int:
        return state[1]

    assert coarse(states[0]) == coarse(states[1])
    assert outcome(states[0]) != outcome(states[1])

    # A refined representation that retains the outcome-relevant coordinate
    # separates this planted pair. This is a generic state-sufficiency fixture,
    # not a Hodge or P-vs-NP theorem.
    def refined(state: tuple[str, int]) -> tuple[str, int]:
        return state

    assert refined(states[0]) != refined(states[1])


def test_primary_source_controls_and_hodge_nonclaim_are_explicit() -> None:
    mapping = _load(MAPPING)
    ids = {item["id"] for item in mapping["primary_source_anchors"]}
    assert ids == {
        "Cavalar-Oliveira-TR25-033",
        "Nishinou-2009.01651",
        "Kloosterman-2104.14845",
        "Movasati-1902.00831",
    }
    text = AUDIT.read_text(encoding="utf-8")
    assert "not a transfer of P-vs-NP mathematics" in text
    assert "does not yet instantiate the exact future `pi` collision" in text
    assert "No Millennium root status changes" in text


def test_r3_metrics_cover_all_axes_and_fail_closed_on_missing_lanes() -> None:
    metrics = _load(METRICS)
    axes = {"KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD"}
    transfer = metrics["cross_problem_action"]["retained_semantic_novelty"]
    assert set(transfer) == axes
    assert transfer == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    aggregate = metrics["known_comparable_latest_lane_novelty_aggregate"]
    assert set(aggregate["excluded_cannot_measure"]) == {"P_VS_NP", "RH_ANALYTIC", "HODGE_DEFORMATION"}
    assert metrics["cross_lane_aggregates"]["state_fingerprint_coverage"] == "0_OF_8_SCIENCE_LANES_CANONICAL_MATERIALIZED_STATES"
    assert metrics["application"]["execution_dependency_pin"] == metrics["framework"]["semantic_git_sha"]
    assert metrics["authority_boundary"]["raw_repository_growth_counted_as_learning"] is False


def test_r3_metrics_self_hash_and_identity_collision_owner() -> None:
    metrics = _load(METRICS)
    patterns = {item["pattern"]: item for item in metrics["recurring_process_patterns"]}
    assert patterns["CONCURRENT_HUMAN_ATOM_IDS_CAN_COLLIDE_ACROSS_BRANCHES"]["owner"] == "RAKL#142"
    _assert_self_hash(metrics)


def test_case_study_preserves_causal_and_identity_boundaries() -> None:
    text = CASE.read_text(encoding="utf-8")
    assert "two independent Navier–Stokes branches froze different mathematical atoms under the same human identity `NS-B1a2`" in text
    assert "No exact model-only/pre-memory counterfactual was frozen" in text
    assert "No Millennium root certificate changed" in text
