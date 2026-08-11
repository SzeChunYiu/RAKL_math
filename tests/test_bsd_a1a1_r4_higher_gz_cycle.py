import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BSD = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer"

PRE = BSD / "07_memory" / "BSD_A1a1_R4_PREACTION_RECEIPT_20260811.json"
SOURCE = BSD / "00_sources" / "BSD_A1a1_R4_COMPLEX_HIGHER_GZ_SOURCE_RECEIPT_20260811.json"
EPISODE = BSD / "07_memory" / "BSD_A1a1_R4_COMPLEX_HIGHER_GZ_TASK_EPISODE_SHADOW_20260811.json"
STRICT_EPISODE = BSD / "07_memory" / "BSD_A1a1_R4_CURRENT_V3_TASK_EPISODE_SHADOW_20260811.taskepisode"
ADMISSION = BSD / "07_memory" / "BSD_A1a1_R4_CURRENT_V3_EPISODE_ADMISSION_20260811.episodeadmission"
FAILURE = BSD / "07_memory" / "BSD_A1a1_R4_COMPLEX_HIGHER_GZ_FAILURE_SHADOW_20260811.json"
TOOL_FAILURE = BSD / "07_memory" / "BSD_A1a1_R4_LEGACY_EPISODE_INVENTORY_FAILURE_SHADOW_20260811.json"
METRICS = BSD / "07_memory" / "BSD_A1a1_RAKL_CYCLE_METRICS_20260811_R4.json"
METRICS_V3 = BSD / "07_memory" / "BSD_A1a1_RAKL_CYCLE_METRICS_CURRENT_V3_SUCCESSOR_20260811_R4.json"
PRETRACE = BSD / "09_trace" / "BSD_A1a1_R4_PREACTION_TRACE_DELTA_20260811.json"
RESULTTRACE = BSD / "09_trace" / "BSD_A1a1_R4_RESULT_TRACE_DELTA_20260811.json"


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
        print(f"::error title=R4 hash mismatch::{label} stored={stored} computed={computed}")
    assert stored == computed


def test_r4_artifact_hashes_and_fibre_binding():
    expected_fibre = "sha256:385d587cb9ab74512adc3fed98e00df9a804c37fd327539c2cea449a97b5417d"
    for path in (PRE, SOURCE, EPISODE, FAILURE, TOOL_FAILURE, METRICS, METRICS_V3):
        _assert_hash(path.name, _load(path))

    assert _load(PRE)["fibre_snapshot_hash"] == expected_fibre
    assert _load(EPISODE)["context_hash"] == expected_fibre
    assert _load(FAILURE)["context_hash"] == expected_fibre
    assert _load(METRICS)["active_atom"]["fibre_snapshot_hash"] == expected_fibre
    assert _load(METRICS_V3)["active_atom"]["fibre_snapshot_hash"] == expected_fibre


def test_r4_current_v3_task_episode_is_exact_shadow_and_not_legacy_inventory_authority():
    episode = _load(STRICT_EPISODE)
    admission = _load(ADMISSION)
    extended = _load(EPISODE)
    failure = _load(FAILURE)

    required = {
        "episode_id", "task_id", "atom_id", "context_hash", "problem_signature",
        "fibre_snapshot_hash", "operator_ids", "action_trace", "observation_ids",
        "verification_ids", "outcome", "residual_signature", "evidence_pointers",
        "artifact_hash", "timestamp", "cost", "storage_admission",
    }
    assert set(episode) == required
    assert episode["artifact_hash"] == _strict_episode_hash(episode)
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert admission["episode_id"] == episode["episode_id"]
    assert admission["episode_artifact_hash"] == episode["artifact_hash"]
    assert admission["storage_status"] == "PROPOSAL_SHADOW_STORED"
    assert admission["inventory_registry_id"].startswith("shadow:")
    assert admission["receipt_canonical_sha256"] == _admission_hash(admission)

    # Legacy pinned inventory scans research/*.json for a top-level episode_id.
    # Extended/failure JSON records are not TaskEpisodes and do not claim that identity;
    # authority is content/hash/storage-bound in the exact current-v3 companion above.
    assert "episode_id" not in extended
    assert extended["shadow_episode_id"] == episode["episode_id"]
    assert "episode_id" not in failure
    assert failure["source_episode_id"] == episode["episode_id"]
    assert extended["successful_reuse_ids"] == ["T-XM-ROOT-BRIDGE-STABILITY-AUDIT"]
    rejected = {item["id"] for item in extended["operators_and_motifs"] if item["status"] == "REJECTED"}
    assert "TREAT_P_ADIC_DERIVATIVE_AS_COMPLEX_S_DERIVATIVE" in rejected


def test_r4_trace_chain_is_contiguous_and_hash_valid():
    pre = _load(PRETRACE)
    result = _load(RESULTTRACE)
    assert result["base_last_event_hash"] == pre["entries"][-1]["artifact_hash"]

    events = pre["entries"] + result["entries"]
    previous = pre["base_last_event_hash"]
    for event in events:
        assert event["previous_event_hash"] == previous
        _assert_hash(event["event_id"], event)
        previous = event["artifact_hash"]


def test_r4_target_ontology_blocks_coordinate_conflation():
    source = _load(SOURCE)
    assert source["bounded_search_result"] == "NO_TARGET_CELL_THEOREM_LOCATED"
    assert source["nonexistence_claim"] is False
    axes = {item["axis"] for item in source["ontology_normalization"]["distinct_axes"]}
    assert axes == {
        "COMPLEX_DERIVATIVE_ORDER",
        "WEIGHT_OR_CYCLE_CODIMENSION",
        "P_ADIC_DEFORMATION_DERIVATIVE_ORDER",
    }
    assert "COMPLEX_S_DERIVATIVE_ORDER_TWO" in source["ontology_normalization"]["target_cell"]


def test_r4_metrics_have_current_surfaces_and_all_novelty_axes():
    metrics = _load(METRICS_V3)
    assert metrics["framework"]["method_version"] == "3.0.0"
    assert metrics["framework"]["current_main_sha"] == "3299072b410ac9136548dfd103e846fc7656c31e"
    required_surfaces = {
        "memory", "routing", "search_query_generation", "source_selection_reliability",
        "claim_extraction", "ontology_terminology_normalization", "mathematical_context_translation",
        "equivalence_similarity", "contextual_theory_gluing", "contradiction_diagnosis",
        "gap_discovery", "experiment_query_selection", "synthesis", "review", "saturation_stopping",
    }
    assert required_surfaces <= set(metrics["process_surfaces_invoked"])
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1, "OPERATOR": 0, "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0, "RELATION": 1, "PATH": 0, "META_METHOD": 0,
    }
    assert set(metrics["saturation_axes"]) >= {
        "retrieval_novelty", "tool_output_novelty", "counterexample_pressure",
        "decomposition_yield", "expert_review_novelty", "method_novelty", "transfer_novelty",
    }
    assert metrics["gates"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gates"]["candidate_generated"] is False
    assert metrics["gates"]["same_context_review_independent"] is False
