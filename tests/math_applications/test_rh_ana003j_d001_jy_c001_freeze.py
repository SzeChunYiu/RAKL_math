from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/rh_ana003j_d001_jy_c001_freeze_fixture.py"


def fixture():
    spec = importlib.util.spec_from_file_location("rh_jy_c001_freeze", FIXTURE)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def load(path: str | Path) -> dict:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_fixture_reproduces_all_artifacts_and_content_hashes() -> None:
    module = fixture()
    expected = module.build_all()
    assert set(expected) == set(module.PATHS.values())
    for relative, value in expected.items():
        assert load(relative) == value
    for name in ("candidate", "falsifier", "validation_inputs"):
        document = expected[module.PATHS[name]]
        assert document["artifact_hash"] == module.canonical_hash(document)
    previous = ""
    for event in expected[module.PATHS["trace"]]["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == module.canonical_hash(event)
        previous = event["artifact_hash"]


def test_extended_trace_conforms_to_pinned_framework_schema() -> None:
    module = fixture()
    trace = module.build_all()[module.PATHS["trace"]]
    schema = load("framework/RAKL/schemas/math-research-trace.schema.json")
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(trace)


def test_exact_main_evidence_and_framework_pin_are_frozen() -> None:
    module = fixture()
    candidate = module.build_all()[module.PATHS["candidate"]]
    assert candidate["chronology"]["application_base_sha"] == (
        "334c3cf0a405906fe14b07067d6d7f73b6170d4f"
    )
    assert candidate["chronology"]["source_assimilation_commit_sha"] == (
        "93ff7026d27a1cf1b4f698448e7a8501b04a07b7"
    )
    assert candidate["chronology"]["framework_pin_sha"] == (
        "d21592b0ff8da988deabb923fd549891ff8ad9f0"
    )
    for name, binding in candidate["evidence_bindings"].items():
        assert binding["raw_sha256"] == module.EXPECTED_RAW_SHA256[name]
        assert hashlib.sha256((ROOT / binding["path"]).read_bytes()).hexdigest() == (
            binding["raw_sha256"]
        )
    pin = load("config/rakl-framework-pin.json")
    assert pin["commit"] == module.FRAMEWORK_SHA
    gitlink = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD:framework/RAKL"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    assert gitlink == module.FRAMEWORK_SHA


def test_exact_direct_envelope_normalization_and_modulus_are_frozen_symbolically() -> None:
    module = fixture()
    candidate = module.build_all()[module.PATHS["candidate"]]
    source = candidate["primary_source"]
    assert source["pdf_sha256"] == (
        "565993a6def48b237a68a92acba604f2c42f99165e0e71e390f8e21a313b74b2"
    )
    assert source["exact_decimal_constants"] == {
        "amplitude": "9.39",
        "log_power_a": "1.515",
        "sqrt_log_decay_c": "0.8274",
        "x_threshold": "2",
    }
    assert candidate["normalization"]["application_source"] == (
        "A(x)=floor(x)-psi(x)"
    )
    assert candidate["normalization"]["required_transfer"] == (
        "|A(x)| <= 1 + |psi(x)-x|"
    )
    assert candidate["normalization"]["floor_error_one_is_mandatory"] is True
    definitions = candidate["exact_definitions"]
    assert definitions["h"] == "h_(n,j)=binom(n,j+1)/j!"
    assert definitions["q"] == "q_(n,j)=binom(n+1,j+2)/j!"
    envelope = candidate["candidate_envelope"]
    assert "2j+5.03" in envelope["specialized_integral_identity"]
    assert "18.78" in envelope["formula"]
    assert "[2(n-1+1.515)/0.8274]^2" in envelope["monotonicity_floor"]
    modulus = envelope["symbolic_modulus"]
    assert "least integer" in modulus["log_threshold"]
    assert modulus["threshold"] == "M_JY(n,epsilon)=exp(m_JY(n,epsilon))"
    assert modulus["evaluation_status"] == "SYMBOLIC_DEFINITION_ONLY_NOT_EVALUATED"


def test_hostile_cross_check_is_independent_and_bellotti_is_not_spliced() -> None:
    module = fixture()
    candidate = module.build_all()[module.PATHS["candidate"]]
    cross_check = candidate["independent_hostile_cross_check"]
    assert cross_check["constants"] == {
        "K": "172",
        "decay": "0.4",
        "x_threshold": "2",
    }
    assert cross_check["decay_gap"] == "D=0.8274-0.4=0.4274"
    assert cross_check["maximizer"] == "v*=3.03/D"
    assert cross_check["maximum"].endswith("=171.43357721989227<172")
    assert "not 2D" in cross_check["denominator_guard"]
    bellotti = candidate["bellotti_boundary"]
    assert bellotti["status"] == (
        "EFFECTIVE_BUT_CONSTANT_AND_THRESHOLD_UNEXPOSED_IN_ACQUIRED_TEXT"
    )
    assert bellotti["ineffectivity_claimed"] is False
    forbidden = " ".join(bellotti["mixing_forbidden"])
    assert "exp(55A_0)" in forbidden
    assert "Bellotti's K_B" in forbidden
    assert candidate["comparison_boundary"]["direct_versus_simple_order_claim"] == (
        "NONE_FROZEN_OR_AUTHORIZED"
    )


def test_planted_worlds_cover_pass_fail_and_cannot_check_without_execution() -> None:
    module = fixture()
    docs = module.build_all()
    falsifier = docs[module.PATHS["falsifier"]]
    worlds = {world["world_id"]: world for world in falsifier["worlds"]}
    assert len(worlds) == 15
    assert {
        world["expected_future_classification"] for world in worlds.values()
    } == {"PASS", "FAIL", "CANNOT_CHECK"}
    assert sum(
        world["expected_future_classification"] == "FAIL" for world in worlds.values()
    ) == 10
    assert sum(
        world["expected_future_classification"] == "CANNOT_CHECK"
        for world in worlds.values()
    ) == 4
    assert worlds["CONTROL-EXACT-DIRECT-FORMULA"]["expected_future_classification"] == (
        "PASS"
    )
    assert "2j+4.03" in worlds["ALG-WRONG-GAMMA-ORDER"]["input_mutation"]
    assert "additive floor-error one" in worlds["NORM-OMIT-FLOOR-ONE"][
        "input_mutation"
    ]
    assert "+1.515" in worlds["MONO-DROP-LOG-POWER"]["classification_basis"]
    assert "exp(55A_0)" in worlds["SOURCE-MIX-BELLOTTI-FACTORS"][
        "input_mutation"
    ]
    assert falsifier["future_evaluator_contract"]["implementation_path"] is None
    assert falsifier["future_evaluator_contract"]["execution_authorized_this_round"] is False
    assert falsifier["result_state"] == "NO_FALSIFIER_RUN_NO_RESULT_CLASSIFICATION"


def test_public_inputs_are_exact_symbolic_constructors_not_evaluated_values() -> None:
    module = fixture()
    inputs = module.build_all()[module.PATHS["validation_inputs"]]
    assert inputs["construction_rules"]["n_values"] == [1, 2, 3, 5]
    assert inputs["construction_rules"]["u_values_for_each_n"] == [
        "U_JY(n)",
        "ceil(U_JY(n))",
        "ceil(U_JY(n))+1",
    ]
    assert len(inputs["inputs"]) == 12
    assert {row["n"] for row in inputs["inputs"]} == {1, 2, 3, 5}
    assert all(row["u_decimal_value"] is None for row in inputs["inputs"])
    assert all(row["B_JY_value"] is None for row in inputs["inputs"])
    assert all(row["M_JY_value"] is None for row in inputs["inputs"])
    checks = " ".join(inputs["intended_future_checks"])
    for required in (
        "coefficient identity",
        "incomplete-gamma identity",
        "nonnegative",
        "monotonicity",
        "endpoint extension",
    ):
        assert required in checks
    assert inputs["numeric_precision_contract"]["status"] == "NOT_FROZEN_IN_THIS_ROUND"
    assert inputs["comparison_rule"].startswith("Do not classify")


def test_freeze_firewall_and_trace_have_no_result_authority() -> None:
    module = fixture()
    docs = module.build_all()
    candidate = docs[module.PATHS["candidate"]]
    firewall = candidate["evaluation_firewall"]
    assert all(value is False for value in firewall.values() if isinstance(value, bool))
    assert firewall["epsilon_sequence_identity"] is None
    assert firewall["diagonal_cutoff_constant_identity"] is None
    authority = candidate["authority"]
    assert authority["candidate_proposal_only"] is True
    assert authority["mathematical_result"] is False
    assert authority["novelty"] is False
    assert authority["independent_review"] is False
    assert authority["li_positivity"] is False
    assert authority["riemann_hypothesis"] is False
    trace = docs[module.PATHS["trace"]]
    assert [event["event_type"] for event in trace["entries"]][-2:] == [
        "NEXT_STEP_PROPOSED",
        "CANDIDATE_PROPOSED",
    ]
    last = trace["entries"][-1]
    assert "NO_FALSIFIER_RUN" in last["outputs"]
    assert "ZERO_MATHEMATICAL_RESULT_CREDIT" in last["outputs"]
    assert all(event["event_type"] != "FALSIFIER_RUN" for event in trace["entries"])
