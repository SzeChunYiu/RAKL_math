import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRE = ROOT / "research/real_math/millennium/hodge/deformation/09_trace/H4d1d0_PRE_ACTION_PACKET_20260811.json"
RESULT = ROOT / "research/real_math/millennium/hodge/deformation/07_memory/H4d1d0_RESULT_EPISODE_DIAGNOSIS_LESSON_20260811.json"
CORRECTION = ROOT / "research/real_math/millennium/hodge/deformation/09_trace/H4d1d0_HASH_CORRECTION_20260811.json"


def _canon_hash(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(payload).hexdigest()


def _strip(value, key):
    out = copy.deepcopy(value)
    out.pop(key)
    return out


def _pointer_set(doc, pointer, value):
    parts = [p for p in pointer.split("/") if p]
    cur = doc
    for part in parts[:-1]:
        cur = cur[part]
    cur[parts[-1]] = value


def test_h4d1d0_pre_action_v3_hashes_and_chronology():
    data = json.loads(PRE.read_text(encoding="utf-8"))

    context = data["context_fiber"]
    assert context["packet_hash"] == "sha256:" + _canon_hash(_strip(context, "packet_hash"))

    fibre = data["problem_fibre_snapshot"]
    assert fibre["snapshot_hash"] == "sha256:" + _canon_hash(_strip(fibre, "snapshot_hash"))

    memory = data["research_memory_review"]
    assert memory["artifact_hash"] == "sha256:" + _canon_hash(_strip(memory, "artifact_hash"))
    assert memory["missed_prior_experience"]["value"] == "CANNOT_MEASURE"
    assert memory["preference_changed"] is True

    expert = data["expert_context_review"]
    assert expert["artifact_hash"] == "sha256:" + _canon_hash(_strip(expert, "artifact_hash"))
    assert expert["synthesis"]["independent_review"] is False

    trace = data["pre_candidate_trace"]
    previous = None
    required = [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert [event["event_type"] for event in trace["events"]] == required
    for event in trace["events"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == "sha256:" + _canon_hash(_strip(event, "artifact_hash"))
        previous = event["artifact_hash"]
    assert trace["final_event_hash"] == previous
    assert trace["artifact_hash"] == "sha256:" + _canon_hash(_strip(trace, "artifact_hash"))

    receipt = data["pre_action_fibre_receipt"]
    assert receipt["framework_commit"] == "812e9cf18345ef430f0a4cc3ff78f93d7f18ed22"
    assert receipt["application_commit"] == "dc83b72201cb58844b2bdc76117e4dcb9190211d"
    assert set(receipt["allowed_outcome_branches"]) == {"SUCCESS", "PARTIAL_SUCCESS", "FAILURE", "BLOCKED", "UNKNOWN"}
    assert receipt["receipt_canonical_sha256"] == _canon_hash(_strip(receipt, "receipt_canonical_sha256"))

    assert data["packet_hash"] == "sha256:" + _canon_hash(_strip(data, "packet_hash"))


def test_h4d1d0_result_episode_and_correction_overlay():
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    correction = json.loads(CORRECTION.read_text(encoding="utf-8"))

    assert result["task_episode"]["artifact_hash"] == "sha256:" + _canon_hash(_strip(result["task_episode"], "artifact_hash"))
    assert result["task_episode"]["outcome"] == "PARTIAL_SUCCESS"
    assert result["result"]["novelty_class"] == "representation"
    assert result["result"]["novel_structure_rank"] == 0
    assert result["result"]["local_vs_gluing"]["root_failure"]

    corrected = copy.deepcopy(result)
    for item in correction["replacements"]:
        parts = [p for p in item["json_pointer"].split("/") if p]
        cur = result
        for part in parts:
            cur = cur[part]
        assert cur == item["incorrect"]
        _pointer_set(corrected, item["json_pointer"], item["correct"])

    for key in ("result", "diagnosis", "failure_experience", "lesson", "successor_obstruction"):
        assert corrected[key]["artifact_hash"] == "sha256:" + _canon_hash(_strip(corrected[key], "artifact_hash"))

    assert corrected["packet_hash"] == correction["corrected_packet_hash_after_replacements"]
    assert corrected["packet_hash"] == "sha256:" + _canon_hash(_strip(corrected, "packet_hash"))
    assert correction["tooling_failure"]["failure_id"] == "F-H4D1D0-MANUAL-HASH-COPY-MISMATCH"


def test_h4d1d0_authority_and_component_scope_guards():
    pre = json.loads(PRE.read_text(encoding="utf-8"))
    result = json.loads(RESULT.read_text(encoding="utf-8"))

    assert "NO_ROOT_AUTHORITY" in pre["authority"]
    assert "ROOT_AUTHORITY_NONE" in result["result"]["authority"]
    assert result["successor_obstruction"]["authority"] == "OPEN_PROPOSAL_RESIDUAL_ONLY"
    assert "selected" in result["result"]["selected_component_falsifier"]["claim"].lower()
    assert "some exact witness component" in result["result"]["class_level_equivalence"]["B"]
    assert result["episode_diagnosis_lesson_separation_asserted"] is True
