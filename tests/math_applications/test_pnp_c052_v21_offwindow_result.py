from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = BASE / "09_trace/c052_v21_offwindow_result_fixture.py"
CHECKER = BASE / "05_falsification/c052_v21_offwindow_independent_checker.py"
PROOF = BASE / "04_candidates/O9d12a2a1b_C052_V21_OFFWINDOW_SYMBOLIC_HAND_PROOF_20260812.json"
CHECK = BASE / "05_falsification/O9d12a2a1b_C052_V21_OFFWINDOW_INDEPENDENT_CHECK_RESULT_20260812.json"
RESULT = BASE / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_RESULT_RECEIPT_20260812.json"
REVIEW = BASE / "08_reviews/O9d12a2a1b_C052_V21_OFFWINDOW_SAME_CONTEXT_REVIEW_20260812.json"
LESSON = BASE / "07_memory/O9d12a2a1b_C052_V21_OFFWINDOW_MATHEMATICAL_EXPERIENCE_20260812.json"
FREEZE_RECEIPT = BASE / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_CANDIDATE_FREEZE_RECEIPT_20260812.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def test_result_artifacts_are_exact_fixture_outputs() -> None:
    built = module("c052_offwindow_result_fixture", FIXTURE).build()
    assert list(built) == [load(PROOF), load(CHECK), load(RESULT), load(REVIEW), load(LESSON)]


def test_all_exact_symbolic_obligations_are_proved_and_checked() -> None:
    proof = load(PROOF)
    result = load(RESULT)
    assert proof["all_obligations_proved"] is True
    assert [row["id"] for row in proof["obligations"]] == [f"O{i}" for i in range(1, 14)]
    assert all(row["status"] == "PROVED" for row in proof["obligations"])
    assert result["result_branch"] == "PROVED_EXACT_QUANTIFIED_SCOPE"
    assert all(row["symbolic_proof"] == "PROVED" and row["independent_check"] == "PASS" for row in result["obligation_status"])
    assert result["marginal_not_independent_caveat_preserved"] is True


def test_explicit_construction_is_semantic_and_pointwise_in_full_a_cell() -> None:
    proof = load(PROOF)
    algorithm = " ".join(proof["construction_algorithm"])
    assert "two untouched clauses" in algorithm
    assert "three positive copies of x1" in algorithm
    assert "2^(a-1-s)" in algorithm
    assert proof["marginal_not_independent_caveat"] == (
        "forall v forall j forall epsilon exists F(v,j,epsilon); no joint-pattern or single-bit-flip claim"
    )
    o7 = proof["obligations"][6]["proof"]
    assert "Fix v" in o7 and "choose q=2" in o7 and "v>=2" in o7


def test_public_k31_formula_bound_receipts_cover_every_marginal() -> None:
    check = load(CHECK)["checker_result"]
    witnesses = check["k31_witnesses"]
    assert check["k31_witness_count"] == 28
    assert {(row["v"], row["j"], row["epsilon"]) for row in witnesses} == {
        (v, j, epsilon) for v in (2, 3) for j in range(1, 8) for epsilon in (0, 1)
    }
    assert all(len(row["formula_bytes"]) == 62 for row in witnesses)
    assert all(len(row["h_label"]) == 32 for row in witnesses)
    assert all(row["canonical_parse_valid"] for row in witnesses)
    assert all(row["unsat_symbolic_anchor"] == "x1 AND not-x1" for row in witnesses)
    assert all(row["unsat_bruteforce_corroboration"] for row in witnesses)
    assert all(row["observed_h_j"] == row["epsilon"] for row in witnesses)
    assert all(row["touched_clause_indices_one_based"] == [2, 3] for row in witnesses)
    assert all(row["anchor_clause_indices_one_based"] == [1, 4] for row in witnesses)


def test_k31_minimality_and_length64_support_are_exactly_scoped() -> None:
    check = load(CHECK)["checker_result"]
    assert check["smaller_premise_cells"] == [{
        "a": 2, "b": 3, "m": 4, "H": 16, "w": 3, "R": 52, "p": 0, "E": 52,
        "k": 26, "adjacent_support": False,
    }]
    assert [(row["a"], row["m"], row["R"], row["p"], row["v_range"]) for row in check["length64_current_support_cells"]] == [
        (1, 8, 64, 0, [1, 1]),
        (4, 3, 63, 1, [8, 15]),
        (6, 2, 64, 0, [32, 63]),
    ]
    public = load(RESULT)["public_k31"]
    assert public == {"witness_count": 28, "current_support_cell_count": 3, "minimality": "PROVED", "status": "PUBLIC_REGRESSION_PASS"}


def test_checker_is_a_separate_reimplementation_and_computation_is_not_proof() -> None:
    source = CHECKER.read_text(encoding="utf-8")
    assert "C041_fx_sat_one_sided" not in source
    assert "c052_v21_offwindow_result_fixture" not in source
    assert "O9d12a2a1b_C052_V21_OFFWINDOW_UNSAT_ANCHOR_LEMMA_FREEZE" not in source
    receipt = load(CHECK)
    assert receipt["authority"] == "COMPUTATIONAL_CORROBORATION_ONLY_NOT_PROOF"
    assert receipt["checker_result"]["checker_independence"] == "REIMPLEMENTED_GRAMMAR_NO_CANDIDATE_OR_C041_EXECUTABLE_IMPORT"
    assert receipt["checker_result"]["all_obligations_pass"] is True
    assert receipt["forbidden_evaluations_executed"] == []


def test_review_and_seven_field_lesson_preserve_authority_boundary() -> None:
    review = load(REVIEW)
    lesson = load(LESSON)
    assert review["verdict"] == "SCOPED_RESULT_SURVIVES_SAME_CONTEXT_REVIEW"
    assert review["blocking_concerns"] == []
    assert review["review_boundary"] == "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW"
    fields = lesson["seven_field_mathematical_lesson"]
    assert set(fields) == {
        "attempted_implication", "exact_result_or_failure", "supported_and_competing_causes",
        "scope", "mathematical_falsifier", "repair_or_next_discriminator", "proof_and_source_evidence",
    }
    assert "local obstruction escape is not overlap" in fields["repair_or_next_discriminator"]
    assert lesson["promotion_status"] == "SCOPED_MATHEMATICAL_EXPERIENCE_NOT_UNIVERSAL_RESEARCH_TOOL"


def test_public_result_trace_is_hash_chained_after_candidate_without_authority_escalation() -> None:
    result = load(RESULT)
    prior = load(FREEZE_RECEIPT)["public_trace_delta"]
    first, second = result["public_trace_deltas"]
    assert [first["event_type"], second["event_type"]] == ["FALSIFIER_RUN", "RESULT_RECORDED"]
    assert first["previous_event_hash"] == prior["artifact_hash"]
    assert second["previous_event_hash"] == first["artifact_hash"]
    assert second["outputs"] == ["PROVED_EXACT_QUANTIFIED_SCOPE", "OPEN_NO_SOLUTION_CERTIFICATE"]


def test_no_overlap_native_hidden_or_root_authority_is_claimed() -> None:
    result = load(RESULT)
    serialized = json.dumps([load(PROOF), load(CHECK), result, load(REVIEW), load(LESSON)])
    assert result["forbidden_evaluations_executed"] == []
    assert result["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert "no H_k intersection P_(k+1) result" in load(PROOF)["non_guarantees"]
    assert "INDEPENDENT_PEER_REVIEW" in serialized
    assert "P_vs_NP_SOLVED" not in serialized
