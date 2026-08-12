#!/usr/bin/env python3
"""Capability-free integrity verifier for the C046 candidate freeze."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
BASE=Path("research/real_math/millennium/p_vs_np")
RECEIPT=BASE/"09_trace/O9d12a2a1b_C046_CANDIDATE_FREEZE_RECEIPT_20260812.json"
JSON_INPUTS={
 "candidate":BASE/"04_candidates/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_LEMMA_FREEZE_20260812.json",
 "evaluator_manifest":BASE/"05_falsification/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_EVALUATOR_FREEZE_20260812.json",
 "authorization":BASE/"09_trace/O9d12a2a1b_C046_EVALUATION_AUTHORIZATION_20260812.json",
 "trace":BASE/"09_trace/O9d12a2a1b_C046_CANDIDATE_FREEZE_TRACE_20260812.json",
 "feedback":BASE/"10_feedback/C046_INVARIANT_FEASIBILITY_FIRST_APPLICATION_FEEDBACK_PROPOSAL_20260812.json",
}
class PacketIntegrityError(RuntimeError):pass
def load(p):
 v=json.loads(p.read_text());
 if not isinstance(v,dict):raise ValueError("top-level object required")
 return v
def h(v):return "sha256:"+hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def raw(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def audit_packet(root):
 root=Path(root);errors=[]
 try:r=load(root/RECEIPT)
 except Exception as exc:return(f"receipt cannot load: {exc}",)
 subject=dict(r);subject["artifact_hash"]=""
 if r.get("artifact_hash")!=h(subject):errors.append("receipt artifact_hash mismatch")
 integ=r.get("full_document_integrity",{})
 if set(integ.get("json_inputs",{}))!=set(JSON_INPUTS):errors.append("receipt json input set mismatch")
 for name,p in JSON_INPUTS.items():
  b=integ.get("json_inputs",{}).get(name,{})
  if b.get("path")!=p.as_posix():errors.append(f"{name}: path mismatch");continue
  try:a=h(load(root/p))
  except Exception as exc:errors.append(f"{name}: cannot load: {exc}");continue
  if b.get("canonical_sha256")!=a:errors.append(f"{name}: digest mismatch")
 for name,b in integ.get("byte_inputs",{}).items():
  p=Path(b.get("path",""))
  try:a=raw(root/p)
  except Exception as exc:errors.append(f"{name}: cannot load: {exc}");continue
  if b.get("raw_sha256")!=a:errors.append(f"{name}: raw digest mismatch")
 if r.get("full_document_integrity_hash")!=h(integ):errors.append("receipt integrity hash mismatch")
 if r.get("chronology",{}).get("target_result_accessed") is not False:errors.append("receipt target access changed")
 if r.get("authority",{}).get("mathematical_result_credit") is not False:errors.append("receipt result credit widened")
 auth=load(root/JSON_INPUTS["authorization"])
 if auth.get("current_task_evaluator_execution_authorized") is not False:errors.append("authorization widened")
 return tuple(errors)
def verify_packet(root):
 e=audit_packet(root)
 if e:raise PacketIntegrityError("C046 candidate packet failed: "+"; ".join(e))
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument("--repo-root",type=Path,default=Path(__file__).resolve().parents[5]);a=p.parse_args(argv)
 try:verify_packet(a.repo_root)
 except PacketIntegrityError as exc:print(json.dumps({"status":"FAIL","error":str(exc)},sort_keys=True));return 1
 print(json.dumps({"status":"PASS","candidate":"C046-HIGH-HALF-SEPARATION-LEMMA-v1","target_result_accessed":False,"evaluator_executed":False},sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
