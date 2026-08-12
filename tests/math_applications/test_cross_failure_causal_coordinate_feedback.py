from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/cross_problem/10_case_study/cross_failure_causal_coordinate_fixture.py"
ARTIFACT = ROOT / "research/real_math/millennium/cross_problem/10_case_study/CROSS_FAILURE_CAUSAL_COORDINATE_FEEDBACK_20260812.json"
SEVEN = {
    "attempted_mathematical_implication",
    "exact_result_or_failure",
    "supported_and_competing_mathematical_causes",
    "scope",
    "mathematical_falsifier",
    "repair_or_next_discriminator",
    "proof_or_source_evidence",
}


def module():
    spec = importlib.util.spec_from_file_location("cross_coordinate", FIXTURE)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def load() -> dict:
    return json.loads(ARTIFACT.read_text(encoding="utf-8"))


def test_artifact_is_exactly_reproducible_and_source_bound() -> None:
    fixture = module()
    artifact = load()
    assert artifact == fixture.build()
    assert artifact["artifact_hash"] == fixture.artifact_hash(artifact)
    for witness in artifact["mathematical_witnesses"]:
        assert SEVEN <= witness.keys()
        assert witness["load_bearing_coordinate"]
        assert witness["causal_status"]
        assert witness["disanalogy"]
        for evidence in witness["proof_or_source_evidence"]:
            assert evidence == fixture.source_binding(evidence["path"])


def test_synthesis_is_morphology_not_cross_domain_causal_claim() -> None:
    artifact = load()
    morphology = artifact["shared_obstruction_morphology"]
    assert "shared morphology only" in morphology["causal_claim_boundary"]
    assert "No common cross-domain causal mechanism is proved" in morphology["causal_claim_boundary"]
    assert {row["problem"] for row in artifact["mathematical_witnesses"]} == {
        "P_VS_NP",
        "RIEMANN_HYPOTHESIS",
        "BIRCH_AND_SWINNERTON_DYER",
        "YANG_MILLS",
    }
    rh = next(row for row in artifact["mathematical_witnesses"] if row["problem"] == "RIEMANN_HYPOTHESIS")
    assert "still-unevaluated" in rh["mathematical_falsifier"]
    assert "preregistered expected branch" in rh["mathematical_falsifier"]


def test_activation_requires_distinct_math_failures_and_controls() -> None:
    challenger = load()["rakl_challenger"]
    activation = challenger["activation_rule"]
    assert activation["minimum_genuinely_distinct_bounded_failures"] == 2
    assert any("not duplicate artifacts" in row for row in activation["requirements"])
    assert any("software" in row.lower() for row in challenger["non_activation_worlds"])
    assurance = challenger["fresh_matched_assurance"]
    assert assurance["required"] is True
    assert "INCUMBENT_RAKL" in assurance["arms"]
    assert any("non-activation" in row for row in assurance["worlds"])
    assert any("CANNOT_CHECK" in row for row in assurance["worlds"])
    assert assurance["falsifier"]
    relation = challenger["current_framework_relation"]
    assert relation["present_classification"] == "OPTIONAL_METHOD_ADJACENT_UNWIRED_TO_MANDATORY_MATHEMATICAL_GATES"
    assert "no natural mathematical efficacy evidence" in relation["evidence_boundary"]
    assert "do not replace failure-diagnosis routing" in relation["evidence_boundary"]
    assert "no new method surface" in relation["consequence"]


def test_zero_authority_and_all_roots_open() -> None:
    artifact = load()
    assert artifact["status"] == "QUARANTINED_PROPOSAL"
    authority = artifact["authority_contract"]
    assert authority["mathematical_credit_units_created"] == 0
    assert all(value is False for key, value in authority.items() if key != "mathematical_credit_units_created")
    assert set(artifact["root_states"].values()) == {"OPEN_NO_SOLUTION_CERTIFICATE"}
    assert artifact["rakl_challenger"]["new_method_surface_requested"] is False
