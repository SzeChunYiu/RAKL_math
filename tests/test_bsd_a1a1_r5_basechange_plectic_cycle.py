import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"

FIBRE = BSD / "01_frontier" / "BSD_A1a1_R5_BASECHANGE_PLECTIC_CONTEXT_FIBRE_20260811.json"
SOURCE = BSD / "00_sources" / "BSD_A1a1_R5_BASECHANGE_PLECTIC_SOURCE_RECEIPT_20260811.json"
AUDIT = BSD / "01_frontier" / "BSD_A1a1_R5_BASECHANGE_PLECTIC_BRIDGE_AUDIT_20260811.md"
EPISODE = BSD / "07_memory" / "BSD_A1a1_R5_CURRENT_V3_TASK_EPISODE_SHADOW_20260811.taskepisode"
ADMISSION = BSD / "07_memory" / "BSD_A1a1_R5_CURRENT_V3_EPISODE_ADMISSION_20260811.episodeadmission"
DIAGNOSIS = BSD / "07_memory" / "BSD_A1a1_R5_DIAGNOSIS_SHADOW_20260811.json"
FAILURE = BSD / "07_memory" / "BSD_A1a1_R5_AUXILIARY_K_FAILURE_SHADOW_20260811.json"
OBSTRUCTION = BSD / "07_memory" / "BSD_A1a1_R5_AUXILIARY_K_OBSTRUCTION_SHADOW_20260811.json"
CASE_STUDY = BSD / "07_memory" / "RAKL_METHOD_CASE_STUDY_BSD_A1a1_BASECHANGE_PLECTIC_20260811_R5.md"
METRICS = BSD / "07_memory" / "BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R5.json"
TRACE = BSD / "09_trace" / "BSD_A1a1_R5_RESULT_TRACE_DELTA_20260811.json"
ROUTE = BSD / "02_problem_dag" / "BSD_A1a1_CURRENT_2026_ROUTE_DIAGNOSTIC.yaml"

