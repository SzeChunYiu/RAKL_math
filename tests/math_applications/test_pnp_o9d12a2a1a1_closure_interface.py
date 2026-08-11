from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "research"
    / "real_math"
    / "millennium"
    / "p_vs_np"
    / "05_falsification"
    / "closure_state_interface_gneq.py"
)


def _load():
    spec = importlib.util.spec_from_file_location("closure_state_interface_gneq", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_normalized_gneq_closure_activation_is_exactly_signature_xor():
    module = _load()
    report = module.audit_small_worlds(n_max=5, k_max=2)
    assert report["verdict"] == "NO_DERIVED_DIFFERENCEWITNESS_WITHIN_NORMALIZED_GNEQ"
    assert report["partition_families_checked"] == 1424
    assert report["ordered_edge_states_checked"] == 24896
    assert report["raw_base_only_difference_example"] is not None


def test_explicit_base_only_collision_does_not_create_higher_order_activation():
    module = _load()
    # U={d0,d1,d2,d3}; E={d0}, H=U\E.
    cuts = (1,)
    assert module.joint_signature(cuts, 0) == (1,)
    assert module.joint_signature(cuts, 1) == (0,)
    assert module.joint_signature(cuts, 2) == (0,)
    assert module.first_stage_activation(cuts, 0, 1) == (True,)
    assert module.first_stage_activation(cuts, 0, 2) == (True,)
    assert module.base_closure(4, 0, 1) != module.base_closure(4, 0, 2)
    full_state = frozenset(range(1 << 4))
    assert module.source_partition_closure(4, cuts, 0, 1) == full_state
    assert module.source_partition_closure(4, cuts, 0, 2) == full_state


def _canonical_hash(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_interface_audit_trace_is_parent_chained_and_candidate_free():
    trace_path = (
        ROOT
        / "research"
        / "real_math"
        / "millennium"
        / "p_vs_np"
        / "09_trace"
        / "O9d12a2a1a1_INTERFACE_AUDIT_TRACE_CONTINUATION_20260811.json"
    )
    trace = json.loads(trace_path.read_text(encoding="utf-8"))
    previous = trace["parent_terminal_hash"]
    assert previous == "sha256:5ab389f01170411bd429c4e742ca1bb1a0caef0244cec9b0a1a6ba0100163e5c"
    assert all(entry["event_type"] != "CANDIDATE_PROPOSED" for entry in trace["entries"])
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = dict(entry)
        expected = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert expected == _canonical_hash(payload)
        previous = expected


def test_interface_audit_dag_keeps_root_open_and_requires_fresh_child_context():
    parent_path = (
        ROOT
        / "research"
        / "real_math"
        / "millennium"
        / "p_vs_np"
        / "02_problem_dag"
        / "O9d12a2a1a1.yaml"
    )
    child_path = parent_path.with_name("O9d12a2a1a1a.yaml")
    parent = parent_path.read_text(encoding="utf-8")
    child = child_path.read_text(encoding="utf-8")
    assert "INTERFACE_AUDIT_NEGATIVE_REATOMIZE_REQUIRED" in parent
    assert "candidate_generation: BLOCKED" in parent
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in parent
    assert "status: OPEN_CONTEXT_REQUIRED" in child
    assert "context_fiber: REQUIRED_FRESH" in child
    assert "candidate_generation: BLOCKED_UNTIL_STRICT_PACKET_AND_MACHINE_GATE" in child
