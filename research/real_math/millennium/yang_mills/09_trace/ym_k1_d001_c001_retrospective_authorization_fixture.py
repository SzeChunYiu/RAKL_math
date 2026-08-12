from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
AUTHORIZATION_BASE_SHA = "0c556fc68cbf4b4d25555437ba4fc26b8128c858"
EVALUATOR_IDENTITY_MERGE_SHA = "ff21299ae77dde937e00c5739de3c526a30736d5"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
CANDIDATE_ID = "YM-S1a2i-K1-D001-C001-TWO-STAGE-SOURCE-BRIDGE"
EVALUATOR = "research/real_math/millennium/yang_mills/05_oracles/ym_k1_d001_c001_two_stage_evaluator.py"
FREEZE = "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_D001_C001_EVALUATOR_IDENTITY_FREEZE_20260812.json"
OUTPUT = ROOT / "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_C001_RETROSPECTIVE_REPRODUCTION_AUTHORIZATION_20260812.json"


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical(value)).hexdigest()


def binding(path: str, application_commit: str) -> dict[str, Any]:
    raw = (ROOT / path).read_bytes()
    blob = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", f"{application_commit}:{path}"],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    return {
        "path": path,
        "application_commit": application_commit,
        "git_blob": blob,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
    }


def build_document() -> dict[str, Any]:
    evaluator_binding = binding(EVALUATOR, EVALUATOR_IDENTITY_MERGE_SHA)
    freeze_binding = binding(FREEZE, EVALUATOR_IDENTITY_MERGE_SHA)
    freeze = json.loads((ROOT / FREEZE).read_text())
    document = {
        "schema_version": "1.0.0",
        "record_type": "YM_K1_D001_C001_RETROSPECTIVE_REPRODUCTION_AUTHORIZATION",
        "authorization_id": "YM-S1a2i-K1-D001-C001-RETROSPECTIVE-REPRODUCTION-AUTHORIZATION-20260812",
        "candidate_id": CANDIDATE_ID,
        "authorization_base_sha": AUTHORIZATION_BASE_SHA,
        "evaluator_identity_merge_sha": EVALUATOR_IDENTITY_MERGE_SHA,
        "framework_sha": FRAMEWORK_SHA,
        "evaluator_binding": evaluator_binding,
        "freeze_binding": freeze_binding,
        "identity_checks": {
            "evaluator_raw_sha256_matches_freeze": evaluator_binding["raw_sha256"] == freeze["evaluator_identity"]["raw_sha256"],
            "evaluator_id": freeze["evaluator_identity"]["evaluator_id"],
            "candidate_id_matches_freeze": freeze["candidate_id"] == CANDIDATE_ID,
            "all_planted_worlds_matched_at_freeze": freeze["all_planted_worlds_match"],
            "direct_stage_b_disproof_route_complete": freeze["candidate_branch_completeness_receipt"]["complete"],
        },
        "authorized_only_after_this_authorization_is_merged": {
            "rerun_exact_frozen_evaluator_bytes": True,
            "reproduce_stage_a_source_passage_audit": True,
            "reproduce_stage_a_branch_classification": True,
            "record_seven_field_mathematical_lesson": True,
            "record_prior_local_non_strict_generation_as_negative_chronology_history": True,
        },
        "mandatory_labels": {
            "run_type": "RETROSPECTIVE_REPRODUCTION_NOT_PROSPECTIVE_DISCOVERY",
            "strict_rakl_discovery_chronology": False,
            "reason": "The bound source result was accessed in local commit 25c0271d before evaluator bytes were publicly frozen.",
        },
        "stage_order": [
            "Reproduce Stage A only from the already-bound public source and exact frozen evaluator bytes.",
            "If Stage A is CANNOT_CHECK or STRONGER_PREMISE_MISMATCH_A, do not enter Stage B.",
            "No Stage-B reproduction is authorized in this round even if Stage A unexpectedly passes.",
        ],
        "current_round_state": {
            "retrospective_source_reproduction_executed": False,
            "target_result_recorded": False,
            "stage_b_entered": False,
            "g_star_selected": False,
        },
        "explicitly_unauthorized": [
            "CLAIMING_STRICT_RAKL_DISCOVERY_CHRONOLOGY",
            "CLAIMING_PROSPECTIVE_OR_UNTOUCHED_RESULT",
            "CHANGING_EVALUATOR_BYTES_OR_CANDIDATE_IDENTITY",
            "ENTERING_STAGE_B",
            "SELECTING_G_STAR",
            "INVENTING_OR_NUMERICALLY_ASSIGNING_SOURCE_CONSTANTS",
            "CLAIMING_INDEPENDENT_PEER_REVIEW",
            "CLAIMING_FULL_STABLE_MANIFOLD_CONTINUUM_OS_OR_MASS_GAP_AUTHORITY",
        ],
        "authority": {
            "licenses_future_retrospective_reproduction_after_merge": True,
            "grants_current_mathematical_result_credit": False,
            "grants_strict_discovery_authority": False,
            "grants_target_truth": False,
            "grants_proof_authority": False,
            "grants_independent_review": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
        "allowed_next_action": "Merge this authorization without target execution; only then publish a separately labeled retrospective Stage-A reproduction.",
        "artifact_hash": "",
    }
    document["artifact_hash"] = sha(document)
    return document


def write_document() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(build_document(), indent=2, sort_keys=True, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_document()
