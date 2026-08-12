from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"
EVALUATOR = BASE / "05_oracles/rh_ana003k_jy_c001_floor_ratio_evaluator.py"
ACTIVATION = BASE / "09_trace/RH_ANA_003k_JY_C001_FLOOR_RATIO_EXECUTION_ACTIVATION_20260812.json"
HAND_PROOF = BASE / "05_oracles/RH_ANA_003k_JY_C001_FLOOR_RATIO_HAND_PROOF_20260812T174900Z.json"
RESULT_FIXTURE = BASE / "09_trace/rh_ana003k_jy_floor_ratio_post_activation_result_fixture.py"


def evaluator():
    spec = importlib.util.spec_from_file_location("rh_ana003k_jy_c001_evaluator", EVALUATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def result_fixture():
    spec = importlib.util.spec_from_file_location("rh_ana003k_jy_c001_fresh_result", RESULT_FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_hash(value: dict) -> str:
    value = dict(value)
    value.pop("artifact_hash", None)
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_execution_activation_follows_merged_freeze_and_binds_exact_evaluator() -> None:
    activation = json.loads(ACTIVATION.read_text())
    assert activation["artifact_hash"] == canonical_hash(activation)
    assert activation["chronology"]["application_main_at_activation"] == "04d8ca7af5c007d3d5f93dd9f47b411a07e95822"
    assert activation["chronology"]["candidate_public_merge"] == "cde7c63769f35230be158f5525239287f51bfb09"
    assert activation["chronology"]["result_accessed"] is False
    assert all(binding["matches"] for binding in activation["verified_frozen_bindings"].values())
    assert activation["evaluator_implementation"]["raw_sha256"] == "sha256:" + hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    assert activation["authority"]["software_credit_units"] == 0


def test_record_checker_fails_closed_without_written_proof() -> None:
    module = evaluator()
    candidate, falsifier, checks = module.load_frozen_inputs(ROOT)
    observed = module.evaluate_rh_ana003k_jy_c001(
        candidate,
        falsifier,
        {"raw_identity_bindings_valid": all(checks.values())},
    )
    assert observed == "CANNOT_CHECK"


def test_post_activation_hand_proof_is_exact_and_precedes_computation() -> None:
    proof = json.loads(HAND_PROOF.read_text())
    assert proof["artifact_hash"] == canonical_hash(proof)
    chronology = proof["chronology"]
    assert chronology["result_round_base_sha"] == "c2479b8c258146be582306d6d75b8af6b3149a81"
    assert chronology["activation_public_merge_sha"] == "c2479b8c258146be582306d6d75b8af6b3149a81"
    assert chronology["record_checker_executed"] is False
    assert chronology["computation_used_in_derivation"] is False
    exact = proof["exact_hand_proof"]
    assert set(exact) == {
        "PO1-RATIO-ALGEBRA", "PO2-ELEMENTARY-LIMIT", "PO3-FIXED-C-QUANTIFIER",
        "PO4-FLOOR-CHAIN", "PO5-SUFFICIENT-SEARCH-BOUND", "PO6-EXPONENTIATION", "PO7-SCOPE",
    }
    assert "exp(t)>=t^3/6" in " ".join(exact["PO2-ELEMENTARY-LIMIT"])
    assert "O_C(log^2(n)/n^(1/3))" in " ".join(exact["PO3-FIXED-C-QUANTIFIER"])
    assert set(proof["proof_obligation_verdicts"].values()) == {"PASS_EXACT_HAND_PROOF"}
    assert proof["authority"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert proof["authority"]["software_credit_units"] == 0


def test_fresh_result_documents_are_deterministic_and_chronology_bound() -> None:
    module = result_fixture()
    documents = module.build_documents()
    for name, document in documents.items():
        assert json.loads((ROOT / module.PATHS[name]).read_text()) == document
        assert document["artifact_hash"] == canonical_hash(document)
    chronology = documents["result"]["chronology"]
    assert chronology["result_round_base_sha"] == "c2479b8c258146be582306d6d75b8af6b3149a81"
    assert chronology["activation_public_merge_sha"] == "c2479b8c258146be582306d6d75b8af6b3149a81"
    assert chronology["hand_proof_commit"] == "2cbc8c07c28707b90134445ca44a6aadd183b9ff"
    assert chronology["hand_proof_commit_precedes_record_checker_execution"] is True
    assert chronology["candidate_or_falsifier_mutated"] is False


def test_all_ten_frozen_worlds_match_and_computation_is_corroboration_only() -> None:
    machine = result_fixture().build_documents()["result"]["machine_validation_receipt"]
    assert machine["all_worlds_pass"] is True
    assert machine["overall_classification"] == "PASS_CANDIDATE_THEOREM"
    assert len(machine["worlds"]) == 10
    assert all(row["pass"] for row in machine["worlds"])
    assert set(machine["raw_identity_checks"].values()) == {True}
    assert machine["corroboration_only_not_proof"] is True
    raw = dict(machine)
    expected_hash = raw.pop("raw_execution_output_sha256")
    raw.pop("corroboration_only_not_proof")
    serialized = (json.dumps(raw, indent=2, sort_keys=True) + "\n").encode()
    assert expected_hash == "sha256:" + hashlib.sha256(serialized).hexdigest()


def test_exact_result_keeps_fixed_c_and_certificate_only_scope() -> None:
    result = result_fixture().build_documents()["result"]
    assert result["status"] == "PASS_FIXED_C_FLOOR_RATIO__CURRENT_SUFFICIENT_CERTIFICATE_INCOMPATIBILITY_ONLY"
    lineage = result["identity_lineage"]
    assert lineage["valid_final_result_identity_count"] == 1
    assert lineage["hand_proof_record_is_input_not_competing_final_result"] is True
    assert lineage["earlier_uncommitted_draft_status"] == "INVALID_CHRONOLOGY_NEVER_COMMITTED_OR_PUSHED_NOT_EVIDENCE"
    assert lineage["earlier_draft_content_used_as_evidence"] is False
    assert lineage["earlier_draft_identity_promoted_or_reused"] is False
    exact = result["exact_mathematical_result"]
    assert exact["asymptotic"] == (
        "For every fixed real C>0, rho_C(n)=O_C(log^2(n)/n^(1/3)) and rho_C(n)->0."
    )
    assert "no N uniform over unbounded C" in exact["quantifiers"]
    assert "does not certify" in exact["interpretation"]
    authority = result["authority"]
    assert authority["actual_jy_remainder"] is False
    assert authority["li_signs"] is False
    assert authority["riemann_hypothesis"] is False
    assert authority["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert result["credit"]["record_checker_computation_alone"] == 0
    assert result["credit"]["git_ci_schema_hash_runtime"] == 0


def test_seven_field_mathematical_lesson_is_substantive_and_zero_software_credit() -> None:
    lesson = result_fixture().build_documents()["lesson"]
    seven = lesson["seven_field_math_lesson"]
    assert set(seven) == {
        "attempted_implication", "exact_result_or_failure", "supported_and_competing_causes",
        "scope", "falsifier", "mathematical_repair", "proof_and_source_evidence",
    }
    assert all(seven.values())
    assert "fixed c" in seven["supported_and_competing_causes"].lower()
    assert "actual-remainder" in seven["scope"]
    assert "zero mathematical credit" in seven["proof_and_source_evidence"]
    assert lesson["deduplication"]["assurance_metadata_mathematical_credit"] == 0
    assert lesson["deduplication"]["global_ledger_updated"] is False


def test_result_trace_extends_frozen_candidate_hash_chain() -> None:
    module = result_fixture()
    trace = module.build_documents()["trace"]
    previous = module.PREVIOUS_EVENT_HASH
    assert [row["event_type"] for row in trace["entries"]] == [
        "FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"
    ]
    for row in trace["entries"]:
        assert row["previous_event_hash"] == previous
        previous = row["artifact_hash"]


def test_framework_revalidation_is_nonblocking_without_authority_inflation() -> None:
    module = result_fixture()
    record = module.build_documents()["framework_revalidation"]
    assert record["application_framework_pin"] == module.FRAMEWORK_PIN
    assert record["framework_origin_main_observed"] == module.FRAMEWORK_MAIN
    assert record["protected_mathematical_surface_changed_since_pin"] is False
    assert record["verdict"] == "CURRENT_NONBLOCKING_NO_NEW_APPLICABLE_CANONICAL_MATH_GATE"
    assert record["grants_mathematical_or_scientific_authority"] is False
