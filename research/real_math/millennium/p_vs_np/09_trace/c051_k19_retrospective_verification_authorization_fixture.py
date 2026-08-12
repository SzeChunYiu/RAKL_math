"""Build public authorization for retrospective C051 k=19 verification.

The shared workspace already contained uncommitted result-shaped artifacts from
a parallel session before this authorization.  This record therefore cannot
grant prospective discovery credit.  It authorizes only post-merge verification
of the exact previously frozen discriminator and preservation of the resulting
mathematical truth/failure at retrospective authority.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CANDIDATE = PNP / "04_candidates/O9d12a2a1b_C051_K19_ALIGNMENT_DISCRIMINATOR_FREEZE_20260812.json"
RETROSPECTIVE = PNP / "04_candidates/O9d12a2a1b_C051_K19_RETROSPECTIVE_DISCRIMINATOR_FREEZE_20260812.json"
EVALUATOR = PNP / "05_falsification/c051_k19_alignment_evaluator.py"
CORRECTION = PNP / "09_trace/O9d12a2a1b_C051_SUPPORT_CONTAMINATION_CORRECTION_20260812.json"
OUTPUT = PNP / "09_trace/O9d12a2a1b_C051_K19_RETROSPECTIVE_VERIFICATION_AUTHORIZATION_20260812.json"


def digest(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def seal(document: dict) -> dict:
    core = dict(document)
    core.pop("artifact_hash", None)
    core["artifact_hash"] = digest(json.dumps(core, sort_keys=True, separators=(",", ":")).encode())
    return core


def build() -> dict:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    retrospective = json.loads(RETROSPECTIVE.read_text(encoding="utf-8"))
    correction = json.loads(CORRECTION.read_text(encoding="utf-8"))
    if correction["corrected_authority"]["candidate_generation_allowed_under_original_strict_gate"] is not False:
        raise RuntimeError("original strict gate must remain failed closed")
    return seal({
        "schema_version": "1.0.0",
        "authorization_id": "PNP-C051-K19-RETROSPECTIVE-VERIFICATION-AUTHORIZATION-20260812",
        "atom_id": "O9d12a2a1b-C051",
        "authority": "PUBLIC_AUTHORIZATION_FOR_RETROSPECTIVE_VERIFICATION_ONLY_NO_PROSPECTIVE_DISCOVERY_CREDIT",
        "application_base_commit": "683fdab891541be87eed6b99741617f5b66f84ef",
        "candidate_bindings": [
            {
                "candidate_id": candidate["candidate_identity"]["candidate_id"],
                "candidate_core_sha256": candidate["candidate_identity"]["candidate_core_sha256"],
                "artifact_hash": candidate["artifact_hash"],
            },
            {
                "candidate_id": retrospective["candidate_identity"]["candidate_id"],
                "candidate_core_sha256": retrospective["candidate_identity"]["candidate_core_sha256"],
                "artifact_hash": retrospective["artifact_hash"],
            },
        ],
        "evaluator_binding": {
            "path": str(EVALUATOR.relative_to(ROOT)),
            "raw_sha256": digest(EVALUATOR.read_bytes()),
        },
        "chronology": {
            "authorization_frozen_at": "2026-08-12T09:55:36Z",
            "verification_executed_in_this_round": False,
            "parallel_uncommitted_result_shaped_artifacts_observed_before_authorization": True,
            "result_value_inspected_for_this_authorization": False,
            "prospective_result_credit_permanently_forfeited": True,
        },
        "licensed_after_public_merge": [
            "execute the exact bound evaluator",
            "construct and check a direct finite mathematical certificate for the observed branch",
            "record the exact result with the seven mathematical lesson coordinates",
            "classify the result as retrospective verification rather than strict RAKL discovery",
        ],
        "forbidden": [
            "claim the k=19 support or result was untouched",
            "claim prospective discovery credit",
            "change the frozen grammar, split, transpose interface, candidate, evaluator, or result branch after execution",
            "infer cover growth, circuit lower bounds, novelty, independent review, or P-versus-NP closure",
        ],
        "mathematical_credit": 0,
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


if __name__ == "__main__":
    OUTPUT.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
