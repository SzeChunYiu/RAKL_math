import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"
PRE = BSD / "01_frontier/BSD_A1a1_R13_PRE_CANDIDATE_PACKET_20260812.json"
SOURCE = BSD / "00_sources/BSD_A1a1_R13_KURIHARA_ORDER_SOURCE_AUDIT_20260812.json"
EPISODE = BSD / "07_memory/BSD_A1a1_R13_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"
DIAGNOSIS = BSD / "07_memory/BSD_A1a1_R13_DIAGNOSIS_SHADOW_20260812.json"
FAILURE = BSD / "07_memory/BSD_A1a1_R13_FAILURE_SHADOW_20260812.json"
PRE_TRACE = BSD / "09_trace/BSD_A1a1_R13_PRE_CANDIDATE_TRACE_20260812.json"
RESULT_TRACE = BSD / "09_trace/BSD_A1a1_R13_RESULT_TRACE_DELTA_20260812.json"


def load(path):
    return json.loads(path.read_text())


def canonical_hash(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def test_r13_root_stays_open_and_episode_is_shadow_only():
    pre, source, episode = load(PRE), load(SOURCE), load(EPISODE)
    assert pre["authority"] == "PROPOSAL_SHADOW_PRE_CANDIDATE_ONLY"
    assert source["authority"] == "PRIMARY_SOURCE_BOUND_SCOPED_AUDIT_NO_ROOT_AUTHORITY"
    assert source["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "PARTIAL_SUCCESS"


def test_r13_strict_v3_episode_hash_binds_current_shape():
    episode = load(EPISODE)
    expected_fields = {
        "episode_id", "task_id", "atom_id", "context_hash", "problem_signature",
        "fibre_snapshot_hash", "operator_ids", "action_trace", "observation_ids",
        "verification_ids", "outcome", "residual_signature", "evidence_pointers",
        "artifact_hash", "timestamp", "cost", "storage_admission",
    }
    assert set(episode) == expected_fields
    content = {key: value for key, value in episode.items() if key != "artifact_hash"}
    assert canonical_hash(content) == episode["artifact_hash"]


def test_r13_does_not_promote_conjecture_1_6_or_low_rank_case():
    source = load(SOURCE)
    claims = {claim["claim_id"]: claim for claim in source["claims"]}
    assert "conjecture" in claims["R13-KP-CONJ1.6-COMPLEX-DISCRETE-COMPARISON"]["statement"].lower()
    assert "analytic rank at most one" in claims["R13-KP-COR1.10-LOW-RANK-CONTROL"]["statement"]
    assert source["scoped_composition"]["status"] == "VALID_CONDITIONAL_COMPOSITION_PENDING_EXACT_WEIGHT2_COORDINATE_BINDING"
    assert "not_proved" in source["scoped_composition"]


def test_r13_residual_is_sharpened_not_closed():
    source = load(SOURCE)
    after = source["residual_sharpening"]["after"]
    assert "COMPLEX_RANK2_TO_TWO_PRIME_NONZERO_KURIHARA_WITNESS_OR_EQUIVALENT_GENERIC_SELMER_UPPER_BOUND_OPEN" in after
    assert "WEIGHT2_KURIHARA_SELMER_TO_ZHANG_R9_SAME_THEORY_COORDINATE_BINDING_OPEN" in after
    assert "EXACT_COMPLEX_RANK2_TO_TRANSVERSE_P_LOCALIZATION_NONZERO_OPEN" in after
    assert "MORDELL_WEIL_SHA_REGULATOR_TAMAGAWA_TORSION_PERIOD_COMPLEX_LEADING_TERM_GLUE_OPEN" in after


def test_r13_episode_diagnosis_failure_remain_distinct_and_linked():
    episode, diagnosis, failure = load(EPISODE), load(DIAGNOSIS), load(FAILURE)
    assert diagnosis["episode_id"] == episode["episode_id"]
    assert diagnosis["episode_is_not_diagnosis"] is True
    assert failure["episode_id"] == episode["episode_id"]
    assert failure["diagnosis_id"] == diagnosis["diagnosis_id"]
    assert failure["obstruction_promotion"] == "NOT_REQUESTED_NOT_AUTHORIZED"
    assert failure["lesson_promotion"] == "NONE"


def test_r13_local_theorem_failure_is_separate_from_root_gluing_failure():
    diagnosis = load(DIAGNOSIS)["diagnosis"]
    assert diagnosis["local_mathematical_status"] == "SUCCESS_SOURCE_THEOREMS_VALID_IN_SCOPE"
    assert diagnosis["not_local_mathematical_failure"] is True
    assert diagnosis["local_to_global_gluing_failure"] is True


def test_r13_hash_chained_trace_extends_merged_r11_not_open_r12():
    pre, result = load(PRE_TRACE), load(RESULT_TRACE)
    assert pre["base_last_event_hash"] == "sha256:223832df6a99f9e8c2dc117e479dcbfdbc66d9b063bfb3ac7910804c00f6bddc"
    assert pre["open_current_work_not_in_base_trace"] == "PR312_R12_OPEN_NOT_MERGED_AT_R13_FREEZE"
    first = pre["entries"][0]
    content = {key: value for key, value in first.items() if key != "artifact_hash"}
    assert "sha256:" + canonical_hash(content) == first["artifact_hash"]
    assert result["base_last_event_hash"] == pre["terminal_event_hash"]
    prior = result["base_last_event_hash"]
    for event in result["entries"]:
        assert event["previous_event_hash"] == prior
        content = {key: value for key, value in event.items() if key != "artifact_hash"}
        assert "sha256:" + canonical_hash(content) == event["artifact_hash"]
        prior = event["artifact_hash"]
    assert result["terminal_event_hash"] == prior
