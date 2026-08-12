#!/usr/bin/env python3
"""Freeze exact post-merge execution authorization for JY C001."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE_SHA = "6425952ad6e7a079adad0a68e93b90fe8b8f9a47"
CANDIDATE_ID = "RH-ANA-003j-D001-JY-C001-DIRECT-ENVELOPE"
BASE = "research/real_math/millennium/riemann_hypothesis"
PATH = f"{BASE}/09_trace/RH_ANA_003j_D001_JY_C001_EXECUTION_AUTHORIZATION_20260812.json"
BOUND = {
    "candidate": (f"{BASE}/04_candidates/RH_ANA_003j_D001_JY_C001_DIRECT_ENVELOPE_CANDIDATE_FREEZE_20260812.json", "ba83993220dd2b587330bbee7000f7e50c7a7fad3ee50c0c7051b9f1a7b7a885"),
    "falsifier": (f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_FALSIFIER_FREEZE_20260812.json", "7e59f54cbde76bd3b1149ff7b03e6c101c6ee63146a71f13c5d271d773d629bb"),
    "public_inputs": (f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_PUBLIC_VALIDATION_INPUTS_20260812.json", "fd0f8f73abf53b54a004ec8ff8bfb9da1592b92cf625cad7c01a31f077b6d7a4"),
    "prior_authorization": (f"{BASE}/09_trace/RH_ANA_003j_D001_JY_C001_EVALUATION_AUTHORIZATION_20260812.json", "99a224ceca4ecced628fd998f0ec2306744b79b283110d7b6d7a767ab8cee4c0"),
    "evaluator_identity": (f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_EVALUATOR_IDENTITY_FREEZE_20260812.json", "93cc82fa7f03effd3be2f589932d95752fedf763bc765074e683d028d5287799"),
    "evaluator": (f"{BASE}/05_oracles/rh_ana003j_d001_jy_c001_evaluator.py", "55c73c2975924683ed537d394af75475022a6703a7a63c9d3a7c46bfeac31267"),
    "dependency_contract": ("requirements-test.txt", "2fd4159c5094a92d7d31b611c275eee49908132b015d8ce3e940ce49829dba22"),
}


def raw_hash(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def canonical_hash(value: dict) -> str:
    subject = copy.deepcopy(value)
    subject["artifact_hash"] = ""
    raw = json.dumps(subject, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def bindings() -> dict:
    result = {}
    for name, (path, expected) in BOUND.items():
        observed = raw_hash(path)
        if observed != expected:
            raise RuntimeError(f"{name} identity mismatch: {observed} != {expected}")
        result[name] = {"path": path, "raw_sha256": observed}
    result["evaluator_identity"]["artifact_hash"] = "sha256:da6fead2da96c2fd570aeb432d19904f601e9659f3000555083f748ae0775524"
    return result


def build() -> dict:
    value = {
        "artifact_hash": "",
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_C001_EXACT_EXECUTION_AUTHORIZATION",
        "authorization_id": "RH-ANA-003j-D001-JY-C001-EXACT-EXECUTION-AUTHORIZATION-20260812",
        "candidate_id": CANDIDATE_ID,
        "status": "FROZEN_INERT_UNTIL_THIS_AUTHORIZATION_IS_MERGED_TO_ACTIVE_MAIN",
        "frozen_at_utc": "2026-08-12T15:40:00Z",
        "chronology": {
            "base_sha": BASE_SHA,
            "base_is_evaluator_identity_merge": True,
            "authorization_commit_sha": None,
            "authorization_merge_sha": None,
            "present_on_active_main": False,
            "evaluator_imported_or_executed": False,
            "result_accessed": False,
        },
        "exact_bindings": bindings(),
        "current_round": {
            "allowed_action": "COMMIT_AND_MERGE_AUTHORIZATION_ONLY",
            "evaluator_import_or_execution_authorized": False,
            "result_classification_authorized": False,
        },
        "post_merge_authorization": {
            "activation_condition": "A successor result round must bind this authorization raw SHA-256 and its exact active-main merge SHA before importing or executing the evaluator.",
            "evaluator_import_and_execution_authorized": True,
            "fixed_public_validation_authorized": True,
            "planted_world_validation_authorized": True,
            "symbolic_derivation_receipt_authorized": True,
            "high_precision_corroboration_authorized": True,
            "materialize_exact_computable_symbolic_M_algorithm_authorized": True,
            "allowed_evaluator_raw_sha256": "55c73c2975924683ed537d394af75475022a6703a7a63c9d3a7c46bfeac31267",
            "precision_dps": 100,
            "relative_tolerance": "1e-70",
        },
        "result_requirements": [
            "Separate the exact substitution proof from direct-quadrature-versus-gammainc numerical corroboration.",
            "Prove coefficient identities exactly and monotonicity only on u>=U_JY(n), retaining +1.515.",
            "Handle integer endpoints with Y*=Y+1/2 and the direction B(log Y*)<=B(log Y).",
            "Explain strict remainder <epsilon from the frozen B<=epsilon/2 definition and all-real threshold.",
            "Materialize the exact computable least-integer-search algorithm for m_JY and M_JY without evaluating any numerical M value.",
            "Record a seven-field mathematical lesson; Git, CI, schemas, hashes, and serialization receive zero mathematical lesson credit.",
        ],
        "forbidden": [
            "numerical B_JY, m_JY, or M_JY values",
            "numerical natural-order remainder tests",
            "epsilon_n selection",
            "diagonal cutoff C selection",
            "moving-diagonal or internal-prefix comparison",
            "candidate/falsifier/public-input mutation",
            "novelty, independent-review, Li-positivity, or RH claim",
        ],
        "authority": {
            "operational_authorization_only": True,
            "mathematical_result": False,
            "proof": False,
            "mathematical_lesson": False,
            "software_or_governance_credit_units": 0,
        },
    }
    value["artifact_hash"] = canonical_hash(value)
    return value


def main() -> None:
    (ROOT / PATH).write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
