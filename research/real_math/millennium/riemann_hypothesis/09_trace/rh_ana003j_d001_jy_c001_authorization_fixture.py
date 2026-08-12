#!/usr/bin/env python3
"""Freeze post-merge authorization for the JY C001 evaluator successor.

This round creates authorization only.  The authorization is inert until its
own commit is merged into active main.  No evaluator is implemented, imported,
or executed here and no validation result is accessed or classified.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
AUTHORIZATION_BASE_SHA = "e14c0708861fe04a0cfad4116e1e9b003e6702ff"
CANDIDATE_ID = "RH-ANA-003j-D001-JY-C001-DIRECT-ENVELOPE"
FROZEN_AT = "2026-08-12T15:20:00Z"

BASE = "research/real_math/millennium/riemann_hypothesis"
PATHS = {
    "authorization": f"{BASE}/09_trace/RH_ANA_003j_D001_JY_C001_EVALUATION_AUTHORIZATION_20260812.json",
}
BOUND = {
    "candidate": {
        "path": f"{BASE}/04_candidates/RH_ANA_003j_D001_JY_C001_DIRECT_ENVELOPE_CANDIDATE_FREEZE_20260812.json",
        "raw_sha256": "ba83993220dd2b587330bbee7000f7e50c7a7fad3ee50c0c7051b9f1a7b7a885",
        "artifact_hash": "sha256:e079308e6d89d6ed028f31843e1f230b5d5bb3636b6a5099f1a679363a31a84b",
        "candidate_core_sha256": "sha256:082bc762b994bce8348da1ea99933fe14c965f9dff98296b6e9177cd94b974be",
    },
    "falsifier": {
        "path": f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_FALSIFIER_FREEZE_20260812.json",
        "raw_sha256": "7e59f54cbde76bd3b1149ff7b03e6c101c6ee63146a71f13c5d271d773d629bb",
        "artifact_hash": "sha256:dcc3611449e8f651fea29983504dcbdb04de72744c5b6192c675cdede853e9bd",
    },
    "public_validation_inputs": {
        "path": f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_PUBLIC_VALIDATION_INPUTS_20260812.json",
        "raw_sha256": "fd0f8f73abf53b54a004ec8ff8bfb9da1592b92cf625cad7c01a31f077b6d7a4",
        "artifact_hash": "sha256:42b2450184a6e819a9373d61346be1cf33b7da5007d9d45b5c8f55ba971fbc01",
    },
    "candidate_trace": {
        "path": f"{BASE}/09_trace/RH_ANA_003j_D001_JY_C001_CANDIDATE_FREEZE_TRACE_20260812.json",
        "raw_sha256": "041b7aad863591ae23abc09fdc119ab8fed46577a85e48a45ff0e7021b87b13c",
        "last_event_hash": "sha256:f60403d63d5282cc94aaff1ebed2a86acabb0a94825a5549b0688006eadbab56",
    },
}


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def canonical_hash(value: dict) -> str:
    subject = copy.deepcopy(value)
    subject["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(canonical(subject)).hexdigest()


def raw_sha256(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def checked_bindings() -> dict[str, dict]:
    bindings = copy.deepcopy(BOUND)
    for name, binding in bindings.items():
        observed = raw_sha256(binding["path"])
        if observed != binding["raw_sha256"]:
            raise RuntimeError(
                f"{name} raw identity mismatch: {observed} != {binding['raw_sha256']}"
            )
        document = json.loads((ROOT / binding["path"]).read_text(encoding="utf-8"))
        if "artifact_hash" in binding and document["artifact_hash"] != binding["artifact_hash"]:
            raise RuntimeError(f"{name} artifact hash mismatch")
        if "candidate_core_sha256" in binding:
            if document["candidate_identity"]["canonical_core_sha256"] != binding["candidate_core_sha256"]:
                raise RuntimeError("candidate core identity mismatch")
        if "last_event_hash" in binding:
            if document["entries"][-1]["artifact_hash"] != binding["last_event_hash"]:
                raise RuntimeError("candidate trace tip mismatch")
    return bindings


def authorization_document() -> dict:
    value = {
        "artifact_hash": "",
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_C001_POSTMERGE_EVALUATION_AUTHORIZATION",
        "authorization_id": "RH-ANA-003j-D001-JY-C001-EVALUATION-AUTHORIZATION-20260812",
        "candidate_id": CANDIDATE_ID,
        "frozen_at_utc": FROZEN_AT,
        "status": "FROZEN_INERT_UNTIL_AUTHORIZATION_MERGED_INTO_ACTIVE_MAIN",
        "chronology": {
            "authorization_base_sha": AUTHORIZATION_BASE_SHA,
            "candidate_freeze_pr": "https://github.com/SzeChunYiu/RAKL_math/pull/404",
            "candidate_freeze_merge_sha": AUTHORIZATION_BASE_SHA,
            "candidate_and_falsifier_public_before_authorization": True,
            "authorization_commit_sha": None,
            "authorization_merge_sha": None,
            "authorization_present_on_active_main": False,
            "evaluator_implemented_before_authorization_freeze": False,
            "evaluator_executed_before_authorization_freeze": False,
            "result_accessed_before_authorization_freeze": False,
        },
        "exact_identity_bindings": checked_bindings(),
        "current_round": {
            "allowed_action": "COMMIT_AND_MERGE_THIS_AUTHORIZATION_ONLY",
            "evaluator_implementation_authorized": False,
            "evaluator_import_or_execution_authorized": False,
            "validation_result_classification_authorized": False,
        },
        "post_merge_successor_authorization": {
            "activation_condition": "A successor must prove that the exact raw bytes of this authorization are committed on active main and bind that active-main merge SHA before implementing or executing the evaluator.",
            "authorized_actions_after_activation": [
                "Implement an evaluator bound to the exact candidate core, candidate artifact, falsifier artifact, and public-input artifact identities above.",
                "Classify only the frozen planted PASS, FAIL, and CANNOT_CHECK worlds.",
                "Run only the twelve public symbolic inputs n in {1,2,3,5} at U_JY(n), ceil(U_JY(n)), and ceil(U_JY(n))+1.",
                "Check the frozen coefficient ledger, exact substitution identity, component nonnegativity, componentwise monotonicity obligations, and endpoint-extension logic.",
                "Emit a receipt that preserves per-obligation PASS, FAIL, or CANNOT_CHECK without averaging or threshold rescue.",
            ],
            "planned_evaluator_path": f"{BASE}/05_oracles/rh_ana003j_d001_jy_c001_evaluator.py",
            "planned_result_path": f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_PUBLIC_VALIDATION_RESULT_20260812.json",
            "scope_expansion_allowed": False,
            "candidate_or_falsifier_mutation_allowed": False,
        },
        "forbidden_even_after_activation": [
            "calculate or publish any numerical B_JY value",
            "calculate or publish any m_JY or M_JY value",
            "run numerical incomplete-gamma validation before a separate precision contract is publicly frozen",
            "run a numerical natural-order remainder test",
            "select epsilon_n",
            "select a diagonal cutoff constant C",
            "attempt a moving-diagonal or internal-prefix conclusion",
            "change the candidate, planted worlds, expected classifications, or public input set",
            "claim a mathematical result, proof, novelty, independent review, Li positivity, or RH",
        ],
        "result_firewall": {
            "evaluator_path_exists": False,
            "evaluator_implemented": False,
            "evaluator_imported": False,
            "evaluator_executed": False,
            "validation_receipt_exists": False,
            "B_JY_values": [],
            "m_JY_values": [],
            "M_JY_values": [],
            "epsilon_sequence_identity": None,
            "diagonal_cutoff_constant_identity": None,
            "result_state": "NOT_EVALUATED",
        },
        "authority": {
            "operational_authorization_only": True,
            "candidate_truth": False,
            "mathematical_result": False,
            "proof": False,
            "novelty": False,
            "independent_review": False,
            "li_positivity": False,
            "riemann_hypothesis": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "software_or_governance_credit_units": 0,
        },
    }
    value["artifact_hash"] = canonical_hash(value)
    return value


def build_all() -> dict[str, dict]:
    return {PATHS["authorization"]: authorization_document()}


def main() -> None:
    for relative, value in build_all().items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
