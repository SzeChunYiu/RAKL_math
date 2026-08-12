"""Inert record checker for the frozen C047 orientation-feasibility lemma.

This file contains no decoder, satisfiability solver, target enumerator, or
proof search.  Import/execution before a separate post-public-freeze
authorization is forbidden by the candidate packet.
"""
from __future__ import annotations


REQUIRED_AUTHORIZATION = "C047-ORIENTATION-PROOF-CHECK-AUTHORIZED-AFTER-PUBLIC-FREEZE"
REQUIRED_OBLIGATIONS = (
    "DEFINE_ORIENTATION_ONLY_FAMILIES",
    "EXHAUSTIVE_ROW_SUPPORT_TRICHOTOMY",
    "DECODER_BRANCH_TO_FRESH_ROW_FORMS",
    "BINARY_HEADER_DISJOINTNESS",
    "MIRROR_AND_TWO_SIDED_CONCLUSION",
)


def evaluate_certificate(certificate: dict, authorization: dict) -> dict:
    if authorization.get("token") != REQUIRED_AUTHORIZATION:
        return {"verdict": "CANNOT_CHECK", "reason": "SEPARATE_POST_FREEZE_AUTHORIZATION_REQUIRED"}
    if authorization.get("candidate_id") != "C047-ORIENTATION-ONLY-SEPARATION-LEMMA-v1":
        return {"verdict": "CANNOT_CHECK", "reason": "CANDIDATE_ID_MISMATCH"}
    statuses = {
        item.get("obligation_id"): item.get("status")
        for item in certificate.get("obligations", [])
        if isinstance(item, dict)
    }
    for obligation in REQUIRED_OBLIGATIONS:
        status = statuses.get(obligation)
        if status == "REFUTED":
            return {"verdict": "FAIL", "falsified_obligation": obligation}
        if status != "PROVED":
            return {"verdict": "CANNOT_CHECK", "missing_obligation": obligation}
    return {"verdict": "PASS", "candidate_id": authorization["candidate_id"]}

