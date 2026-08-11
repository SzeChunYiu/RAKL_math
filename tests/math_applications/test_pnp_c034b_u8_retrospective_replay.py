from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
SOURCE = PNP / "00_sources/RAKL_PVSNP_C034_C040_EXTERNAL_LEDGER_20260811.md"
REPLAY = PNP / "05_falsification/c034b_u8_retrospective_replay.py"
RECEIPT = PNP / "05_falsification/C034B_U8_RETROSPECTIVE_REPLAY_RECEIPT_20260811.json"
SCHEMA = ROOT / "schemas/pnp-c034b-u8-retrospective-replay.schema.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def _module():
    spec = importlib.util.spec_from_file_location("c034b_u8_replay", REPLAY)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_u8_receipt_is_schema_valid_self_hashed_and_deterministic() -> None:
    module = _module()
    observed = module.build_receipt()
    assert observed == _load(RECEIPT)
    schema = _load(SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(observed)
    assert observed["artifact_hash"] == _hash(observed)
    assert observed["source_binding"]["source_sha256"] == "sha256:" + hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert observed["evaluator_contract"]["implementation_sha256"] == "sha256:" + hashlib.sha256(REPLAY.read_bytes()).hexdigest()


def test_pass_world_establishes_only_reconstructed_finite_lp_equality() -> None:
    receipt = _load(RECEIPT)
    world = receipt["validation_worlds"]["pass"]
    assert world["verdict"] == "PASS"
    assert world["complement_edge_count"] == 8
    assert world["relevant_generator_pair_count"] == 12
    assert world["full_union_pair_count"] == 3025
    assert world["primal_support_count"] == 17
    assert world["dual_support_count"] == 20
    assert Fraction(world["primal_total"]) == Fraction(49, 24)
    assert Fraction(world["dual_total"]) == Fraction(49, 24)
    assert world["minimum_scaled_primal_coverage"] == 24
    assert world["maximum_scaled_dual_load"] == 24
    assert all(value >= 24 for value in world["generator_separation_lower_bounds"])
    assert receipt["source_binding"]["certificate_support_difference"] == {
        "ledger_reported_primal_support": 21,
        "ledger_reported_dual_support": 24,
        "regenerated_primal_support": 17,
        "regenerated_dual_support": 20,
        "interpretation": "DIFFERENT_MATCHING_CERTIFICATE_REPRESENTATION_NOT_ORIGINAL_CERTIFICATE_RECOVERY",
    }
    assert receipt["claim_update"]["original_missing_bundle_verdict"] == "CANNOT_CHECK_MISSING_CERTIFICATE_AND_RECEIPT"
    assert all(receipt["authority_contract"][field] is False for field in receipt["authority_contract"])


def test_planted_fail_and_structural_cannot_check_worlds_fail_closed() -> None:
    module = _module()
    planted = module.verify_world(module.planted_fail_world())
    assert planted["verdict"] == "FAIL"
    assert planted["minimum_scaled_primal_coverage"] < 24
    assert planted["falsifier"] == "PLANTED_PRIMAL_WEIGHT_REDUCTION_DETECTED"

    structural = module.verify_world(module.structural_cannot_check_world())
    assert structural == {
        "verdict": "CANNOT_CHECK",
        "reason": "MISSING_AMBIENT_BIPARTITION",
    }


def test_zero_star_padding_is_executably_evaluator_invariant() -> None:
    module = _module()
    baseline = module.pass_world()
    padded = module.zero_star_padding_world()
    assert baseline["generator_pairs"] == padded["generator_pairs"]
    result = module.verify_world(padded)
    assert result["verdict"] == "PASS"
    assert result["exact_optimum"] == "49/24"
    assert result["full_union_pair_count"] == 3025
    assert _load(RECEIPT)["validation_worlds"]["zero_star_padding_invariance"] == result


def test_hostile_certificate_mutations_do_not_pass() -> None:
    module = _module()
    for mutation in (module.mutate_primal_weight, module.mutate_dual_weight, module.drop_generator_pair):
        result = module.verify_world(mutation(module.pass_world()))
        assert result["verdict"] != "PASS"
