from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
V1 = PNP / "01_frontier/O9d12a2a1a1b1_SOURCE_NATIVE_THEOREM_INVENTORY_R1_20260811.json"
V2 = PNP / "01_frontier/O9d12a2a1a1b1_SOURCE_NATIVE_THEOREM_INVENTORY_R1_V2_20260811.json"
REVIEW = PNP / "08_reviews/O9d12a2a1a1b1_SOURCE_INVENTORY_R1_HOSTILE_MATH_REVIEW_20260811.json"
TRACE = PNP / "09_trace/O9d12a2a1a1b1_SOURCE_INVENTORY_R1_RESULT_TRACE_20260811.json.shadow"
CORRECTION = PNP / "08_reviews/O9d12a2a1a1b1_SOURCE_INVENTORY_R1_CHRONOLOGY_CORRECTION_20260811.json"
V2_SCHEMA = ROOT / "schemas/pnp-source-native-theorem-inventory-r1-v2.schema.json"
CORRECTION_SCHEMA = ROOT / "schemas/pnp-source-inventory-r1-chronology-correction.schema.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
    return parsed


def test_v2_preserves_v1_bytes_and_corrects_review_chronology_only() -> None:
    v1, v2, review, trace, correction = map(
        _load, [V1, V2, REVIEW, TRACE, CORRECTION]
    )
    for value, schema_path in [(v2, V2_SCHEMA), (correction, CORRECTION_SCHEMA)]:
        schema = _load(schema_path)
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(value)
        assert value["artifact_hash"] == _hash(value)

    predecessor = v2["predecessor_binding"]
    assert predecessor["raw_sha256"] == "sha256:" + hashlib.sha256(V1.read_bytes()).hexdigest()
    assert predecessor["artifact_hash"] == v1["artifact_hash"]
    assert predecessor["disposition"] == "SUPERSEDED_CHRONOLOGY_DEFECT_RETAINED"
    review_binding = v2["review_binding"]
    assert review_binding["raw_sha256"] == "sha256:" + hashlib.sha256(REVIEW.read_bytes()).hexdigest()
    assert review_binding["artifact_hash"] == review["artifact_hash"]

    assert _time(v1["recorded_at"]) < _time(trace["events"][0]["recorded_at"])
    assert _time(trace["events"][0]["recorded_at"]) < _time(review["recorded_at"])
    assert _time(review["recorded_at"]) < _time(v2["recorded_at"])
    assert v2["chronology_correction"]["mathematical_payload_changed"] is False
    assert v2["chronology_correction"]["outcome_changed"] is False
    assert v2["chronology_correction"]["historical_bytes_rewritten"] is False

    # Aside from version/identity/time/hash and the explicit correction bindings,
    # V2 preserves the exact mathematical payload and narrow authority boundary.
    normalized_v2 = copy.deepcopy(v2)
    for field in ["predecessor_binding", "review_binding", "chronology_correction"]:
        normalized_v2.pop(field)
    normalized_v2["schema_version"] = v1["schema_version"]
    normalized_v2["inventory_id"] = v1["inventory_id"]
    normalized_v2["recorded_at"] = v1["recorded_at"]
    normalized_v2["artifact_hash"] = v1["artifact_hash"]
    assert normalized_v2 == v1
    assert v2["discriminator_evaluation"]["outcome_branch"] == "SUCCESS"
    assert v2["root_status"] == "OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE"
    assert not any(v2["authority_contract"].values())

    assert correction["predecessor"] == predecessor
    assert correction["review_binding"] == review_binding
    assert correction["successor"]["artifact_hash"] == v2["artifact_hash"]
    assert correction["successor"]["raw_sha256"] == "sha256:" + hashlib.sha256(V2.read_bytes()).hexdigest()
    assert correction["historical_trace_binding"]["artifact_hash"] == trace["artifact_hash"]
    assert not any(correction["authority_contract"].values())
