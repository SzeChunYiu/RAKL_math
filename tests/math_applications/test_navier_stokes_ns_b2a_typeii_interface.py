import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def _load(rel):
    return json.loads((NS / rel).read_text(encoding="utf-8"))


def _canonical_hash(payload):
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_ns_b2a_context_is_frozen_without_candidate_authority():
    context = _load("01_frontier/NS-B2a_CONTEXT_FIBER_20260811.json")
    assert context["atom_id"] == "NS-B2a"
    assert context["root_authority"] == "NONE"
    assert context["chronology"]["first_theorem_candidate_at"] is None
    assert context["chronology"]["retrospective_backward_smallness_strict_credit"] == "ZERO"
    assert "Euler" in context["object_context"]
    assert any(
        "backward uniqueness" in item.lower()
        for item in context["forbidden_shortcuts"]
    )

    packet_hash = context.pop("packet_hash")
    assert packet_hash == _canonical_hash(context)


def test_ns_b2a_trace_has_current_pre_candidate_order_and_hash_chain():
    trace = _load("09_trace/NS-B2a_PRE_CANDIDATE_TRACE_20260811.json")
    required = [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    event_types = [entry["event_type"] for entry in trace["entries"]]
    assert event_types == required
    assert "CANDIDATE_PROPOSED" not in event_types
    assert "PROMOTED" not in event_types

    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = {
            k: v
            for k, v in entry.items()
            if k not in {"artifact_hash", "previous_event_hash"}
        }
        assert entry["artifact_hash"] == _canonical_hash(payload)
        previous = entry["artifact_hash"]


def test_ns_b2a_dag_keeps_far_field_and_euler_rigidity_open():
    dag = _load("02_problem_dag/NS-B2a_DELTA_20260811.yaml")
    by_id = {item["id"]: item for item in dag["obligations"]}
    assert dag["root_authority"] == "NONE"
    assert by_id["NS-B2a-O3"]["status"] == "OPEN"
    assert by_id["NS-B2a-O4"]["strict_candidate_credit"] == "ZERO"
    assert by_id["NS-B2a-O5"]["status"] == "OPEN"
    assert by_id["NS-B2a-O6"]["status"] == "BLOCKED"
