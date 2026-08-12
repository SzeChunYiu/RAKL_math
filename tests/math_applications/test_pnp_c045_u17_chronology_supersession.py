from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"

ARTIFACTS = {
    "exposure_audit": PNP
    / "09_trace/O9d12a2a1b_C045_U17_PRE_FREEZE_EXPOSURE_AUDIT_20260812.json",
    "receipt_correction": PNP
    / "09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_RECEIPT_V2_CORRECTION_20260812.json",
    "trace_supersession": PNP
    / "09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_TRACE_V2_SUPERSESSION_20260812.json",
    "plan_quarantine": PNP
    / "04_candidates/negative_history/O9d12a2a1b_C045_U17_INCIDENCE_PLAN_V1_POST_EXPOSURE_QUARANTINE_20260812.json",
}

V1_RECEIPT = PNP / "09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_RECEIPT_20260812.json"
V1_TRACE = PNP / "09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_TRACE_20260812.json"
V1_PLAN = PNP / "04_candidates/O9d12a2a1b_C045_U17_INCIDENCE_CLASSIFICATION_PLAN_FREEZE_20260812.json"
V1_EVALUATOR_MANIFEST = PNP / "05_falsification/O9d12a2a1b_C045_U17_INCIDENCE_EVALUATOR_FREEZE_20260812.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_sha256(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _raw_sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _git(*arguments: str, binary: bool = False) -> str | bytes:
    run = subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        text=not binary,
    )
    return run.stdout if binary else run.stdout.strip()


def test_four_versioned_artifacts_are_strictly_self_hashed_and_acyclic() -> None:
    documents = {name: _load(path) for name, path in ARTIFACTS.items()}
    assert set(documents) == {
        "exposure_audit",
        "receipt_correction",
        "trace_supersession",
        "plan_quarantine",
    }
    for document in documents.values():
        assert document["artifact_hash"] == _canonical_sha256(document)
        assert document["full_document_integrity"]["canonicalization"] == (
            "UTF8_JSON_SORT_KEYS_COMPACT_WITH_ARTIFACT_HASH_EMPTY"
        )

    audit_hash = documents["exposure_audit"]["artifact_hash"]
    receipt_hash = documents["receipt_correction"]["artifact_hash"]
    trace_hash = documents["trace_supersession"]["artifact_hash"]
    assert documents["receipt_correction"]["upstream_bindings"] == {
        "exposure_audit_artifact_hash": audit_hash
    }
    assert documents["trace_supersession"]["upstream_bindings"] == {
        "exposure_audit_artifact_hash": audit_hash,
        "receipt_correction_artifact_hash": receipt_hash,
    }
    quarantine_bindings = documents["plan_quarantine"]["upstream_bindings"]
    assert quarantine_bindings == {
        "exposure_audit_artifact_hash": audit_hash,
        "receipt_correction_artifact_hash": receipt_hash,
        "trace_supersession_artifact_hash": trace_hash,
    }


def test_exposure_audit_binds_exact_public_chronology_and_cannot_check_boundary() -> None:
    audit = _load(ARTIFACTS["exposure_audit"])
    assert audit["source_binding"] == {
        "repository": "https://github.com/SzeChunYiu/RAKL_math.git",
        "correction_base_commit": "9d7d167b5ffa398582550a0492a1e895786137d4",
        "framework_pin": "43897d3afaf0038385102d5acc64793c05ec40f0",
        "github_metadata_observed_at": "2026-08-12T01:49:26Z",
    }
    chronology = audit["chronology"]
    assert chronology["earliest_defensible_public_exposure"] == {
        "kind": "GITHUB_PR_CREATED",
        "pr": 228,
        "timestamp": "2026-08-12T01:17:20Z",
        "url": "https://github.com/SzeChunYiu/RAKL_math/pull/228",
    }
    assert chronology["result_signaling_commit"] == {
        "sha": "b8f59bca9609d454612e45a8998e584dad7aa043",
        "authored_at": "2026-08-12T01:09:38Z",
        "committed_at": "2026-08-12T01:09:38Z",
        "subject": "research(pnp): prove C045 G17 block separability upper cover",
        "public_push_time": "CANNOT_CHECK",
    }
    assert chronology["embedded_freezes"] == {
        "plan": "2026-08-12T01:18:28Z",
        "evaluator_manifest": "2026-08-12T01:18:29Z",
        "receipt": "2026-08-12T01:18:31Z",
    }
    exposure = datetime.fromisoformat("2026-08-12T01:17:20Z")
    assert int(
        (datetime.fromisoformat(chronology["embedded_freezes"]["plan"]) - exposure).total_seconds()
    ) == 68
    assert int(
        (datetime.fromisoformat(chronology["embedded_freezes"]["evaluator_manifest"]) - exposure).total_seconds()
    ) == 69
    assert int(
        (datetime.fromisoformat(chronology["embedded_freezes"]["receipt"]) - exposure).total_seconds()
    ) == 71
    assert chronology["candidate_commit"] == {
        "sha": "93a15a994a03482982a0393f521df3e449b4cf2a",
        "committed_at": "2026-08-12T01:29:51Z",
        "subject": "research(pnp): freeze C045 U17 incidence classifier",
    }
    assert chronology["candidate_merge"] == {
        "pull_request": 232,
        "sha": "9b6354da2123cb93ed164bed1628c46fbcf334f6",
        "merged_at": "2026-08-12T01:38:20Z",
        "subject": "research(pnp): freeze C045 U17 incidence classifier (#232)",
    }
    assert audit["verdict"] == "TARGET_EXPOSED_BEFORE_ALL_THREE_EMBEDDED_FREEZES"


