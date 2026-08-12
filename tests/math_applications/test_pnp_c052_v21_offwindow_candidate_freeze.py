from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = BASE / "09_trace/c052_v21_offwindow_candidate_freeze_fixture.py"
CANDIDATE = BASE / "04_candidates/O9d12a2a1b_C052_V21_OFFWINDOW_UNSAT_ANCHOR_LEMMA_FREEZE_20260812.json"
FALSIFIER = BASE / "05_falsification/O9d12a2a1b_C052_V21_OFFWINDOW_LEMMA_FALSIFIER_MANIFEST_20260812.json"
RECEIPT = BASE / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_CANDIDATE_FREEZE_RECEIPT_20260812.json"
PRE_TRACE = BASE / "09_trace/O9d12a2a1b_C052_V21_SUPERSEDING_PRE_CANDIDATE_TRACE_20260812.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def module():
    spec = importlib.util.spec_from_file_location("c052_v21_offwindow_freeze", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def test_freeze_artifacts_match_the_inert_serializer() -> None:
    assert list(module().build()) == [load(CANDIDATE), load(FALSIFIER), load(RECEIPT)]


def test_candidate_freezes_the_exact_marginal_quantifiers_and_boundary() -> None:
    candidate = load(CANDIDATE)
    claim = candidate["exact_quantified_candidate"]
    assert candidate["status"] == "FROZEN_NOT_PROVED_NOT_EXECUTED"
    assert "a>=2, m>=4" in claim["cell_quantifiers"]
    assert claim["window_premise"] == (
        "H<=k and k+6<R, equivalently x[k..k+6] lies wholly in the unpadded literal payload"
    )
    assert claim["full_a_cell_quantifier"] == "for every v with 2^(a-1)<=v<=2^a-1"
    assert claim["marginal_quantifiers"] == "for every j in {1,...,7} and every epsilon in {0,1}"
    caveat = candidate["marginal_not_independent_caveat"]
    assert caveat["asserted_meaning"].startswith("For each fixed (v,j,epsilon)")
    assert "two witnesses can be chosen to differ only at coordinate j" in caveat["not_asserted"]
    assert "all 2^7 window patterns occur" in caveat["not_asserted"]


def test_k31_is_only_an_unevaluated_planned_public_regression() -> None:
    candidate = load(CANDIDATE)
    regression = candidate["smallest_planned_public_regression"]
    assert regression["status"] == "UNEVALUATED_PLANNED_REGRESSION_IDENTITY_ONLY"
    assert regression["expected_parent_cell_for_future_proof"] == {
        "k": 31,
        "a": 2,
        "b": 3,
        "m": 5,
        "v_range": [2, 3],
        "H": 16,
        "w": 3,
        "R": 61,
        "p": 1,
        "E": 62,
        "window_parent_indices": [31, 37],
        "window_payload_offsets": [15, 21],
        "expected_touched_clause_indices_one_based": [2, 3],
    }
    assert regression["required_current_encoded_length"] == 64
    assert len(regression["expected_exhaustive_current_cells_for_future_proof"]) == 3
    assert regression["witness_formulas_or_labels_included"] is False
    assert regression["arithmetic_or_semantic_evaluation_executed_in_this_round"] is False


def test_proof_obligations_and_falsifier_fail_closed_without_execution() -> None:
    candidate = load(CANDIDATE)
    obligations = candidate["proof_obligations_for_future_authorized_check"]
    assert len(obligations) == 13
    assert "O7_EVERY_VARIABLE_INDEX_BIT_HAS_BOTH_LEGAL_MARGINAL_VALUES_FOR_EVERY_FIXED_V_IN_THE_FULL_A_CELL" in obligations
    assert "O12_NO_SMALLER_ADJACENT_SUPPORTED_PREMISE_CELL" in obligations
    assert "O13_MARGINAL_QUANTIFIER_IS_NOT_STRENGTHENED_TO_SINGLE_BIT_FLIP_OR_JOINT_PATTERN_COVERAGE" in obligations
    falsifier = load(FALSIFIER)
    assert falsifier["status"] == "FROZEN_NOT_IMPLEMENTED_NOT_EXECUTED"
    assert falsifier["execution_surface"] == {
        "implementation_path": None,
        "entrypoint": None,
        "executed": False,
    }
    assert falsifier["allowed_future_outcomes"] == [
        "CANDIDATE_SURVIVES_EXACT_SCOPE",
        "CANDIDATE_REFUTED",
        "CANNOT_CHECK",
    ]
    assert falsifier["hidden_world_policy"]["hidden_labels_included"] is False


def test_receipt_preserves_v21_lineage_trace_delta_and_zero_credit() -> None:
    candidate = load(CANDIDATE)
    falsifier = load(FALSIFIER)
    receipt = load(RECEIPT)
    prior = load(PRE_TRACE)
    assert receipt["application_base_sha"] == "ce7e3491c67ae62b387ce77e71cb1bf37acace48"
    assert receipt["framework_pin"] == "d21592b0ff8da988deabb923fd549891ff8ad9f0"
    assert receipt["source_identities"]["candidate_artifact_hash"] == candidate["artifact_hash"]
    assert receipt["source_identities"]["falsifier_artifact_hash"] == falsifier["artifact_hash"]
    delta = receipt["public_trace_delta"]
    assert delta["event_type"] == "CANDIDATE_PROPOSED"
    assert delta["chronology_order_index"] == 33
    assert delta["previous_event_hash"] == prior["entries"][-1]["artifact_hash"]
    assert "FALSIFIER_RUN" not in json.dumps(receipt)
    assert "RESULT_RECORDED" not in json.dumps(receipt)
    assert receipt["authority"] == {
        "candidate_is_proposal_only": True,
        "mathematical_result_credit": 0,
        "mathematical_saturation_credit": 0,
        "independent_review": False,
        "p_vs_np_authority": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    }


def test_fixture_has_no_decoder_witness_or_evaluation_implementation_surface() -> None:
    source = FIXTURE.read_text(encoding="utf-8")
    forbidden = [
        "C041_fx_sat_one_sided import",
        "decode_formula",
        "is_satisfiable",
        "def classify(",
        "def evaluate(",
        "def materialize(",
    ]
    assert not any(token in source for token in forbidden)
    candidate = load(CANDIDATE)
    assert all(value is False for value in candidate["future_result_firewall"].values())
    assert candidate["credit"]["mathematical_result"] == 0
    assert candidate["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
