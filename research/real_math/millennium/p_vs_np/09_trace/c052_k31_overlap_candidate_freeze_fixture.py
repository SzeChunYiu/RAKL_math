"""Serialize inert C052 k31 overlap discriminator/falsifier identities.

No certificate, label, formula, evaluator implementation, SAT/UNSAT check,
overlap comparison, or evaluated result is produced by this module.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
CANDIDATE_OUT = PNP / "04_candidates/O9d12a2a1b_C052_K31_OVERLAP_DISCRIMINATOR_IDENTITY_20260812.json"
FALSIFIER_OUT = PNP / "05_falsification/O9d12a2a1b_C052_K31_OVERLAP_FALSIFIER_IDENTITY_20260812.json"
RECEIPT_OUT = PNP / "09_trace/O9d12a2a1b_C052_K31_OVERLAP_CANDIDATE_FREEZE_RECEIPT_20260812.json"

APPLICATION_BASE_SHA = "8b05d8248c68b7fe80e42cb202f0129d55df751e"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
CANDIDATE_FROZEN_AT = "2026-08-12T14:52:38Z"
FALSIFIER_FROZEN_AT = "2026-08-12T14:52:39Z"
RECEIPT_FROZEN_AT = "2026-08-12T14:52:40Z"
CANDIDATE_ID = "PNP-C052-K31-TARGET-BLIND-OVERLAP-CERTIFICATE-DISCRIMINATOR-v1"
FALSIFIER_ID = "PNP-C052-K31-OVERLAP-CERTIFICATE-FALSIFIER-v1"
PREVIOUS_EVENT_HASH = "sha256:cad6a71070adf7deffcdf0af98b374878c235576381f429efbcecda0ed16537c"

SOURCE_BINDINGS = {
    "context": {
        "path": "research/real_math/millennium/p_vs_np/01_frontier/O9d12a2a1b_C052_K31_OVERLAP_CONTEXT_20260812.json",
        "raw_sha256": "sha256:f3a8dd3efbdfb034b1549341f51c47bf417d9d10c5e301caad76dda19f2b215b",
        "content_hash": "sha256:9b195fe641a94855ac068e8aec4d20c55a051b377e5f91b22e57944036391482",
        "git_blob": "e57537977dc8bffbac8ce61a8e43114f291c75bd",
    },
    "memory_review": {
        "path": "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C052_K31_OVERLAP_RESEARCH_MEMORY_REVIEW_20260812.json",
        "raw_sha256": "sha256:b5bc34335f5e15677bd8ea4f44e23fdcb7313cf10c6d0bb04c6643bef82304ea",
        "content_hash": "sha256:d5da74964ed9e9815fb65af1a516191788c2ec7be50e5464c75a432f8dffa0cd",
        "git_blob": "1d2833f43fa24686058c87d4e8893ce354aa15dc",
    },
    "shortcut_review": {
        "path": "research/real_math/millennium/p_vs_np/08_reviews/O9d12a2a1b_C052_K31_OVERLAP_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
        "raw_sha256": "sha256:90ef5bc08757da741badcb36752fdaa4e0c0ed59603714ecdc9cec2f7e9ddec6",
        "content_hash": "sha256:06285109d6c733336517015041a6f1959516f9cb17ee9add7cdcae60cc76e74a",
        "git_blob": "cebfebca050bafc63acd7415ef3a6fb04181e458",
    },
    "certificate_firewall": {
        "path": "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C052_K31_OVERLAP_CERTIFICATE_FIREWALL_20260812.json",
        "raw_sha256": "sha256:cb2501908327ec03a0a103691f824e06514616e04fda170b6803eef4935da971",
        "content_hash": "sha256:fda8088b8bde32488f9a9e18096f2c2e6d1b61bd23a36b74996dc74acd045103",
        "git_blob": "276a35919a72ebc1d9b68115cbf8a85dc0c0236a",
    },
    "pre_candidate_trace": {
        "path": "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C052_K31_OVERLAP_PRE_CANDIDATE_TRACE_20260812.json",
        "raw_sha256": "sha256:b53fc0311ad4d49e6f89938b306d788785f9b6290d192261a6fafdbcb044b5f1",
        "last_event_id": "O9d12a2a1b-C052-K31-OVERLAP-E08",
        "last_event_hash": PREVIOUS_EVENT_HASH,
        "git_blob": "ce564addfb9c432c14703c1a630fe9a630a6fd2f",
    },
    "pre_candidate_gate": {
        "path": "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C052_K31_OVERLAP_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
        "raw_sha256": "sha256:14ff95e6a48cd51e74824530f61292ec9e5276f72a6c66132d8a184b3d7f6f83",
        "content_hash": "sha256:6749bd81c19e691c7089808fb252bffef86c5397a066a3fb8844c82ce84e3ead",
        "git_blob": "7f6d27e7e08a6e1e4b9254c490498ddde10bca1a",
    },
    "c041_grammar": {
        "path": "research/real_math/millennium/p_vs_np/04_candidates/C041_fx_sat_one_sided.py",
        "raw_sha256": "sha256:c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a",
        "git_blob": "fcc4814dd618da96ef9bb8144a4783a0a6e886e1",
    },
    "c048_transfer_condition": {
        "path": "research/real_math/millennium/p_vs_np/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_TRANSFER_CONDITION_FREEZE_20260812.json",
        "raw_sha256": "sha256:e2a924e708c1ab17b78e06a3935fd48772c0c172b9f01b0c756de80f1430908b",
        "content_hash": "sha256:b03a1090e7b25222dc2377e309b8600b6e2064d6fc74f702b1f3f984d68cff5e",
        "git_blob": "fed9057163bec46325115e8f6cfbb5c6f3c3d485",
    },
    "c048_proof_certificate": {
        "path": "research/real_math/millennium/p_vs_np/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_PROOF_CERTIFICATE_FREEZE_20260812.json",
        "raw_sha256": "sha256:fd4d478d816c50423f2d6fbd668305bec911bcf3a035a2a5b516eb08796ec16c",
        "content_hash": "sha256:84ebf84c9b90a99c3f5e348bacad53ee1d700e2d0c746805cf4b8a0439cd1e33",
        "git_blob": "1283219dec4d6a39cf43d5f2d9a4fafa1883d016",
    },
}


def digest(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def seal(document: dict) -> dict:
    core = dict(document)
    core.pop("artifact_hash", None)
    core["artifact_hash"] = digest(
        json.dumps(core, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    )
    return core


def assert_sources() -> None:
    for binding in SOURCE_BINDINGS.values():
        path = ROOT / binding["path"]
        if digest(path.read_bytes()) != binding["raw_sha256"]:
            raise RuntimeError(f"bound source moved: {binding['path']}")
        if "content_hash" in binding:
            document = json.loads(path.read_text(encoding="utf-8"))
            actual = document.get("artifact_hash", document.get("packet_hash"))
            if actual != binding["content_hash"]:
                raise RuntimeError(f"bound content hash moved: {binding['path']}")
    trace = json.loads((ROOT / SOURCE_BINDINGS["pre_candidate_trace"]["path"]).read_text(encoding="utf-8"))
    if trace["entries"][-1]["artifact_hash"] != PREVIOUS_EVENT_HASH:
        raise RuntimeError("pre-candidate trace tip moved")


def candidate_identity() -> dict:
    return seal({
        "schema_version": "1.0.0",
        "candidate_id": CANDIDATE_ID,
        "atom_id": "O9d12a2a1b-C052-K31-OVERLAP",
        "candidate_kind": "INERT_TARGET_BLIND_EXACT_CERTIFICATE_DISCRIMINATOR_IDENTITY",
        "frozen_at_utc": CANDIDATE_FROZEN_AT,
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_pin": FRAMEWORK_SHA,
        "source_bindings": SOURCE_BINDINGS,
        "qoi": "Decide exact H_31 intersection P_32 only from a source-bound complete positive or negative certificate.",
        "target_blindness": {
            "target_result_used_to_choose_identity": False,
            "overlap_label_or_branch_included": False,
            "public_marginal_witnesses_used_as_overlap_candidates": False,
            "same branch rules apply before any certificate content is accessed": True,
        },
        "architecture": {
            "frontend": "rederive exact source identities, formula-bound memberships, proof completeness, and full 32-bit equality/separation",
            "decision_kernel_input": ["source_binding_valid", "positive_certificate_complete_and_valid", "negative_certificate_complete_and_valid", "malformed_or_ambiguous"],
            "integration_obligation": "the full discriminator must invoke the exact kernel identity and propagate its branch without caller-supplied authority booleans",
            "standalone_kernel_worlds_are_insufficient": True,
        },
        "positive_certificate_obligations": [
            "P1 exact C041/C048 and pre-candidate source identities match",
            "P2 one exact canonical length-62 parent word lies in the frozen (a,b,m,v) support cell",
            "P3 the parent word is decoded to a formula-bound C041 3CNF and an independently checkable proof establishes UNSAT",
            "P4 split the exact parent word as r||c with |r|=|c|=31 and derive the 32-bit label h=1||c",
            "P5 one exact canonical length-64 current word lies in one of the three frozen current support cells",
            "P6 derive its exact 32-bit prefix p and check byte-for-byte h=p",
            "P7 bind the common label to the unchanged C048 literal-transpose collision equivalence",
        ],
        "negative_certificate_obligations": [
            "N1 exact C041/C048 and pre-candidate source identities match",
            "N2 quantify the complete frozen parent cell including every canonical formula and semantic UNSAT membership",
            "N3 quantify all three frozen current cells including every canonical current formula",
            "N4 provide either a universal invariant separating every H_31 member from every P_32 member or an exhaustive enumeration with proof of completeness",
            "N5 independently check that no identical 32-bit label has both formula-bound memberships",
            "N6 fail closed if canonicality, UNSAT, full-cell coverage, proof trust, or completeness is missing",
        ],
        "branch_contract": {
            "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE": "all P1-P7 pass and no conflicting valid negative certificate exists",
            "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE": "all N1-N6 pass and no conflicting valid positive certificate exists",
            "CANNOT_CHECK": "otherwise, including malformed, incomplete, source-mismatched, marginal-only, ambiguous, or conflicting input",
        },
        "allowed_branches": [
            "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE",
            "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE",
            "CANNOT_CHECK",
        ],
        "fail_closed_non_guarantees": [
            "coordinate-wise marginals do not establish a common label",
            "ambient canonical syntax does not establish H_31 membership",
            "support-cell arithmetic does not establish overlap or disjointness",
            "computation without a proof/completeness certificate is not a mathematical result",
            "no cover, circuit, novelty, independent-review, or P-versus-NP authority",
        ],
        "implementation": None,
        "evaluation_authorized": False,
        "result_state": "UNEVALUATED",
        "credit": {"mathematical_result": 0, "mathematical_saturation": 0, "software_process": 0, "independent_review": 0},
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def falsifier_identity(candidate: dict) -> dict:
    return seal({
        "schema_version": "1.0.0",
        "falsifier_id": FALSIFIER_ID,
        "candidate_id": CANDIDATE_ID,
        "candidate_artifact_hash": candidate["artifact_hash"],
        "identity_kind": "INERT_FUTURE_FALSIFIER_AND_INTEGRATION_WORLD_MANIFEST",
        "frozen_at_utc": FALSIFIER_FROZEN_AT,
        "future_worlds": [
            {
                "world_id": "K31-PLANTED-POSITIVE-CERTIFICATE-KERNEL-v1",
                "layer": "decision_kernel",
                "future_materialization_obligation": "supply synthetically validated P1-P7 flags without any native k31 label",
                "expected_branch": "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE",
                "materialized": False,
                "standalone_credit": "ZERO_MATHEMATICAL_OR_INTEGRATION_CREDIT",
            },
            {
                "world_id": "K31-PLANTED-NEGATIVE-CERTIFICATE-KERNEL-v1",
                "layer": "decision_kernel",
                "future_materialization_obligation": "supply synthetically validated N1-N6 flags without any native k31 enumeration",
                "expected_branch": "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE",
                "materialized": False,
                "standalone_credit": "ZERO_MATHEMATICAL_OR_INTEGRATION_CREDIT",
            },
            {
                "world_id": "K31-MALFORMED-CERTIFICATE-CANNOT-CHECK-v1",
                "layer": "full_discriminator",
                "future_materialization_obligation": "omit or corrupt one mandatory source/proof/membership field",
                "expected_branch": "CANNOT_CHECK",
                "materialized": False,
            },
            {
                "world_id": "K31-MARGINAL-ONLY-FALSE-POSITIVE-v1",
                "layer": "full_discriminator",
                "future_materialization_obligation": "submit only the already-public coordinate-wise marginal theorem and witness-count receipt, never witness bits",
                "expected_branch": "CANNOT_CHECK",
                "materialized": False,
            },
            {
                "world_id": "K31-SOURCE-BINDING-MISMATCH-v1",
                "layer": "integration",
                "future_materialization_obligation": "mutate one C041/C048/pre-candidate source hash while all caller flags claim validity",
                "expected_branch": "CANNOT_CHECK",
                "materialized": False,
            },
            {
                "world_id": "K31-FRONTEND-KERNEL-BRANCH-PROPAGATION-v1",
                "layer": "integration",
                "future_materialization_obligation": "prove the full frontend serializes the exact kernel input, invokes the bound kernel, and propagates each branch unchanged",
                "expected_branches": ["NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE", "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE", "CANNOT_CHECK"],
                "materialized": False,
            },
        ],
        "independence_requirements": [
            "future falsifier must rederive source hashes and certificate obligations rather than import candidate proof code",
            "kernel planted worlds must not be represented as full-discriminator validation",
            "integration worlds must reject caller-supplied authority booleans",
            "same-context roles are not independent peer review",
        ],
        "decisive_refuters": [
            "acceptance of a marginal-only packet as NONEMPTY",
            "acceptance of an incomplete enumeration as EMPTY",
            "any source mismatch producing a decisive branch",
            "any valid positive or negative certificate producing the wrong branch",
            "kernel invocation or branch-propagation mismatch in the full discriminator",
        ],
        "implementation": None,
        "worlds_materialized": False,
        "evaluation_authorized": False,
        "result_accessed": False,
        "credit": {"mathematical_result": 0, "independent_review": 0, "root_authority": 0},
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def receipt(candidate: dict, falsifier: dict) -> dict:
    trace_delta = {
        "event_id": "O9d12a2a1b-C052-K31-OVERLAP-E09",
        "atom_id": "O9d12a2a1b-C052-K31-OVERLAP",
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": RECEIPT_FROZEN_AT,
        "state_summary": "Only inert target-blind discriminator and falsifier identities are frozen; no evaluator, certificate, formula, label, or result exists in this round.",
        "action_summary": "Freeze exact positive/negative/CANNOT_CHECK branch contracts and future planted/integration world identities.",
        "evidence_pointers": [str(CANDIDATE_OUT.relative_to(ROOT)), str(FALSIFIER_OUT.relative_to(ROOT))],
        "alternatives_considered": ["run overlap now", "construct a common label", "freeze only a kernel", "freeze full source-bound discriminator plus mandatory integration worlds"],
        "decision_rationale": "The pre-candidate packet permits candidate generation but the full-label result remains firewalled; freeze identities before any materialization or execution.",
        "outputs": [candidate["artifact_hash"], falsifier["artifact_hash"], "ZERO_RESULT_OR_MATHEMATICAL_CREDIT"],
        "uncertainties": ["no certificate materialized", "same-context review is not independent"],
        "residuals": ["future public evaluation authorization required", "H_31 intersection P_32 unresolved", "root open"],
        "next_steps": ["PR and merge this identity freeze", "freeze a separate evaluation authorization before implementation or world materialization"],
        "previous_event_hash": PREVIOUS_EVENT_HASH,
    }
    trace_delta["artifact_hash"] = digest(
        json.dumps(trace_delta, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    )
    return seal({
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C052-K31-OVERLAP-CANDIDATE-FREEZE-RECEIPT-20260812",
        "application_base_sha": APPLICATION_BASE_SHA,
        "framework_pin": FRAMEWORK_SHA,
        "candidate_id": CANDIDATE_ID,
        "candidate_artifact_hash": candidate["artifact_hash"],
        "falsifier_id": FALSIFIER_ID,
        "falsifier_artifact_hash": falsifier["artifact_hash"],
        "frozen_at_utc": RECEIPT_FROZEN_AT,
        "trace_delta": trace_delta,
        "chronology_firewall": {
            "candidate_identity_frozen": True,
            "falsifier_identity_frozen": True,
            "implementation_created": False,
            "new_formula_or_label_constructed": False,
            "public_witness_bits_or_labels_inspected_or_compared": False,
            "SAT_UNSAT_or_overlap_executed": False,
            "future_world_materialized": False,
            "evaluation_authorized": False,
            "result_accessed": False,
        },
        "next_authorized_action": "PR_REVIEW_MERGE_ONLY",
        "credit": {"mathematical_result": 0, "mathematical_saturation": 0, "Git_CI_trace": 0, "independent_review": 0},
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def build() -> tuple[dict, dict, dict]:
    assert_sources()
    candidate = candidate_identity()
    falsifier = falsifier_identity(candidate)
    return candidate, falsifier, receipt(candidate, falsifier)


def write() -> tuple[dict, dict, dict]:
    documents = build()
    for path, document in zip((CANDIDATE_OUT, FALSIFIER_OUT, RECEIPT_OUT), documents):
        path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return documents


if __name__ == "__main__":
    write()
