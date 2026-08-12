from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/rh_ana003j_d001_jy_c001_evaluator_freeze_fixture.py"


def fixture():
    spec = importlib.util.spec_from_file_location("jy_eval_freeze", FIXTURE)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def test_manifest_is_deterministic_and_exactly_binds_evaluator() -> None:
    module = fixture()
    actual = json.loads((ROOT / module.PATH).read_text())
    assert actual == module.build()
    assert actual["artifact_hash"] == module.canonical_hash(actual)
    evaluator = ROOT / actual["evaluator_identity"]["path"]
    assert hashlib.sha256(evaluator.read_bytes()).hexdigest() == (
        "55c73c2975924683ed537d394af75475022a6703a7a63c9d3a7c46bfeac31267"
    )


def test_evaluator_source_is_syntax_valid_but_never_imported() -> None:
    module = fixture()
    manifest = module.build()
    source = (ROOT / manifest["evaluator_identity"]["path"]).read_text()
    ast.parse(source)
    assert manifest["status"] == "FROZEN_NOT_IMPORTED_NOT_EXECUTED"
    assert manifest["current_round_firewall"] == {
        "execution_authorized": False,
        "evaluator_imported": False,
        "evaluator_executed": False,
        "result_classified": False,
        "receipt_created": False,
    }


def test_precision_and_output_scope_are_frozen() -> None:
    manifest = fixture().build()
    assert manifest["precision_contract"]["decimal_digits"] == 100
    assert manifest["precision_contract"]["relative_tolerance"] == "1e-70"
    assert manifest["precision_contract"]["authority"] == (
        "NUMERICAL_CORROBORATION_ONLY_NOT_PROOF"
    )
    behavior = " ".join(manifest["frozen_behavior"])
    for forbidden_output in (
        "B_JY",
        "m_JY",
        "M_JY",
        "natural-order remainder",
        "epsilon_n",
        "diagonal cutoff",
    ):
        assert forbidden_output in behavior


def test_prior_authorization_is_explicitly_insufficient_for_execution() -> None:
    manifest = fixture().build()
    note = manifest["bound_authorization"]["note"]
    assert "did not bind these bytes" in note
    assert "later authorization must bind this exact evaluator raw SHA-256" in note
    assert manifest["chronology"]["next_step"] == (
        "MERGE_IDENTITY_FREEZE_THEN_FREEZE_UPDATED_EXECUTION_AUTHORIZATION"
    )
    authority = manifest["authority"]
    assert authority["evaluator_identity_only"] is True
    assert authority["mathematical_result"] is False
    assert authority["proof"] is False
    assert authority["software_or_governance_credit_units"] == 0
