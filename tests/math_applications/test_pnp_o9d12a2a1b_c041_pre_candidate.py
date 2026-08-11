from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema
from rakl.failure_lattice import (
    DifferenceWitness,
    ReuseVerdict,
    assess_method_reuse,
    reconstruct_failure_lattice,
)
from rakl.math_context import (
    ContextGateVerdict,
    MathContextFiber,
    MethodTransfer,
    audit_math_context_fiber,
)
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import (
    MemoryQueryStatus,
    ResearchMemoryReview,
    ResearchMemoryVerdict,
    audit_research_memory_review,
)
from rakl.research_tool_inventory import (
    ResearchTool,
    ResearchToolAuthority,
    ToolApplicabilityVerdict,
    ToolApplicabilityWitness,
    assess_tool_applicability,
)
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)
from rakl.root_coordinate_preservation import (
    BridgeEdge,
    CoordinateAuthority,
    EdgeProofStatus,
    Obligation,
    PreservationGateVerdict,
    PreservationVerdict,
    RegisteredStateObservation,
    RootCoordinatePreservationReceipt,
    audit_root_coordinate_preservation,
)

ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
ATOM = "O9d12a2a1b"
CONTEXT_PATH = PNP / "01_frontier/O9d12a2a1b_C041_MATH_CONTEXT_FIBER_20260811.json"
SIZE_PATH = PNP / "01_frontier/O9d12a2a1b_C041_SIZE_RATE_CONTRACT_20260811.json"
RELEVANCE_PATH = PNP / "05_falsification/C037_CYLINDER_RELEVANCE_REPLAY_RECEIPT_20260811.json"
MEMORY_PATH = PNP / "07_memory/O9d12a2a1b_C041_RESEARCH_MEMORY_REVIEW_20260811.json"
FAILURE_PATH = PNP / "07_memory/O9d12a2a1b_C041_FAILURE_LATTICE_SNAPSHOT_20260811.json"
TOOL_PATH = PNP / "07_memory/O9d12a2a1b_C041_TOOL_SNAPSHOT_20260811.json"
APPLICABILITY_PATH = PNP / "07_memory/O9d12a2a1b_C041_TOOL_APPLICABILITY_20260811.json"
TRACE_PATH = PNP / "09_trace/O9d12a2a1b_C041_PRE_CANDIDATE_TRACE_20260811.json"
PRE_ACTION_PATH = PNP / "09_trace/O9d12a2a1b_C041_PRE_ACTION_20260811.json"
DW_PATH = PNP / "07_memory/O9d12a2a1b_C041_DIFFERENCE_WITNESSES_20260811.json"
ROOT_PATH = PNP / "09_trace/O9d12a2a1b_C041_ROOT_COORDINATE_PRESERVATION_20260811.json"
REVIEW_PATH = PNP / "08_reviews/O9d12a2a1b_C041_EXPERT_CONTEXT_REVIEW_20260811.json"
ATOM_PATH = PNP / "02_problem_dag/O9d12a2a1b_C041_ATOMIZATION_20260811.json"
EXPECTED_FRAMEWORK = "91f182a3e7ad7ba670babbec5f49a1304da2d933"
EXPECTED_APPLICATION = "ec623f7114eac82e0d329f755c7a161c79aaf269"
EXPECTED_PRESERVATION_SHA256 = "96bd3b23a1ca367748795ff1fe1130a19ff69e011498c655d9accddeb1879632"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def raw_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value: dict, field: str, *, prefix: bool = True) -> str:
    payload = copy.deepcopy(value)
    payload[field] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    digest = hashlib.sha256(raw.encode()).hexdigest()
    return ("sha256:" if prefix else "") + digest


def context_value(raw: dict) -> MathContextFiber:
    return MathContextFiber(
        atom_id=raw["atom_id"],
        object_context=raw["object_context"],
        structural_coordinates=tuple(raw["structural_coordinates"]),
        equivalent_formulations=tuple(raw["equivalent_formulations"]),
        solved_analogues=tuple(raw["solved_analogues"]),
        near_solved_analogues=tuple(raw["near_solved_analogues"]),
        method_transfers=tuple(
            MethodTransfer(
                source_context=item["source_context"],
                method=item["method"],
                shared_structure=tuple(item["shared_structure"]),
                required_assumptions=tuple(item["required_assumptions"]),
                disanalogies=tuple(item["disanalogies"]),
                repair_question=item["repair_question"],
                source_anchors=tuple(item["source_anchors"]),
            )
            for item in raw["method_transfers"]
        ),
        explicit_disanalogies=tuple(raw["explicit_disanalogies"]),
        source_anchors=tuple(raw["source_anchors"]),
        analogy_scan_status=raw["analogy_scan_status"],
        cross_domain_analogies=(),
        analogy_scan_notes=raw["analogy_scan_notes"],
        frozen_at=raw["frozen_at"],
        first_candidate_at=None,
        packet_hash=raw["packet_hash"],
    )


