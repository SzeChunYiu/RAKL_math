from __future__ import annotations

from fractions import Fraction
import hashlib
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import subprocess
import sys

import jsonschema
from rakl.failure_lattice import reconstruct_failure_lattice
from rakl.research_trace import ResearchTraceEventType


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003j_d001_source_result_fixture.py"


def module():
    spec = importlib.util.spec_from_file_location("rh_ana003j_d001_source_result", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_documents_exactly_match_fixture_and_framework_schemas() -> None:
    fixture = module()
    docs = fixture.build_documents(ROOT)
    assert set(docs) == set(fixture.PATHS)
    for name, relative in fixture.PATHS.items():
        assert load(ROOT / relative) == docs[name], name
    for name, schema_name in (
        ("failure", "failure-experience-lattice.schema.json"),
        ("trace", "math-research-trace.schema.json"),
    ):
        schema = load(ROOT / "framework/RAKL/schemas" / schema_name)
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(docs[name])


def test_public_freeze_and_exact_acquired_source_identities_are_bound() -> None:
    fixture = module()
    docs = fixture.build_documents(ROOT)
    freeze = docs["source"]["freeze_binding"]
    assert hashlib.sha256((ROOT / freeze["path"]).read_bytes()).hexdigest() == freeze["raw_sha256"]
    blob = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", f"{freeze['public_merge_sha']}:{freeze['path']}"],
        check=True, stdout=subprocess.PIPE, text=True,
    ).stdout.strip()
    assert blob == freeze["git_blob"]
    parent_source = load(RH / "01_frontier/RH_ANA_003j_SOURCE_METHOD_TRANSFER_PACKET_20260812.json")
    parent_hashes = {row["id"]: row.get("pdf_sha256") for row in parent_source["primary_sources"]}
    exact = {row["source_id"]: row for row in docs["source"]["exact_sources"]}
    assert exact["BELLOTTI-2508.02041v1"]["pdf_sha256"] == parent_hashes["BELLOTTI-2508.02041v1"]
    assert exact["DUNSTER-GIL-SEGURA-1705.01190v1"]["pdf_sha256"] == parent_hashes["DUNSTER-GIL-SEGURA-1705.01190v1"]
    assert exact["BELLOTTI-2508.02041v1"]["ineffectivity_claimed"] is False
    assert exact["BELLOTTI-2508.02041v1"]["global_source_absence_claimed"] is False


def test_exact_laguerre_derivative_coefficient_identity() -> None:
    # Finite exact worlds verify the persisted algebra but do not replace its hand proof.
    for n in range(1, 13):
        p = [Fraction((-1) ** j * comb(n, j + 1), factorial(j)) for j in range(n)]
        derivative_minus_p = []
        for j in range(n):
            derivative = Fraction(j + 1) * p[j + 1] if j + 1 < n else Fraction(0)
            derivative_minus_p.append(derivative - p[j])
        expected = [Fraction((-1) ** (j + 1) * comb(n + 1, j + 2), factorial(j)) for j in range(n)]
        assert derivative_minus_p == expected


def test_precise_branch_preserves_conditional_envelope_and_rejects_explicit_source_modulus() -> None:
    docs = module().build_documents(ROOT)
    source, result = docs["source"], docs["result"]
    assert source["selected_result_branch"] == "QUALITATIVE_OR_INEFFECTIVE_SOURCE_ONLY_NO_EXPLICIT_MODULUS"
    assert "QUALITATIVE/UNEXPOSED" in source["branch_precision"]
    statuses = {row["obligation"]: row["status"] for row in source["source_obligation_results"]}
    assert statuses["Bellotti absolute implied constant and dependency scope"] == "NOT_EXPLICITLY_EXPOSED_BY_ACQUIRED_V1"
    assert statuses["Bellotti sufficiently-large-x threshold and dependency scope"] == "NOT_EXPLICITLY_EXPOSED_BY_ACQUIRED_V1"
    assert statuses["exact coefficient norm for L_(n-1)^(1)"] == "DERIVABLE_AS_FINITE_EXPRESSION_IN_N"
    certificate = result["exact_mathematical_result"]["conditional_boundary_tail_modulus"]
    assert "q_(n,j)=binom(n+1,j+2)/j!" in " ".join(certificate["definitions"])
    assert "Gamma(2j+2,d sqrt(u))" in certificate["conditional_envelope"]["formula"]
    assert certificate["conditional_modulus"]["source_complete_materialization_status"].startswith("NOT_MATERIALIZED")
    assert result["target_identity_firewall"] == {
        "epsilon_sequence_identity": None,
        "cutoff_constant_identity": None,
        "diagonal_comparison_attempted": False,
        "M_n_epsilon_n_le_Y_n_status": "NOT_AUTHORIZED_NOT_EVALUATED",
    }


def test_seven_field_mathematical_lesson_and_failure_lattice_are_scoped() -> None:
    docs = module().build_documents(ROOT)
    lesson = docs["lesson"]
    required = {
        "attempted_mathematical_implication",
        "exact_mathematical_result_or_failure",
        "supported_and_competing_mathematical_causes",
        "scope",
        "mathematical_falsifier",
        "repair_or_next_discriminator",
        "proof_or_source_evidence",
    }
    assert required <= set(lesson)
    assert "no claim that all literature lacks" in lesson["scope"]
    assert "Before revisiting epsilon_n or Y_n" in lesson["repair_or_next_discriminator"]
    lattice = reconstruct_failure_lattice(docs["failure"])
    assert len(lattice.experiences) == 2
    current = next(x for x in lattice.experiences if x.failure_id.startswith("F-RH-ANA003j-D001"))
    assert current.diagnosis_status.value == "SUPPORTED"
    assert "not a theorem of ineffectivity" in current.selected_diagnosis
    assert len(lattice.links) == 1
    assert lattice.links[0].relation.value == "SHARES_BROKEN_ASSUMPTION_WITH"
    assert "causes are not asserted identical" in lattice.links[0].rationale


def test_trace_is_append_only_and_review_is_not_independent() -> None:
    docs = module().build_documents(ROOT)
    parent = load(RH / "09_trace/RH_ANA_003j_PRE_CANDIDATE_TRACE_20260812.json")
    entries = docs["trace"]["entries"]
    assert entries[: len(parent["entries"])] == parent["entries"]
    assert [entry["event_type"] for entry in entries[-5:]] == [
        ResearchTraceEventType.FALSIFIER_RUN.value,
        ResearchTraceEventType.PROOF_CHECKED.value,
        ResearchTraceEventType.RESULT_RECORDED.value,
        ResearchTraceEventType.RESIDUAL_OPENED.value,
        ResearchTraceEventType.REVIEWED.value,
    ]
    for prior, current in zip(entries, entries[1:]):
        assert current["previous_event_hash"] == prior["artifact_hash"]
    fixture = module()
    for entry in entries[-5:]:
        payload = dict(entry)
        declared = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert declared == fixture.canonical_hash(payload)
    review = docs["review"]
    assert review["review_authority"] == "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT"
    assert review["independent_review"] is False
    assert review["blocking_concerns"] == []
    assert docs["dag"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
