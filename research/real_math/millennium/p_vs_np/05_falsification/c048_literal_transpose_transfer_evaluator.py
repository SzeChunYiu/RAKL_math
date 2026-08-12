"""Inert record checker for the frozen C048 transfer lemma.

It has no decoder, SAT solver, enumeration, graph materializer, or target-result
capability. It checks only that a later public certificate records all frozen
mathematical obligations and the narrow authorization binds this candidate.
"""
from __future__ import annotations

REQUIRED = (
    "RELATION_COMPLEMENT_TRANSPOSE_IDENTITY",
    "BOTH_ENDPOINTS_AND_REDUCTION_MAP_SWAP",
    "SUFFIX_ROW_PROJECTION_CHARACTERIZATION",
    "EXACT_COLLISION_IFF_OVERLAP_LANGUAGE",
    "COLLISION_AND_REDUCTION_ARE_INDEPENDENT_NECESSARY_CONDITIONS",
)
CANDIDATE_ID = "C048-LITERAL-TRANSPOSE-TRANSFER-CONDITION-v1"


def evaluate_certificate(certificate: dict, authorization: dict) -> dict:
    if authorization.get("candidate_id") != CANDIDATE_ID:
        return {"verdict": "FAIL", "reason": "candidate mismatch"}
    if authorization.get("proof_check_authorized") is not True:
        return {"verdict": "FAIL", "reason": "not authorized"}
    if certificate.get("candidate_id") != CANDIDATE_ID:
        return {"verdict": "FAIL", "reason": "certificate mismatch"}
    rows = certificate.get("obligations", [])
    by_id = {row.get("obligation_id"): row for row in rows}
    if tuple(row.get("obligation_id") for row in rows) != REQUIRED:
        return {"verdict": "FAIL", "reason": "obligation order or set changed"}
    if not all(by_id[item].get("status") == "PROVED" and by_id[item].get("evidence_pointer") for item in REQUIRED):
        return {"verdict": "FAIL", "reason": "missing proved record"}
    return {"verdict": "PASS", "candidate_id": CANDIDATE_ID}
