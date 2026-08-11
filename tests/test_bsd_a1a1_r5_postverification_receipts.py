import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
M = ROOT / "research" / "real_math" / "millennium" / "birch_swinnerton_dyer" / "07_memory"
DIAG = M / "BSD_A1a1_R5_PROVENANCE_PROCESS_DIAGNOSIS_20260811.json"
FAIL = M / "BSD_A1a1_R5_PROVENANCE_PROCESS_FAILURE_20260811.json"
METRICS = M / "BSD_A1a1_RAKL_CYCLE_METRICS_SUCCESSOR_20260811_R5.json"
ADDENDUM = M / "RAKL_METHOD_CASE_STUDY_BSD_A1a1_BASECHANGE_PLECTIC_20260811_R5_CI_ADDENDUM.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(obj):
    payload = dict(obj)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_postverification_receipts_are_hash_valid_and_additive():
    for path in [DIAG, FAIL, METRICS, ADDENDUM]:
        assert path.exists(), path
    for path in [DIAG, FAIL, METRICS]:
        obj = load(path)
        assert obj["artifact_hash"] == canonical_hash(obj)


def test_process_failure_is_not_misclassified_as_math_or_learning():
    diagnosis = load(DIAG)
    failure = load(FAIL)
    metrics = load(METRICS)
    assert diagnosis["mathematical_failure"] is False
    assert diagnosis["gluing_failure"] is False
    assert failure["status"] == "OBSERVED_ONLY"
    assert failure["effect_on_mathematical_outcome"].startswith("NONE")
    assert metrics["retained_semantic_novelty"] == {
        "KNOWLEDGE": 1, "OPERATOR": 0, "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0, "RELATION": 1, "PATH": 1, "META_METHOD": 0,
    }


def test_ci_failure_repair_and_self_head_limitation_are_explicit():
    metrics = load(METRICS)
    gate = metrics["gate_and_provenance"]
    assert gate["first_ci"]["status"] == "FAIL"
    assert gate["first_ci"]["classification"] == "PROVENANCE_TOOLING_META_POLICY"
    assert gate["pre_successor_ci"]["status"] == "PASS"
    assert gate["pre_successor_ci"]["tests"] == "459 passed in 35.54s"
    assert gate["pre_successor_ci"]["verified_execution_framework_pin"] == "787c7e00af2a5877ccb715bc807ec14f52974e9c"
    assert gate["receipt_containing_head_ci_status"].startswith("CANNOT_MEASURE")
    assert metrics["application"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["outcome"]["candidate_generated"] is False
