"""Build the C047 result after every proof input was public.

Only the inert record checker is imported.  No decoder, satisfiability solver,
later target, or result-signalling successor branch is accessed.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys


BASE = Path("research/real_math/millennium/p_vs_np")
CERTIFICATE_PATH = BASE / "04_candidates/O9d12a2a1b_C047_ORIENTATION_ONLY_SEPARATION_PROOF_CERTIFICATE_FREEZE_20260812.json"
AUTHORIZATION_PATH = BASE / "09_trace/O9d12a2a1b_C047_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json"
EVALUATOR_PATH = BASE / "05_falsification/c047_orientation_feasibility_evaluator.py"
CANDIDATE_TRACE_PATH = BASE / "09_trace/O9d12a2a1b_C047_CANDIDATE_FREEZE_TRACE_20260812.json"
PRIOR_FAILURE_PATH = BASE / "07_memory/O9d12a2a1b_C045_U17_COUPLING_FAILURE_DELTA_20260812.json"
RESULT_PATH = BASE / "05_falsification/O9d12a2a1b_C047_ORIENTATION_FEASIBILITY_PROOF_CHECK_RESULT_20260812.json"
TRACE_PATH = BASE / "09_trace/O9d12a2a1b_C047_POST_FREEZE_RESULT_TRACE_20260812.json"
FAILURE_PATH = BASE / "07_memory/O9d12a2a1b_C047_ORIENTATION_REPAIR_FAILURE_EXPERIENCE_DELTA_20260812.json"
SATURATION_PATH = BASE / "10_case_study/C047_ORIENTATION_REPAIR_MATHEMATICAL_SATURATION_RECEIPT_20260812.json"
EPISODE_PATH = BASE / "10_case_study/C047_ORIENTATION_REPAIR_TASK_EPISODE_20260812.json"

CANDIDATE_ID = "C047-ORIENTATION-ONLY-SEPARATION-LEMMA-v1"
EVALUATOR_RAW_SHA256 = "28040619b04031d33932203d96fdbb49a0da697c8990e096c9b00bf562a21043"
CERTIFICATE_ARTIFACT_HASH = "sha256:550622d9ab4ad635b253d6a41cbf084974540b748d47d6b360b61684934cbd9c"
AUTHORIZATION_ARTIFACT_HASH = "sha256:1838f134fb0bbb2495ccbbd15a026f05da29b8298d67f8b572c39fad755db12c"
PUBLIC_INPUT_FREEZE_COMMIT = "95ac661de3dce2c100ff9ed34e531becb47d7d92"
PUBLIC_INPUT_OBSERVED_AT = "2026-08-12T03:09:34Z"
EXECUTED_AT = "2026-08-12T03:09:48Z"
RECORDED_AT = "2026-08-12T03:10:00Z"
RAW_OUTPUT_SHA256 = "8de95b41966c74771f74f4dd5831c2c1fcb8d19ff30068428a84348749e3b105"


def _hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _seal(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = ""
    result["artifact_hash"] = _hash(result)
    return result


def _load(root: Path, path: Path) -> dict:
    value = json.loads((root / path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"not a JSON object: {path}")
    return value


def _verify_seal(value: dict, expected: str, label: str) -> None:
    subject = dict(value)
    subject["artifact_hash"] = ""
    if value.get("artifact_hash") != expected or _hash(subject) != expected:
        raise RuntimeError(f"{label} identity changed")


def load_exact_evaluator(root: Path):
    source = root / EVALUATOR_PATH
    if hashlib.sha256(source.read_bytes()).hexdigest() != EVALUATOR_RAW_SHA256:
        raise RuntimeError("frozen evaluator bytes changed")
    spec = importlib.util.spec_from_file_location("pnp_c047_frozen_evaluator", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen evaluator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _event(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = _hash(result)
    return result


def build_documents(root: Path) -> dict[str, dict]:
    certificate = _load(root, CERTIFICATE_PATH)
    authorization = _load(root, AUTHORIZATION_PATH)
    _verify_seal(certificate, CERTIFICATE_ARTIFACT_HASH, "certificate")
    _verify_seal(authorization, AUTHORIZATION_ARTIFACT_HASH, "authorization")
    if authorization.get("certificate_artifact_hash") != CERTIFICATE_ARTIFACT_HASH:
        raise RuntimeError("authorization is not bound to certificate")
    evaluator = load_exact_evaluator(root)
    evaluator_output = evaluator.evaluate_certificate(certificate, authorization)
    if evaluator_output != {"verdict": "PASS", "candidate_id": CANDIDATE_ID}:
        raise RuntimeError(f"unexpected frozen evaluator output: {evaluator_output}")

    result = _seal({
        "schema_version": "1.0.0",
        "result_id": "PNP-C047-ORIENTATION-FEASIBILITY-PROOF-CHECK-RESULT-20260812",
        "atom_id": "O9d12a2a1b-C047",
        "candidate_id": CANDIDATE_ID,
        "status": "PASS_SAME_CONTEXT_CERTIFICATE_RECORD_CHECK",
        "execution": {"executed_at": EXECUTED_AT, "evaluator_path": str(EVALUATOR_PATH), "evaluator_raw_sha256": EVALUATOR_RAW_SHA256, "operation": "evaluate_certificate(exact_certificate, exact_public_authorization)", "network_used": False, "raw_output_sha256": RAW_OUTPUT_SHA256},
        "chronology": {
            "pre_candidate_public_commit": "d84e3814f1d8f355246f2bddb6982c3a1859fb6c",
            "candidate_evaluator_public_commit": "e033df7a4f0276abb218027451754695679ec288",
            "public_proof_input_freeze": {"pull_request": 260, "url": "https://github.com/SzeChunYiu/RAKL_math/pull/260", "remote_head_sha": PUBLIC_INPUT_FREEZE_COMMIT, "observed_at": PUBLIC_INPUT_OBSERVED_AT},
            "evaluation_strictly_after_public_input_freeze": PUBLIC_INPUT_OBSERVED_AT < EXECUTED_AT,
        },
        "inputs": {"certificate": {"path": str(CERTIFICATE_PATH), "artifact_hash": CERTIFICATE_ARTIFACT_HASH}, "authorization": {"path": str(AUTHORIZATION_PATH), "artifact_hash": AUTHORIZATION_ARTIFACT_HASH}},
        "evaluator_output": evaluator_output,
        "obligation_summary": {"required_count": 5, "proved_record_count": 5, "obligation_ids": [item["obligation_id"] for item in certificate["obligations"]], "all_evidence_pointers_nonempty": all(bool(item.get("evidence_pointer")) for item in certificate["obligations"])},
        "mathematical_result": {
            "lemma": "For every n>=18, neither the prefix-preserving new-old mirror nor its union with the original old-new block has a complement row equal to a current canonical MAGIC n-bit prefix.",
            "proof_core": ["old/inherited rows begin 0", "the all-zero fresh row begins 10", "a canonical prefix-mirror row begins 1||MAGIC=1111...", "a current canonical prefix begins MAGIC=1110..."],
            "failed_repair": "quadrant orientation alone, with prefix r kept as the fresh-row coordinate",
            "bounded_failure_cause": "the fresh leading bit shifts the fixed MAGIC header; coarse high-half occupancy therefore fails exact interface congruence",
            "repair_condition": "a successor must change the label map or split (for example test suffix-to-row literal transpose) and separately preserve the NP language/reduction before coupling can be viable",
        },
        "interpretation": {"passed": "The exact inert evaluator accepted five present PROVED obligation records with evidence pointers.", "mathematical_reading": "The same-context hand derivation gives a scoped symbolic impossibility for mirror-only and two-sided prefix-preserving orientation repair.", "formal_proof_checked": False, "semantic_derivation_independently_checked": False, "evaluator_checks_record_completeness_not_derivation_semantics": True},
        "target_access": {"proof_obligation_evaluator_imported_and_executed": True, "target_decoder_imported_or_executed": False, "later_target_enumerated": False, "later_target_result_accessed": False, "finite_collision_level_selected": False},
        "residuals": ["literal matrix transpose with suffix c on the fresh row", "header-aligning relabelling or unequal/overlapping split with language preservation", "independent mathematical review", "formal proof and bounded novelty review", "cover/circuit bridge and P-versus-NP root"],
        "authority": {"same_context_hand_derivation_record_check": True, "theorem_truth": False, "formal_proof": False, "independent_review": False, "novelty": False, "cover_or_circuit_lower_bound": False, "p_vs_np_authority": False, "root_status": "OPEN"},
    })

    prior_failure = _load(root, PRIOR_FAILURE_PATH)["experiences"][0]
    c047_experience = _seal({
        "failure_id": "F-PNP-C047-ORIENTATION-ONLY-INTERFACE-MISALIGNMENT",
        "atom_id": "O9d12a2a1b-C047",
        "candidate_id": "C047-PREFIX-PRESERVING-MIRROR-OR-TWO-SIDED-REPAIR",
        "context_packet_hash": _load(root, BASE / "01_frontier/O9d12a2a1b_C047_MATH_CONTEXT_FIBER_20260812.json")["packet_hash"],
        "research_trace_event_id": "O9d12a2a1b-C047-E11",
        "method_family": "repair recursive complement interaction by moving or copying the decoded prefix coordinate from old rows to fresh rows",
        "failure_mode": "The repair reaches the correct coarse high half but cannot reuse a current canonical prefix row: prepending the fresh bit shifts MAGIC from 1110... to 1111..., while the all-zero exception begins 10.",
        "residual_signature": ["coarse partition obstruction removed", "exact binary interface remains disjoint", "mirror-only and two-sided variants both fail", "literal transpose/suffix-row and relabelling remain untested"],
        "broken_assumptions": ["fresh-row high-half occupancy was treated as sufficient for row reuse", "mirroring quadrant placement was treated as mirroring the full coordinate interface", "bidirectional support presence was treated as sufficient for mathematical interaction"],
        "scope_conditions": ["exact C041 total decoder and MAGIC=11100101", "equal prefix/suffix split", "prefix coordinate r placed as fresh row M+r", "mirror-only or union with original old-new block", "n>=18", "no statement about literal transpose, relabelling, cover growth, circuits, or P versus NP"],
        "competing_diagnoses": ["fixed-header one-bit shift causes exact disjointness", "the all-zero fallback creates a hidden collision", "an inherited row enters the current high half", "literal transpose was silently conflated with prefix-preserving mirror", "C046's interaction diagnosis was wrong"],
        "selected_diagnosis": "SUPPORTED BOUNDED MATHEMATICAL CAUSE: within the frozen orientation-only class, the exact label map prepends one to the prior prefix. Exhaustive decoder branches then yield only low rows, 10..., or 1||MAGIC=1111..., each symbolically disjoint from current MAGIC=1110.... This specializes the atlas interaction/interface-loss class without identifying a cause for all possible successor families.",
        "diagnosis_status": "SUPPORTED",
        "evidence_pointers": [str(CERTIFICATE_PATH), str(RESULT_PATH), str(SATURATION_PATH), "research/real_math/millennium/cross_problem/07_memory/GLOBAL_MATHEMATICAL_FAILURE_CAUSE_ATLAS_20260812.json#FM-PNP-C043-C046-SEMANTICS-WITHOUT-INTERACTION"],
        "falsifier_or_attempt": "Exhibit, under the exact frozen decoder and prefix-to-fresh-row map, a supported row outside the three classes or equality between any class header and current MAGIC; alternatively show the family definition actually uses suffix c or relabelling.",
        "observed_result": "The symbolic trichotomy closes all frozen cases and the record checker passed after public input freeze; no later target was enumerated.",
        "local_repair_attempts": ["next test literal transpose with suffix c on the fresh row as a distinct atom", "require an exact label-interface collision witness before cover evaluation", "audit language/reduction preservation for every relabelling or split change"],
        "timestamp": RECORDED_AT,
    })
    failure = {
        "experiences": [prior_failure, c047_experience],
        "links": [{"source_id": c047_experience["failure_id"], "target_id": prior_failure["failure_id"], "relation": "CONTEXT_SPECIALIZATION_OF", "rationale": "C047 tests one explicit orientation repair proposed after C045/C046 and proves that this subfamily still lacks the exact row-interface interaction required for backward coupling.", "evidence_pointers": [str(CERTIFICATE_PATH), str(PRIOR_FAILURE_PATH)]}],
    }

    saturation = _seal({
        "atom_id": "O9d12a2a1b-C047",
        "candidate_id": CANDIDATE_ID,
        "round_kind": "BOUNDED_CANONICAL_MATHEMATICAL_SATURATION",
        "mathematical_credit": {"orientation_only_impossibility_lemma": True, "exact_binary_header_falsifier": True, "bounded_broken_assumption_and_repair_condition": True, "software_schema_hash_chronology_ci_pr_credit": 0},
        "lesson": "Changing a recursive construction into the correct coarse row half is not enough to restore interaction. Under the frozen equal split and prefix-to-fresh-row map, the generated header is shifted to 1||MAGIC=1111..., while the required current prefix remains MAGIC=1110...; exact interface congruence, not quadrant occupancy, is the load-bearing condition.",
        "failure_cause": {"status": "SUPPORTED_BOUNDED", "cause": "prefix-preserving quadrant mirroring shifts the fixed header and leaves the exact row languages disjoint", "atlas_relation": "CONTEXT_SPECIALIZATION_OF FM-PNP-C043-C046-SEMANTICS-WITHOUT-INTERACTION", "unique_global_cause_claimed": False},
        "framework_feedback": {"status": "PROPOSAL_ONLY_APPLICATION_FEEDBACK", "proposal": "After a coarse structural repair, require a fine-interface congruence witness before target enumeration or downstream evaluation.", "framework_change_requested": False, "framework_authority": "NONE", "fresh_self_rakl_assurance_required": True},
        "scope": ["mirror-only and two-sided prefix-preserving orientation variants", "n>=18 and exact C041 decoder", "literal transpose and relabelled/split-changing families remain open", "no cover/circuit lower bound or novelty claim", "same-context review is not independent review"],
        "residual": "C048 should test suffix-to-fresh-row literal transpose or a separately frozen header-aligned label map, with an exact language/reduction preservation witness before any target access.",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
        "root_authority": "NONE",
    })
    episode = _seal({
        "schema_version": "1.0.0",
        "episode_id": "PNP-C047-ORIENTATION-REPAIR-TASK-EPISODE-20260812",
        "atom_id": "O9d12a2a1b-C047",
        "action_trace": ["froze context, dual memory, shortcut review, expert cell, and hash-chained trace before candidate", "publicly froze exact candidate and inert evaluator", "publicly froze hand certificate and narrow authorization", "executed only the inert record checker", "recorded symbolic lemma, failed repair, bounded cause, residual, and authority limits"],
        "mathematical_success": "proved a scoped interface-disjointness lemma for two orientation-only variants",
        "mathematical_failure": "the smallest prefix-preserving mirror/two-sided repair does not restore canonical row collision",
        "why_it_failed": "quadrant change repairs only the leading half bit; it shifts rather than aligns the fixed MAGIC header",
        "how_to_improve_problem_search": ["separate literal transpose from informal mirror terminology", "require exact source-to-target coordinate mapping", "test label-language intersection symbolically before target enumeration", "preserve language and reduction under any label-map change"],
        "next_atom": "target-blind suffix-to-fresh-row literal-transpose feasibility with language-preservation witness",
        "authority": {"same_context": True, "independent_review": False, "formal_proof": False, "root_status": "OPEN_NO_SOLUTION_CERTIFICATE"},
        "evidence_pointers": [str(CERTIFICATE_PATH), str(RESULT_PATH), str(FAILURE_PATH), str(SATURATION_PATH)],
    })

    prior_trace = _load(root, CANDIDATE_TRACE_PATH)
    entries = list(prior_trace["entries"])
    falsifier = _event({"event_id": "O9d12a2a1b-C047-E10", "atom_id": "O9d12a2a1b-C047", "event_type": "FALSIFIER_RUN", "timestamp": EXECUTED_AT, "state_summary": "All exact proof inputs were public at PR 260 head 95ac661 before the inert evaluator ran.", "action_summary": "Check five frozen symbolic obligations without decoder or target access.", "evidence_pointers": [str(CERTIFICATE_PATH), str(AUTHORIZATION_PATH), str(RESULT_PATH)], "alternatives_considered": ["enumerate later targets", "weaken scope", "run exact record checker"], "decision_rationale": "Only the record check preserves the frozen target-blind chronology.", "outputs": ["PASS", result["artifact_hash"], "TARGET_RESULT_UNACCESSED"], "uncertainties": ["record checker does not verify derivation semantics", "same-context review is not independent"], "residuals": ["literal transpose and relabelling open", "root OPEN"], "next_steps": ["record narrow result and failed repair", "open residual without target access"], "previous_event_hash": entries[-1]["artifact_hash"]})
    entries.append(falsifier)
    recorded = _event({"event_id": "O9d12a2a1b-C047-E11", "atom_id": "O9d12a2a1b-C047", "event_type": "RESULT_RECORDED", "timestamp": RECORDED_AT, "state_summary": "The scoped orientation-only separation lemma is supported by a complete hand derivation and exact record PASS; the proposed mirror/two-sided repair fails.", "action_summary": "Record the mathematical lemma, broken assumption, bounded failure cause, and zero root authority.", "evidence_pointers": [str(RESULT_PATH), str(FAILURE_PATH), str(SATURATION_PATH)], "alternatives_considered": ["call high-half occupancy a successful repair", "generalize to all mirrored families", "record only the exact scoped impossibility"], "decision_rationale": "Exact headers prove only the third conclusion; broader variants are outside the frozen family.", "outputs": ["SCOPED_ORIENTATION_ONLY_IMPOSSIBILITY", "SUPPORTED_BOUNDED_FAILURE_CAUSE", "ROOT_OPEN"], "uncertainties": ["independent/formal/novelty checks absent"], "residuals": ["suffix-row transpose", "header-aligned label map", "cover/circuit bridges"], "next_steps": ["open a fresh strict atom for literal transpose", "require language/reduction preservation before candidate"], "previous_event_hash": entries[-1]["artifact_hash"]})
    entries.append(recorded)
    residual = _event({"event_id": "O9d12a2a1b-C047-E12", "atom_id": "O9d12a2a1b-C047", "event_type": "RESIDUAL_OPENED", "timestamp": "2026-08-12T03:10:01Z", "state_summary": "Orientation-only prefix placement is closed negatively; repairs that change the label interface remain open.", "action_summary": "Open C048 only as a target-blind literal-transpose or header-aligned label-map feasibility atom.", "evidence_pointers": [str(FAILURE_PATH), str(EPISODE_PATH)], "alternatives_considered": ["repeat prefix mirror", "enumerate targets", "change the interface with preservation obligations"], "decision_rationale": "The proven residual is exact header mismatch, so the next action must change that coordinate rather than repeat quadrant placement.", "outputs": ["C048_PROPOSED_TARGET_BLIND", "NO_TARGET_ACCESS"], "uncertainties": ["suffix language may still fail to align", "NP reduction preservation under relabelling is unproved"], "residuals": ["exact label-interface construction", "language preservation", "root OPEN"], "next_steps": ["freeze a new C048 context before candidate generation"], "previous_event_hash": entries[-1]["artifact_hash"]})
    entries.append(residual)
    trace = {"trace_id": "PNP-O9d12a2a1b-C047-POST-FREEZE-RESULT-TRACE-20260812", "entries": entries}
    return {"result": result, "failure": failure, "saturation": saturation, "episode": episode, "trace": trace}


if __name__ == "__main__":
    repository_root = Path(__file__).resolve().parents[5]
    print(json.dumps(build_documents(repository_root), indent=2, sort_keys=True))
