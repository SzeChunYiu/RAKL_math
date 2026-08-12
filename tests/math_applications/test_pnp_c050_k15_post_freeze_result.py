from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c050_k15_result_fixture.py"
ARTIFACTS = {
    "result": PNP / "05_falsification/O9d12a2a1b_C050_K15_PROOF_CHECK_RESULT_20260812.json",
    "failure": PNP / "07_memory/O9d12a2a1b_C050_K15_FAILURE_EXPERIENCE_20260812.json",
    "lesson": PNP / "07_memory/O9d12a2a1b_C050_K15_MATHEMATICAL_LESSON_20260812.json",
    "review": PNP / "08_reviews/O9d12a2a1b_C050_K15_RESULT_REVIEW_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C050_K15_POST_FREEZE_RESULT_TRACE_20260812.json",
}


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _module():
    spec = importlib.util.spec_from_file_location("pnp_c050_k15_result", FIXTURE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_result_documents_match_executed_fixture() -> None:
    assert {name: _load(path) for name, path in ARTIFACTS.items()} == _module().build_documents()


def test_exact_result_is_scoped_k15_impossibility_with_all_branches() -> None:
    result = _load(ARTIFACTS["result"])
    assert result["status"] == "PASS_SAME_CONTEXT_HAND_PROOF_RECORD_CHECK"
    assert result["evaluator_output"] == {
        "candidate_id": "C050-K15-TARGET-BLIND-SELECTOR-DISCRIMINATOR-v1",
        "checked_current_parameter_pairs": [[2, 2], [3, 2]] + [[v, 1] for v in range(8, 16)],
        "common_separating_coordinate": 3,
        "h15_fixed_bit": 1,
        "p16_fixed_bit": 0,
        "obligations_checked": 8,
        "status": "PASS",
        "verdict": "SCOPED_OVERLAP_IMPOSSIBILITY",
    }
    math = result["exact_mathematical_result"]
    assert math["lemma"] == "H_15 intersection P_16 is empty."
    assert math["separation"] == "Every h in H_15 has h[3]=1, while every p in P_16 has p[3]=MAGIC[3]=0."
    assert math["current_branch_exhaustion"] == (
        "P_16 has exactly the unpadded (v,m)=(2,2),(3,2) regimes and the padded (v,m)=(8,1),...,(15,1) regimes at encoded length 32; all begin canonical MAGIC."
    )
    assert math["scope_consequence"] == "The result is k=15 only; no conclusion is drawn for any other k or for cover growth."


def test_chronology_binds_public_candidate_and_local_proof_input_commit() -> None:
    result = _load(ARTIFACTS["result"])
    chronology = result["chronology"]
    assert chronology["candidate_public_merge"] == "0b0f1840f99043a57050d625683ba8311fef3f24"
    assert chronology["candidate_merge_precedes_result_access"] is True
    assert chronology["proof_input_commit"] == "db520bae16f64419778e9f73240db8af42227d85"
    assert chronology["proof_inputs_frozen_before_execution"] is True
    assert chronology["evaluation_base_commit"] == "db520bae16f64419778e9f73240db8af42227d85"
    assert chronology["result_accessed_at"] == "2026-08-12T07:05:11Z"


def test_seven_field_mathematical_lesson_is_complete_and_deduplicated() -> None:
    lesson = _load(ARTIFACTS["lesson"])
    seven = lesson["seven_field_math_lesson"]
    assert set(seven) == {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "falsifier",
        "mathematical_repair",
        "proof_and_source_evidence",
    }
    assert lesson["credit_type"] == "SCOPED_EXACT_SYMBOLIC_IMPOSSIBILITY_PROOF"
    assert lesson["deduplication"] == {
        "new_global_cause_claimed": False,
        "relation_to_c049": "SPECIALIZATION_AND_REPETITION_OF_FIXED_VARIABLE_CODE_VERSUS_MAGIC_MISMATCH",
        "new_scoped_mathematical_unit_count": 1,
        "global_ledger_updated": False,
        "literature_novelty_claim": False,
        "independent_review_credit": 0,
        "assurance_metadata_mathematical_credit": 0,
    }
    assert "all-zero" in seven["scope"]
    assert "every frozen length-32 branch" in seven["proof_and_source_evidence"]


def test_failure_experience_and_residual_do_not_generalize() -> None:
    failure = _load(ARTIFACTS["failure"])
    assert failure["diagnosis"]["status"] == "SUPPORTED_BOUNDED"
    assert failure["diagnosis"]["unique_global_cause_claimed"] is False
    assert failure["typed_relations"] == [
        {
            "relation": "INSTANCE_OF",
            "target_failure_id": "F-PNP-C049-K12-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
            "witness": "At k=12 the forced H bit was coordinate 4; at k=15 the changed split moves a forced v=1 variable-code bit to H coordinate 3, which again meets a zero in MAGIC. The coordinate differs, so the k=15 derivation is new scoped evidence but not a new global mechanism.",
        }
    ]
    assert failure["residual"] == (
        "Whether H_k intersects P_(k+1) for any untouched k>15 remains open and requires a fresh context, target-blind selector, field derivation, and frozen discriminator."
    )
    assert failure["scope"][-1] == "no finite-to-general extrapolation"


def test_result_review_is_same_context_and_non_independent() -> None:
    review = _load(ARTIFACTS["review"])
    assert review["review_authority"] == "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW"
    assert review["verdict"] == "ACCEPT_SCOPED_K15_EMPTY_INTERSECTION_HAND_PROOF"
    assert review["independent_review"] is False
    assert {row["role"] for row in review["role_reviews"]} == {
        "domain_theory_lead",
        "adversarial_falsification_lead",
        "formal_methods_lead",
        "novelty_research_value_lead",
    }
    assert "not a new global cause" in review["deduplication_note"]


def test_trace_records_result_review_and_open_residual_only() -> None:
    trace = _load(ARTIFACTS["trace"])
    assert [entry["event_type"] for entry in trace["entries"][-4:]] == [
        "FALSIFIER_RUN",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
        "REVIEWED",
    ]
    assert trace["entries"][-3]["outputs"] == [
        "H15_INTERSECTION_P16_EMPTY",
        "K15_ONLY",
        "ROOT_OPEN",
    ]
    assert trace["entries"][-2]["outputs"] == [
        "K_GT_15_REMAINS_OPEN",
        "NO_FINITE_TO_GENERAL_EXTRAPOLATION",
    ]
    assert "PROMOTED" not in json.dumps(trace)


def test_no_global_ledger_or_software_math_credit() -> None:
    result = _load(ARTIFACTS["result"])
    lesson = _load(ARTIFACTS["lesson"])
    assert result["credit"]["software_process"] == 0
    assert result["credit"]["ci_schema_hash_runtime"] == 0
    assert lesson["deduplication"]["global_ledger_updated"] is False
    assert not any("LEDGER" in path.name for path in ARTIFACTS.values())
