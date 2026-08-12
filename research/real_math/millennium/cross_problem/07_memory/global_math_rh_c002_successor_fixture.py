#!/usr/bin/env python3
"""Build the one-unit RH C002 successor of the math-only saturation ledger."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
MEMORY = ROOT / "research/real_math/millennium/cross_problem/07_memory"
OLD = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_PNP_C050_K15_SUCCESSOR_20260812.json"
NEW = MEMORY / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_RH_C002_SUCCESSOR_20260812.json"
LESSON = ROOT / "research/real_math/millennium/riemann_hypothesis/07_memory/RH_ANA_003_ABEL_001_C002_SCOPED_MATHEMATICAL_LESSON_20260812.json"
RESULT = ROOT / "research/real_math/millennium/riemann_hypothesis/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json"
CORRECTION = ROOT / "research/real_math/millennium/riemann_hypothesis/05_oracles/RH_ANA_003_ABEL_001_C002_RESULT_BRANCH_CLASSIFICATION_CORRECTION_20260812.json"
BASE = "6fd16ea7363607021c1b0815dd3f27db7e4b3e5f"
FRAMEWORK = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
ITEM = "MATH-RH-ABEL-C002-FIXED-N-NATURAL-ORDER-NONABSOLUTE"
OLD_RAW = "6b3279e91de8e5a6c8b964154abba2e7ff403eb595fdad4de8cbb6b19208baaa"
OLD_BLOB = "66a679c442217f27aa4ca2a495710064623aac1a"


def raw_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def semantic(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(semantic(payload)).hexdigest()


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(path)
    return value


def build() -> dict:
    if raw_hash(OLD) != OLD_RAW:
        raise RuntimeError("predecessor ledger bytes changed")
    old = load(OLD)
    lesson = load(LESSON)
    correction = load(CORRECTION)
    if correction["corrected_classification"] != "PROVED_FIXED_N_NATURAL_ORDER_IDENTITY":
        raise RuntimeError("C002 result is not mapped to the exact frozen success branch")
    value = copy.deepcopy(old)
    value["ledger_id"] = "GLOBAL-MATH-ONLY-SATURATION-LEDGER-RH-C002-SUCCESSOR-20260812"
    value["as_of_utc"] = "2026-08-12T08:20:00Z"
    value["base_repository_sha"] = BASE
    value["authority_universe"] = {
        "kind": "MERGED_ORIGIN_MAIN_ONLY",
        "pending_or_open_pr_material_counted": False,
        "repository_sha": BASE,
        "rule": (
            f"Only content reachable from exact frozen origin/main {BASE} is eligible. "
            "Git/merge/CI status supplies assurance only and zero mathematical credit."
        ),
    }
    value["successor_lineage"] = {
        "predecessor_artifact_hash": old["artifact_hash"],
        "predecessor_raw_sha256": OLD_RAW,
        "predecessor_git_blob": OLD_BLOB,
        "predecessor_path": OLD.relative_to(ROOT).as_posix(),
        "predecessor_repository_sha": old["base_repository_sha"],
        "preservation": (
            "THE PNP C050 K15 SUCCESSOR AND ALL 48 PRIOR CREDITED ITEMS REMAIN "
            "CANONICAL-BYTE-SEMANTICALLY UNCHANGED; ADDS EXACTLY ONE DEDUPLICATED "
            "MERGED RH C002 PROOF_OR_LEMMA UNIT; THE POSTMERGE RESULT-BRANCH LABEL "
            "REPAIR EARNS ZERO MATHEMATICAL CREDIT; NO GLOBAL FAILURE CAUSE IS ADDED."
        ),
    }
    lanes = {lane["lane_id"]: lane for lane in value["lanes"]}
    item = {
        "item_id": ITEM,
        "credit_type": "PROOF_OR_LEMMA",
        "exact_claim": (
            "For every fixed integer n>=1 and nonintegral real X>=1, with "
            "a_m=1-Lambda(m), A(x)=floor(x)-psi(x), and "
            "b_n(x)=L_{n-1}^{(1)}(log x)/x, the natural-order identity "
            "lim_{Y->infinity} sum_{X<m<=Y} a_m b_n(m) = "
            "-A(X)b_n(X)-integral_X^infinity A(t)b_n'(t)dt holds; the transformed "
            "integral is absolutely convergent, while the original term series "
            "sum_m |a_m b_n(m)| diverges, witnessed on m=6k, including n=1."
        ),
        "scope": (
            "Each fixed integer n>=1, nonintegral X>=1, the frozen Laguerre normalization, "
            "Bellotti arXiv:2508.02041v1 equations (1.3)-(1.4) and Theorem 1.5, "
            "and original integer order only; constants may depend on n."
        ),
        "authority": "SAME_CONTEXT_HAND_DERIVATION_RECORD_CHECK_PASS",
        "mathematical_credit": True,
        "credit_units": 1,
        "evidence_pointers": [
            LESSON.relative_to(ROOT).as_posix(),
            RESULT.relative_to(ROOT).as_posix(),
            CORRECTION.relative_to(ROOT).as_posix(),
        ],
        "seven_field_math_lesson": copy.deepcopy(lesson["seven_field_math_lesson"]),
        "non_implications": [
            "No n-uniformity, series reordering or regrouping, PR316 rate, Li-coefficient positivity, novelty, independent review, or Riemann Hypothesis consequence.",
            "The effective result classification is the exact frozen branch PROVED_FIXED_N_NATURAL_ORDER_IDENTITY; the invalid renamed label is quarantined and adds no mathematical unit.",
            "Git, merges, CI, tests, schemas, hashes, serialization, runtime, chronology, telemetry, and same-context review supply zero additional mathematical credit and zero independent-review credit.",
        ],
    }
    lanes["riemann_hypothesis"]["credited_items"].append(item)
    value["totals"]["mathematical_credit_units"] = 49
    value["totals"]["mathematical_credit_units_by_lane"]["riemann_hypothesis"] = 8
    value["totals"]["mathematical_credit_units_by_type"]["PROOF_OR_LEMMA"] = 17
    value["bounded_disposition"]["rh_c002"] = {
        "classification": "SCOPED_FIXED_N_NATURAL_ORDER_ABEL_PROOF",
        "credited_item_id": ITEM,
        "credit_units": 1,
        "effective_frozen_result_branch": "PROVED_FIXED_N_NATURAL_ORDER_IDENTITY",
        "invalid_result_label_credit_units": 0,
        "postmerge_governance_repair_credit_units": 0,
        "seven_field_math_lesson_preserved_exactly": True,
        "global_failure_cause_added": False,
        "global_ledger_state": "MERGED_RESULT_SYNTHESIZED_THIS_SUCCESSOR",
    }
    value["bounded_disposition"]["failure_atlas"] = {
        "action": "NO_NEW_DISTINCT_CAUSE",
        "added_cause_ids": [],
        "reason": (
            "C002 is a positive scoped proof unit. The predecessor C001 notation defect remains "
            "local negative history and the result-label defect is governance-only, so neither "
            "creates a new global mathematical failure cause in this synthesis."
        ),
        "unchanged_atlas_path": (
            "research/real_math/millennium/cross_problem/07_memory/"
            "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_YM_R20_HODGE_C007_SUCCESSOR_20260812.json"
        ),
    }
    value["artifact_hash"] = ""
    value["artifact_hash"] = artifact_hash(value)
    return value


def main() -> None:
    NEW.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
