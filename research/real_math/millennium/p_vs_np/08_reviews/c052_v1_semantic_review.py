"""Post-execution semantic review of the frozen C052 v1 escape interface.

This is a same-context review pass, not an independent evaluator.  It checks
whether an escape certificate ranges over the semantic parent set H_k rather
than merely over the ambient set of syntactically legal literal tokens.
"""

from __future__ import annotations


REQUIRED_WITNESS_QUANTIFIER = "EVERY_V_EVERY_INDEX_BOTH_CLAUSE_ORDERS"


def review_escape_claim(cell: object, claimed: object) -> dict:
    base = {
        "review_kind": "SAME_CONTEXT_POST_EXECUTION_SEMANTIC_REVIEW",
        "independent_peer_review": False,
        "classifier_promotion": "BLOCKED",
        "native_gate": "BLOCKED",
    }
    if not isinstance(cell, dict) or not isinstance(claimed, dict):
        return {
            **base,
            "semantic_outcome": "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT",
            "blocking_reason": "Input or claimed result is not a complete mapping.",
        }
    if claimed.get("branch") != "ESCAPE_ADMISSIBLE":
        return {
            **base,
            "semantic_outcome": "NOT_APPLICABLE_TO_NON_ESCAPE_BRANCH",
            "blocking_reason": "This review only audits the v1 escape certificate.",
        }
    certificate = claimed.get("certificate")
    if not isinstance(certificate, dict):
        return {
            **base,
            "semantic_outcome": "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT",
            "blocking_reason": "Escape certificate is absent.",
        }
    family = certificate.get("unsat_preserving_witness_family")
    if not isinstance(family, dict) or family.get("complete") is not True:
        return {
            **base,
            "semantic_outcome": "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT",
            "blocking_reason": (
                "The all-syntax bit audit does not supply an explicit UNSAT-preserving "
                "witness family inside H_k for every claimed variable-count/index/sign variation."
            ),
            "shared_omission": (
                "The v1 classifier and its same-context falsifier both range over ambient "
                "syntax and therefore agreement cannot detect this semantic-subset gap."
            ),
        }
    if cell.get("unsat_witness_quantifier") != REQUIRED_WITNESS_QUANTIFIER:
        return {
            **base,
            "semantic_outcome": "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT",
            "blocking_reason": "The UNSAT-preserving witness quantifier is missing or weaker than frozen completeness.",
        }
    return {
        **base,
        "semantic_outcome": "WITNESS_PRESENT_REQUIRES_SEPARATE_PROOF_CHECK",
        "blocking_reason": "Presence of a witness object is not itself proof; validate it in a separately versioned proof artifact.",
    }
