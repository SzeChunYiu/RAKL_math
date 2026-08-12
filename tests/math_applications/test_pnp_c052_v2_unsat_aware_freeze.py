from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = BASE / "09_trace/c052_v2_unsat_aware_freeze_fixture.py"
CONTEXT = BASE / "01_frontier/O9d12a2a1b_C052_V2_UNSAT_AWARE_CONTEXT_DELTA_20260812.json"
MEMORY = BASE / "07_memory/O9d12a2a1b_C052_V2_RESEARCH_MEMORY_REVIEW_20260812.json"
REVIEW = BASE / "08_reviews/O9d12a2a1b_C052_V2_EXPERT_CONTEXT_REVIEW_20260812.json"
CLASSIFIER = BASE / "04_candidates/O9d12a2a1b_C052_V2_UNSAT_AWARE_CLASSIFIER_IDENTITY_20260812.json"
FALSIFIER = BASE / "05_falsification/O9d12a2a1b_C052_V2_INDEPENDENT_FALSIFIER_IDENTITY_20260812.json"
TRAP = BASE / "05_falsification/O9d12a2a1b_C052_V2_SEMANTIC_SUBSET_TRAP_IDENTITY_20260812.json"
AUTH = BASE / "09_trace/O9d12a2a1b_C052_V2_FRESH_HOSTILE_AUTHORIZATION_20260812.json"
TRACE = BASE / "09_trace/O9d12a2a1b_C052_V2_IDENTITY_FREEZE_TRACE_20260812.json"
REVALIDATION = BASE / "09_trace/O9d12a2a1b_C052_V2_FRAMEWORK_REVALIDATION_D21592B_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_v2_freeze", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def raw_sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def test_v2_freeze_artifacts_match_inert_serializer() -> None:
    built = module().build()
    paths = [CONTEXT, MEMORY, REVIEW, CLASSIFIER, FALSIFIER, TRAP, AUTH, TRACE, REVALIDATION]
    assert [load(path) for path in paths] == list(built)
    assert load(CLASSIFIER)["status"] == "FROZEN_NOT_EXECUTED"
    assert load(FALSIFIER)["status"] == "FROZEN_NOT_EXECUTED"
    assert load(AUTH)["chronology"] == {
        "v2_classifier_implemented": False,
        "v2_falsifier_implemented": False,
        "semantic_subset_trap_executed": False,
        "fresh_hostile_world_materialized": False,
        "fresh_hostile_world_executed": False,
        "native_parametric_evaluation_executed": False,
        "decoder_sat_overlap_executed": False,
    }


def test_v2_escape_requires_witnesses_inside_hk_not_ambient_syntax() -> None:
    classifier = load(CLASSIFIER)
    escape = classifier["certificate_interfaces"]["escape_admissible"]
    assert "explicit_canonical_UNSAT_formula_in_H_k_for_each_coordinate_matching_MAGIC" in escape
    assert "truth_or_symbolic_UNSAT_proof_for_each_formula" in escape
    assert "both_bits_in_H_k_if_variability_is_claimed" in escape
    assert "ambient_syntax_variation_is_insufficient" in escape
    assert classifier["semantic_domain"] == (
        "H_k, the canonical UNSAT parent language at half-length k; not the ambient canonical syntax language"
    )
    assert classifier["result_algebra"]["ordered_precedence"] == [
        "CANNOT_CHECK",
        "FORCED_CONFLICT",
        "ESCAPE_ADMISSIBLE",
        "UNRESOLVED",
    ]


def test_planted_semantic_subset_trap_catches_ambient_only_escape() -> None:
    trap = load(TRAP)
    assert trap["ambient_syntax_bits_at_coordinate"] == [0, 1]
    assert trap["semantic_subset_bits_at_coordinate"] == [0]
    assert trap["MAGIC_bit"] == 1
    assert trap["expected_v2_branch"] == "FORCED_CONFLICT"
    assert trap["ambient_only_buggy_branch"] == "ESCAPE_ADMISSIBLE"
    assert trap["failure_if"] == (
        "v2 returns ESCAPE_ADMISSIBLE from ambient variation without an H_k-preserving witness"
    )