def memory_value(raw: dict) -> ResearchMemoryReview:
    return ResearchMemoryReview(
        target_atom_id=raw["target_atom_id"],
        target_context_hash=raw["target_context_hash"],
        tool_inventory_snapshot_hash=raw["tool_inventory_snapshot_hash"],
        failure_lattice_snapshot_hash=raw["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(raw["tool_query_status"]),
        failure_query_status=MemoryQueryStatus(raw["failure_query_status"]),
        candidate_method_families=tuple(raw["candidate_method_families"]),
        relevant_tool_ids=tuple(raw["relevant_tool_ids"]),
        relevant_failure_ids=tuple(raw["relevant_failure_ids"]),
        selected_tool_ids=tuple(raw["selected_tool_ids"]),
        tool_applicability_notes=tuple(raw["tool_applicability_notes"]),
        failure_reuse_notes=tuple(raw["failure_reuse_notes"]),
        unresolved_warnings=tuple(raw["unresolved_warnings"]),
        evidence_pointers=tuple(raw["evidence_pointers"]),
        artifact_hash=raw["artifact_hash"],
    )


def trace_value(raw: dict) -> MathResearchTrace:
    entries = []
    previous = ""
    for item in raw["entries"]:
        assert item["previous_event_hash"] == previous
        assert item["artifact_hash"] == canonical_hash(item, "artifact_hash")
        previous = item["artifact_hash"]
        entries.append(
            ResearchTraceEntry(
                event_id=item["event_id"],
                atom_id=item["atom_id"],
                event_type=ResearchTraceEventType(item["event_type"]),
                timestamp=item["timestamp"],
                state_summary=item["state_summary"],
                action_summary=item["action_summary"],
                evidence_pointers=tuple(item["evidence_pointers"]),
                alternatives_considered=tuple(item["alternatives_considered"]),
                decision_rationale=item["decision_rationale"],
                outputs=tuple(item["outputs"]),
                uncertainties=tuple(item["uncertainties"]),
                residuals=tuple(item["residuals"]),
                next_steps=tuple(item["next_steps"]),
                artifact_hash=item["artifact_hash"],
                previous_event_hash=item["previous_event_hash"],
            )
        )
    return MathResearchTrace(trace_id=raw["trace_id"], entries=tuple(entries))


def root_value(raw: dict) -> RootCoordinatePreservationReceipt:
    return RootCoordinatePreservationReceipt(
        receipt_id=raw["receipt_id"],
        root_claim_id=raw["root_claim_id"],
        root_coordinate=raw["root_coordinate"],
        surrogate_coordinate=raw["surrogate_coordinate"],
        bridge_edges=tuple(
            BridgeEdge(
                edge_id=x["edge_id"],
                source_coordinate=x["source_coordinate"],
                target_coordinate=x["target_coordinate"],
                interface_map=x["interface_map"],
                proof_status=EdgeProofStatus(x["proof_status"]),
                enabling_assumptions=tuple(x["enabling_assumptions"]),
            )
            for x in raw["bridge_edges"]
        ),
        obligations=tuple(
            Obligation(
                obligation_id=x["obligation_id"],
                description=x["description"],
                non_compensatory=x["non_compensatory"],
                discharged_by_surrogate_evidence_only=x[
                    "discharged_by_surrogate_evidence_only"
                ],
            )
            for x in raw["obligations"]
        ),
        known_disanalogies=tuple(raw["known_disanalogies"]),
        source_authority=CoordinateAuthority(raw["source_authority"]),
        target_authority=CoordinateAuthority(raw["target_authority"]),
        cheapest_hostile_world=raw["cheapest_hostile_world"],
        registered_observations=tuple(
            RegisteredStateObservation(
                state_id=x["state_id"],
                projected_state=x["projected_state"],
                registered_downstream_outcome=x["registered_downstream_outcome"],
            )
            for x in raw["registered_observations"]
        ),
        reverification_triggers=tuple(raw["reverification_triggers"]),
        prior_failure_ids=tuple(raw["prior_failure_ids"]),
        schema_version=raw["schema_version"],
    )


def tool_value(raw: dict) -> ResearchTool:
    return ResearchTool(
        tool_id=raw["tool_id"], name=raw["name"], kind=raw["kind"],
        abstraction=raw["abstraction"], source_atom_id=raw["source_atom_id"],
        source_candidate_id=raw["source_candidate_id"],
        source_result_ids=tuple(raw["source_result_ids"]),
        source_context_hash=raw["source_context_hash"],
        authority=ResearchToolAuthority(raw["authority"]),
        preconditions=tuple(raw["preconditions"]),
        structural_signature=tuple(raw["structural_signature"]),
        operation=raw["operation"],
        guaranteed_effects=tuple(raw["guaranteed_effects"]),
        non_guarantees=tuple(raw["non_guarantees"]),
        validation_obligations=tuple(raw["validation_obligations"]),
        evidence_pointers=tuple(raw["evidence_pointers"]),
        known_failure_ids=tuple(raw["known_failure_ids"]),
        successful_reuse_ids=tuple(raw["successful_reuse_ids"]),
        proof_backing=tuple(raw["proof_backing"]),
        artifact_hash=raw["artifact_hash"],
    )


def difference_value(raw: dict) -> DifferenceWitness:
    return DifferenceWitness(
        target_atom_id=raw["target_atom_id"],
        target_context_hash=raw["target_context_hash"],
        method_family=raw["method_family"],
        prior_failure_ids=tuple(raw["prior_failure_ids"]),
        changed_structural_coordinates=tuple(raw["changed_structural_coordinates"]),
        restored_or_replaced_assumptions=tuple(raw["restored_or_replaced_assumptions"]),
        prior_falsifier_escape_reason=raw["prior_falsifier_escape_reason"],
        cheapest_repeat_failure_test=raw["cheapest_repeat_failure_test"],
        evidence_pointers=tuple(raw["evidence_pointers"]),
    )


def test_c041_schema_valid_runtime_gates_pass_without_a_candidate() -> None:
    context_raw, memory_raw, trace_raw = load(CONTEXT_PATH), load(MEMORY_PATH), load(TRACE_PATH)
    schema_pairs = (
        ("math-context-fiber.schema.json", context_raw),
        ("research-memory-review.schema.json", memory_raw),
        ("math-research-trace.schema.json", trace_raw),
        ("root-coordinate-preservation-receipt-v1.schema.json", load(ROOT_PATH)),
        ("failure-experience-lattice.schema.json", load(FAILURE_PATH)),
        ("research-tool-inventory.schema.json", load(TOOL_PATH)),
    )
    for name, value in schema_pairs:
        schema = load(ROOT / "framework/RAKL/schemas" / name)
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(value)

    context, memory, trace = context_value(context_raw), memory_value(memory_raw), trace_value(trace_raw)
    preservation = root_value(load(ROOT_PATH))
    assert audit_math_context_fiber(context).verdict is ContextGateVerdict.PASS
    assert audit_research_memory_review(
        memory, atom_id=ATOM, context_hash=context.packet_hash
    ).verdict is ResearchMemoryVerdict.PASS
    assert audit_pre_candidate_trace(
        trace, atom_id=ATOM, context_packet_hash=context.packet_hash
    ).verdict is TraceGateVerdict.PASS
    assert audit_root_coordinate_preservation(preservation).verdict is PreservationVerdict.INTERFACE_UNPROVED
    assert [entry.event_type.value for entry in trace.entries] == [
        "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW", "NEXT_STEP_PROPOSED",
    ]
    assert all(
        entry.event_type is not ResearchTraceEventType.CANDIDATE_PROPOSED
        for entry in trace.entries
    )

    plan = plan_math_research(
        signature=ProblemSignature(
            objects=("graph-realizable full-cover instances", "fractional dual certificates", "uniform extension"),
            relations=("cylinder relevance", "dual feasibility", "augmentation", "divergence", "size-rate composition"),
            domain="complexity theory / full semi-filter fusion covers / P versus NP",
            goal_type="freeze C041 pre-candidate mathematics before one explicit extension rule",
        ),
        record=MathResearchRecord(claim_id=ATOM),
        context_fiber=context,
        memory_review=memory,
        research_trace=trace,
        preservation_receipt=preservation,
        require_preservation_gate=True,
        expected_preservation_sha256=EXPECTED_PRESERVATION_SHA256,
    )
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert trace.entries[-1].outputs == (
        "next_action:MATERIALIZE_ONE_LOCAL_C041_RULE_THEN_FREEZE_FINITE_GATE",
        "candidate_identity:none",
        "root_preservation_sha256:" + EXPECTED_PRESERVATION_SHA256,
        "root_authority:none",
    )


def test_c041_runtime_tool_applicability_is_validation_scoped() -> None:
    tool_raw = load(TOOL_PATH)["tools"][0]
    receipt = load(APPLICABILITY_PATH)
    witness_raw = receipt["witness"]
    witness = ToolApplicabilityWitness(
        target_atom_id=witness_raw["target_atom_id"],
        target_context_hash=witness_raw["target_context_hash"],
        tool_id=witness_raw["tool_id"],
        matched_preconditions=tuple(witness_raw["matched_preconditions"]),
        unmatched_preconditions=tuple(witness_raw["unmatched_preconditions"]),
        shared_structural_coordinates=tuple(witness_raw["shared_structural_coordinates"]),
        changed_structural_coordinates=tuple(witness_raw["changed_structural_coordinates"]),
        known_failure_ids_reviewed=tuple(witness_raw["known_failure_ids_reviewed"]),
        target_validation_plan=tuple(witness_raw["target_validation_plan"]),
        evidence_pointers=tuple(witness_raw["evidence_pointers"]),
    )
    assessment = assess_tool_applicability(tool_value(tool_raw), witness)
    assert assessment.verdict is ToolApplicabilityVerdict.APPLICABLE_WITH_VALIDATION
    assert receipt["assessment"]["verdict"] == assessment.verdict.value
    assert receipt["artifact_hash"] == canonical_hash(receipt, "artifact_hash")


def test_c041_failure_lattice_and_difference_witnesses_are_runtime_real() -> None:
    document = load(FAILURE_PATH)
    lattice = reconstruct_failure_lattice(document)
    assert {item.failure_id for item in lattice.experiences} == {
        "F-C024-FRACTIONAL-INTEGRALITY-GAP",
        "F-C037-ARBITRARY-EXTENSION-NONMONOTONE",
        "F-C041-POLYTIME-EXPLICITNESS-SUPERPOLY-CONTRADICTION",
    }
    c037 = next(
        item for item in lattice.experiences
        if item.failure_id == "F-C037-ARBITRARY-EXTENSION-NONMONOTONE"
    )
    assert "rho_frac drops exactly from 3/2 to 1" in c037.observed_result
    assert "two supported lifts relevant and one irrelevant" in c037.observed_result
    explicitness = next(
        item for item in lattice.experiences
        if item.failure_id == "F-C041-POLYTIME-EXPLICITNESS-SUPERPOLY-CONTRADICTION"
    )
    assert explicitness.diagnosis_status.value == "VERIFIED_IMPOSSIBILITY"
    assert "polynomial-size circuits" in explicitness.observed_result
    memory = load(MEMORY_PATH)
    assert memory["failure_lattice_snapshot_hash"] == raw_hash(FAILURE_PATH)
    assert memory["tool_inventory_snapshot_hash"] == raw_hash(TOOL_PATH)

    witnesses = load(DW_PATH)
    assert witnesses["artifact_hash"] == canonical_hash(witnesses, "artifact_hash")
    by_id = {row["witness_id"]: row for row in witnesses["difference_witnesses"]}
    c024 = by_id["C041-DW-C024"]
    c024_assessment = assess_method_reuse(
        lattice,
        target_atom_id=ATOM,
        target_context_hash=load(CONTEXT_PATH)["packet_hash"],
        method_family="plain fractional set-cover / semi-filter packing relaxation",
        relevant_failure_ids=tuple(c024["prior_failure_ids"]),
        difference_witness=difference_value(c024),
    )
    assert c024_assessment.verdict is ReuseVerdict.DIFFERENCE_WITNESSED
    assert c024["reuse_assessment"]["verdict"] == c024_assessment.verdict.value

    c037 = by_id["C041-DW-C037"]
    c037_assessment = assess_method_reuse(
        lattice,
        target_atom_id=ATOM,
        target_context_hash=load(CONTEXT_PATH)["packet_hash"],
        method_family="graph-extension monotonicity for fractional full-cover value",
        relevant_failure_ids=tuple(c037["prior_failure_ids"]),
        difference_witness=None,
    )
    assert c037_assessment.verdict is ReuseVerdict.SAME_CONTEXT_RETRY
    assert c037["reuse_assessment"]["verdict"] == c037_assessment.verdict.value
    assert c037["witness_status"] == "REQUIRED_FUTURE_DIFFERENCE_WITNESS_NOT_SUPPLIED_TO_GATE"
    assert "G_NEQ" in by_id["C041-DW-C024"]["cheapest_repeat_failure_test"]
    assert "zero residual augmentation" in by_id["C041-DW-C037"]["cheapest_repeat_failure_test"]


def test_c041_size_rate_contract_is_exact_and_non_compensatory() -> None:
    contract = load(SIZE_PATH)
    assert contract["artifact_hash"] == canonical_hash(contract, "artifact_hash")
    assert "complement ground set" in contract["family_domain"]["registered_form"]
    assert "associated graph" in contract["family_domain"]["registered_form"]
    assert contract["primary_size_coordinate"]["definition"] == (
        "N_n = |R_n|+|C_n| = 2M_n"
    )
    bounds = contract["explicit_graph_description"]["proved_bounds"]
    assert bounds == [
        "N_n - 1 <= D_n",
        "D_n <= N_n^2/4 + 4 log2(N_n) + 2",
        "log D_n = Theta(log N_n) as n -> infinity",
    ]
    scales = contract["boolean_function_input_scale"]
    assert scales["direct_adjacency_definition"] == "a_n = 2n bits for f_{G_n}(r,c), where G_n=[M_n]^2\\U_n"
    assert scales["source_wrapper_definition"] == (
        "b_n = 2n + 1 bits for the related total Boolean function in the source remark"
    )
    outcomes = {
        row["outcome"]: row["condition"]
        for row in contract["frozen_certificate_route_outcomes"]
    }
    assert {
        "CERTIFICATE_MASS_BOUNDED",
        "CERTIFICATE_MASS_UNBOUNDED_SUBLOGARITHMIC",
        "CERTIFICATE_MASS_THETA_LOGARITHMIC",
        "CERTIFICATE_MASS_SUPERLOGARITHMIC",
        "CERTIFICATE_MASS_IRREGULAR",
    } == set(outcomes)
    assert contract["epistemic_outcome"]["outcome"] == "CANNOT_CHECK"
    assert contract["epistemic_outcome"]["saturation_credit"] is False
    assert contract["superlogarithmic_composition_gate"]["required_limit"] == (
        "(L_0 + sum_{i<n} d(i)) / log h(n) -> infinity"
    )
    assert "NP language" in contract["root_rate_gate"]["root_required_strength"]
    assert "P is contained in P/poly" in contract["uniform_explicitness"]["forbidden_combination"]
    assert "in E" in contract["uniform_explicitness"]["local_language_consequence"]
    assert "Unbounded certificate mass in n alone" in contract["non_guarantees"][0]


def test_c037_exact_cylinder_replay_has_two_survivors_and_one_loss() -> None:
    receipt = load(RELEVANCE_PATH)
    assert receipt["artifact_hash"] == canonical_hash(receipt, "artifact_hash")
    parent = [tuple(edge) for edge in receipt["parent_edges"]]
    child = [tuple(edge) for edge in receipt["child_edges"]]
    child_index = {edge: bit for bit, edge in enumerate(child)}

    def lift(mask: int) -> int:
        return sum(
            1 << child_index[edge]
            for old_bit, edge in enumerate(parent)
            if (mask >> old_bit) & 1
        )

    def contains(minimals: list[int], subset: int) -> bool:
        return any(minimal & subset == minimal for minimal in minimals)

    recomputed = []
    for row in receipt["supported_cylinder_lifts"]:
        lifted = [lift(mask) for mask in row["parent_minimal_masks"]]
        assert lifted == row["child_cylinder_minimal_masks"]
        witnesses = [
            generator
            for generator in receipt["child_generator_pairs"]
            if contains(lifted, generator["row_mask"])
            and contains(lifted, generator["column_mask"])
        ]
        recomputed.append(bool(witnesses))
        assert witnesses == row["child_generator_witnesses"]

    assert receipt["summary"] == {
        "positive_weight_parent_support_count": 3,
        "child_relevant_lift_count": 2,
        "child_irrelevant_lift_count": 1,
        "lost_parent_minimal_masks": [2, 4],
        "lost_child_cylinder_minimal_masks": [4, 8],
    }
    assert recomputed == [True, True, False]
    assert "does not prove it is the unique cause" in receipt["mathematical_conclusion"]


def test_c041_trace_chronology_has_no_future_evidence_and_no_candidate() -> None:
    trace = load(TRACE_PATH)
    method_event = next(x for x in trace["entries"] if x["event_type"] == "METHOD_TRANSFER_REVIEW")
    assert DW_PATH.relative_to(ROOT).as_posix() not in method_event["evidence_pointers"]
    expert = next(x for x in trace["entries"] if x["event_type"] == "EXPERT_CONTEXT_REVIEW")
    memory = next(x for x in trace["entries"] if x["event_type"] == "EXPERIENCE_MEMORY_REVIEW")
    assert method_event["timestamp"] < expert["timestamp"] < memory["timestamp"]
    assert load(DW_PATH)["recorded_at"] < memory["timestamp"]
    assert load(APPLICABILITY_PATH)["recorded_at"] < memory["timestamp"]
    assert load(REVIEW_PATH)["recorded_at"] < expert["timestamp"]
    assert not any(x["event_type"] == "CANDIDATE_PROPOSED" for x in trace["entries"])


def test_c041_pre_action_uses_latest_framework_and_math_outcome_worlds() -> None:
    document = load(PRE_ACTION_PATH)
    schema = load(ROOT / "framework/RAKL/schemas/pre-action-fibre-receipt-v1.schema.json")
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(document)
    assert document["receipt_canonical_sha256"] == canonical_hash(
        document, "receipt_canonical_sha256", prefix=False
    )
    assert document["framework_commit"] == EXPECTED_FRAMEWORK
    assert document["application_commit"] == EXPECTED_APPLICATION
    assert subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", f"{EXPECTED_APPLICATION}:framework/RAKL"],
        check=True, stdout=subprocess.PIPE, text=True,
    ).stdout.strip() == EXPECTED_FRAMEWORK
    discriminator = document["predeclared_discriminator"]
    for world in (
        "RELEVANCE_FAILURE", "LIFTED_FEASIBILITY_FAILURE", "ZERO_AUGMENTATION",
        "RECURRENCE_BOUND_INSUFFICIENT", "RATE_FAILURE",
        "FINITE_GATE_SURVIVES_UNIVERSAL_UNPROVED", "CANNOT_CHECK",
    ):
        assert world in discriminator
    assert document["allowed_outcome_branches"] == [
        "SUCCESS", "PARTIAL_SUCCESS", "FAILURE", "BLOCKED", "UNKNOWN"
    ]
    root_binding = next(
        x for x in document["selected_retrievals"]
        if x["retrieval_id"] == "C041-ROOT-PRESERVATION"
    )
    assert root_binding["payload_hash"] == EXPECTED_PRESERVATION_SHA256
    assert "zero mathematical saturation credit" in discriminator


