from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/p_vs_np/09_trace/c052_parametric_residue_preaction_fixture.py"
RECORD = ROOT / "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C052_PARAMETRIC_RESIDUE_PRE_ACTION_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("pnp_c052_preaction", FIXTURE)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def test_c052_preaction_matches_fixture_and_is_result_free() -> None:
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    assert record == module().build()
    assert record["atom_id"] == "O9d12a2a1b-C052"
    assert record["result_firewall"]["candidate_generated"] is False
    assert record["result_firewall"]["new_level_result_accessed"] is False
    assert record["predeclared_next_discriminator"]["allowed_outcomes"] == [
        "SCOPED_PARAMETRIC_OBSTRUCTION_CLASS",
        "EXPLICIT_ESCAPE_RESIDUE_CLASS",
        "MIXED_CLASSIFICATION_WITH_OPEN_BRANCHES",
        "CANNOT_CHECK",
    ]


def test_c052_learns_mathematical_cause_not_software_metadata() -> None:
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    failure = record["failure_learning"]
    assert "suffix-start phase" in failure["supported_cause"]
    assert len(failure["competing_causes"]) == 4
    assert failure["mathematical_falsifier"].startswith("A supported parameter product")
    assert record["credit"] == {
        "mathematical_result_units": 0,
        "same_context_review_independence": 0,
        "software_git_ci_hash_schema_chronology": 0,
    }
    assert record["self_rakl_proposal"]["proposed_change"].startswith("NO_NEW_FRAMEWORK_SURFACE")


def test_c052_every_source_pointer_resolves() -> None:
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    for pointer in record["failure_learning"]["proof_and_source_evidence"]:
        assert (ROOT / pointer).is_file(), pointer
