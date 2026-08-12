import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"
PACKET = BASE / "10_case_study/YM-S1a2j_RAKL_V3_CASE_STUDY_METRICS_TASK_EPISODE_20260812_R21.json"
TRACE = BASE / "09_trace/YM-S1a2j_RESEARCH_TRACE_20260812_R21.json"
CANDIDATE = BASE / "04_candidates/YM-S1a2j_C001_INFINITE_VOLUME_OS_ONE_STEP_TRANSFER_20260812_R21.md"
FIBRE = BASE / "01_frontier/YM-S1a2j_PRE_ACTION_FIBRE_20260812_R21.json"

AXES = {
    "KNOWLEDGE",
    "OPERATOR",
    "EXPERIENCE_PATTERN",
    "OBSTRUCTION",
    "RELATION",
    "PATH",
    "META_METHOD",
}


def _load(path: Path):
    return json.loads(path.read_text())


def test_r21_packet_is_shadow_only_and_root_not_promoted():
    packet = _load(PACKET)
    assert packet["authority"] == "PROPOSAL_SHADOW_MEASUREMENT_ONLY"
    metrics = packet["RAKL_CYCLE_METRICS"]
    assert metrics["RAKL"]["method_version"] == "3.0.0"
    assert metrics["RAKL"]["main_sha"] == "b0a5820dc607b0ef711d5aa1fc6d2bbcec39d311"
    assert metrics["gate_provenance_ci"]["root_promotion"] == "DENIED / NOT_ATTEMPTED"
    assert metrics["gate_provenance_ci"]["protected_authority_transition"] == "NONE"
    assert packet["TaskEpisode"]["authority"] == "PROPOSAL_SHADOW_MEASUREMENT_ONLY"


def test_r21_all_seven_novelty_axes_are_explicit_and_protected_zero():
    metrics = _load(PACKET)["RAKL_CYCLE_METRICS"]
    novelty = metrics["retained_semantic_novelty"]
    proposal = novelty["proposal_shadow_authority_inert"]
    protected = novelty["protected_authoritative"]
    assert set(proposal) == AXES
    assert set(protected) == AXES
    assert all(v == 0 for v in protected.values())
    assert set(metrics["saturation_axes"]) == AXES


def test_r21_required_current_method_surfaces_and_memory_receipt_present():
    metrics = _load(PACKET)["RAKL_CYCLE_METRICS"]
    surfaces = set(metrics["canonical_method_specs_process_surfaces_invoked"])
    for required in {
        "decomposition",
        "routing",
        "search_query_generation",
        "source_selection_reliability",
        "claim_extraction",
        "mathematical_context_translation",
        "contextual_theory_gluing",
        "contradiction_diagnosis",
        "gap_discovery",
        "memory",
        "review",
        "authority_promotion",
        "saturation_stopping",
        "prompting_context_policy",
    }:
        assert required in surfaces
    memory = metrics["memory"]
    assert memory["retrieved_or_consulted_count"] == len(memory["retrieved_or_consulted_ids"])
    assert memory["selected_count"] == len(memory["selected_ids"])
    assert memory["rejected_count"] == len(memory["rejected_ids"])
    assert metrics["rakl_changed_action_relative_to_pre_memory_pre_gate_preference"]["changed"] is True


def test_r21_fibre_hash_correction_is_explicit_not_silently_rewritten():
    packet = _load(PACKET)
    metrics = packet["RAKL_CYCLE_METRICS"]
    measured = metrics["atom_fibre"]["fibre_snapshot_hash"]
    invalid = metrics["atom_fibre"]["invalid_original_internal_hash"]
    assert measured == "sha256:07607acbbec64b99ec8f4f10e366d2e8c61dae4faa10b9e31bf65a0313a52249"
    assert invalid == "sha256:6ea7945825f1ed2a75bb8d3fda3b5f03c88ccc8a07662fd68b6cf85682986f96"
    assert measured != invalid
    frozen = _load(FIBRE)
    assert "6ea794" in frozen["fibre_snapshot_hash"]
    assert "MF-YM-S1a2j-R21-FIBRE-HASH-PLACEHOLDER" in metrics["new_ids"]["failure_ids"]


def test_r21_trace_hash_chain_replays():
    trace = _load(TRACE)
    prev = ""
    for event in trace["events"]:
        assert event["previous_event_hash"] == prev
        payload = {
            "event_id": event["event_id"],
            "ordinal": event["ordinal"],
            "event_type": event["event_type"],
            "output": event["output"],
            "previous_event_hash": event["previous_event_hash"],
        }
        digest = hashlib.sha256(
            json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        ).hexdigest()
        assert event["event_hash"] == f"sha256:{digest}"
        prev = event["event_hash"]
    assert trace["trace_final_hash"] == prev


def test_r21_candidate_proves_only_fixed_cutoff_positive_transfer_composition():
    text = CANDIDATE.read_text()
    assert "bounded nonnegative log-convex sequence" in text
    assert "Adjacent link RP makes this nonnegative" in text
    assert "same-theory positive self-adjoint one-step transfer contraction" in text
    assert "does **not** prove strict positivity/injectivity" in text
    assert "no lattice-spacing-uniform physical lower bound" in text
    assert "Independent review credit remains `0/3`" in text
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in text


def test_r21_outcome_and_residual_keep_continuum_open():
    metrics = _load(PACKET)["RAKL_CYCLE_METRICS"]
    assert "LOCAL_SUCCESS" in metrics["outcome"]
    assert "CONTINUUM_OPEN" in metrics["outcome"]
    assert "A-UNIFORM-RG-CONTINUUM-UNBOUND" in metrics["residual_after"]
    assert metrics["resource_proxies"]["independent_mathematical_reviews"] == 0
