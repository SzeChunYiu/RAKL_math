"""Versioned correction for the retrospective U8 exact finite-LP replay.

V1 and its same-context review remain immutable failed history.  This V2 binds
their bytes, repairs chronology and Git provenance, and keeps the regenerated
17/20 certificate separate from the still-missing externally reported 21/24
certificates.  It grants no theorem, asymptotic, novelty, P-vs-NP, independent
review, or strict context-first discovery authority.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
V1_REPLAY = PNP / "05_falsification/c034b_u8_retrospective_replay.py"
V2_SCHEMA = ROOT / "schemas/pnp-c034b-u8-retrospective-v2-correction.schema.json"

SOURCE_INTRO = "e923f658f62c4e0eedfde090522feb7b9569c87e"
ASSESSMENT_INTRO = "569559e0787d09c2979cbfc2d209fc0bdaab889f"
APPLICATION_BASE = "1d248204b35426695419f1a5a477e49cf163d39b"
V1_RESULT_COMMIT = "b23a081eb875f6492172e6a93b2fa9bdef0deb67"
V1_REVIEW_COMMIT = "abc704ac780b56c84faeb34cdeafd21ce96dccef"
INTEGRATED_BASE = "0fee64d32a5697ac678c65b97e9d61b2700f0a23"


class BindingFailure(Exception):
    """A bounded, public Git-binding failure reason."""


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def _git(*arguments: str, binary: bool = False) -> str | bytes:
    run = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=not binary,
    )
    return run.stdout if binary else run.stdout.strip()


def _v1_module():
    spec = importlib.util.spec_from_file_location("c034b_u8_v1_frozen", V1_REPLAY)
    if spec is None or spec.loader is None:
        raise RuntimeError("V1 replay loader unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _historical_binding(path: str, commit: str, blob: str, raw_sha256: str) -> dict:
    return {
        "path": path,
        "commit": commit,
        "git_blob_sha": blob,
        "raw_sha256": "sha256:" + raw_sha256,
    }


def audit_git_bindings(receipt: dict) -> dict[str, object]:
    """Fail-closed audit of the exact historical source/provenance relations."""

    required = {
        "application_base_commit",
        "application_base_tree",
        "source_introduction_commit",
        "source_introduction_tree",
        "source_path",
        "source_git_blob_sha",
        "source_raw_sha256",
        "assessment_introduction_commit",
        "assessment_introduction_tree",
        "assessment_path",
        "assessment_git_blob_sha",
        "assessment_raw_sha256",
        "assessment_artifact_hash",
        "v1_result_commit",
        "integrated_base_commit",
        "integrated_base_tree",
    }
    source = receipt.get("source_binding")
    if not isinstance(source, dict) or not required.issubset(source):
        return {"verdict": "CANNOT_CHECK", "reason": "MISSING_GIT_BINDING_FIELDS"}

    def require(condition: bool, reason: str) -> None:
        if not condition:
            raise BindingFailure(reason)

    try:
        require(
            _git("rev-parse", f'{source["application_base_commit"]}^{{tree}}')
            == source["application_base_tree"],
            "APPLICATION_BASE_TREE_MISMATCH",
        )
        require(
            _git("rev-parse", f'{source["source_introduction_commit"]}^{{tree}}')
            == source["source_introduction_tree"],
            "SOURCE_INTRODUCTION_TREE_MISMATCH",
        )
        require(
            _git("rev-parse", f'{source["assessment_introduction_commit"]}^{{tree}}')
            == source["assessment_introduction_tree"],
            "ASSESSMENT_INTRODUCTION_TREE_MISMATCH",
        )
        require(
            _git("rev-parse", f'{source["integrated_base_commit"]}^{{tree}}')
            == source["integrated_base_tree"],
            "INTEGRATED_BASE_TREE_MISMATCH",
        )
        for older, newer, reason in (
            (source["source_introduction_commit"], source["application_base_commit"], "SOURCE_NOT_ANCESTOR_OF_APPLICATION_BASE"),
            (source["assessment_introduction_commit"], source["application_base_commit"], "ASSESSMENT_NOT_ANCESTOR_OF_APPLICATION_BASE"),
            (source["application_base_commit"], source["v1_result_commit"], "APPLICATION_BASE_NOT_ANCESTOR_OF_V1_RESULT"),
            (source["v1_result_commit"], source["integrated_base_commit"], "V1_RESULT_NOT_ANCESTOR_OF_INTEGRATED_BASE"),
        ):
            require(_git("merge-base", "--is-ancestor", older, newer) == "", reason)

        source_intro_blob = _git(
            "rev-parse", f'{source["source_introduction_commit"]}:{source["source_path"]}'
        )
        require(source_intro_blob == source["source_git_blob_sha"], "SOURCE_BLOB_MISMATCH")
        require(
            _git("rev-parse", f'{source["application_base_commit"]}:{source["source_path"]}')
            == source_intro_blob,
            "SOURCE_CHANGED_BEFORE_APPLICATION_BASE",
        )
        source_raw = _git(
            "show", f'{source["application_base_commit"]}:{source["source_path"]}', binary=True
        )
        require(isinstance(source_raw, bytes), "SOURCE_RAW_UNAVAILABLE")
        require(
            "sha256:" + hashlib.sha256(source_raw).hexdigest() == source["source_raw_sha256"]
            and source_raw == (ROOT / source["source_path"]).read_bytes(),
            "SOURCE_RAW_SHA256_MISMATCH",
        )

        assessment_intro_blob = _git(
            "rev-parse",
            f'{source["assessment_introduction_commit"]}:{source["assessment_path"]}',
        )
        require(
            assessment_intro_blob == source["assessment_git_blob_sha"],
            "ASSESSMENT_BLOB_MISMATCH",
        )
        require(
            _git(
                "rev-parse",
                f'{source["application_base_commit"]}:{source["assessment_path"]}',
            )
            == assessment_intro_blob,
            "ASSESSMENT_CHANGED_BEFORE_APPLICATION_BASE",
        )
        assessment_raw = _git(
            "show",
            f'{source["application_base_commit"]}:{source["assessment_path"]}',
            binary=True,
        )
        require(isinstance(assessment_raw, bytes), "ASSESSMENT_RAW_UNAVAILABLE")
        assessment_value = json.loads(assessment_raw)
        require(
            "sha256:" + hashlib.sha256(assessment_raw).hexdigest()
            == source["assessment_raw_sha256"]
            and assessment_raw == (ROOT / source["assessment_path"]).read_bytes()
            and assessment_value.get("artifact_hash") == source["assessment_artifact_hash"],
            "ASSESSMENT_RAW_OR_ARTIFACT_HASH_MISMATCH",
        )
    except BindingFailure as exc:
        return {"verdict": "FAIL", "reason": str(exc)}
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        return {"verdict": "FAIL", "reason": "GIT_BINDING_AUDIT_ERROR", "detail": type(exc).__name__}
    return {"verdict": "PASS", "checked_relations": 14}


def build_receipt() -> dict[str, object]:
    v1 = _v1_module()
    source_binding = {
        "repository_url": "https://github.com/SzeChunYiu/RAKL_math.git",
        "application_base_commit": APPLICATION_BASE,
        "application_base_tree": "3a9a94633603a7795b684bdefd0d91c31635c6fc",
        "source_introduction_commit": SOURCE_INTRO,
        "source_introduction_tree": "3ae7195e633a67a69820db35a5edc80842e75f56",
        "source_path": "research/real_math/millennium/p_vs_np/00_sources/RAKL_PVSNP_C034_C040_EXTERNAL_LEDGER_20260811.md",
        "source_git_blob_sha": "f97f7183e61313e0e43d4a8f9b27ba8dcff64671",
        "source_raw_sha256": "sha256:3db396674e15231f7cda79964d20c252ef99f6cd9058f20aa27173376075429d",
        "assessment_introduction_commit": ASSESSMENT_INTRO,
        "assessment_introduction_tree": "73bff7e3b9d8c6bd53ea1402b1f7f4db386f4a0b",
        "assessment_path": "research/real_math/millennium/p_vs_np/08_reviews/C034_C040_EXTERNAL_LEDGER_ASSESSMENT_20260811.json",
        "assessment_git_blob_sha": "7ebbbfaa75fd2744a77295a31889edc2c325b8c4",
        "assessment_raw_sha256": "sha256:c64edcf80f2048562182c16a32d5f58416324f3a5c876a430f96902af095cae5",
        "assessment_artifact_hash": "sha256:31c75fcccae6866eb0464dbd661b02ad0312f535de4944b2400194ce522ec14b",
        "v1_result_commit": V1_RESULT_COMMIT,
        "integrated_base_commit": INTEGRATED_BASE,
        "integrated_base_tree": "5d312e9d26d28e312ffd1932b9a2ee460097c2bd",
        "target_exposed_before_replay": True,
    }
    receipt: dict[str, object] = {
        "schema_version": "2.0.0",
        "receipt_id": "PNP-C034B-U8-RETROSPECTIVE-EXACT-REPLAY-V2-CORRECTION-20260811",
        "recorded_at": "2026-08-11T15:48:41Z",
        "framework_pin": "9027cc6beab7e935d714bbdf8e902b89b50caaa8",
        "correction_base_commit": INTEGRATED_BASE,
        "correction_implementation": {
            "path": str(Path(__file__).resolve().relative_to(ROOT)),
            "raw_sha256": "sha256:" + hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "correction_schema": {
            "path": str(V2_SCHEMA.relative_to(ROOT)),
            "raw_sha256": "sha256:" + hashlib.sha256(V2_SCHEMA.read_bytes()).hexdigest(),
        },
        "supersession": {
            "supersedes_receipt_id": "PNP-C034B-U8-RETROSPECTIVE-EXACT-REPLAY-20260811",
            "historical_bytes_preserved": True,
            "v1_review_preserved_as_failed_history": True,
            "blocking_reasons": [
                "V1 recorded_at is 8078 seconds after the commit containing V1",
                "V1 schema accepts integer and terminal-LF artifact hashes",
                "V1 tests do not execute the application-base/source/prior-assessment Git bindings",
            ],
        },
        "superseded_v1_bindings": {
            "receipt": {
                **_historical_binding(
                    "research/real_math/millennium/p_vs_np/05_falsification/C034B_U8_RETROSPECTIVE_REPLAY_RECEIPT_20260811.json",
                    V1_RESULT_COMMIT,
                    "f81a8a4a01655c5d656ab4624a50dfcd8e80d830",
                    "679c834889e65b364ec9df40b5673280b7e064d7afb4247b7f7d722fc81a6ee0",
                ),
                "artifact_hash": "sha256:90876b5870687e5657cfe6689c887866f6366fd8c05933fd6554b4e8dcc6c43b",
            },
            "implementation": _historical_binding(
                "research/real_math/millennium/p_vs_np/05_falsification/c034b_u8_retrospective_replay.py",
                V1_RESULT_COMMIT,
                "431f5a611bed4f8803347c38906a76fec9665472",
                "6305b6013909c2659c88b96eee445f625b1f7543b55a5fa22c56378e2a634ac6",
            ),
            "schema": _historical_binding(
                "schemas/pnp-c034b-u8-retrospective-replay.schema.json",
                V1_RESULT_COMMIT,
                "e4bd8e46d09f3987fa49176e7278fe1af5c3fdfe",
                "491c48cc0984cd7205bad0080758d7df8b85133a63bcac5676bea715b81ebbda",
            ),
            "test": _historical_binding(
                "tests/math_applications/test_pnp_c034b_u8_retrospective_replay.py",
                V1_RESULT_COMMIT,
                "11f9aca701d06c42e843dec7496893edad5a2660",
                "a90ae2b4ebb169ed881b319fc4637c68980086468d417802f774126eae1c22e4",
            ),
            "review": _historical_binding(
                "research/real_math/millennium/p_vs_np/08_reviews/C034B_U8_RETROSPECTIVE_HOSTILE_REVIEW_20260811.md",
                V1_REVIEW_COMMIT,
                "8fa93bd911f65e6f23682dbc3a2a64648f227c28",
                "f1486cbf1091fbfeca966927a651e7239c56ac3b6dc23569e8a97bb45f734af3",
            ),
        },
        "chronology_correction": {
            "source_introduction_time": "2026-08-11T15:50:53+02:00",
            "assessment_introduction_time": "2026-08-11T15:54:43+02:00",
            "application_base_commit_time": "2026-08-11T17:07:02+02:00",
            "v1_result_commit_time": "2026-08-11T17:20:22+02:00",
            "v1_review_commit_time": "2026-08-11T17:24:44+02:00",
            "integrated_base_commit_time": "2026-08-11T17:42:36+02:00",
            "v1_recorded_at": "2026-08-11T17:35:00+00:00",
            "v1_future_offset_seconds": 8078,
            "v1_chronology_verdict": "INVALID_FUTURE_RELATIVE_TO_CONTAINING_COMMIT",
            "v2_chronology_verdict": "REALIZABLE_AFTER_INTEGRATED_BASE",
        },
        "source_binding": source_binding,
        "object_qoi_context": {
            "object": "the reconstructed finite full-semi-filter fractional cover LP induced by U8",
            "qoi": "exact optimum of that source-bound reconstructed finite evaluator",
            "evidence_boundary": "retrospective regeneration after the target 49/24 and reported 21/24 support counts were exposed",
        },
        "certificate_boundary": {
            "regenerated_primal_support": 17,
            "regenerated_dual_support": 20,
            "ledger_reported_primal_support": 21,
            "ledger_reported_dual_support": 24,
            "interpretation": "DIFFERENT_MATCHING_CERTIFICATE_REPRESENTATION_NOT_ORIGINAL_CERTIFICATE_RECOVERY",
        },
        "validation_worlds": {},
        "claim_update": {
            "v1_receipt_status": "SUPERSEDED_BY_V2_CORRECTION_FAILED_HISTORY_RETAINED",
            "reconstructed_finite_lp_status": "RETROSPECTIVE_EXACT_REPLAY_PASS_SOURCE_AND_CHRONOLOGY_BOUND",
            "reported_external_certificate_status": "STILL_MISSING_NOT_REPRODUCED",
            "reported_external_support_counts_status": "UNVERIFIED_21_PRIMAL_24_DUAL",
            "root_status": "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE",
        },
        "review_authority": "SAME_CONTEXT_INTERNAL_CORRECTION_NOT_INDEPENDENT_PEER_REVIEW",
        "authority_contract": {
            "grants_proof_authority": False,
            "grants_p_vs_np_root_authority": False,
            "grants_theorem_authority": False,
            "grants_asymptotic_authority": False,
            "grants_novelty_authority": False,
            "grants_review_independence": False,
            "grants_strict_rakl_discovery_credit": False,
            "promotes_missing_external_certificate": False,
        },
        "residuals": [
            "recover the original external 21-primal and 24-dual certificates and their verifier receipts",
            "formally or independently assure the C034a reduction before extending beyond the reconstructed full-union LP",
            "obtain isolated external review before stronger finite-claim promotion",
        ],
        "artifact_hash": "",
    }
    planted = copy.deepcopy(receipt)
    planted["source_binding"]["source_raw_sha256"] = "sha256:" + "0" * 64
    structural = copy.deepcopy(receipt)
    del structural["source_binding"]["application_base_commit"]
    receipt["validation_worlds"] = {
        "finite_replay_pass": v1.verify_world(v1.pass_world()),
        "finite_replay_planted_fail": v1.verify_world(v1.planted_fail_world()),
        "git_binding_pass": audit_git_bindings(receipt),
        "planted_fail": audit_git_bindings(planted),
        "structural_cannot_check": audit_git_bindings(structural),
    }
    receipt["artifact_hash"] = _canonical_hash(receipt)
    return receipt


def main() -> None:
    print(json.dumps(build_receipt(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
