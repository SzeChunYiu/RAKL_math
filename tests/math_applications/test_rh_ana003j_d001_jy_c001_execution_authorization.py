from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/rh_ana003j_d001_jy_c001_execution_authorization_fixture.py"


def fixture():
    spec = importlib.util.spec_from_file_location("jy_exec_auth", FIXTURE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_authorization_is_deterministic_and_exactly_bound() -> None:
    module = fixture()
    actual = json.loads((ROOT / module.PATH).read_text())
    assert actual == module.build()
    assert actual["artifact_hash"] == module.canonical_hash(actual)
    for binding in actual["exact_bindings"].values():
        assert hashlib.sha256((ROOT / binding["path"]).read_bytes()).hexdigest() == binding["raw_sha256"]
    assert actual["post_merge_authorization"]["allowed_evaluator_raw_sha256"] == (
        "55c73c2975924683ed537d394af75475022a6703a7a63c9d3a7c46bfeac31267"
    )


def test_current_round_is_inert_and_result_scope_is_exact() -> None:
    authorization = fixture().build()
    assert authorization["chronology"]["base_sha"] == "6425952ad6e7a079adad0a68e93b90fe8b8f9a47"
    assert authorization["chronology"]["evaluator_imported_or_executed"] is False
    assert authorization["chronology"]["result_accessed"] is False
    assert authorization["current_round"]["evaluator_import_or_execution_authorized"] is False
    future = authorization["post_merge_authorization"]
    assert future["fixed_public_validation_authorized"] is True
    assert future["materialize_exact_computable_symbolic_M_algorithm_authorized"] is True
    assert future["precision_dps"] == 100
    assert future["relative_tolerance"] == "1e-70"


def test_math_requirements_and_nonclaims_are_explicit() -> None:
    authorization = fixture().build()
    requirements = " ".join(authorization["result_requirements"])
    for phrase in ("substitution proof", "u>=U_JY(n)", "Y*=Y+1/2", "<epsilon", "least-integer-search", "seven-field mathematical lesson"):
        assert phrase in requirements
    forbidden = " ".join(authorization["forbidden"])
    for phrase in ("numerical B_JY", "epsilon_n", "diagonal cutoff C", "moving-diagonal", "Li-positivity", "RH"):
        assert phrase in forbidden
    authority = authorization["authority"]
    assert authority["operational_authorization_only"] is True
    assert authority["mathematical_result"] is False
    assert authority["mathematical_lesson"] is False
    assert authority["software_or_governance_credit_units"] == 0
