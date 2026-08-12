from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from rakl.failure_lattice import reconstruct_failure_lattice
from rakl.schema_reference_constraints import check_reference_constraints


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
DELTA = YM / "07_memory/YM-S1A2_OS_SZZ_GLUING_FAILURE_EXPERIENCE_DELTA_20260812.json"
SCHEMA = ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json"

SOURCE_HASHES = {
    YM / "09_trace/YM-S1A1_POST_CANDIDATE_TRACE_20260811.json":
        "6807a64900905621c358e51fb3c4bef14167c764235893020667d356231e1ecb",
    YM / "02_problem_dag/YM-S1A2.yaml":
        "e4b280878fdcc55b5da37d67ec26c57d17b2830153084c80023e73a748fb87f3",
    YM / "04_candidates/YM-S1A1_C001_V2_DENSE_SOURCE_COMMON_RATE_SPECTRAL_EXCLUSION_20260811.md":
        "7cd5b6cf8070aa792c3793e55f332f139953897180ec792f2f893113df680bf9",
    YM / "03_sources/YM-S1A1_SOURCE_PACKET_20260811.md":
        "424f58f281e8ad4bf028937e2e1c5e209e35abfda86d2850cc3899588773b15b",
    YM / "01_frontier/YM-S1A1_CONTEXT_FIBER_20260811.json":
        "195e9727d7c7b28a8789fffbbcded587921d0074f5fef07ab19ae91e2fbc10dd",
}


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_os_szz_gluing_delta_is_one_full_runtime_conformant_failure_experience() -> None:
    delta = _load(DELTA)
    schema = _load(SCHEMA)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(delta)
    assert check_reference_constraints(delta, schema) == ()

    assert len(delta["experiences"]) == 1
    assert delta["links"] == []
    failure = delta["experiences"][0]
    unhashed = copy.deepcopy(failure)
    unhashed["artifact_hash"] = ""
    assert failure["artifact_hash"] == _canonical_hash(unhashed)

    lattice = reconstruct_failure_lattice(delta)
    assert len(lattice.experiences) == 1
    assert lattice.links == ()
    assert lattice.experiences[0].failure_id == (
        "F-YM-S1A2-OS-SZZ-SAME-THEORY-GLUING-UNBOUND"
    )


def test_failure_is_exactly_bound_to_e011_and_preserves_the_context_required_child() -> None:
    failure = _load(DELTA)["experiences"][0]
    trace = _load(YM / "09_trace/YM-S1A1_POST_CANDIDATE_TRACE_20260811.json")
    event = next(item for item in trace["entries"] if item["event_id"] == "YM-S1A1-E011")

    assert failure["research_trace_event_id"] == event["event_id"]
    assert event["event_type"] == "RESIDUAL_OPENED"
    assert "child_atom:YM-S1a2" in event["outputs"]
    assert "failure_category:GLUING_REPRESENTATION_BINDING" in event["outputs"]
    assert failure["atom_id"] == "YM-S1a2"
    assert failure["context_packet_hash"] == (
        "sha256:082ddb6131aa0316cbdd17248d762af6bc036caed877a2acce42087f1c940e3a"
    )
    assert failure["candidate_id"] == (
        "YM-S1A1-C001-V2-DENSE-SOURCE-COMMON-RATE-SPECTRAL-EXCLUSION"
    )

    child = (YM / "02_problem_dag/YM-S1A2.yaml").read_text(encoding="utf-8")
    assert "status: CONTEXT_REQUIRED" in child
    assert "allowed: false" in child
    assert "root_authority: NONE" in child


def test_diagnosis_separates_observed_interface_failure_from_unproved_cause_and_transfer() -> None:
    failure = _load(DELTA)["experiences"][0]
    assert failure["diagnosis_status"] == "SUPPORTED"
    assert "SUPPORTED_BOUNDED_DIAGNOSIS" in failure["selected_diagnosis"]
    assert "CANNOT_IDENTIFY_UNIQUE_MATHEMATICAL_CAUSE" in failure["selected_diagnosis"]
    assert "not a counterexample" in " ".join(failure["scope_conditions"])
    assert "not a verified impossibility theorem" in " ".join(failure["scope_conditions"])

    repairs = "\n".join(failure["local_repair_attempts"])
    assert "NARROW_SAFE_MATHEMATICAL_TRANSFER_CONDITION" in repairs
    assert "NO_SAFE_MATHEMATICAL_TRANSFER" in repairs
    assert "same strong-coupling infinite-volume theory" in repairs
    assert "density/cyclicity" in repairs
    assert "no G5, G6, G7, continuum, novelty, or Clay-root authority" in repairs


def test_failure_delta_does_not_rewrite_the_frozen_source_artifacts() -> None:
    for path, expected in SOURCE_HASHES.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected

    failure = _load(DELTA)["experiences"][0]
    for pointer in failure["evidence_pointers"]:
        if not pointer.startswith("research/"):
            continue
        relative = pointer.split("#", 1)[0]
        assert (ROOT / relative).is_file()
