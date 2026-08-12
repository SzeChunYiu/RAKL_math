from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
import pytest
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_research_trace,
)


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c045_u17_incidence_candidate_freeze_fixture.py"
VERIFIER = PNP / "09_trace/verify_c045_candidate_freeze_packet.py"
EVALUATOR = PNP / "05_falsification/c045_u17_incidence_classification_evaluator.py"

ARTIFACTS = {
    "candidate": PNP
    / "04_candidates/O9d12a2a1b_C045_U17_INCIDENCE_CLASSIFICATION_PLAN_FREEZE_20260812.json",
    "evaluator_manifest": PNP
    / "05_falsification/O9d12a2a1b_C045_U17_INCIDENCE_EVALUATOR_FREEZE_20260812.json",
    "trace": PNP
    / "09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_TRACE_20260812.json",
    "receipt": PNP
    / "09_trace/O9d12a2a1b_C045_CANDIDATE_FREEZE_RECEIPT_20260812.json",
}


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def test_c045_candidate_freeze_matches_fixture_and_exact_source_identity() -> None:
    fixture = _load_module("pnp_c045_candidate_fixture", FIXTURE)
    expected = fixture.build_documents()
    assert set(expected) == set(ARTIFACTS)
    for name, path in ARTIFACTS.items():
        assert path.is_file(), path
        assert _load(path) == expected[name]

    assert fixture.APPLICATION_BASE_SHA == "4653b516349d158279a8792aa503c209ed0cecab"
    assert fixture.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert fixture.DECODER_GIT_BLOB == "fcc4814dd618da96ef9bb8144a4783a0a6e886e1"
    assert fixture.DECODER_RAW_SHA256 == (
        "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"
    )
    assert fixture.SPARSE_GIT_BLOB == "f81c4b20af57528432e1077810528be02450c7c3"
    assert fixture.SPARSE_RAW_SHA256 == (
        "a151014f45b0fd6ac7a0235b01b0f6fd8de8b7b2d1d816dca3e8dd4e6dd32e3b"
    )
    assert fixture.PRE_GATE_CANONICAL_SHA256 == (
        "sha256:bad15fef7e3914dc54a85d6e306dfb553242a3b1ecbe83a8f28a64827634c118"
    )


def test_c045_freezes_one_typed_plan_with_all_five_exclusive_branches() -> None:
    candidate = _load(ARTIFACTS["candidate"])
    assert candidate["candidate_id"] == "C045-U17-INCIDENCE-CLASSIFICATION-PLAN-v1"
    assert candidate["candidate_kind"] == "TYPED_PLAN_ONLY_NO_TARGET_OUTPUT"
    assert candidate["target_extension"] == "U16_TO_U17_IMMEDIATE_SOURCE_EXTENSION"
    assert candidate["registered_branches"] == [
        "NO_NEW_SEMANTIC_CELL",
        "NO_CROSS_COMPONENT_COUPLING",
        "CROSS_COMPONENT_COUPLING_WITNESS",
        "OLD_TYPE_COLLISION_OR_SPLIT",
        "CANNOT_CHECK",
    ]
    assert candidate["branch_precedence"] == [
        "CANNOT_CHECK_ON_IDENTITY_OR_COMPLETENESS_FAILURE",
        "OLD_TYPE_COLLISION_OR_SPLIT",
        "NO_NEW_SEMANTIC_CELL",
        "CROSS_COMPONENT_COUPLING_WITNESS",
        "NO_CROSS_COMPONENT_COUPLING",
    ]
    assert {item["obligation_id"] for item in candidate["analytic_obligations"]} == {
        "C045-A1",
        "C045-A2",
        "C045-A3",
        "C045-A4",
    }
    assert {item["obligation_id"] for item in candidate["exhaustive_obligations"]} == {
        "C045-E1",
        "C045-E2",
        "C045-E3",
        "C045-E4",
        "C045-E5",
        "C045-E6",
        "C045-E7",
    }
    assert len(candidate["falsifiers"]) >= 9
    assert candidate["target_access"] == {
        "decoder_imported_or_executed": False,
        "evaluator_imported_or_executed": False,
        "target_enumerated": False,
        "target_output_accessed": False,
        "outcome_branch_selected": False,
    }
    assert candidate["authority"]["licensed_action_exercised"] == (
        "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"
    )
    assert candidate["authority"]["generic_runtime_candidate_paths_non_authoritative"] is True
    assert candidate["authority"]["grants_cover_or_lower_bound_conclusion"] is False
    assert candidate["authority"]["mathematical_saturation_credit"] is False
    assert candidate["authority"]["mathematical_result_credit"] is False


