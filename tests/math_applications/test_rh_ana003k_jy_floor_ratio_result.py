from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"
EVALUATOR = BASE / "05_oracles/rh_ana003k_jy_c001_floor_ratio_evaluator.py"
ACTIVATION = BASE / "09_trace/RH_ANA_003k_JY_C001_FLOOR_RATIO_EXECUTION_ACTIVATION_20260812.json"


def evaluator():
    spec = importlib.util.spec_from_file_location("rh_ana003k_jy_c001_evaluator", EVALUATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_hash(value: dict) -> str:
    value = dict(value)
    value.pop("artifact_hash", None)
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_execution_activation_follows_merged_freeze_and_binds_exact_evaluator() -> None:
    activation = json.loads(ACTIVATION.read_text())
    assert activation["artifact_hash"] == canonical_hash(activation)
    assert activation["chronology"]["application_main_at_activation"] == "04d8ca7af5c007d3d5f93dd9f47b411a07e95822"
    assert activation["chronology"]["candidate_public_merge"] == "cde7c63769f35230be158f5525239287f51bfb09"
    assert activation["chronology"]["result_accessed"] is False
    assert all(binding["matches"] for binding in activation["verified_frozen_bindings"].values())
    assert activation["evaluator_implementation"]["raw_sha256"] == "sha256:" + hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    assert activation["authority"]["software_credit_units"] == 0


def test_record_checker_fails_closed_without_written_proof() -> None:
    module = evaluator()
    candidate, falsifier, checks = module.load_frozen_inputs(ROOT)
    observed = module.evaluate_rh_ana003k_jy_c001(
        candidate,
        falsifier,
        {"raw_identity_bindings_valid": all(checks.values())},
    )
    assert observed == "CANNOT_CHECK"