def test_c041_math_lessons_exclude_software_assurance_from_saturation() -> None:
    review = load(REVIEW_PATH)
    boundary = review["mathematical_lesson_boundary"]
    assert "exact counterexamples" in boundary["count_as_math"]
    assert "broken mathematical assumptions" in boundary["count_as_math"]
    assert "Git/PR/branch movement" in boundary["assurance_only"]
    assert "CI/test counts" in boundary["assurance_only"]
    assert "never contributes to mathematical knowledge or experience saturation" in boundary["rule"]
    assert review["review_authority"] == (
        "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW"
    )
    assert review["candidate_identity"] is None
    assert review["root_status"] == "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE"


def test_c041_atom_and_root_keep_local_math_separate_from_root_authority() -> None:
    atom = load(ATOM_PATH)
    size = load(SIZE_PATH)
    assert atom["artifact_hash"] == canonical_hash(atom, "artifact_hash")
    assert atom["size_rate_contract"]["artifact_hash"] == size["artifact_hash"]
    assert atom["authority_boundary"]["candidate_proposed"] is False
    root = root_value(load(ROOT_PATH))
    report = audit_root_coordinate_preservation(root)
    assert report.verdict is PreservationVerdict.INTERFACE_UNPROVED
    assert report.advances_root_claim is False
    assert report.surrogate_may_be_prioritized is True
    assert load(ROOT_PATH)["receipt_canonical_sha256"] == EXPECTED_PRESERVATION_SHA256
    assert set(report.unproved_interface_edge_ids) == {
        "C041-RCP-E4", "C041-RCP-E5", "C041-RCP-E6", "C041-RCP-E7"
    }
