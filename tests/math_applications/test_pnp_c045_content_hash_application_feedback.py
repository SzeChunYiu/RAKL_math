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
FEEDBACK = ROOT / "research/real_math/millennium/p_vs_np/10_feedback"
BUNDLE = FEEDBACK / "C045_TYPED_CONTENT_HASH_APPLICATION_FEEDBACK_BUNDLE_20260812.json"

OBSERVED_PRODUCER = "4c33934030f98ba81a77b419d2317a1b31173fdc"
OBSERVED_TREE = "d7104d18f0f34317b358dedadd72a101d4359bdf"
FRAMEWORK_COMMIT = "43897d3afaf0038385102d5acc64793c05ec40f0"
FRAMEWORK_VERSION = "0.1.0"
REPOSITORY_URL = "https://github.com/SzeChunYiu/RAKL_math.git"

EXPECTED_EVIDENCE = {
    "tests/math_applications/test_pnp_c045_u17_component_coupling_gate.py": (
        "509166aff36d1a3405bce999fd1ac74841ed5394",
        "094f4aa36c1a7da18264fabe89fc35ce375d19a644ae68acf30f9fbb3cb8ef20",
    ),
    "research/real_math/millennium/p_vs_np/09_trace/verify_c045_pre_candidate_packet.py": (
        "a3bcb6de281b6e2095aaf945d8f03f711a460181",
        "8ba86835ed71d9ba48d4a7d0fff4b770baa689db70042437f7205366760e79ee",
    ),
    "research/real_math/millennium/p_vs_np/09_trace/c045_u17_component_coupling_pre_candidate_fixture.py": (
        "692cff249bea0de115ad109bf836994966023129",
        "d202550785405078e56a27dd6d1a3dc1859810f45cd8111090d130f639aacc47",
    ),
    "research/real_math/millennium/p_vs_np/01_frontier/O9d12a2a1b_C045_MATH_CONTEXT_FIBER_20260812.json": (
        "c169d750a5e962f5109a57b6138ebfa906c7b557",
        "258510be7eb0fbfcc63a8e4b45129cae811de580ba8cfcd2664cdc396c4b0830",
    ),
    "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C045_PRE_CANDIDATE_TRACE_20260812.json": (
        "832ea87152ebeda8702f8001739ba926e698211e",
        "06801151ba6b71b3356f5ed374936abbb8fedb3321c3ababb8bf767c525f7fad",
    ),
    "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C045_LATEST_RAKL_GATE_RECEIPT_20260812.json": (
        "d89d70c745abe03060cb0a916cbe375ae1c65f1b",
        "62eaa24185ac20dba9a324f53d7b06bb05796236e5cc81ffbebd2ba1484bc675",
    ),
}


def _git(*args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=True,
        stdout=subprocess.PIPE,
        text=not binary,
    )
    return result.stdout if binary else result.stdout.strip()


def _canonical_sha256(value: object) -> str:
    raw = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _raw_sha256(commit: str, path: str) -> str:
    raw = _git("show", f"{commit}:{path}", binary=True)
    assert isinstance(raw, bytes)
    return hashlib.sha256(raw).hexdigest()


def _load_bundle() -> dict:
    document = json.loads(BUNDLE.read_text(encoding="utf-8"))
    assert isinstance(document, dict)
    return document


def _rehash(document: dict) -> dict:
    subject = copy.deepcopy(document)
    subject.pop("bundle_canonical_sha256", None)
    document["bundle_canonical_sha256"] = _canonical_sha256(subject)
    return document


@pytest.fixture(scope="module")
def producer_checkout(tmp_path_factory: pytest.TempPathFactory) -> Path:
    document = _load_bundle()
    checkout = tmp_path_factory.mktemp("c045-feedback") / "RAKL_math"
    subprocess.run(
        ["git", "clone", "-q", "--no-checkout", str(ROOT), str(checkout)],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(checkout), "remote", "set-url", "origin", REPOSITORY_URL],
        check=True,
    )
    subprocess.run(
        [
            "git",
            "-C",
            str(checkout),
            "checkout",
            "-q",
            "--detach",
            document["producer"]["commit_sha"],
        ],
        check=True,
    )
    return checkout


def _import(document: dict, producer_checkout: Path):
    source = str(FRAMEWORK / "src")
    if source not in sys.path:
        sys.path.insert(0, source)
    from rakl.application_feedback import import_application_feedback

    return import_application_feedback(
        document,
        source_repository=producer_checkout,
        current_framework_commit_sha=FRAMEWORK_COMMIT,
        current_framework_version=FRAMEWORK_VERSION,
    )


