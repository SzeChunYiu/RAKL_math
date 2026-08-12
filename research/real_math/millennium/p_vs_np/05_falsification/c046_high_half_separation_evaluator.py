"""Inert proof-obligation evaluator for the frozen C046 separation lemma.

This module has no target decoder, SAT solver, enumeration, network, or result
capability.  It consumes only a later, separately authorized proof certificate
whose fields discharge the four frozen mathematical obligations.
"""
from __future__ import annotations

REQUIRED_AUTHORIZATION = "C046-SEPARATION-PROOF-CHECK-AUTHORIZED-AFTER-PUBLIC-FREEZE"
REQUIRED_OBLIGATIONS = (
    "BASE_U3_ROW_PROJECTION",
    "INDUCTIVE_SUPPORT_QUADRANT_CONTAINMENT",
    "MAGIC_LEADING_BIT_PREFIX_CONTAINMENT",
    "DISJOINT_HALF_INTERVAL_CONCLUSION",
)


def evaluate_certificate(certificate: dict, authorization: dict) -> dict:
    if authorization.get("token") != REQUIRED_AUTHORIZATION:
        return {"verdict": "CANNOT_CHECK", "reason": "SEPARATE_POST_FREEZE_AUTHORIZATION_REQUIRED"}
    if authorization.get("candidate_id") != "C046-HIGH-HALF-SEPARATION-LEMMA-v1":
        return {"verdict": "CANNOT_CHECK", "reason": "CANDIDATE_IDENTITY_MISMATCH"}
    records = certificate.get("obligations")
    if not isinstance(records, list):
        return {"verdict": "CANNOT_CHECK", "reason": "OBLIGATION_RECORDS_MISSING"}
    by_id = {item.get("obligation_id"): item for item in records if isinstance(item, dict)}
    if set(by_id) != set(REQUIRED_OBLIGATIONS):
        return {"verdict": "CANNOT_CHECK", "reason": "OBLIGATION_SET_MISMATCH"}
    for obligation_id in REQUIRED_OBLIGATIONS:
        item = by_id[obligation_id]
        if item.get("status") not in {"PROVED", "REFUTED"} or not item.get("evidence_pointer"):
            return {"verdict": "CANNOT_CHECK", "reason": f"INCOMPLETE:{obligation_id}"}
        if item["status"] == "REFUTED":
            return {"verdict": "FAIL", "falsified_obligation": obligation_id}
    return {"verdict": "PASS", "candidate_id": authorization["candidate_id"]}
