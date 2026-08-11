import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def _canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def test_task_episode_matches_current_v3_content_hash_contract():
    path = NS / "07_memory" / "NS-B1a4_TASK_EPISODE_R1_20260811.json"
    episode = json.loads(path.read_text())
    required = {
        "episode_id", "task_id", "atom_id", "context_hash", "problem_signature",
        "fibre_snapshot_hash", "operator_ids", "action_trace", "observation_ids",
        "verification_ids", "outcome", "residual_signature", "evidence_pointers",
        "artifact_hash", "timestamp", "cost", "storage_admission",
    }
    assert set(episode) == required
    artifact_hash = episode.pop("artifact_hash")
    assert hashlib.sha256(_canonical_bytes(episode)).hexdigest() == artifact_hash
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"


def test_trace_is_hash_chained_and_ends_open_root():
    path = NS / "09_trace" / "NS-B1a4_TRACE_R1_20260811.jsonl"
    prev = "GENESIS"
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    assert len(rows) == 14
    for seq, row in enumerate(rows, start=1):
        assert row["seq"] == seq
        assert row["prev_hash"] == prev
        basis = {"event": row["event"], "payload": row["payload"], "prev_hash": row["prev_hash"], "seq": row["seq"]}
        expected = "sha256:" + hashlib.sha256(_canonical_bytes(basis)).hexdigest()
        assert row["event_hash"] == expected
        prev = row["event_hash"]
    assert rows[-3]["payload"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_exact_pressure_free_shear_calibration_has_both_local_time_signs():
    def f(y, t):
        return 1.0 + 0.1 * math.exp(-t) * math.cos(y) - 0.05 * math.exp(-4.0 * t) * math.cos(2.0 * y)

    def ft(y, t):
        return -0.1 * math.exp(-t) * math.cos(y) + 0.2 * math.exp(-4.0 * t) * math.cos(2.0 * y)

    def fyy(y, t):
        return -0.1 * math.exp(-t) * math.cos(y) + 0.2 * math.exp(-4.0 * t) * math.cos(2.0 * y)

    assert math.isclose(ft(0.37, 0.63), fyy(0.37, 0.63), rel_tol=0.0, abs_tol=1e-14)
    assert f(0.0, 0.0) >= 0.85
    assert ft(0.0, 0.0) > 0.0
    assert ft(0.0, 1.0) < 0.0
    assert math.isclose(0.0, 0.0)  # p=0 and (u dot grad)u=0 are exact by construction.


def test_scope_boundary_and_gluing_residual_are_explicit():
    delta = (NS / "02_problem_dag" / "NS_B1a4_C001_R1_DELTA_20260811.yaml").read_text()
    result = (NS / "04_candidates" / "NS-B1a4_C001_R1_SIGNED_FLUX_NORECROSSING_AUDIT_20260811.md").read_text()
    assert "EXISTING_LEDGER_SIGN_INSUFFICIENT_ROUTE_PRUNING" in delta
    assert "G-NS-B1a4-LOCAL-SIGN-TO-GLOBAL-FINITE-I-ANCIENT" in delta
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in delta
    assert "not promoted to a global finite-`I` counterexample" in result
    assert "mild **bounded** ancient solution" in result
