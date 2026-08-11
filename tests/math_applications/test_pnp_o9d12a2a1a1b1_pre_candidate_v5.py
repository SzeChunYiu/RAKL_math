from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re

import jsonschema
import pytest

from rakl.failure_lattice import reconstruct_failure_lattice
from rakl.math_context import ContextGateVerdict, MathContextFiber, MethodTransfer, audit_math_context_fiber
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.pre_action_receipt import PreActionFibreReceipt, RejectedRetrieval, RetrievalAuthority, SelectedRetrieval
from rakl.problem_fibre import FibreKnowledgeItem, ProblemAtom, compile_problem_fibre
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview, ResearchMemoryVerdict, audit_research_memory_review
from rakl.research_tool_inventory import ResearchTool, ResearchToolAuthority, ResearchToolInventory
from rakl.semantic_shortcut import REQUIRED_SHORTCUT_ACTIONS, ShortcutReviewVerdict
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FRAMEWORK_SCHEMAS = ROOT / "framework/RAKL/schemas"
ATOM = "O9d12a2a1a1b1"


def load(path: str | Path) -> dict:
    absolute = Path(path)
    if not absolute.is_absolute():
        absolute = ROOT / absolute
    value = json.loads(absolute.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def canonical_hash(value: dict, field: str = "artifact_hash") -> str:
    payload = copy.deepcopy(value)
    payload[field] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def runner_module():
    path = ROOT / "tools/run_pnp_o9d12a2a1a1b1_pre_candidate_v5.py"
    spec = importlib.util.spec_from_file_location("pnp_o9_v5_runner", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def research_tools(raw: dict) -> tuple[ResearchTool, ...]:
    return tuple(
        ResearchTool(
            tool_id=item["tool_id"], name=item["name"], kind=item["kind"], abstraction=item["abstraction"],
            source_atom_id=item["source_atom_id"], source_candidate_id=item["source_candidate_id"],
            source_result_ids=tuple(item["source_result_ids"]), source_context_hash=item["source_context_hash"],
            authority=ResearchToolAuthority(item["authority"]), preconditions=tuple(item["preconditions"]),
            structural_signature=tuple(item["structural_signature"]), operation=item["operation"],
            guaranteed_effects=tuple(item["guaranteed_effects"]), non_guarantees=tuple(item["non_guarantees"]),
            validation_obligations=tuple(item["validation_obligations"]), evidence_pointers=tuple(item["evidence_pointers"]),
            known_failure_ids=tuple(item.get("known_failure_ids", ())), successful_reuse_ids=tuple(item.get("successful_reuse_ids", ())),
            proof_backing=tuple(item.get("proof_backing", ())), artifact_hash=item["artifact_hash"],
        )
        for item in raw["tools"]
    )


def context_fibre(raw: dict) -> MathContextFiber:
    return MathContextFiber(
        atom_id=raw["atom_id"], object_context=raw["object_context"],
        structural_coordinates=tuple(raw["structural_coordinates"]), equivalent_formulations=tuple(raw["equivalent_formulations"]),
        solved_analogues=tuple(raw["solved_analogues"]), near_solved_analogues=tuple(raw["near_solved_analogues"]),
        method_transfers=tuple(MethodTransfer(
            source_context=item["source_context"], method=item["method"], shared_structure=tuple(item["shared_structure"]),
            required_assumptions=tuple(item["required_assumptions"]), disanalogies=tuple(item["disanalogies"]),
            repair_question=item["repair_question"], source_anchors=tuple(item["source_anchors"]),
        ) for item in raw["method_transfers"]),
        explicit_disanalogies=tuple(raw["explicit_disanalogies"]), source_anchors=tuple(raw["source_anchors"]),
        analogy_scan_status=raw["analogy_scan_status"], cross_domain_analogies=(), analogy_scan_notes=raw["analogy_scan_notes"],
        frozen_at=raw["frozen_at"], first_candidate_at=None, packet_hash=raw["packet_hash"],
    )


def memory_review(raw: dict) -> ResearchMemoryReview:
    return ResearchMemoryReview(
        target_atom_id=raw["target_atom_id"], target_context_hash=raw["target_context_hash"],
        tool_inventory_snapshot_hash=raw["tool_inventory_snapshot_hash"], failure_lattice_snapshot_hash=raw["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(raw["tool_query_status"]), failure_query_status=MemoryQueryStatus(raw["failure_query_status"]),
        candidate_method_families=tuple(raw["candidate_method_families"]), relevant_tool_ids=tuple(raw["relevant_tool_ids"]),
        relevant_failure_ids=tuple(raw["relevant_failure_ids"]), selected_tool_ids=tuple(raw["selected_tool_ids"]),
        tool_applicability_notes=tuple(raw["tool_applicability_notes"]), failure_reuse_notes=tuple(raw["failure_reuse_notes"]),
        unresolved_warnings=tuple(raw["unresolved_warnings"]), evidence_pointers=tuple(raw["evidence_pointers"]), artifact_hash=raw["artifact_hash"],
    )


def trace_value(raw: dict) -> MathResearchTrace:
    entries: list[ResearchTraceEntry] = []
    previous = ""
    for item in raw["entries"]:
        assert item["previous_event_hash"] == previous
        assert item["artifact_hash"] == canonical_hash(item)
        previous = item["artifact_hash"]
        entries.append(ResearchTraceEntry(
            event_id=item["event_id"], atom_id=item["atom_id"], event_type=ResearchTraceEventType(item["event_type"]),
            timestamp=item["timestamp"], state_summary=item["state_summary"], action_summary=item["action_summary"],
            evidence_pointers=tuple(item["evidence_pointers"]), alternatives_considered=tuple(item["alternatives_considered"]),
            decision_rationale=item["decision_rationale"], outputs=tuple(item["outputs"]), uncertainties=tuple(item["uncertainties"]),
            residuals=tuple(item["residuals"]), next_steps=tuple(item["next_steps"]), artifact_hash=item["artifact_hash"],
            previous_event_hash=item["previous_event_hash"],
        ))
    return MathResearchTrace(trace_id=raw["trace_id"], entries=tuple(entries))


def test_pnp_o9d12a2a1a1b1_pre_candidate_v5_runtime_fibre_and_pre_action_are_exact() -> None:
    context_raw = load(PNP / "01_frontier/O9d12a2a1a1b1_MATH_CONTEXT_FIBER_V2_20260811.json")
    memory_raw = load(PNP / "07_memory/O9d12a2a1a1b1_RESEARCH_MEMORY_REVIEW_V2_20260811.json")
    tools_raw = load(PNP / "07_memory/O9d12a2a1a1b1_TOOL_SNAPSHOT_V2_20260811.json")
    failures_raw = load(PNP / "07_memory/O9d12a2a1a1b1_FAILURE_SNAPSHOT_V2_20260811.json")
    trace_raw = load(PNP / "09_trace/O9d12a2a1a1b1_PRE_CANDIDATE_TRACE_V3_20260811.json")
    warning = load(PNP / "07_memory/O9d12a2a1a1b1_NONCANONICAL_PARENT_WARNING_V2_20260811.json")

    context = context_fibre(context_raw)
    memory = memory_review(memory_raw)
    trace = trace_value(trace_raw)
    assert audit_math_context_fiber(context).verdict is ContextGateVerdict.PASS
    assert audit_research_memory_review(memory, atom_id=ATOM, context_hash=context.packet_hash).verdict is ResearchMemoryVerdict.PASS
    assert audit_pre_candidate_trace(trace, atom_id=ATOM, context_packet_hash=context.packet_hash).verdict is TraceGateVerdict.FAIL
    assert len(reconstruct_failure_lattice(failures_raw).experiences) == 6
    assert warning["authority"]["canonical_failure_memory"] is False
    assert [item.event_type.value for item in trace.entries] == [
        "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW", "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW", "NEXT_STEP_PROPOSED"
    ]
    assert trace.entries[-1].outputs == ("next_action:SOURCE_NATIVE_T_RULE_THEOREM_INVENTORY", "candidate_identity:none", "root_authority:none")
    assert all(item.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED for item in trace.entries)

    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("shared integral t-pair cover/cyclic system", "source-native theorem inventory"),
            relations=("integral coverage", "shared-rule reuse", "cheap-target and multiplexing controls"),
            domain="complexity theory / set-theoretic fusion / P versus NP",
            goal_type="freeze the source-native theorem-inventory action before any mathematical candidate",
        ),
        record=MathResearchRecord(claim_id=ATOM), context_fiber=context, memory_review=memory, research_trace=trace,
    )
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.CANNOT_CHECK
    assert plan.trace_gate.verdict is TraceGateVerdict.CANNOT_CHECK
    assert plan.candidate_generation_allowed is False
    assert plan.pre_candidate_actions == REQUIRED_SHORTCUT_ACTIONS

    source_pdf = PNP / "00_sources/ECCC_TR25_033_20250318.pdf"
    retrieval = load(PNP / "00_sources/ECCC_TR25_033_SOURCE_RETRIEVAL_RECEIPT_20260811.json")
    assert hashlib.sha256(source_pdf.read_bytes()).hexdigest() == retrieval["artifact"]["raw_sha256"]
    assert retrieval["artifact"]["byte_count"] == source_pdf.stat().st_size == 464382

    fibre_raw = load(PNP / "01_frontier/O9d12a2a1a1b1_PROBLEM_FIBRE_V3_20260811.json")
    atom_raw = fibre_raw["atom"]
    atom = ProblemAtom(
        atom_id=atom_raw["atom_id"], goal=atom_raw["goal"], context_hash=atom_raw["context_hash"],
        structural_coordinates=tuple(atom_raw["structural_coordinates"]), desired_effects=tuple(atom_raw["desired_effects"]),
        dependencies=tuple(atom_raw["dependencies"]), interface_keys=tuple(atom_raw["interface_keys"]),
    )
    knowledge = tuple(FibreKnowledgeItem(
        item_id=item["item_id"], kind=item["kind"], structural_signature=tuple(item["structural_signature"]),
        effects=tuple(item["effects"]), context_tags=tuple(item["context_tags"]), authority=item["authority"], payload_hash=item["payload_hash"],
    ) for item in fibre_raw["knowledge_items"])
    rebuilt = compile_problem_fibre(
        atom, knowledge_items=knowledge, tool_inventory=ResearchToolInventory(tools=research_tools(tools_raw)),
        failure_lattice=reconstruct_failure_lattice(failures_raw), candidate_method_families=tuple(fibre_raw["compilation"]["candidate_method_families"]),
        top_k_each=fibre_raw["compilation"]["top_k_each"],
    )
    assert rebuilt.snapshot_hash == fibre_raw["snapshot_hash"]
    assert [item.item_id for item in rebuilt.knowledge_items] == [item["item_id"] for item in fibre_raw["knowledge_items"]]
    assert [item.tool_id for item in rebuilt.tools] == fibre_raw["tool_ids"]
    assert [item.failure_id for item in rebuilt.failures] == fibre_raw["failure_ids"]
    assert fibre_raw["candidate_generation"] is False and fibre_raw["task_episode_created"] is False
    for binding in fibre_raw["input_bindings"]:
        assert hashlib.sha256((ROOT / binding["path"]).read_bytes()).hexdigest() == binding["raw_sha256"]

    pre_raw = load(PNP / "09_trace/O9d12a2a1a1b1_PRE_ACTION_FIBRE_RECEIPT_V3_20260811.json")
    jsonschema.Draft202012Validator(
        load(FRAMEWORK_SCHEMAS / "pre-action-fibre-receipt-v1.schema.json"), format_checker=jsonschema.FormatChecker()
    ).validate(pre_raw)
    pre = PreActionFibreReceipt(
        receipt_id=pre_raw["receipt_id"], framework_repository=pre_raw["framework_repository"], framework_commit=pre_raw["framework_commit"],
        application_repository=pre_raw["application_repository"], application_commit=pre_raw["application_commit"], task_id=pre_raw["task_id"],
        atom_id=pre_raw["atom_id"], context_hash=pre_raw["context_hash"], fibre_snapshot_hash=pre_raw["fibre_snapshot_hash"],
        operator_ids=tuple(pre_raw["operator_ids"]), selected_retrievals=tuple(SelectedRetrieval(
            retrieval_id=item["retrieval_id"], authority=RetrievalAuthority(item["authority"]), payload_hash=item["payload_hash"]
        ) for item in pre_raw["selected_retrievals"]), rejected_retrievals=tuple(RejectedRetrieval(
            retrieval_id=item["retrieval_id"], rejection_reason=item["rejection_reason"]
        ) for item in pre_raw["rejected_retrievals"]), predeclared_discriminator=pre_raw["predeclared_discriminator"],
        allowed_outcome_branches=tuple(pre_raw["allowed_outcome_branches"]), frozen_at_utc=pre_raw["frozen_at_utc"], sequence_index=pre_raw["sequence_index"],
    )
    assert pre.document() == pre_raw
    assert pre.fibre_snapshot_hash == rebuilt.snapshot_hash
    assert pre.framework_commit == fibre_raw["framework_commit"]
    assert pre.application_commit == fibre_raw["application_commit"]
    assert pre.operator_ids == ("SOURCE_NATIVE_T_RULE_THEOREM_INVENTORY",)
    problem_retrieval = next(item for item in pre.selected_retrievals if item.retrieval_id == "PNP-O9D12A2A1A1B1-PROBLEM-FIBRE-V3")
    assert problem_retrieval.payload_hash == hashlib.sha256((PNP / "01_frontier/O9d12a2a1a1b1_PROBLEM_FIBRE_V3_20260811.json").read_bytes()).hexdigest()


def valid_machine_fixture(module) -> dict:
    z40, z64, p64 = "a" * 40, "a" * 64, "sha256:" + "a" * 64
    source = {
        "repository_url": module.APPLICATION_REPOSITORY, "application_base_commit": module.BASE_COMMIT,
        "application_base_tree": module.BASE_TREE, "latest_main_at_freeze": module.BASE_COMMIT,
        "subject_commit": module.BASE_COMMIT, "subject_tree": module.BASE_TREE,
        "framework_repository_url": module.FRAMEWORK_REPOSITORY, "framework_pin": module.FRAMEWORK_PIN,
        "git_audit": {"verdict": "PASS", "checked_relations": 12, "current_origin_main_at_freeze": True, "worktree_framework_head_checked": True,
                      "subject_checkout_head_checked": True, "subject_checkout_clean_checked": True, "isolated_detached_execution": True},
    }
    bindings = [{"path": p, "kind": k, "commit": module.BASE_COMMIT, "git_blob_sha": z40, "raw_sha256": z64, "size_bytes": 1} for p, k in module.TESTED_INPUTS]
    def run(scope, command, log):
        return {"scope": scope, "command": command, "environment": dict(module.EXACT_ENVIRONMENT), "started_at": "2026-08-11T16:30:00Z", "ended_at": "2026-08-11T16:30:01Z", "duration_seconds": 1.0,
                "exit_code": 0, "result": "PASS", "passed": 1, "failed": 0, "skipped": 0, "log_path": log, "log_sha256": z64, "log_size_bytes": 1}
    return {
        "schema_version": "rakl-math-pnp-machine-run-v5", "receipt_id": "RAKL-MATH-PNP-O9d12a2a1a1b1-MACHINE-RUN-V5-20260811", "atom_id": ATOM,
        "recorded_at": "2026-08-11T16:30:02Z", "source_binding": source, "input_bindings": bindings,
        "runs": [run("FOCUSED_V5_GATE_PRE_RECEIPT", module.FOCUSED_COMMAND, module.FOCUSED_LOG_PATH), run("EXACT_APPLICATION_SUITE_PRE_RECEIPT", module.FULL_COMMAND, module.FULL_LOG_PATH)],
        "all_required_runs_passed": True,
        "authority_contract": {k: False for k in ("mathematical_result", "proof_authority", "novelty_authority", "independent_peer_review", "p_vs_np_authority", "framework_promotion_authority")},
        "artifact_hash": p64,
    }


def valid_gate_fixture(module, machine: dict) -> dict:
    z64, p64 = "a" * 64, "sha256:" + "a" * 64
    artifacts = [{"path": p, "kind": k, "raw_sha256": z64, "size_bytes": 1} for p, k in module.TESTED_INPUTS + module.ENVELOPE_OUTPUTS]
    gate_pass = {"verdict": "PASS", "reasons": ["runtime_reconstructed_in_focused_v5_test"]}
    return {
        "schema_version": "rakl-math-pnp-pre-candidate-gate-v5", "receipt_id": "RAKL-MATH-PNP-O9d12a2a1a1b1-PRE-CANDIDATE-GATE-V5-20260811", "atom_id": ATOM,
        "status": "PROSPECTIVE_PROCESS_GATES_PASS_PRE_ACTION_FIBRE_FROZEN_NO_MATHEMATICAL_CANDIDATE", "recorded_at": "2026-08-11T16:31:00Z",
        "source_binding": copy.deepcopy(machine["source_binding"]),
        "primary_source_binding": {"path": module.TESTED_INPUTS[12][0], "url": "https://eccc.weizmann.ac.il/report/2025/033/download/", "raw_sha256": module.PRIMARY_SOURCE_SHA256, "retrieval_receipt_path": module.TESTED_INPUTS[13][0]},
        "supersession": {"v0_status": "REJECTED_PRE_CANDIDATE_AUTHORIZATION", "v0_correction_path": module.TESTED_INPUTS[0][0], "v0_correction_hash": p64,
                           "original_v0_gate_path": module.TESTED_INPUTS[16][0], "original_v0_gate_raw_sha256": z64, "original_v0_gate_artifact_hash": p64,
                           "v2_status": "REJECTED_PRE_CANDIDATE_AUTHORIZATION", "v2_correction_path": module.TESTED_INPUTS[1][0], "v2_correction_hash": p64,
                           "original_v2_gate_path": module.TESTED_INPUTS[17][0], "original_v2_gate_raw_sha256": z64, "original_v2_gate_artifact_hash": p64,
                           "v3_status": "HISTORICAL_PASS_AT_OWN_FREEZE_SUPERSEDED_FOR_CURRENT_MAIN",
                           "prior_v3_machine_path": module.TESTED_INPUTS[20][0], "prior_v3_machine_raw_sha256": z64, "prior_v3_machine_artifact_hash": p64,
                           "prior_v3_gate_path": module.TESTED_INPUTS[21][0], "prior_v3_gate_raw_sha256": z64, "prior_v3_gate_artifact_hash": p64,
                           "v4_status": "REJECTED_ASSURANCE_ENVELOPE_PROVENANCE_AND_CHRONOLOGY",
                           "v4_failure_path": module.TESTED_INPUTS[24][0], "v4_failure_raw_sha256": z64, "v4_failure_artifact_hash": p64,
                           "prior_v4_machine_path": module.TESTED_INPUTS[25][0], "prior_v4_machine_raw_sha256": z64, "prior_v4_machine_artifact_hash": p64,
                           "prior_v4_gate_path": module.TESTED_INPUTS[26][0], "prior_v4_gate_raw_sha256": z64, "prior_v4_gate_artifact_hash": p64,
                           "historical_bytes_modified": False},
        "artifacts": artifacts,
        "runtime_gate": {"context_packet_hash": p64, "memory_review_hash": p64, "expert_review_hash": p64, "trace_terminal_hash": p64,
                         "context_gate": gate_pass, "memory_gate": gate_pass, "trace_gate": gate_pass,
                         "plan_math_research": {"candidate_generation_allowed": True, "pre_candidate_actions": [], "candidate_paths_used": False, "candidate_identity": None},
                         "problem_fibre": {"path": module.TESTED_INPUTS[14][0], "snapshot_hash": z64, "authority": "PROPOSAL_ONLY_RETRIEVAL_VIEW"},
                         "pre_action_fibre_receipt": {"path": module.TESTED_INPUTS[15][0], "receipt_canonical_sha256": z64, "action_executed": False, "authority": "PROPOSAL_ONLY_PROCESS_TELEMETRY"}},
        "machine_run": {"path": module.MACHINE_RECEIPT_PATH, "raw_sha256": z64, "artifact_hash": p64, "focused_log_path": module.FOCUSED_LOG_PATH,
                        "focused_log_sha256": z64, "full_log_path": module.FULL_LOG_PATH, "full_log_sha256": z64, "all_required_runs_passed": True},
        "authority_contract": {k: False for k in ("candidate_proposed", "mathematical_result", "proof_authority", "novelty_authority", "independent_peer_review", "p_vs_np_authority", "framework_promotion_authority", "fibre_search_universe_complete")},
        "next_action": "SOURCE_NATIVE_T_RULE_THEOREM_INVENTORY_IN_A_SEPARATE_VERSIONED_ROUND", "artifact_hash": p64,
    }


def test_pnp_o9d12a2a1a1b1_pre_candidate_v5_schemas_reject_type_length_case_newline_duplicates_and_omissions() -> None:
    module = runner_module()
    machine = valid_machine_fixture(module)
    gate = valid_gate_fixture(module, machine)
    validators = []
    for path, value in ((module.MACHINE_SCHEMA_PATH, machine), (module.GATE_SCHEMA_PATH, gate)):
        schema = load(path)
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
        validator.validate(value)
        validators.append(validator)
    machine_validator, gate_validator = validators

    def hostile_values(original: str) -> tuple[object, ...]:
        prefix = "sha256:" if original.startswith("sha256:") else ""
        body = original[len(prefix):]
        return (7, "", prefix + body[:-1], prefix + body + "0", original.upper(), original + "\n", original + "\r\n")
    for index in range(len(machine["input_bindings"])):
        for key in ("git_blob_sha", "raw_sha256"):
            for value in hostile_values(machine["input_bindings"][index][key]):
                bad = copy.deepcopy(machine); bad["input_bindings"][index][key] = value
                assert list(machine_validator.iter_errors(bad))
    for key in ("subject_commit", "subject_tree", "framework_pin"):
        for value in hostile_values(machine["source_binding"][key]):
            bad = copy.deepcopy(machine); bad["source_binding"][key] = value
            assert list(machine_validator.iter_errors(bad))
    for run_index in range(2):
        for value in hostile_values(machine["runs"][run_index]["log_sha256"]):
            bad = copy.deepcopy(machine); bad["runs"][run_index]["log_sha256"] = value
            assert list(machine_validator.iter_errors(bad))
        bad = copy.deepcopy(machine); del bad["runs"][run_index]["ended_at"]
        assert list(machine_validator.iter_errors(bad))
        bad = copy.deepcopy(machine); bad["runs"][run_index]["ended_at"] = "not-a-date"
        assert list(machine_validator.iter_errors(bad))
    duplicate = copy.deepcopy(machine); duplicate["input_bindings"][1] = copy.deepcopy(duplicate["input_bindings"][0])
    assert list(machine_validator.iter_errors(duplicate))
    duplicate_run = copy.deepcopy(machine); duplicate_run["runs"][1] = copy.deepcopy(duplicate_run["runs"][0])
    assert list(machine_validator.iter_errors(duplicate_run))
    omitted = copy.deepcopy(machine); omitted["input_bindings"].pop()
    assert list(machine_validator.iter_errors(omitted))

    for index in range(len(gate["artifacts"])):
        for value in hostile_values(gate["artifacts"][index]["raw_sha256"]):
            bad = copy.deepcopy(gate); bad["artifacts"][index]["raw_sha256"] = value
            assert list(gate_validator.iter_errors(bad))
    for key in ("context_packet_hash", "memory_review_hash", "expert_review_hash", "trace_terminal_hash"):
        for value in hostile_values(gate["runtime_gate"][key]):
            bad = copy.deepcopy(gate); bad["runtime_gate"][key] = value
            assert list(gate_validator.iter_errors(bad))
    for key in (
        "original_v0_gate_raw_sha256", "original_v0_gate_artifact_hash",
        "original_v2_gate_raw_sha256", "original_v2_gate_artifact_hash",
        "prior_v3_machine_raw_sha256", "prior_v3_machine_artifact_hash",
        "prior_v3_gate_raw_sha256", "prior_v3_gate_artifact_hash",
        "v4_failure_raw_sha256", "v4_failure_artifact_hash",
        "prior_v4_machine_raw_sha256", "prior_v4_machine_artifact_hash",
        "prior_v4_gate_raw_sha256", "prior_v4_gate_artifact_hash",
    ):
        for value in hostile_values(gate["supersession"][key]):
            bad = copy.deepcopy(gate); bad["supersession"][key] = value
            assert list(gate_validator.iter_errors(bad))
    duplicate_gate = copy.deepcopy(gate); duplicate_gate["artifacts"][1] = copy.deepcopy(duplicate_gate["artifacts"][0])
    assert list(gate_validator.iter_errors(duplicate_gate))
    omitted_gate = copy.deepcopy(gate); omitted_gate["artifacts"].pop()
    assert list(gate_validator.iter_errors(omitted_gate))


def test_pnp_o9d12a2a1a1b1_pre_candidate_v5_git_audit_executes_and_mutations_fail_closed() -> None:
    module = runner_module()
    source = valid_machine_fixture(module)["source_binding"]
    assert module.audit_git_state(source, require_current_origin=False) == {
        "verdict": "PASS", "checked_relations": 12, "current_origin_main_at_freeze": False, "worktree_framework_head_checked": False
    }
    current_audit = module.audit_git_state(source, require_current_origin=True)
    if module.git("rev-parse", "refs/remotes/origin/main") == module.BASE_COMMIT:
        assert current_audit == {
            "verdict": "PASS", "checked_relations": 12, "current_origin_main_at_freeze": True, "worktree_framework_head_checked": True
        }
    else:
        assert current_audit == {"verdict": "FAIL", "reason": "ORIGIN_MAIN_MOVED_BEFORE_FREEZE"}
    mutations = [
        ("application_base_commit", "0" * 40), ("application_base_tree", "0" * 40),
        ("latest_main_at_freeze", "0" * 40), ("subject_tree", "0" * 40), ("framework_pin", "0" * 40),
        ("repository_url", "https://invalid.example/repo.git"),
    ]
    for key, value in mutations:
        bad = copy.deepcopy(source); bad[key] = value
        assert module.audit_git_state(bad, require_current_origin=False)["verdict"] != "PASS"
    missing = copy.deepcopy(source); del missing["subject_commit"]
    assert module.audit_git_state(missing) == {"verdict": "CANNOT_CHECK", "reason": "MISSING_GIT_BINDING_FIELDS"}
    malformed = copy.deepcopy(source); malformed["subject_commit"] = 7
    assert module.audit_git_state(malformed)["verdict"] == "FAIL"

    with pytest.raises(SystemExit, match="current HEAD does not equal"):
        module._require_clean_subject_checkout("0" * 40)
    original_git = module.git
    try:
        subject = original_git("rev-parse", "HEAD")
        module.git = lambda *args, **kwargs: subject if args == ("rev-parse", "HEAD") else "?? hostile-untracked"
        with pytest.raises(SystemExit, match="not clean"):
            module._require_clean_subject_checkout(subject)
    finally:
        module.git = original_git


def test_pnp_o9d12a2a1a1b1_pre_candidate_v5_historical_supersession_is_direct_and_exact() -> None:
    module = runner_module()
    audit = module.audit_historical_supersession()
    assert audit["verdict"] == "PASS"
    assert audit["checked_documents"] == 9
    assert audit["checked_schemas"] == 6
    assert audit["checked_v3_historical_inputs"] == 20
    for document_index in (0, 1, 16, 17, 20, 21, 24, 25, 26):
        document = load(module.TESTED_INPUTS[document_index][0])
        assert document["artifact_hash"] == canonical_hash(document)
    v0_failure = load(module.TESTED_INPUTS[0][0])
    v2_failure = load(module.TESTED_INPUTS[1][0])
    v0_path, v2_path = module.TESTED_INPUTS[16][0], module.TESTED_INPUTS[17][0]
    v0_rows = [row for row in v0_failure["failed_packet_bindings"] if row["path"] == v0_path]
    v2_rows = [row for row in v2_failure["v2_bindings"] if row["path"] == v2_path]
    assert len(v0_rows) == len(v2_rows) == 1
    assert v0_rows[0]["raw_sha256"] == hashlib.sha256((ROOT / v0_path).read_bytes()).hexdigest()
    assert v2_rows[0]["raw_sha256"] == hashlib.sha256((ROOT / v2_path).read_bytes()).hexdigest()


def test_pnp_o9d12a2a1a1b1_pre_candidate_v5_machine_and_gate_receipts_when_present_are_raw_bound() -> None:
    module = runner_module()
    machine_path = ROOT / module.MACHINE_RECEIPT_PATH
    gate_path = ROOT / module.GATE_RECEIPT_PATH
    if not machine_path.exists():
        assert not gate_path.exists()
        return
    machine = load(machine_path)
    module.validate_document(machine, module.MACHINE_SCHEMA_PATH)
    assert machine["artifact_hash"] == canonical_hash(machine)
    assert module.audit_git_state(machine["source_binding"], require_current_origin=False)["verdict"] == "PASS"
    assert module.audit_input_bindings(machine) == {"verdict": "PASS", "checked_bindings": len(module.TESTED_INPUTS)}
    subject = machine["source_binding"]["subject_commit"]
    historical_inputs = {
        binding["path"]: module.git("show", f"{subject}:{binding['path']}", binary=True)
        for binding in machine["input_bindings"]
    }
    assert module.audit_machine_semantics(machine)["verdict"] == "PASS"
    impossible_time = copy.deepcopy(machine)
    impossible_time["runs"][0]["ended_at"] = "2099-01-01T00:00:00Z"
    assert module.audit_machine_semantics(impossible_time)["verdict"] == "FAIL"
    future_machine = copy.deepcopy(machine)
    future_machine["recorded_at"] = "2099-01-01T00:00:00Z"
    assert module.audit_machine_semantics(future_machine)["verdict"] == "FAIL"
    reversed_runs = copy.deepcopy(machine)
    reversed_runs["runs"][1]["started_at"] = reversed_runs["runs"][0]["started_at"]
    reversed_runs["runs"][1]["ended_at"] = reversed_runs["runs"][0]["ended_at"]
    assert module.audit_machine_semantics(reversed_runs)["verdict"] == "FAIL"
    false_count = copy.deepcopy(machine)
    false_count["runs"][0]["passed"] += 1
    assert module.audit_machine_semantics(false_count)["verdict"] == "FAIL"
    for run in machine["runs"]:
        raw = (ROOT / run["log_path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == run["log_sha256"]
        assert len(raw) == run["log_size_bytes"]
        passed, failed, skipped = module._parse_pytest_counts(raw.decode("utf-8"))
        assert (passed, failed, skipped) == (run["passed"], run["failed"], run["skipped"])
    if not gate_path.exists():
        return
    gate = load(gate_path)
    module.validate_document(gate, module.GATE_SCHEMA_PATH)
    assert gate["artifact_hash"] == canonical_hash(gate)
    assert gate["machine_run"]["raw_sha256"] == hashlib.sha256(machine_path.read_bytes()).hexdigest()
    assert gate["machine_run"]["artifact_hash"] == machine["artifact_hash"]
    assert len({item["path"] for item in gate["artifacts"]}) == len(module.TESTED_INPUTS + module.ENVELOPE_OUTPUTS)
    assert len({item["kind"] for item in gate["artifacts"]}) == len(module.TESTED_INPUTS + module.ENVELOPE_OUTPUTS)
    for item in gate["artifacts"]:
        raw = historical_inputs.get(item["path"], (ROOT / item["path"]).read_bytes())
        assert hashlib.sha256(raw).hexdigest() == item["raw_sha256"]
        assert len(raw) == item["size_bytes"]
    assert all(value is False for value in gate["authority_contract"].values())
    assert module.audit_gate_bindings(gate, machine)["verdict"] == "PASS"

    def wrong_hash(value: str) -> str:
        prefix = "sha256:" if value.startswith("sha256:") else ""
        replacement = prefix + "0" * (len(value) - len(prefix))
        return replacement if replacement != value else prefix + "1" * (len(value) - len(prefix))

    semantic_mutations: list[dict] = []
    bad = copy.deepcopy(gate); bad["source_binding"]["subject_commit"] = "0" * 40; semantic_mutations.append(bad)
    bad = copy.deepcopy(gate); bad["runtime_gate"]["context_packet_hash"] = wrong_hash(bad["runtime_gate"]["context_packet_hash"]); semantic_mutations.append(bad)
    bad = copy.deepcopy(gate); bad["supersession"]["original_v0_gate_raw_sha256"] = wrong_hash(bad["supersession"]["original_v0_gate_raw_sha256"]); semantic_mutations.append(bad)
    bad = copy.deepcopy(gate); bad["machine_run"]["raw_sha256"] = wrong_hash(bad["machine_run"]["raw_sha256"]); semantic_mutations.append(bad)
    bad = copy.deepcopy(gate); bad["recorded_at"] = "2000-01-01T00:00:00Z"; semantic_mutations.append(bad)
    bad = copy.deepcopy(gate); bad["recorded_at"] = "2099-01-01T00:00:00Z"; semantic_mutations.append(bad)
    for bad in semantic_mutations:
        module.validate_document(bad, module.GATE_SCHEMA_PATH)
        assert module.audit_gate_bindings(bad, machine)["verdict"] == "FAIL"
