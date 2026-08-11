from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CROSS = ROOT / "research/real_math/millennium/cross_problem"
HODGE = ROOT / "research/real_math/millennium/hodge_conjecture"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def test_hm1a_is_a_real_surface_shifted_cross_problem_tool_retrieval() -> None:
    memory = _load(HODGE / "07_memory/HM1a_RESEARCH_MEMORY_REVIEW_20260811.json")
    failure = _load(HODGE / "07_memory/HM1a_FAILURE_EXPERIENCE_DELTA_20260811.json")
    tool = _load(HODGE / "07_memory/HM1a_RESEARCH_TOOL_DELTA_20260811.json")

    assert memory["tool_query_status"] == "MATCHES_FOUND"
    assert memory["failure_query_status"] == "MATCHES_FOUND"
    assert memory["selected_tool_ids"] == ["T-XM-ROOT-BRIDGE-STABILITY-AUDIT"]
    assert memory["relevant_failure_ids"] == ["F-XM001-POINTWISE-GAP-COLLAPSE"]
    assert any("actual Chow source" in note for note in memory["tool_applicability_notes"])
    assert any("no lattice-spacing limit" in note for note in memory["tool_applicability_notes"])

    experience = failure["experience"]
    assert experience["failure_id"] == "F-HM1a-OPEN-ROOT-LIKE-PIECE"
    assert experience["diagnosis_status"] == "SUPPORTED"
    assert failure["links"][0]["target_id"] == "F-XM001-POINTWISE-GAP-COLLAPSE"
    assert tool["tool"]["tool_id"] == "T-HODGE-SOURCE-BEARING-DECOMPOSITION-SCREEN"
    assert "F-HM1a-OPEN-ROOT-LIKE-PIECE" in tool["tool"]["known_failure_ids"]


def test_xm003_preserves_retrieval_failure_without_promoting_tool_or_root() -> None:
    delta = _load(CROSS / "07_memory/XM003_FAILURE_EXPERIENCE_DELTA_20260811.json")
    experience = delta["experience"]
    copy_for_hash = copy.deepcopy(experience)
    recorded = copy_for_hash["artifact_hash"]
    copy_for_hash["artifact_hash"] = ""

    assert recorded == _canonical_hash(copy_for_hash)
    assert experience["failure_id"] == "F-XM002-CROSS-PROBLEM-RETRIEVAL-MISS"
    assert experience["diagnosis_status"] == "SUPPORTED"
    assert "completeness/counting claims" in experience["selected_diagnosis"]

    audit = (CROSS / "04_candidates/XM003_HODGE_RETRIEVAL_COVERAGE_AUDIT_20260811.md").read_text(
        encoding="utf-8"
    )
    assert "third mathematically disanalogous target transfer" in audit
    assert "Do **not** yet claim mature retrieval reliability" in audit
    assert "RAKL issue #119" in audit
    assert "NO_MATHEMATICAL_THEOREM" in audit
    assert "ROOT_AUTHORITY_NONE" in audit
