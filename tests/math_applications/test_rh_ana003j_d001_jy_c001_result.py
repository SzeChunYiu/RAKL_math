from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/rh_ana003j_d001_jy_c001_result_fixture.py"


def fixture():
    spec = importlib.util.spec_from_file_location("jy_c001_result", FIXTURE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_result_documents_reproduce_and_are_hash_bound() -> None:
    module = fixture()
    docs = module.build_all()
    assert set(docs) == set(module.PATHS.values())
    for path, expected in docs.items():
        actual = json.loads((ROOT / path).read_text())
        assert actual == expected
        assert actual["artifact_hash"] == module.canonical_hash(actual)


def test_authorized_machine_receipt_passes_fixed_inputs_and_worlds() -> None:
    module = fixture()
    result = module.build_all()[module.PATHS["result"]]
    receipt = result["machine_validation_receipt"]
    assert receipt["overall_classification"] == "PASS"
    assert receipt["symbolic_derivation"]["pass"] is True
    assert receipt["public_validation"]["pass"] is True
    assert len(receipt["public_validation"]["rows"]) == 12
    assert receipt["planted_world_validation"]["pass"] is True
    assert len(receipt["planted_world_validation"]["rows"]) == 15
    assert receipt["public_validation"]["precision_dps"] == 100
    assert receipt["public_validation"]["corroboration_only_not_proof"] is True


def test_exact_proof_and_repaired_computable_modulus_are_materialized() -> None:
    module = fixture()
    result = module.build_all()[module.PATHS["result"]]
    proved = result["proved_fixed_n_result"]
    assert "ds=2r c^(-2)dr" in " ".join(proved["change_of_variables_proof"])
    assert "2j+5.03" in " ".join(proved["change_of_variables_proof"])
    assert "+1.515" in proved["monotonicity_domain"]
    assert "B_JY(n,log Y*)<=B_JY(n,log Y)" in proved["integer_endpoint_extension"]
    least = proved["frozen_least_modulus"]
    assert least["existence"].startswith("PROVED")
    assert least["least_index_computability"] == "CANNOT_CHECK"
    assert "equality" in least["blocker"]
    algorithm = " ".join(proved["computable_sufficient_tilde_modulus_algorithm"])
    assert "dovetail stage" in algorithm
    assert "certified enclosures" in algorithm
    assert "strictly below epsilon/2" in algorithm
    assert "tilde_M_JY(n,epsilon)=exp" in algorithm
    assert "ceil(exp" in algorithm
    assert "not claimed to equal the frozen least-index" in algorithm
    assert "<epsilon/2<epsilon" in proved["strict_epsilon_and_all_real_Y"]
    assert proved["numerical_M_values_materialized"] is False


def test_forbidden_numerical_outputs_and_diagonal_are_absent() -> None:
    module = fixture()
    result = module.build_all()[module.PATHS["result"]]
    forbidden = result["machine_validation_receipt"]["forbidden_outputs"]
    assert forbidden["B_JY_values"] == []
    assert forbidden["m_JY_values"] == []
    assert forbidden["M_JY_values"] == []
    assert forbidden["natural_order_remainder_values"] == []
    assert forbidden["epsilon_sequence_identity"] is None
    assert forbidden["diagonal_cutoff_constant_identity"] is None
    authority = result["authority"]
    assert authority["fixed_n_direct_envelope"] is True
    assert authority["frozen_least_M_exists"] is True
    assert authority["frozen_least_M_computability"] == "CANNOT_CHECK"
    assert authority["computable_sufficient_tilde_M_algorithm"] is True
    assert authority["numerical_M_value"] is False
    assert authority["epsilon_n_or_diagonal"] is False
    assert authority["riemann_hypothesis"] is False


def test_seven_field_lesson_is_mathematical_and_governance_is_zero_credit() -> None:
    module = fixture()
    lesson = module.build_all()[module.PATHS["lesson"]]
    required = {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "mathematical_falsifier",
        "mathematical_repair",
        "proof_source_evidence",
    }
    assert required <= set(lesson)
    assert len(lesson["mathematical_research_lessons"]) == 7
    math_text = " ".join(lesson["mathematical_research_lessons"])
    for phrase in ("source substitution", "floor", "Jacobian", "+1.515", "endpoint", "non-strict", "corroboration"):
        assert phrase in math_text
    assert "zero mathematical-lesson" in lesson["nonmathematical_governance_note"]
    assert lesson["framework_delta"] == "NONE; no reusable framework change is proposed or promoted."


def test_same_context_review_is_scoped_and_not_independent() -> None:
    module = fixture()
    review = module.build_all()[module.PATHS["review"]]
    assert review["review_authority"] == "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT_REVIEW"
    assert review["verdict"] == "PASS_SCOPED_FIXED_N_RESULT_ONLY"
    assert len(review["lenses"]) == 5
    assert "moving diagonal" in review["strongest_objection"]
    assert "RH" in review["nonclaims"]
