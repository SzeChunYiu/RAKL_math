"""Assurance checks for the pre-output C042 structural gate freeze."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
GATE_PATH = PNP / "05_falsification/c042_activation_quotient_gate.py"
FREEZE_PATH = PNP / "09_trace/O9d12a2a1b_C042_GATE_FREEZE_20260812.json"


def _load_gate():
    spec = importlib.util.spec_from_file_location("c042_activation_freeze", GATE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_length_formula_is_frozen_without_running_the_native_gate() -> None:
    gate = _load_gate()
    assert gate.canonical_even_length(1, 1) == 16
    assert gate.canonical_even_length(1, 2) == 24
    assert gate.canonical_even_length(2, 1) == 22
    assert gate.canonical_even_length(3, 1) == 22


def test_freeze_binds_statement_evaluator_predictions_and_unknown_outputs() -> None:
    freeze = json.loads(FREEZE_PATH.read_text(encoding="utf-8"))
    assert freeze["candidate_id"] == "C042-ACTIVATION-QUOTIENT-GATE-v1"
    assert freeze["evaluator"]["sha256"] == hashlib.sha256(
        GATE_PATH.read_bytes()
    ).hexdigest()
    statement = PNP / "04_candidates/C042_ACTIVATION_THRESHOLD_FREEZE_20260812.md"
    assert freeze["statement"]["sha256"] == hashlib.sha256(
        statement.read_bytes()
    ).hexdigest()
    assert freeze["predictions"]["U9_quotient_full_cover_number"] == "UNKNOWN"
    assert freeze["predictions"]["U13_quotient_full_cover_number"] == "UNKNOWN"
    assert freeze["chronology"]["executable_output_accessed"] is False
    assert freeze["artifact_hash"] == _canonical_hash(freeze)
