from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c050_k15_candidate_freeze_fixture.py"
VERIFIER = PNP / "09_trace/verify_c050_k15_candidate_freeze.py"
EVALUATOR = PNP / "05_falsification/c050_k15_alignment_inert_evaluator.py"
ARTIFACTS = {
    "candidate": PNP / "04_candidates/O9d12a2a1b_C050_K15_SELECTOR_DISCRIMINATOR_FREEZE_20260812.json",
    "manifest": PNP / "05_falsification/O9d12a2a1b_C050_K15_ALIGNMENT_EVALUATOR_FREEZE_20260812.json",
    "authorization": PNP / "09_trace/O9d12a2a1b_C050_K15_EVALUATION_AUTHORIZATION_20260812.json",
    "framework_binding": PNP / "09_trace/O9d12a2a1b_C050_K15_FRAMEWORK_SUBJECT_FREEZE_BINDING_20260812.json",
    "framework_observation": PNP / "09_trace/O9d12a2a1b_C050_K15_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C050_K15_CANDIDATE_FREEZE_TRACE_20260812.json",
    "receipt": PNP / "09_trace/O9d12a2a1b_C050_K15_CANDIDATE_FREEZE_RECEIPT_20260812.json",
}


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _encoded_length(v: int, m: int) -> tuple[int, int, bool]:
    raw = 8 + (2 * v.bit_length() - 1) + (2 * m.bit_length() - 1) + 3 * m * (
        1 + v.bit_length()
    )
    return raw, raw + raw % 2, bool(raw % 2)


def test_candidate_freeze_documents_are_exact_fixture_outputs() -> None:
    fixture = _module("pnp_c050_k15_fixture", FIXTURE)
    assert {name: _load(path) for name, path in ARTIFACTS.items()} == fixture.build_documents()


def test_source_only_selector_proves_k15_without_overlap_access() -> None:
    candidate = _load(ARTIFACTS["candidate"])
    selector = candidate["selector"]
    assert selector["selected_k"] == 15
    assert selector["eligible_domain"] == "integers k>=14; the quarantined family is excluded by process identity, not by its mathematical content"
    assert selector["uses_overlap_bits"] is False
    assert selector["uses_decoder_or_evaluator"] is False
    assert selector["uses_target_result"] is False
    assert selector["length_function"] == (
        "R(v,m)=8+(2*bit_length(v)-1)+(2*bit_length(m)-1)+"
        "3*m*(1+bit_length(v)); E(v,m)=R(v,m)+(R(v,m) mod 2)"
    )

    proof = candidate["selector_proof"]
    assert proof["unsat_clause_lower_bound"] == "Every one-clause 3CNF is satisfiable, so canonical UNSAT requires m>=2."
    assert proof["length_28_impossibility"]["v_eq_1"] == {
        "E_1_2": 24,
        "E_1_3": 30,
        "monotonic_for_m_ge_3": True,
    }
    assert proof["length_28_impossibility"]["v_ge_2_m_ge_2_minimum"] == {
        "attained_at": [2, 2],
        "encoded_length": 32,
    }
    assert proof["length_30_unsat_capable_regime"]["parameters"] == {"v": 1, "m": 3}
    assert proof["length_30_unsat_capable_regime"]["raw_length"] == 30
    assert proof["length_30_unsat_capable_regime"]["padding"] is False
    assert proof["length_30_unsat_capable_regime"]["unsat_proof"] == (
        "The first two clauses force z and not-z respectively; the third clause is redundant, so no assignment satisfies all three."
    )

    assert _encoded_length(1, 2) == (24, 24, False)
    assert _encoded_length(1, 3) == (30, 30, False)
    assert _encoded_length(2, 2) == (32, 32, False)
    assert all(_encoded_length(v, 2)[1] >= 32 for v in range(2, 64))


def test_all_length_32_canonical_parameter_branches_are_frozen() -> None:
    candidate = _load(ARTIFACTS["candidate"])
    expected = [
        {"v_range": [2, 3], "m": 2, "raw_length": 32, "padding": False},
        {"v_range": [8, 15], "m": 1, "raw_length": 31, "encoded_length": 32, "padding": True},
    ]
    assert candidate["selector_proof"]["length_32_canonical_regimes"] == expected

    actual = []
    for v in range(1, 64):
        for m in range(1, 16):
            raw, encoded, padded = _encoded_length(v, m)
            if encoded == 32:
                actual.append((v, m, raw, padded))
    asserted = [
        (v, row["m"], row["raw_length"], row["padding"])
        for row in expected
        for v in range(row["v_range"][0], row["v_range"][1] + 1)
    ]
    assert asserted == actual


def test_discriminator_is_two_sided_and_does_not_predict_target_result() -> None:
    candidate = _load(ARTIFACTS["candidate"])
    discriminator = candidate["discriminator"]
    assert discriminator["qoi"] == "EXACT_H15_INTERSECTION_P16_CLASSIFICATION"
    assert discriminator["predicted_result"] is None
    assert discriminator["allowed_result_branches"] == [
        "EXACT_OVERLAP_WITNESS",
        "SCOPED_OVERLAP_IMPOSSIBILITY",
        "BOUNDED_NO_MATCH_ONLY",
        "CANNOT_CHECK",
    ]
    assert discriminator["positive_witness"] == (
        "x=r||c has length 30 with |r|=|c|=15; x has an explicit canonical parse and a mathematical UNSAT proof; "
        "y has length 32 with an explicit canonical parse; prefix_16(y)=1||c bit-for-bit."
    )
    assert discriminator["negative_certificate"] == (
        "A symbolic proof exhausts every frozen length-30 parent branch and every frozen length-32 current branch and derives a contradiction to canonical parsing, exact equality, or parent UNSAT."
    )
    assert candidate["target_access"] == {
        "decoder_imported_or_executed": False,
        "evaluator_imported_or_executed": False,
        "overlap_bits_compared": False,
        "target_result_accessed": False,
        "target_result_determined": False,
    }


