from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from rakl.research_tool_inventory import (
    ResearchTool,
    ResearchToolAuthority,
    ToolApplicabilityVerdict,
    ToolApplicabilityWitness,
    assess_tool_applicability,
    validate_research_tool,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/cross_problem"
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _tool_from_raw(raw: dict) -> ResearchTool:
    return ResearchTool(
        tool_id=raw["tool_id"],
        name=raw["name"],
        kind=raw["kind"],
        abstraction=raw["abstraction"],
        source_atom_id=raw["source_atom_id"],
        source_candidate_id=raw["source_candidate_id"],
        source_result_ids=tuple(raw["source_result_ids"]),
        source_context_hash=raw["source_context_hash"],
        authority=ResearchToolAuthority(raw["authority"]),
        preconditions=tuple(raw["preconditions"]),
        structural_signature=tuple(raw["structural_signature"]),
        operation=raw["operation"],
        guaranteed_effects=tuple(raw["guaranteed_effects"]),
        non_guarantees=tuple(raw["non_guarantees"]),
        validation_obligations=tuple(raw["validation_obligations"]),
        evidence_pointers=tuple(raw["evidence_pointers"]),
        known_failure_ids=tuple(raw.get("known_failure_ids", [])),
        successful_reuse_ids=tuple(raw.get("successful_reuse_ids", [])),
        proof_backing=tuple(raw.get("proof_backing", [])),
        artifact_hash=raw["artifact_hash"],
    )


def test_xm002_promoted_tool_is_content_bound_and_narrow() -> None:
    raw = _load(BASE / "07_memory/XM002_TOOL_INVENTORY_PROMOTION_20260811.json")[
        "tools"
    ][0]
    payload = copy.deepcopy(raw)
    artifact_hash = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert artifact_hash == _canonical_hash(payload)

    tool = _tool_from_raw(raw)
    assert validate_research_tool(tool) == ()
    assert tool.authority is ResearchToolAuthority.CONDITIONALLY_REUSABLE
    assert tool.successful_reuse_ids == ("BSD-A1a1-XM001-ROOT-BRIDGE-REUSE",)
    assert not tool.proof_backing
    assert "does not identify a universal common mathematical obstruction across Millennium problems" in tool.non_guarantees


def test_xm002_bsd_reuse_still_requires_target_validation() -> None:
    raw = _load(BASE / "07_memory/XM002_TOOL_INVENTORY_PROMOTION_20260811.json")[
        "tools"
    ][0]
    tool = _tool_from_raw(raw)
    memory = _load(BSD / "07_memory/BSD_A1a1_RESEARCH_MEMORY_REVIEW_20260811.json")

    assert tool.tool_id in memory["selected_tool_ids"]
    assert "F-XM001-POINTWISE-GAP-COLLAPSE" in memory["relevant_failure_ids"]
    assert any("DifferenceWitness" in note for note in memory["tool_applicability_notes"])

    witness = ToolApplicabilityWitness(
        target_atom_id=memory["target_atom_id"],
        target_context_hash=memory["target_context_hash"],
        tool_id=tool.tool_id,
        matched_preconditions=tool.preconditions,
        unmatched_preconditions=(),
        shared_structural_coordinates=(
            "valid local/surrogate coordinate precedes a distinct root-critical coordinate",
            "an explicit preservation implication is required across the bridge",
        ),
        changed_structural_coordinates=(
            "Yang-Mills cutoff/physical normalization -> BSD complex-s/anticyclotomic-T directional order",
        ),
        known_failure_ids_reviewed=("F-XM001-POINTWISE-GAP-COLLAPSE",),
        target_validation_plan=(
            "inspect the Castella-Hsieh interpolation/order implication boundary",
            "separate exact complex-s order from exact anticyclotomic-T order",
            "split the DAG at the earliest missing noncircular preservation arrow",
        ),
        evidence_pointers=(
            "research/real_math/millennium/birch_swinnerton_dyer/01_frontier/BSD_A1a_COMPLEX_TO_KATO_IMPLICATION_GRAPH_20260811.md",
        ),
    )
    assessment = assess_tool_applicability(tool, witness)
    assert assessment.verdict is ToolApplicabilityVerdict.APPLICABLE_WITH_VALIDATION

    implication_graph = (
        BSD / "01_frontier/BSD_A1a_COMPLEX_TO_KATO_IMPLICATION_GRAPH_20260811.md"
    ).read_text(encoding="utf-8")
    assert "BSD-A1a1-THETA-ORDER-COMPARISON" in implication_graph
    assert "BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE" in implication_graph
    assert "does not determine theta order from complex analytic rank" in implication_graph


def test_xm002_reuse_trace_is_hash_chained() -> None:
    trace = _load(BASE / "09_trace/XM002_REUSE_TRACE_20260811.json")
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = copy.deepcopy(entry)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        previous = artifact_hash

    assert [entry["event_type"] for entry in trace["entries"]] == [
        "REVIEWED",
        "PROMOTED",
    ]
    assert trace["entries"][-1]["outputs"][0] == (
        "T-XM-ROOT-BRIDGE-STABILITY-AUDIT authority=CONDITIONALLY_REUSABLE"
    )
