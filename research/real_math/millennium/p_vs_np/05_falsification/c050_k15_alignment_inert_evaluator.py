"""Inert public contract for a future, separately authorized evaluation.

This module deliberately has no grammar parser, satisfiability routine, target
data, search loop, or result branch.  Its only executable behavior is to fail
closed until a successor authorization is public.
"""

from __future__ import annotations


class TargetEvaluationNotAuthorized(RuntimeError):
    """Raised because this freeze artifact cannot inspect the target."""


def evaluate_target() -> None:
    """Fail closed; a successor artifact must supply all target capability."""

    raise TargetEvaluationNotAuthorized(
        "target evaluation is not authorized by this inert freeze contract"
    )


if __name__ == "__main__":
    raise SystemExit("inert contract only; target evaluation is not authorized")
