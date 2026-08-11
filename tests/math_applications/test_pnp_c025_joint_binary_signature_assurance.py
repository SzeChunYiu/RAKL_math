from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
ORACLE = BASE / "05_falsification/joint_binary_signature_calibration.py"
PREREG = BASE / "04_candidates/C025_joint_binary_signature_calibration_preregistration.json"
RECEIPT = BASE / "05_falsification/C025_JOINT_SIGNATURE_CALIBRATION_RECEIPT_20260811.json"


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _load_module():
    spec = importlib.util.spec_from_file_location("pnp_c025_oracle", ORACLE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_c025_preregistration_precedes_and_binds_the_evaluation() -> None:
    prereg = json.loads(PREREG.read_text(encoding="utf-8"))
    payload = copy.deepcopy(prereg)
    payload["artifact_hash"] = ""
    assert prereg["artifact_hash"] == _canonical_hash(payload)
    assert prereg["candidate_id"] == "C025"
    assert prereg["chronology"]["pre_candidate_gate_observation"][
        "candidate_generation_allowed"
    ] is True
    assert prereg["frozen_at"] < "2026-08-12T00:00:00Z"
    assert "P_VS_NP_ROOT_AUTHORITY_NONE" in prereg["authority_ceiling"]

    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    receipt_payload = copy.deepcopy(receipt)
    receipt_payload["artifact_hash"] = ""
    assert receipt["artifact_hash"] == _canonical_hash(receipt_payload)
    assert receipt["bindings"]["preregistration_artifact_hash"] == prereg["artifact_hash"]
    assert receipt["bindings"]["preregistration_file_sha256"] == _file_hash(PREREG)
    assert receipt["bindings"]["executable_file_sha256"] == _file_hash(ORACLE)
    assert receipt["evaluated_at"] > prereg["frozen_at"]


def test_joint_cut_coverage_is_exactly_signature_inequality_on_small_worlds() -> None:
    oracle = _load_module()
    for n_labels in range(2, 5):
        max_bits = math.ceil(math.log2(n_labels))
        for n_bits in range(max_bits + 1):
            for cuts in oracle.iter_cut_families(n_labels, n_bits):
                signatures = oracle.joint_signatures(n_labels, cuts)
                for left in range(n_labels):
                    for right in range(n_labels):
                        if left == right:
                            continue
                        assert oracle.directly_separated(cuts, left, right) == (
                            signatures[left] != signatures[right]
                        )
                assert oracle.direct_full_semifilter_family_cover(
                    n_labels, cuts
                ) == (len(set(signatures)) == n_labels)


def test_counterexample_first_search_and_construction_recover_exact_logarithmic_gate() -> None:
    oracle = _load_module()
    for n_labels in range(2, 5):
        required = (n_labels - 1).bit_length()
        assert oracle.exhaustive_minimum_bits(n_labels) == required
        cuts = oracle.canonical_binary_cuts(n_labels)
        assert len(cuts) == required
        assert oracle.is_covering_family(n_labels, cuts)

    for n_labels in (2, 3, 4, 5, 8, 9, 16, 17):
        required = (n_labels - 1).bit_length()
        assert 2 ** (required - 1) < n_labels <= 2**required
        assert oracle.is_covering_family(
            n_labels, oracle.canonical_binary_cuts(n_labels)
        )


def test_receipt_preserves_low_order_failure_and_scope_ceiling(tmp_path: Path) -> None:
    oracle = _load_module()
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    assert receipt["verdict"] == "PASS_SCOPED_CALIBRATION_WITH_CAPACITY_NO_GO"
    assert all(item["calibration_pass"] for item in receipt["case_results"])
    assert all(item["low_order_collision_forced"] for item in receipt["case_results"])
    assert receipt["capacity_falsifier"]["observed_result"] == (
        "FIRST_ORDER_CARDINALITY_ONLY_ARGUMENT_LOGARITHMICALLY_CAPPED"
    )
    assert receipt["capacity_falsifier"]["route_effect"] == (
        "REJECT_AS_SUPERLOG_PRIMARY_ROUTE_WITHIN_FROZEN_SCOPE"
    )
    assert receipt["full_semifilter_definition_regression"]["all_equivalent"] is True
    assert [item["direct_vs_signature_mismatches"] for item in receipt["full_semifilter_definition_regression"]["results"]] == [0, 0, 0]
    assert receipt["claim_scope"]["higher_order_closure_signatures"] == "NOT_TESTED"
    assert receipt["claim_scope"]["p_vs_np"] == "NO_AUTHORITY"
    assert "COMPUTATION_IS_NOT_PROOF" in receipt["authority"]

    regenerated = tmp_path / "receipt.json"
    oracle.write_receipt(
        preregistration_path=PREREG,
        output_path=regenerated,
        evaluated_at=receipt["evaluated_at"],
    )
    assert regenerated.read_bytes() == RECEIPT.read_bytes()


def test_c025_success_failure_and_method_lesson_are_scoped_and_content_bound() -> None:
    from rakl.failure_lattice import (
        FailureDiagnosisStatus,
        FailureExperience,
        validate_failure_experience,
    )
    from rakl.research_tool_inventory import (
        ResearchTool,
        ResearchToolAuthority,
        validate_research_tool,
    )

    failure_bundle = json.loads(
        (BASE / "07_memory/C025_FAILURE_EXPERIENCE_DELTA_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    raw_failure = failure_bundle["experience"]
    failure_payload = copy.deepcopy(raw_failure)
    failure_payload["artifact_hash"] = ""
    assert raw_failure["artifact_hash"] == _canonical_hash(failure_payload)
    failure = FailureExperience(
        failure_id=raw_failure["failure_id"],
        atom_id=raw_failure["atom_id"],
        candidate_id=raw_failure["candidate_id"],
        context_packet_hash=raw_failure["context_packet_hash"],
        research_trace_event_id=raw_failure["research_trace_event_id"],
        method_family=raw_failure["method_family"],
        failure_mode=raw_failure["failure_mode"],
        residual_signature=tuple(raw_failure["residual_signature"]),
        broken_assumptions=tuple(raw_failure["broken_assumptions"]),
        scope_conditions=tuple(raw_failure["scope_conditions"]),
        competing_diagnoses=tuple(raw_failure["competing_diagnoses"]),
        selected_diagnosis=raw_failure["selected_diagnosis"],
        diagnosis_status=FailureDiagnosisStatus(raw_failure["diagnosis_status"]),
        evidence_pointers=tuple(raw_failure["evidence_pointers"]),
        falsifier_or_attempt=raw_failure["falsifier_or_attempt"],
        observed_result=raw_failure["observed_result"],
        artifact_hash=raw_failure["artifact_hash"],
        timestamp=raw_failure["timestamp"],
        local_repair_attempts=tuple(raw_failure["local_repair_attempts"]),
    )
    assert validate_failure_experience(failure) == ()
    assert failure.diagnosis_status is FailureDiagnosisStatus.SUPPORTED
    assert raw_failure["next_discriminator"]
    assert any("higher-order" in item for item in raw_failure["scope_conditions"])

    lesson = failure_bundle["reusable_method_lesson_candidate"]
    lesson_payload = copy.deepcopy(lesson)
    lesson_payload["artifact_hash"] = ""
    assert lesson["artifact_hash"] == _canonical_hash(lesson_payload)
    assert lesson["status"].startswith("PROPOSAL_ONLY")
    assert "not independently recurrent" in lesson["transport_scope"]
    assert any("CANNOT_CHECK" in item for item in lesson["framework_validation_obligations"])

    raw_tool = json.loads(
        (BASE / "07_memory/C025_RESEARCH_TOOL_DELTA_20260811.json").read_text(
            encoding="utf-8"
        )
    )["tool"]
    tool_payload = copy.deepcopy(raw_tool)
    tool_payload["artifact_hash"] = ""
    assert raw_tool["artifact_hash"] == _canonical_hash(tool_payload)
    tool = ResearchTool(
        tool_id=raw_tool["tool_id"],
        name=raw_tool["name"],
        kind=raw_tool["kind"],
        abstraction=raw_tool["abstraction"],
        source_atom_id=raw_tool["source_atom_id"],
        source_candidate_id=raw_tool["source_candidate_id"],
        source_result_ids=tuple(raw_tool["source_result_ids"]),
        source_context_hash=raw_tool["source_context_hash"],
        authority=ResearchToolAuthority(raw_tool["authority"]),
        preconditions=tuple(raw_tool["preconditions"]),
        structural_signature=tuple(raw_tool["structural_signature"]),
        operation=raw_tool["operation"],
        guaranteed_effects=tuple(raw_tool["guaranteed_effects"]),
        non_guarantees=tuple(raw_tool["non_guarantees"]),
        validation_obligations=tuple(raw_tool["validation_obligations"]),
        evidence_pointers=tuple(raw_tool["evidence_pointers"]),
        known_failure_ids=tuple(raw_tool["known_failure_ids"]),
        successful_reuse_ids=tuple(raw_tool["successful_reuse_ids"]),
        proof_backing=tuple(raw_tool["proof_backing"]),
        artifact_hash=raw_tool["artifact_hash"],
    )
    assert validate_research_tool(tool) == ()
    assert tool.authority is ResearchToolAuthority.VERIFIED_LOCAL
    assert tool.known_failure_ids == ("F-C025-FIRST-ORDER-CANONICAL-COLLAPSE",)
    failure_reconciliation = failure_bundle["identity_reconciliation"]
    assert failure_reconciliation["canonical_failure_id"] == failure.failure_id
    assert failure_reconciliation["parallel_id_disposition"].startswith("NOT_MINTED")
    tool_bundle = json.loads(
        (BASE / "07_memory/C025_RESEARCH_TOOL_DELTA_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    assert tool_bundle["identity_reconciliation"]["canonical_tool_id"] == tool.tool_id
    assert tool_bundle["identity_reconciliation"]["parallel_id_disposition"].startswith(
        "NOT_MINTED"
    )


def test_c025_trace_continuation_is_hash_chained_and_never_promotes_root() -> None:
    from rakl.research_trace import (
        MathResearchTrace,
        ResearchTraceEntry,
        ResearchTraceEventType,
        TraceGateVerdict,
        audit_research_trace,
    )

    parent = json.loads(
        (
            BASE
            / "09_trace/O9d12a2a1a_PRE_CANDIDATE_TRACE_MIGRATION_REPAIRED_20260811.json"
        ).read_text(encoding="utf-8")
    )
    continuation = json.loads(
        (BASE / "09_trace/O9d12a2a1a_C025_TRACE_CONTINUATION_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    assert continuation["parent_trace_id"] == parent["trace_id"]
    assert continuation["trace_id"].endswith("-C025-CONTINUATION")
    assert continuation["parent_terminal_hash"] == parent["entries"][-1]["artifact_hash"]

    previous = ""
    entries = []
    for raw in parent["entries"] + continuation["entries"]:
        assert raw["previous_event_hash"] == previous
        payload = copy.deepcopy(raw)
        payload["artifact_hash"] = ""
        assert raw["artifact_hash"] == _canonical_hash(payload)
        previous = raw["artifact_hash"]
        entries.append(
            ResearchTraceEntry(
                event_id=raw["event_id"],
                atom_id=raw["atom_id"],
                event_type=ResearchTraceEventType(raw["event_type"]),
                timestamp=raw["timestamp"],
                state_summary=raw["state_summary"],
                action_summary=raw["action_summary"],
                evidence_pointers=tuple(raw["evidence_pointers"]),
                alternatives_considered=tuple(raw.get("alternatives_considered", ())),
                decision_rationale=raw.get("decision_rationale", ""),
                outputs=tuple(raw.get("outputs", ())),
                uncertainties=tuple(raw.get("uncertainties", ())),
                residuals=tuple(raw.get("residuals", ())),
                next_steps=tuple(raw.get("next_steps", ())),
                artifact_hash=raw["artifact_hash"],
                previous_event_hash=raw.get("previous_event_hash", ""),
            )
        )
    report = audit_research_trace(
        MathResearchTrace(trace_id=parent["trace_id"], entries=tuple(entries))
    )
    assert report.verdict is TraceGateVerdict.PASS
    assert [entry.event_type for entry in entries[-5:]] == [
        ResearchTraceEventType.CANDIDATE_PROPOSED,
        ResearchTraceEventType.FALSIFIER_RUN,
        ResearchTraceEventType.RESULT_RECORDED,
        ResearchTraceEventType.RESIDUAL_OPENED,
        ResearchTraceEventType.REVIEWED,
    ]
    assert all(entry.event_type is not ResearchTraceEventType.PROMOTED for entry in entries)
    assert "root_status:OPEN_NO_SOLUTION_CERTIFICATE" in entries[-1].outputs

    review = (BASE / "08_reviews/SAME_CONTEXT_RESULT_REVIEW_C025_20260811.md").read_text(
        encoding="utf-8"
    )
    assert "NOT_INDEPENDENT" in review
    assert "ROOT_AUTHORITY_NONE" in review
    assert "provisional parallel capacity failure/tool names: not minted" in review



def test_parallel_assurance_fork_preserves_pre_result_chronology() -> None:
    parent = json.loads(
        (
            BASE
            / "09_trace/O9d12a2a1a_PRE_CANDIDATE_TRACE_MIGRATION_REPAIRED_20260811.json"
        ).read_text(encoding="utf-8")
    )
    fork = json.loads(
        (
            BASE
            / "09_trace/O9d12a2a1a_C025_PARALLEL_ASSURANCE_TRACE_20260811.json"
        ).read_text(encoding="utf-8")
    )
    assert fork["parent_trace_id"] == parent["trace_id"]
    previous = parent["entries"][-1]["artifact_hash"]
    for raw in fork["entries"]:
        assert raw["previous_event_hash"] == previous
        payload = copy.deepcopy(raw)
        payload["artifact_hash"] = ""
        assert raw["artifact_hash"] == _canonical_hash(payload)
        previous = raw["artifact_hash"]
    assert [raw["event_type"] for raw in fork["entries"]] == [
        "CANDIDATE_PROPOSED",
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "REVIEWED",
    ]
    assert fork["entries"][0]["timestamp"] < json.loads(
        RECEIPT.read_text(encoding="utf-8")
    )["evaluated_at"]
    canonical = json.loads(
        (BASE / "09_trace/O9d12a2a1a_C025_TRACE_CONTINUATION_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    assert "parallel_trace:RECONCILED_PRESERVED" in canonical["entries"][-1]["outputs"]

def test_synthesis_receipt_explicitly_reconciles_parallel_lineage() -> None:
    receipt_path = BASE / "05_falsification/C025_SYNTHESIS_RECEIPT_20260811.json"
    synthesis = json.loads(receipt_path.read_text(encoding="utf-8"))
    payload = copy.deepcopy(synthesis)
    payload["artifact_hash"] = ""
    assert synthesis["artifact_hash"] == _canonical_hash(payload)
    assert synthesis["chronology"]["pre_result_registration_commit"] == (
        "03a4cb9a0bce32374d79210d8b712670c11626a7"
    )
    for binding in synthesis["artifact_bindings"].values():
        path = ROOT / binding["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == binding["file_sha256"]

    identities = synthesis["identity_reconciliation"]
    assert identities["canonical_failure_id"] == "F-C025-FIRST-ORDER-CANONICAL-COLLAPSE"
    assert identities["canonical_tool_id"] == "T-PNP-GNEQ-JOINT-SIGNATURE-CALIBRATION"
    assert identities["parallel_provisional_failure_id"]["disposition"].startswith(
        "NOT_MINTED"
    )
    assert identities["parallel_provisional_tool_id"]["disposition"].startswith(
        "NOT_MINTED"
    )
    assert identities["supersession_action"] == "NONE_NO_ACCEPTED_DUPLICATE_ID"
    assert synthesis["claim_scope"]["p_vs_np_root"] == "NO_AUTHORITY"
    assert synthesis["method_lesson"]["framework_transport"].endswith(
        "QUARANTINED_PROPOSAL"
    )
