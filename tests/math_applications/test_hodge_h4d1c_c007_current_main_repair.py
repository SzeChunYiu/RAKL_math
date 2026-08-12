from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/hodge/deformation"
ROUTE = BASE / "03_routes/H4d1c_C007_TANGENT_INTEGRABILITY_REPAIR_20260812.md"
PACKET = BASE / "07_memory/H4d1c_C007_MATHEMATICAL_LESSON_20260812.json"
SOURCE = BASE / "00_sources/H4d1c_C007_ALGEBRAIC_GEOMETRY_SOURCE_RECEIPT_20260812.json"
PREDECESSOR = BASE / "07_memory/H4d1c_C006_CANDIDATE_LESSON_20260812.json"
FRAMEWORK_SHA = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
BASE_SHA = "451d9506d365f06eb314323523ba123edd3ffb32"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_c007_is_one_scoped_mathematical_unit_on_merged_c006() -> None:
    packet = _load(PACKET)
    assert packet["unit_id"] == "MATH-HODGE-C007-SINGULAR-TANGENT-SURJECTIVITY-NONIMPLICATION"
    assert packet["mathematical_unit_count"] == 1
    assert packet["credit_type"] == "EXPLICIT_CONSTRUCTION_OR_COUNTEREXAMPLE"
    assert packet["predecessor"]["status"] == "MERGED_AND_CREDITED"
    assert packet["predecessor"]["unit_id"] == "MATH-HODGE-C006-RAMIFICATION-POINTWISE-DIFFERENTIAL-NONIMPLICATION"
    assert PREDECESSOR.is_file()
    assert packet["framework"]["rakl_main_sha"] == FRAMEWORK_SHA
    assert packet["application"]["base_sha"] == BASE_SHA


def test_c007_cusp_counterexample_and_attached_certificate_are_exact() -> None:
    packet = _load(PACKET)
    result = packet["exact_result_or_failure"]
    assert "V(y^2-x^3)" in result
    assert "T_0 W = T_0 A^2_C" in result
    assert "proper closed subset" in result
    assert packet["attached_sufficient_certificate"]["separate_credit_units"] == 0
    assert packet["attached_sufficient_certificate"]["statement"] == (
        "If pi:W->H is proper, H is irreducible, and pi is smooth at some w in W, then pi(W)=H."
    )


def test_c007_records_exactly_the_seven_math_lesson_fields() -> None:
    lesson = _load(PACKET)["seven_field_math_lesson"]
    assert list(lesson) == [
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "falsifier",
        "mathematical_repair",
        "proof_and_source_evidence",
    ]
    assert "actual Hodge-incidence" in lesson["scope"]
    assert "smooth at w" in lesson["falsifier"]


def test_c007_sources_bind_open_and_closed_image_steps() -> None:
    source = _load(SOURCE)
    roles = {item["role"]: item for item in source["sources"]}
    assert roles["SMOOTH_MORPHISMS_UNIVERSALLY_OPEN"]["tag"] == "056G"
    assert roles["PROPER_MORPHISMS_HAVE_CLOSED_IMAGE"]["tag"] == "01W6"
    assert all(item["authority"] == "PRIMARY_REFERENCE_CONTROL" for item in roles.values())
    route = ROUTE.read_text(encoding="utf-8")
    assert "C006 is merged and credited" in route
    assert "not an actual Hodge-incidence" in route


def test_c007_non_task_containers_do_not_claim_taskepisode_identity() -> None:
    for path in (PACKET, SOURCE):
        value = _load(path)
        assert "episode_id" not in value
        assert "task_id" not in value
        assert "storage_admission" not in value


def test_c007_does_not_create_global_successor_ledger() -> None:
    memory = ROOT / "research/real_math/millennium/cross_problem/07_memory"
    assert not (memory / "GLOBAL_MATH_ONLY_SATURATION_LEDGER_HODGE_C007_SUCCESSOR_20260812.json").exists()
    assert not (memory / "GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_HODGE_C007_SUCCESSOR_20260812.json").exists()
