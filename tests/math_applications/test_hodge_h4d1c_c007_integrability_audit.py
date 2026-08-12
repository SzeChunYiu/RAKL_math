import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"


def canonical_episode_hash(doc: dict) -> str:
    payload = {k: v for k, v in doc.items() if k != "artifact_hash"}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def test_c007_task_episode_is_content_bound_shadow() -> None:
    p = BASE / "07_memory/H4d1c_C007_TASK_EPISODE_SHADOW_20260812.json"
    doc = json.loads(p.read_text())
    required = {
        "episode_id", "task_id", "atom_id", "context_hash", "problem_signature",
        "fibre_snapshot_hash", "operator_ids", "action_trace", "observation_ids",
        "verification_ids", "outcome", "residual_signature", "evidence_pointers",
        "artifact_hash", "timestamp", "cost", "storage_admission",
    }
    assert set(doc) == required
    assert doc["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert doc["outcome"] == "PARTIAL_SUCCESS"
    assert doc["artifact_hash"] == canonical_episode_hash(doc)


def test_c007_cusp_falsifier_has_zero_linear_constraint() -> None:
    # f(x,y)=y^2-x^3.  Its gradient vanishes at the cusp origin, so the
    # Zariski tangent space there is the full ambient C^2; the inclusion's
    # tangent map is therefore surjective although the image remains the cusp.
    def grad_f(x: int, y: int) -> tuple[int, int]:
        return (-3 * x * x, 2 * y)

    assert grad_f(0, 0) == (0, 0)


def test_c007_keeps_local_and_gluing_failures_separate() -> None:
    diagnosis = json.loads((BASE / "07_memory/H4d1c_C007_DIAGNOSIS_20260812.json").read_text())
    assert diagnosis["local_mathematical_failure"].startswith("YES:")
    assert diagnosis["local_to_global_gluing_failure"].startswith("SEPARATE:")
    route = (BASE / "03_routes/H4d1c_C007_TANGENT_SURJECTIVITY_INTEGRABILITY_AUDIT_20260812.md").read_text()
    assert "A^1_C -> P^1_C" in route
    assert "O-H4D1C-SMOOTH-SOURCE-OR-DIRECT-IMAGE-CERTIFICATE" in route


def test_c007_framework_and_root_bindings_are_frozen() -> None:
    ctx = json.loads((BASE / "01_frontier/H4d1c_C007_PREACTION_CONTEXT_20260812.json").read_text())
    fw = json.loads((BASE / "01_frontier/H4d1c_C007_FRAMEWORK_SUBJECT_FREEZE_20260812.json").read_text())
    root = json.loads((BASE / "01_frontier/H4d1c_C007_ROOT_PRESERVATION_20260812.json").read_text())
    expected = "bd6b0e3edeb2b94b3f31b17e111c7a278f461f96"
    assert ctx["framework"]["live_main_sha"] == expected
    assert fw["frozen_rakl_main_sha"] == expected
    assert root["root_issue"] == 6
    assert "rational Hodge" in root["root_claim_scope"]
