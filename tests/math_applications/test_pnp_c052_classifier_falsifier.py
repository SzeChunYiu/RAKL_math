from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
CLASSIFIER = BASE / "04_candidates/c052_support_phase_classifier.py"
FALSIFIER = BASE / "05_falsification/c052_independent_classifier_falsifier.py"
SEMANTIC_REVIEW = BASE / "08_reviews/c052_v1_semantic_review.py"
HOSTILE = BASE / "05_falsification/O9d12a2a1b_C052_HOSTILE_SUPPORTED_ESCAPE_CELL_20260812.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def complete_cell(*, k: int, a: int, m: int, a_plus: int, m_plus: int) -> dict:
    def raw(aa: int, mm: int) -> int:
        return 6 + 2 * aa + 2 * mm.bit_length() + 3 * mm * (1 + aa)

    parent_raw = raw(a, m)
    current_raw = raw(a_plus, m_plus)
    return {
        "k": k,
        "a": a,
        "b": m.bit_length(),
        "m": m,
        "v_range": [1 << (a - 1), (1 << a) - 1],
        "parent_padding": parent_raw % 2,
        "a_plus": a_plus,
        "b_plus": m_plus.bit_length(),
        "m_plus": m_plus,
        "v_plus_range": [1 << (a_plus - 1), (1 << a_plus) - 1],
        "current_padding": current_raw % 2,
        "literal_index_quantifier": "ALL_LEGAL_1_TO_V",
        "literal_sign_quantifier": "BOTH",
        "unsat_witness_quantifier": "EVERY_V_EVERY_INDEX_BOTH_CLAUSE_ORDERS",
    }


def hostile_cell() -> dict:
    receipt = json.loads(HOSTILE.read_text(encoding="utf-8"))
    cell = receipt["cell"]
    return complete_cell(
        k=cell["k"],
        a=cell["a"],
        m=cell["m"],
        a_plus=cell["a_plus"],
        m_plus=cell["m_plus"],
    )


def test_classifier_reproduces_both_c050_cells_and_c051() -> None:
    classifier = load_module("c052_classifier", CLASSIFIER)
    worlds = [
        complete_cell(k=15, a=1, m=3, a_plus=2, m_plus=2),
        complete_cell(k=15, a=1, m=3, a_plus=4, m_plus=1),
        complete_cell(k=19, a=1, m=4, a_plus=3, m_plus=2),
    ]
    for cell in worlds:
        result = classifier.classify(cell)
        assert result["branch"] == "FORCED_CONFLICT"
        assert result["certificate"]["coordinate_j"] == 3
        assert result["certificate"]["forced_parent_bit"] == 1
        assert result["certificate"]["MAGIC_bit"] == 0
        assert result["certificate"]["all_v_indices_signs_coverage_proof"]["complete"] is True


def test_v1_classifier_raw_escape_is_semantically_insufficient() -> None:
    classifier = load_module("c052_classifier", CLASSIFIER)
    semantic_review = load_module("c052_semantic_review", SEMANTIC_REVIEW)
    result = classifier.classify(hostile_cell())
    assert result["branch"] == "ESCAPE_ADMISSIBLE"
    assert result["certificate"]["universally_forced_unequal_coordinates"] == []
    assert result["certificate"]["not_overlap_disclaimer"] is True
    assert "unsat_preserving_witness_family" not in result["certificate"]
    reviewed = semantic_review.review_escape_claim(hostile_cell(), result)
    assert reviewed["semantic_outcome"] == "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT"
    assert reviewed["classifier_promotion"] == "BLOCKED"
    assert reviewed["native_gate"] == "BLOCKED"
    assert result["non_guarantees"] == [
        "not an intersection witness",
        "not a SAT or UNSAT result",
        "not a theorem or P-versus-NP result",
    ]


def test_classifier_preserves_unresolved_and_cannot_check_branches() -> None:
    classifier = load_module("c052_classifier", CLASSIFIER)
    unresolved = classifier.classify(complete_cell(k=11, a=2, m=1, a_plus=1, m_plus=2))
    assert unresolved["branch"] == "UNRESOLVED"
    assert "literal payload" in unresolved["certificate"]["failed_certificate_obligations"][0]
    malformed = complete_cell(k=15, a=1, m=3, a_plus=2, m_plus=2)
    malformed["parent_padding"] = 1
    cannot = classifier.classify(malformed)
    assert cannot["branch"] == "CANNOT_CHECK"
    assert "parent_padding" in cannot["certificate"]["input_or_support_validation_failure"]


def test_syntactic_variation_without_unsat_preserving_witness_cannot_escape() -> None:
    classifier = load_module("c052_classifier", CLASSIFIER)
    semantic_review = load_module("c052_semantic_review", SEMANTIC_REVIEW)
    cell = hostile_cell()
    cell["unsat_witness_quantifier"] = "ABSENT"
    result = classifier.classify(cell)
    assert result["branch"] == "ESCAPE_ADMISSIBLE"
    reviewed = semantic_review.review_escape_claim(cell, result)
    assert reviewed["semantic_outcome"] == "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT"
    assert "UNSAT-preserving" in reviewed["blocking_reason"]


def test_independent_falsifier_recomputes_all_three_worlds() -> None:
    classifier = load_module("c052_classifier", CLASSIFIER)
    falsifier = load_module("c052_falsifier", FALSIFIER)
    worlds = [
        complete_cell(k=15, a=1, m=3, a_plus=2, m_plus=2),
        complete_cell(k=15, a=1, m=3, a_plus=4, m_plus=1),
        complete_cell(k=19, a=1, m=4, a_plus=3, m_plus=2),
        hostile_cell(),
    ]
    for cell in worlds:
        claimed = classifier.classify(cell)
        audit = falsifier.audit(cell, claimed)
        assert audit["outcome"] == "CLASSIFIER_SURVIVES"
        assert audit["recomputed_support_phase_quantifier_coverage"] is True
        assert audit["classifier_certificate_reused"] is False


def test_falsifier_catches_wrong_hostile_branch_and_has_no_candidate_import() -> None:
    falsifier = load_module("c052_falsifier", FALSIFIER)
    wrong = {"branch": "FORCED_CONFLICT", "certificate": {}}
    audit = falsifier.audit(hostile_cell(), wrong)
    assert audit["outcome"] == "CLASSIFIER_FALSIFIED"
    assert audit["expected_branch"] == "ESCAPE_ADMISSIBLE"
    source = FALSIFIER.read_text(encoding="utf-8")
    assert "c052_support_phase_classifier" not in source
    assert "04_candidates" not in source
    assert "classifier_certificate_reused\": True" not in source
