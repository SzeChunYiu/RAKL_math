import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FRONTIER = ROOT / "research/real_math/millennium/cross_problem/01_frontier/XM018_HODGE_BSD_CONJUNCTIVE_GLUE_DIFFERENCEWITNESS_20260812.json"
EPISODE = ROOT / "research/real_math/millennium/cross_problem/07_memory/XM018_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
TRACE = ROOT / "research/real_math/millennium/cross_problem/09_trace/XM018_HASH_CHAINED_TRACE_20260812.json"
METRICS = ROOT / "research/real_math/millennium/cross_problem/10_study_pattern/RAKL_METHOD_CASE_STUDY_AND_CYCLE_METRICS_XM018_20260812.json"


def _load(path):
    return json.loads(path.read_text())


def _canonical_hash(document):
    payload = {k: v for k, v in document.items() if k != "artifact_hash"}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_xm018_shadow_authority_and_binding():
    frontier = _load(FRONTIER)
    episode = _load(EPISODE)
    assert frontier["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["episode"]["fibre_snapshot_hash"] == frontier["fibre_snapshot_hash"]
    assert frontier["artifact_hash"] == _canonical_hash(frontier)
    assert episode["episode"]["artifact_hash"] == _canonical_hash(episode["episode"])
    assert episode["authority"].startswith("PROPOSAL_SHADOW_ONLY")


def test_xm018_differencewitness_is_scoped_nonexpansion():
    frontier = _load(FRONTIER)
    assert frontier["difference_witness"]["hard_boundary"] == "INTERSECTION_IS_NOT_GENERATION"
    assert frontier["cheapest_falsifier"]["verdict"] == "TRANSFER_SURVIVES_IN_SCOPED_LINEARIZED_FORM"
    assert any("generative" in item.lower() for item in frontier["disanalogies"])
    # Exact finite-dimensional calibration: if all candidate directions have zero
    # localization, taking further intersections cannot create a nonzero one.
    loc_values = {"k": 0, "w": 1}
    conjunctive_carrier = {"k"}
    assert all(loc_values[v] == 0 for v in conjunctive_carrier)
    generated_carrier = {"k", "w"}
    assert any(loc_values[v] != 0 for v in generated_carrier)


def test_xm018_trace_is_hash_chained_and_root_unpromoted():
    trace = _load(TRACE)
    previous = "GENESIS"
    for entry in trace["entries"]:
        assert entry["previous_hash"] == previous
        assert entry["artifact_hash"] == _canonical_hash(entry)
        previous = entry["artifact_hash"]
    assert trace["terminal_hash"] == previous
    assert trace["authority"] == "PROPOSAL_SHADOW_ONLY"


def test_xm018_metrology_has_all_seven_axes_and_no_protected_growth():
    metrics = _load(METRICS)["RAKL_CYCLE_METRICS"]
    axes = {"KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION", "RELATION", "PATH", "META_METHOD"}
    assert set(metrics["retained_semantic_novelty"].keys()) == axes
    assert set(metrics["protected_retained_semantic_novelty"].keys()) == axes
    assert all(v == 0 for v in metrics["protected_retained_semantic_novelty"].values())
    assert metrics["gate_provenance_ci"]["root_status"] == "ALL_SIX_OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["independent_mathematical_review"] == "0/3"