def test_c045_evaluator_is_exactly_frozen_but_not_imported_or_executed() -> None:
    manifest = _load(ARTIFACTS["evaluator_manifest"])
    evaluator_bytes = EVALUATOR.read_bytes()
    source = evaluator_bytes.decode("utf-8")
    assert manifest["status"] == "FROZEN_FOR_LATER_POST_FREEZE_EXECUTION_NOT_RUN"
    assert manifest["evaluator"]["path"] == EVALUATOR.relative_to(ROOT).as_posix()
    assert manifest["evaluator"]["raw_sha256"] == hashlib.sha256(evaluator_bytes).hexdigest()
    assert manifest["target_access"]["evaluator_imported_or_executed"] is False
    assert manifest["target_access"]["decoder_imported_or_executed"] is False
    assert manifest["later_execution_gate"]["post_freeze_authorization_required"] is True
    assert manifest["later_execution_gate"]["current_task_execution_authorized"] is False
    assert "POST_FREEZE_AUTHORIZATION_REQUIRED" in source
    assert "def classify_certificate(certificate: dict, authorization: dict)" in source
    for forbidden_import in (
        "C041_fx_sat_one_sided",
        "c041_sparse_bridge_repair",
        "c043_first_row_split_gate",
        "c044_retrospective_quotient_multiplexing",
    ):
        assert forbidden_import not in source


def test_c045_candidate_trace_has_only_a_plan_candidate_event_and_no_result() -> None:
    trace = _load(ARTIFACTS["trace"])
    schema = _load(ROOT / "framework/RAKL/schemas/math-research-trace.schema.json")
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(trace)
    assert len(trace["entries"]) == 9
    event = trace["entries"][-1]
    assert event["event_type"] == "CANDIDATE_PROPOSED"
    assert event["previous_event_hash"] == (
        "sha256:83cb11b84072c529c9e617e448dfefaa693f04e6a6bd4ba9f737bc4aae0a3de9"
    )
    assert event["outputs"][:4] == [
        "C045-U17-INCIDENCE-CLASSIFICATION-PLAN-v1",
        "PLAN_ONLY",
        "TARGET_OUTCOME_UNOBSERVED",
        "ZERO_MATHEMATICAL_RESULT_CREDIT",
    ]
    assert event["outputs"][4].startswith("candidate_artifact_hash:sha256:")
    assert event["outputs"][5].startswith("evaluator_manifest_artifact_hash:sha256:")
    assert event["outputs"][6].startswith("evaluator_raw_sha256:")
    artifact_text = json.dumps(trace, sort_keys=True)
    assert "RESULT_RECORDED" not in artifact_text
    assert "FALSIFIER_RUN" not in artifact_text
    runtime_trace = MathResearchTrace(
        trace_id=trace["trace_id"],
        entries=tuple(
            ResearchTraceEntry(
                **{
                    **entry,
                    "event_type": ResearchTraceEventType(entry["event_type"]),
                    "evidence_pointers": tuple(entry.get("evidence_pointers", [])),
                    "alternatives_considered": tuple(entry.get("alternatives_considered", [])),
                    "outputs": tuple(entry.get("outputs", [])),
                    "uncertainties": tuple(entry.get("uncertainties", [])),
                    "residuals": tuple(entry.get("residuals", [])),
                    "next_steps": tuple(entry.get("next_steps", [])),
                }
            )
            for entry in trace["entries"]
        ),
    )
    assert audit_research_trace(runtime_trace).verdict is TraceGateVerdict.PASS


def test_c045_candidate_freeze_receipt_binds_full_content_without_a_cycle() -> None:
    verifier = _load_module("pnp_c045_candidate_verifier", VERIFIER)
    receipt = _load(ARTIFACTS["receipt"])
    integrity = receipt["full_document_integrity"]
    assert set(integrity["json_inputs"]) == {
        "pre_candidate_gate",
        "candidate",
        "evaluator_manifest",
        "trace",
    }
    assert set(integrity["byte_inputs"]) == {
        "evaluator_source",
        "decoder_source",
        "sparse_semantics_source",
    }
    assert "receipt" not in integrity["json_inputs"]
    assert "receipt" not in integrity["byte_inputs"]
    assert receipt["application_authority"] == {
        "generic_runtime_candidate_paths_non_authoritative": True,
        "licensed_actions": ["FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"],
        "candidate_construction_authorized": False,
        "target_evaluator_execution_authorized": False,
        "cover_or_lower_bound_conclusion_authorized": False,
    }
    assert receipt["credit"] == {
        "mathematical_saturation_credit": False,
        "mathematical_result_credit": False,
        "strict_discovery_result_credit": False,
    }
    assert receipt["review_authority"] == (
        "SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW"
    )
    assert verifier.audit_packet(ROOT) == ()
    verifier.verify_packet(ROOT)


