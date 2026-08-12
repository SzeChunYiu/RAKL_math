from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c050_k15_proof_input_fixture.py"
EVALUATOR = PNP / "05_falsification/c050_k15_alignment_proof_checker.py"
ARTIFACTS = {
    "certificate": PNP / "04_candidates/O9d12a2a1b_C050_K15_PROOF_CERTIFICATE_FREEZE_20260812.json",
    "authorization": PNP / "09_trace/O9d12a2a1b_C050_K15_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json",
    "chronology": PNP / "09_trace/O9d12a2a1b_C050_K15_PROOF_INPUT_CHRONOLOGY_20260812.json",
}


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_proof_input_documents_match_fixture() -> None:
    fixture = _module("pnp_c050_k15_proof_input", FIXTURE)
    assert {name: _load(path) for name, path in ARTIFACTS.items()} == fixture.build_documents()


def test_public_candidate_identity_and_merge_are_exact() -> None:
    certificate = _load(ARTIFACTS["certificate"])
    chronology = _load(ARTIFACTS["chronology"])
    assert certificate["candidate_id"] == "C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1"
    assert certificate["candidate_core_sha256"] == "sha256:c869e4726c36551b69f10407dd482f30d83f2b2a8129c5364ac2c08eda4c1d43"
    assert certificate["candidate_artifact_hash"] == "sha256:47bf8d99a7c5620b8ab8f2e3fadfb762125df921bed4b65fe2ddb56f4733c5e1"
    assert chronology["candidate_public_freeze"] == {
        "merge_commit": "0b0f1840f99043a57050d625683ba8311fef3f24",
        "candidate_blob": "cd20d173cebad0357593041d8591766313143269",
        "merge_is_ancestor_of_result_base": True,
        "result_base_commit": "02c5fb7764116cf075d8dd5efd7b6fe835275ab9",
    }
    assert chronology["target_result_access_before_this_freeze"] is False


def test_hand_certificate_exhausts_parent_and_every_current_branch() -> None:
    certificate = _load(ARTIFACTS["certificate"])
    obligations = {row["obligation_id"]: row for row in certificate["obligations"]}
    assert set(obligations) == {
        "PARENT_LENGTH_30_PARAMETER_EXHAUSTION",
        "CURRENT_LENGTH_32_PARAMETER_BRANCH_EXHAUSTION",
        "EXACT_CANONICAL_PARENT_PARSE",
        "EXACT_CANONICAL_CURRENT_PARSE",
        "EXACT_1C_EQUALS_PREFIX16_BITWISE",
        "PARENT_UNSAT_PROOF_INDEPENDENT_OF_SYNTAX",
        "SWAPPED_REDUCTION_PRESERVED",
        "BOUNDED_SCOPE_ONLY",
    }
    assert all(row["status"] == "PROVED" for row in obligations.values())
    branches = obligations["CURRENT_LENGTH_32_PARAMETER_BRANCH_EXHAUSTION"]["branches"]
    assert branches == [
        {"v_values": [2, 3], "m": 2, "raw_length": 32, "padding": False},
        {"v_values": list(range(8, 16)), "m": 1, "raw_length": 31, "encoded_length": 32, "padding": True},
    ]
    assert obligations["EXACT_1C_EQUALS_PREFIX16_BITWISE"]["proof"] == (
        "For every h=1||c in H_15, h[3]=x[17]=1. For every p in P_16, p begins MAGIC=11100101, so p[3]=MAGIC[3]=0. Hence exact equality h=p is impossible."
    )


def test_parent_parse_and_unsat_proof_are_exact() -> None:
    certificate = _load(ARTIFACTS["certificate"])
    witness = certificate["source_side_nonvacuity_witness"]
    assert witness == {
        "formula": "(z OR z OR z) AND (not-z OR not-z OR not-z) AND (z OR z OR z)",
        "header": "111001011011",
        "payload": "010101111111010101",
        "word_x": "111001011011010101111111010101",
        "r": "111001011011010",
        "c": "101111111010101",
        "h_1c": "1101111111010101",
        "unsat_proof": "The first clause requires z=true and the second clause requires z=false; therefore no assignment satisfies their conjunction, regardless of the redundant third clause.",
    }
    assert len(witness["word_x"]) == 30
    assert witness["word_x"] == witness["r"] + witness["c"]
    assert witness["h_1c"] == "1" + witness["c"]
    assert witness["h_1c"][3] == "1"


def test_authorized_checker_is_bound_to_frozen_contract_but_has_no_decoder() -> None:
    authorization = _load(ARTIFACTS["authorization"])
    assert authorization["proof_check_authorized"] is True
    assert authorization["authorized_operation"] == "evaluate_certificate(exact_certificate, exact_authorization)"
    assert authorization["target_decoder_access_authorized"] is False
    assert authorization["formula_enumeration_authorized"] is False
    assert authorization["evaluator_raw_sha256"] == hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    source = EVALUATOR.read_text(encoding="utf-8")
    for forbidden in (
        "C041_fx_sat_one_sided",
        "decode_formula",
        "is_satisfiable",
        "materialize_complement",
        "subprocess",
    ):
        assert forbidden not in source


def test_checker_accepts_exact_certificate_and_rejects_planted_branch_loss() -> None:
    checker = _module("pnp_c050_k15_checker", EVALUATOR)
    certificate = _load(ARTIFACTS["certificate"])
    authorization = _load(ARTIFACTS["authorization"])
    report = checker.evaluate_certificate(certificate, authorization)
    assert report == {
        "candidate_id": "C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1",
        "checked_current_parameter_pairs": [[2, 2], [3, 2]] + [[v, 1] for v in range(8, 16)],
        "common_separating_coordinate": 3,
        "h15_fixed_bit": 1,
        "p16_fixed_bit": 0,
        "obligations_checked": 8,
        "status": "PASS",
        "verdict": "SCOPED_OVERLAP_IMPOSSIBILITY",
    }
    mutated = json.loads(json.dumps(certificate))
    branch_row = next(
        row
        for row in mutated["obligations"]
        if row["obligation_id"] == "CURRENT_LENGTH_32_PARAMETER_BRANCH_EXHAUSTION"
    )
    branch_row["branches"][1]["v_values"].remove(15)
    try:
        checker.evaluate_certificate(mutated, authorization)
    except checker.CertificateCheckError as exc:
        assert "length-32 branches are not exhaustive" in str(exc)
    else:
        raise AssertionError("checker accepted an omitted frozen branch")