def test_correction_distinguishes_session_local_nonexecution_from_project_exposure() -> None:
    correction = _load(ARTIFACTS["receipt_correction"])
    boundary = correction["corrected_chronology"]
    assert boundary["session_local_decoder_imported_or_executed"] is False
    assert boundary["session_local_evaluator_imported_or_executed"] is False
    assert boundary["session_local_target_enumerated"] is False
    assert boundary["project_level_target_exposed_before_freeze"] is True
    assert boundary["candidate_precedes_any_target_access"] is False
    assert boundary["session_local_nonexecution_does_not_restore_target_blindness"] is True
    assert correction["authority"] == {
        "prospective_u17_authority": False,
        "strict_discovery_authority": False,
        "u17_execution_authorized_for_strict_discovery": False,
        "u17_strict_discovery_execution_barred_permanently": True,
        "retrospective_truth_check_allowed": True,
        "retrospective_reproducibility_allowed": True,
        "mathematical_saturation_credit": False,
        "mathematical_result_credit": False,
        "p_vs_np_authority": False,
        "root_status": "OPEN",
    }
    assert correction["review_authority"] == (
        "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW"
    )


def test_historical_result_blind_claims_are_preserved_and_explicitly_superseded() -> None:
    v1_receipt = _load(V1_RECEIPT)
    v1_trace_text = V1_TRACE.read_text(encoding="utf-8")
    assert v1_receipt["chronology"]["candidate_precedes_any_target_access"] is True
    assert v1_receipt["chronology"]["target_output_accessed"] is False
    assert "TARGET_OUTCOME_UNOBSERVED" in v1_trace_text
    assert "result-blind" in v1_trace_text

    supersession = _load(ARTIFACTS["trace_supersession"])
    assert supersession["historical_preservation"]["v1_bytes_preserved"] is True
    assert supersession["supersession"]["supersedes_all_v1_result_blind_assertions"] is True
    assert supersession["supersession"]["replacement_status"] == (
        "POST_EXPOSURE_RETROSPECTIVE_ONLY_U17_NOT_AN_UNTOUCHED_TARGET"
    )
    assert supersession["next_action"] == (
        "FREEZE_A_NEW_CONTEXT_FIRST_CANDIDATE_AND_EVALUATOR_ON_AN_UNTOUCHED_SUCCESSOR_TARGET"
    )
    assert supersession["forbidden_next_actions"] == [
        "DO_NOT_EXECUTE_THE_U17_EVALUATOR_FOR_STRICT_DISCOVERY",
        "DO_NOT_USE_PR_229_AS_PROSPECTIVE_EVIDENCE",
        "DO_NOT_ERASE_OR_REWRITE_V1_HISTORY",
    ]

    historical = supersession["historical_bindings"]
    for name, path in {
        "v1_receipt": V1_RECEIPT,
        "v1_trace": V1_TRACE,
        "v1_plan": V1_PLAN,
        "v1_evaluator_manifest": V1_EVALUATOR_MANIFEST,
    }.items():
        binding = historical[name]
        assert binding["path"] == path.relative_to(ROOT).as_posix()
        assert binding["raw_sha256"] == _raw_sha256(path)
        assert _git("show", f'9b6354da2123cb93ed164bed1628c46fbcf334f6:{binding["path"]}', binary=True) == path.read_bytes()
        assert _git("rev-parse", f'9b6354da2123cb93ed164bed1628c46fbcf334f6:{binding["path"]}') == binding["git_blob_sha"]


def test_quarantine_retains_only_retrospective_value_and_keeps_root_open() -> None:
    quarantine = _load(ARTIFACTS["plan_quarantine"])
    assert quarantine["quarantined_candidate_id"] == "C045-U17-INCIDENCE-CLASSIFICATION-PLAN-v1"
    assert quarantine["disposition"] == (
        "POST_EXPOSURE_RETROSPECTIVE_PLAN_AND_INERT_EVALUATOR_ONLY"
    )
    assert quarantine["retained_value"] == [
        "RETROSPECTIVE_TRUTH_CHECK",
        "RETROSPECTIVE_REPRODUCIBILITY",
        "NEGATIVE_CHRONOLOGY_HISTORY",
    ]
    assert quarantine["retained_authority"] == [
        "RETROSPECTIVE_TRUTH_CHECK",
        "RETROSPECTIVE_REPRODUCIBILITY",
    ]
    assert quarantine["negative_chronology_history_preserved"] is True
    assert quarantine["prohibited_authority"] == [
        "PROSPECTIVE_U17_AUTHORITY",
        "STRICT_DISCOVERY_CREDIT",
        "MATHEMATICAL_SATURATION_CREDIT",
        "MATHEMATICAL_RESULT_CREDIT",
        "P_VS_NP_AUTHORITY",
    ]
    assert quarantine["u17_evaluator_execution"]["strict_discovery_authorized"] is False
    assert quarantine["u17_evaluator_execution"]["strict_discovery_bar_is_permanent"] is True
    assert quarantine["u17_evaluator_execution"]["retrospective_execution_requires_separate_authorization"] is True
    assert quarantine["root_status"] == "OPEN"


@pytest.mark.parametrize("artifact_name", sorted(ARTIFACTS))
def test_substantive_mutation_is_rejected_by_stale_full_content_hash(
    artifact_name: str,
) -> None:
    document = _load(ARTIFACTS[artifact_name])
    declared = document["artifact_hash"]
    document["hostile_mutation"] = "ATTEMPT_TO_REWRITE_CHRONOLOGY"
    assert document["artifact_hash"] == declared
    assert _canonical_sha256(document) != declared