EXPECTED_FIBRE = "sha256:0738fbeff600a8025d89c0d0c215272768e23133d2291e0cbb29734d08f1ecf2"
R4_LAST = "sha256:b66bf6b5d2f0b91823a1eb049586da2b98d8e1f6463419c50adeec8f7d6fe603"


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _hash_without_artifact_hash(obj):
    payload = dict(obj)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _strict_episode_hash(obj):
    payload = dict(obj)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def _admission_hash(obj):
    payload = dict(obj)
    payload.pop("receipt_canonical_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def _assert_hash(label, obj):
    stored = obj["artifact_hash"]
    computed = _hash_without_artifact_hash(obj)
    if stored != computed:
        print(f"::error title=R5 hash mismatch::{label} stored={stored} computed={computed}")
    assert stored == computed


def test_r5_required_packet_surfaces_exist():
    for path in (FIBRE, SOURCE, AUDIT, EPISODE, ADMISSION, DIAGNOSIS, FAILURE, OBSTRUCTION, CASE_STUDY, METRICS, TRACE, ROUTE):
        assert path.exists(), path


def test_r5_hashes_and_fibre_binding():
    for path in (SOURCE, DIAGNOSIS, FAILURE, OBSTRUCTION, METRICS):
        _assert_hash(path.name, _load(path))

    episode = _load(EPISODE)
    admission = _load(ADMISSION)
    assert episode["artifact_hash"] == _strict_episode_hash(episode)
    assert admission["receipt_canonical_sha256"] == _admission_hash(admission)

    assert episode["context_hash"] == EXPECTED_FIBRE
    assert episode["fibre_snapshot_hash"] == EXPECTED_FIBRE
    assert _load(DIAGNOSIS)["context_hash"] == EXPECTED_FIBRE
    assert _load(FAILURE)["context_hash"] == EXPECTED_FIBRE
    assert _load(OBSTRUCTION)["context_hash"] == EXPECTED_FIBRE
    assert _load(METRICS)["active_atom"]["fibre_snapshot_hash"] == EXPECTED_FIBRE


def test_r5_strict_v3_episode_admission_and_episode_diagnosis_failure_obstruction_separation():
    episode = _load(EPISODE)
    admission = _load(ADMISSION)
    diagnosis = _load(DIAGNOSIS)
    failure = _load(FAILURE)
    obstruction = _load(OBSTRUCTION)

    required = {
        "episode_id", "task_id", "atom_id", "context_hash", "problem_signature",
        "fibre_snapshot_hash", "operator_ids", "action_trace", "observation_ids",
        "verification_ids", "outcome", "residual_signature", "evidence_pointers",
        "artifact_hash", "timestamp", "cost", "storage_admission",
    }
    assert set(episode) == required
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert admission["episode_id"] == episode["episode_id"]
    assert admission["episode_artifact_hash"] == episode["artifact_hash"]
    assert admission["storage_status"] == "PROPOSAL_SHADOW_STORED"
    assert admission["inventory_registry_id"].startswith("shadow:")

    assert diagnosis["source_episode_id"] == episode["episode_id"]
    assert failure["source_episode_id"] == episode["episode_id"]
    assert failure["diagnosis_id"] == diagnosis["diagnosis_id"]
    assert failure["status"] == "OBSERVED_ONLY"
    assert obstruction["source_episode_id"] == episode["episode_id"]
    assert obstruction["diagnosis_id"] == diagnosis["diagnosis_id"]
    assert obstruction["failure_id"] == failure["failure_id"]
    assert obstruction["promotion_status"] == "PROPOSAL_SHADOW_ONLY"


def test_r5_trace_extends_r4_hash_chain():
    trace = _load(TRACE)
    assert trace["base_last_event_hash"] == R4_LAST
    previous = R4_LAST
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        _assert_hash(event["event_id"], event)
        previous = event["artifact_hash"]
    assert previous == "sha256:168c42cc9f472ea942413e52b1ac96dd17dfc76277c464a8dde400a48ea7649e"


def test_r5_source_scope_and_complex_coordinate_local_lemma():
    source = _load(SOURCE)
    derivation = source["exact_local_derivation"]
    assert "ord_{s=1} L(E/K,s)=2" in derivation["conclusions"]
    assert "L''(E/K,1)=L''(E,1)*L(E^K,1) != 0" in derivation["conclusions"]
    assert source["downstream_bridge_audit"]["result"] == "NO_EXACT_TARGET_CELL_THEOREM_LOCATED_IN_BOUNDED_SEARCH"
    assert source["downstream_bridge_audit"]["nonexistence_claim"] is False
    assert source["local_condition_compatibility_audit"]["verdict"].startswith("STRONG_FINITE_LOCAL_PRESCRIPTION_EVIDENCE")
    assert source["root_scope_guard"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_r5_metrics_are_conservative_and_use_current_method_surfaces():
    metrics = _load(METRICS)
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["framework"]["software_package_version"] == "0.1.0"
    required_surfaces = {
        "memory", "routing", "search_query_generation", "source_selection_reliability",
        "claim_extraction", "ontology_terminology_normalization", "mathematical_context_translation",
        "equivalence_similarity", "contextual_theory_gluing", "contradiction_diagnosis",
        "gap_discovery", "experiment_query_selection", "synthesis", "review", "saturation_stopping",
    }
    assert required_surfaces <= set(metrics["process_surfaces_invoked"])
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 1,
        "PATH": 1,
        "META_METHOD": 0,
    }
    assert metrics["outcome"]["novelty_class_primary"] == "compositional"
    assert metrics["gates"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gates"]["candidate_generated"] is False
    assert metrics["gates"]["same_context_review_independent"] is False
    assert metrics["gates"]["protected_obstruction_promotion"] is False
    assert metrics["hypothesis_and_coordinate_ledger"]["complex_vs_p_adic_coordinate_faithfulness"].startswith("PRESERVED_COMPLEX_S")
    assert metrics["state_fingerprints"]["warning"].endswith("not counted as learning")
    assert metrics["rakl_action_effect"]["causal_attribution_claim"] is False


def test_r5_route_keeps_local_and_global_residuals_separate():
    route = ROUTE.read_text(encoding="utf-8")
    assert "AUXILIARY_K_EXACT_PLECTIC_LOCAL_RESIDUAL_COMPATIBILITY_PLUS_NONVANISHING" in route
    assert "E_OVER_K_COMPLEX_SECOND_DERIVATIVE_TO_PLECTIC_NONVANISHING" in route
    assert "PLETIC_SELMER_TO_E_OVER_Q_MORDELL_WEIL_REGULATOR_SHA_TAMAGAWA_TORSION_GLUING" in route
    assert "LOCAL_SOURCE_INTERFACE" in route
    assert "LOCAL_MATHEMATICAL_BRIDGE" in route
    assert "LOCAL_TO_GLOBAL_GLUING" in route
    assert "root_state: OPEN_NO_SOLUTION_CERTIFICATE" in route
