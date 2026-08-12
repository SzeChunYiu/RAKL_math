"""Append the frozen candidate and observed mathematical result to the trace."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
PRE = BASE / "09_trace/NS-B2a1a2_PRE_CANDIDATE_TRACE_20260812.json"
OUT = BASE / "09_trace/NS-B2a1a2_FINAL_TRACE_20260812.json"
CONTEXT = BASE / "01_frontier/NS-B2a1a2_CONTEXT_FIBER_20260812.json"
RESULT = BASE / "04_candidates/NS-B2a1a2_C001_ESCAPING_BUMP_RESULT_20260812.md"
RECEIPT = BASE / "05_falsification/NS-B2a1a2_C001_ESCAPING_BUMP_RECEIPT_20260812.json"
FAILURE = BASE / "07_memory/NS-B2a1a2_C001_FAILURE_EXPERIENCE_CANONICAL_20260812.json"
REVIEW = BASE / "08_reviews/NS-B2a1a2_C001_SAME_CONTEXT_REVIEW_20260812.json"
SATURATION = BASE / "10_case_study/NS-B2a1a2_C001_MATHEMATICAL_SATURATION_RECEIPT_20260812.json"


def _hash(document: dict) -> str:
    return "sha256:" + hashlib.sha256(
        json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def build_trace() -> dict:
    trace = json.loads(PRE.read_text())
    context = json.loads(CONTEXT.read_text())
    receipt = json.loads(RECEIPT.read_text())
    failure = json.loads(FAILURE.read_text())
    review = json.loads(REVIEW.read_text())
    saturation = json.loads(SATURATION.read_text())
    previous = trace["entries"][-1]["artifact_hash"]
    specs = [
        ("CANDIDATE_PROPOSED", "2026-08-12T08:10:00+00:00", "The runtime gate licensed one bounded functional validation.", "Freeze the exact translated-bump statement before execution.", [context["packet_hash"], "sha256:fc4885b3625d49423a68a683e7f1d89fe223cf704f54479250723aa4169672e9"], ["use a fixed-amplitude bump", "attempt a PDE solution construction"], "The amplitude sqrt(a_k)/F_k exactly calibrates normalized A while testing absolute mass escape.", ["NS-B2a1a2-C001-ESCAPING-BUMP", "sha256:fc4885b3625d49423a68a683e7f1d89fe223cf704f54479250723aa4169672e9"], ["The family is not a PDE solution."], [], ["Run the executable formula checker and complete the hand proof."]),
        ("FALSIFIER_RUN", "2026-08-12T08:12:00+00:00", "The candidate identity and formulas were frozen.", "Execute the bounded logarithmic-window, support, normalization, and mass checks.", [receipt["artifact_hash"]], [], "The executable screen checks exact candidate formulas but is not itself proof of the asymptotic statements.", [receipt["verdict"], receipt["artifact_hash"]], [], [], ["Record the analytic proof and tail equivalence."]),
        ("RESULT_RECORDED", "2026-08-12T08:14:00+00:00", "The calibrated family passes every formula and hostile support check.", "Record the direct construction proof and iff intermediate-annulus tightness lemma.", [_file_hash(RESULT), receipt["artifact_hash"]], [], "The explicit field refutes the bare functional implication; the inner-plus-annular decomposition isolates the sharp repair.", ["BARE_TRANSFER_REFUTED_SHARP_TIGHTNESS_CONDITION", _file_hash(RESULT)], ["No conclusion about PDE-generated sequences."], ["PDE_SCALE_ALIGNED_TIGHTNESS_REMAINS_OPEN"], ["Open a PDE-specific child or signed-flux bypass."]),
        ("RESIDUAL_OPENED", "2026-08-12T08:15:00+00:00", "The functional transfer is pruned but a PDE-derived modulus has not been tested.", "Register the canonical failure and child NS-B2a1a3.", [failure["experiences"][0]["artifact_hash"]], [], "The counterexample identifies the missing coordinate without blacklisting dynamics-specific repairs.", [failure["experiences"][0]["failure_id"]], ["Pressure and vanishing viscosity remain unaudited at the new child."], ["NS-B2a1a3", "NS-B2a1b"], ["Freeze fresh context before any PDE-specific candidate."]),
        ("REVIEWED", "2026-08-12T08:16:00+00:00", "A scoped construction, tail lemma, and residual are recorded.", "Run role-separated same-context hostile review and enforce the no-independence boundary.", [review["artifact_hash"]], ["claim a PDE counterexample", "claim literature novelty", "count same-context review as independent"], "All escalations are rejected; only the functional lesson survives.", [review["artifact_hash"], "PASS_SCOPED"], [review["strongest_objection"]], ["independent mathematical review absent"], ["Retain OPEN_NO_SOLUTION_CERTIFICATE."]),
        ("PROMOTED", "2026-08-12T08:17:00+00:00", "The bounded mathematical lesson survived scoped review.", "Promote only the route-pruning lesson and proposal-only application feedback.", [saturation["artifact_hash"]], ["promote a Navier-Stokes theorem", "promote a reusable framework rule"], "The explicit counterexample and exact tail condition deserve scoped mathematical credit; all framework feedback remains proposal-only and root authority remains none.", [saturation["artifact_hash"], "SCOPED_ANALYTIC_ROUTE_PRUNING_ONLY"], ["No independent review or novelty certificate."], ["NS0_OPEN_NO_SOLUTION_CERTIFICATE"], ["Continue only through a freshly gated residual atom."]),
    ]
    for offset, spec in enumerate(specs, start=8):
        event_type, timestamp, state, action, evidence, alternatives, rationale, outputs, uncertainties, residuals, next_steps = spec
        entry = {
            "event_id": f"NS-B2a1a2-E{offset:02d}",
            "atom_id": "NS-B2a1a2",
            "event_type": event_type,
            "timestamp": timestamp,
            "state_summary": state,
            "action_summary": action,
            "evidence_pointers": evidence,
            "alternatives_considered": alternatives,
            "decision_rationale": rationale,
            "outputs": outputs,
            "uncertainties": uncertainties,
            "residuals": residuals,
            "next_steps": next_steps,
            "artifact_hash": "",
            "previous_event_hash": previous,
        }
        entry["artifact_hash"] = _hash(entry)
        trace["entries"].append(entry)
        previous = entry["artifact_hash"]
    return trace


if __name__ == "__main__":
    OUT.write_text(json.dumps(build_trace(), indent=2, ensure_ascii=False) + "\n")
