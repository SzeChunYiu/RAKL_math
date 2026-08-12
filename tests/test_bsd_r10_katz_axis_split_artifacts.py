import hashlib, json
from pathlib import Path

BASE = Path("research/real_math/millennium/birch_swinnerton_dyer")

def load(rel):
    return json.loads((BASE / rel).read_text())

def test_bsd_r10_scope_and_gate_split():
    src = load("00_sources/BSD_A1a1_R10_KATZ_AXIS_GATE_SPLIT_SOURCE_AUDIT_20260812.json")
    assert src["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert src["verified_local_decomposition"]["dimension_gate"]["uses_finite_Sha_in_this_displayed_step"] is False
    assert src["verified_local_decomposition"]["dimension_gate"]["uses_ord_Lp_star_eq_1_in_this_displayed_step"] is False
    assert "finite Sha" in src["verified_local_decomposition"]["transverse_localization_gate"]["input"]
    assert src["coordinate_axis_audit"]["interpolation_region"].startswith("Theorem 2.1.1")
    assert src["bounded_current_literature_search"]["completeness"].startswith("NOT_CLAIMED")

def test_bsd_r10_shadow_episode_and_separation():
    ep = load("07_memory/BSD_A1a1_R10_KATZ_AXIS_TASK_EPISODE_SHADOW_20260812.taskepisode")
    dg = load("07_memory/BSD_A1a1_R10_KATZ_AXIS_DIAGNOSIS_SHADOW_20260812.json")
    fl = load("07_memory/BSD_A1a1_R10_KATZ_INTERPOLATION_FAILURE_SHADOW_20260812.json")
    ls = load("07_memory/BSD_A1a1_R10_GATE_SPLIT_LESSON_CANDIDATE_20260812.json")
    assert ep["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert ep["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert dg["episode_lineage"] == ep["episode_id"]
    assert fl["diagnosis_lineage"] == dg["diagnosis_id"]
    assert ls["authority"].startswith("CANDIDATE_PROPOSAL_ONLY")
    assert fl["failure_id"] not in ep["episode_id"]

def test_bsd_r10_trace_chain_and_no_root_promotion():
    tr = load("09_trace/BSD_A1a1_R10_KATZ_AXIS_TRACE_DELTA_20260812.json")
    prev = tr["base_last_event_hash"]
    for e in tr["entries"]:
        assert e["previous_event_hash"] == prev
        core = dict(e); got = core.pop("artifact_hash")
        calc = "sha256:" + hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()
        assert got == calc
        prev = got
    assert tr["terminal_event_hash"] == prev
    assert all("ROOT_CERTIFICATE" not in " ".join(e["outputs"]) for e in tr["entries"])
