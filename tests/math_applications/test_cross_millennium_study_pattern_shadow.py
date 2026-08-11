from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError


ROOT = Path(__file__).resolve().parents[2]
BASE = (
    ROOT
    / "research/real_math/millennium/cross_problem/10_study_pattern"
)
PINNED_FRAMEWORK = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
SOURCE_COMMIT = "e05613ae4a86f8fbdc842bb51a51e41d5150d1fc"
SOURCE_TREE = "dcd5a558a38190ff9d28eb22484587a4f5b18851"
MEMORY_FIRST_ORDER = [
    "QUERY_CANONICAL_RESEARCH_TOOL_INVENTORY",
    "QUERY_CANONICAL_FAILURE_LATTICE",
    "FREEZE_EXPERIENCE_MEMORY_REVIEW",
    "LOAD_QUARANTINED_EPISODE_AND_LESSON_PROPOSALS",
    "APPLY_CAPPED_SEARCH_PRIORITY_ADVISORY",
    "RECORD_NEXT_STEP_PROPOSED",
]
FORBIDDEN_GRANTS = (
    "grants_tool_authority",
    "grants_proof_authority",
    "grants_gluing_authority",
    "grants_theorem_authority",
    "grants_framework_authority",
    "grants_review_independence",
)


def _load(name: str) -> dict:
    value = json.loads((BASE / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: dict) -> str:
    unhashed = copy.deepcopy(value)
    unhashed["artifact_hash"] = ""
    raw = json.dumps(
        unhashed,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *arguments],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _validator(schema_name: str) -> Draft202012Validator:
    schema = _load(schema_name)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _assert_frozen_authority(contract: dict, *, allowed_effect: str) -> None:
    assert contract["effective_authority"] == "PROPOSAL_ONLY"
    assert contract["allowed_effect"] == allowed_effect
    for field in FORBIDDEN_GRANTS:
        assert contract[field] is False


def _assert_safe_preregistration(document: dict) -> None:
    assert document["status"] == "FROZEN_BEFORE_PILOT_RESULTS"
    assert document["authority"] == "PROPOSAL_ONLY"
    assert document["incumbent_framework"]["commit_sha"] == PINNED_FRAMEWORK
    assert document["unmerged_challenger_design_input"]["state_at_freeze"] == (
        "OPEN_UNMERGED_UNTRUSTED"
    )
    arms = {arm["arm_id"]: arm for arm in document["arms"]}
    assert arms["B_CANONICAL_THEN_QUARANTINED"]["ordered_steps"] == (
        MEMORY_FIRST_ORDER
    )
    _assert_frozen_authority(
        document["authority_contract"], allowed_effect="SEARCH_PRIORITY_ONLY"
    )
    assert document["decision_rule"]["framework_promotion"] == (
        "FORBIDDEN_FROM_THIS_PILOT"
    )


def test_shadow_proposals_are_self_hashed_schema_valid_and_dual_lineage() -> None:
    episode_validator = _validator("EXPERIENCE_EPISODE_PROPOSAL.schema.json")
    lesson_validator = _validator("LESSON_PROPOSAL.schema.json")
    support = _load("EXPERIENCE_EPISODE_PROPOSAL_SUPPORT_EXAMPLE_20260811.json")
    contradiction = _load(
        "EXPERIENCE_EPISODE_PROPOSAL_CONTRADICTION_EXAMPLE_20260811.json"
    )
    lesson = _load("LESSON_PROPOSAL_EXAMPLE_20260811.json")

    for episode in (support, contradiction):
        episode_validator.validate(episode)
        assert episode["artifact_hash"] == _canonical_hash(episode)
        _assert_frozen_authority(
            episode["authority_contract"], allowed_effect="SEARCH_PRIORITY_ONLY"
        )
    lesson_validator.validate(lesson)
    assert lesson["artifact_hash"] == _canonical_hash(lesson)
    _assert_frozen_authority(
        lesson["authority_contract"], allowed_effect="SEARCH_PRIORITY_ONLY"
    )

    assert support["source_role"] == "SUPPORT"
    assert contradiction["source_role"] == "CONTRADICTION"
    assert lesson["supporting_episode_proposal_ids"] == [support["proposal_id"]]
    assert lesson["contradicting_episode_proposal_ids"] == [
        contradiction["proposal_id"]
    ]
    assert lesson["memory_precedence"] == {
        "framework_commit": PINNED_FRAMEWORK,
        "ordered_steps": MEMORY_FIRST_ORDER,
    }
    assert lesson["authority_contract"]["maximum_absolute_priority_delta"] == 0.1
    assert lesson["authority_contract"]["may_change_candidate_eligibility"] is False
    assert lesson["authority_contract"]["may_override_canonical_memory"] is False
    assert lesson["authority_contract"]["may_suppress_failure_warning"] is False


@pytest.mark.parametrize(
    ("target", "mutation"),
    [
        ("episode", ("effective_authority", "PROOF_BACKED")),
        ("episode", ("grants_theorem_authority", True)),
        ("episode", ("grants_framework_authority", True)),
        ("lesson", ("allowed_effect", "TOOL_PROMOTION")),
        ("lesson", ("maximum_absolute_priority_delta", 100.0)),
        ("lesson", ("may_change_candidate_eligibility", True)),
        ("lesson", ("may_suppress_failure_warning", True)),
        ("lesson", ("grants_gluing_authority", True)),
    ],
)
def test_hostile_caller_cannot_mint_authority_through_proposal_fields(
    target: str, mutation: tuple[str, object]
) -> None:
    if target == "episode":
        validator = _validator("EXPERIENCE_EPISODE_PROPOSAL.schema.json")
        document = _load(
            "EXPERIENCE_EPISODE_PROPOSAL_SUPPORT_EXAMPLE_20260811.json"
        )
    else:
        validator = _validator("LESSON_PROPOSAL.schema.json")
        document = _load("LESSON_PROPOSAL_EXAMPLE_20260811.json")
    field, value = mutation
    document["authority_contract"][field] = value
    with pytest.raises(ValidationError):
        validator.validate(document)

    injected = _load(
        "EXPERIENCE_EPISODE_PROPOSAL_SUPPORT_EXAMPLE_20260811.json"
        if target == "episode"
        else "LESSON_PROPOSAL_EXAMPLE_20260811.json"
    )
    injected["requested_authority"] = "PROOF_BACKED"
    with pytest.raises(ValidationError):
        validator.validate(injected)


def test_preregistered_pilot_is_frozen_matched_and_fails_closed_on_hostile_order() -> None:
    prereg = _load("STUDY_PATTERN_AB_PILOT_PREREGISTRATION_20260811.json")
    assert prereg["artifact_hash"] == _canonical_hash(prereg)
    _assert_safe_preregistration(prereg)

    assert [case["stratum"] for case in prereg["cases"]] == [
        "KNOWN_ANSWER",
        "KNOWN_ANSWER",
        "NEAR_SOLVED",
        "NEAR_SOLVED",
    ]
    assert set(prereg["metrics"]) == {
        "repeat_failure_detection_rate",
        "valid_next_action_rate",
        "cost",
        "false_lesson_rate",
    }
    assert prereg["metrics"]["false_lesson_rate"].endswith(
        "zero denominator is CANNOT_CHECK, not zero"
    )
    assert prereg["matched_resources"]["trials_per_arm_case"] == 1
    assert prereg["evaluator"]["separation"] == (
        "same-context protected evaluator packet; not independent peer review"
    )
    assert prereg["result_receipt_contract"]["hash_rule"] == (
        "canonical JSON SHA-256 with artifact_hash blank"
    )

    hostile = copy.deepcopy(prereg)
    hostile["arms"][1]["ordered_steps"] = [
        "LOAD_QUARANTINED_EPISODE_AND_LESSON_PROPOSALS",
        *MEMORY_FIRST_ORDER[:3],
        *MEMORY_FIRST_ORDER[-2:],
    ]
    with pytest.raises(AssertionError):
        _assert_safe_preregistration(hostile)

    hostile = copy.deepcopy(prereg)
    hostile["authority_contract"]["grants_tool_authority"] = True
    with pytest.raises(AssertionError):
        _assert_safe_preregistration(hostile)


def test_source_and_successor_receipts_have_exact_non_circular_git_bindings() -> None:
    receipt = _load("STUDY_PATTERN_SOURCE_BINDING_RECEIPT_20260811.json")
    assert receipt["artifact_hash"] == _canonical_hash(receipt)
    assert receipt["source_commit_sha"] == SOURCE_COMMIT
    assert receipt["source_tree_sha"] == SOURCE_TREE
    assert receipt["framework_authority_commit"] == PINNED_FRAMEWORK
    assert _git("cat-file", "-t", SOURCE_COMMIT) == "commit"
    assert _git("rev-parse", f"{SOURCE_COMMIT}^{{tree}}") == SOURCE_TREE
    assert (
        subprocess.run(
            ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", SOURCE_COMMIT, "HEAD"],
            check=False,
        ).returncode
        == 0
    )

    for binding in receipt["bindings"]:
        assert _git("rev-parse", f"{SOURCE_COMMIT}:{binding['path']}") == (
            binding["git_blob_sha"]
        )
        source_bytes = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"{SOURCE_COMMIT}:{binding['path']}"],
            check=True,
            capture_output=True,
        ).stdout
        assert hashlib.sha256(source_bytes).hexdigest() == binding["content_sha256"]

    assert receipt["chronology"] == {
        "source_artifacts_committed_before_receipt": True,
        "pilot_results_existed_at_source_commit": False,
        "receipt_is_not_bound_to_itself": "non-circular successor commit",
    }
    _assert_frozen_authority(
        receipt["authority_contract"],
        allowed_effect="SOURCE_IDENTITY_ASSURANCE_ONLY",
    )


def test_all_embedded_source_bindings_resolve_at_the_exact_application_commit() -> None:
    documents = [
        _load("EXPERIENCE_EPISODE_PROPOSAL_SUPPORT_EXAMPLE_20260811.json"),
        _load("EXPERIENCE_EPISODE_PROPOSAL_CONTRADICTION_EXAMPLE_20260811.json"),
    ]
    prereg = _load("STUDY_PATTERN_AB_PILOT_PREREGISTRATION_20260811.json")
    bindings = [
        binding for document in documents for binding in document["source_bindings"]
    ] + [case["source_binding"] for case in prereg["cases"]]

    for binding in bindings:
        commit = binding["commit_sha"]
        assert binding["repository_url"] == "https://github.com/SzeChunYiu/RAKL_math.git"
        assert _git("cat-file", "-t", commit) == "commit"
        assert _git("rev-parse", f"{commit}^{{tree}}") == binding["tree_sha"]
        assert _git("rev-parse", f"{commit}:{binding['path']}") == (
            binding["git_blob_sha"]
        )
        source_bytes = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"{commit}:{binding['path']}"],
            check=True,
            capture_output=True,
        ).stdout
        assert hashlib.sha256(source_bytes).hexdigest() == binding["content_sha256"]
