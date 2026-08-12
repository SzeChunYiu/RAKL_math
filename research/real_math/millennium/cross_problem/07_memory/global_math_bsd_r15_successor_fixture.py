#!/usr/bin/env python3
"""Build the one-unit BSD R15 ledger successor and zero-new-cause atlas successor."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_RH_C002_SUCCESSOR_20260812.json"
NEW_LEDGER = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_BSD_R15_SUCCESSOR_20260812.json"
OLD_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_YM_R20_HODGE_C007_SUCCESSOR_20260812.json"
NEW_ATLAS = MEMORY / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_BSD_R15_SUCCESSOR_20260812.json"
LESSON = ROOT / "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a2_R15_SCOPED_MATHEMATICAL_LESSON_20260812.json"
RESULT = ROOT / "research/real_math/millennium/birch_swinnerton_dyer/00_sources/BSD_A1a2_R15_KUMMER_SHA_EXACT_RANK_RESULT_20260812.json"
DAG = ROOT / "research/real_math/millennium/birch_swinnerton_dyer/02_problem_dag/BSD_A1a2_R15_KUMMER_SHA_DAG_DELTA_20260812.yaml"
REVIEW = ROOT / "research/real_math/millennium/birch_swinnerton_dyer/08_reviews/BSD_A1a2_R15_RESULT_REVIEW_20260812.md"
BASE = "f3275302b2198bbd15d551d57adce85c5762c013"
ITEM = "MATH-BSD-R15-KUMMER-SHA-CORANK-DECOMPOSITION"
SPECIALIZATION = "SP-BSD-R15-UNCONTROLLED-QUOTIENT-CORANK"
PARENT_CAUSE = "FM-BSD-ARITHMETIC-PREMISE-REIMPORT"
OLD_LEDGER_RAW = "bd41c089a30b803f1bde81511f7205beab3c47306d50c788bf6a515a5e9e0243"
OLD_LEDGER_BLOB = "5493f8251a2951239cad1f7abaded5c1f71e94dd"
OLD_ATLAS_RAW = "fe9d71646b451548f11edb301bf3c1e7b736e688fc87e3108b233d68dad01f8e"
OLD_ATLAS_BLOB = "38995f589715c1496c5e91cfe81e18a0743656fc"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(path)
    return value


def semantic(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def raw_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(semantic(payload)).hexdigest()


def seven_fields(lesson: dict) -> dict:
    return {
        "attempted_implication": lesson["attempted_implication"],
        "exact_result_or_failure": lesson["exact_result_or_failure"],
        "supported_and_competing_causes": copy.deepcopy(lesson["supported_and_competing_causes"]),
        "scope": lesson["scope"],
        "mathematical_falsifier": lesson["mathematical_falsifier"],
        "mathematical_repair_or_next_discriminator": lesson["mathematical_repair_or_next_discriminator"],
        "proof_or_source_evidence": copy.deepcopy(lesson["proof_or_source_evidence"]),
    }


def build_ledger() -> dict:
    if raw_hash(OLD_LEDGER) != OLD_LEDGER_RAW:
        raise RuntimeError("predecessor ledger bytes changed")
    old, lesson = load(OLD_LEDGER), load(LESSON)
    value = copy.deepcopy(old)
    value["ledger_id"] = "GLOBAL-MATH-ONLY-SATURATION-LEDGER-BSD-R15-SUCCESSOR-20260812"
    value["as_of_utc"] = "2026-08-12T09:45:00Z"
    value["base_repository_sha"] = BASE
    value["authority_universe"] = {
        "kind": "MERGED_ORIGIN_MAIN_ONLY",
        "pending_or_open_pr_material_counted": False,
        "repository_sha": BASE,
        "rule": (
            f"Only mathematical content reachable from exact frozen origin/main {BASE} is eligible. "
            "Git, CI, schemas, hashes, chronology, telemetry, and same-context review have zero mathematical credit."
        ),
    }
    value["successor_lineage"] = {
        "predecessor_artifact_hash": old["artifact_hash"],
        "predecessor_raw_sha256": OLD_LEDGER_RAW,
        "predecessor_git_blob": OLD_LEDGER_BLOB,
        "predecessor_path": OLD_LEDGER.relative_to(ROOT).as_posix(),
        "predecessor_repository_sha": old["base_repository_sha"],
        "preservation": (
            "THE RH C002 SUCCESSOR AND ALL 49 PRIOR CREDITED ITEMS REMAIN BYTE-SEMANTICALLY "
            "UNCHANGED; ADDS EXACTLY ONE DEDUPLICATED BSD R15 PROOF_OR_LEMMA UNIT. "
            "THE R15 FAILURE MECHANISM IS CLASSIFIED AS A SPECIALIZATION OF EXISTING "
            "BSD ARITHMETIC-PREMISE REIMPORT/REPRESENTATION RELOCATION, SO THE GLOBAL "
            "FAILURE-CAUSE COUNT DOES NOT INCREASE."
        ),
    }
    item = {
        "item_id": ITEM,
        "credit_type": "PROOF_OR_LEMMA",
        "exact_claim": (
            "For an elliptic curve E/Q, a prime p, and the usual Kummer p-infinity Selmer group, "
            "corank_Zp Sel(Q,E[p^infinity]) = rank_Z E(Q) + "
            "corank_Zp Sha(E/Q)[p^infinity]. Consequently, if the Selmer corank is two, "
            "then rank_Z E(Q)=2 if and only if Sha(E/Q)[p^infinity] has corank zero; "
            "in the stated cofinitely generated scope, this is equivalent to finiteness."
        ),
        "scope": (
            "Same E/Q and p; usual Kummer Selmer structure; cofinitely generated p-primary groups; "
            "a source-bound hand lemma. No actual infinite-Sha elliptic curve, exact finite Sha order, "
            "complex-to-Kurihara calibration, refined leading term, novelty, or BSD root conclusion."
        ),
        "authority": "SOURCE_BOUND_HAND_LEMMA_SAME_CONTEXT_REVIEW_ONLY",
        "mathematical_credit": True,
        "credit_units": 1,
        "evidence_pointers": [
            RESULT.relative_to(ROOT).as_posix(),
            LESSON.relative_to(ROOT).as_posix(),
            DAG.relative_to(ROOT).as_posix(),
            REVIEW.relative_to(ROOT).as_posix(),
        ],
        "seven_field_math_lesson": seven_fields(lesson),
        "deduplication": {
            "new_relative_to_bsd_r9": "R9 gives only complex analytic rank two -> p-infinity Selmer corank at least two under Zhang hypotheses; R15 gives the exact internal Selmer/Mordell-Weil/Sha corank decomposition.",
            "new_relative_to_bsd_r12": "R12 equates p-infinity Selmer corank with V_p Bloch-Kato dimension; R15 decomposes that common arithmetic size into Mordell-Weil rank plus the p-divisible Sha quotient.",
            "not_a_second_failure_cause": "The quotient term is the exact arithmetic specialization of the already credited premise-reimport/representation-relocation mechanism, not a new global mechanism family."
        },
        "non_implications": [
            "Logical non-sufficiency of the exact sequence is not an exhibited elliptic-curve counterexample with infinite Sha.",
            "Exact Selmer corank two does not establish Mordell-Weil rank two until the p-primary Sha quotient is independently controlled.",
            "Finiteness/corank zero does not identify the exact Sha order or any regulator, Tamagawa, torsion, period, or complex leading-term factor.",
            "Git, CI, schemas, hashes, chronology, telemetry, repository growth, and same-context review add zero mathematical credit and zero independent-review credit."
        ],
    }
    lane = next(lane for lane in value["lanes"] if lane["lane_id"] == "birch_swinnerton_dyer")
    lane["credited_items"].append(item)
    value["totals"]["mathematical_credit_units"] = 50
    value["totals"]["mathematical_credit_units_by_lane"]["birch_swinnerton_dyer"] = 4
    value["totals"]["mathematical_credit_units_by_type"]["PROOF_OR_LEMMA"] = 18
    value["bounded_disposition"]["bsd_r15"] = {
        "classification": "SOURCE_BOUND_EXACT_SEQUENCE_CORANK_DECOMPOSITION",
        "credited_item_id": ITEM,
        "credit_units": 1,
        "new_theorem_novelty": False,
        "seven_field_math_lesson_preserved": True,
        "failure_cause_classification": "SPECIALIZATION_OF_EXISTING_FM_BSD_ARITHMETIC_PREMISE_REIMPORT",
        "new_global_failure_cause_units": 0,
    }
    value["bounded_disposition"]["failure_atlas"] = {
        "action": "ADD_SPECIALIZATION_WITH_ZERO_NEW_DISTINCT_CAUSE",
        "added_cause_ids": [],
        "specialization_id": SPECIALIZATION,
        "parent_cause_id": PARENT_CAUSE,
        "reason": (
            "R15 identifies the exact omitted arithmetic premise inside the Selmer representation: "
            "the quotient Sha[p^infinity] must have corank zero. This sharpens, rather than duplicates, "
            "the existing BSD cause that arithmetic carriers relocate or reimport the root-facing premise."
        ),
        "successor_atlas_path": NEW_ATLAS.relative_to(ROOT).as_posix(),
    }
    value["artifact_hash"] = ""
    value["artifact_hash"] = artifact_hash(value)
    return value


def build_atlas() -> dict:
    if raw_hash(OLD_ATLAS) != OLD_ATLAS_RAW:
        raise RuntimeError("predecessor atlas bytes changed")
    old, lesson = load(OLD_ATLAS), load(LESSON)
    value = copy.deepcopy(old)
    value["atlas_id"] = "GLOBAL-MATHEMATICAL-FAILURE-CAUSE-ATLAS-BSD-R15-SUCCESSOR-20260812"
    value["as_of_utc"] = "2026-08-12T09:45:00Z"
    value["authority_universe"] = {
        "kind": "MERGED_ORIGIN_MAIN_ONLY",
        "repository_sha": BASE,
        "pending_or_open_pr_material_counted": False,
        "mathematical_only": True,
        "software_assurance_excluded_from_mathematical_causality": True,
    }
    value["successor_lineage"] = {
        "predecessor_artifact_hash": old["artifact_hash"],
        "predecessor_raw_sha256": OLD_ATLAS_RAW,
        "predecessor_git_blob": OLD_ATLAS_BLOB,
        "predecessor_path": OLD_ATLAS.relative_to(ROOT).as_posix(),
        "predecessor_repository_sha": old["authority_universe"]["repository_sha"],
        "preservation": (
            "ALL 12 PRIOR DISTINCT FAILURE MECHANISMS REMAIN BYTE-SEMANTICALLY UNCHANGED. "
            "BSD R15 ADDS ONE SEVEN-FIELD SPECIALIZATION UNDER FM-BSD-ARITHMETIC-PREMISE-REIMPORT "
            "AND ZERO NEW DISTINCT GLOBAL FAILURE CAUSES."
        ),
    }
    value["failure_mechanism_specializations"] = [{
        "specialization_id": SPECIALIZATION,
        "parent_cause_id": PARENT_CAUSE,
        "equivalence_class": "CROSS-REPRESENTATION-RELOCATION",
        "classification": "VERIFIED_EXACT_SEQUENCE_SPECIALIZATION_NOT_NEW_CAUSE",
        "attempted_implication": lesson["attempted_implication"],
        "exact_result_or_failure": lesson["exact_result_or_failure"],
        "supported_and_competing_causes": copy.deepcopy(lesson["supported_and_competing_causes"]),
        "mechanism_mapping": {
            "carrier_or_representation": "p-infinity Selmer corank",
            "target_coordinate": "Mordell-Weil rank",
            "relocated_or_reimported_obligation": "corank_Zp Sha(E/Q)[p^infinity]=0, equivalently p-primary Sha finiteness in the cofinite scope",
            "exact_interface": "0 -> E(Q) tensor Q_p/Z_p -> Sel(Q,E[p^infinity]) -> Sha(E/Q)[p^infinity] -> 0",
            "why_not_new": (
                "The parent mechanism already records that a Selmer carrier does not discharge the missing root-facing arithmetic premise. "
                "R15 identifies that premise exactly as the quotient corank in this coordinate transition; it does not introduce a different failure morphology."
            ),
        },
        "scope": lesson["scope"],
        "mathematical_falsifier": lesson["mathematical_falsifier"],
        "repair_or_next_discriminator": lesson["mathematical_repair_or_next_discriminator"],
        "proof_or_source_evidence": copy.deepcopy(lesson["proof_or_source_evidence"]),
        "evidence_pointers": [RESULT.relative_to(ROOT).as_posix(), LESSON.relative_to(ROOT).as_posix()],
        "new_global_failure_cause_credit_units": 0,
        "mathematical_ledger_credit_units": 1,
        "nonclaim": "No actual elliptic curve with positive Sha[p^infinity] corank is asserted; this is an exact logical sufficiency diagnosis."
    }]
    value["bounded_disposition"] = {
        "distinct_failure_mechanisms_before": len(old["failure_mechanisms"]),
        "distinct_failure_mechanisms_after": len(old["failure_mechanisms"]),
        "new_distinct_failure_mechanism_ids": [],
        "added_specialization_ids": [SPECIALIZATION],
        "deduplication_verdict": "SPECIALIZATION_OF_EXISTING_BSD_PREMISE_REIMPORT_AND_CROSS_REPRESENTATION_RELOCATION",
        "mathematical_basis": (
            "The exact sequence shows how the Selmer carrier aggregates the target rank with an uncontrolled quotient. "
            "Using carrier exactness as target exactness therefore imports quotient-zero as an unstated premise, matching the existing mechanism."
        ),
    }
    value["artifact_hash"] = ""
    value["artifact_hash"] = artifact_hash(value)
    return value


def main() -> None:
    NEW_ATLAS.write_text(json.dumps(build_atlas(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEW_LEDGER.write_text(json.dumps(build_ledger(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
