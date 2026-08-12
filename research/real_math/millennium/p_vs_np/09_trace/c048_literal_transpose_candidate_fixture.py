"""Deterministic C048 literal-transpose candidate freeze; no evaluation."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

APPLICATION_BASE_SHA="76b783531956249160e36639dd6326fd2f5911ee"
PRE_CANDIDATE_FREEZE_SHA="f765a0cb27d4602eb41bc4a38887696c6a954707"
FRAMEWORK_SHA="43897d3afaf0038385102d5acc64793c05ec40f0"
CANDIDATE_ID="C048-LITERAL-TRANSPOSE-TRANSFER-CONDITION-v1"
FROZEN_AT="2026-08-12T04:01:00Z"
BASE="research/real_math/millennium/p_vs_np"
PRE_GATE=f"{BASE}/09_trace/O9d12a2a1b_C048_PRE_CANDIDATE_GATE_RECEIPT_20260812.json"
PRE_TRACE=f"{BASE}/09_trace/O9d12a2a1b_C048_PRE_CANDIDATE_TRACE_20260812.json"
EVALUATOR=f"{BASE}/05_falsification/c048_literal_transpose_transfer_evaluator.py"
EVALUATOR_RAW="c6dad8202ae0dcaf1bce4b0b6c45b6ffad9c39cd636626e57715ca1624c994b6"
PRE_GATE_BLOB="c95d076e2dca04d1e5aa4b81c85c6b159edcfb69"
PRE_GATE_RAW="26a9370f781fc3c95a11b2eaa7cc99161e31e8636af92a05022f1130897a1e32"
PRE_TRACE_BLOB="58e06181159111d4c29422bb70e1fd0589967ddd"
PRE_TRACE_RAW="ea18de8d393fb901b06926ab7ab81a4dff6af8b4f641fd89964222549995316b"
PATHS={
 "candidate":f"{BASE}/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_TRANSFER_CONDITION_FREEZE_20260812.json",
 "manifest":f"{BASE}/05_falsification/O9d12a2a1b_C048_LITERAL_TRANSPOSE_TRANSFER_EVALUATOR_FREEZE_20260812.json",
 "authorization":f"{BASE}/09_trace/O9d12a2a1b_C048_EVALUATION_AUTHORIZATION_20260812.json",
 "trace":f"{BASE}/09_trace/O9d12a2a1b_C048_CANDIDATE_FREEZE_TRACE_20260812.json",
 "feedback":f"{BASE}/10_feedback/C048_TRANSPOSE_TWO_INTERFACE_APPLICATION_FEEDBACK_PROPOSAL_20260812.json",
 "receipt":f"{BASE}/09_trace/O9d12a2a1b_C048_CANDIDATE_FREEZE_RECEIPT_20260812.json",
}

def h(v): return "sha256:"+hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def seal(v):
 r=dict(v); r["artifact_hash"]=""; r["artifact_hash"]=h(r); return r

def build_documents():
 candidate=seal({
  "schema_version":"1.0.0","candidate_id":CANDIDATE_ID,"atom_id":"O9d12a2a1b-C048","candidate_kind":"MATHEMATICAL_TRANSFER_CONDITION_LEMMA_CANDIDATE","frozen_at":FROZEN_AT,
  "definitions":{
   "parent_side":"M=2^k",
   "parent_word":"x=bin_k(r)||bin_k(c)",
   "original_cross_complement":"(r,M+c) belongs to U iff Dec(x) is UNSAT",
   "literal_transpose":"U^T={(b,a):(a,b) in U}; hence the cross point is (M+c,r)",
   "transposed_graph":"G^T=[2M]^2\\U^T",
   "canonical_current_prefix_language":"P_(k+1)={first k+1 bits of canonical C041 words of length 2(k+1)}",
   "unsat_suffix_language":"S_k={c: exists r with Dec(bin_k(r)||bin_k(c)) canonical and UNSAT}",
  },
  "statement":{
   "part_A_reduction_faithfulness":"For every ordered query (a,b), (a,b) in G iff (b,a) in G^T. Therefore the correctly swapped reduction F -> (M+c,r) preserves x=r||c and satisfies F in SAT iff (M+c,r) in G^T whenever the original C041 reduction satisfies F in SAT iff (r,M+c) in G.",
   "part_B_row_projection":"The high-row projection contributed by the literal-transpose cross block is exactly {M+c:c in S_k}, whose (k+1)-bit words are {1||bin_k(c):c in S_k}.",
   "part_C_collision_condition":"A literal-transpose high row is a current canonical prefix exactly when {1||bin_k(c):c in S_k} intersects P_(k+1); equivalently some canonical UNSAT parent word r||c has suffix c equal to the final k bits of a canonical current prefix beginning with 1.",
   "part_D_repair_verdict_rule":"Reduction faithfulness and row-label collision are separate necessary conditions. Full literal transposition with the swapped reduction map proves the former only. A collision without endpoint-swapped language equivalence is a failed repair, not success; absence of overlap also fails the repair.",
   "scope":"all k>=2 under the exact C041 square domain, total decoder, equal split, and full relation transpose",
  },
  "attempted_implication":"literal transposition might repair C047 by putting suffix c, rather than prefix r, on the fresh row while preserving the NP-complete graph language",
  "predicted_mathematical_outcome":"the transpose succeeds exactly on reduction faithfulness; collision feasibility reduces to the frozen suffix-tail overlap condition and is not inferred from transposition alone",
  "proof_obligations":["RELATION_COMPLEMENT_TRANSPOSE_IDENTITY","BOTH_ENDPOINTS_AND_REDUCTION_MAP_SWAP","SUFFIX_ROW_PROJECTION_CHARACTERIZATION","EXACT_COLLISION_IFF_OVERLAP_LANGUAGE","COLLISION_AND_REDUCTION_ARE_INDEPENDENT_NECESSARY_CONDITIONS"],
  "falsifiers":["an ordered pair changes graph membership after both coordinates and the whole complement relation are transposed","the original cross point (r,M+c) transposes to anything other than (M+c,r)","a high row outside {M+c:c in S_k}","a collision without a witness in the stated overlap language or an overlap witness without a collision","the unchanged old reduction F->(r,M+c) is claimed to target G^T"],
  "assumptions":["full relation transpose, not one-endpoint movement","both query endpoints swap in the reduction","unchanged C041 decoder and equal split","square ambient domain so complement commutes with transpose","exact label equality is the collision QoI"],
  "non_guarantees":["no claim that the overlap language is nonempty at any level","no target enumeration or cover evaluation","no cover/circuit lower bound, novelty, or P-versus-NP authority","same-context derivation is not independent review"],
  "source_identity":{"application_base_commit":APPLICATION_BASE_SHA,"pre_candidate_freeze_commit":PRE_CANDIDATE_FREEZE_SHA,"framework_commit":FRAMEWORK_SHA,"pre_candidate_gate":{"path":PRE_GATE,"git_blob":PRE_GATE_BLOB,"raw_sha256":PRE_GATE_RAW}},
  "target_access":{"decoder_imported_or_executed":False,"evaluator_imported_or_executed":False,"later_target_enumerated":False,"later_target_result_accessed":False,"finite_collision_level_selected":False},
  "credit_boundary":{"mathematical_content":["exact transpose identity","endpoint-swapped reduction condition","row-language characterization","collision iff overlap transfer condition","falsifiers and scope"],"assurance_only_zero_credit":["Git/branch/PR chronology","CI/tests","schemas/hashes/serialization","runtime/evaluator wiring"],"candidate_freeze_mathematical_result_credit":False},
 })
 manifest=seal({"schema_version":"1.0.0","manifest_id":"PNP-C048-LITERAL-TRANSPOSE-EVALUATOR-FREEZE-20260812","candidate_id":CANDIDATE_ID,"frozen_at":FROZEN_AT,"status":"FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED","evaluator":{"path":EVALUATOR,"raw_sha256":EVALUATOR_RAW},"required_obligations":candidate["proof_obligations"],"target_result_capability":False,"later_execution_gate":{"separate_post_freeze_authorization_required":True,"current_task_execution_authorized":False,"target_enumeration_forbidden":True},"authority":{"proof_authority":False,"mathematical_result_credit":False,"p_vs_np_authority":False}})
 authorization=seal({"schema_version":"1.0.0","authorization_id":"PNP-C048-EVALUATION-AUTHORIZATION-20260812","candidate_id":CANDIDATE_ID,"evaluator_raw_sha256":EVALUATOR_RAW,"current_task_evaluator_execution_authorized":False,"later_target_access_authorized":False,"finite_target_scan_authorized":False,"allowed_next_action":"PUBLICLY_FREEZE_EXACT_CANDIDATE_AND_INERT_EVALUATOR_BEFORE_PROOF_CHECK","future_proof_check_requires_separate_authorization":True,"target_result_state":"TARGET_RESULT_UNACCESSED","mathematical_result_credit":False})
 pre=json.loads(Path(PRE_TRACE).read_text()); entries=list(pre["entries"])
 event={"event_id":"O9d12a2a1b-C048-E09","atom_id":"O9d12a2a1b-C048","event_type":"CANDIDATE_PROPOSED","timestamp":FROZEN_AT,"state_summary":"Strict gates passed publicly; one literal-transpose transfer-condition lemma and inert checker are frozen without decoder, target, or evaluator access.","action_summary":"Freeze exact relation-transpose, swapped-reduction, suffix-row, and collision-overlap obligations.","evidence_pointers":[PATHS["candidate"],PATHS["manifest"],PATHS["authorization"],PRE_GATE],"alternatives_considered":["claim collision from high-half occupancy","retain old ordered reduction","enumerate target levels","freeze the two-interface transfer condition"],"decision_rationale":"A literal transpose changes both endpoints. The smallest target-blind mathematical action separates automatic relation/reduction equivariance from the still-open label-language overlap.","outputs":[CANDIDATE_ID,"MATHEMATICAL_TRANSFER_CONDITION_CANDIDATE","TARGET_RESULT_UNACCESSED",candidate["artifact_hash"]],"uncertainties":["proof not checked","overlap nonemptiness unresolved","same-context review is not independent"],"residuals":["proof obligations unexecuted","overlap language unresolved","root OPEN"],"next_steps":["publish freeze","then freeze proof certificate and narrow authorization","never enumerate downstream targets"],"previous_event_hash":entries[-1]["artifact_hash"]}; event["artifact_hash"]=h(event); entries.append(event)
 trace={"trace_id":"PNP-O9d12a2a1b-C048-CANDIDATE-FREEZE-TRACE-20260812","entries":entries}
 feedback=seal({"schema_version":"1.0.0","feedback_id":"PNP-C048-TRANSPOSE-TWO-INTERFACE-PROPOSAL-20260812","source_atom_id":"O9d12a2a1b-C048","status":"APPLICATION_FEEDBACK_PROPOSAL_ONLY_NOT_PROMOTED","proposed_method_lesson":"When transporting an ordered relation by transposition, audit exact interface congruence and semantic/reduction equivariance separately; neither substitutes for the other.","mathematical_basis_if_validated":"full transpose preserves graph membership under coordinate swap, while desired row collision is a separate suffix-tail overlap condition","validation_obligations":["validate the exact C048 lemma","test examples where transpose preserves semantics but has no desired collision","test examples where an apparent collision accompanies an incorrect unswapped reduction","fresh Self-RAKL assurance before any framework promotion"],"authority":{"framework_evolution_authority":False,"method_promotion_authority":False,"same_context_review_is_independent":False},"credit":{"feedback_transport_mathematical_result_credit":False,"software_process_credit":0}})
 docs={"candidate":candidate,"manifest":manifest,"authorization":authorization,"trace":trace,"feedback":feedback}
 integrity={"algorithm":"SHA-256","canonicalization":"JSON_SORT_KEYS_COMPACT_UTF8","json_inputs":{n:{"path":PATHS[n],"canonical_sha256":h(d)} for n,d in sorted(docs.items())},"byte_inputs":{"evaluator":{"path":EVALUATOR,"raw_sha256":EVALUATOR_RAW},"pre_gate":{"path":PRE_GATE,"git_blob":PRE_GATE_BLOB,"raw_sha256":PRE_GATE_RAW},"pre_trace":{"path":PRE_TRACE,"git_blob":PRE_TRACE_BLOB,"raw_sha256":PRE_TRACE_RAW}}}
 receipt=seal({"schema_version":"1.0.0","receipt_id":"PNP-C048-LITERAL-TRANSPOSE-CANDIDATE-FREEZE-20260812","candidate_id":CANDIDATE_ID,"frozen_at":FROZEN_AT,"chronology":{"pre_candidate_freeze_commit":PRE_CANDIDATE_FREEZE_SHA,"candidate_frozen_after_pre_candidate_gate":True,"candidate_publication_status":"TO_BE_PUBLISHED_BEFORE_ANY_EVALUATION","target_result_accessed":False,"evaluator_imported_or_executed":False},"full_document_integrity":integrity,"full_document_integrity_hash":h(integrity),"authority":{"candidate_is_mathematical_proposal":True,"theorem_truth":False,"independent_review":False,"mathematical_result_credit":False,"p_vs_np_authority":False,"root_status":"OPEN"},"allowed_next_action":"PUSH_PUBLIC_FREEZE_THEN_CREATE_SEPARATE_PROOF_CERTIFICATE_AND_AUTHORIZATION"})
 docs["receipt"]=receipt; return docs

if __name__=="__main__": print(json.dumps(build_documents(),indent=2,sort_keys=True))
