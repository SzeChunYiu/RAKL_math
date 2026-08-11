from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework/RAKL"
BUNDLE = ROOT / "research/real_math/millennium/birch_swinnerton_dyer/10_feedback/BSD_A1a1_APPLICATION_FEEDBACK_BUNDLE_20260811.json"
PRODUCER = "17eb26688dfb13eaaab429bd554d1a29bbf332af"


def _git(*args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(["git", "-C", str(ROOT), *args], check=True, stdout=subprocess.PIPE, text=not binary)
    return result.stdout if binary else result.stdout.strip()


def test_bsd_runtime_hash_lesson_is_exact_proposal_only_feedback() -> None:
    document = json.loads(BUNDLE.read_text(encoding="utf-8"))
    schema = json.loads((FRAMEWORK / "schemas/application-feedback-bundle.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    validator.validate(document)
    subject = copy.deepcopy(document)
    subject.pop("bundle_canonical_sha256")
    observed = hashlib.sha256(json.dumps(subject, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    assert observed == document["bundle_canonical_sha256"]
    assert document["producer"]["commit_sha"] == PRODUCER
    assert document["producer"]["tree_sha"] == _git("rev-parse", f"{PRODUCER}^{{tree}}")
    item = document["items"][0]
    source = item["source"]
    raw = _git("show", f'{PRODUCER}:{source["path"]}', binary=True)
    assert isinstance(raw, bytes)
    assert source["git_blob_sha"] == _git("rev-parse", f'{PRODUCER}:{source["path"]}')
    assert json.loads(raw) == item["payload"]
    payload_hash = hashlib.sha256(json.dumps(item["payload"], sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    assert payload_hash == item["payload_canonical_sha256"]
    assert item["payload"]["validation_status"] == "UNVALIDATED_PROPOSAL"
    assert document["authority_envelope"] == {
        "requested_authority": "HEURISTIC", "proposal_only": True,
        "inventory_mutation_allowed": False, "failure_lattice_mutation_allowed": False,
        "promotion_allowed": False,
    }


def test_bsd_feedback_bundle_runtime_parses_but_cannot_self_promote() -> None:
    source = str(FRAMEWORK / "src")
    if source not in sys.path:
        sys.path.insert(0, source)
    from rakl.application_feedback import parse_application_feedback_bundle
    document = json.loads(BUNDLE.read_text(encoding="utf-8"))
    bundle = parse_application_feedback_bundle(document)
    assert bundle.bundle_canonical_sha256 == document["bundle_canonical_sha256"]
    assert bundle.requested_authority == "HEURISTIC"
    assert bundle.proposal_only is True
    assert bundle.inventory_mutation_allowed is False
    assert bundle.failure_lattice_mutation_allowed is False
    assert bundle.promotion_allowed is False

    schema = json.loads((FRAMEWORK / "schemas/application-feedback-bundle.schema.json").read_text(encoding="utf-8"))
    hostile = copy.deepcopy(document)
    hostile["authority_envelope"]["promotion_allowed"] = True
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.Draft202012Validator(schema).validate(hostile)
