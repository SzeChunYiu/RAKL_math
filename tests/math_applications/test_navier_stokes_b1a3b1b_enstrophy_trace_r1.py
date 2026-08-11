import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research/real_math/millennium/navier_stokes"


def canonical_sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def test_context_memory_fibre_hashes_and_nonpromotion():
    context = json.loads((NS / "01_frontier/NS-B1a3b1b_CONTEXT_FIBER_R1_20260811.json").read_text())
    packet_hash = context.pop("packet_hash")
    assert packet_hash == "sha256:" + canonical_sha(context)
    assert context["root_contract"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert context["root_contract"]["independent_mathematical_reviews"] == "0/3"
    assert context["framework"]["method_version"] == "3.0.0"

    memory = json.loads((NS / "07_memory/NS-B1a3b1b_RESEARCH_MEMORY_REVIEW_R1_20260811.json").read_text())
    artifact_hash = memory.pop("artifact_hash")
    assert artifact_hash == "sha256:" + canonical_sha(memory)
    assert memory["rakl_changed_observable_action_preference"] is True
    assert memory["missed_memory_audit"]["status"] == "CANNOT_MEASURE"

    fibre = json.loads((NS / "09_trace/NS-B1a3b1b_FIBRE_SNAPSHOT_R1_20260811.json").read_text())
    fibre_hash = fibre.pop("fibre_snapshot_hash")
    assert fibre_hash == "sha256:" + canonical_sha(fibre)
    assert "EP-NS-B1a3b1a-C001-R1-20260811" in fibre["selected_episode_ids"]


def test_pre_action_receipt_self_hash_and_pending_authority():
    receipt = json.loads((NS / "09_trace/NS-B1a3b1b_PRE_ACTION_RECEIPT_R1_20260811.json.shadow").read_text())
    digest = receipt.pop("receipt_canonical_sha256")
    assert digest == canonical_sha(receipt)
    pending = [x for x in receipt["selected_retrievals"] if x["authority"] == "PENDING"]
    assert [x["retrieval_id"] for x in pending] == ["EP-NS-B1a3b1a-C001-R1-20260811"]
    assert "y_a(t)=a(T-t)^(-1/2)" in receipt["predeclared_discriminator"]


def test_scalar_endpoint_profile_is_integrable_unbounded_and_ode_compatible():
    C0 = 1.0
    a = 1.0
    assert a * a >= 1.0 / (2.0 * C0)
    for s in (1.0, 0.25, 0.01, 1e-6):
        y = a / math.sqrt(s)
        dy_dt = a / (2.0 * s ** 1.5)
        assert dy_dt <= C0 * y ** 3 * (1.0 + 1e-12)
        assert math.isclose(math.sqrt(s) * y, a)
    eps = 1e-6
    assert 2.0 * a * math.sqrt(eps) < 1.0
    assert a / math.sqrt(1e-24) > 1e10


def test_episode_diagnosis_obstruction_lesson_are_distinct():
    episode = json.loads((NS / "10_case_study/NS-B1a3b1b_C001_R1_TASK_EPISODE_20260811.json.shadow").read_text())
    diagnosis = json.loads((NS / "07_memory/NS-B1a3b1b_C001_DIAGNOSIS_R1_20260811.json").read_text())
    obstruction = json.loads((NS / "07_memory/NS-B1a3b1b_C001_OBSTRUCTION_R1_20260811.json.shadow").read_text())
    lesson = json.loads((NS / "07_memory/NS-B1a3b1b_C001_LESSON_R1_20260811.json.shadow").read_text())
    assert episode["episode_id"] in diagnosis["supporting_episode_ids"]
    assert episode["episode_id"] in obstruction["supporting_episode_ids"]
    assert episode["episode_id"] in lesson["supporting_episode_ids"]
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert obstruction["authority"] == "OBSERVED_ONLY_PROPOSAL_SHADOW"
    assert lesson["authority"] == "CANDIDATE"


def test_metrics_has_all_seven_axes_and_raw_growth_excluded():
    metrics = json.loads((NS / "10_case_study/NS-B1a3b1b_C001_R1_RAKL_CYCLE_METRICS_20260811.json").read_text())
    axes = metrics["retained_semantic_novelty"]
    assert axes == {"KNOWLEDGE": 0, "OPERATOR": 0, "EXPERIENCE_PATTERN": 1, "OBSTRUCTION": 1, "RELATION": 1, "PATH": 1, "META_METHOD": 0}
    assert metrics["raw_repository_growth_counted_as_learning"] is False
    assert metrics["gate_status"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"
