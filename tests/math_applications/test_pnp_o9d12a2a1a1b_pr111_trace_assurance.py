from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
    audit_research_trace,
)


ROOT = Path(__file__).resolve().parents[2]
TRACE_PATH = Path(
    "research/real_math/millennium/p_vs_np/09_trace/"
    "O9d12a2a1a1b_TRACE_20260811.json"
)
RECEIPT_PATH = Path(
    "research/real_math/millennium/p_vs_np/09_trace/"
    "O9d12a2a1a1b_PR111_TRACE_ASSURANCE_CORRECTION_20260811.json"
)
SCHEMA_PATH = Path("schemas/pnp-o9d12a2a1a1b-trace-assurance-correction.schema.json")
PR111_MERGE = "bd36e1661053a07b53af8f0b8bdf44da7c9d677e"
PR111_TREE = "fb1b9fc53ccb82e1e6b559451517867aaf2b5b55"
TRACE_BLOB = "fd6515efd43d37001057f2857e31acf92c9ef035"
TRACE_RAW_SHA256 = "cb001cd93c808e49355e4edea416fe1e891dcbcfa8fc1ae805642da907f86553"
RUNTIME_REASONS = [
    "trace_entry_2:memory_review_outputs_missing",
    "trace_entry_2:memory_review_warnings_or_uncertainties_missing",
    "trace_entry_4:expert_review_uncertainties_missing",
]
MANDATORY_GAPS = {
    "missing_events": ["ANALOGY_SCAN", "NEXT_STEP_PROPOSED"],
    "out_of_order_events": [
        "EXPERIENCE_MEMORY_REVIEW precedes METHOD_TRANSFER_REVIEW and EXPERT_CONTEXT_REVIEW"
    ],
    "candidate_identity_event": "ABSENT",
}
AUTHORITY_FLAGS = (
    "grants_strict_context_first_discovery_authority",
    "grants_candidate_generation_authority",
    "grants_proof_authority",
    "grants_novelty_authority",
    "grants_p_vs_np_root_authority",
    "grants_independent_review_credit",
    "grants_framework_promotion_authority",
)


def _load(path: Path) -> dict:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: dict) -> str:
    unhashed = copy.deepcopy(value)
    unhashed["artifact_hash"] = ""
    raw = json.dumps(
        unhashed,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _trace(document: dict) -> MathResearchTrace:
    entries = []
    for item in document["entries"]:
        entries.append(
            ResearchTraceEntry(
                event_id=item["event_id"],
                atom_id=item["atom_id"],
                event_type=ResearchTraceEventType(item["event_type"]),
                timestamp=item["timestamp"],
                state_summary=item["state_summary"],
                action_summary=item["action_summary"],
                evidence_pointers=tuple(item["evidence_pointers"]),
                alternatives_considered=tuple(item.get("alternatives_considered", [])),
                decision_rationale=item.get("decision_rationale", ""),
                outputs=tuple(item.get("outputs", [])),
                uncertainties=tuple(item.get("uncertainties", [])),
                residuals=tuple(item.get("residuals", [])),
                next_steps=tuple(item.get("next_steps", [])),
                artifact_hash=item.get("artifact_hash", ""),
                previous_event_hash=item.get("previous_event_hash", ""),
            )
        )
    return MathResearchTrace(document["trace_id"], tuple(entries))


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def test_pr111_trace_failure_is_preserved_without_rewriting_history() -> None:
    historical = _load(TRACE_PATH)
    trace = _trace(historical)
    base = audit_research_trace(trace)
    gate = audit_pre_candidate_trace(
        trace,
        atom_id="O9d12a2a1a1b",
        context_packet_hash=historical["context_hash"],
    )
    assert base.verdict is TraceGateVerdict.FAIL
    assert list(base.reasons) == RUNTIME_REASONS
    assert gate.verdict is TraceGateVerdict.FAIL

    event_types = [item["event_type"] for item in historical["entries"]]
    assert "ANALOGY_SCAN" not in event_types
    assert "NEXT_STEP_PROPOSED" not in event_types
    assert event_types.index("EXPERIENCE_MEMORY_REVIEW") < event_types.index(
        "METHOD_TRANSFER_REVIEW"
    )
    assert event_types.index("EXPERIENCE_MEMORY_REVIEW") < event_types.index(
        "EXPERT_CONTEXT_REVIEW"
    )

    receipt = _load(RECEIPT_PATH)
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    assert receipt["audit"]["runtime_verdict"] == "FAIL"
    assert receipt["audit"]["runtime_reasons"] == RUNTIME_REASONS
    assert receipt["audit"]["mandatory_pre_candidate_gaps"] == MANDATORY_GAPS
    assert receipt["disposition"]["historical_trace_bytes_modified"] is False
    assert receipt["disposition"]["local_recurrence_lemma_may_be_checked_separately"] is True
    assert receipt["disposition"]["strict_rakl_discovery_claim"] == "REJECTED"
    for flag in AUTHORITY_FLAGS:
        assert receipt["authority_contract"][flag] is False

    source = receipt["historical_source_binding"]
    assert source == {
        "repository_url": "https://github.com/SzeChunYiu/RAKL_math.git",
        "commit_sha": PR111_MERGE,
        "tree_sha": PR111_TREE,
        "path": str(TRACE_PATH),
        "git_blob_sha": TRACE_BLOB,
        "raw_sha256": TRACE_RAW_SHA256,
    }
    assert _git("rev-parse", f"{PR111_MERGE}^{{tree}}") == PR111_TREE
    assert _git("rev-parse", f"{PR111_MERGE}:{TRACE_PATH}") == TRACE_BLOB
    raw = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{PR111_MERGE}:{TRACE_PATH}"],
        check=True,
        capture_output=True,
    ).stdout
    assert hashlib.sha256(raw).hexdigest() == TRACE_RAW_SHA256


def test_correction_opens_a_fresh_child_instead_of_backfilling_pr111() -> None:
    receipt = _load(RECEIPT_PATH)
    next_cycle = receipt["required_successor_cycle"]
    assert next_cycle["child_atom_id"] == "O9d12a2a1a1b1"
    assert next_cycle["historical_trace_reuse_for_candidate_gate"] is False
    assert next_cycle["required_pre_candidate_events"] == [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "NEXT_STEP_PROPOSED",
    ]
    assert next_cycle["requires_fresh_plan_math_research_pass"] is True
    assert next_cycle["candidate_generation_before_pass"] == "FORBIDDEN"
