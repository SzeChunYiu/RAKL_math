#!/usr/bin/env python3
"""Append-only correction for the C002 post-freeze result-branch label."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = "research/real_math/millennium/riemann_hypothesis"
MERGE_COMMIT = "318984a0b9f78fd6b8ed426ecf2b6ef64d07cb3b"
CANDIDATE_ID = "RH-ANA-003-ABEL-001-C002-FIXED-N-NATURAL-ORDER-ABEL"
CANDIDATE_CORE = "sha256:b9bd54e72850dbc31b2fba344d978ee3660f0004bf81fb237347f0eb8b5ab3ab"
INVALID_LABEL = "ALL_O1_O7_SUPPORTED_BY_FROZEN_HAND_PROOF"
FROZEN_LABEL = "PROVED_FIXED_N_NATURAL_ORDER_IDENTITY"
RECORDED_AT = "2026-08-12T08:18:00Z"
RESULT_RAW = "0d1dd6087f752307f4270ce97b1ad4f88d6809037a856c979837b85d94b91b6b"
MANIFEST_RAW = "526e0dc2b54ee8d9bd98b70cc129cae25bc363dc979df8370fe7d077d8a1ced2"

RESULT = ROOT / f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json"
MANIFEST = ROOT / f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_EVALUATOR_FREEZE_20260812.json"
CANDIDATE = ROOT / f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_FIXED_N_ABEL_CANDIDATE_FREEZE_20260812.json"
PROOF_INPUT = ROOT / f"{BASE}/04_candidates/RH_ANA_003_ABEL_001_C002_PROOF_INPUT_FREEZE_20260812.json"
PATHS = {
    "correction": f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_RESULT_BRANCH_CLASSIFICATION_CORRECTION_20260812.json",
    "receipt": f"{BASE}/09_trace/RH_ANA_003_ABEL_001_C002_RESULT_BRANCH_POSTMERGE_REPAIR_RECEIPT_20260812.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def raw_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seal(value: dict) -> dict:
    value = dict(value)
    value.pop("artifact_hash", None)
    value["artifact_hash"] = canonical_hash(value)
    return value


def build_documents() -> dict[str, dict]:
    if raw_hash(RESULT) != RESULT_RAW or raw_hash(MANIFEST) != MANIFEST_RAW:
        raise RuntimeError("merged result/evaluator history changed")
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    proof_input = json.loads(PROOF_INPUT.read_text(encoding="utf-8"))
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    frozen_candidate_branches = candidate["allowed_result_branches"]
    frozen_proof_branches = proof_input["allowed_result_branches"]
    if frozen_candidate_branches != frozen_proof_branches:
        raise RuntimeError("candidate and proof-input branch contracts differ")
    if FROZEN_LABEL not in frozen_candidate_branches or INVALID_LABEL in frozen_candidate_branches:
        raise RuntimeError("unexpected frozen result-branch contract")
    if result["evaluator_output"]["verdict"] != INVALID_LABEL:
        raise RuntimeError("merged result no longer exhibits reviewed label defect")

    correction = seal({
        "schema_version": "1.0.0",
        "correction_id": "RH-ANA-003-ABEL-001-C002-RESULT-BRANCH-CLASSIFICATION-CORRECTION-20260812",
        "candidate_id": CANDIDATE_ID,
        "candidate_core_sha256": CANDIDATE_CORE,
        "source_merge_commit": MERGE_COMMIT,
        "source_result": {"path": str(RESULT.relative_to(ROOT)), "raw_sha256": RESULT_RAW},
        "source_evaluator_manifest": {"path": str(MANIFEST.relative_to(ROOT)), "raw_sha256": MANIFEST_RAW},
        "finding": {
            "review_source": "Cursor Bugbot postmerge review on PR361; automated code review, not independent mathematical peer review",
            "invalid_observed_label": INVALID_LABEL,
            "exact_frozen_success_branch": FROZEN_LABEL,
            "defect": "the evaluator/result renamed the already frozen positive result branch",
        },
        "append_only_decision": {
            "historical_files_rewritten": False,
            "invalid_label_quarantined": True,
            "mathematical_proof_quarantined": False,
            "scoped_mathematical_lesson_changed": False,
            "classification_superseded_prospectively": True,
        },
        "branch_mapping": {
            "observed_result_facts": [
                "O1-O7 supported by the frozen same-context hand certificate",
                "the fixed-n natural-order identity is proved",
                "the original term series is nonabsolute",
            ],
            "mapped_frozen_branch": FROZEN_LABEL,
            "mapping_basis": (
                "The candidate's exact permitted positive branch names the fixed-n natural-order identity. "
                "The nonabsolute statement is part of the same frozen candidate conclusion and does not create a new branch."
            ),
            "new_mathematical_result_created": False,
        },
        "corrected_classification": FROZEN_LABEL,
        "scope": "result-branch classification label only",
        "authority": "APPEND_ONLY_GOVERNANCE_REPAIR_NO_NEW_MATHEMATICS_NO_INDEPENDENT_REVIEW",
        "credit": {"mathematical": 0, "saturation": 0, "root": 0, "operational_governance_only": True},
        "global_ledger_updated": False,
        "recorded_at": RECORDED_AT,
    })
    receipt = seal({
        "schema_version": "1.0.0",
        "receipt_id": "RH-ANA-003-ABEL-001-C002-RESULT-BRANCH-POSTMERGE-REPAIR-20260812",
        "candidate_id": CANDIDATE_ID,
        "source_merge_commit": MERGE_COMMIT,
        "historical_result_raw_sha256": RESULT_RAW,
        "historical_manifest_raw_sha256": MANIFEST_RAW,
        "correction_artifact_hash": correction["artifact_hash"],
        "invalid_label": INVALID_LABEL,
        "effective_frozen_result_branch": FROZEN_LABEL,
        "historical_artifacts_preserved": True,
        "mathematical_proof_or_lesson_modified": False,
        "mathematical_credit": 0,
        "global_ledger_updated": False,
        "status": "PASS_APPEND_ONLY_BRANCH_LABEL_CORRECTION",
        "recorded_at": RECORDED_AT,
    })
    return {"correction": correction, "receipt": receipt}


def main() -> None:
    for name, document in build_documents().items():
        path = ROOT / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
