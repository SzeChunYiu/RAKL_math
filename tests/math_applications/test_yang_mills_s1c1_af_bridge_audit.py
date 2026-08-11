from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"
SHADOW = ROOT / "research" / "real_math" / "millennium" / "cross_problem" / "10_study_pattern"
EPISODE = YM / "07_memory" / "YM_S1C1_EXPERIENCE_EPISODE_PROPOSAL_20260811.json"
CONTEXT = YM / "01_frontier" / "YM_S1C1_RETROSPECTIVE_CONTEXT_FIBRE_20260811.json"
SOURCE = YM / "03_sources" / "YM_S1C1_FAIZAL_SHABIR_AF_ENTRY_AUDIT_20260811.md"
FAILURE = YM / "07_memory" / "YM_S1C1_FAILURE_EXPERIENCE_DELTA_20260811.json"
SATURATION = YM / "07_memory" / "YM_S1C1_SATURATION_VECTOR_20260811.json"
CASE_STUDY = YM / "08_reviews" / "RAKL_METHOD_CASE_STUDY_YM_S1C1_20260811.md"
CHILD = YM / "02_problem_dag" / "YM_S1C1a_delta.yaml"


def _canonical_hash(value: dict) -> str:
    unhashed = copy.deepcopy(value)
    unhashed["artifact_hash"] = ""
    raw = json.dumps(
        unhashed,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _git_bytes(*args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=True,
        capture_output=True,
    ).stdout


def _git_text(*args: str) -> str:
    return _git_bytes(*args).decode("utf-8").strip()


def test_ym_s1c1_uses_canonical_proposal_only_v3_shadow_schema() -> None:
    schema = json.loads((SHADOW / "EXPERIENCE_EPISODE_PROPOSAL.schema.json").read_text())
    episode = json.loads(EPISODE.read_text())
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(episode)

    assert episode["artifact_hash"] == _canonical_hash(episode)
    assert episode["status"] == "PROPOSAL_ONLY"
    assert episode["source_role"] == "CONTRADICTION"
    assert episode["reported_outcome"] == "PARTIAL_SUCCESS"
    assert episode["residual_signature"]
    contract = episode["authority_contract"]
    assert contract["effective_authority"] == "PROPOSAL_ONLY"
    assert contract["allowed_effect"] == "SEARCH_PRIORITY_ONLY"
    for field in (
        "grants_tool_authority",
        "grants_proof_authority",
        "grants_gluing_authority",
        "grants_theorem_authority",
        "grants_framework_authority",
        "grants_review_independence",
    ):
        assert contract[field] is False


def test_ym_s1c1_context_fibre_is_self_hashed_and_bound_to_episode() -> None:
    context = json.loads(CONTEXT.read_text())
    episode = json.loads(EPISODE.read_text())

    assert context["artifact_hash"] == _canonical_hash(context)
    assert episode["context_hash"] == context["artifact_hash"]
    assert context["chronology"] == "RETROSPECTIVE"
    assert context["authority"] == "PROPOSAL_ONLY"
    assert context["fibre"]["operators_selected"] == [
        "PRIMARY_SOURCE_COLLISION_AUDIT",
        "ROOT_BRIDGE_STABILITY_AUDIT",
        "CONTRASTIVE_DISCRIMINATION",
        "GLUING_INTERFACE_AUDIT",
    ]
    assert context["fibre"]["retrieved_but_rejected"]
    assert "bare_coupling_coordinate" in context["fibre"]["interface_keys"]


def test_ym_s1c1_episode_source_bindings_are_exact_git_and_content_bindings() -> None:
    episode = json.loads(EPISODE.read_text())
    for binding in episode["source_bindings"]:
        commit = binding["commit_sha"]
        path = binding["path"]
        assert _git_text("rev-parse", f"{commit}^{{tree}}") == binding["tree_sha"]
        assert _git_text("rev-parse", f"{commit}:{path}") == binding["git_blob_sha"]
        source_bytes = _git_bytes("show", f"{commit}:{path}")
        assert hashlib.sha256(source_bytes).hexdigest() == binding["content_sha256"]


def test_ym_s1c1_failure_gluing_and_saturation_scope_remain_fail_closed() -> None:
    failure = json.loads(FAILURE.read_text())
    saturation = json.loads(SATURATION.read_text())
    source = SOURCE.read_text()
    child = CHILD.read_text()

    assert failure["failure_id"] == "F-YM-S1C1-FIXED-REFERENCE-BARE-COUPLING-ESCAPE"
    assert failure["diagnosis_status"] == "OBSERVED_ONLY"
    assert failure["selected_diagnosis"] == ""
    assert "does not claim nonexistence" in " ".join(failure["scope_conditions"])

    assert set(saturation["axes"]) == {
        "KNOWLEDGE",
        "OPERATOR",
        "EXPERIENCE_PATTERN",
        "OBSTRUCTION",
        "RELATION",
        "PATH",
        "META_METHOD",
    }
    assert saturation["absolute_completeness"] is False

    assert "beta_K -> beta_* < infinity" in source
    assert "FIXED_REFERENCE_ENTRY_DOES_NOT_ESTABLISH_BARE_COUPLING_ESCAPE" in source
    assert "does **not** show that no asymptotically-free trajectory exists" in source
    assert "fixed-domain RG control -> genuine Wilson bare trajectory" in source

    assert "candidate_generation_gate:" in child
    assert "allowed: false" in child
    assert "ROOT_AUTHORITY_NONE" in child


def test_ym_s1c1_method_case_study_records_math_and_v3_process_failures() -> None:
    case_study = CASE_STUDY.read_text()
    assert "FRESH_SOURCE_COLLISION_GATE" in case_study
    assert "V3_ADOPTION_HANDSHAKE" in case_study
    assert "bridge/gluing failure" in case_study
    assert "application-local ad-hoc shadow record" in case_study
    assert "does **not** mint a lesson proposal" in case_study
