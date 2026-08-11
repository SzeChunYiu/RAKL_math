from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

from rakl.failure_lattice import (
    FailureDiagnosisStatus,
    FailureExperience,
    FailureExperienceLattice,
    FailureLink,
    FailureRelation,
    add_failure_experience,
    add_failure_link,
)
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"
FRAMEWORK_SCHEMAS = ROOT / "framework/RAKL/schemas"
PR34_MERGE = "4838969ecc18a091da79a059b58b8568634289b7"
PR34_PARENT = "8bc7a9cf17adf347e5be13ab61a08a690dda895e"
PR34_TREE = "33613657e6f1545bafa8a56b3680b7a2bc6bf00b"

CONTEXT = BASE / "01_frontier/H4d1a_CONTEXT_FIBER_20260811.json"
OLD_TRACE = BASE / "09_trace/H4d1a_PRE_CANDIDATE_TRACE_20260811.json"
INVALID_CONTINUATION = BASE / "09_trace/H4d1a_CALIBRATION_TRACE_CONTINUATION_20260811.json"
TRACE = BASE / "09_trace/H4d1a_CANONICAL_COMBINED_POST_RESULT_TRACE_20260811.json"
LATTICE = BASE / "07_memory/H4d1a_FAILURE_EXPERIENCE_LATTICE_COMBINED_20260811.json"
SOURCE = BASE / "01_frontier/H4d1a_PRIDHAM_SOURCE_REBINDING_20260811.json"
CORRECTION = BASE / "10_case_study/H4d1a_C001_POSTMERGE_ASSURANCE_CORRECTION_20260811.json"
SOURCE_SCHEMA = ROOT / "schemas/hodge-source-rebinding-receipt.schema.json"
CORRECTION_SCHEMA = ROOT / "schemas/hodge-postmerge-assurance-correction.schema.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _assert_self_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    observed = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert observed == _canonical_hash(payload)
    return observed


