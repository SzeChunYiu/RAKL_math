from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ResultBranch(str, Enum):
    APPLICABLE_BRIDGE = "APPLICABLE_BRIDGE"
    STRONGER_PREMISE_MISMATCH_A = "STRONGER_PREMISE_MISMATCH_A"
    FLOW_MARGIN_FAIL_B = "FLOW_MARGIN_FAIL_B"
    CANNOT_CHECK = "CANNOT_CHECK"


class StageADerivation(str, Enum):
    SEPARATE_CONSTANTS = "SEPARATE_CONSTANTS"
    CONFLATED_SOURCE_CONSTANT = "CONFLATED_SOURCE_CONSTANT"
    INSUFFICIENT = "INSUFFICIENT"


class StageBProof(str, Enum):
    EXACT_INTERVAL_MARGIN = "EXACT_INTERVAL_MARGIN"
    EXACT_PREDICATE_DISPROVED = "EXACT_PREDICATE_DISPROVED"
    FACTOR_TWO_ONLY = "FACTOR_TWO_ONLY"
    INSUFFICIENT = "INSUFFICIENT"
    NOT_ENTERED = "NOT_ENTERED"


@dataclass(frozen=True)
class EvaluationWorld:
    stage_a_derivation: StageADerivation
    stage_a_compatibility_proved: bool | None
    g_star_frozen_before_stage_b: bool
    stage_b_proof: StageBProof


@dataclass(frozen=True)
class EvaluationResult:
    branch: ResultBranch
    stage_a_status: str
    stage_b_status: str
    reason: str


def evaluate(world: EvaluationWorld) -> EvaluationResult:
    """Evaluate the frozen two-stage mathematical discriminator.

    This function routes already-specified mathematical evidence.  It does not
    choose constants, enlarge a source domain, or infer a Stage-B interval.
    """

    if world.stage_a_derivation is StageADerivation.INSUFFICIENT:
        return EvaluationResult(
            ResultBranch.CANNOT_CHECK,
            "CANNOT_CHECK",
            "NOT_ENTERED",
            "The source does not determine the Stage-A constant roles or their compatibility.",
        )

    if world.stage_a_derivation is StageADerivation.CONFLATED_SOURCE_CONSTANT:
        # The frozen source-world has C_dom=C_force=C and 0<rho<1.  Therefore
        # c_K/C_dom = 4/(1-rho) > 1 without assigning a numerical value to C.
        return EvaluationResult(
            ResultBranch.STRONGER_PREMISE_MISMATCH_A,
            "FAIL",
            "NOT_ENTERED",
            "With C_dom=C_force=C and 0<rho<1, c_K=4C/(1-rho)>C_dom.",
        )

    if world.stage_a_compatibility_proved is None:
        return EvaluationResult(
            ResultBranch.CANNOT_CHECK,
            "CANNOT_CHECK",
            "NOT_ENTERED",
            "Separate constants were asserted but their compatibility was not proved.",
        )
    if not world.stage_a_compatibility_proved:
        return EvaluationResult(
            ResultBranch.STRONGER_PREMISE_MISMATCH_A,
            "FAIL",
            "NOT_ENTERED",
            "The separately derived constants violate c_K<=C_dom.",
        )

    if not world.g_star_frozen_before_stage_b:
        return EvaluationResult(
            ResultBranch.CANNOT_CHECK,
            "PASS",
            "CANNOT_CHECK",
            "Stage B cannot run before a positive g_star is separately frozen.",
        )
    if world.stage_b_proof is StageBProof.EXACT_PREDICATE_DISPROVED:
        return EvaluationResult(
            ResultBranch.FLOW_MARGIN_FAIL_B,
            "PASS",
            "FAIL",
            "At least one exact full-interval Stage-B predicate was disproved.",
        )
    if world.stage_b_proof is StageBProof.FACTOR_TWO_ONLY:
        return EvaluationResult(
            ResultBranch.FLOW_MARGIN_FAIL_B,
            "PASS",
            "FAIL",
            "The factor-two comparison yields coefficient 1+rho>1, not the exact next radius.",
        )
    if world.stage_b_proof is StageBProof.INSUFFICIENT:
        return EvaluationResult(
            ResultBranch.CANNOT_CHECK,
            "PASS",
            "CANNOT_CHECK",
            "The full-interval Stage-B predicates were not proved or disproved.",
        )
    if world.stage_b_proof is StageBProof.EXACT_INTERVAL_MARGIN:
        return EvaluationResult(
            ResultBranch.APPLICABLE_BRIDGE,
            "PASS",
            "PASS",
            "Separate compatible constants and both exact interval predicates are proved.",
        )
    return EvaluationResult(
        ResultBranch.CANNOT_CHECK,
        "PASS",
        "CANNOT_CHECK",
        "Stage A passed but Stage B was not entered.",
    )
