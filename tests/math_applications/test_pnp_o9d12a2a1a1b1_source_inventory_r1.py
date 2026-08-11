from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
INVENTORY = PNP / "01_frontier/O9d12a2a1a1b1_SOURCE_NATIVE_THEOREM_INVENTORY_R1_20260811.json"
SCHEMA = ROOT / "schemas/pnp-source-native-theorem-inventory-r1.schema.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _assert_t30_does_not_claim_arbitrary_lambda_equality(inventory: dict) -> None:
    row = next(row for row in inventory["theorem_rows"] if row["row_id"] == "ECCC-T30")
    witness = row["difference_witness"]
    assert witness["match_assessment"] == "MATCH"
    assert "optimal cover" in witness["source_to_target_map"].lower()
    assert witness["implication_direction"] == "D_cyclic_intersection = r <= m"


def test_source_inventory_r1_schema_hash_chronology_and_primary_bytes() -> None:
    inventory = _load(INVENTORY)
    schema = _load(SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    validator.validate(inventory)
    assert inventory["artifact_hash"] == _canonical_hash(inventory)

    pre = inventory["pre_action_binding"]
    pre_path = ROOT / pre["path"]
    raw = pre_path.read_bytes()
    assert pre["raw_sha256"] == "sha256:" + hashlib.sha256(raw).hexdigest()
    pre_value = json.loads(raw)
    canonical_value = dict(pre_value)
    canonical_value.pop("receipt_canonical_sha256")
    canonical_raw = json.dumps(
        canonical_value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    assert pre["canonical_sha256"] == "sha256:" + hashlib.sha256(canonical_raw).hexdigest()
    assert pre_value["allowed_outcome_branches"] == pre["allowed_outcome_branches"]
    assert _timestamp(pre_value["frozen_at_utc"]) < _timestamp(inventory["recorded_at"])

    for source in inventory["source_universe"]:
        if source["local_path"] is None:
            assert source["raw_sha256"] is None
            assert source["size_bytes"] is None
            continue
        source_bytes = (ROOT / source["local_path"]).read_bytes()
        assert source["raw_sha256"] == "sha256:" + hashlib.sha256(source_bytes).hexdigest()
        assert source["size_bytes"] == len(source_bytes)


def test_theorem_rows_are_scope_quantifier_and_non_guarantee_complete() -> None:
    inventory = _load(INVENTORY)
    sources = inventory["source_universe"]
    assert [source["source_id"] for source in sources] == [
        "ECCC-TR25-033-2025",
        "RAZBOROV-1989",
        "KARCHMER-1993",
        "WIGDERSON-1993",
        "NAKAYAMA-MARUOKA-1995",
    ]
    assert [source["content_status"] for source in sources] == [
        "FULL_PRIMARY_CONTENT_INSPECTED",
        "FULL_PRIMARY_CONTENT_INSPECTED",
        "METADATA_ONLY_PRIMARY_CONTENT_UNAVAILABLE",
        "FULL_PRIMARY_CONTENT_INSPECTED",
        "METADATA_ONLY_PRIMARY_CONTENT_UNAVAILABLE",
    ]

    rows = inventory["theorem_rows"]
    by_id = {row["row_id"]: row for row in rows}
    assert len(by_id) == len(rows) == 16
    assert [row["row_id"] for row in rows] == [
        "ECCC-C17",
        "ECCC-D18-D21",
        "ECCC-T22",
        "ECCC-T24-C27-EQ6-EQ8",
        "ECCC-COR28",
        "ECCC-T30",
        "ECCC-COR35",
        "ECCC-P36-T37",
        "ECCC-P38-L39",
        "ECCC-P40-C41-L42-L43",
        "ECCC-D21-WIG95-RESTRICTION",
        "ECCC-D44-D46-T45",
        "ECCC-P47-L48-C49",
        "ECCC-INTRO-NM95-SCOPE",
        "RAZ89-C25-T26-T27",
        "WIG93-META-THEOREM-CONVERSE",
    ]
    t24_dependence = by_id["ECCC-T24-C27-EQ6-EQ8"]["t_dependence"]
    assert "D_intersection(A|B) <= r^2 <= m^2" in t24_dependence
    assert "arbitrary legal witness" in t24_dependence
    assert by_id["ECCC-T30"]["discriminator_status"] == (
        "EXACT_LITERAL_R1_MATCH_ROOT_EQUIVALENT"
    )
    assert by_id["ECCC-P36-T37"]["discriminator_status"] == (
        "TARGET_SPECIFIC_RANDOM_BOUND_ONLY"
    )
    assert by_id["ECCC-D21-WIG95-RESTRICTION"]["shared_cover_fusion_interface"] == (
        "RESTRICTION_MISMATCH_WARNING"
    )
    for row in rows:
        assert row["quantifiers"]
        assert row["assumptions"]
        assert row["restriction_class"]
        assert row["non_guarantees"]
        witness = row["difference_witness"]
        assert witness["source_to_target_map"]
        assert witness["preserved_conditions"]
        assert witness["changed_or_broken_conditions"]
        assert witness["implication_direction"]
        assert witness["match_assessment"] in {"MATCH", "NO_MATCH", "SCOPE_WARNING"}
        assert witness["rationale"]

    assert by_id["ECCC-T24-C27-EQ6-EQ8"]["difference_witness"][
        "match_assessment"
    ] == "MATCH"
    _assert_t30_does_not_claim_arbitrary_lambda_equality(inventory)

    for row_id in ("RAZ89-C25-T26-T27", "WIG93-META-THEOREM-CONVERSE"):
        assert set(by_id[row_id]["difference_witness"]) == {
            "source_to_target_map",
            "preserved_conditions",
            "changed_or_broken_conditions",
            "implication_direction",
            "match_assessment",
            "rationale",
        }

    assert inventory["inventory_coverage"] == {
        "material_rows_recorded": 16,
        "coverage_claim": "MATERIAL_R1_ROWS_REVIEWED_NOT_EXHAUSTIVE_OF_ALL_RESULTS",
        "ancestry_completeness": (
            "INCOMPLETE_CANNOT_CHECK_WHETHER_STRONGER_OR_DIFFERENT_BOUND_EXISTS"
        ),
    }

    row_ids = set(by_id)
    for lesson in inventory["mathematical_experience"]:
        assert set(lesson["evidence_rows"]) <= row_ids


def test_schema_rejects_source_binding_and_theorem_row_inventory_drift() -> None:
    inventory = _load(INVENTORY)
    validator = jsonschema.Draft202012Validator(_load(SCHEMA))

    hostile = copy.deepcopy(inventory)
    hostile["source_universe"][0]["content_status"] = (
        "METADATA_ONLY_PRIMARY_CONTENT_UNAVAILABLE"
    )
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(hostile)

    hostile = copy.deepcopy(inventory)
    hostile["source_universe"][1]["raw_sha256"] = "sha256:" + "0" * 64
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(hostile)

    hostile = copy.deepcopy(inventory)
    hostile["source_universe"][3]["local_path"] = None
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(hostile)

    hostile = copy.deepcopy(inventory)
    hostile["theorem_rows"][1]["row_id"] = "POST_HOC_REPLACEMENT"
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(hostile)

    hostile = copy.deepcopy(inventory)
    hostile["theorem_rows"].append(copy.deepcopy(hostile["theorem_rows"][-1]))
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(hostile)

    hostile = copy.deepcopy(inventory)
    del hostile["theorem_rows"][0]["difference_witness"]
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(hostile)

    hostile = copy.deepcopy(inventory)
    hostile["theorem_rows"][0]["difference_witness"]["match_assessment"] = (
        "POST_HOC_MATCH"
    )
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(hostile)

    hostile = copy.deepcopy(inventory)
    t30 = next(row for row in hostile["theorem_rows"] if row["row_id"] == "ECCC-T30")
    t30["difference_witness"]["implication_direction"] = (
        "D_cyclic_intersection = m for every arbitrary Lambda"
    )
    with pytest.raises(AssertionError):
        _assert_t30_does_not_claim_arbitrary_lambda_equality(hostile)


def test_success_match_preserves_incomplete_ancestry_without_candidate_or_root_authority() -> None:
    inventory = _load(INVENTORY)
    evaluation = inventory["discriminator_evaluation"]
    assert evaluation == {
        "conditions": evaluation["conditions"],
        "modern_source_findings": evaluation["modern_source_findings"],
        "required_primary_sources_fully_inspected": False,
        "blocked_source_ids": [
            "KARCHMER-1993",
            "NAKAYAMA-MARUOKA-1995",
        ],
        "provisional_match_status": (
            "EXACT_MATCH_ON_INSPECTED_PRIMARY_SOURCE_WITH_ANCESTRY_COMPLETENESS_UNRESOLVED"
        ),
        "final_verdict": "MATCH_FOUND_ECCC_T24_AND_T30",
        "outcome_branch": "SUCCESS",
        "candidate_generation_allowed": False,
        "candidate_generated": False,
    }
    assert inventory["root_status"] == "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE"
    assert not any(inventory["authority_contract"].values())
    assert inventory["review_authority"].endswith("NOT_INDEPENDENT_PEER_REVIEW")

    schema = _load(SCHEMA)
    validator = jsonschema.Draft202012Validator(schema)
    for field, value in [
        ("outcome_branch", "BLOCKED"),
        ("final_verdict", "CANNOT_CHECK_REQUIRED_PRIMARY_SOURCE_CONTENT_UNAVAILABLE"),
        (
            "provisional_match_status",
            "CANNOT_PROMOTE_MODERN_SOURCE_PARTIAL_FINDINGS_BECAUSE_R1_COMPLETENESS_IS_BLOCKED",
        ),
        ("candidate_generated", True),
        ("candidate_generation_allowed", True),
        ("required_primary_sources_fully_inspected", True),
    ]:
        hostile = copy.deepcopy(inventory)
        hostile["discriminator_evaluation"][field] = value
        with pytest.raises(jsonschema.ValidationError):
            validator.validate(hostile)
    hostile = copy.deepcopy(inventory)
    hostile["authority_contract"]["grants_p_vs_np_root_authority"] = True
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(hostile)


def test_operational_access_failures_are_not_mathematical_failure_experiences() -> None:
    inventory = _load(INVENTORY)
    excluded = set(inventory["operational_assurance_excluded_from_mathematical_experience"])
    assert excluded == {
        "HTTP access status",
        "Git branch movement",
        "CI execution",
        "artifact hashing",
        "timestamp chronology",
    }
    for lesson in inventory["mathematical_experience"]:
        assert lesson["kind"] in {
            "SCOPED_SUCCESS_KNOWLEDGE",
            "ROUTE_PRUNING",
            "METHOD_TRANSFER_BOUNDARY",
            "TRANSFER_WARNING",
        }
        assert not any(term in lesson["lesson"] for term in excluded)
    assert inventory["scope_gap"]["status"] == (
        "PROSPECTIVE_R2_SCOPE_ADDITION_REQUIRED_NOT_BACKFILLED"
    )


def test_hostile_math_review_and_shadow_trace_bind_exact_result() -> None:
    review_path = PNP / (
        "08_reviews/O9d12a2a1a1b1_SOURCE_INVENTORY_R1_"
        "HOSTILE_MATH_REVIEW_20260811.json"
    )
    trace_path = PNP / (
        "09_trace/O9d12a2a1a1b1_SOURCE_INVENTORY_R1_"
        "RESULT_TRACE_20260811.json.shadow"
    )
    review_schema_path = ROOT / (
        "schemas/pnp-source-inventory-r1-hostile-math-review.schema.json"
    )
    trace_schema_path = ROOT / (
        "schemas/pnp-source-inventory-r1-result-trace-shadow.schema.json"
    )
    inventory = _load(INVENTORY)
    review = _load(review_path)
    trace = _load(trace_path)
    for value, schema_path in [
        (review, review_schema_path),
        (trace, trace_schema_path),
    ]:
        schema = _load(schema_path)
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(value)
        assert value["artifact_hash"] == _canonical_hash(value)

    assert review["reviewed_artifact"] == {
        "path": str(INVENTORY.relative_to(ROOT)),
        "artifact_hash": inventory["artifact_hash"],
    }
    assert review["narrow_verdict"]["outcome_branch"] == "SUCCESS"
    assert not review["narrow_verdict"]["candidate_generated"]
    assert review["review_authority"].endswith("NOT_INDEPENDENT_PEER_REVIEW")
    assert not any(review["authority_contract"].values())

    events = trace["events"]
    assert [event["event_type"] for event in events] == [
        "RESULT_RECORDED",
        "REVIEWED",
        "NEXT_STEP_PROPOSED",
    ]
    assert events[0]["previous_event_hash"] == inventory["pre_action_binding"][
        "canonical_sha256"
    ]
    for index, event in enumerate(events):
        event_payload = copy.deepcopy(event)
        expected = event_payload["event_hash"]
        event_payload["event_hash"] = ""
        raw = json.dumps(
            event_payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        assert expected == "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()
        if index:
            assert event["previous_event_hash"] == events[index - 1]["event_hash"]
    assert trace["storage_authority"] == (
        "SHADOW_NONCANONICAL_NO_TASK_EPISODE_ADMISSION"
    )
    assert not any(trace["authority_contract"].values())
