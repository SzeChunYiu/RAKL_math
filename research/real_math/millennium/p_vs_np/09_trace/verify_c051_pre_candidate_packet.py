#!/usr/bin/env python3
"""Capability-free full-document integrity verifier for C051 pre-candidate state."""
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime
from pathlib import Path

BASE = Path("research/real_math/millennium/p_vs_np")
GATE = BASE / "09_trace/O9d12a2a1b_C051_PRE_CANDIDATE_GATE_RECEIPT_20260812.json"
INPUTS = {
    "atomization": BASE / "02_problem_dag/O9d12a2a1b_C051_ATOMIZATION_20260812.json",
    "context": BASE / "01_frontier/O9d12a2a1b_C051_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": BASE / "07_memory/O9d12a2a1b_C051_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": BASE / "07_memory/O9d12a2a1b_C051_FAILURE_SNAPSHOT_20260812.json",
    "memory": BASE / "07_memory/O9d12a2a1b_C051_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": BASE / "07_memory/O9d12a2a1b_C051_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": BASE / "08_reviews/O9d12a2a1b_C051_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": BASE / "08_reviews/O9d12a2a1b_C051_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": BASE / "09_trace/O9d12a2a1b_C051_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": BASE / "09_trace/O9d12a2a1b_C051_PRE_CANDIDATE_TRACE_20260812.json",
    "framework_binding": BASE / "09_trace/O9d12a2a1b_C051_FRAMEWORK_SUBJECT_FREEZE_BINDING_20260812.json",
    "framework_observation": BASE / "09_trace/O9d12a2a1b_C051_FRAMEWORK_SUBJECT_REVALIDATION_20260812.json",
}
class PacketIntegrityError(RuntimeError): pass
def load(path):
    value=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value,dict): raise ValueError("top-level JSON must be object")
    return value
def digest(value): return "sha256:"+hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def audit_packet(root):
    root=Path(root); errors=[]
    try: gate=load(root/GATE)
    except Exception as exc: return (f"gate: cannot load: {exc}",)
    subject=dict(gate); subject["artifact_hash"]=""
    if gate.get("artifact_hash") != digest(subject): errors.append("gate: artifact_hash mismatch")
    integrity=gate.get("full_document_integrity",{})
    if integrity.get("algorithm")!="SHA-256" or integrity.get("canonicalization")!="JSON_SORT_KEYS_COMPACT_UTF8": errors.append("gate: integrity contract mismatch")
    bindings=integrity.get("inputs",{})
    if set(bindings)!=set(INPUTS): errors.append("gate: full-document input set is not exact")
    for name,path in INPUTS.items():
        binding=bindings.get(name,{})
        if binding.get("path")!=path.as_posix(): errors.append(f"{name}: path mismatch"); continue
        try: actual=digest(load(root/path))
        except Exception as exc: errors.append(f"{name}: cannot load: {exc}"); continue
        if binding.get("canonical_sha256")!=actual: errors.append(f"{name}: full-document digest mismatch")
    if gate.get("artifact_bindings",{}).get("full_document_integrity_hash")!=digest(integrity): errors.append("gate: integrity hash mismatch")
    if gate.get("gate_verdicts",{}).get("licensed_action")!="FREEZE_K19_ALIGNMENT_DISCRIMINATOR_ONLY": errors.append("gate: wrong licensed action")
    if gate.get("gate_verdicts",{}).get("framework_subject")!="CURRENT_UNCHANGED": errors.append("gate: framework subject not current")
    if gate.get("application_authority",{}).get("target_evaluator_execution_authorized") is not False: errors.append("gate: evaluator authorization widened")
    chronology=gate.get("chronology",{})
    if chronology.get("target_result_accessed") is not True: errors.append("gate: k13 exposure not recorded")
    if chronology.get("untouched_target_result_accessed") is not False: errors.append("gate: k19 target access boundary changed")
    if chronology.get("target_state") != "K13_QUARANTINED_PROCESS_CONTAMINATION__K19_TARGET_RESULT_UNACCESSED": errors.append("gate: wrong target state")
    if chronology.get("quarantined_families") != ["k=13"]: errors.append("gate: k13 quarantine missing")
    authority=gate.get("application_authority",{})
    if authority.get("isolated_target_blind_operator_required") is not True: errors.append("gate: isolated target-blind operator not required")
    framework_binding=load(root/INPUTS["framework_binding"]); framework_observation=load(root/INPUTS["framework_observation"])
    if framework_binding.get("authoritative_framework_sha") != gate.get("framework_commit"): errors.append("framework: freeze SHA mismatch")
    if framework_observation.get("observed_current_main_sha") != gate.get("framework_commit"): errors.append("framework: observed main SHA mismatch")
    if framework_observation.get("verdict") != "CURRENT_UNCHANGED": errors.append("framework: revalidation did not pass unchanged")
    expert=load(root/INPUTS["expert_review"])
    if expert.get("review_authority")!="SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW": errors.append("expert: authority widened")
    atomization=load(root/INPUTS["atomization"]); context=load(root/INPUTS["context"]); trace=load(root/INPUTS["trace"])
    memory=load(root/INPUTS["memory"]); failure_snapshot=load(root/INPUTS["failure_snapshot"])
    witness=failure_snapshot.get("difference_witness",{}); reuse=failure_snapshot.get("reuse_assessment",{})
    required_witness_fields={"target_atom_id","target_context_hash","method_family","prior_failure_ids","changed_structural_coordinates","restored_or_replaced_assumptions","prior_falsifier_escape_reason","cheapest_repeat_failure_test","evidence_pointers"}
    if not required_witness_fields.issubset(witness): errors.append("failure reuse: protected DifferenceWitness fields missing")
    if witness.get("target_atom_id") != atomization.get("atom_id") or witness.get("target_context_hash") != context.get("packet_hash"): errors.append("failure reuse: witness target binding mismatch")
    if reuse.get("verdict") != "DIFFERENCE_WITNESSED": errors.append("failure reuse: protected reuse gate did not pass")
    if memory.get("relevant_failure_ids") != reuse.get("relevant_failure_ids"): errors.append("failure reuse: memory review ids differ from assessed ids")
    if memory.get("failure_lattice_snapshot_hash") != digest(failure_snapshot): errors.append("failure reuse: memory review is not bound to C051 failure snapshot")
    try:
        chronology_floor=max(datetime.fromisoformat(atomization["recorded_at"].replace("Z","+00:00")),datetime.fromisoformat(context["frozen_at"].replace("Z","+00:00")))
        if any(datetime.fromisoformat(entry["timestamp"].replace("Z","+00:00"))<=chronology_floor for entry in trace["entries"]): errors.append("trace: event predates or equals atom/context freeze")
    except (KeyError, TypeError, ValueError) as exc: errors.append(f"trace: invalid chronology: {exc}")
    return tuple(errors)
def verify_packet(root):
    errors=audit_packet(root)
    if errors: raise PacketIntegrityError("C051 packet failed: "+"; ".join(errors))
def main(argv=None):
    parser=argparse.ArgumentParser(); parser.add_argument("--repo-root",type=Path,default=Path(__file__).resolve().parents[5]); args=parser.parse_args(argv)
    try: verify_packet(args.repo_root)
    except PacketIntegrityError as exc: print(json.dumps({"status":"FAIL","error":str(exc)},sort_keys=True)); return 1
    print(json.dumps({"status":"PASS","licensed_action":"FREEZE_K19_ALIGNMENT_DISCRIMINATOR_ONLY","k13_quarantined":True,"untouched_target_result_accessed":False,"k19_target_result_accessed":False},sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
