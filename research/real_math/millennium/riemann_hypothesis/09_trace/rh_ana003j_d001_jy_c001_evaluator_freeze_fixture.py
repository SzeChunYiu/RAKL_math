#!/usr/bin/env python3
"""Freeze the exact JY C001 evaluator bytes without importing or executing it."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE_SHA = "ee36bd9bb629d7d07461322dca32bbce614e2e81"
CANDIDATE_ID = "RH-ANA-003j-D001-JY-C001-DIRECT-ENVELOPE"
BASE = "research/real_math/millennium/riemann_hypothesis"
EVALUATOR = f"{BASE}/05_oracles/rh_ana003j_d001_jy_c001_evaluator.py"
AUTHORIZATION = f"{BASE}/09_trace/RH_ANA_003j_D001_JY_C001_EVALUATION_AUTHORIZATION_20260812.json"
REQUIREMENTS = "requirements-test.txt"
EVALUATOR_RAW_SHA256 = "55c73c2975924683ed537d394af75475022a6703a7a63c9d3a7c46bfeac31267"
AUTHORIZATION_RAW_SHA256 = "99a224ceca4ecced628fd998f0ec2306744b79b283110d7b6d7a767ab8cee4c0"
REQUIREMENTS_RAW_SHA256 = "2fd4159c5094a92d7d31b611c275eee49908132b015d8ce3e940ce49829dba22"
PATH = f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_EVALUATOR_IDENTITY_FREEZE_20260812.json"


def raw_hash(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def canonical_hash(value: dict) -> str:
    subject = copy.deepcopy(value)
    subject["artifact_hash"] = ""
    raw = json.dumps(subject, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def build() -> dict:
    for path, expected in (
        (EVALUATOR, EVALUATOR_RAW_SHA256),
        (AUTHORIZATION, AUTHORIZATION_RAW_SHA256),
        (REQUIREMENTS, REQUIREMENTS_RAW_SHA256),
    ):
        observed = raw_hash(path)
        if observed != expected:
            raise RuntimeError(f"identity mismatch: {path}: {observed} != {expected}")
    value = {
        "artifact_hash": "",
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003J_D001_JY_C001_EVALUATOR_IDENTITY_FREEZE",
        "freeze_id": "RH-ANA-003j-D001-JY-C001-EVALUATOR-FREEZE-20260812",
        "candidate_id": CANDIDATE_ID,
        "status": "FROZEN_NOT_IMPORTED_NOT_EXECUTED",
        "frozen_at_utc": "2026-08-12T15:30:00Z",
        "chronology": {
            "base_sha": BASE_SHA,
            "base_is_merged_authorization": True,
            "evaluator_implemented_after_authorization": True,
            "evaluator_imported_or_executed": False,
            "result_accessed": False,
            "next_step": "MERGE_IDENTITY_FREEZE_THEN_FREEZE_UPDATED_EXECUTION_AUTHORIZATION",
        },
        "evaluator_identity": {
            "path": EVALUATOR,
            "raw_sha256": EVALUATOR_RAW_SHA256,
            "language": "Python 3",
            "entrypoint": "run_validation(root=ROOT)",
            "dependency_contract": {
                "path": REQUIREMENTS,
                "raw_sha256": REQUIREMENTS_RAW_SHA256,
                "mpmath": ">=1.3,<2",
            },
        },
        "precision_contract": {
            "decimal_digits": 100,
            "relative_tolerance": "1e-70",
            "corroboration_method": "direct mpmath quadrature in original s variable versus independent upper-incomplete-gamma evaluation",
            "scope": "The exact twelve public symbolic u constructors and j=0,...,n-1 only.",
            "authority": "NUMERICAL_CORROBORATION_ONLY_NOT_PROOF",
        },
        "frozen_behavior": [
            "Verify exact raw identities of candidate, falsifier, public inputs, and merged authorization before evaluation.",
            "Derive h and q coefficient identities with exact Fraction arithmetic for n in {1,2,3,5}.",
            "Evaluate only the preregistered twelve public symbolic u constructors.",
            "Corroborate only the frozen incomplete-gamma integral identity at 100 decimal digits and 1e-70 relative tolerance.",
            "Check structural nonnegativity, the frozen U_JY domain, planted classifications, and endpoint-extension derivation.",
            "Return no numerical B_JY, m_JY, M_JY, natural-order remainder, epsilon_n, or diagonal cutoff value.",
        ],
        "bound_authorization": {
            "path": AUTHORIZATION,
            "raw_sha256": AUTHORIZATION_RAW_SHA256,
            "artifact_hash": "sha256:afc7c85be7a2d9f61d5f356256708b2d4ac70074b52fe8843306e003179058cf",
            "note": "The earlier authorization named the path but did not bind these bytes. Therefore this freeze cannot execute; a later authorization must bind this exact evaluator raw SHA-256.",
        },
        "current_round_firewall": {
            "execution_authorized": False,
            "evaluator_imported": False,
            "evaluator_executed": False,
            "result_classified": False,
            "receipt_created": False,
        },
        "authority": {
            "evaluator_identity_only": True,
            "mathematical_result": False,
            "proof": False,
            "novelty": False,
            "independent_review": False,
            "li_or_rh_authority": False,
            "software_or_governance_credit_units": 0,
        },
    }
    value["artifact_hash"] = canonical_hash(value)
    return value


def main() -> None:
    path = ROOT / PATH
    path.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
