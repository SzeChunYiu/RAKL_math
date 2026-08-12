"""Inert falsifier for the prospective YM R20 K-coordinate scalar candidate.

This candidate-freeze round records only the exact symbolic proposition,
source-binding obligations, result branches, and falsifier identity.  It has no
symbolic algebra, numerical threshold search, source retrieval, or theorem
classification capability.
"""


class TargetEvaluationNotAuthorized(RuntimeError):
    """Raised because scalar evaluation belongs to a later public round."""


def evaluate(*_args, **_kwargs):
    raise TargetEvaluationNotAuthorized(
        "YM-S1a2i-K1-C001 is frozen but scalar/source evaluation is not authorized"
    )
