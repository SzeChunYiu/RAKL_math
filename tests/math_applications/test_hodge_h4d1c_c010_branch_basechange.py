import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"


def canonical_hash(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def load(rel):
    return json.loads((BASE / rel).read_text())


def test_c010_task_episode_is_content_bound_shadow():
    ep = load("07_memory/H4d1c_C010_TASK_EPISODE_SHADOW_20260812.json")
    claimed = ep.pop("artifact_hash")
    assert canonical_hash(ep) == claimed
    assert ep["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert ep["outcome"] == "PARTIAL_SUCCESS"
    assert "O-H4D1C-BRANCH-RELATIVE-SMOOTHNESS-OR-DIRECT-DOMINANCE" in ep["residual_signature"]


def test_c010_hash_chain_is_reconstructible():
    trace = load("09_trace/H4d1c_C010_HASH_CHAIN_TRACE_20260812.json")
    previous = None
    for event in trace["events"]:
        assert event["previous_event_hash"] == previous
        claimed = event["artifact_hash"]
        payload = {k: v for k, v in event.items() if k != "artifact_hash"}
        actual = "sha256:" + canonical_hash(payload)
        assert actual == claimed
        previous = claimed
    assert trace["terminal_event_hash"] == previous


def test_c010_scope_and_residual_guards():
    fibre = load("01_frontier/H4d1c_C010_FROZEN_FIBRE_20260812.json")
    metrics = load("09_trace/H4d1c_C010_RAKL_CYCLE_METRICS_20260812.json")
    failure = load("07_memory/H4d1c_C010_FAILURE_20260812.json")
    diagnosis = load("07_memory/H4d1c_C010_DIAGNOSIS_20260812.json")
    obstruction = load("07_memory/H4d1c_C010_OBSTRUCTION_20260812.json")

    assert "rational coefficients Q only at the root" in fibre["coefficient_category_scope"]
    assert fibre["application"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert failure["local_to_global_gluing_failure"] is False
    assert diagnosis["failure_category"] == "LOCAL_MATHEMATICAL_REPRESENTATION_AND_ROUTING"
    assert obstruction["obstruction_id"] == "O-H4D1C-BRANCH-RELATIVE-SMOOTHNESS-OR-DIRECT-DOMINANCE"
    assert set(metrics["retained_novelty_seven_axes"]) >= {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD"
    }
    for axis in ("KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD"):
        assert metrics["retained_novelty_seven_axes"][axis] == 0
    assert metrics["gates_and_provenance"]["root_promotion_gate"].startswith("BLOCKED")


def test_c010_result_does_not_overclaim_hodge_authority():
    route = (BASE / "03_routes/H4d1c_C010_BRANCH_BASECHANGE_SMOOTHNESS_NOGO_20260812.md").read_text()
    assert "not a necessary condition" in route
    assert "not claimed to be a Hodge witness incidence" in route
    assert "ROOT_AUTHORITY_NONE" in route
    assert "B tensor_A B ~= B" in route


def test_c010_repeated_process_failure_is_linked_not_promoted():
    pf = load("07_memory/H4d1c_C010_PROCESS_FAILURE_20260812.json")
    assert pf["mathematical_failure"] is False
    assert pf["repetition_count_in_this_lineage"] == 3
    assert "F-H4D1C-C008-PREFREEZE-HYPOTHESIS-EXPOSURE" in pf["repeat_link"]
    assert "F-H4D1C-C009-PREFREEZE-HYPOTHESIS-EXPOSURE" in pf["repeat_link"]
    assert pf["authority"] == "PROPOSAL_SHADOW_FAILURE_ONLY"
