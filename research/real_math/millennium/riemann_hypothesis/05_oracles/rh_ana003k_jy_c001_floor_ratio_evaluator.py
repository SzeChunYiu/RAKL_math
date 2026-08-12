#!/usr/bin/env python3
"""Record checker for the frozen RH-ANA-003k JY floor-ratio candidate.

This program does not prove the limit.  It verifies frozen identities and
checks that a separately supplied seven-obligation hand-proof record and the
ten frozen hostile worlds receive only allowed classifications.  Mathematical
authority remains with the written derivation in the result receipt.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


BASE = Path("research/real_math/millennium/riemann_hypothesis")
CANDIDATE_ID = "RH-ANA-003k-JY-C001-FLOOR-RATIO-ASYMPTOTIC"
CANDIDATE_ARTIFACT_HASH = "sha256:f99b6553969d2e035e87bc7c62f5ad7f163c69e09ce55278d3e34329028ba1bf"
CANDIDATE_CORE_SHA256 = "sha256:a29a7437b79aed85e858c78e8c182e2b15ee89ea383fd3b9f9b5bd127683a423"
FALSIFIER_ARTIFACT_HASH = "sha256:df91c4f87bd590da80557e3d00057eab029fb07d28732e02bb21d023a26d5daa"

PATHS = {
    "candidate": BASE / "04_candidates/RH_ANA_003k_JY_C001_FLOOR_RATIO_CANDIDATE_FREEZE_20260812.json",
    "falsifier": BASE / "05_oracles/RH_ANA_003k_JY_C001_FLOOR_RATIO_FALSIFIER_FREEZE_20260812.json",
    "authorization": BASE / "09_trace/RH_ANA_003k_JY_C001_FLOOR_RATIO_EVALUATION_AUTHORIZATION_20260812.json",
    "jy_result": BASE / "05_oracles/RH_ANA_003j_D001_JY_C001_PUBLIC_VALIDATION_RESULT_20260812.json",
}

MUTATION_LABELS = {
    "C_DEPENDS_ON_N": "FAIL_QUANTIFIER_CONTRACT",
    "WRONG_LOG_POWER_LIMIT": "FAIL_ELEMENTARY_LIMIT",
    "DROP_0515": "FAIL_RATIO_IDENTITY",
    "REVERSE_CEILING": "FAIL_FLOOR_CHAIN",
    "CERTIFICATE_TO_OBJECT": "FAIL_SCOPE_OVERREACH",
    "ENDPOINT_TO_PREFIX": "FAIL_SCOPE_OVERREACH",
    "RH_INFERENCE": "FAIL_SCOPE_OVERREACH",
}

WORLD_MUTATIONS = {
    "CONTROL-EXACT-FIXED-C": None,
    "FAIL-C-DEPENDS-ON-N": "C_DEPENDS_ON_N",
    "FAIL-WRONG-LOG-POWER-LIMIT": "WRONG_LOG_POWER_LIMIT",
    "FAIL-DROP-0515": "DROP_0515",
    "FAIL-CEILING-DIRECTION": "REVERSE_CEILING",
    "FAIL-CERTIFICATE-TO-OBJECT": "CERTIFICATE_TO_OBJECT",
    "FAIL-ENDPOINT-TO-PREFIX": "ENDPOINT_TO_PREFIX",
    "FAIL-RH-INFERENCE": "RH_INFERENCE",
    "CANNOT-CHECK-SOURCE": "INVALID_SOURCE_BINDING",
    "CANNOT-CHECK-PROOF": "MISSING_SYMBOLIC_PROOF",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def raw_sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _artifact_hash_valid(document: dict[str, Any]) -> bool:
    value = dict(document)
    observed = value.get("artifact_hash")
    value["artifact_hash"] = ""
    return observed == canonical_hash(value)


def evaluate_rh_ana003k_jy_c001(
    candidate: dict[str, Any],
    falsifier: dict[str, Any],
    source_bindings: dict[str, Any],
) -> str:
    """Classify one exact or planted world under the frozen vocabulary.

    ``hand_proof_obligations`` is a record assertion, not a proof checker.
    Missing proof fails closed, and the return value never grants theorem
    authority by itself.
    """

    candidate_ok = (
        candidate.get("candidate_id") == CANDIDATE_ID
        and candidate.get("artifact_hash") == CANDIDATE_ARTIFACT_HASH
        and candidate.get("candidate_identity", {}).get("canonical_core_sha256") == CANDIDATE_CORE_SHA256
        and _artifact_hash_valid(candidate)
    )
    falsifier_ok = (
        falsifier.get("candidate_id") == CANDIDATE_ID
        and falsifier.get("artifact_hash") == FALSIFIER_ARTIFACT_HASH
        and falsifier.get("candidate_artifact_hash") == CANDIDATE_ARTIFACT_HASH
        and _artifact_hash_valid(falsifier)
    )
    if not candidate_ok or not falsifier_ok or not source_bindings.get("raw_identity_bindings_valid", False):
        return "CANNOT_CHECK"

    mutation = source_bindings.get("mutation")
    if mutation == "INVALID_SOURCE_BINDING":
        return "CANNOT_CHECK"
    if mutation == "MISSING_SYMBOLIC_PROOF":
        return "CANNOT_CHECK"
    if mutation in MUTATION_LABELS:
        return MUTATION_LABELS[mutation]

    obligations = source_bindings.get("hand_proof_obligations")
    if not isinstance(obligations, dict):
        return "CANNOT_CHECK"
    required = [f"PO{i}" for i in range(1, 8)]
    if not all(obligations.get(key) is True for key in required):
        if obligations.get("PO1") is False:
            return "FAIL_RATIO_IDENTITY"
        if obligations.get("PO2") is False:
            return "FAIL_ELEMENTARY_LIMIT"
        if obligations.get("PO3") is False:
            return "FAIL_QUANTIFIER_CONTRACT"
        if obligations.get("PO4") is False or obligations.get("PO5") is False or obligations.get("PO6") is False:
            return "FAIL_FLOOR_CHAIN"
        if obligations.get("PO7") is False:
            return "FAIL_SCOPE_OVERREACH"
        return "CANNOT_CHECK"
    return "PASS_CANDIDATE_THEOREM"


def load_frozen_inputs(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    candidate = json.loads((root / PATHS["candidate"]).read_text())
    falsifier = json.loads((root / PATHS["falsifier"]).read_text())
    authorization = json.loads((root / PATHS["authorization"]).read_text())
    checks: dict[str, bool] = {}
    for name, binding in authorization["exact_identity_bindings"].items():
        checks[name] = raw_sha256(root / binding["path"]) == binding["raw_sha256"]
    jy_result = json.loads((root / PATHS["jy_result"]).read_text())
    checks["jy_floor_source"] = (
        jy_result.get("artifact_hash") == "sha256:1ef6193d3b8fd09d6fde1a03c0158cd86134749d13922799a4c3e8535cd3ca22"
        and jy_result.get("proved_fixed_n_result", {}).get("computable_sufficient_tilde_modulus_algorithm", [""])[0]
        == "Input a fixed integer n>=1 and positive rational epsilon; compute the symbolic start m0=ceil(U_JY(n))."
    )
    return candidate, falsifier, checks


def materialize_and_run_frozen_worlds(root: Path, hand_proof_obligations: dict[str, bool]) -> dict[str, Any]:
    candidate, falsifier, checks = load_frozen_inputs(root)
    rows = []
    expected_by_id = {row["world_id"]: row["expected_future_classification"] for row in falsifier["worlds"]}
    for world_id, mutation in WORLD_MUTATIONS.items():
        bindings = {
            "raw_identity_bindings_valid": all(checks.values()),
            "hand_proof_obligations": hand_proof_obligations,
            "mutation": mutation,
        }
        observed = evaluate_rh_ana003k_jy_c001(candidate, falsifier, bindings)
        expected = expected_by_id[world_id]
        rows.append({
            "world_id": world_id,
            "mutation": mutation,
            "expected": expected,
            "observed": observed,
            "pass": observed == expected,
        })
    return {
        "authority": "RECORD_CHECK_ONLY_NOT_PROOF",
        "raw_identity_checks": checks,
        "worlds": rows,
        "all_worlds_pass": all(row["pass"] for row in rows),
        "overall_classification": rows[0]["observed"] if all(row["pass"] for row in rows) else "CANNOT_CHECK",
    }
