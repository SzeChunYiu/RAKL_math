"""Serialize the authorized C052 off-window proof/check result artifacts."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
CANDIDATE = BASE / "04_candidates/O9d12a2a1b_C052_V21_OFFWINDOW_UNSAT_ANCHOR_LEMMA_FREEZE_20260812.json"
AUTHORIZATION = BASE / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_EVALUATION_AUTHORIZATION_20260812.json"
FREEZE_RECEIPT = BASE / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_CANDIDATE_FREEZE_RECEIPT_20260812.json"
CHECKER = BASE / "05_falsification/c052_v21_offwindow_independent_checker.py"
PROOF = BASE / "04_candidates/O9d12a2a1b_C052_V21_OFFWINDOW_SYMBOLIC_HAND_PROOF_20260812.json"
CHECK_RECEIPT = BASE / "05_falsification/O9d12a2a1b_C052_V21_OFFWINDOW_INDEPENDENT_CHECK_RESULT_20260812.json"
RESULT = BASE / "09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_RESULT_RECEIPT_20260812.json"
REVIEW = BASE / "08_reviews/O9d12a2a1b_C052_V21_OFFWINDOW_SAME_CONTEXT_REVIEW_20260812.json"
LESSON = BASE / "07_memory/O9d12a2a1b_C052_V21_OFFWINDOW_MATHEMATICAL_EXPERIENCE_20260812.json"

APPLICATION_BASE_SHA = "f9c1fc6d367d99cb685f310703dffacbb71f8c3e"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
AUTHORIZATION_BLOB = "c1224faa0416a20a96a29eeb6d050ef5db9e8df5"
RESULT_AT = "2026-08-12T14:25:06Z"
ATOM_ID = "O9d12a2a1b-C052-V2.1"
CANDIDATE_ID = "PNP-C052-OFFWINDOW-UNSAT-ANCHOR-MARGINAL-LEMMA-v1"


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def canonical_hash(value: object) -> str:
    return "sha256:" + hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def seal(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = canonical_hash(value)
    return result


def file_sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def checker_module():
    spec = importlib.util.spec_from_file_location("c052_offwindow_independent_checker", CHECKER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def proof_document() -> dict:
    obligations = [
        {"id": "O1", "status": "PROVED", "proof": "For a=bit_length(v), b=bit_length(m), gamma lengths are 2a-1 and 2b-1. Hence H=8+(2a-1)+(2b-1)=6+2a+2b. Each of 3m literals has sign plus a index bits, so w=1+a, R=H+3mw, p=R mod 2, and E=R+p=2k by the premise."},
        {"id": "O2", "status": "PROVED", "proof": "A clause is a consecutive block of L=3w=3(a+1)>=9 payload bits. An interval of seven consecutive bits cannot meet three such blocks: the shortest interval meeting blocks q and q+2 runs from the last bit of q through the first bit of q+2 and has L+2>=11 bits. Thus x[k..k+6] touches at most two clauses."},
        {"id": "O3", "status": "PROVED", "proof": "There are m>=4 clauses and O2 removes at most two touched clauses. Therefore at least m-2>=2 untouched clauses remain."},
        {"id": "O4", "status": "PROVED", "proof": "Choose two untouched clauses A,B and variable 1, legal for every v>=1. C041 permits repeated literals, so A=(x1 OR x1 OR x1) and B=(not x1 OR not x1 OR not x1) are canonical 3-literal clauses for every v in the entire a-cell."},
        {"id": "O5", "status": "PROVED", "proof": "A requires x1=true and B requires x1=false. No assignment satisfies both, independently of every other clause and every literal placed in a touched clause. Hence every constructed parent formula is UNSAT."},
        {"id": "O6", "status": "PROVED", "proof": "If x[k+j-1] is a sign phase, set the target literal sign to epsilon and use variable index 1. The anchor clauses are untouched, so O5 preserves UNSAT for epsilon=0 and epsilon=1."},
        {"id": "O7", "status": "PROVED", "proof": "Fix v in [2^(a-1),2^a-1] and an a-bit index coordinate s counted from the MSB. To realize bit 1 choose q=2^(a-1-s), which lies in [1,2^(a-1)] subset [1,v]. To realize bit 0 choose q=1 unless s is the LSB, and choose q=2 for the LSB. Since a>=2, v>=2; these choices are legal and have the requested bit. Put q in the target touched literal. O5 preserves UNSAT."},
        {"id": "O8", "status": "PROVED", "proof": "Within fixed (a,b,m), signs and legal a-bit indices change only payload content, not MAGIC, gamma fields, token count, R, p, or E. The constructed formula therefore has exact canonical length 2k; splitting it as r||c gives 1||c in H_k because O5 proves UNSAT."},
        {"id": "O9", "status": "PROVED", "proof": "By definition h[0]=1=MAGIC[0]. For each j=1,...,7, O6 or O7 supplies an H_k member for epsilon=MAGIC[j] (indeed for both epsilon values). Therefore no h[j], j=0,...,7, is universally forced unequal to MAGIC[j]."},
        {"id": "O10", "status": "PROVED", "proof": "At (a,b,m)=(2,3,5), H=16,w=3,R=61,p=1,E=62,k=31. The window x[31..37] is payload offsets 15..21. Nine payload bits form each clause, so offsets 15..17 lie in clause 2 and 18..21 in clause 3 (one-based); clauses 1,4,5 are untouched."},
        {"id": "O11", "status": "PROVED", "proof": "E=64 means R is 63 or 64. If m>=9 then already a=1,m=9 gives R>64, so m<=8. Substitution for m=1,...,8 gives respectively R=11+5a,16+8a,19+11a,24+14a,27+17a,30+20a,33+23a,38+26a. The only positive integer solutions at 63 or 64 are (a,m,R,p)=(6,2,64,0),(4,3,63,1),(1,8,64,0), with the asserted full v-ranges."},
        {"id": "O12", "status": "PROVED", "proof": "Among premise cells, (a,m)=(2,4) has E=52 and is the only possible cell below E=62: a=2,m>=5 gives E>=62, while a>=3,m>=4 gives E>=66. Its adjacent length is 54. E=54 requires R in {53,54}; m>=7 gives R>=56 at a=1. For m=1,...,6, R is 11+5a,16+8a,19+11a,24+14a,27+17a,30+20a, none equal 53 or 54 for positive integer a. Thus length 54 has no support, while O10 and O11 give adjacent support at k=31. Hence k=31 is least."},
        {"id": "O13", "status": "PROVED", "proof": "The quantifier order is forall v forall j forall epsilon exists F(v,j,epsilon). The construction may change other bits and may choose a different formula for every triple. It asserts neither a common formula for a joint pattern nor witnesses differing only at j. Legal indices are not a full Boolean cube, so no stronger reading is inferred."},
    ]
    return seal({
        "schema_version": "1.0.0",
        "proof_id": "PNP-C052-V21-OFFWINDOW-SYMBOLIC-HAND-PROOF-20260812",
        "candidate_id": CANDIDATE_ID,
        "atom_id": ATOM_ID,
        "proved_statement": "For every frozen premise cell, every fixed v in its full a-cell, every j=1..7, and every epsilon in {0,1}, an exact canonical UNSAT length-2k parent exists with h[j]=epsilon. Consequently no h[0..7] coordinate is universally forced unequal to MAGIC. With adjacent support this removes only that local coordinate obstruction.",
        "construction_algorithm": [
            "compute H,w,R,p,k and map x[k+j-1] to its payload literal token and phase",
            "mark every clause touched by x[k..k+6] and choose any two untouched clauses A,B",
            "set A to three positive copies of x1 and B to three negative copies of x1",
            "if the target phase is a sign, set it to epsilon with index 1",
            "if it is index bit s, use 2^(a-1-s) for epsilon 1; for epsilon 0 use 2 at the LSB and 1 otherwise",
            "fill remaining literals with any legal literals, encode canonically, append the parity pad, and split at k",
        ],
        "obligations": obligations,
        "all_obligations_proved": all(row["status"] == "PROVED" for row in obligations),
        "marginal_not_independent_caveat": "forall v forall j forall epsilon exists F(v,j,epsilon); no joint-pattern or single-bit-flip claim",
        "scope": ["exact C041 grammar", "a>=2", "m>=4", "x[k..k+6] wholly in unpadded payload", "coordinate-wise marginals only", "k31 public regression"],
        "non_guarantees": ["no H_k intersection P_(k+1) result", "no hidden/native result", "no novelty, circuit lower bound, or P-versus-NP authority"],
        "authority": "SAME_CONTEXT_SYMBOLIC_HAND_PROOF_NOT_FORMAL_NOT_INDEPENDENT",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def check_receipt() -> dict:
    check = checker_module().run_public_check()
    return seal({
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C052-V21-OFFWINDOW-INDEPENDENT-IMPLEMENTATION-CHECK-20260812",
        "candidate_id": CANDIDATE_ID,
        "checker_raw_sha256": file_sha(CHECKER),
        "checker_result": check,
        "verdict": "PASS_ALL_O1_O13" if check["all_obligations_pass"] else "FAIL_OR_CANNOT_CHECK",
        "independence_boundary": "IMPLEMENTATION_DISTINCT_FROM_PROOF_SERIALIZER_BUT_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
        "authority": "COMPUTATIONAL_CORROBORATION_ONLY_NOT_PROOF",
        "forbidden_evaluations_executed": check["forbidden_evaluations_executed"],
    })


def result_receipt(proof: dict, check: dict) -> dict:
    passed = proof["all_obligations_proved"] and check["verdict"] == "PASS_ALL_O1_O13"
    prior_event = json.loads(FREEZE_RECEIPT.read_text(encoding="utf-8"))["public_trace_delta"]
    falsifier_event = {
        "event_id": "O9d12a2a1b-C052-V21-E34",
        "atom_id": ATOM_ID,
        "event_type": "FALSIFIER_RUN",
        "timestamp": RESULT_AT,
        "chronology_order_index": 34,
        "state_summary": "Only authorized O1-O13 and the public k31 regression were checked after authorization merged.",
        "action_summary": "Run the independently reimplemented grammar/length/marginal checker without overlap, native, or hidden evaluation.",
        "evidence_pointers": [str(CHECK_RECEIPT.relative_to(ROOT)), str(CHECKER.relative_to(ROOT))],
        "outputs": [check["artifact_hash"], check["verdict"]],
        "uncertainties": ["computation is corroboration only", "review remains same-context"],
        "residuals": ["overlap remains open", "P-versus-NP root remains open"],
        "next_steps": ["record the result only if symbolic and independent-implementation obligations agree"],
        "previous_event_hash": prior_event["artifact_hash"],
    }
    falsifier_event["artifact_hash"] = canonical_hash(falsifier_event)
    result_event = {
        "event_id": "O9d12a2a1b-C052-V21-E35",
        "atom_id": ATOM_ID,
        "event_type": "RESULT_RECORDED",
        "timestamp": RESULT_AT,
        "chronology_order_index": 35,
        "state_summary": "The frozen marginal lemma survives all exact symbolic obligations and the public k31 regression in its bounded scope.",
        "action_summary": "Record PROVED_EXACT_QUANTIFIED_SCOPE without overlap, hidden, native, circuit, or root escalation.",
        "evidence_pointers": [str(PROOF.relative_to(ROOT)), str(CHECK_RECEIPT.relative_to(ROOT)), str(RESULT.relative_to(ROOT))],
        "outputs": ["PROVED_EXACT_QUANTIFIED_SCOPE", "OPEN_NO_SOLUTION_CERTIFICATE"],
        "uncertainties": ["no independent peer review", "no overlap result"],
        "residuals": ["actual H_k intersection P_(k+1) remains open", "root remains open"],
        "next_steps": ["preserve the result as scoped mathematical experience", "require a separate candidate freeze before any overlap question"],
        "previous_event_hash": falsifier_event["artifact_hash"],
    }
    result_event["artifact_hash"] = canonical_hash(result_event)
    return seal({
        "schema_version": "1.0.0",
        "result_id": "PNP-C052-V21-OFFWINDOW-LEMMA-RESULT-20260812",
        "candidate_id": CANDIDATE_ID,
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_pin": FRAMEWORK_SHA,
        "authorization": {"path": str(AUTHORIZATION.relative_to(ROOT)), "git_blob": AUTHORIZATION_BLOB, "raw_sha256": file_sha(AUTHORIZATION)},
        "source_bindings": {"candidate_raw_sha256": file_sha(CANDIDATE), "proof_artifact_hash": proof["artifact_hash"], "check_artifact_hash": check["artifact_hash"]},
        "result_branch": "PROVED_EXACT_QUANTIFIED_SCOPE" if passed else "CANNOT_CHECK",
        "obligation_status": [{"id": row["id"], "symbolic_proof": row["status"], "independent_check": check["checker_result"]["obligations"][i]["status"]} for i, row in enumerate(proof["obligations"])],
        "public_trace_deltas": [falsifier_event, result_event],
        "exact_mathematical_result": "The off-window UNSAT-anchor marginal lemma holds in its frozen scope. The least adjacent-supported premise cell is k=31 with parent (a,b,m)=(2,3,5), v in {2,3}; its seven-bit window touches clauses 2 and 3, and length 64 has exactly the three frozen current support cells. This proves only absence of a universal unequal coordinate among h[0..7].",
        "public_k31": {"witness_count": check["checker_result"]["k31_witness_count"], "current_support_cell_count": len(check["checker_result"]["length64_current_support_cells"]), "minimality": "PROVED", "status": "PUBLIC_REGRESSION_PASS"},
        "marginal_not_independent_caveat_preserved": True,
        "forbidden_evaluations_executed": [],
        "mathematical_credit": ["scoped symbolic off-window lemma", "explicit UNSAT-preserving construction", "k31 minimal adjacent-support classification"],
        "zero_credit": ["Git/CI/hashes", "computation as proof", "independent review", "overlap/native/hidden/P-versus-NP claims"],
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def review_document(proof: dict, result: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "review_id": "PNP-C052-V21-OFFWINDOW-SAME-CONTEXT-REVIEW-20260812",
        "candidate_id": CANDIDATE_ID,
        "result_artifact_hash": result["artifact_hash"],
        "lenses": {
            "domain_theory": "The contradictory untouched pair preserves UNSAT without assuming ambient syntax equals H_k.",
            "adversarial_quantifiers": "The proof uses forall v forall j forall epsilon exists F; it does not commute the existential or promise isolated bit flips.",
            "formal_methods": "O1-O13 align with the frozen statement; computation independently reimplements grammar but is corroboration only.",
            "research_value": "The result converts a recurring local obstruction into a scoped sufficient escape lemma, not overlap or a lower bound.",
        },
        "strongest_objection": "Index-bit variability could fail near a truncated a-cell; O7 answers this pointwise for every fixed v using explicit legal indices.",
        "blocking_concerns": [],
        "verdict": "SCOPED_RESULT_SURVIVES_SAME_CONTEXT_REVIEW",
        "review_boundary": "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
        "proof_artifact_hash": proof["artifact_hash"],
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def lesson_document(result: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "experience_id": "MATH-PNP-C052-OFFWINDOW-UNSAT-ANCHOR-20260812",
        "atom_id": ATOM_ID,
        "candidate_id": CANDIDATE_ID,
        "result_artifact_hash": result["artifact_hash"],
        "seven_field_mathematical_lesson": {
            "attempted_implication": "A seven-bit payload window with two clauses outside every touched clause should admit H_k-internal marginal variation and remove every local forced-MAGIC coordinate obstruction.",
            "exact_result_or_failure": "The implication is proved in the frozen scope. A seven-bit interval meets at most two clauses because clause width is at least nine; two untouched opposite repeated-unit clauses preserve UNSAT while each sign or index coordinate attains either marginal value. The least adjacent-supported cell is k=31.",
            "supported_and_competing_causes": "Supported cause is semantic decoupling: the untouched contradictory pair carries UNSAT while touched literals vary. Ambient syntax variability, padding arithmetic alone, and adjacent support alone are rejected as causes because none proves H_k membership.",
            "scope": "Exact C041 grammar; a>=2,m>=4; window wholly in unpadded payload; forall v forall j forall epsilon exists formula; public k31 regression. No joint pattern, isolated flip, overlap, native, hidden, circuit, or root claim.",
            "mathematical_falsifier": "A premise cell whose window touches at least three clauses, fewer than two untouched clauses, a fixed v/index bit lacking a legal marginal, rejection of repeated literals by the grammar, or a satisfying assignment to the anchor pair would refute an obligation.",
            "repair_or_next_discriminator": "Use the lemma only as a scoped pruning rule, then freeze a separate candidate before asking whether any escaped cell actually yields H_k intersection P_(k+1); local obstruction escape is not overlap.",
            "proof_and_source_evidence": "Symbolic O1-O13 hand proof plus formula-bound public k31 receipts and an independently reimplemented checker. The checker is corroboration, and the review is same-context rather than independent peer review.",
        },
        "promotion_status": "SCOPED_MATHEMATICAL_EXPERIENCE_NOT_UNIVERSAL_RESEARCH_TOOL",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def build() -> tuple[dict, ...]:
    proof = proof_document()
    check = check_receipt()
    result = result_receipt(proof, check)
    review = review_document(proof, result)
    lesson = lesson_document(result)
    return proof, check, result, review, lesson


def write() -> tuple[dict, ...]:
    values = build()
    for path, value in zip((PROOF, CHECK_RECEIPT, RESULT, REVIEW, LESSON), values):
        path.write_bytes(canonical_bytes(value))
    return values


if __name__ == "__main__":
    write()
