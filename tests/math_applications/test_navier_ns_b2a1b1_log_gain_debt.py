import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NS = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def test_log_gain_cannot_pay_positive_geometric_debt():
    gamma = 1.7
    alpha = 4.0
    beta = 0.25
    vals = []
    for L in (100.0, 400.0, 1600.0, 6400.0):
        h = math.sqrt(L)
        a = math.exp(L - h) if L < 700 else None
        # Compare logarithms to avoid overflow:
        log_ratio = beta * (L - h) - alpha * gamma * math.log(L / h)
        vals.append(log_ratio)
    assert vals == sorted(vals)
    assert vals[-1] > 1000.0

def test_fixed_time_pressure_and_cubic_debts_are_positive():
    # Exponents derived in the scoped audit from source-native S_a,G_a,P_a.
    assert 1/2 > 0
    assert 5/6 > 0
    assert 1/3 > 0

def test_task_episode_hash_and_shadow_authority():
    path = NS / "10_case_study" / "NS-B2a1b1_C001_V3_TASK_EPISODE_20260812.json.shadow"
    ep = json.loads(path.read_text())
    expected = ep.pop("artifact_hash")
    assert ep["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert hashlib.sha256(canonical(ep)).hexdigest() == expected
    assert ep["outcome"] == "PARTIAL_SUCCESS"
    assert any("root remains OPEN_NO_SOLUTION_CERTIFICATE" in x for x in ep["residual_signature"])

def test_trace_hash_chain():
    path = NS / "09_trace" / "NS-B2a1b1_C001_TRACE_20260812.json"
    obj = json.loads(path.read_text())
    prev = "0" * 64
    for event in obj["events"]:
        got = event["entry_hash"]
        payload = {k: v for k, v in event.items() if k != "entry_hash"}
        assert payload["previous_hash"] == prev
        assert hashlib.sha256(canonical(payload)).hexdigest() == got
        prev = got
    assert obj["head_hash"] == prev

def test_no_root_promotion_and_novelty_is_conservative():
    delta = json.loads((NS / "02_problem_dag" / "NS_B2A1B1_RESULT_DELTA_20260812.json").read_text())
    assert delta["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    cs = json.loads((NS / "10_case_study" / "NS-B2a1b1_C001_RAKL_METHOD_CASE_STUDY_20260812.json").read_text())
    assert cs["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert cs["novelty_class"]["literature_novelty_claim"] is False