def test_c045_feedback_is_one_exact_proposal_only_meta_observation() -> None:
    document = _load_bundle()
    schema = json.loads(
        (FRAMEWORK / "schemas/application-feedback-bundle.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(document)
    assert document["bundle_canonical_sha256"] == _canonical_sha256(
        {key: value for key, value in document.items() if key != "bundle_canonical_sha256"}
    )

    assert len(document["items"]) == 1
    item = document["items"][0]
    assert item["kind"] == "META_OBSERVATION"
    assert item["kind"] not in {"FAILURE_EXPERIENCE", "TOOL_CANDIDATE"}
    assert item["payload"]["validation_status"] == "UNVALIDATED_PROPOSAL"
    assert document["framework_requirement"] == {
        "repository_url": "https://github.com/SzeChunYiu/RAKL.git",
        "commit_sha": FRAMEWORK_COMMIT,
        "version": FRAMEWORK_VERSION,
    }
    assert document["authority_envelope"] == {
        "requested_authority": "HEURISTIC",
        "proposal_only": True,
        "inventory_mutation_allowed": False,
        "failure_lattice_mutation_allowed": False,
        "promotion_allowed": False,
    }


def test_c045_feedback_binds_exact_merged_application_evidence() -> None:
    document = _load_bundle()
    item = document["items"][0]
    payload = item["payload"]
    binding = payload["observed_application_binding"]
    assert binding["commit_sha"] == OBSERVED_PRODUCER
    assert binding["tree_sha"] == OBSERVED_TREE
    assert _git("rev-parse", f"{OBSERVED_PRODUCER}^{{tree}}") == OBSERVED_TREE
    assert binding["framework_commit"] == FRAMEWORK_COMMIT
    assert binding["evidence"] == [
        {"path": path, "git_blob_sha": blob, "raw_sha256": digest}
        for path, (blob, digest) in EXPECTED_EVIDENCE.items()
    ]
    for path, (blob, digest) in EXPECTED_EVIDENCE.items():
        assert _git("rev-parse", f"{OBSERVED_PRODUCER}:{path}") == blob
        assert _raw_sha256(OBSERVED_PRODUCER, path) == digest

    # The feedback payload did not exist in the immutable observed tree.  The
    # transport producer is therefore a transparent one-commit child whose
    # parent is the exact observed main, rather than a false commit:path claim.
    transport = document["producer"]
    assert _git("rev-parse", f"{transport['commit_sha']}^") == OBSERVED_PRODUCER
    assert _git("rev-parse", f"{transport['commit_sha']}^{{tree}}") == transport["tree_sha"]


def test_c045_feedback_transport_and_context_bindings_are_exact() -> None:
    document = _load_bundle()
    producer = document["producer"]["commit_sha"]
    item = document["items"][0]
    source = item["source"]
    bindings = item["application_bindings"]
    raw = _git("show", f"{producer}:{source['path']}", binary=True)
    assert isinstance(raw, bytes)
    assert source["git_blob_sha"] == _git("rev-parse", f"{producer}:{source['path']}")
    assert json.loads(raw) == item["payload"]
    assert item["payload_canonical_sha256"] == _canonical_sha256(item["payload"])
    for role in ("result", "trace", "context"):
        path = bindings[f"{role}_path"]
        assert bindings[f"{role}_git_blob_sha"] == _git(
            "rev-parse", f"{producer}:{path}"
        )
        assert bindings[f"{role}_sha256"] == _raw_sha256(producer, path)
    assert bindings["context_sha256"] == item["payload"]["context_sha256"]


def test_c045_feedback_import_is_quarantined_and_grants_zero_authority(
    producer_checkout: Path,
) -> None:
    document = _load_bundle()
    receipt = _import(document, producer_checkout)
    assert receipt.verdict.value == "QUARANTINED_PROPOSAL"
    assert receipt.effective_authority == "HEURISTIC"
    assert receipt.inventory_mutation_performed is False
    assert receipt.failure_lattice_mutation_performed is False
    assert receipt.grants_scientific_authority is False
    assert receipt.grants_method_promotion is False

    authority = document["items"][0]["payload"]["authority_contract"]
    assert authority == {
        "effective_authority": "PROPOSAL_ONLY",
        "grants_mathematical_saturation": False,
        "grants_mathematical_result": False,
        "grants_p_vs_np_root_authority": False,
        "grants_framework_evolution_authority": False,
        "grants_review_independence": False,
        "grants_method_promotion": False,
        "grants_framework_promotion": False,
        "grants_review_authority": False,
    }


def test_c045_feedback_names_the_incomplete_contract_and_compensating_control() -> None:
    payload = _load_bundle()["items"][0]["payload"]
    assert payload["failure_attribution"] == "IMPLEMENTATION_DEFECT"
    assert payload["classification"] == "CLASS_A_SOFTWARE_ASSURANCE_DEFECT"
    assert payload["mathematical_lesson_credit"] is False
    assert payload["failure_experience_credit"] is False
    assert {row["type"] for row in payload["affected_typed_hash_contracts"]} == {
        "MathContextFiber",
        "ResearchMemoryReview",
        "ObstructionTransformationEpisode",
        "ObstructionTransformationReview",
        "StructuralMappingWitness",
    }
    assert payload["compensating_control"]["status"] == "DETECTS_IN_C045"
    assert payload["compensating_control"]["generic_contract_repaired"] is False

    cases = {case["case_id"]: case["expected"] for case in payload["future_protected_benchmark"]["cases"]}
    assert cases == {
        "CLEAN_CANONICAL_HASH": "PASS",
        "EVERY_SEMANTIC_DATACLASS_FIELD_STALE_HASH": "FAIL",
        "NESTED_TRANSFERS_ANALOGIES_OBSTRUCTION_MAPPING_GLUE_EXHAUSTION_LIFT": "FAIL",
        "STALE_CONTEXT_BLOCKS_MEMORY": "FAIL",
        "STALE_MEMORY_BLOCKS_SHORTCUT": "FAIL",
        "REHASHED_REVIEW_WITHOUT_TRACE_REBIND": "FAIL",
        "REHASHED_EPISODE_WITHOUT_MEMORY_SNAPSHOT_REBIND": "FAIL",
        "LEGITIMATE_SUCCESSOR_AFTER_ALL_DOWNSTREAM_REBINDINGS": "PASS",
        "MALFORMED_PREFIX_LENGTH_CASE_WHITESPACE_ENCODING": "FAIL",
        "MISSING_OBJECT": "CANNOT_CHECK",
        "CANONICAL_JSON_FORMAT_AND_KEY_ORDER_INVARIANCE": "PASS",
        "DATACLASS_FIELD_COVERAGE_ASSERTION": "PASS",
        "PLANTED_WEAK_IDENTIFIER_ONLY_HASH": "FAIL",
    }
    assert payload["future_protected_benchmark"]["chronology"] == (
        "freeze evaluator and benchmark outside challenger write authority before framework implementation"
    )


@pytest.mark.parametrize(
    "mutation",
    (
        "envelope",
        "kind",
        "producer_sha",
        "source_blob",
        "result_hash",
        "validation_status",
        "zero_mathematical_saturation",
        "zero_mathematical_result",
        "zero_root",
        "zero_framework_promotion",
        "zero_review_authority",
    ),
)
def test_c045_feedback_hostile_mutations_are_rejected(
    mutation: str, producer_checkout: Path
) -> None:
    hostile = copy.deepcopy(_load_bundle())
    item = hostile["items"][0]
    if mutation == "envelope":
        hostile["authority_envelope"]["promotion_allowed"] = True
    elif mutation == "kind":
        item["kind"] = "FAILURE_EXPERIENCE"
    elif mutation == "producer_sha":
        hostile["producer"]["commit_sha"] = "0" * 40
    elif mutation == "source_blob":
        item["source"]["git_blob_sha"] = "0" * 40
    elif mutation == "result_hash":
        item["application_bindings"]["result_sha256"] = "0" * 64
    elif mutation == "validation_status":
        item["payload"]["validation_status"] = "VALIDATED"
        item["payload_canonical_sha256"] = _canonical_sha256(item["payload"])
    elif mutation.startswith("zero_"):
        authority_key = {
            "zero_mathematical_saturation": "grants_mathematical_saturation",
            "zero_mathematical_result": "grants_mathematical_result",
            "zero_root": "grants_p_vs_np_root_authority",
            "zero_framework_promotion": "grants_framework_promotion",
            "zero_review_authority": "grants_review_authority",
        }[mutation]
        item["payload"]["authority_contract"][authority_key] = True
        item["payload_canonical_sha256"] = _canonical_sha256(item["payload"])
    else:  # pragma: no cover
        raise AssertionError(mutation)
    _rehash(hostile)
    receipt = _import(hostile, producer_checkout)
    assert receipt.verdict.value != "QUARANTINED_PROPOSAL"

