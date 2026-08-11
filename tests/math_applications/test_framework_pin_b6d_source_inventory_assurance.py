from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema
from rakl.pre_action_receipt import (
    PreActionFibreReceipt,
    RejectedRetrieval,
    RetrievalAuthority,
    SelectedRetrieval,
    gate_consequential_operator_execution,
)

ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework/RAKL"
RECEIPT = ROOT / "receipts/framework-pin-sync-b6d0326-20260811.json"
SCHEMA = ROOT / "schemas/framework-pin-sync-b6d0326-receipt.schema.json"
PRE_ACTION = ROOT / (
    "research/real_math/millennium/p_vs_np/09_trace/"
    "O9d12a2a1a1b1_SOURCE_INVENTORY_R1_PRE_ACTION_20260811.json"
)
R1_RESULT = ROOT / (
    "research/real_math/millennium/p_vs_np/01_frontier/"
    "O9d12a2a1a1b1_SOURCE_NATIVE_THEOREM_INVENTORY_R1_20260811.json"
)


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(cwd), *args],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()


def _pre_action(value: dict) -> PreActionFibreReceipt:
    return PreActionFibreReceipt(
        receipt_id=value["receipt_id"],
        framework_repository=value["framework_repository"],
        framework_commit=value["framework_commit"],
        application_repository=value["application_repository"],
        application_commit=value["application_commit"],
        task_id=value["task_id"],
        atom_id=value["atom_id"],
        context_hash=value["context_hash"],
        fibre_snapshot_hash=value["fibre_snapshot_hash"],
        operator_ids=tuple(value["operator_ids"]),
        selected_retrievals=tuple(
            SelectedRetrieval(
                item["retrieval_id"],
                RetrievalAuthority(item["authority"]),
                item["payload_hash"],
            )
            for item in value["selected_retrievals"]
        ),
        rejected_retrievals=tuple(
            RejectedRetrieval(item["retrieval_id"], item["rejection_reason"])
            for item in value["rejected_retrievals"]
        ),
        predeclared_discriminator=value["predeclared_discriminator"],
        allowed_outcome_branches=tuple(value["allowed_outcome_branches"]),
        frozen_at_utc=value["frozen_at_utc"],
        sequence_index=value["sequence_index"],
        schema_version=value["schema_version"],
    )


def test_b6d_framework_sync_receipt_is_exact_non_authorizing_and_integrated() -> None:
    receipt = _load(RECEIPT)
    schema = _load(SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(receipt)
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    delta = receipt["framework_delta"]
    # This receipt is historical after a later pin refresh.  Preserve and audit
    # the exact b6d object instead of coupling it to today's live gitlink.
    assert _git(
        FRAMEWORK, "cat-file", "-e", f'{delta["current_commit"]}^{{commit}}'
    ) == ""
    assert _git(
        FRAMEWORK, "rev-parse", f'{delta["current_commit"]}^{{tree}}'
    ) == delta["current_tree"]
    assert int(
        _git(
            FRAMEWORK,
            "rev-list",
            "--count",
            f'{delta["previous_commit"]}..{delta["current_commit"]}',
        )
    ) == delta["commits_between"]
    assert len(
        _git(
            FRAMEWORK,
            "diff",
            "--name-only",
            delta["previous_commit"],
            delta["current_commit"],
        ).splitlines()
    ) == delta["changed_files"]
    assert _git(ROOT, "show", "-s", "--format=%P", receipt["application_integration"]["integration_merge_commit"]).split() == [
        receipt["application_integration"]["pre_merge_head"],
        receipt["application_integration"]["live_origin_main"],
    ]
    assert not any(receipt["authority_contract"].values())
    assert receipt["compatibility_repair"]["historical_artifacts_rewritten"] is False
    assert receipt["compatibility_repair"]["current_storage_admission_gate_weakened"] is False


def test_latest_gate_replay_is_allowed_but_cannot_backfill_latest_process_credit() -> None:
    receipt = _load(RECEIPT)
    raw = PRE_ACTION.read_bytes()
    pre = json.loads(raw)
    binding = receipt["pre_action_gate_replay"]
    assert binding["historical_receipt_raw_sha256"] == (
        "sha256:" + hashlib.sha256(raw).hexdigest()
    )
    historical = _pre_action(pre)
    assert binding["historical_receipt_canonical_sha256"] == (
        "sha256:" + historical.receipt_canonical_sha256
    )
    report = gate_consequential_operator_execution(
        historical,
        intended_operator_id=binding["intended_operator_id"],
        intended_fibre_snapshot_hash=pre["fibre_snapshot_hash"],
        intended_falsifier=pre["predeclared_discriminator"],
        intended_atom_id=pre["atom_id"],
        intended_context_hash=pre["context_hash"],
        intended_task_id=pre["task_id"],
    )
    assert report.verdict.value == binding["verdict"] == "ALLOWED"
    assert list(report.reasons) == binding["reasons"]
    assert report.may_execute is binding["may_execute"] is True
    assert binding["original_execution_used_latest_gate"] is False
    assert binding["strict_latest_process_credit"] is False
    assert binding["prospective_r2_requires_fresh_gate_and_root_preservation_receipt"] is True
    assert report.grants_prospective_or_theorem_authority is False

    r1 = _load(R1_RESULT)
    assert r1["artifact_hash"] == receipt["historical_r1_result_binding"]["artifact_hash"]
    assert r1["framework"]["commit"] == receipt["historical_r1_result_binding"][
        "framework_commit"
    ]
    assert r1["root_status"] == "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE"
