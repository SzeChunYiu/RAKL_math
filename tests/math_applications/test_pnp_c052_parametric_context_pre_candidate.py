from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.failure_lattice import ReuseVerdict
from rakl.framework_candidate_freeze import CandidateFreezeRevalidationVerdict
from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import ResearchTraceEventType, TraceGateVerdict, audit_pre_candidate_trace
from rakl.root_coordinate_preservation import PreservationGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict

ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c052_parametric_context_pre_candidate_fixture.py"
PREACTION = PNP / "09_trace/O9d12a2a1b_C052_PARAMETRIC_RESIDUE_PRE_ACTION_20260812.json"
PREACTION_FIXTURE = PNP / "09_trace/c052_parametric_residue_preaction_fixture.py"
PREACTION_TEST = ROOT / "tests/math_applications/test_pnp_c052_parametric_residue_preaction.py"


def module():
    spec = importlib.util.spec_from_file_location("pnp_c052_context_pre", FIXTURE)
    assert spec is not None and spec.loader is not None
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def raw_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_c052_gate_passes_but_licenses_identity_freeze_only() -> None:
    m = module()
    plan, fiber, memory, tm, shortcut, trace, _ = m.build_current_gate_plan()
    assert m.APPLICATION_BASE_SHA == "b7ca6ac51fa8319b559e95402c47959c626f284a"
    assert m.FRAMEWORK_CURRENT_SHA == "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
    assert m.FRAMEWORK_PIN_SHA == "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.framework_subject_gate.verdict is CandidateFreezeRevalidationVerdict.CURRENT_UNCHANGED
    assert plan.candidate_generation_allowed is True
    assert shortcut.selected_mode is ShortcutMode.SEARCH
    assert shortcut.selected_episode_ids == (
        "E-PNP-C052-REPARAMETERIZE-BY-SUPPORT-AND-TOKEN-PHASE",
    )
    assert fiber.first_candidate_at is None
    assert tm.snapshot_hash == shortcut.episode_memory_snapshot_hash
    assert audit_pre_candidate_trace(
        trace,
        atom_id=m.ATOM,
        context_packet_hash=fiber.packet_hash,
        obstruction_transformation_review_hash=shortcut.artifact_hash,
    ).verdict is TraceGateVerdict.PASS
    assert memory.relevant_failure_ids == (
        "F-PNP-C050-K15-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
        "F-PNP-C051-K19-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
    )


def test_c052_documents_match_fixture_and_pinned_schemas() -> None:
    m = module()
    expected = m.build_documents()
    assert set(expected) == set(m.PATHS)
    for name, relative in m.PATHS.items():
        assert load(ROOT / relative) == expected[name]
    schemas = {
        "context": "math-context-fiber.schema.json",
        "memory": "research-memory-review.schema.json",
        "transformation_memory": "obstruction-transformation-memory.schema.json",
        "shortcut_review": "obstruction-transformation-review.schema.json",
        "preservation": "root-coordinate-preservation-receipt-v1.schema.json",
        "trace": "math-research-trace.schema.json",
    }
    for name, schema_name in schemas.items():
        jsonschema.Draft202012Validator(
            load(ROOT / "framework/RAKL/schemas" / schema_name),
            format_checker=jsonschema.FormatChecker(),
        ).validate(expected[name])


