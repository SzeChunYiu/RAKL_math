from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003_abel001_candidate_freeze_fixture.py"
INERT = RH / "05_oracles/rh_ana003_abel001_inert_evaluator.py"


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


def test_candidate_documents_match_deterministic_fixture() -> None:
    module = _module("rh_abel001_candidate", FIXTURE)
    expected = module.build_documents()
    assert set(expected) == set(module.PATHS)
    for name, relative in module.PATHS.items():
        assert _load(ROOT / relative) == expected[name]


def test_exact_fixed_n_statement_and_scope_are_frozen() -> None:
    module = _module("rh_abel001_candidate_scope", FIXTURE)
    candidate = module.build_documents()["candidate"]
    assert candidate["quantifier_order"] == "FOR_EACH_FIXED_INTEGER_N_GE_1__THEN_TAKE_Y_TO_INFINITY"
    assert candidate["definitions"]["cumulative_source"] == "A(x)=sum_{m<=x}a_m=floor(x)-psi(x)"
    assert "A(Y)b_n(Y)-A(X)b_n(X)" in candidate["candidate_statement"]["finite_endpoint_identity"]
    assert "m=6k" in next(row["obligation"] for row in candidate["proof_obligations"] if row["id"] == "O7-NONABSOLUTE-WITNESS")
    assert candidate["explicit_exclusions"] == [
        "NO_N_UNIFORMITY",
        "NO_SERIES_REORDERING_OR_REGROUPING",
        "NO_PR316_RATE_OR_CUTOFF_CLAIM",
        "NO_LI_COEFFICIENT_SIGN_CLAIM",
        "NO_RIEMANN_HYPOTHESIS_CLAIM",
        "NO_NOVELTY_CLAIM",
        "NO_INDEPENDENT_REVIEW_CLAIM",
    ]
    assert candidate["seven_field_mathematical_rubric"]["exact_result_or_failure"] == "UNEVALUATED_CANDIDATE_FREEZE_ONLY"
    assert {row["status"] for row in candidate["proof_obligations"]} == {"FROZEN_UNEVALUATED"}


def test_result_branches_and_falsifiers_fail_closed() -> None:
    module = _module("rh_abel001_candidate_branches", FIXTURE)
    docs = module.build_documents()
    candidate = docs["candidate"]
    authorization = docs["authorization"]
    receipt = docs["receipt"]
    assert candidate["allowed_result_branches"] == [
        "PROVED_FIXED_N_NATURAL_ORDER_IDENTITY",
        "FINITE_ENDPOINT_IDENTITY_FALSE",
        "BELLOTTI_BOUNDARY_OR_INTEGRAL_INSUFFICIENT",
        "ABSOLUTE_DIVERGENCE_WITNESS_FALSE",
        "CANNOT_CHECK",
    ]
    assert authorization["current_round_evaluator_execution_authorized"] is False
    assert authorization["proof_derivation_authorized"] is False
    assert authorization["result_classification_authorized"] is False
    assert receipt["authority"]["target_theorem_truth"] is False
    assert receipt["authority"]["mathematical_result_credit"] is False
    assert receipt["authority"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_evaluator_is_actually_inert() -> None:
    module = _module("rh_abel001_inert", INERT)
    with pytest.raises(module.TargetEvaluationNotAuthorized):
        module.evaluate()
    source = INERT.read_text(encoding="utf-8")
    for forbidden in ("sympy", "mpmath", "subprocess", "scipy", "requests"):
        assert forbidden not in source
