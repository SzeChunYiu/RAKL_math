from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import jsonschema
import pytest
from rakl.math_context import ContextGateVerdict
from rakl.research_memory import ResearchMemoryVerdict
from rakl.research_trace import ResearchTraceEventType, TraceGateVerdict
from rakl.root_coordinate_preservation import PreservationGateVerdict
from rakl.semantic_shortcut import ShortcutMode, ShortcutReviewVerdict


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c045_u17_component_coupling_pre_candidate_fixture.py"
VERIFIER = PNP / "09_trace/verify_c045_pre_candidate_packet.py"

ARTIFACTS = {
    "atomization": PNP / "02_problem_dag/O9d12a2a1b_C045_ATOMIZATION_20260812.json",
    "context": PNP / "01_frontier/O9d12a2a1b_C045_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": PNP / "07_memory/O9d12a2a1b_C045_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": PNP / "07_memory/O9d12a2a1b_C045_FAILURE_SNAPSHOT_20260812.json",
    "memory": PNP / "07_memory/O9d12a2a1b_C045_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": PNP / "07_memory/O9d12a2a1b_C045_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": PNP / "08_reviews/O9d12a2a1b_C045_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": PNP / "08_reviews/O9d12a2a1b_C045_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": PNP / "09_trace/O9d12a2a1b_C045_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C045_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": PNP / "09_trace/O9d12a2a1b_C045_LATEST_RAKL_GATE_RECEIPT_20260812.json",
}