def test_difference_witness_blocks_k12_fixed_bit_transport() -> None:
    candidate = _load(ARTIFACTS["candidate"])
    witness = candidate["difference_witness_vs_k12"]
    assert witness["changed_structural_coordinate"] == (
        "The parent half-length changes from 12 to 15: the v=1,m=3 length-30 split occurs three payload bits after the 12-bit header, rather than at the k=12 payload boundary."
    )
    assert witness["failed_assumption_not_transported"] == (
        "The k=12 proof's complete-payload suffix pattern and its single forced shared-bit mismatch are not assumed at k=15."
    )
    assert witness["new_current_branch_structure"] == (
        "Length 32 has both unpadded v in {2,3},m=2 branches and padded v in {8,...,15},m=1 branches; every branch must be checked."
    )
    assert witness["cheapest_repeat_failure_test"].startswith("After a separate public authorization")


def test_inert_evaluator_and_firewall_cannot_access_or_classify_target() -> None:
    manifest = _load(ARTIFACTS["manifest"])
    authorization = _load(ARTIFACTS["authorization"])
    assert manifest["status"] == "FROZEN_INERT_CONTRACT_NOT_IMPORTED_NOT_EXECUTED"
    assert manifest["evaluator"]["raw_sha256"] == hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    assert manifest["target_result_capability"] is False
    assert authorization["current_task_evaluator_execution_authorized"] is False
    assert authorization["decoder_access_authorized"] is False
    assert authorization["target_bit_comparison_authorized"] is False
    assert authorization["target_result_state"] == "H15_INTERSECTION_P16_UNACCESSED_UNDETERMINED"
    source = EVALUATOR.read_text(encoding="utf-8")
    for forbidden in (
        "C041_fx_sat_one_sided",
        "decode_formula",
        "is_satisfiable",
        "materialize_complement",
        "subprocess",
        "prefix_16",
        "H15",
        "P16",
    ):
        assert forbidden not in source
    evaluator = _module("pnp_c050_k15_inert", EVALUATOR)
    try:
        evaluator.evaluate_target()
    except evaluator.TargetEvaluationNotAuthorized as exc:
        assert str(exc) == "target evaluation is not authorized by this inert freeze contract"
    else:
        raise AssertionError("inert evaluator unexpectedly returned")


def test_latest_framework_subject_is_rebound_and_current() -> None:
    binding = _load(ARTIFACTS["framework_binding"])
    observation = _load(ARTIFACTS["framework_observation"])
    assert binding["authoritative_framework_sha"] == "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
    assert binding["pre_candidate_packet_hash"] == "b50f857493e88680bd74943321316451b379c664e0e39d7d2d709f01d5be2a56"
    assert observation["observed_current_main_sha"] == binding["authoritative_framework_sha"]
    assert observation["intervening_diff"] == []
    assert observation["verdict"] == "CURRENT_UNCHANGED"
    assert observation["licenses_candidate_materialization"] is True
    assert observation["grants_scientific_authority"] is False


def test_trace_stops_at_candidate_and_no_math_ledger_credit_is_created() -> None:
    trace = _load(ARTIFACTS["trace"])
    receipt = _load(ARTIFACTS["receipt"])
    assert trace["entries"][-1]["event_type"] == "CANDIDATE_PROPOSED"
    serialized = json.dumps(trace)
    assert "FALSIFIER_RUN" not in serialized
    assert "RESULT_RECORDED" not in serialized
    assert receipt["authority"] == {
        "candidate_is_mathematical_proposal": True,
        "selector_same_context_derivation_frozen": True,
        "target_theorem_truth": False,
        "independent_review": False,
        "mathematical_result_credit": False,
        "mathematical_saturation_credit": False,
        "p_vs_np_authority": False,
        "root_status": "OPEN",
    }
    assert not any("LEDGER" in path.name for path in ARTIFACTS.values())


def test_capability_free_verifier_detects_candidate_mutation(tmp_path: Path) -> None:
    verifier = _module("pnp_c050_k15_verify", VERIFIER)
    assert verifier.audit_packet(ROOT) == ()
    for path in ARTIFACTS.values():
        target = tmp_path / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())
    target_evaluator = tmp_path / EVALUATOR.relative_to(ROOT)
    target_evaluator.parent.mkdir(parents=True, exist_ok=True)
    target_evaluator.write_bytes(EVALUATOR.read_bytes())
    candidate_path = tmp_path / ARTIFACTS["candidate"].relative_to(ROOT)
    candidate = _load(candidate_path)
    candidate["selector"]["selected_k"] = 16
    candidate_path.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert any("candidate: full-document digest mismatch" in error for error in verifier.audit_packet(tmp_path))
