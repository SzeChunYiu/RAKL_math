from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/riemann_hypothesis/09_trace/rh_ana003k_jy_ratio_candidate_freeze_fixture.py"


def fixture():
    spec=importlib.util.spec_from_file_location("rh_ana003k_c001_freeze",FIXTURE)
    assert spec and spec.loader
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def load(path: str) -> dict:
    value=json.loads((ROOT/path).read_text());assert isinstance(value,dict);return value


def test_fixture_reproduces_exact_inert_freeze_artifacts() -> None:
    module=fixture();docs=module.build_all()
    assert set(docs)==set(module.PATHS.values())
    for path,expected in docs.items():
        assert load(path)==expected
        if "artifact_hash" in expected:
            assert expected["artifact_hash"]==module.hash_with_blank(expected,"artifact_hash")
    event=docs[module.PATHS["trace"]]["entries"][0]
    assert event["previous_event_hash"]==module.PREVIOUS_EVENT_HASH
    assert event["artifact_hash"]==module.hash_with_blank(event,"artifact_hash")


def test_candidate_freezes_exact_theorem_quantifiers_and_seven_obligations() -> None:
    module=fixture();docs=module.build_all();candidate=docs[module.PATHS["candidate"]]
    assert candidate["candidate_id"]=="RH-ANA-003k-JY-C001-FLOOR-RATIO-ASYMPTOTIC"
    core=module.candidate_core()
    assert "For every fixed C>0" in core["theorem_statement_to_evaluate_later"]
    assert "lim_(n->infinity) rho_C(n)=0" in core["theorem_statement_to_evaluate_later"]
    assert "u_n(C)<F_n<=U_JY(n)<=ceil(U_JY(n))<=tilde_m_JY(n,epsilon)" in core["theorem_statement_to_evaluate_later"]
    assert core["definitions"]["F_n"]=="[2(n+0.515)/0.8274]^2"
    assert len(candidate["proof_obligations"])==7
    assert candidate["frozen_constant_contract"]=={"C":"arbitrary fixed real C>0","C_may_depend_on_n":False,"numeric_C_selected":False,"epsilon_sequence_needed_for_floor_result":False}


def test_scope_is_current_sufficient_certificate_only() -> None:
    module=fixture();docs=module.build_all();candidate=docs[module.PATHS["candidate"]]
    interpretation=candidate["exact_scoped_interpretation_if_proved"]
    assert "current Johnston--Yang sufficient certificate" in interpretation
    assert "only failure of that sufficient certificate" in interpretation
    exclusions=" ".join(candidate["non_implications"])
    assert "actual natural-order remainder" in exclusions
    assert "Li coefficient" in exclusions
    assert "Riemann hypothesis" in exclusions
    assert candidate["authority"]["root_state"]=="OPEN_NO_SOLUTION_CERTIFICATE"


def test_no_limit_result_or_evaluator_execution_occurs() -> None:
    module=fixture();docs=module.build_all();candidate=docs[module.PATHS["candidate"]]
    assert candidate["status"]=="FROZEN_UNEVALUATED_ELEMENTARY_ASYMPTOTIC_CANDIDATE"
    assert all(value is False for value in candidate["evaluation_firewall"].values())
    evaluator=docs[module.PATHS["evaluator"]]
    assert evaluator["evaluator_identity"]["kind"]=="INERT_SYMBOLIC_PROOF_CONTRACT_NO_IMPLEMENTATION"
    assert all(value is False for value in evaluator["current_round_firewall"].values())
    assert "computation alone is corroboration only" in evaluator["evaluator_identity"]["proof_authority_requirement"]
    authorization=docs[module.PATHS["authorization"]]
    assert authorization["current_round"]["implementation_authorized"] is False
    assert authorization["current_round"]["execution_authorized"] is False
    assert authorization["current_round"]["result_classification_authorized"] is False


def test_falsifiers_detect_quantifier_chain_and_scope_errors() -> None:
    module=fixture();docs=module.build_all();falsifier=docs[module.PATHS["falsifier"]]
    worlds={world["world_id"]:world for world in falsifier["worlds"]}
    assert len(worlds)==10
    assert worlds["FAIL-C-DEPENDS-ON-N"]["expected_future_classification"]=="FAIL_QUANTIFIER_CONTRACT"
    assert worlds["FAIL-CEILING-DIRECTION"]["expected_future_classification"]=="FAIL_FLOOR_CHAIN"
    assert worlds["FAIL-CERTIFICATE-TO-OBJECT"]["expected_future_classification"]=="FAIL_SCOPE_OVERREACH"
    assert worlds["CANNOT-CHECK-PROOF"]["expected_future_classification"]=="CANNOT_CHECK"
    assert all(world["materialized"] is False for world in worlds.values())
    assert falsifier["result_state"]=="NO_FALSIFIER_RUN_NO_RESULT_CLASSIFICATION"


def test_lesson_is_mathematical_seven_field_and_pre_result() -> None:
    module=fixture();docs=module.build_all();lesson=docs[module.PATHS["lesson"]]
    fields={"attempted_implication","exact_result_or_failure","supported_and_competing_causes","scope","mathematical_falsifier","mathematical_repair","proof_source_evidence"}
    assert all(lesson[field] for field in fields)
    assert "No result yet" in lesson["exact_result_or_failure"]
    assert "zero mathematical credit" in lesson["nonmathematical_governance_note"]
    assert lesson["authority"]["mathematical_result"] is False


def test_authorization_binds_serialized_identities_and_requires_later_activation() -> None:
    module=fixture();docs=module.build_all();authorization=docs[module.PATHS["authorization"]]
    for name,binding in authorization["exact_identity_bindings"].items():
        raw=(json.dumps(docs[module.PATHS[name]],indent=2,sort_keys=True)+"\n").encode()
        import hashlib
        assert binding["raw_sha256"]=="sha256:"+hashlib.sha256(raw).hexdigest()
    assert authorization["status"]=="FROZEN_INERT_UNTIL_MERGED_AND_SEPARATELY_ACTIVATED"
    assert "later round" in authorization["post_merge_activation"]["condition"]
    assert authorization["authority"]["software_credit_units"]==0
