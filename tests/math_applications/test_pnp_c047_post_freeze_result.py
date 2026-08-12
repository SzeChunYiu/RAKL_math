from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
from rakl.failure_lattice import FailureDiagnosisStatus, FailureRelation, reconstruct_failure_lattice


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c047_orientation_repair_result_fixture.py"
RESULT = PNP / "05_falsification/O9d12a2a1b_C047_ORIENTATION_FEASIBILITY_PROOF_CHECK_RESULT_20260812.json"
FAILURE = PNP / "07_memory/O9d12a2a1b_C047_ORIENTATION_REPAIR_FAILURE_EXPERIENCE_DELTA_20260812.json"
SATURATION = PNP / "10_case_study/C047_ORIENTATION_REPAIR_MATHEMATICAL_SATURATION_RECEIPT_20260812.json"
EPISODE = PNP / "10_case_study/C047_ORIENTATION_REPAIR_TASK_EPISODE_20260812.json"
TRACE = PNP / "09_trace/O9d12a2a1b_C047_POST_FREEZE_RESULT_TRACE_20260812.json"


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_c047_result_matches_exact_post_public_freeze_fixture() -> None:
    fixture = _module("pnp_c047_result", FIXTURE)
    expected = fixture.build_documents(ROOT)
    assert _load(RESULT) == expected["result"]
    assert _load(FAILURE) == expected["failure"]
    assert _load(SATURATION) == expected["saturation"]
    assert _load(EPISODE) == expected["episode"]
    assert _load(TRACE) == expected["trace"]
    result = expected["result"]
    assert result["chronology"]["public_proof_input_freeze"]["remote_head_sha"] == "95ac661de3dce2c100ff9ed34e531becb47d7d92"
    assert result["chronology"]["evaluation_strictly_after_public_input_freeze"] is True
    assert result["execution"]["raw_output_sha256"] == "8de95b41966c74771f74f4dd5831c2c1fcb8d19ff30068428a84348749e3b105"


def test_c047_mathematical_result_and_authority_are_narrow() -> None:
    result = _load(RESULT)
    assert result["mathematical_result"]["failed_repair"] == "quadrant orientation alone, with prefix r kept as the fresh-row coordinate"
    assert "shifts the fixed MAGIC header" in result["mathematical_result"]["bounded_failure_cause"]
    assert "suffix-to-row literal transpose" in result["mathematical_result"]["repair_condition"]
    assert result["target_access"] == {
        "proof_obligation_evaluator_imported_and_executed": True,
        "target_decoder_imported_or_executed": False,
        "later_target_enumerated": False,
        "later_target_result_accessed": False,
        "finite_collision_level_selected": False,
    }
    assert result["authority"] == {
        "same_context_hand_derivation_record_check": True,
        "theorem_truth": False,
        "formal_proof": False,
        "independent_review": False,
        "novelty": False,
        "cover_or_circuit_lower_bound": False,
        "p_vs_np_authority": False,
        "root_status": "OPEN",
    }


def test_c047_evaluator_retains_pass_fail_and_cannot_check() -> None:
    fixture = _module("pnp_c047_result_branches", FIXTURE)
    certificate = _load(fixture.CERTIFICATE_PATH)
    authorization = _load(fixture.AUTHORIZATION_PATH)
    evaluator = fixture.load_exact_evaluator(ROOT)
    assert evaluator.evaluate_certificate(certificate, {}) == {"verdict": "CANNOT_CHECK", "reason": "SEPARATE_POST_FREEZE_AUTHORIZATION_REQUIRED"}
    refuted = json.loads(json.dumps(certificate))
    refuted["obligations"][3]["status"] = "REFUTED"
    assert evaluator.evaluate_certificate(refuted, authorization) == {"verdict": "FAIL", "falsified_obligation": "BINARY_HEADER_DISJOINTNESS"}
    assert evaluator.evaluate_certificate(certificate, authorization)["verdict"] == "PASS"


def test_c047_failure_lattice_is_runtime_and_schema_valid() -> None:
    document = _load(FAILURE)
    schema = _load(ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json")
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(document)
    lattice = reconstruct_failure_lattice(document)
    c047 = next(item for item in lattice.experiences if item.failure_id == "F-PNP-C047-ORIENTATION-ONLY-INTERFACE-MISALIGNMENT")
    assert c047.diagnosis_status is FailureDiagnosisStatus.SUPPORTED
    assert "does not" not in c047.selected_diagnosis.lower() or "without identifying" in c047.selected_diagnosis.lower()
    assert lattice.links[0].relation is FailureRelation.CONTEXT_SPECIALIZATION_OF
    assert lattice.links[0].target_id == "F-PNP-C045-U17-COUPLING-HYPOTHESIS-REFUTED"


def test_c047_trace_is_hash_chained_through_residual() -> None:
    trace = _load(TRACE)
    assert [entry["event_type"] for entry in trace["entries"][-3:]] == ["FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED"]
    for previous, current in zip(trace["entries"], trace["entries"][1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    assert trace["entries"][-1]["outputs"] == ["C048_PROPOSED_TARGET_BLIND", "NO_TARGET_ACCESS"]


def test_c047_math_credit_excludes_software_and_feedback_is_proposal_only() -> None:
    saturation = _load(SATURATION)
    assert saturation["mathematical_credit"]["orientation_only_impossibility_lemma"] is True
    assert saturation["mathematical_credit"]["exact_binary_header_falsifier"] is True
    assert saturation["mathematical_credit"]["software_schema_hash_chronology_ci_pr_credit"] == 0
    assert saturation["failure_cause"]["status"] == "SUPPORTED_BOUNDED"
    assert saturation["failure_cause"]["unique_global_cause_claimed"] is False
    assert saturation["framework_feedback"]["status"] == "PROPOSAL_ONLY_APPLICATION_FEEDBACK"
    assert saturation["framework_feedback"]["framework_authority"] == "NONE"
    assert saturation["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_c047_result_fixture_has_no_target_capability() -> None:
    source = FIXTURE.read_text(encoding="utf-8")
    for forbidden in ("C041_fx_sat_one_sided", "decode_formula", "is_satisfiable", "materialize_complement", "subprocess"):
        assert forbidden not in source
