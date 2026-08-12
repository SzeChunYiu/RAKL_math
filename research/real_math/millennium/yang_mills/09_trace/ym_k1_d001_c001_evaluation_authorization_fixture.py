from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any

ROOT = Path(__file__).resolve().parents[5]
PARENT_MAIN_SHA = "46000411f3edc7b96eba3ddb201e45f2b6d690ce"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
CANDIDATE_ID = "YM-S1a2i-K1-D001-C001-TWO-STAGE-SOURCE-BRIDGE"
CANDIDATE = "research/real_math/millennium/yang_mills/04_candidates/YM-S1a2i_K1_D001_C001_TWO_STAGE_SOURCE_BRIDGE_FREEZE_20260812.json"
FALSIFIER = "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_D001_C001_INERT_FALSIFIER_FREEZE_20260812.json"
RECEIPT = "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_C001_CANDIDATE_FREEZE_RECEIPT_20260812.json"
SOURCE_AUDIT = "research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_K1_D001_WILSON_SOURCE_APPLICABILITY_AUDIT_20260812.json"
OUTPUT = ROOT / "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_C001_POSTMERGE_EVALUATION_AUTHORIZATION_20260812.json"


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def _sha(value: Any) -> str:
    return "sha256:" + hashlib.sha256(_canonical(value)).hexdigest()


def _binding(path: str) -> dict[str, Any]:
    raw = (ROOT / path).read_bytes()
    document = json.loads(raw)
    blob = subprocess.run(["git", "-C", str(ROOT), "rev-parse", f"{PARENT_MAIN_SHA}:{path}"], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()
    return {
        "path": path,
        "application_commit": PARENT_MAIN_SHA,
        "git_blob": blob,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_sha256": _sha(document),
        "declared_artifact_hash": document.get("artifact_hash", ""),
    }


def build_document() -> dict[str, Any]:
    candidate = json.loads((ROOT / CANDIDATE).read_text())
    falsifier = json.loads((ROOT / FALSIFIER).read_text())
    receipt = json.loads((ROOT / RECEIPT).read_text())
    core = {
        "schema_version": "1.0.0",
        "authorization_id": "YM-S1a2i-K1-D001-C001-POSTMERGE-EVALUATION-AUTHORIZATION-20260812",
        "candidate_id": CANDIDATE_ID,
        "parent_main_sha": PARENT_MAIN_SHA,
        "framework_sha": FRAMEWORK_SHA,
        "public_freeze_binding": {
            "candidate": _binding(CANDIDATE),
            "declarative_falsifier": _binding(FALSIFIER),
            "freeze_receipt": _binding(RECEIPT),
        },
        "identity_checks": {
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "falsifier_core_sha256": falsifier["falsifier_identity"]["canonical_core_sha256"],
            "receipt_candidate_core_sha256": receipt["candidate_core_sha256"],
            "candidate_id_alignment": candidate["candidate_id"] == falsifier["candidate_id"] == receipt["candidate_id"] == CANDIDATE_ID,
            "candidate_core_alignment": candidate["candidate_identity"]["canonical_core_sha256"] == falsifier["candidate_core_sha256"] == receipt["candidate_core_sha256"],
            "falsifier_core_alignment": falsifier["falsifier_identity"]["canonical_core_sha256"] == receipt["falsifier_core_sha256"],
        },
        "authorized_only_after_this_authorization_is_merged": {
            "stage_a_public_source_passage_audit": True,
            "stage_a_source_faithful_constant_derivation_attempt": True,
            "stage_a_branch_classification": True,
            "stage_b_entry_only_if_stage_a_passes": True,
            "stage_b_g_star_freeze_before_margin_evaluation": True,
            "stage_b_exact_interval_margin_evaluation_after_g_star_freeze": True,
            "declarative_planted_world_evaluator_implementation": True,
            "declarative_planted_world_execution": True,
            "seven_field_mathematical_lesson_after_material_result": True,
        },
        "authorized_evidence_boundary": {
            "public_primary_source": {
                "author": "Jonathan J. Wilson",
                "zenodo_version_doi": "10.5281/zenodo.19393832",
                "zenodo_concept_doi": "10.5281/zenodo.19393831",
                "pdf_sha256": "08013e1ce75c8b2be79c62ba61f70e30024b9bb427c465ceab7ee9266236690d",
                "tex_sha256": "ef936e502e84b0cafabc594c9705c16c9c1df29dc95f2a6a679b6b446c526c18",
                "authorized_passages": [
                    "PDF pp.141,145-148,172; equations (566)-(586); Lemmas 40.3-40.4; Theorem 40.5; Definition A.15.3",
                    "TeX lines 9279-9291,9554-9584,9595-9680,9725-9750,11481-11499",
                ],
                "authority": "PRIMARY_AUTHOR_OPEN_ARTIFACT_NOT_INDEPENDENT_PEER_REVIEW",
            },
            "existing_source_audit": _binding(SOURCE_AUDIT),
            "restriction": "Use only the bound public source files and already-public application artifacts; no private correspondence, hidden source, invented constants, or unbound source version.",
        },
        "stage_order_and_fail_close": [
            "Stage A must run first and may return STRONGER_PREMISE_MISMATCH_A or CANNOT_CHECK.",
            "Stage B is unauthorized unless Stage A returns a source-proven pass.",
            "A positive g_star and its source-faithful derivation must be frozen in a separate artifact before Stage B target evaluation.",
            "APPLICABLE_BRIDGE requires both stages; it remains only a local K-coordinate applicability result.",
        ],
        "explicitly_unauthorized": [
            "EVALUATION_BEFORE_THIS_AUTHORIZATION_IS_MERGED_TO_MAIN",
            "CHANGING_CANDIDATE_OR_FALSIFIER_IDENTITY",
            "REINTERPRETING_THE_DISPLAYED_SOURCE_C_WITHOUT_DERIVATION",
            "CHOOSING_HIDDEN_OR_INVENTED_CONSTANT_VALUES",
            "SKIPPING_STAGE_A",
            "SELECTING_G_STAR_AFTER_MARGIN_RESULT_ACCESS",
            "CLAIMING_INDEPENDENT_PEER_REVIEW",
            "CLAIMING_REFUTATION_OF_YANG_MILLS_OR_THE_FULL_SOURCE",
            "CLAIMING_FULL_GRAPH_TRANSFORM_OR_STABLE_MANIFOLD_CLOSURE",
            "CLAIMING_CONTINUUM_CONSTRUCTION_OS_RECONSTRUCTION_OR_MASS_GAP",
        ],
        "current_round_execution_state": {
            "authorization_publication_pending": True,
            "source_proof_evaluation_executed": False,
            "planted_world_evaluator_implemented": False,
            "planted_worlds_executed": False,
            "stage_a_result_accessed": False,
            "stage_b_result_accessed": False,
            "g_star_selected": False,
            "result_classified": False,
        },
        "authority": {
            "licenses_future_scoped_evaluation_after_merge": True,
            "grants_target_truth": False,
            "grants_mathematical_result_credit": False,
            "grants_proof_authority": False,
            "grants_independent_review": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
        "allowed_next_action": "MERGE THIS AUTHORIZATION WITHOUT EVALUATION; only then implement and run the bound evaluator/source audit in a successor result round.",
        "artifact_hash": "",
    }
    core["artifact_hash"] = _sha(core)
    return core


def write_document() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(build_document(), indent=2, sort_keys=True, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_document()
