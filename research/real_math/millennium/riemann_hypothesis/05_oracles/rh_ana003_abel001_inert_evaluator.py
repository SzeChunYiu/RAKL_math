"""Inert evaluator for the prospective fixed-n Abel-interface candidate.

This round freezes identity and proof obligations only.  It has no numerical,
symbolic, source-retrieval, or theorem-classification capability.
"""


class TargetEvaluationNotAuthorized(RuntimeError):
    """Raised because target proof evaluation belongs to a later round."""


def evaluate(*_args, **_kwargs):
    raise TargetEvaluationNotAuthorized(
        "RH-ANA-003-ABEL-001 is frozen but not authorized for proof evaluation"
    )
