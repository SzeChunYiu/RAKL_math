from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from math import ceil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "real_math" / "millennium" / "p_vs_np"
C041_PATH = BASE / "04_candidates" / "C041_fx_sat_one_sided.py"


def load_c041():
    spec = importlib.util.spec_from_file_location("pnp_c041_support_spectrum_calibration", C041_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def half_length_formula(w: int, m: int) -> int:
    return 3 + w + m.bit_length() + ceil(3 * m * (w + 1) / 2)


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def test_half_length_formula_matches_frozen_encoder_on_bounded_valid_formulas() -> None:
    # Calibration only. The cycle packet contains the hand derivation and converse proof.
    c041 = load_c041()
    clause = ((1, False), (1, False), (1, False))
    for v in range(1, 33):
        w = v.bit_length()
        for m in range(1, 9):
            formula = c041.Formula3CNF(v, tuple(clause for _ in range(m)), "CALIBRATION")
            encoded = c041.encode_formula(formula)
            assert len(encoded) // 2 == half_length_formula(w, m)


def test_fixed_w_successive_support_gap_is_at_least_three_on_bounded_range() -> None:
    # Finite regression mirrors but does not replace the exact parity proof.
    for w in range(1, 17):
        values = [half_length_formula(w, m) for m in range(1, 65)]
        assert min(b - a for a, b in zip(values, values[1:])) >= 3


def test_first_post14_syntax_supported_consecutive_pair_calibration() -> None:
    assert half_length_formula(1, 3) == 15
    assert half_length_formula(2, 2) == 16
    assert half_length_formula(4, 1) == 16


def test_shadow_task_episode_hash_matches_current_v3_content_contract() -> None:
    path = BASE / "09_trace" / "O9d12a2a1b_C050_SUPPORT_SPECTRUM_RV_TASK_EPISODE_20260812.json"
    container = json.loads(path.read_text())
    assert "episode_id" not in container
    assert container["inventory_disposition"] == "NESTED_TASK_EPISODE_NOT_TOP_LEVEL_INVENTORY_OBJECT"
    assert container["chronology_status"] == "RETROSPECTIVE_ONLY"
    episode = container["task_episode"]
    payload = {
        "episode_id": episode["episode_id"],
        "task_id": episode["task_id"],
        "atom_id": episode["atom_id"],
        "context_hash": episode["context_hash"],
        "problem_signature": episode["problem_signature"],
        "fibre_snapshot_hash": episode["fibre_snapshot_hash"],
        "operator_ids": episode["operator_ids"],
        "action_trace": episode["action_trace"],
        "observation_ids": episode["observation_ids"],
        "verification_ids": episode["verification_ids"],
        "outcome": episode["outcome"],
        "residual_signature": episode["residual_signature"],
        "evidence_pointers": episode["evidence_pointers"],
        "timestamp": episode["timestamp"],
        "cost": episode["cost"],
        "storage_admission": episode["storage_admission"],
    }
    assert hashlib.sha256(canonical_bytes(payload)).hexdigest() == episode["artifact_hash"]
    assert episode["artifact_hash"] == "67f6d9938bf4908880f5497b84f8041cbbb7c4f2ffd606922d0cebdcd0348064"
    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"


def test_shadow_trace_hash_chain_and_zero_protected_novelty() -> None:
    trace_path = BASE / "09_trace" / "O9d12a2a1b_C050_SUPPORT_SPECTRUM_RV_TRACE_20260812.json"
    trace = json.loads(trace_path.read_text())
    previous = "GENESIS"
    for index, event in enumerate(trace["events"]):
        assert event["index"] == index
        assert event["previous_event_hash"] == previous
        payload = {key: value for key, value in event.items() if key != "event_hash"}
        assert hashlib.sha256(canonical_bytes(payload)).hexdigest() == event["event_hash"]
        previous = event["event_hash"]
    assert trace["last_event_hash"] == previous
    assert previous == "88bc6b2dac9a55083a88c7ab88d70f98f10a430d0c3b2a041d983f6631997128"

    packet_path = BASE / "10_case_study" / "C050_SUPPORT_SPECTRUM_RV_VERIFIED_DISCOVERY_CYCLE_20260812.json"
    packet = json.loads(packet_path.read_text())
    metrics = packet["RAKL_CYCLE_METRICS"]
    assert metrics["retained_semantic_novelty_protected"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
    }
    assert packet["application_subject"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert packet["chronology"]["status"] == "RETROSPECTIVE_ONLY"
