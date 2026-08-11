import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"
M = BSD / "07_memory"
F = BSD / "01_frontier"
D = BSD / "02_problem_dag"

SOURCE = BSD / "00_sources" / "BSD_A1a1_R5_BASECHANGE_PLECTIC_SOURCE_RECEIPT_20260811.json"
EPISODE = M / "BSD_A1a1_R5_CURRENT_V3_TASK_EPISODE_SHADOW_20260811.taskepisode"
ADMISSION = M / "BSD_A1a1_R5_CURRENT_V3_EPISODE_ADMISSION_20260811.episodeadmission"
DIAGNOSIS = M / "BSD_A1a1_R5_DIAGNOSIS_SHADOW_20260811.json"
FAILURE = M / "BSD_A1a1_R5_AUXILIARY_K_FAILURE_SHADOW_20260811.json"
OBSTRUCTION = M / "BSD_A1a1_R5_AUXILIARY_K_OBSTRUCTION_SHADOW_20260811.json"
METRICS = M / "BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R5.json"
TRACE = BSD / "09_trace" / "BSD_A1a1_R5_RESULT_TRACE_DELTA_20260811.json"
ROUTE = D / "BSD_A1a1_R5_BASECHANGE_PLECTIC_ROUTE_DIAGNOSTIC_20260811.yaml"
FIBRE = F / "BSD_A1a1_R5_BASECHANGE_PLECTIC_CONTEXT_FIBRE_20260811.json"
AUDIT = F / "BSD_A1a1_R5_BASECHANGE_PLECTIC_BRIDGE_AUDIT_20260811.md"
CASE_STUDY = M / "RAKL_METHOD_CASE_STUDY_BSD_A1a1_BASECHANGE_PLECTIC_20260811_R5.md"

FIBRE_HASH = "sha256:0738fbeff600a8025d89c0d0c215272768e23133d2291e0cbb29734d08f1ecf2"
R4_LAST = "sha256:b66bf6b5d2f0b91823a1eb049586da2b98d8e1f6463419c50adeec8f7d6fe603"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(obj, field="artifact_hash", prefix="sha256:"):
    payload = dict(obj)
    payload.pop(field, None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return prefix + hashlib.sha256(raw).hexdigest()


def test_r5_packet_exists_and_prior_current_route_is_not_modified():
    for path in [SOURCE, EPISODE, ADMISSION, DIAGNOSIS, FAILURE, OBSTRUCTION,
                 METRICS, TRACE, ROUTE, FIBRE, AUDIT, CASE_STUDY]:
        assert path.exists(), path
    current_route = D / "BSD_A1a1_CURRENT_2026_ROUTE_DIAGNOSTIC.yaml"
    text = current_route.read_text(encoding="utf-8")
    assert text.startswith("schema_version: bsd-current-frontier-route-diagnostic-v1")
    assert "cycle_base: 8a608f340d47b4b6ae612275b0595faf6b804432" in text


def test_r5_hashes_and_v3_episode_admission():
    for path in [SOURCE, DIAGNOSIS, FAILURE, OBSTRUCTION, METRICS]:
        obj = load(path)
        assert obj["artifact_hash"] == canonical_hash(obj)

    episode = load(EPISODE)
    strict = canonical_hash(episode, prefix="")
    assert episode["artifact_hash"] == strict
    assert episode["context_hash"] == FIBRE_HASH
    assert episode["fibre_snapshot_hash"] == FIBRE_HASH
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"

    admission = load(ADMISSION)
    expected = canonical_hash(admission, field="receipt_canonical_sha256", prefix="")
    assert admission["receipt_canonical_sha256"] == expected
    assert admission["episode_id"] == episode["episode_id"]
    assert admission["episode_artifact_hash"] == episode["artifact_hash"]


def test_r5_episode_diagnosis_failure_obstruction_are_distinct():
    episode = load(EPISODE)
    diagnosis = load(DIAGNOSIS)
    failure = load(FAILURE)
    obstruction = load(OBSTRUCTION)
    assert diagnosis["source_episode_id"] == episode["episode_id"]
    assert failure["diagnosis_id"] == diagnosis["diagnosis_id"]
    assert failure["status"] == "OBSERVED_ONLY"
    assert obstruction["failure_id"] == failure["failure_id"]
    assert obstruction["promotion_status"] == "PROPOSAL_SHADOW_ONLY"


def test_r5_trace_extends_r4_chain():
    trace = load(TRACE)
    assert trace["base_last_event_hash"] == R4_LAST
    previous = R4_LAST
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == canonical_hash(event)
        previous = event["artifact_hash"]
    assert previous == "sha256:168c42cc9f472ea942413e52b1ac96dd17dfc76277c464a8dde400a48ea7649e"


def test_r5_source_scope_and_exact_complex_relation():
    source = load(SOURCE)
    conclusions = source["exact_local_derivation"]["conclusions"]
    assert "ord_{s=1} L(E/K,s)=2" in conclusions
    assert "L''(E/K,1)=L''(E,1)*L(E^K,1) != 0" in conclusions
    assert source["downstream_bridge_audit"]["nonexistence_claim"] is False
    assert source["root_scope_guard"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_r5_metrics_and_route_are_conservative():
    metrics = load(METRICS)
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1, "OPERATOR": 0, "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0, "RELATION": 1, "PATH": 1, "META_METHOD": 0,
    }
    assert metrics["outcome"]["novelty_class_primary"] == "compositional"
    assert metrics["gates"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gates"]["candidate_generated"] is False
    assert metrics["gates"]["protected_obstruction_promotion"] is False
    assert metrics["rakl_action_effect"]["causal_attribution_claim"] is False

    route = ROUTE.read_text(encoding="utf-8")
    for token in [
        "AUXILIARY_K_EXACT_PLECTIC_LOCAL_RESIDUAL_COMPATIBILITY_PLUS_NONVANISHING",
        "E_OVER_K_COMPLEX_SECOND_DERIVATIVE_TO_PLECTIC_NONVANISHING",
        "PLETIC_SELMER_TO_E_OVER_Q_MORDELL_WEIL_REGULATOR_SHA_TAMAGAWA_TORSION_GLUING",
        "LOCAL_SOURCE_INTERFACE", "LOCAL_MATHEMATICAL_BRIDGE", "LOCAL_TO_GLOBAL_GLUING",
        "root_state: OPEN_NO_SOLUTION_CERTIFICATE",
    ]:
        assert token in route
