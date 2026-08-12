from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/rh_ana003k_jy_moving_diagonal_pre_candidate_fixture.py"


def fixture():
    spec = importlib.util.spec_from_file_location("rh_ana003k_pre", FIXTURE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load(path: str) -> dict:
    value = json.loads((ROOT / path).read_text())
    assert isinstance(value, dict)
    return value


def test_fixture_reproduces_all_hash_bound_artifacts() -> None:
    module = fixture()
    docs = module.build_all()
    assert set(docs) == set(module.PATHS.values())
    for path, expected in docs.items():
        assert load(path) == expected
        if "artifact_hash" in expected:
            assert expected["artifact_hash"] == module.hash_with_blank(expected, "artifact_hash")
    context = docs[module.PATHS["context"]]
    assert context["packet_hash"] == module.hash_with_blank(context, "packet_hash")
    tm = docs[module.PATHS["transformation_memory"]]
    assert tm["snapshot_hash"] == module.hash_with_blank(tm, "snapshot_hash")
    previous = ""
    for event in docs[module.PATHS["trace"]]["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == module.hash_with_blank(event, "artifact_hash")
        previous = event["artifact_hash"]


def test_current_v3_schemas_accept_context_memory_shortcut_and_trace() -> None:
    module = fixture()
    docs = module.build_all()
    schemas = {
        "context": "math-context-fiber.schema.json",
        "memory": "research-memory-review.schema.json",
        "transformation_memory": "obstruction-transformation-memory.schema.json",
        "shortcut": "obstruction-transformation-review.schema.json",
        "trace": "math-research-trace.schema.json",
    }
    for name, schema_name in schemas.items():
        schema = load(f"framework/RAKL/schemas/{schema_name}")
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(docs[module.PATHS[name]])


def test_object_and_scope_are_moving_diagonal_pre_candidate_only() -> None:
    module = fixture()
    docs = module.build_all()
    atom = docs[module.PATHS["atomization"]]
    assert atom["candidate_generation_allowed"] is False
    assert atom["blockers"] == [
        "epsilon_n not selected",
        "diagonal constant C not selected",
        "symbolic discriminator not executed",
    ]
    gate = docs[module.PATHS["gate"]]
    assert gate["application_base_sha"] == "80f8fb5e8c8417bd045cfae9c31df0a19e670eac"
    assert gate["framework_sha"] == "d21592b0ff8da988deabb923fd549891ff8ad9f0"
    assert gate["candidate_generation_allowed"] is False
    assert gate["chronology"] == {
        "candidate_identity": None,
        "epsilon_sequence_identity": None,
        "diagonal_constant_identity": None,
        "discriminator_executed": False,
        "result_accessed": False,
    }


def test_source_deductions_preserve_sufficient_versus_necessary_boundary() -> None:
    module = fixture()
    docs = module.build_all()
    source = docs[module.PATHS["source"]]
    text = " ".join(source["source_facts"] + source["context_deductions_to_freeze_not_evaluate"])
    assert "u_n=log Y_n" in text
    assert "tilde_m_JY>=ceil(U_JY)" in text
    assert "rho_C(n)" in text
    context = docs[module.PATHS["context"]]
    assert "sufficient versus necessary thresholds" in context["structural_coordinates"]
    disanalogies = " ".join(context["explicit_disanalogies"])
    assert "sufficient threshold is not necessary" in disanalogies
    assert "failure of the current certificate is not RH refutation" in disanalogies


def test_dual_memory_and_search_route_are_bound() -> None:
    module = fixture()
    docs = module.build_all()
    memory = docs[module.PATHS["memory"]]
    assert memory["tool_query_status"] == "MATCHES_FOUND"
    assert memory["failure_query_status"] == "MATCHES_FOUND"
    assert memory["selected_tool_ids"] == ["T-RH-JY-C001-FIXED-N-SUFFICIENT-TILDE-M"]
    assert "F-RH-SUFFICIENT-CERTIFICATE-NOT-NECESSARY" in memory["relevant_failure_ids"]
    shortcut = docs[module.PATHS["shortcut"]]
    assert shortcut["selected_mode"] == "SEARCH"
    assert shortcut["direct_search_status"] == "MATCHES_FOUND"
    assert shortcut["jump_search_status"] == "NOT_RUN"
    assert shortcut["glue_search_status"] == "NOT_RUN"
    witness = shortcut["direct_mapping_witnesses"][0]
    assert witness["unmatched_source_preconditions"] == [
        "epsilon_n and exact diagonal/C are not frozen"
    ]


def test_discriminator_freezes_branches_and_falsifiers_without_execution() -> None:
    module = fixture()
    docs = module.build_all()
    discriminator = docs[module.PATHS["discriminator"]]
    assert discriminator["status"] == "FROZEN_NOT_EXECUTED_NO_BRANCH_SELECTED"
    assert discriminator["candidate_identity"] is None
    assert discriminator["unselected_parameters"] == {
        "epsilon_sequence": None,
        "diagonal_family": None,
        "diagonal_constant_C": None,
    }
    branches = {row["branch"] for row in discriminator["allowed_future_branches"]}
    assert branches == {
        "PASS_FLOOR_COMPATIBLE",
        "FAIL_CURRENT_SUFFICIENT_CERTIFICATE_GROWTH",
        "PASS_FULL_DIAGONAL_COMPATIBILITY",
        "FAIL_EPSILON_DEPENDENT_EXCESS",
        "CANNOT_CHECK",
    }
    assert len(discriminator["planted_falsifiers"]) == 6
    assert all(value is False for value in discriminator["execution_firewall"].values())
    assert "not claimed" not in discriminator["symbolic_probe"]["future_proof_obligation"]
    full_branch = next(
        row
        for row in discriminator["allowed_future_branches"]
        if row["branch"] == "PASS_FULL_DIAGONAL_COMPATIBILITY"
    )
    assert "log diagonal log Y_n" in full_branch["condition"]
    expert = docs[module.PATHS["expert"]]
    assert "log diagonal log Y_n" in expert["mathematical_lesson_fields"]["mathematical_falsifier"]
    source = docs[module.PATHS["source"]]
    assert "log diagonal log Y_n" in source["method_transfer_matrix"][0]["repair_question"]


def test_expert_review_and_trace_credit_only_math_context() -> None:
    module = fixture()
    docs = module.build_all()
    expert = docs[module.PATHS["expert"]]
    assert expert["review_authority"] == "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT_REVIEW"
    assert len(expert["lenses"]) == 5
    assert "sufficient modulus can fail" in expert["strongest_objection"]
    lesson = expert["mathematical_lesson_fields"]
    assert set(lesson) == {
        "attempted_mathematical_implication",
        "exact_mathematical_result_or_failure",
        "supported_causes",
        "competing_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_new_mathematical_move",
        "proof_or_source_evidence",
    }
    assert all(lesson[field] for field in lesson)
    assert "No diagonal result is evaluated here" in lesson["exact_mathematical_result_or_failure"]
    assert "do not infer actual remainder failure" in lesson["repair_or_new_mathematical_move"]
    assert expert["nonmathematical_credit"].startswith("ZERO")
    trace = docs[module.PATHS["trace"]]
    assert [event["event_type"] for event in trace["entries"]] == [
        "ATOMIZED", "CONTEXT_FROZEN", "ANALOGY_SCAN", "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW", "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW", "NEXT_STEP_PROPOSED",
    ]
    assert all("PRE_CANDIDATE_ONLY" in event["outputs"] for event in trace["entries"])
    assert all("ZERO_SOFTWARE_MATH_CREDIT" in event["outputs"] for event in trace["entries"])
    assert all(event["event_type"] not in {"CANDIDATE_PROPOSED", "FALSIFIER_RUN", "RESULT_RECORDED"} for event in trace["entries"])
