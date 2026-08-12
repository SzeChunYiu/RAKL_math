#!/usr/bin/env python3
"""Capability-free full-document integrity verifier for C046 pre-candidate state."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

BASE = Path("research/real_math/millennium/p_vs_np")
GATE = BASE / "09_trace/O9d12a2a1b_C046_PRE_CANDIDATE_GATE_RECEIPT_20260812.json"
INPUTS = {
    "atomization": BASE / "02_problem_dag/O9d12a2a1b_C046_ATOMIZATION_20260812.json",
    "context": BASE / "01_frontier/O9d12a2a1b_C046_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": BASE / "07_memory/O9d12a2a1b_C046_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": BASE / "07_memory/O9d12a2a1b_C046_FAILURE_SNAPSHOT_20260812.json",
    "memory": BASE / "07_memory/O9d12a2a1b_C046_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": BASE / "07_memory/O9d12a2a1b_C046_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": BASE / "08_reviews/O9d12a2a1b_C046_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": BASE / "08_reviews/O9d12a2a1b_C046_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "preservation": BASE / "09_trace/O9d12a2a1b_C046_ROOT_COORDINATE_PRESERVATION_20260812.json",
    "trace": BASE / "09_trace/O9d12a2a1b_C046_PRE_CANDIDATE_TRACE_20260812.json",
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
    if gate.get("gate_verdicts",{}).get("licensed_action")!="FREEZE_HIGH_HALF_SEPARATION_LEMMA_CANDIDATE_ONLY": errors.append("gate: wrong licensed action")
    if gate.get("application_authority",{}).get("target_evaluator_execution_authorized") is not False: errors.append("gate: evaluator authorization widened")
    if gate.get("chronology",{}).get("target_result_accessed") is not False: errors.append("gate: target access boundary changed")
    expert=load(root/INPUTS["expert_review"])
    if expert.get("review_authority")!="SAME_CONTEXT_ROLE_SEPARATED_INTERNAL_REVIEW_NOT_INDEPENDENT_PEER_REVIEW": errors.append("expert: authority widened")
    return tuple(errors)
def verify_packet(root):
    errors=audit_packet(root)
    if errors: raise PacketIntegrityError("C046 packet failed: "+"; ".join(errors))
def main(argv=None):
    parser=argparse.ArgumentParser(); parser.add_argument("--repo-root",type=Path,default=Path(__file__).resolve().parents[5]); args=parser.parse_args(argv)
    try: verify_packet(args.repo_root)
    except PacketIntegrityError as exc: print(json.dumps({"status":"FAIL","error":str(exc)},sort_keys=True)); return 1
    print(json.dumps({"status":"PASS","licensed_action":"FREEZE_HIGH_HALF_SEPARATION_LEMMA_CANDIDATE_ONLY","target_result_accessed":False},sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
