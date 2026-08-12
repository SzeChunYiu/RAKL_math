from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

from rakl.structural_types import TransferDecision
from rakl.structural_transport_v2 import ObligationKind, ObligationStatus


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c052_structural_transport_v2_audit_fixture.py"
RECEIPT = PNP / "08_reviews/O9d12a2a1b_C052_STRUCTURAL_TRANSPORT_V2_AUDIT_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("pnp_c052_transport_v2_audit", FIXTURE)
    assert spec is not None and spec.loader is not None
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def test_c052_transport_audit_matches_machine_readable_receipt() -> None:
    m = module()
    expected = m.build_document()
    assert json.loads(RECEIPT.read_text(encoding="utf-8")) == expected
    claimed = expected["artifact_hash"].removeprefix("sha256:")
    content = dict(expected)
    content["artifact_hash"] = ""
    raw = json.dumps(content, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert hashlib.sha256(raw).hexdigest() == claimed
    documents = m.build_documents()
    for name in ("framework_rebinding", "framework_revalidation"):
        path = ROOT / m.PATHS[name]
        assert json.loads(path.read_text(encoding="utf-8")) == documents[name]


def test_c052_current_framework_rebind_is_chronological_not_retroactive() -> None:
    m = module()
    documents = m.build_documents()
    binding = documents["framework_rebinding"]
    observation = documents["framework_revalidation"]
    assert binding["authoritative_framework_sha"] == m.FRAMEWORK_CURRENT_SHA
    assert binding["rebind_chronology"]["historical_context_framework_binding_sha"] == m.HISTORICAL_CONTEXT_FRAMEWORK_SHA
    assert binding["rebind_chronology"]["historical_context_binding_preserved_not_rewritten"] is True
    assert binding["rebind_chronology"]["historical_preaction_application_pin"] == m.HISTORICAL_PREACTION_APPLICATION_PIN_SHA
    assert binding["rebind_chronology"]["candidate_or_falsifier_identity_existed_at_rebind"] is False
    assert binding["rebind_chronology"]["historical_identity_only_license_status_before_revalidation"] == (
        "STALE_FOR_ANY_FUTURE_CLASSIFIER_FREEZE"
    )
    assert binding["intervening_surface_classification"]["protected_added_at_496edc"] == [
        "src/rakl/structural_transport_v2.py"
    ]
    assert observation["verdict"] == "CURRENT_UNCHANGED"
    assert observation["licenses_candidate_materialization"] is True
    assert observation["licensed_action"] == "PRESERVE_PRIOR_IDENTITY_FREEZE_ONLY_LICENSE"
    assert observation["supersession"]["historical_62e97d_identity_only_license"] == "STALE_FOR_FUTURE_USE"
    assert observation["supersession"]["current_a6946c7_mandatory_gate_revalidation"] == (
        "SUPERSEDES_HISTORICAL_LICENSE_FOR_FUTURE_CLASSIFIER_FREEZE"
    )
    optional = observation["optional_transport_v2_disposition"]
    assert optional["wired_into_mandatory_C052_gate"] is False
    assert optional["audit_verdict"] == "CANNOT_CHECK"
    assert optional["blocks_already_supported_same_domain_identity_freeze_route"] is False
    assert optional["blocks_transport_v2_certified_mapping_claim"] is True
    assert optional["blocks_theorem_or_mathematical_result_claim"] is True
    assert observation["classifier_or_falsifier_execution_authorized"] is False
    assert observation["mathematical_result_credit"] == 0


def test_c052_audit_is_obligation_level_and_fails_closed() -> None:
    m = module()
    source, target, witness, assessment = m.build_assessment()
    assert source.qoi == target.qoi == witness.qoi == m.EXACT_QOI
    assert assessment.decision is TransferDecision.CANNOT_CHECK

    required_kinds = {
        ObligationKind.QOI,
        ObligationKind.ROLE,
        ObligationKind.RELATION,
        ObligationKind.INVARIANT,
        ObligationKind.PRECONDITION,
        ObligationKind.BOUNDARY,
        ObligationKind.FORBIDDEN_LOSS,
    }
    assert {item.kind for item in witness.obligations} == required_kinds
    assert len([item for item in witness.obligations if item.kind is ObligationKind.ROLE]) == 7
    assert len([item for item in witness.obligations if item.kind is ObligationKind.RELATION]) == 5
    assert len([item for item in witness.obligations if item.kind is ObligationKind.INVARIANT]) == 5
    # Five exact episode preconditions plus the downstream target-blind identity obligation.
    assert len([item for item in witness.obligations if item.kind is ObligationKind.PRECONDITION]) == 6
    assert len([item for item in witness.obligations if item.kind is ObligationKind.BOUNDARY]) == 5
    assert len([item for item in witness.obligations if item.kind is ObligationKind.FORBIDDEN_LOSS]) == 6

    traces = {item.obligation_id: item for item in assessment.traces}
    assert traces["PRE-ESCAPE-OUTPUTS-PRESERVED"].status is ObligationStatus.UNKNOWN
    assert traces["PRE-FUTURE-IDENTITIES-TARGET-BLIND"].status is ObligationStatus.UNKNOWN
    assert all(
        traces[f"LOSS-{index:02d}"].status is ObligationStatus.UNKNOWN
        for index in range(1, 7)
    )
    assert "requires_external_verifier" in assessment.reasons
    assert "forbidden_loss_preservation_unverified" in assessment.reasons


def test_c052_audit_preserves_scope_and_has_zero_math_credit() -> None:
    document = module().build_document()
    assert document["framework_binding"] == {
        "current_runtime_sha": "a6946c740b50413faf0eee218cc490dd6383e9ab",
        "structural_transport_v2_introduction_sha": "496edc5ead136980287ac2e72efb486691945366",
        "structural_transport_v2_sha256": "f8b03ab9965f04400fac2d74c8c533e2354046025887b6aefd8b79968cf99e87",
        "quantifier_runtime_sha256": "cbbf7c125a505f4914a2253e75e5a809c67fb74e8193cc31d19ab3019938accc",
        "quantifier_schema_sha256": "2874ab098fd28941c1e001abdb90b2a164d0af6fe282bbcbdf68bdb38403917f",
    }
    assert document["authority"] == {
        "audit_decision": "CANNOT_CHECK",
        "classifier_or_falsifier_identity_created": False,
        "execution_authority": False,
        "mathematical_result_credit": 0,
        "proof_authority": False,
        "mandatory_same_domain_identity_freeze_route_blocked": False,
        "transport_v2_certified_candidate_generation_authority": False,
        "independent_review_credit": 0,
        "git_ci_schema_hash_chronology_credit": 0,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    }
    lesson = document["seven_field_mathematical_lesson"]
    assert set(lesson) == {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_discriminator",
        "proof_and_source_evidence",
    }
    text = json.dumps(document, sort_keys=True)
    for forbidden in (
        "target_k_selected\": true",
        "new_k_enumeration_authorized\": true",
        "classifier_identity_created\": true",
        "falsifier_identity_created\": true",
        "mathematical_result_credit\": 1",
    ):
        assert forbidden not in text


def test_c052_audit_fixture_has_no_result_capability() -> None:
    text = FIXTURE.read_text(encoding="utf-8")
    for forbidden in (
        "from C041_fx_sat_one_sided",
        "import C041_fx_sat_one_sided",
        "decode_formula(",
        "is_satisfiable(",
        "materialize_complement(",
        "import subprocess",
        "import z3",
        "import pysat",
    ):
        assert forbidden not in text