def _validate(value: dict, schema_path: Path) -> None:
    schema = _load(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(value)


def _trace_entry(raw: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
        event_id=raw["event_id"], atom_id=raw["atom_id"],
        event_type=ResearchTraceEventType(raw["event_type"]), timestamp=raw["timestamp"],
        state_summary=raw["state_summary"], action_summary=raw["action_summary"],
        evidence_pointers=tuple(raw["evidence_pointers"]),
        alternatives_considered=tuple(raw["alternatives_considered"]),
        decision_rationale=raw["decision_rationale"], outputs=tuple(raw["outputs"]),
        uncertainties=tuple(raw["uncertainties"]), residuals=tuple(raw["residuals"]),
        next_steps=tuple(raw["next_steps"]), artifact_hash=raw["artifact_hash"],
        previous_event_hash=raw["previous_event_hash"],
    )


def _failure(raw: dict) -> FailureExperience:
    return FailureExperience(
        failure_id=raw["failure_id"], atom_id=raw["atom_id"],
        candidate_id=raw["candidate_id"], context_packet_hash=raw["context_packet_hash"],
        research_trace_event_id=raw["research_trace_event_id"],
        method_family=raw["method_family"], failure_mode=raw["failure_mode"],
        residual_signature=tuple(raw["residual_signature"]),
        broken_assumptions=tuple(raw.get("broken_assumptions", [])),
        scope_conditions=tuple(raw["scope_conditions"]),
        competing_diagnoses=tuple(raw["competing_diagnoses"]),
        selected_diagnosis=raw["selected_diagnosis"],
        diagnosis_status=FailureDiagnosisStatus(raw["diagnosis_status"]),
        evidence_pointers=tuple(raw["evidence_pointers"]),
        falsifier_or_attempt=raw["falsifier_or_attempt"], observed_result=raw["observed_result"],
        artifact_hash=raw["artifact_hash"], timestamp=raw["timestamp"],
        local_repair_attempts=tuple(raw.get("local_repair_attempts", [])),
    )


def _source_errors(receipt: dict) -> tuple[str, ...]:
    errors: list[str] = []
    old = receipt["withdrawn_source"]
    current = receipt["current_source"]
    if old["arxiv_id"] != "1112.6001v4" or old["status"] != "WITHDRAWN":
        errors.append("withdrawn predecessor status not preserved")
    if old["superseded_by"] != "1208.3111v4":
        errors.append("withdrawn predecessor successor mismatch")
    if current["arxiv_id"] != "1208.3111v4" or current["status"] != "CURRENT":
        errors.append("current source identity mismatch")
    if current["supersedes"] != "1112.6001v4":
        errors.append("current source does not bind withdrawn predecessor")
    if receipt["authority_rebinding"]["active_primary_source"] != "1208.3111v4":
        errors.append("active authority not rebound to current source")
    if receipt["authority_rebinding"]["historical_source_authority"] != "QUARANTINED_WITHDRAWN_PROVENANCE_ONLY":
        errors.append("withdrawn source not quarantined")
    return tuple(errors)


def test_pr34_subject_bytes_and_invalid_continuation_remain_immutable() -> None:
    subtree = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", f"{PR34_MERGE}:research/real_math/millennium/hodge/deformation"],
        check=True, stdout=subprocess.PIPE, text=True,
    ).stdout.strip()
    assert subtree == PR34_TREE
    paths = subprocess.run(
        ["git", "-C", str(ROOT), "diff", "--name-only", PR34_PARENT, PR34_MERGE, "--", "research/real_math/millennium/hodge/deformation", "tests/math_applications/test_hodge_h4d1a_strict_packet.py", "tests/math_applications/test_hodge_h4d1a_route_pruning.py"],
        check=True, stdout=subprocess.PIPE, text=True,
    ).stdout.splitlines()
    assert paths
    for relative in paths:
        historical = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"{PR34_MERGE}:{relative}"],
            check=True, stdout=subprocess.PIPE,
        ).stdout
        assert historical == (ROOT / relative).read_bytes()

    invalid = _load(INVALID_CONTINUATION)
    schema = _load(FRAMEWORK_SCHEMAS / "math-research-trace.schema.json")
    with pytest.raises(ValidationError):
        Draft202012Validator(schema).validate(invalid)
    invalid_trace = MathResearchTrace(
        trace_id=invalid["trace_id"],
        entries=tuple(_trace_entry(raw) for raw in invalid["entries"]),
    )
    assert audit_pre_candidate_trace(
        invalid_trace, atom_id="H4d1a", context_packet_hash=_load(CONTEXT)["packet_hash"]
    ).verdict is TraceGateVerdict.FAIL


def test_current_pridham_source_is_rebound_and_hostile_status_tampering_fails() -> None:
    receipt = _load(SOURCE)
    _validate(receipt, SOURCE_SCHEMA)
    _assert_self_hash(receipt)
    assert _source_errors(receipt) == ()
    assert "errors in the formulae" in receipt["withdrawn_source"]["withdrawal_reason"]
    assert "Goodwillie's theorem" in receipt["withdrawn_source"]["withdrawal_reason"]
    assert receipt["withdrawn_source"]["retrieved_content_sha256"] == (
        "sha256:d28747db1d530d17cb09aedb68a5d3859c7066da0ff26bb5553511debf14a350"
    )
    assert receipt["current_source"]["title"] == "Semiregularity as a consequence of Goodwillie's theorem"
    assert receipt["current_source"]["retrieval_url"] == (
        "https://export.arxiv.org/api/query?id_list=1208.3111"
    )
    assert receipt["current_source"]["retrieved_content_sha256"] == (
        "sha256:cf35e4d017cfb12c4ab34755485824ec8ab5bf57b1f8761c3b83931951ef4f8a"
    )

    forged = copy.deepcopy(receipt)
    forged["withdrawn_source"]["status"] = "CURRENT"
    assert "withdrawn predecessor status not preserved" in _source_errors(forged)
    forged = copy.deepcopy(receipt)
    forged["authority_rebinding"]["active_primary_source"] = "1112.6001v4"
    assert "active authority not rebound to current source" in _source_errors(forged)