def test_c052_quantifier_domain_and_latest_fail_closed_semantics_are_explicit() -> None:
    m = module()
    docs = m.build_documents()
    context = docs["context"]
    joined = " ".join(context["structural_coordinates"])
    for required in (
        "bit_length(v)",
        "bit_length(m)",
        "6+2a+2b",
        "3m w(a)",
        "R(a,b,m) mod 2",
        "E(a,b,m)=2k",
        "E(a_plus,b_plus,m_plus)=2(k+1)",
        "phi_c0=(k-H(a,b)) mod w(a)",
        "h[j]=x[k+j-1]",
        "MAGIC=11100101",
    ):
        assert required in joined
    assert "c[0]=x[k]" in joined and "equivalently h[1]" in joined
    assert "h[0]=1 is prepended" in joined
    assert "every v with 2^(a-1)<=v<=2^a-1" in joined
    assert "every legal literal index and sign" in joined
    witness = docs["quantifier_witness"]
    assert witness["schema_version"] == "quantifier-compatibility-witness-v1"
    assert witness["point_global_scope"] == "MISALIGNED"
    assert witness["point_global_substitution_permitted"] == "YES"
    assert witness["gluing_status"] == "CONDITIONAL"
    assert witness["condition"]
    assert witness["required_scope_witness"] not in {"UNKNOWN", "NOT_APPLICABLE"}
    assert witness["unknown_fields"] == []
    assert witness["misaligned_axes_without_substitution"] == []
    content = dict(witness)
    claimed = content.pop("witness_canonical_sha256")
    raw = json.dumps(content, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert hashlib.sha256(raw).hexdigest() == claimed
    binding_text = json.dumps(docs["framework_binding"], sort_keys=True)
    assert "src/rakl/quantifier_compatibility.py" in binding_text
    assert m.FRAMEWORK_QUANTIFIER_RUNTIME_SHA256 in binding_text
    assert m.FRAMEWORK_QUANTIFIER_SCHEMA_SHA256 in binding_text


def test_c052_exact_difference_witnesses_cover_both_parent_failures() -> None:
    m = module()
    docs = m.build_documents()
    witnesses, assessments, expected_snapshot = m.failure_reuse_bundle(docs["context"]["packet_hash"])
    assert docs["failure_snapshot"] == expected_snapshot
    assert len(witnesses) == len(assessments) == 2
    assert all(item.verdict is ReuseVerdict.DIFFERENCE_WITNESSED for item in assessments)
    assert {item.prior_failure_ids for item in witnesses} == {
        ("F-PNP-C050-K15-FIXED-VARIABLE-BIT-VERSUS-MAGIC",),
        ("F-PNP-C051-K19-FIXED-VARIABLE-BIT-VERSUS-MAGIC",),
    }
    for witness in witnesses:
        assert witness.changed_structural_coordinates
        assert witness.restored_or_replaced_assumptions
        assert witness.prior_falsifier_escape_reason.startswith("C052 does not assert escape")
        assert "must reproduce" in witness.cheapest_repeat_failure_test
    snapshot = docs["failure_snapshot"]
    assert len(snapshot["registered_failures"]) == 2
    assert snapshot["new_level_result_accessed"] is False
    assert snapshot["mathematical_credit"] is False


def test_c052_lessons_are_mathematical_seven_field_records() -> None:
    docs = module().build_documents()
    source = docs["source_packet"]
    required = {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "proof_and_source_evidence",
        "falsifier",
        "mathematical_repair",
    }
    lessons = source["parent_seven_field_mathematical_lessons"]
    assert {item["source_atom"] for item in lessons} == {
        "O9d12a2a1b-C050",
        "O9d12a2a1b-C051",
    }
    assert all(set(item["fields"]) == required for item in lessons)
    combined = json.dumps(lessons, sort_keys=True)
    assert "h[3]=1" in combined and "MAGIC[3]=0" in combined
    assert source["credit"] == {
        "git_ci_schema_hash_chronology": 0,
        "independent_review": 0,
        "mathematical_results": 0,
    }
    expert = docs["expert_review"]
    assert len(expert["role_reviews"]) == 7
    assert "does not license a universal quantifier" in expert["strongest_objection"]
    assert expert["independent_review_credit"] == 0
    assert expert["mathematical_result_credit"] is False


def test_c052_has_no_candidate_result_or_target_capability() -> None:
    docs = module().build_documents()
    atom = docs["atomization"]
    gate = docs["gate"]
    assert atom["candidate_proposed"] is False
    assert atom["classifier_identity"] is None
    assert atom["falsifier_identity"] is None
    assert atom["new_level_result_accessed"] is False
    assert atom["target_k_selected"] is False
    assert gate["gate_verdicts"]["licensed_action"] == (
        "FREEZE_C052_TARGET_BLIND_CLASSIFIER_AND_INDEPENDENT_FALSIFIER_IDENTITIES_ONLY"
    )
    assert gate["application_authority"]["only_identity_freeze_authorized"] is True
    for field in (
        "classifier_execution_authorized",
        "falsifier_execution_authorized",
        "new_k_enumeration_authorized",
        "target_k_selection_authorized",
        "decoder_sat_overlap_access_authorized",
        "parametric_theorem_candidate_authorized",
    ):
        assert gate["application_authority"][field] is False
    events = [entry["event_type"] for entry in docs["trace"]["entries"]]
    assert events == [
        ResearchTraceEventType.ATOMIZED.value,
        ResearchTraceEventType.CONTEXT_FROZEN.value,
        ResearchTraceEventType.ANALOGY_SCAN.value,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW.value,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW.value,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW.value,
        ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW.value,
        ResearchTraceEventType.NEXT_STEP_PROPOSED.value,
    ]
    assert ResearchTraceEventType.CANDIDATE_PROPOSED.value not in events
    assert ResearchTraceEventType.RESULT_RECORDED.value not in events
    text = FIXTURE.read_text(encoding="utf-8")
    for forbidden in (
        "from C041_fx_sat_one_sided",
        "import C041_fx_sat_one_sided",
        "decode_formula(",
        "is_satisfiable(",
        "materialize_complement(",
        "import subprocess",
        "import z3",
        "import pysat",
    ):
        assert forbidden not in text


def test_c052_trace_hash_chain_and_parent_preaction_are_immutable() -> None:
    docs = module().build_documents()
    entries = docs["trace"]["entries"]
    assert entries[0]["previous_event_hash"] == ""
    assert all(entries[index]["previous_event_hash"] == entries[index - 1]["artifact_hash"] for index in range(1, len(entries)))
    assert raw_sha256(PREACTION) == "b90b1fa2899319ad9365593c6b8ffd86aec6b81deba52fac5b84a4ef28f9e974"
    assert raw_sha256(PREACTION_FIXTURE) == "f4a38c5ac3833c76a11ae62847060ad80c6dcdf1b71987ca957203d7407ad65a"
    assert raw_sha256(PREACTION_TEST) == "9374c3c24a1a355e9347fa0327edc5805aa27e5e08f2c75198f7f1950d70deb5"
