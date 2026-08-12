"""Build the C046 proof-obligation result after its inputs were public.

This fixture imports only the already-frozen inert evaluator.  It never imports
the target decoder, enumerates a later target, or selects a collision level.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys


BASE = Path("research/real_math/millennium/p_vs_np")
CERTIFICATE_PATH = BASE / "04_candidates/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_PROOF_CERTIFICATE_FREEZE_20260812.json"
AUTHORIZATION_PATH = BASE / "09_trace/O9d12a2a1b_C046_POST_FREEZE_PROOF_CHECK_AUTHORIZATION_20260812.json"
EVALUATOR_PATH = BASE / "05_falsification/c046_high_half_separation_evaluator.py"
CANDIDATE_TRACE_PATH = BASE / "09_trace/O9d12a2a1b_C046_CANDIDATE_FREEZE_TRACE_20260812.json"
RESULT_PATH = BASE / "05_falsification/O9d12a2a1b_C046_HIGH_HALF_SEPARATION_PROOF_CHECK_RESULT_20260812.json"
TRACE_PATH = BASE / "09_trace/O9d12a2a1b_C046_POST_FREEZE_RESULT_TRACE_20260812.json"

CANDIDATE_ID = "C046-HIGH-HALF-SEPARATION-LEMMA-v1"
EVALUATOR_RAW_SHA256 = "c45fd7a7e8fc05f61ef653a07c3882c1c33fbf878a98391646c8db0338a65193"
CERTIFICATE_ARTIFACT_HASH = "sha256:275241364fc0136bc18f74a341704514690bae687bb163caa221f8e3a2dcd47f"
AUTHORIZATION_ARTIFACT_HASH = "sha256:b2290b278f872538a3656fed585d23961dee8f3cd576f746d1a0f126e3f5758b"
PUBLIC_INPUT_FREEZE_COMMIT = "ae9c196d3f879ba6b1140af0878a416cf16df6c0"
PUBLIC_INPUT_OBSERVED_AT = "2026-08-12T02:29:52Z"
EXECUTED_AT = "2026-08-12T02:32:55Z"
RECORDED_AT = "2026-08-12T02:33:01Z"
RAW_OUTPUT_SHA256 = "e0e536c9c6a5460f4bd36069f9455fe3ff87b548ab44ffd9c63cb03f1d3dd23a"


def _hash(value: dict) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _seal(value: dict) -> dict:
    sealed = dict(value)
    sealed["artifact_hash"] = ""
    sealed["artifact_hash"] = _hash(sealed)
    return sealed


def _load(root: Path, path: Path) -> dict:
    value = json.loads((root / path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"not a JSON object: {path}")
    return value


def _verify_seal(value: dict, expected: str, label: str) -> None:
    if value.get("artifact_hash") != expected:
        raise RuntimeError(f"{label} declared artifact hash changed")
    candidate = dict(value)
    candidate["artifact_hash"] = ""
    if _hash(candidate) != expected:
        raise RuntimeError(f"{label} canonical content changed")


def load_exact_evaluator(root: Path):
    source = root / EVALUATOR_PATH
    if hashlib.sha256(source.read_bytes()).hexdigest() != EVALUATOR_RAW_SHA256:
        raise RuntimeError("frozen evaluator bytes changed")
    spec = importlib.util.spec_from_file_location("pnp_c046_frozen_evaluator", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen evaluator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _event(payload: dict) -> dict:
    event = dict(payload)
    event["artifact_hash"] = _hash(event)
    return event


def build_documents(root: Path) -> dict[str, dict]:
    certificate = _load(root, CERTIFICATE_PATH)
    authorization = _load(root, AUTHORIZATION_PATH)
    _verify_seal(certificate, CERTIFICATE_ARTIFACT_HASH, "certificate")
    _verify_seal(authorization, AUTHORIZATION_ARTIFACT_HASH, "authorization")
    if certificate.get("candidate_id") != CANDIDATE_ID:
        raise RuntimeError("certificate candidate identity changed")
    if authorization.get("certificate_artifact_hash") != CERTIFICATE_ARTIFACT_HASH:
        raise RuntimeError("authorization is not bound to the exact certificate")
    if authorization.get("evaluator_raw_sha256") != EVALUATOR_RAW_SHA256:
        raise RuntimeError("authorization is not bound to the exact evaluator")

    evaluator = load_exact_evaluator(root)
    evaluator_output = evaluator.evaluate_certificate(certificate, authorization)
    if evaluator_output.get("verdict") != "PASS":
        raise RuntimeError(f"frozen C046 proof-obligation evaluation did not pass: {evaluator_output}")

    result = _seal(
        {
            "schema_version": "1.0.0",
            "result_id": "PNP-C046-HIGH-HALF-SEPARATION-PROOF-CHECK-RESULT-20260812",
            "atom_id": "O9d12a2a1b-C046",
            "candidate_id": CANDIDATE_ID,
            "status": "PASS_SAME_CONTEXT_CERTIFICATE_RECORD_CHECK",
            "execution": {
                "executed_at": EXECUTED_AT,
                "evaluator_path": str(EVALUATOR_PATH),
                "evaluator_raw_sha256": EVALUATOR_RAW_SHA256,
                "operation": "evaluate_certificate(exact_certificate, exact_post_freeze_authorization)",
                "network_used": False,
                "raw_output_sha256": RAW_OUTPUT_SHA256,
            },
            "chronology": {
                "candidate_evaluator_and_no_execution_authorization_freeze_commit": "c76177457d6c75189b7cc80a3ccc012cb9f1e655",
                "public_freeze_chronology_commit": "68a0d8bcd4a13a351bb10738dc36ede1a97204e8",
                "public_proof_input_freeze": {
                    "pull_request": 244,
                    "url": "https://github.com/SzeChunYiu/RAKL_math/pull/244",
                    "remote_head_sha": PUBLIC_INPUT_FREEZE_COMMIT,
                    "observed_at": PUBLIC_INPUT_OBSERVED_AT,
                },
                "evaluation_strictly_after_public_input_freeze": PUBLIC_INPUT_OBSERVED_AT < EXECUTED_AT,
            },
            "inputs": {
                "certificate": {
                    "path": str(CERTIFICATE_PATH),
                    "artifact_hash": CERTIFICATE_ARTIFACT_HASH,
                },
                "authorization": {
                    "path": str(AUTHORIZATION_PATH),
                    "artifact_hash": AUTHORIZATION_ARTIFACT_HASH,
                },
            },
            "evaluator_output": evaluator_output,
            "obligation_summary": {
                "required_count": 4,
                "proved_record_count": 4,
                "obligation_ids": [record["obligation_id"] for record in certificate["obligations"]],
                "all_evidence_pointers_nonempty": all(
                    bool(record.get("evidence_pointer")) for record in certificate["obligations"]
                ),
            },
            "interpretation": {
                "passed": "The exact frozen evaluator accepted the exact certificate because all four frozen obligation records were present, marked PROVED, and carried nonempty evidence pointers under the exact post-freeze token.",
                "mathematical_reading": "The same-context direct derivation supports the high-half separation candidate and eliminates the need to enumerate a later collision target inside the frozen one-sided family, subject to source identity and proof review.",
                "formal_proof_checked": False,
                "semantic_derivation_independently_checked": False,
                "evaluator_checks_record_completeness_not_derivation_semantics": True,
            },
            "target_access": {
                "proof_obligation_evaluator_imported_and_executed": True,
                "target_decoder_imported_or_executed": False,
                "later_target_enumerated": False,
                "later_target_result_accessed": False,
                "finite_collision_level_selected": False,
            },
            "residuals": [
                "independent mathematical review of the direct derivation is still absent",
                "formal proof is absent",
                "novelty is unchecked",
                "no cover or circuit lower bound follows",
                "the P-versus-NP root remains open",
            ],
            "authority": {
                "same_context_hand_derivation_record_check": True,
                "theorem_truth": False,
                "formal_proof": False,
                "independent_review": False,
                "novelty": False,
                "cover_or_circuit_lower_bound": False,
                "p_vs_np_authority": False,
                "root_status": "OPEN",
            },
        }
    )

    prior_trace = _load(root, CANDIDATE_TRACE_PATH)
    entries = list(prior_trace["entries"])
    falsifier_run = _event(
        {
            "event_id": "O9d12a2a1b-C046-E10",
            "atom_id": "O9d12a2a1b-C046",
            "event_type": "FALSIFIER_RUN",
            "timestamp": EXECUTED_AT,
            "state_summary": "The exact proof certificate and narrow post-freeze authorization were publicly visible at PR 244 head ae9c196 before the inert evaluator was imported or executed.",
            "action_summary": "Run the exact frozen record-completeness evaluator on the exact public proof certificate; do not import the target decoder or enumerate any later target.",
            "evidence_pointers": [str(CERTIFICATE_PATH), str(AUTHORIZATION_PATH), str(RESULT_PATH)],
            "alternatives_considered": ["enumerate a later target", "change an obligation after exposure", "run the exact inert proof check"],
            "decision_rationale": "Only the third action preserves the public candidate/evaluator chronology and the target-access boundary.",
            "outputs": ["PASS", result["artifact_hash"], "TARGET_RESULT_UNACCESSED"],
            "uncertainties": ["the evaluator checks certificate records rather than proof semantics", "same-context execution is not independent review"],
            "residuals": ["formal and independent proof checks remain absent", "root OPEN"],
            "next_steps": ["record the narrow PASS without theorem inflation", "rerun exact CI", "do not enumerate later targets"],
            "previous_event_hash": entries[-1]["artifact_hash"],
        }
    )
    entries.append(falsifier_run)
    result_recorded = _event(
        {
            "event_id": "O9d12a2a1b-C046-E11",
            "atom_id": "O9d12a2a1b-C046",
            "event_type": "RESULT_RECORDED",
            "timestamp": RECORDED_AT,
            "state_summary": "C046's exact certificate-record evaluator returned PASS after public exposure of all frozen inputs; the target remained unaccessed.",
            "action_summary": "Record the PASS with the evaluator's narrow semantics and preserve all non-authority boundaries.",
            "evidence_pointers": [str(RESULT_PATH), str(TRACE_PATH)],
            "alternatives_considered": ["promote theorem truth", "claim a circuit consequence", "record a same-context certificate-record PASS only"],
            "decision_rationale": "The evaluator validates obligation-record completeness, not derivation semantics, formality, novelty, or P-versus-NP consequences, so only the narrow result is supportable.",
            "outputs": ["PASS_SAME_CONTEXT_CERTIFICATE_RECORD_CHECK", "TARGET_RESULT_UNACCESSED", "ROOT_OPEN"],
            "uncertainties": ["independent mathematical review absent", "formal proof absent", "novelty unchecked"],
            "residuals": ["C046 requires independent proof review for stronger authority", "P-versus-NP root OPEN"],
            "next_steps": ["merge latest main before merge-readiness CI", "request independent review if stronger lemma authority is desired", "do not search later finite collision targets in this lane without reopening the frozen family assumptions"],
            "previous_event_hash": entries[-1]["artifact_hash"],
        }
    )
    entries.append(result_recorded)
    trace = {
        "trace_id": "PNP-O9d12a2a1b-C046-POST-FREEZE-RESULT-TRACE-20260812",
        "entries": entries,
    }
    return {"result": result, "trace": trace}


if __name__ == "__main__":
    repository_root = Path(__file__).resolve().parents[5]
    print(json.dumps(build_documents(repository_root), indent=2, sort_keys=True))
