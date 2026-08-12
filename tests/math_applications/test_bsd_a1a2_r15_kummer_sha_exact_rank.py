import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"
RESULT = BSD / "00_sources/BSD_A1a2_R15_KUMMER_SHA_EXACT_RANK_RESULT_20260812.json"
LESSON = BSD / "07_memory/BSD_A1a2_R15_SCOPED_MATHEMATICAL_LESSON_20260812.json"
TRACE = BSD / "09_trace/BSD_A1a2_R15_RETROSPECTIVE_RESULT_TRACE_20260812.json"
DAG = BSD / "02_problem_dag/BSD_A1a2_R15_KUMMER_SHA_DAG_DELTA_20260812.yaml"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def artifact_hash(value):
    payload = dict(value)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_r15_exact_sequence_lemma_and_scope_are_explicit():
    result = load(RESULT)
    lemma = result["lemma"]
    assert "corank_Zp S = rank_Z E(Q) + corank_Zp X" in lemma["statement"]
    assert "if and only if corank_Zp X=0" in lemma["statement"]
    assert "No actual elliptic curve with infinite Sha[p^infinity] is exhibited." in lemma["nonclaims"]
    assert result["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert result["root_promotion"] == "FORBIDDEN_NO_ROOT_CERTIFICATE"


def test_r15_preserves_all_seven_mathematical_lesson_fields():
    lesson = load(LESSON)
    required = {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "mathematical_falsifier",
        "mathematical_repair_or_next_discriminator",
        "proof_or_source_evidence",
    }
    assert required <= lesson.keys()
    assert lesson["supported_and_competing_causes"]["supported"]
    assert len(lesson["supported_and_competing_causes"]["competing"]) >= 3
    assert lesson["zero_mathematical_credit"] == [
        "git", "ci", "schema", "hash", "chronology", "telemetry"
    ]


def test_r15_does_not_backfill_strict_discovery_chronology():
    result, trace = load(RESULT), load(TRACE)
    assert result["authority"].startswith("RETROSPECTIVE_SOURCE_BOUND_HAND_LEMMA")
    assert result["discovery_chronology"].startswith("NOT_STRICT_CONTEXT_FIRST")
    assert trace["strict_pre_candidate_trace_present"] is False
    assert [event["event_type"] for event in trace["entries"]] == [
        "CANDIDATE_PROPOSED", "FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"
    ]


def test_r15_trace_and_artifacts_are_content_bound():
    for path in (RESULT, LESSON, TRACE):
        value = load(path)
        assert value["artifact_hash"] == artifact_hash(value)
    trace = load(TRACE)
    previous = None
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == artifact_hash(event)
        previous = event["artifact_hash"]
    assert trace["terminal_event_hash"] == previous


def test_r15_proof_dag_opens_sha_finiteness_child_and_keeps_root_open():
    dag = yaml.safe_load(DAG.read_text(encoding="utf-8"))
    assert dag["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert dag["closed_scoped_node"]["state"] == "SOURCE_BOUND_HAND_LEMMA"
    assert {node["id"] for node in dag["open_children"]} == {
        "BSD-A1a3-COMPLEX-RANK-TWO-TO-P-PRIMARY-SHA-FINITENESS-OR-INDEPENDENT-MW-RANK-TWO",
        "BSD-A1a2-COMPLEX-TAYLOR-ORDER-TO-KURIHARA-ORDER",
    }
    assert dag["root_promotion"] == "FORBIDDEN_NO_ROOT_CERTIFICATE"