def test_falsifier_is_distinct_and_recomputes_semantic_membership() -> None:
    classifier = load(CLASSIFIER)
    falsifier = load(FALSIFIER)
    assert raw_sha(CLASSIFIER) != raw_sha(FALSIFIER)
    assert falsifier["independence_boundary"]["classifier_import_allowed"] is False
    assert falsifier["independence_boundary"]["classifier_certificate_reuse_allowed"] is False
    assert falsifier["independent_checks"][:3] == [
        "recompute exact adjacent support and derived padding",
        "recompute h[0] versus h[1]=c[0] indexing and token phase",
        "validate every escape witness is canonical, has the registered length, and is UNSAT",
    ]
    assert classifier["identity_id"] != falsifier["identity_id"]
    auth = load(AUTH)
    assert auth["identity_bytes"] == {
        "classifier_raw_sha256": raw_sha(CLASSIFIER),
        "falsifier_raw_sha256": raw_sha(FALSIFIER),
        "semantic_trap_raw_sha256": raw_sha(TRAP),
        "byte_distinct": True,
    }


def test_fresh_hidden_world_excludes_consumed_k20_and_is_not_materialized() -> None:
    auth = load(AUTH)
    fresh = auth["fresh_hidden_hostile_world"]
    assert fresh["world_id"] == "C052-V2-FRESH-HIDDEN-UNSAT-AWARE-HOSTILE-v1"
    assert fresh["excluded_consumed_half_lengths"] == [20]
    assert fresh["value_status"] == "WITHHELD_NOT_MATERIALIZED_NOT_EXECUTED"
    assert fresh["ordering"] == "LEXICOGRAPHIC_ASCENDING"
    assert fresh["bounded_domain"] == {
        "k": [8, 128],
        "a": [1, 8],
        "m": [2, 32],
        "a_plus": [1, 8],
        "m_plus": [1, 32],
    }
    assert auth["mandatory_future_execution_order"] == [
        "C050-k15-bounded-regression",
        "C051-k19-bounded-regression",
        "C052-V2-SEMANTIC-SUBSET-TRAP-v1",
        "C052-V2-FRESH-HIDDEN-UNSAT-AWARE-HOSTILE-v1",
    ]


def test_v2_context_memory_and_review_bind_the_exact_math_failure() -> None:
    context = load(CONTEXT)
    memory = load(MEMORY)
    review = load(REVIEW)
    assert context["atomic_obstruction"] == (
        "Certify local forced-bit escape over H_k without substituting ambient canonical syntax for the UNSAT semantic subset."
    )
    assert context["consumed_hidden_validation_worlds"] == [
        "C052 v1 controlled hostile world at k=20"
    ]
    assert context["k20_future_status"] == (
        "PUBLIC_REGRESSION_OR_NONACTIVATION_USE_ALLOWED_BUT_NOT_FRESH_HIDDEN_VALIDATION"
    )
    assert memory["relevant_failure_ids"] == [
        "F-PNP-C052-V1-UNSAT-SUBSET-OMISSION",
        "F-PNP-C052-LOCAL-FORCED-CONFLICT-UNIVERSALITY-REFUTED",
    ]
    assert review["strongest_objection"].startswith("A syntactically variable bit may be fixed")
    assert review["review_boundary"] == "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW"
    lesson = context["seven_field_mathematical_failure_lesson"]
    assert set(lesson) == {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "falsifier",
        "mathematical_repair",
        "proof_and_source_evidence",
    }
    assert "ambient canonical syntax" in lesson["exact_result_or_failure"]


def test_trace_freezes_all_precandidate_steps_before_v2_identity() -> None:
    trace = load(TRACE)
    assert [entry["event_type"] for entry in trace["entries"][-9:]] == [
        "ATOMIZED",
        "CONTEXT_FROZEN",
        "ANALOGY_SCAN",
        "METHOD_TRANSFER_REVIEW",
        "EXPERT_CONTEXT_REVIEW",
        "EXPERIENCE_MEMORY_REVIEW",
        "OBSTRUCTION_TRANSFORMATION_REVIEW",
        "NEXT_STEP_PROPOSED",
        "CANDIDATE_PROPOSED",
    ]
    for previous, current in zip(trace["entries"], trace["entries"][1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    assert trace["entries"][-1]["outputs"][-1] == "ZERO_MATHEMATICAL_RESULT_CREDIT"


def test_latest_framework_revalidation_changes_no_protected_math_gate() -> None:
    observation = load(REVALIDATION)
    assert observation["observed_current_main_sha"] == "d21592b0ff8da988deabb923fd549891ff8ad9f0"
    assert observation["protected_mathematical_gate_files_changed"] == []
    assert observation["mathematical_result_credit"] == 0
    assert observation["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_v2_fixture_has_no_implementation_or_hidden_world_execution_surface() -> None:
    source = FIXTURE.read_text(encoding="utf-8")
    forbidden = [
        "def classify(",
        "def audit(",
        "def materialize(",
        "decode_formula",
        "is_satisfiable",
        "materialize_complement",
    ]
    assert not any(token in source for token in forbidden)