def _load_fixture():
    spec = importlib.util.spec_from_file_location("pnp_c045_pre_candidate_fixture", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load_verifier():
    spec = importlib.util.spec_from_file_location("pnp_c045_packet_verifier", VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from _walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_keys(child)


def test_c045_all_current_v3_pre_candidate_gates_pass_without_candidate() -> None:
    module = _load_fixture()
    plan, fiber, memory, transformation_memory, shortcut, trace, preservation = (
        module.build_current_gate_plan()
    )
    assert module.FRAMEWORK_SHA == "43897d3afaf0038385102d5acc64793c05ec40f0"
    assert module.APPLICATION_BASE_SHA == "e5f50a1dc5c20bee7cfc3c3d6edf980d5cc72e1c"
    assert module.C044_MERGE_COMMIT == "122ade1bbf5e396b30d28e49a20bb3b02adf4ca9"
    assert module.C044_CONTENT_COMMIT == "49b0d13bbefbc469c5f171a90434b299c5e1c5a7"
    assert module.C044_RESULT_BLOB == "a0e71d36ff2e07d79c5e55caf171792a491f1c56"
    assert module.C044_RECEIPT_BLOB == "2c164c794723fe39a49da4b110fccc4eaf427198"
    assert module.C044_FAILURE_BLOB == "e805d3f9a3e0625a4dab632b34ba359902ca9f0c"
    assert module.C044_TOOL_BLOB == "70f51a496fc1b6c325cec20d648838088ab97873"
    assert module.C044_PROOF_REVIEW_BLOB == "b2324a92a48663d5d922807bbf199c2e989232ea"
    assert module.C044_LOWER_REVIEW_BLOB == "e97fc8a5febe4474e23a9213af283c8f44243e5e"
    assert module.C044_TRACE_BLOB == "ae0a5119404a49afe84ea8c8729b898ef4d12f49"
    assert module.C044_FEEDBACK_BLOB == "9206662bdb1565569dcbd7b7ba3871bce592966a"
    assert module.C043_FAILURE_BLOB == "c9e47beb4059028d64f199249dfbbed663d9b668"
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.shortcut_gate.verdict is ShortcutReviewVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.preservation_gate.verdict is PreservationGateVerdict.SEARCH_LICENSED
    assert plan.candidate_generation_allowed is True
    assert plan.pre_candidate_actions == ()
    assert shortcut.selected_mode is ShortcutMode.SEARCH
    assert shortcut.selected_episode_ids == ("E-PNP-C044-EXACT-COMPONENT-COUPLING-GATE",)
    assert transformation_memory.snapshot_hash
    assert memory.selected_tool_ids == ("T-PNP-EXACT-NEIGHBORHOOD-TYPE-UPPER-BOUND",)
    assert fiber.first_candidate_at is None
    assert preservation.root_claim_id == module.ATOM
    assert [entry.event_type for entry in trace.entries] == [
        ResearchTraceEventType.ATOMIZED,
        ResearchTraceEventType.CONTEXT_FROZEN,
        ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW,
        ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW,
        ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    ]


def test_c045_artifacts_are_schema_valid_and_match_runtime_fixture() -> None:
    module = _load_fixture()
    expected = module.build_documents()
    assert set(expected) == set(ARTIFACTS)
    for name, path in ARTIFACTS.items():
        assert path.is_file(), path
        assert _load(path) == expected[name]

    schema_names = {
        "context": "math-context-fiber.schema.json",
        "memory": "research-memory-review.schema.json",
        "transformation_memory": "obstruction-transformation-memory.schema.json",
        "shortcut_review": "obstruction-transformation-review.schema.json",
        "preservation": "root-coordinate-preservation-receipt-v1.schema.json",
        "trace": "math-research-trace.schema.json",
    }
    for name, schema_name in schema_names.items():
        schema = _load(ROOT / "framework/RAKL/schemas" / schema_name)
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(expected[name])


def test_c045_packet_is_result_blind_and_has_no_target_capability() -> None:
    module = _load_fixture()
    documents = module.build_documents()
    forbidden_keys = {
        "result",
        "observed_result",
        "target_outcome",
        "quotient_complement",
        "explicit_pairs",
        "target_cells",
        "witness_cells",
        "target_count",
        "cover_number",
    }
    assert not (forbidden_keys & set(_walk_keys(documents)))

    artifact_text = "\n".join(
        json.dumps(document, sort_keys=True) for document in documents.values()
    )
    assert "TARGET_OUTCOME_UNOBSERVED" in artifact_text
    assert "CANDIDATE_PROPOSED" not in artifact_text
    assert "rho(G17)=" not in artifact_text
    assert "rho(G_17)=" not in artifact_text

    capability_free_source_text = "\n".join(
        path.read_text(encoding="utf-8") for path in (FIXTURE, VERIFIER)
    )
    for forbidden in (
        "C041_fx_sat_one_sided",
        "decode_formula",
        "is_satisfiable",
        "canonical_cover_oracle",
        "full_cover_oracle",
        "c043_first_row_split_gate",
        "c044_retrospective_quotient_multiplexing",
        "subprocess",
    ):
        assert forbidden not in capability_free_source_text


def test_c045_freezes_branch_complete_incidence_gate_without_an_outcome() -> None:
    atomization = _load(ARTIFACTS["atomization"])
    assert atomization["target_extension"] == "U16_TO_U17_IMMEDIATE_SOURCE_EXTENSION"
    assert atomization["qoi"] == "EXACT_FULL_HISTORY_QUOTIENT_COMPONENT_INCIDENCE"
    assert atomization["allowed_result_branches"] == [
        "NO_NEW_SEMANTIC_CELL",
        "NO_CROSS_COMPONENT_COUPLING",
        "CROSS_COMPONENT_COUPLING_WITNESS",
        "OLD_TYPE_COLLISION_OR_SPLIT",
        "CANNOT_CHECK",
    ]
    assert atomization["candidate_generation_allowed"] is False
    assert atomization["target_output_accessed"] is False

    gate = _load(ARTIFACTS["gate"])
    assert gate["gate_verdicts"]["candidate_generation_allowed"] is True
    assert gate["gate_verdicts"]["licensed_action"] == (
        "FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"
    )
    assert gate["chronology"]["candidate_identity"] is None
    assert gate["chronology"]["candidate_proposed"] is False
    assert gate["chronology"]["target_output_accessed"] is False
    assert gate["authority"]["grants_mathematical_result"] is False
    assert gate["authority"]["grants_p_vs_np_authority"] is False


def test_c045_is_a_zero_credit_pre_candidate_context_refresh() -> None:
    module = _load_fixture()
    documents = module.build_documents()
    atomization = documents["atomization"]
    gate = documents["gate"]

    assert atomization["refresh"]["kind"] == "PRE_CANDIDATE_CONTEXT_REFRESH"
    assert atomization["refresh"]["previous_packet_commit"] == (
        "7238973d18e67356bd5e7cbf2d6214da32f0e81e"
    )
    assert atomization["refresh"]["mathematical_saturation_credit"] is False
    assert atomization["refresh"]["mathematical_result_credit"] is False
    assert atomization["refresh"]["target_output_accessed"] is False

    assert gate["application_base_commit"] == module.APPLICATION_BASE_SHA
    assert gate["refresh"]["kind"] == "PRE_CANDIDATE_CONTEXT_REFRESH"
    assert gate["refresh"]["mathematical_saturation_credit"] is False
    assert gate["refresh"]["mathematical_result_credit"] is False
    assert gate["refresh"]["strict_discovery_result_credit"] is False
    assert gate["refresh"]["candidate_identity"] is None
    assert gate["refresh"]["target_output_accessed"] is False
    assert gate["authority"]["mathematical_saturation_credit"] is False
    assert gate["authority"]["mathematical_result_credit"] is False

    c044 = gate["source_authority_bindings"]["c044"]
    assert c044["merge_commit"] == module.C044_MERGE_COMMIT
    assert c044["content_commit"] == module.C044_CONTENT_COMMIT
    assert c044["included_in_application_base"] == module.APPLICATION_BASE_SHA
    assert {binding["blob"] for binding in c044["files"]} == {
        module.C044_RESULT_BLOB,
        module.C044_RECEIPT_BLOB,
        module.C044_FAILURE_BLOB,
        module.C044_TOOL_BLOB,
        module.C044_PROOF_REVIEW_BLOB,
        module.C044_LOWER_REVIEW_BLOB,
        module.C044_TRACE_BLOB,
        module.C044_FEEDBACK_BLOB,
    }
    files = {binding["role"]: binding for binding in c044["files"]}
    assert files["retrospective_upper_result"] == {
        "role": "retrospective_upper_result",
        "path": module.C044_RESULT_PATH,
        "blob": module.C044_RESULT_BLOB,
    }
    assert files["canonical_support_receipt"]["path"] == module.C044_RECEIPT_PATH
    assert files["canonical_support_receipt"]["declared_artifact_hash"] == (
        "sha256:0f726e5d6c59a26d66d68b239c17ac672e4bfb2dc7acf86c0e5d41ab698097c0"
    )
    assert files["failure_experience"]["path"] == module.C044_FAILURE_PATH
    assert files["failure_experience"]["declared_artifact_hash"] == (
        "sha256:3dee514ab96532e869c7f3fb402844f7640667751682c86e0b338d9e1bf4c353"
    )
    assert files["proposal_only_tool"]["path"] == module.C044_TOOL_PATH
    assert files["proposal_only_tool"]["declared_artifact_hash"] == (
        "sha256:94ea03890853a5cd19747e1be95c03dae009449d64a8a8854d805e9cda68367e"
    )
    assert files["upper_proof_hostile_review"]["path"] == module.C044_PROOF_REVIEW_PATH
    assert files["lower_authority_review"]["path"] == module.C044_LOWER_REVIEW_PATH
    assert files["retrospective_trace"]["path"] == module.C044_TRACE_PATH
    assert files["component_coupling_feedback"]["path"] == module.C044_FEEDBACK_PATH


def test_c045_full_document_integrity_verifier_accepts_committed_packet() -> None:
    verifier = _load_verifier()
    gate = _load(ARTIFACTS["gate"])
    integrity = gate["full_document_integrity"]

    assert integrity["algorithm"] == "SHA-256"
    assert integrity["canonicalization"] == "JSON_SORT_KEYS_COMPACT_UTF8"
    assert set(integrity["inputs"]) == set(ARTIFACTS) - {"gate"}
    assert "gate" not in integrity["inputs"]
    assert gate["application_authority"] == {
        "generic_runtime_candidate_paths_non_authoritative": True,
        "licensed_actions": ["FREEZE_INCIDENCE_CLASSIFICATION_PLAN_ONLY"],
        "candidate_construction_authorized": False,
        "target_evaluator_execution_authorized": False,
    }
    assert verifier.audit_packet(ROOT) == ()
    verifier.verify_packet(ROOT)


@pytest.mark.parametrize(
    ("document_name", "mutation", "declared_hash_path"),
    [
        ("context", "object_context", ("packet_hash",)),
        ("memory", "applicability_note", ("artifact_hash",)),
        ("shortcut_review", "mapping_disanalogy", ("artifact_hash",)),
        ("trace", "state_summary", ("entries", 0, "artifact_hash")),
        ("transformation_memory", "nested_episode", ("episodes", 0, "artifact_hash")),
        ("shortcut_review", "nested_mapping", ("direct_mapping_witnesses", 0, "artifact_hash")),
    ],
)
def test_c045_full_document_integrity_rejects_substantive_hash_preserving_mutations(
    tmp_path: Path,
    document_name: str,
    mutation: str,
    declared_hash_path: tuple[str | int, ...],
) -> None:
    verifier = _load_verifier()
    documents = {name: _load(path) for name, path in ARTIFACTS.items()}
    document = documents[document_name]

    def nested(value, path):
        for part in path:
            value = value[part]
        return value

    declared_before = nested(document, declared_hash_path)
    if mutation == "object_context":
        document["object_context"] += " HOSTILE_UNBOUND_CONTEXT_MUTATION"
    elif mutation == "applicability_note":
        document["tool_applicability_notes"][0] += " HOSTILE_UNBOUND_APPLICABILITY_MUTATION"
    elif mutation == "mapping_disanalogy":
        document["direct_mapping_witnesses"][0]["disanalogies"][0] += (
            " HOSTILE_UNBOUND_DISANALOGY_MUTATION"
        )
    elif mutation == "state_summary":
        document["entries"][0]["state_summary"] += " HOSTILE_UNBOUND_TRACE_MUTATION"
    elif mutation == "nested_episode":
        document["episodes"][0]["operation"] += " HOSTILE_UNBOUND_EPISODE_MUTATION"
    elif mutation == "nested_mapping":
        document["direct_mapping_witnesses"][0]["precondition_mapping"][0][1] += (
            " HOSTILE_UNBOUND_MAPPING_MUTATION"
        )
    else:  # pragma: no cover - parameter list is closed above
        raise AssertionError(mutation)
    assert nested(document, declared_hash_path) == declared_before

    for name, source_path in ARTIFACTS.items():
        target = tmp_path / source_path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(documents[name], indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    with pytest.raises(verifier.PacketIntegrityError, match=document_name):
        verifier.verify_packet(tmp_path)
