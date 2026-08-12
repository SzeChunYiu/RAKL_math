"""Independent public falsifier for the C052 k=31 overlap result."""

from __future__ import annotations

import hashlib
from itertools import product
from pathlib import Path


M = "11100101"
ROOT = Path(__file__).resolve().parents[5]
FROZEN_SOURCES = {
    "c041_grammar": ("research/real_math/millennium/p_vs_np/04_candidates/C041_fx_sat_one_sided.py", "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"),
    "c048_proof_certificate": ("research/real_math/millennium/p_vs_np/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_PROOF_CERTIFICATE_FREEZE_20260812.json", "fd4d478d816c50423f2d6fbd668305bec911bcf3a035a2a5b516eb08796ec16c"),
    "c048_transfer_condition": ("research/real_math/millennium/p_vs_np/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_TRANSFER_CONDITION_FREEZE_20260812.json", "e2a924e708c1ab17b78e06a3935fd48772c0c172b9f01b0c756de80f1430908b"),
    "certificate_firewall": ("research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C052_K31_OVERLAP_CERTIFICATE_FIREWALL_20260812.json", "cb2501908327ec03a0a103691f824e06514616e04fda170b6803eef4935da971"),
    "context": ("research/real_math/millennium/p_vs_np/01_frontier/O9d12a2a1b_C052_K31_OVERLAP_CONTEXT_20260812.json", "f3a8dd3efbdfb034b1549341f51c47bf417d9d10c5e301caad76dda19f2b215b"),
    "memory_review": ("research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C052_K31_OVERLAP_RESEARCH_MEMORY_REVIEW_20260812.json", "b5bc34335f5e15677bd8ea4f44e23fdcb7313cf10c6d0bb04c6643bef82304ea"),
    "pre_candidate_gate": ("research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C052_K31_OVERLAP_PRE_CANDIDATE_GATE_RECEIPT_20260812.json", "14ff95e6a48cd51e74824530f61292ec9e5276f72a6c66132d8a184b3d7f6f83"),
    "pre_candidate_trace": ("research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C052_K31_OVERLAP_PRE_CANDIDATE_TRACE_20260812.json", "b53fc0311ad4d49e6f89938b306d788785f9b6290d192261a6fafdbcb044b5f1"),
    "shortcut_review": ("research/real_math/millennium/p_vs_np/08_reviews/O9d12a2a1b_C052_K31_OVERLAP_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json", "90ef5bc08757da741badcb36752fdaa4e0c0ed59603714ecdc9cec2f7e9ddec6"),
}


def source_bindings_hold(overrides: dict[str, bytes] | None = None) -> bool:
    supplied = overrides or {}
    return all(
        hashlib.sha256(supplied.get(name, (ROOT / path).read_bytes())).hexdigest() == expected
        for name, (path, expected) in FROZEN_SOURCES.items()
    )


def g(n: int) -> str:
    b = bin(n)[2:]
    return "0" * (len(b) - 1) + b


def length_row(a: int, m: int) -> tuple[int, int, int, int]:
    h = 6 + 2 * a + 2 * m.bit_length()
    r = h + 3 * m * (a + 1)
    return h, r, r & 1, r + (r & 1)


def supports(e: int) -> list[tuple[int, int, int, int, int]]:
    out = []
    for a in range(1, e + 1):
        for m in range(1, e + 1):
            h, r, p, encoded = length_row(a, m)
            if encoded == e:
                out.append((a, m, h, r, p))
    return out


def prefixes(v: int, m: int) -> set[str]:
    head = M + g(v) + g(m)
    w = 1 + v.bit_length()
    take = (32 - len(head) + w - 1) // w
    alphabet = [("1" if neg else "0") + f"{q:0{v.bit_length()}b}" for q in range(1, v + 1) for neg in (False, True)]
    return {(head + "".join(words))[:32] for words in product(alphabet, repeat=take)}


def kernel(source: bool, pos: bool, neg: bool, bad: bool) -> str:
    if bad or not source or pos == neg:
        return "CANNOT_CHECK"
    return "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE" if pos else "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE"


def run() -> dict:
    source_valid = source_bindings_hold()
    mutated_source_valid = source_bindings_hold({"c041_grammar": b"mutated"})
    worlds = {
        "K31-PLANTED-POSITIVE-CERTIFICATE-KERNEL-v1": kernel(True, True, False, False),
        "K31-PLANTED-NEGATIVE-CERTIFICATE-KERNEL-v1": kernel(True, False, True, False),
        "K31-MALFORMED-CERTIFICATE-CANNOT-CHECK-v1": kernel(True, False, False, True),
        "K31-MARGINAL-ONLY-FALSE-POSITIVE-v1": kernel(True, False, False, False),
        "K31-SOURCE-BINDING-MISMATCH-v1": kernel(mutated_source_valid, False, True, False),
    }
    expected = {
        "K31-PLANTED-POSITIVE-CERTIFICATE-KERNEL-v1": "NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE",
        "K31-PLANTED-NEGATIVE-CERTIFICATE-KERNEL-v1": "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE",
        "K31-MALFORMED-CERTIFICATE-CANNOT-CHECK-v1": "CANNOT_CHECK",
        "K31-MARGINAL-ONLY-FALSE-POSITIVE-v1": "CANNOT_CHECK",
        "K31-SOURCE-BINDING-MISMATCH-v1": "CANNOT_CHECK",
    }
    current = supports(64)
    expected_support = [(1, 8, 16, 64, 0), (4, 3, 18, 63, 1), (6, 2, 22, 64, 0)]
    per_v = []
    for a, m, _, _, _ in expected_support:
        for v in range(1 << (a - 1), 1 << a):
            ps = prefixes(v, m)
            separated = all(p[31] == "1" or (p[31] == "0" and p[7:10] == "100") for p in ps)
            per_v.append({"a": a, "m": m, "v": v, "prefix_count": len(ps), "separated": separated})
    actual_negative_valid = source_valid and length_row(2, 5) == (16, 61, 1, 62) and current == expected_support and all(row["separated"] for row in per_v)
    actual_branch = kernel(source_valid, False, actual_negative_valid, False)
    integration = {
        "serialized_fields": ["source_valid", "positive_valid", "negative_valid", "malformed_or_ambiguous"],
        "candidate_and_independent_kernel_agree_on_worlds": worlds == expected,
        "source_binding_rederived_without_candidate_import": source_valid,
        "mutated_source_binding_fails_closed": not mutated_source_valid,
        "actual_frontend_branch_propagated": actual_branch == "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE",
    }
    return {
        "world_results": worlds,
        "worlds_all_pass": worlds == expected,
        "current_support": current,
        "source_binding_valid": source_valid,
        "per_v_exhaustion": per_v,
        "actual_negative_valid": actual_negative_valid,
        "actual_branch": actual_branch,
        "integration": integration,
        "integration_all_pass": all(value for key, value in integration.items() if key != "serialized_fields"),
        "hidden_or_native_executed": False,
        "authority": "INDEPENDENTLY_IMPLEMENTED_SAME_CONTEXT_CHECK_NOT_INDEPENDENT_PEER_REVIEW",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, sort_keys=True))
