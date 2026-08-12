from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/rh_ana003j_d001_jy_c001_authorization_fixture.py"


def fixture():
    spec = importlib.util.spec_from_file_location("rh_jy_c001_authorization", FIXTURE)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def load(path: str) -> dict:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_fixture_reproduces_exact_authorization_and_hash() -> None:
    module = fixture()
    expected = module.build_all()
    assert set(expected) == set(module.PATHS.values())
    authorization = expected[module.PATHS["authorization"]]
    assert load(module.PATHS["authorization"]) == authorization
    assert authorization["artifact_hash"] == module.canonical_hash(authorization)


def test_candidate_falsifier_inputs_and_trace_are_exactly_bound() -> None:
    module = fixture()
    authorization = module.authorization_document()
    assert authorization["chronology"]["authorization_base_sha"] == (
        "e14c0708861fe04a0cfad4116e1e9b003e6702ff"
    )
    bindings = authorization["exact_identity_bindings"]
    assert bindings["candidate"]["candidate_core_sha256"] == (
        "sha256:082bc762b994bce8348da1ea99933fe14c965f9dff98296b6e9177cd94b974be"
    )
    for binding in bindings.values():
        assert hashlib.sha256((ROOT / binding["path"]).read_bytes()).hexdigest() == (
            binding["raw_sha256"]
        )
    assert bindings["falsifier"]["artifact_hash"] == (
        "sha256:dcc3611449e8f651fea29983504dcbdb04de72744c5b6192c675cdede853e9bd"
    )
    assert bindings["public_validation_inputs"]["artifact_hash"] == (
        "sha256:42b2450184a6e819a9373d61346be1cf33b7da5007d9d45b5c8f55ba971fbc01"
    )
    assert bindings["candidate_trace"]["last_event_hash"] == (
        "sha256:f60403d63d5282cc94aaff1ebed2a86acabb0a94825a5549b0688006eadbab56"
    )


def test_authorization_is_inert_until_its_own_merge() -> None:
    module = fixture()
    authorization = module.authorization_document()
    chronology = authorization["chronology"]
    assert chronology["authorization_commit_sha"] is None
    assert chronology["authorization_merge_sha"] is None
    assert chronology["authorization_present_on_active_main"] is False
    current = authorization["current_round"]
    assert current == {
        "allowed_action": "COMMIT_AND_MERGE_THIS_AUTHORIZATION_ONLY",
        "evaluator_implementation_authorized": False,
        "evaluator_import_or_execution_authorized": False,
        "validation_result_classification_authorized": False,
    }
    planned = ROOT / authorization["post_merge_successor_authorization"][
        "planned_evaluator_path"
    ]
    assert not planned.exists()


def test_post_merge_scope_is_fixed_public_validation_only() -> None:
    module = fixture()
    authorization = module.authorization_document()
    successor = authorization["post_merge_successor_authorization"]
    allowed = " ".join(successor["authorized_actions_after_activation"])
    assert "PASS, FAIL, and CANNOT_CHECK" in allowed
    assert "twelve public symbolic inputs" in allowed
    assert "n in {1,2,3,5}" in allowed
    assert "componentwise monotonicity" in allowed
    assert successor["scope_expansion_allowed"] is False
    assert successor["candidate_or_falsifier_mutation_allowed"] is False
    forbidden = " ".join(authorization["forbidden_even_after_activation"])
    for required in (
        "numerical B_JY",
        "m_JY or M_JY",
        "numerical incomplete-gamma",
        "natural-order remainder",
        "epsilon_n",
        "diagonal cutoff constant C",
        "Li positivity",
        "RH",
    ):
        assert required in forbidden


def test_no_results_or_mathematical_authority_are_created() -> None:
    module = fixture()
    authorization = module.authorization_document()
    firewall = authorization["result_firewall"]
    for key in (
        "evaluator_path_exists",
        "evaluator_implemented",
        "evaluator_imported",
        "evaluator_executed",
        "validation_receipt_exists",
    ):
        assert firewall[key] is False
    assert firewall["B_JY_values"] == []
    assert firewall["m_JY_values"] == []
    assert firewall["M_JY_values"] == []
    assert firewall["result_state"] == "NOT_EVALUATED"
    authority = authorization["authority"]
    assert authority["operational_authorization_only"] is True
    assert all(
        authority[key] is False
        for key in (
            "candidate_truth",
            "mathematical_result",
            "proof",
            "novelty",
            "independent_review",
            "li_positivity",
            "riemann_hypothesis",
        )
    )
    assert authority["software_or_governance_credit_units"] == 0
