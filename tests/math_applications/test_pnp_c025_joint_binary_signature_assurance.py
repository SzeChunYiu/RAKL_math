from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
ORACLE = BASE / "05_falsification/joint_binary_signature_calibration.py"
PREREG = BASE / "04_candidates/C025_joint_binary_signature_calibration_preregistration.json"
RECEIPT = BASE / "05_falsification/C025_JOINT_SIGNATURE_CALIBRATION_RECEIPT_20260811.json"
CHRONOLOGY_AUDIT = (
    BASE
    / "04_candidates/negative_history/C025_RETROSPECTIVE_ASSURANCE_CHRONOLOGY_AUDIT_20260811.json"
)
POSTRESULT_ADDENDUM = BASE / "07_memory/C025_POSTRESULT_ASSURANCE_ADDENDUM_20260811.json"
SYNTHESIS_RECEIPT = BASE / "05_falsification/C025_SYNTHESIS_RECEIPT_20260811.json"


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


def _git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=check,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def _git_provenance_errors(receipt: dict[str, object]) -> tuple[str, ...]:
    provenance = receipt["git_provenance"]
    assert isinstance(provenance, dict)
    errors: list[str] = []

    anchor = provenance["integration_anchor_commit"]
    assert isinstance(anchor, str)
    if _git("cat-file", "-e", f"{anchor}^{{commit}}", check=False).returncode != 0:
        errors.append("integration anchor commit is missing")
        return tuple(errors)

    merge = provenance["provenance_merge"]
    assert isinstance(merge, dict)
    merge_commit = merge["commit"]
    assert isinstance(merge_commit, str)
    if _git("cat-file", "-e", f"{merge_commit}^{{commit}}", check=False).returncode != 0:
        errors.append("provenance merge commit is missing")
    else:
        observed_tree = _git("rev-parse", f"{merge_commit}^{{tree}}").stdout.decode().strip()
        if observed_tree != merge["tree"]:
            errors.append("provenance merge tree mismatch")
        observed_parents = _git("show", "-s", "--format=%P", merge_commit).stdout.decode().split()
        if observed_parents != merge["parents"]:
            errors.append("provenance merge parents mismatch")
        first_parent_tree = _git("rev-parse", f"{merge_commit}^1^{{tree}}").stdout.decode().strip()
        if first_parent_tree != merge["first_parent_tree"]:
            errors.append("provenance first-parent tree mismatch")
        if observed_tree != first_parent_tree:
            errors.append("provenance merge imported result-tree content")

    required = provenance["required_ancestors"]
    assert isinstance(required, dict)
    for role, commit in required.items():
        assert isinstance(role, str) and isinstance(commit, str)
        if _git("cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode != 0:
            errors.append(f"required ancestor commit missing: {role}")
            continue
        if _git("merge-base", "--is-ancestor", commit, anchor, check=False).returncode != 0:
            errors.append(f"required ancestor not durable: {role}")

    bindings = provenance["historical_blob_bindings"]
    assert isinstance(bindings, dict)
    for role, binding in bindings.items():
        assert isinstance(role, str) and isinstance(binding, dict)
        commit = binding["commit"]
        path = binding["path"]
        assert isinstance(commit, str) and isinstance(path, str)
        if _git("cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode != 0:
            errors.append(f"historical commit missing: {role}")
            continue
        tree = _git("rev-parse", f"{commit}^{{tree}}").stdout.decode().strip()
        if tree != binding["tree"]:
            errors.append(f"historical tree mismatch: {role}")
        blob_probe = _git("rev-parse", f"{commit}:{path}", check=False)
        if blob_probe.returncode != 0:
            errors.append(f"historical path missing: {role}")
            continue
        if blob_probe.stdout.decode().strip() != binding["git_blob_sha"]:
            errors.append(f"historical blob mismatch: {role}")
        raw = _git("show", f"{commit}:{path}").stdout
        if "sha256:" + hashlib.sha256(raw).hexdigest() != binding["raw_sha256"]:
            errors.append(f"historical raw hash mismatch: {role}")

    preservation = provenance["canonical_target_preservation"]
    assert isinstance(preservation, dict)
    for role, binding in preservation.items():
        assert isinstance(role, str) and isinstance(binding, dict)
        source = _git("show", f'{binding["source_commit"]}:{binding["path"]}').stdout
        current = (ROOT / binding["path"]).read_bytes()
        if source != current:
            errors.append(f"canonical target bytes changed: {role}")
        if "sha256:" + hashlib.sha256(current).hexdigest() != binding["raw_sha256"]:
            errors.append(f"canonical target raw hash mismatch: {role}")
        blob = _git("rev-parse", f'{binding["source_commit"]}:{binding["path"]}').stdout.decode().strip()
        if blob != binding["git_blob_sha"]:
            errors.append(f"canonical target blob mismatch: {role}")
    return tuple(errors)


def test_c025_case_plan_precedes_result_but_does_not_freeze_evaluator_identity() -> None:
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

    audit = json.loads(CHRONOLOGY_AUDIT.read_text(encoding="utf-8"))
    audit_payload = copy.deepcopy(audit)
    audit_payload["artifact_hash"] = ""
    assert audit["artifact_hash"] == _canonical_hash(audit_payload)
    assert audit["registration"]["commit"] == (
        "03a4cb9a0bce32374d79210d8b712670c11626a7"
    )
    assert audit["registration"]["evaluator_present_at_commit"] is False
    assert audit["registration"]["evaluator_bytes_or_hash_frozen"] is False
    assert audit["result_source"]["commit"] == (
        "1bfad13d82548fe61f70cd9f18828fe0240c8556"
    )
    assert audit["ancestry"]["registration_is_ancestor_of_result"] is False
    assert audit["ancestry"]["result_is_ancestor_of_integration_head"] is True
    assert "RETROSPECTIVE_EXECUTABLE_ASSURANCE" in audit["disposition"]


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
    assert any("higher-order" in item for item in raw_failure["scope_conditions"])

    addendum = json.loads(POSTRESULT_ADDENDUM.read_text(encoding="utf-8"))
    addendum_payload = copy.deepcopy(addendum)
    addendum_payload["artifact_hash"] = ""
    assert addendum["artifact_hash"] == _canonical_hash(addendum_payload)
    assert addendum["lineage"]["immutable_parent_failure_artifact_hash"] == (
        raw_failure["artifact_hash"]
    )
    lesson = addendum["method_lesson_candidate"]
    assert lesson["status"].startswith("PROPOSAL_ONLY")
    assert "not independently recurrent" in lesson["transport_scope"]
    assert any("CANNOT_CHECK" in item for item in lesson["validation_obligations"])

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
    assert addendum["lineage"]["immutable_parent_tool_artifact_hash"] == (
        tool.artifact_hash
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



def test_parallel_assurance_trace_is_retrospective_and_preserves_failed_chronology() -> None:
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
        "RESULT_RECORDED",
        "EXPERIENCE_MEMORY_REVIEW",
        "REVIEWED",
    ]
    assert all(
        raw["event_type"] not in {"CANDIDATE_PROPOSED", "FALSIFIER_RUN", "PROMOTED"}
        for raw in fork["entries"]
    )
    assert fork["source_lineage"]["strict_preregistration_authority"] is False
    assert fork["source_lineage"]["result_commit"] == (
        "1bfad13d82548fe61f70cd9f18828fe0240c8556"
    )
    canonical = json.loads(
        (BASE / "09_trace/O9d12a2a1a_C025_TRACE_CONTINUATION_20260811.json").read_text(
            encoding="utf-8"
        )
    )
    assert "parallel_trace:RETROSPECTIVE_RECONCILED" in canonical["entries"][-1]["outputs"]

def test_synthesis_receipt_explicitly_reconciles_parallel_lineage() -> None:
    synthesis = json.loads(SYNTHESIS_RECEIPT.read_text(encoding="utf-8"))
    payload = copy.deepcopy(synthesis)
    payload["artifact_hash"] = ""
    assert synthesis["artifact_hash"] == _canonical_hash(payload)
    assert synthesis["chronology"]["pre_result_case_plan_commit"] == (
        "03a4cb9a0bce32374d79210d8b712670c11626a7"
    )
    assert synthesis["chronology"]["original_result_commit"] == (
        "1bfad13d82548fe61f70cd9f18828fe0240c8556"
    )
    assert synthesis["chronology"]["registration_is_ancestor_of_result"] is False
    assert synthesis["chronology"]["evaluator_identity_pre_result_frozen"] is False
    assert synthesis["synthesis_target"]["target_branch_head_at_repair"] == (
        "2b264d50b0bb224bfab62e7503656bc92d933b68"
    )
    assert synthesis["synthesis_target"]["live_main_at_repair"] == (
        "b8f3467959f2f44a2cf686d9c005071739284dc8"
    )
    assert synthesis["synthesis_target"]["integration_commit_after_live_main_merge"] == (
        "a423518794d7bbbfabfcf59ff14804491629b544"
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
    assert identities["canonical_failure_artifact_hash_preserved"] == (
        "sha256:1ad323128652a32e1e1441339a94dba970374029d321acd951ea3afc442a3223"
    )
    assert identities["canonical_tool_artifact_hash_preserved"] == (
        "sha256:bff3cc8c347f3ad4b007775d69abadffd408b8db2b3863990baf7b5c76d87475"
    )
    assert identities["postresult_addendum_id"] == "C025-POSTRESULT-ASSURANCE-ADDENDUM-v1"
    assert "BACKFILLED_STRICT_PREREGISTRATION_IMPLICATION_SUPERSEDED" in (
        identities["supersession_action"]
    )
    assert synthesis["claim_scope"]["p_vs_np_root"] == "NO_AUTHORITY"
    assert synthesis["method_lesson"]["framework_transport"].endswith(
        "QUARANTINED_PROPOSAL"
    )


def test_synthesis_receipt_git_provenance_is_executable_and_durable() -> None:
    synthesis = json.loads(SYNTHESIS_RECEIPT.read_text(encoding="utf-8"))
    assert _git_provenance_errors(synthesis) == ()


def test_synthesis_receipt_git_provenance_planted_failures_fail_closed() -> None:
    synthesis = json.loads(SYNTHESIS_RECEIPT.read_text(encoding="utf-8"))

    missing_commit = copy.deepcopy(synthesis)
    missing_commit["git_provenance"]["required_ancestors"]["result_commit"] = "0" * 40
    assert "required ancestor commit missing: result_commit" in _git_provenance_errors(
        missing_commit
    )

    missing_path = copy.deepcopy(synthesis)
    missing_path["git_provenance"]["historical_blob_bindings"]["result_executable"][
        "path"
    ] = "research/real_math/millennium/p_vs_np/05_falsification/DOES_NOT_EXIST.py"
    assert "historical path missing: result_executable" in _git_provenance_errors(
        missing_path
    )

    forged_blob = copy.deepcopy(synthesis)
    forged_blob["git_provenance"]["historical_blob_bindings"]["result_receipt"][
        "git_blob_sha"
    ] = "f" * 40
    assert "historical blob mismatch: result_receipt" in _git_provenance_errors(
        forged_blob
    )

    forged_hash = copy.deepcopy(synthesis)
    forged_hash["git_provenance"]["canonical_target_preservation"]["failure_memory"][
        "raw_sha256"
    ] = "sha256:" + "f" * 64
    assert "canonical target raw hash mismatch: failure_memory" in _git_provenance_errors(
        forged_hash
    )
