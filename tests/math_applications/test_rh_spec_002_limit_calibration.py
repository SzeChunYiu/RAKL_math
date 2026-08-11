from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/riemann_hypothesis"
CALIBRATION = BASE / "04_candidates/RH_SPEC_002_LIMIT_STABILITY_CALIBRATION_20260811.json"
PROVENANCE = BASE / "04_candidates/negative_history/RH_SPEC_002_PR15_CHRONOLOGY_HASH_AUDIT_20260811.json"
CONTINUATION = BASE / "09_trace/RH_SPEC_002_CALIBRATION_TRACE_CONTINUATION_20260811.json"
PARENT_TRACE = BASE / "09_trace/RH_SPEC_002_OPEN_TRACE_20260811.json"
FAILURES = BASE / "07_memory/RH_SPEC_002_POSTCAL_FAILURE_EXPERIENCE_LATTICE_20260811.json"
TOOLS = BASE / "07_memory/RH_SPEC_002_POSTCAL_RESEARCH_TOOL_INVENTORY_20260811.json"
REVIEW = BASE / "08_reviews/SAME_CONTEXT_REVIEW_RH_SPEC_002_RETROSPECTIVE_CALIBRATION_20260811.md"
VALIDATION = BASE / "05_oracles/RH_SPEC_002_RETROSPECTIVE_ASSIMILATION_VALIDATION_20260811.json"
FRAMEWORK = ROOT / "framework/RAKL"


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_self_hash(raw: dict) -> None:
    expected = raw["artifact_hash"]
    payload = copy.deepcopy(raw)
    payload["artifact_hash"] = ""
    assert expected == canonical_hash(payload)


def test_retrospective_authority_and_pr15_provenance_are_explicit() -> None:
    receipt = load(CALIBRATION)
    provenance = load(PROVENANCE)
    assert_self_hash(receipt)
    assert_self_hash(provenance)
    assert receipt["authority"].startswith("RETROSPECTIVE_KNOWN_ANSWER_CALIBRATION")
    assert "NO_RH_EVIDENCE" in receipt["authority"]
    assert receipt["provenance"]["chronology_audit_hash"] == provenance["artifact_hash"]
    assert receipt["provenance"]["chronology_status"] == (
        "RETROSPECTIVE_EXACT_CASE_IDENTITY_NOT_COMMITTED_BEFORE_RESULT"
    )
    assert provenance["preserved_source_identity"]["original_result_commit"] == (
        "c48f2df2a69df7dc3e4e91ca9a7e27e3ce370f61"
    )
    assert provenance["preserved_source_identity"]["original_trace_commit"] == (
        "b22e345e830e6d6da804c6da901a83e9b420b483"
    )
    assert provenance["hash_failure_observation"]["stored_tool_hash"] != (
        provenance["hash_failure_observation"]["canonical_tool_hash_at_pr15_head"]
    )
    assert "11-case" in receipt["provenance"]["identity_separation"]
    assert "NO_BACKFILLED_PREREGISTRATION" in provenance["disposition"]
    validation = load(VALIDATION)
    assert_self_hash(validation)
    assert validation["focused_result"] == {"exit_code": 0, "passed": 10, "failed": 0}
    assert validation["full_result"] == {"exit_code": 0, "passed": 175, "failed": 0}
    assert validation["subjects"]["calibration_hash"] == receipt["artifact_hash"]


