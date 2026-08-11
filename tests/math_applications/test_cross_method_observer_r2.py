from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
METRICS = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_CYCLE_METRICS_CROSS_OBSERVER_20260811_R2.json"
STUDY = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_METHOD_CASE_STUDY_20260811_R2.md"


def _load() -> dict[str, object]:
    return json.loads(METRICS.read_text(encoding="utf-8"))


def test_observer_binds_current_subjects_and_stale_pin_separately() -> None:
    payload = _load()
    assert payload["framework"]["semantic_git_sha"] == "bd1a2768f0f474ff44ffa25243241f94bfaf6466"
    assert payload["application"]["base_sha"] == "d13bb40fab2448f983a73f5964ab2d3fd2db489c"
    assert payload["application"]["execution_dependency_pin"] == "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
    assert payload["framework"]["method_version"] == "CANNOT_MEASURE"


def test_known_novelty_aggregate_is_explicitly_partial() -> None:
    payload = _load()
    aggregate = payload["known_comparable_novelty_aggregate"]
    assert aggregate["included"] == ["NAVIER_STOKES", "YANG_MILLS", "HODGE", "BIRCH_SWINNERTON_DYER"]
    assert aggregate["excluded_cannot_measure"] == ["P_VS_NP", "RIEMANN_HYPOTHESIS"]
    assert aggregate["totals"] == {
        "KNOWLEDGE": 4,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 2,
        "OBSTRUCTION": 3,
        "RELATION": 4,
        "PATH": 2,
        "META_METHOD": 0,
    }
    assert aggregate["scope"].startswith("KNOWN_LOWER_BOUND_ONLY")


def test_unlicensed_cross_lane_rates_fail_closed() -> None:
    payload = _load()
    aggregate = payload["cross_lane_aggregates"]
    assert str(aggregate["repeated_failure_rate"]).startswith("CANNOT_MEASURE")
    assert str(aggregate["retrieval_miss_rate"]).startswith("CANNOT_MEASURE")
    assert str(aggregate["canonical_successful_reuse_count"]).startswith("CANNOT_MEASURE")
    assert aggregate["state_fingerprint_coverage"] == "0_OF_6_CANONICAL_CROSS_LANE_STATES"


def test_xm006_stays_retrospective_and_nonpromoting() -> None:
    payload = _load()
    xm006 = payload["cross_problem_action"]
    assert xm006["difference_witness_status"] == "RETROSPECTIVE_ZERO_PREREGISTRATION_CREDIT"
    assert xm006["exact_head_ci"] == "PASS_WORKFLOW_31492079826"
    assert xm006["integration_freshness"].startswith("BLOCKED_")
    assert payload["authority_boundary"]["root_solution_certificates_created"] == 0
    assert payload["authority_boundary"]["framework_promotions_created"] == 0
    assert payload["authority_boundary"]["tool_promotions_created"] == 0
    assert payload["authority_boundary"]["independent_review_credit"] is False


def test_metrics_self_hash_and_study_boundaries() -> None:
    payload = _load()
    claimed = payload.pop("artifact_hash")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    assert claimed == "sha256:" + hashlib.sha256(canonical).hexdigest()

    text = STUDY.read_text(encoding="utf-8")
    assert "not a six-problem total" in text
    assert "No Millennium root certificate changed" in text
    assert "Same-context roles receive no independent-review credit" in text
    assert "Raw files" not in text or "files, commits, prose, PRs or raw repository growth as learning" in text
