import hashlib
import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"
CONTEXT_CORRECTION = (
    NS
    / "10_case_study/NS-B1a3b1_R2_CONTEXT_HASH_ASSURANCE_CORRECTION_V2_20260811.json"
)


def _load(rel):
    return json.loads((NS / rel).read_text())


def _canonical_hash(obj, excluded):
    payload = {k: v for k, v in obj.items() if k not in excluded}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def test_context_memory_fibre_and_episode_hashes():
    correction = json.loads(CONTEXT_CORRECTION.read_text())
    assert correction["artifact_hash"] == "sha256:" + _canonical_hash(
        correction, {"artifact_hash"}
    )
    assert correction["correction_class"] == (
        "RETROSPECTIVE_ASSURANCE_ONLY_NO_RETROACTIVE_CONTEXT_FREEZE"
    )

    binding = correction["source_version_binding"]
    context_path = ROOT / binding["path"]
    context_raw = context_path.read_bytes()
    assert len(context_raw) == binding["size_bytes"]
    assert "sha256:" + hashlib.sha256(context_raw).hexdigest() == binding["raw_sha256"]
    assert _git("rev-parse", f'{binding["introduced_commit"]}:{binding["path"]}') == (
        binding["git_blob_sha"]
    )
    assert _git("hash-object", str(context_path)) == binding["git_blob_sha"]

    related = {item["role"]: item for item in correction["related_hash_audit"]}
    assert set(related) == {
        "context_packet",
        "memory_review",
        "fibre_snapshot",
        "task_episode_shadow",
    }
    for item in related.values():
        subject_raw = (ROOT / item["path"]).read_bytes()
        assert "sha256:" + hashlib.sha256(subject_raw).hexdigest() == item["raw_sha256"]

    # The R2 context is historical negative assurance evidence: its committed
    # bytes are preserved, while the stale stored hash is explicitly rejected.
    ctx = json.loads(context_raw)
    context_recomputed = "sha256:" + _canonical_hash(ctx, {"packet_hash"})
    assert related["context_packet"]["stored_hash"] == ctx["packet_hash"]
    assert related["context_packet"]["recomputed_remove_key_hash"] == context_recomputed
    assert related["context_packet"]["status"] == "MISMATCH_PRESERVED"
    assert ctx["packet_hash"] != context_recomputed
    disposition = correction["historical_context_disposition"]
    assert disposition["stored_packet_hash"] == ctx["packet_hash"]
    assert disposition["recomputed_packet_hash"] == context_recomputed
    assert disposition["stored_equals_recomputed"] is False
    assert disposition["strict_pre_candidate_gate_status"] == (
        "INVALID_NO_RETROACTIVE_REPAIR"
    )

    mem = _load("07_memory/NS-B1a3b1_RESEARCH_MEMORY_REVIEW_R2_20260811.json")
    mem_recomputed = "sha256:" + _canonical_hash(mem, {"artifact_hash"})
    assert mem["artifact_hash"] == mem_recomputed
    assert related["memory_review"]["stored_hash"] == mem["artifact_hash"]
    assert related["memory_review"]["recomputed_remove_key_hash"] == mem_recomputed
    assert related["memory_review"]["status"] == "MATCH"

    fibre = _load("09_trace/NS-B1a3b1_FIBRE_SNAPSHOT_R2_20260811.json")
    fibre_recomputed = "sha256:" + _canonical_hash(fibre, {"fibre_snapshot_hash"})
    assert fibre["fibre_snapshot_hash"] == fibre_recomputed
    assert related["fibre_snapshot"]["stored_hash"] == fibre["fibre_snapshot_hash"]
    assert related["fibre_snapshot"]["recomputed_remove_key_hash"] == fibre_recomputed
    assert related["fibre_snapshot"]["status"] == "MATCH"

    ep = _load("10_case_study/NS-B1a3b1_C001_R2_V3_TASK_EPISODE_20260811.json.shadow")
    episode_recomputed = _canonical_hash(ep, {"artifact_hash"})
    assert ep["artifact_hash"] == episode_recomputed
    assert related["task_episode_shadow"]["stored_hash"] == ep["artifact_hash"]
    assert related["task_episode_shadow"]["recomputed_remove_key_hash"] == episode_recomputed
    assert related["task_episode_shadow"]["status"] == "MATCH"
    assert ep["outcome"] == "PARTIAL_SUCCESS"
    assert correction["epistemic_status"]["mathematical_authority"] == "NONE"
    assert correction["epistemic_status"]["root_status"] == (
        "OPEN_NO_SOLUTION_CERTIFICATE"
    )


def test_hash_chained_traces_are_contiguous():
    pre = _load("09_trace/NS-B1a3b1_PRE_CANDIDATE_TRACE_R2_20260811.json")
    prev = None
    for event in pre["events"]:
        assert event["previous_event_hash"] == prev
        expected = "sha256:" + _canonical_hash(event, {"artifact_hash"})
        assert event["artifact_hash"] == expected
        prev = event["artifact_hash"]
    assert pre["final_hash"] == prev

    post = _load("09_trace/NS-B1a3b1_RESULT_TRACE_CONTINUATION_R2_20260811.json")
    assert post["continues_from"] == pre["final_hash"]
    prev = pre["final_hash"]
    for event in post["events"]:
        assert event["previous_event_hash"] == prev
        expected = "sha256:" + _canonical_hash(event, {"artifact_hash"})
        assert event["artifact_hash"] == expected
        prev = event["artifact_hash"]
    assert post["final_hash"] == prev


def test_log_bmo_zoom_weight_is_nonexpansive_for_zoom_in():
    for r in (1.0, 0.5, 0.1, 1e-6):
        for rho in (0.49, 0.25, 0.01, 1e-8):
            assert 0 < r * rho < 0.5
            ratio = abs(math.log(rho)) / abs(math.log(r * rho))
            assert ratio <= 1.0 + 1e-15


def test_metrics_do_not_promote_root_and_count_all_axes():
    metrics = _load("10_case_study/NS-B1a3b1_C001_R2_RAKL_CYCLE_METRICS_20260811.json")
    novelty = metrics["saturation_retained_semantic_novelty"]
    assert set(novelty) == {
        "KNOWLEDGE", "OPERATOR", "EXPERIENCE_PATTERN", "OBSTRUCTION",
        "RELATION", "PATH", "META_METHOD"
    }
    assert metrics["outcome"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["root_promotion_gate"] == "BLOCKED"
    assert metrics["raw_repository_growth_counted_as_learning"] is False
