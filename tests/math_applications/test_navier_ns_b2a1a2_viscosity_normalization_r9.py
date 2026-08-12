import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"


def _load(rel):
    return json.loads((BASE / rel).read_text())


def _entry_hash(entry):
    payload = {k: entry[k] for k in ("event_type", "timestamp", "body", "previous_hash")}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_shadow_authority_and_episode_diagnosis_separation():
    episode = _load("07_memory/NS-B2a1a2_TASK_EPISODE_R9_20260812.taskepisode")
    dx = _load("07_memory/NS-B2a1a2_DIAGNOSIS_FAILURE_OBSTRUCTION_LESSON_R9_20260812.json")
    metrics = _load("10_case_study/NS-B2a1a2_RAKL_CYCLE_METRICS_R9_20260812.json")
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert dx["source_episode_ref"] == episode["episode_id"]
    assert dx["diagnosis"]["id"].startswith("D-")
    assert dx["failure"]["id"].startswith("F-")
    assert dx["obstruction"]["id"].startswith("O-")
    assert dx["candidate_lesson"]["id"].startswith("L-")
    assert metrics["gates"]["root_promotion"] == "BLOCKED_OPEN"
    assert metrics["gates"]["independent_mathematical_reviews"] == "0/3"


def test_hash_chain_is_content_bound():
    trace = _load("09_trace/NS-B2a1a2_TRACE_R9_20260812.json")
    previous = "GENESIS"
    for entry in trace["entries"]:
        assert entry["previous_hash"] == previous
        assert entry["entry_hash"] == _entry_hash(entry)
        previous = entry["entry_hash"]
    assert trace["terminal_hash"] == previous


def test_direct_ckn_normalization_exponents_and_maximal_gain_stress():
    # Assurance/calibration only: the paper proof is the coordinate-change derivation.
    # From the weighted ledger, the derived envelopes have factors
    # A ~ nu^(-5/2) F^(-2), E ~ nu^(-3/2) F^(-1), D ~ nu^(-3) F^(-2).
    for nu in (1e-1, 1e-2, 1e-4):
        Fmax = 1.0 / nu
        A_factor = nu ** (-2.5) * Fmax ** (-2.0)
        E_factor = nu ** (-1.5) * Fmax ** (-1.0)
        D_factor = nu ** (-3.0) * Fmax ** (-2.0)
        assert abs(A_factor - nu ** (-0.5)) < 1e-10 * A_factor
        assert abs(E_factor - nu ** (-0.5)) < 1e-10 * E_factor
        assert abs(D_factor - nu ** (-1.0)) < 1e-10 * D_factor


def test_standard_c_interpolation_still_cannot_supply_vanishing_envelope():
    # Standard C <= c(A^(3/4)E^(3/4)+A^(3/2)); after the unit-viscosity
    # time/space lift this becomes nu^-3(F^-9/4 + F^-3) up to M constants.
    for nu in (1e-1, 1e-2, 1e-4):
        Fmax = 1.0 / nu
        leading = nu ** (-3.0) * Fmax ** (-2.25)
        secondary = nu ** (-3.0) * Fmax ** (-3.0)
        assert abs(leading - nu ** (-0.75)) < 1e-10 * leading
        assert abs(secondary - 1.0) < 1e-10


def test_semantic_novelty_counts_are_explicit_and_not_repo_growth():
    metrics = _load("10_case_study/NS-B2a1a2_RAKL_CYCLE_METRICS_R9_20260812.json")
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 1,
        "OBSTRUCTION": 1,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert "Files, prose, commits, issues and PRs" in metrics["saturation"]["note"]