@pytest.mark.parametrize(
    ("target_name", "mutation"),
    [
        ("candidate", "registered_branch"),
        ("candidate", "analytic_obligation"),
        ("evaluator_manifest", "later_execution_gate"),
        ("trace", "state_summary"),
        ("pre_candidate_gate", "context_digest"),
        ("evaluator_source", "source_bytes"),
        ("decoder_source", "decoder_bytes"),
        ("sparse_semantics_source", "sparse_bytes"),
    ],
)
def test_c045_candidate_verifier_rejects_stale_hash_substantive_mutations(
    tmp_path: Path, target_name: str, mutation: str
) -> None:
    verifier = _load_module("pnp_c045_candidate_verifier_mutation", VERIFIER)
    receipt = _load(ARTIFACTS["receipt"])
    json_documents = {
        "candidate": _load(ARTIFACTS["candidate"]),
        "evaluator_manifest": _load(ARTIFACTS["evaluator_manifest"]),
        "trace": _load(ARTIFACTS["trace"]),
        "receipt": receipt,
        "pre_candidate_gate": _load(
            PNP / "09_trace/O9d12a2a1b_C045_LATEST_RAKL_GATE_RECEIPT_20260812.json"
        ),
    }
    original_declared_hashes = {
        name: document.get("artifact_hash")
        for name, document in json_documents.items()
    }
    evaluator_bytes = EVALUATOR.read_bytes()
    decoder_bytes = (PNP / "04_candidates/C041_fx_sat_one_sided.py").read_bytes()
    sparse_bytes = (PNP / "05_falsification/c041_sparse_bridge_repair.py").read_bytes()

    if mutation == "registered_branch":
        json_documents["candidate"]["registered_branches"][0] = "HOSTILE_BRANCH"
    elif mutation == "analytic_obligation":
        json_documents["candidate"]["analytic_obligations"][0]["requirement"] += (
            " HOSTILE_MUTATION"
        )
    elif mutation == "later_execution_gate":
        json_documents["evaluator_manifest"]["later_execution_gate"][
            "current_task_execution_authorized"
        ] = True
    elif mutation == "state_summary":
        json_documents["trace"]["entries"][0]["state_summary"] += " HOSTILE_MUTATION"
    elif mutation == "context_digest":
        json_documents["pre_candidate_gate"]["full_document_integrity"]["inputs"][
            "context"
        ]["canonical_sha256"] = "sha256:" + "0" * 64
    elif mutation == "source_bytes":
        evaluator_bytes += b"\n# HOSTILE_SOURCE_MUTATION\n"
    elif mutation == "decoder_bytes":
        decoder_bytes += b"\n# HOSTILE_DECODER_IDENTITY_MUTATION\n"
    elif mutation == "sparse_bytes":
        sparse_bytes += b"\n# HOSTILE_SPARSE_IDENTITY_MUTATION\n"
    else:  # pragma: no cover
        raise AssertionError(mutation)

    for name, declared in original_declared_hashes.items():
        assert json_documents[name].get("artifact_hash") == declared

    path_map = {
        "candidate": ARTIFACTS["candidate"],
        "evaluator_manifest": ARTIFACTS["evaluator_manifest"],
        "trace": ARTIFACTS["trace"],
        "receipt": ARTIFACTS["receipt"],
        "pre_candidate_gate": PNP
        / "09_trace/O9d12a2a1b_C045_LATEST_RAKL_GATE_RECEIPT_20260812.json",
    }
    for name, source_path in path_map.items():
        target = tmp_path / source_path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(json_documents[name], indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    byte_sources = {
        EVALUATOR: evaluator_bytes,
        PNP / "04_candidates/C041_fx_sat_one_sided.py": decoder_bytes,
        PNP / "05_falsification/c041_sparse_bridge_repair.py": sparse_bytes,
    }
    for source_path, content in byte_sources.items():
        target = tmp_path / source_path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)

    with pytest.raises(verifier.PacketIntegrityError, match=target_name):
        verifier.verify_packet(tmp_path)
