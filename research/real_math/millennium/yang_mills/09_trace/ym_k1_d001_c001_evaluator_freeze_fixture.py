from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
PARENT_MAIN_SHA = "6d191b91d2201e28ba2a505dad7b5a9515e54605"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
CANDIDATE_ID = "YM-S1a2i-K1-D001-C001-TWO-STAGE-SOURCE-BRIDGE"
EVALUATOR = ROOT / "research/real_math/millennium/yang_mills/05_oracles/ym_k1_d001_c001_two_stage_evaluator.py"
OUTPUT = ROOT / "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_D001_C001_EVALUATOR_IDENTITY_FREEZE_20260812.json"


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical(value)).hexdigest()


def module():
    spec = importlib.util.spec_from_file_location("ym_k1_d001_c001_two_stage_evaluator", EVALUATOR)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def planted_world_receipt() -> list[dict[str, Any]]:
    m = module()
    worlds = [
        ("WORLD-A-B-PASS-SEPARATE-CONSTANTS-EXACT-MARGIN", m.EvaluationWorld(m.StageADerivation.SEPARATE_CONSTANTS, True, True, m.StageBProof.EXACT_INTERVAL_MARGIN), "APPLICABLE_BRIDGE"),
        ("WORLD-A-FAIL-CONFLATED-C-TRAP", m.EvaluationWorld(m.StageADerivation.CONFLATED_SOURCE_CONSTANT, False, False, m.StageBProof.NOT_ENTERED), "STRONGER_PREMISE_MISMATCH_A"),
        ("WORLD-B-FAIL-FACTOR-TWO-TRAP", m.EvaluationWorld(m.StageADerivation.SEPARATE_CONSTANTS, True, True, m.StageBProof.FACTOR_TWO_ONLY), "FLOW_MARGIN_FAIL_B"),
        ("WORLD-CANNOT-CHECK-UPSTREAM-CONSTANTS", m.EvaluationWorld(m.StageADerivation.INSUFFICIENT, None, False, m.StageBProof.NOT_ENTERED), "CANNOT_CHECK"),
    ]
    return [
        {
            "world_id": world_id,
            "expected_branch": expected,
            "observed_branch": m.evaluate(world).branch.value,
            "match": m.evaluate(world).branch.value == expected,
        }
        for world_id, world, expected in worlds
    ]


def build_document() -> dict[str, Any]:
    worlds = planted_world_receipt()
    document = {
        "schema_version": "1.0.0",
        "record_type": "YM_K1_D001_C001_EVALUATOR_IDENTITY_FREEZE",
        "freeze_id": "YM-S1a2i-K1-D001-C001-EVALUATOR-IDENTITY-FREEZE-20260812",
        "candidate_id": CANDIDATE_ID,
        "parent_main_sha": PARENT_MAIN_SHA,
        "framework_sha": FRAMEWORK_SHA,
        "evaluator_identity": {
            "evaluator_id": "YM-S1a2i-K1-D001-C001-TWO-STAGE-EVALUATOR-v1",
            "path": str(EVALUATOR.relative_to(ROOT)),
            "raw_sha256": hashlib.sha256(EVALUATOR.read_bytes()).hexdigest(),
            "frozen_contract": [
                "Stage A routes INSUFFICIENT to CANNOT_CHECK.",
                "Stage A routes literal conflated C_dom=C_force=C with 0<rho<1 to STRONGER_PREMISE_MISMATCH_A.",
                "Stage A routes separately derived incompatible constants to STRONGER_PREMISE_MISMATCH_A.",
                "Stage B cannot enter without a Stage-A pass and a separately frozen positive g_star.",
                "Stage B rejects a factor-two-only argument as FLOW_MARGIN_FAIL_B.",
                "APPLICABLE_BRIDGE requires Stage-A compatibility and exact full-interval Stage-B predicates.",
            ],
        },
        "planted_world_receipt": worlds,
        "all_planted_worlds_match": all(row["match"] for row in worlds),
        "chronology_boundary": {
            "evaluator_was_specified_by_pr405_and_authorized_for_implementation_by_pr407": True,
            "evaluator_bytes_publicly_frozen_before_any_future_authorized_execution": True,
            "prior_local_unpublished_result_commit": "25c0271d6a0f379cad4dab3c2a4be56d732f5a00",
            "prior_local_result_access_preceded_public_evaluator_byte_freeze": True,
            "strict_rakl_discovery_chronology_for_prior_generation": False,
            "future_reproduction_must_be_labeled_retrospective_not_prospective_discovery": True,
        },
        "current_round_state": {
            "source_audit_executed": False,
            "target_stage_a_evaluated": False,
            "target_stage_b_evaluated": False,
            "g_star_selected": False,
            "target_result_recorded": False,
        },
        "authority": {
            "evaluator_identity_frozen": True,
            "licenses_target_execution": False,
            "grants_mathematical_result_credit": False,
            "grants_target_truth": False,
            "grants_proof_authority": False,
            "grants_independent_review": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
        "allowed_next_action": "Merge evaluator identity without target evaluation; then freeze a separate retrospective-reproduction authorization bound to these bytes.",
        "artifact_hash": "",
    }
    document["artifact_hash"] = sha(document)
    return document


def write_document() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(build_document(), indent=2, sort_keys=True, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_document()