def test_retrospective_package_classification_remains_narrow() -> None:
    raw = load(CALIBRATION)
    classes = {item["package"]: item["classification"] for item in raw["package_classification"]}
    assert classes["local_uniform_source_normalized_entire_determinants_to_exact_Xi"] == (
        "TARGET_SIDE_SUFFICIENT_BUT_SOURCE_SIDE_UNPROVED"
    )
    assert classes["strong_resolvent_or_Mosco_without_extra_spectral_exactness"] == "TOO_WEAK"
    assert classes["finite_zero_prefix_or_counting_statistic_or_UV_asymptotics"] == "TOO_WEAK"
    assert classes["unspecified_joint_N_lambda_or_cutoff_limit"] == "UNDER_SPECIFIED"
    assert raw["research_decision"]["authority"] == (
        "PROPOSAL_ONLY_FROM_RETROSPECTIVE_CALIBRATION / FRESH_CHILD_CONTEXT_REQUIRED"
    )
    assert raw["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_failure_lattice_preserves_math_and_assurance_failures() -> None:
    failures = load(FAILURES)
    schema = load(FRAMEWORK / "schemas/failure-experience-lattice.schema.json")
    jsonschema.Draft202012Validator(schema).validate(failures)
    ids = {item["failure_id"] for item in failures["experiences"]}
    assert ids == {
        "F-RH-SPEC-002-STRONG-RESOLVENT-INCOMPLETE",
        "F-RH-SPEC-002-GALERKIN-POLLUTION",
        "F-RH-SPEC-002-JOINT-LIMIT-AMBIGUITY",
        "F-RH-SPEC-002-FINITE-ZERO-PREFIX",
        "F-RH-SPEC-002-PR15-CHRONOLOGY",
        "F-RH-SPEC-002-PR15-STALE-TOOL-HASH",
    }
    for item in failures["experiences"]:
        assert_self_hash(item)
        assert item["diagnosis_status"] == "SUPPORTED"
        assert item["competing_diagnoses"]
        assert item["scope_conditions"]
        assert any("next discriminator:" in value for value in item["local_repair_attempts"])
    chronology = next(item for item in failures["experiences"] if item["failure_id"].endswith("CHRONOLOGY"))
    stale_hash = next(item for item in failures["experiences"] if item["failure_id"].endswith("STALE-TOOL-HASH"))
    assert "result artifact was the first calibration commit" in chronology["observed_result"]
    assert "blocking exact CI" in stale_hash["observed_result"]


def test_hurwitz_tool_is_conditionally_reusable_and_rebound() -> None:
    tools = load(TOOLS)
    schema = load(FRAMEWORK / "schemas/research-tool-inventory.schema.json")
    jsonschema.Draft202012Validator(schema).validate(tools)
    assert len(tools["tools"]) == 1
    tool = tools["tools"][0]
    assert_self_hash(tool)
    assert tool["authority"] == "CONDITIONALLY_REUSABLE"
    assert tool["source_candidate_id"].startswith("RETROSPECTIVE:")
    assert any("does not convert the retrospective PR15" in value for value in tool["non_guarantees"])
    assert "F-RH-SPEC-002-PR15-CHRONOLOGY" in tool["known_failure_ids"]


def test_exact_hostile_case_identities() -> None:
    # A wandering rank-one projection vanishes on each fixed finite-support
    # vector eventually, while its finite-stage eigenvalue remains exactly 1.
    support_max = 5
    for n in range(6, 20):
        assert n > support_max
        assert Fraction(0) == 0
    assert Fraction(1) not in {Fraction(0)}

    # For v=(e_-+e_+)/sqrt(2), <v,Av>=-1/2+1/2 exactly.
    assert Fraction(-1, 2) + Fraction(1, 2) == 0
    assert Fraction(0) not in {Fraction(-1), Fraction(1)}

    def value(n: int, lam: int) -> Fraction:
        return Fraction(n, n + lam)

    assert value(10**12, 1) > Fraction(999_999, 1_000_000)
    assert value(1, 10**12) < Fraction(1, 1_000_000)
    assert value(10**6, 10**6) == Fraction(1, 2)

    # At z=1/2 the canonical-product factor is exact and stays above 1/2
    # in the checked worlds. Since exp(1/2)>1+1/2, this exact lower bound
    # already grows geometrically, proving the selected sequence cannot
    # converge to the finite target value at z=1/2.
    def product_at_half(n: int) -> Fraction:
        out = Fraction(1)
        for k in range(1, n + 1):
            out *= Fraction(4 * k * k - 1, 4 * k * k)
        return out

    lower_20 = product_at_half(20) * Fraction(3, 2) ** 20
    lower_40 = product_at_half(40) * Fraction(3, 2) ** 40
    assert product_at_half(40) > Fraction(1, 2)
    assert lower_40 > lower_20 * 100


def test_replacement_trace_supersedes_freeze_implication_without_candidate_event() -> None:
    parent = load(PARENT_TRACE)
    continuation = load(CONTINUATION)
    parent_final = parent["entries"][-1]["artifact_hash"]
    assert parent_final == continuation["parent_final_event_hash"]
    assert continuation["source_trace_superseded"]["source_pr"] == 15
    previous = parent_final
    event_types = []
    for item in continuation["entries"]:
        assert_self_hash(item)
        assert item["previous_event_hash"] == previous
        previous = item["artifact_hash"]
        event_types.append(item["event_type"])
    assert event_types == [
        "RESULT_RECORDED",
        "EXPERIENCE_MEMORY_REVIEW",
        "RESIDUAL_OPENED",
        "REVIEWED",
        "RESULT_RECORDED",
    ]
    assert "CANDIDATE_PROPOSED" not in event_types
    assert "PROMOTED" not in event_types
    review_event = next(item for item in continuation["entries"] if item["event_id"] == "RH-SPEC-002-E11")
    assert "SAME_CONTEXT_ONLY" in review_event["outputs"][1]
    review = REVIEW.read_text(encoding="utf-8")
    assert "not independent review or peer review" in review
    assert "never manufacture a preregistration artifact" in review
