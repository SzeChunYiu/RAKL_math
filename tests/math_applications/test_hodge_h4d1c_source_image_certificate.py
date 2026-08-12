from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HODGE = ROOT / "research/real_math/millennium/hodge/deformation"
CONTEXT = HODGE / "01_frontier/H4d1c_C005_SOURCE_IMAGE_CONTEXT_20260812.json"
ROUTE = HODGE / "03_routes/H4d1c_C005_CLOSED_TOPDIM_SOURCE_IMAGE_CERTIFICATE_20260812.md"
EPISODE = HODGE / "07_memory/H4d1c_C005_TASK_EPISODE_SHADOW_20260812.jsonl"
DIAGNOSIS = HODGE / "07_memory/H4d1c_C005_DIAGNOSIS_20260812.json"
OBSTRUCTION = HODGE / "07_memory/H4d1c_C005_OBSTRUCTION_20260812.json"
LESSON = HODGE / "07_memory/H4d1c_C005_CANDIDATE_LESSON_20260812.json"
METRICS = HODGE / "09_trace/H4d1c_C005_RAKL_CYCLE_METRICS_20260812.json"
TRACE = HODGE / "09_trace/H4d1c_C005_HASH_CHAIN_TRACE_20260812.json"
CASE_STUDY = HODGE / "10_case_study/H4d1c_C005_RAKL_METHOD_CASE_STUDY_20260812.md"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_packet_keeps_episode_diagnosis_obstruction_lesson_distinct() -> None:
    episode = json.loads(EPISODE.read_text(encoding="utf-8").strip())
    diagnosis = _load(DIAGNOSIS)
    obstruction = _load(OBSTRUCTION)
    lesson = _load(LESSON)

    assert episode["episode_id"] == "H4d1c-C005-CLOSED-TOPDIM-SOURCE-IMAGE-CERTIFICATE"
    assert diagnosis["diagnosis_id"] == "D-H4D1C-IMAGE-COMPLETENESS-IS-CLOSED-TOPDIM-PROBLEM"
    assert obstruction["obstruction_id"] == "O-H4D1C-SAME-CLASS-CLOSED-TOPDIM-SOURCE-IMAGE"
    assert lesson["lesson_id"] == "L-H4D1C-CLOSED-TOPDIM-IMAGE-COVERS-IRREDUCIBLE-BRANCH-V1"
    assert len({episode["episode_id"], diagnosis["diagnosis_id"], obstruction["obstruction_id"], lesson["lesson_id"]}) == 4
    assert lesson["authority"] == "CANDIDATE"
    assert "exact_mathematical_success_or_failure" in lesson
    assert "mathematical_evidence" in lesson


def test_source_image_certificate_states_all_load_bearing_hypotheses_and_scope() -> None:
    route = ROUTE.read_text(encoding="utf-8")
    for phrase in (
        "Exact same-class binding",
        "Closed image",
        "One irreducible target component",
        "Top-dimensional image",
        "Then `L = H` as reduced germs",
        "set-theoretic local branch coverage",
        "does **not** prove equality of scheme structures",
        "OPEN_NO_SOLUTION_CERTIFICATE",
    ):
        assert phrase in route

    assert "Delete closedness" in route
    assert "Delete irreducibility/component binding" in route
    assert "Delete exact-class binding" in route
    assert "Ignore monodromy" in route


def test_framework_pin_fibre_and_metrics_boundaries() -> None:
    context = _load(CONTEXT)
    metrics = _load(METRICS)
    assert context["framework"]["live_main_sha"] == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert context["framework"]["method_version"] == "3.0.0"
    assert context["fibre_snapshot_hash"] == metrics["active_atom"]["fibre_snapshot_hash"]
    assert context["context_hash"] == metrics["active_atom"]["context_hash"]
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["gate_provenance_ci"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["raw_repository_growth_counts_as_learning"] is False
    assert metrics["verification"]["independent_mathematical_review_credit"] == "0/3"


def test_trace_hash_chain_recomputes() -> None:
    trace = _load(TRACE)
    prev = "GENESIS"
    for event in trace["chain"]:
        payload = {key: event[key] for key in ("seq", "event", "payload")}
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        expected = "sha256:" + hashlib.sha256((prev + "|" + canonical).encode()).hexdigest()
        assert event["prev_hash"] == prev
        assert event["event_hash"] == expected
        prev = expected
    assert trace["chain_tip"] == prev


def test_case_study_explicitly_separates_local_math_from_gluing_and_process() -> None:
    study = CASE_STUDY.read_text(encoding="utf-8")
    assert "Global local-to-global continuation was **not attempted**" in study
    assert "Same-context review is not independent review" in study
    assert "Raw repository growth receives zero learning credit" in study
    assert "COMPOSITIONAL" in study
    assert "image-certificate checklist" in study
