from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
SOURCE = PNP / "00_sources/RAKL_PVSNP_C034_C040_EXTERNAL_LEDGER_20260811.md"
REPLAY = PNP / "05_falsification/c037_external_ledger_replay.py"
REPLAY_RECEIPT = PNP / "05_falsification/C037_EXTERNAL_LEDGER_REPLAY_RECEIPT_20260811.json"
ASSESSMENT = PNP / "08_reviews/C034_C040_EXTERNAL_LEDGER_ASSESSMENT_20260811.json"
SCHEMA = ROOT / "schemas/pnp-c034-c040-external-ledger-assessment.schema.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def test_external_ledger_bytes_are_preserved_with_rendering_defect_visible() -> None:
    raw = SOURCE.read_bytes()
    assert len(raw) == 15_639
    assert raw.count(b"\n") == 549
    assert hashlib.sha256(raw).hexdigest() == "3db396674e15231f7cda79964d20c252ef99f6cd9058f20aa27173376075429d"
    assert raw.count(b"\r") == 5
    assert raw.count(b"\\rho") == 5


def test_c037_replay_is_exact_rational_and_deterministic() -> None:
    spec = importlib.util.spec_from_file_location("c037_replay", REPLAY)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    observed = module.build_receipt()
    assert observed == _load(REPLAY_RECEIPT)
    assert observed["artifact_hash"] == _hash(observed)
    oracle = ROOT / observed["oracle_path"]
    assert observed["oracle_sha256"] == "sha256:" + hashlib.sha256(oracle.read_bytes()).hexdigest()
    assert observed["oracle_git_blob_sha"] == "2a516b166fe2c01e0f478a73aa60e4b8bb48b6b3"
    parent, child = observed["instances"]
    assert (parent["relevant_semifilter_count"], parent["full_union_pair_count"]) == (19, 25)
    assert (child["relevant_semifilter_count"], child["full_union_pair_count"]) == (141, 90)
    assert Fraction(parent["exact_optimum"]) == Fraction(3, 2)
    assert Fraction(child["exact_optimum"]) == 1
    assert Fraction(observed["strict_drop"]) == Fraction(1, 2)
    assert all(item["primal_feasible"] and item["dual_feasible"] for item in observed["instances"])


def test_assessment_schema_authority_and_missing_bundle_fail_closed() -> None:
    assessment = _load(ASSESSMENT)
    schema = _load(SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    validator.validate(assessment)
    assert assessment["artifact_hash"] == _hash(assessment)
    assert assessment["packet_status"] == "QUARANTINED_EXTERNAL_PROPOSAL"
    assert assessment["bundle_completeness"]["present_artifact_count"] == 1
    assert assessment["bundle_completeness"]["missing_artifact_count"] == 26
    assert assessment["authority_contract"] == {
        "grants_proof_authority": False,
        "grants_p_vs_np_root_authority": False,
        "grants_theorem_authority": False,
        "grants_novelty_authority": False,
        "grants_framework_authority": False,
        "grants_review_independence": False,
        "grants_strict_rakl_process_credit": False,
        "may_promote_reported_certificates": False,
    }
    by_id = {item["claim_id"]: item for item in assessment["claim_assessments"]}
    assert by_id["C034A-FULL-UNION-DOMINATION"]["verdict"] == "DESK_CHECK_PASS_PROOF_AUTHORITY_NONE"
    assert by_id["C037-STRICT-DECREASE"]["verdict"] == "INDEPENDENT_FINITE_REPLAY_PASS"
    for claim_id in ["C034B-U8-49/24", "C035-U9-21/10", "C036-U10-62573/29279", "C040-U11-917741/428806"]:
        assert by_id[claim_id]["verdict"] == "CANNOT_CHECK_MISSING_CERTIFICATE_AND_RECEIPT"

    for field in assessment["authority_contract"]:
        hostile = copy.deepcopy(assessment)
        hostile["authority_contract"][field] = True
        with pytest.raises(jsonschema.ValidationError):
            validator.validate(hostile)


def test_displayed_rule_counts_and_rational_increments_recompute() -> None:
    assessment = _load(ASSESSMENT)
    assert assessment["desk_checks"]["rule_counts"] == [
        {"m": m, "all_rules": (4**m - 2 * 3**m + 2**m) // 2,
         "full_union_rules": (3**m - 2 ** (m + 1) + 1) // 2}
        for m in range(8, 12)
    ]
    values = [Fraction(49, 24), Fraction(21, 10), Fraction(62573, 29279), Fraction(917741, 428806)]
    assert assessment["desk_checks"]["reported_increments"] == [str(values[i + 1] - values[i]) for i in range(3)]
