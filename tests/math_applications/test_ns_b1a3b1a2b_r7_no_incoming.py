from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "RAKL" / "src"))

from rakl.summation_compatibility import (  # noqa: E402
    ConvergenceStatus,
    GluingConsumer,
    GluingStatus,
    PermissionStatus,
    SummationCompatibilityWitness,
    WitnessAuditVerdict,
    audit_summation_compatibility,
)

BASE = ROOT / "research" / "real_math" / "millennium" / "navier_stokes"


def _load(name: str) -> dict:
    return json.loads((BASE / "05_falsification" / name).read_text())


def _witness(doc: dict) -> SummationCompatibilityWitness:
    return SummationCompatibilityWitness(
        witness_id=doc["witness_id"], atom_id=doc["atom_id"],
        source_accumulation_method=doc["source_accumulation_method"],
        convergence_status=ConvergenceStatus(doc["convergence_status"]),
        finite_grouping_permitted=PermissionStatus(doc["finite_grouping_permitted"]),
        infinite_regrouping_reordering_permitted=PermissionStatus(doc["infinite_regrouping_reordering_permitted"]),
        nested_limit_order=doc["nested_limit_order"], local_block_definition=doc["local_block_definition"],
        block_tail_or_convergence_theorem_required=doc["block_tail_or_convergence_theorem_required"],
        alternate_summation_equivalence_proof=doc["alternate_summation_equivalence_proof"],
        gluing_status=GluingStatus(doc["gluing_status"]), evidence_pointers=tuple(doc["evidence_pointers"]),
        recorded_at_utc=doc["recorded_at_utc"],
    )


def test_temporal_witness_passes_gluing_but_never_theorem_authority():
    doc = _load("NS-B1a3b1a2b_R7_SUMMATION_TEMPORAL_WITNESS_20260812.json")
    witness = _witness(doc)
    assert witness.witness_canonical_sha256 == doc["witness_canonical_sha256"]
    audit = audit_summation_compatibility(witness, expected_atom_id="NS-B1a3b1a2b-R7", consumer=GluingConsumer.LOCAL_TO_GLOBAL_GLUING, claimed_witness_hash=doc["witness_canonical_sha256"])
    assert audit.verdict is WitnessAuditVerdict.GLUING_AUTHORITY_OK
    assert audit.grants_gluing_authority is True
    theorem = audit_summation_compatibility(witness, expected_atom_id="NS-B1a3b1a2b-R7", consumer=GluingConsumer.THEOREM_AUTHORITY)
    assert theorem.verdict is WitnessAuditVerdict.THEOREM_AUTHORITY_REJECTED


def test_spatial_lorentz_transport_fails_closed():
    doc = _load("NS-B1a3b1a2b_R7_SUMMATION_SPATIAL_WITNESS_20260812.json")
    witness = _witness(doc)
    assert witness.witness_canonical_sha256 == doc["witness_canonical_sha256"]
    audit = audit_summation_compatibility(witness, expected_atom_id="NS-B1a3b1a2b-R7", consumer=GluingConsumer.LOCAL_TO_GLOBAL_GLUING, claimed_witness_hash=doc["witness_canonical_sha256"])
    assert audit.verdict is WitnessAuditVerdict.FAIL_CLOSED_UNKNOWN
    assert audit.grants_gluing_authority is False


def test_shell_majorants_are_summable_and_root_stays_blocked():
    assert math.isfinite(sum((2.0 ** (2*k)) * math.exp(-(4.0**k)/8.0) for k in range(20)))
    assert sum(2.0 ** (-3*k) for k in range(40)) < 2.0
    metrics = json.loads((BASE / "10_case_study" / "NS-B1a3b1a2b_R7_RAKL_CYCLE_METRICS_20260812.json").read_text())
    assert metrics["gate_provenance_ci"]["root_gate"] == "BLOCKED_OPEN_NO_SOLUTION_CERTIFICATE"
    assert metrics["gate_provenance_ci"]["independent_math_review"] == "0/3"
    assert all(v == 0 for v in metrics["retained_semantic_novelty"]["protected_canonical"].values())
