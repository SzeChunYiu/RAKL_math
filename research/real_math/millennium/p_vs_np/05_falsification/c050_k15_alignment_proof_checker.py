"""Exact record checker for the frozen C050 k=15 discriminator.

This successor implements the operation named by the inert public contract. It
checks the hand/symbolic certificate and independently recomputes only the
public grammar-length branch set and the declared separating coordinate.  It
does not import a decoder, enumerate formula words, search for overlap, or
grant proof authority by itself.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


CANDIDATE_ID = "C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1"
CANDIDATE_CORE_SHA256 = (
    "sha256:c869e4726c36551b69f10407dd482f30d83f2b2a8129c5364ac2c08eda4c1d43"
)
CANDIDATE_ARTIFACT_HASH = (
    "sha256:47bf8d99a7c5620b8ab8f2e3fadfb762125df921bed4b65fe2ddb56f4733c5e1"
)
REQUIRED_OBLIGATIONS = (
    "PARENT_LENGTH_30_PARAMETER_EXHAUSTION",
    "CURRENT_LENGTH_32_PARAMETER_BRANCH_EXHAUSTION",
    "EXACT_CANONICAL_PARENT_PARSE",
    "EXACT_CANONICAL_CURRENT_PARSE",
    "EXACT_1C_EQUALS_PREFIX16_BITWISE",
    "PARENT_UNSAT_PROOF_INDEPENDENT_OF_SYNTAX",
    "SWAPPED_REDUCTION_PRESERVED",
    "BOUNDED_SCOPE_ONLY",
)
EXPECTED_BRANCHES = (
    {"v_values": [2, 3], "m": 2, "raw_length": 32, "padding": False},
    {
        "v_values": list(range(8, 16)),
        "m": 1,
        "raw_length": 31,
        "encoded_length": 32,
        "padding": True,
    },
)


class CertificateCheckError(RuntimeError):
    """Raised when the supplied record differs from the frozen contract."""


def _canonical_hash(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _sealed_hash(document: dict[str, Any]) -> str:
    subject = dict(document)
    subject["artifact_hash"] = ""
    return _canonical_hash(subject)


def _raw_length(v: int, m: int) -> int:
    return (
        8
        + (2 * v.bit_length() - 1)
        + (2 * m.bit_length() - 1)
        + 3 * m * (1 + v.bit_length())
    )


def _encoded_length(v: int, m: int) -> int:
    raw = _raw_length(v, m)
    return raw + raw % 2


def _actual_length_32_pairs() -> list[list[int]]:
    pairs: list[list[int]] = []
    # The certificate proves m>=3 cannot return to length 32. This bounded
    # range is a redundant hostile record check, not the mathematical proof.
    for v in range(1, 33):
        for m in range(1, 8):
            if _encoded_length(v, m) == 32:
                pairs.append([v, m])
    return pairs


def evaluate_certificate(
    certificate: dict[str, Any], authorization: dict[str, Any]
) -> dict[str, Any]:
    """Check the exact frozen certificate and return its scoped branch."""

    if certificate.get("candidate_id") != CANDIDATE_ID:
        raise CertificateCheckError("candidate identity mismatch")
    if certificate.get("candidate_core_sha256") != CANDIDATE_CORE_SHA256:
        raise CertificateCheckError("candidate core hash mismatch")
    if certificate.get("candidate_artifact_hash") != CANDIDATE_ARTIFACT_HASH:
        raise CertificateCheckError("candidate artifact hash mismatch")
    obligations = certificate.get("obligations")
    if not isinstance(obligations, list):
        raise CertificateCheckError("obligations missing")
    by_id = {row.get("obligation_id"): row for row in obligations}
    if tuple(row.get("obligation_id") for row in obligations) != REQUIRED_OBLIGATIONS:
        raise CertificateCheckError("obligation order or identity mismatch")
    if any(by_id[item].get("status") != "PROVED" for item in REQUIRED_OBLIGATIONS):
        raise CertificateCheckError("not every obligation is proved")
    branch_row = by_id["CURRENT_LENGTH_32_PARAMETER_BRANCH_EXHAUSTION"]
    if tuple(branch_row.get("branches", ())) != EXPECTED_BRANCHES:
        raise CertificateCheckError("length-32 branches are not exhaustive")
    expected_pairs = [[2, 2], [3, 2]] + [[v, 1] for v in range(8, 16)]
    if _actual_length_32_pairs() != expected_pairs:
        raise CertificateCheckError("independent public length arithmetic disagrees")
    parent = certificate.get("source_side_nonvacuity_witness", {})
    word = parent.get("word_x", "")
    r = parent.get("r", "")
    c = parent.get("c", "")
    h = parent.get("h_1c", "")
    if len(word) != 30 or word != r + c or len(r) != 15 or len(c) != 15:
        raise CertificateCheckError("parent split record mismatch")
    if h != "1" + c or len(h) != 16 or h[3] != "1":
        raise CertificateCheckError("H15 fixed-coordinate record mismatch")
    bit_row = by_id["EXACT_1C_EQUALS_PREFIX16_BITWISE"]
    if bit_row.get("separating_coordinate") != 3:
        raise CertificateCheckError("separating coordinate changed")
    if bit_row.get("h15_fixed_bit") != 1 or bit_row.get("p16_fixed_bit") != 0:
        raise CertificateCheckError("separating bit values changed")
    if authorization.get("candidate_id") != CANDIDATE_ID:
        raise CertificateCheckError("authorization candidate mismatch")
    if authorization.get("proof_check_authorized") is not True:
        raise CertificateCheckError("proof check is not authorized")
    if authorization.get("authorized_operation") != (
        "evaluate_certificate(exact_certificate, exact_authorization)"
    ):
        raise CertificateCheckError("authorized operation mismatch")
    if authorization.get("certificate_artifact_hash") != certificate.get(
        "artifact_hash"
    ):
        raise CertificateCheckError("authorization certificate hash mismatch")
    if certificate.get("artifact_hash") != _sealed_hash(certificate):
        raise CertificateCheckError("certificate artifact hash mismatch")
    return {
        "candidate_id": CANDIDATE_ID,
        "checked_current_parameter_pairs": expected_pairs,
        "common_separating_coordinate": 3,
        "h15_fixed_bit": 1,
        "p16_fixed_bit": 0,
        "obligations_checked": len(REQUIRED_OBLIGATIONS),
        "status": "PASS",
        "verdict": "SCOPED_OVERLAP_IMPOSSIBILITY",
    }


__all__ = ["CertificateCheckError", "evaluate_certificate"]