def test_combined_trace_is_schema_valid_hash_chained_and_runtime_valid() -> None:
    raw = _load(TRACE)
    _validate(raw, FRAMEWORK_SCHEMAS / "math-research-trace.schema.json")
    pre = _load(OLD_TRACE)
    continuation = _load(INVALID_CONTINUATION)
    assert raw["entries"] == pre["entries"] + continuation["entries"]
    previous = ""
    entries = []
    for item in raw["entries"]:
        assert item["previous_event_hash"] == previous
        previous = _assert_self_hash(item)
        entries.append(_trace_entry(item))
    trace = MathResearchTrace(trace_id=raw["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(
        trace, atom_id="H4d1a", context_packet_hash=_load(CONTEXT)["packet_hash"]
    ).verdict is TraceGateVerdict.PASS
    assert entries[-1].event_type is ResearchTraceEventType.RESIDUAL_OPENED
    assert entries[-1].atom_id == "H4d1b"


def test_combined_failure_lattice_reconstructs_with_supported_typed_link() -> None:
    raw = _load(LATTICE)
    _validate(raw, FRAMEWORK_SCHEMAS / "failure-experience-lattice.schema.json")
    parent = _load(BASE / "07_memory/H4d1a_FAILURE_EXPERIENCE_LATTICE_20260811.json")
    child = _load(BASE / "07_memory/H4d1a_FAILURE_EXPERIENCE_DELTA_20260811.json")
    assert raw["experiences"] == parent["experiences"] + child["experiences"]
    lattice = FailureExperienceLattice()
    for item in raw["experiences"]:
        _assert_self_hash(item)
        lattice = add_failure_experience(lattice, _failure(item))
    for item in raw["links"]:
        lattice = add_failure_link(
            lattice,
            FailureLink(
                source_id=item["source_id"], target_id=item["target_id"],
                relation=FailureRelation(item["relation"]), rationale=item["rationale"],
                evidence_pointers=tuple(item.get("evidence_pointers", [])),
            ),
        )
    assert {item.failure_id for item in lattice.experiences} == {
        "F-H4D1-DETECTOR-KERNEL-GAP", "F-H4D1A-SAME-DETECTOR-BRANCH-NOGO"
    }
    assert len(lattice.links) == 1
    assert lattice.links[0].source_id == "F-H4D1A-SAME-DETECTOR-BRANCH-NOGO"
    assert lattice.links[0].target_id == "F-H4D1-DETECTOR-KERNEL-GAP"
    assert lattice.links[0].relation is FailureRelation.CONTEXT_SPECIALIZATION_OF


def test_postmerge_correction_downgrades_episode_and_blocks_h4d1b_candidate() -> None:
    receipt = _load(CORRECTION)
    _validate(receipt, CORRECTION_SCHEMA)
    _assert_self_hash(receipt)
    assert receipt["historical_git_bindings"] == {
        "pr34_merge": PR34_MERGE,
        "pr34_first_parent": PR34_PARENT,
        "pr34_hodge_subtree": PR34_TREE,
        "framework_pin": "bd1a2768f0f474ff44ffa25243241f94bfaf6466",
    }
    assert (
        "sha256:1c3d58c35c05024bee06f0505de102e4df12db8b0340c06a02121769d1c365f2"
        in receipt["evidence_pointers"]
    )
    assert receipt["historical_episode_classification"] == {
        "classification": "LEGACY_NON_V3_RETROSPECTIVE_ROUTE_PRUNING",
        "canonical_task_episode_present": False,
        "strict_discovery_credit": "NONE",
        "retrospective_backfill_allowed": False,
    }
    assert receipt["h4d1b_gate"]["candidate_generation_allowed"] is False
    assert receipt["h4d1b_gate"]["required_before_candidate"] == [
        "fresh H4d1b context fiber with current source binding",
        "fresh dual-memory review bound to combined failure lattice",
        "fresh seven-event pre-candidate trace",
        "role-separated same-context expert review",
    ]
    assert receipt["mathematical_scope"]["retained_result"] == (
        "FIRST_ORDER_SAME_DETECTOR_PROPER_NONZERO_NOGO"
    )
    assert receipt["mathematical_scope"]["hodge_root_authority"] == "NONE"
    candidate_files = list((BASE / "04_candidates").glob("*H4d1b*")) if (BASE / "04_candidates").exists() else []
    assert candidate_files == []
