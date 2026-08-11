"""Exact finite regression for C025's G_NEQ joint-signature calibration.

This module checks only the elementary signature/counting layer. It does not
enumerate arbitrary semi-filters and does not confer theorem or novelty authority.
"""

from __future__ import annotations

from math import ceil, log2


def bit_signature(vertex: int, width: int) -> tuple[int, ...]:
    """Return the little-endian width-bit label of a zero-based vertex."""
    if vertex < 0:
        raise ValueError("vertex must be nonnegative")
    if width < 0:
        raise ValueError("width must be nonnegative")
    if vertex >= (1 << width):
        raise ValueError("vertex does not fit in width bits")
    return tuple((vertex >> bit) & 1 for bit in range(width))


def minimum_binary_signature_width(count: int) -> int:
    """Minimum number of binary coordinates needed for count distinct labels."""
    if count < 1:
        raise ValueError("count must be positive")
    if count == 1:
        return 0
    return ceil(log2(count))


def covers_gneq_canonical_by_signatures(signatures: list[tuple[int, ...]]) -> bool:
    """Claim-41 reduction: every unequal pair must differ in some coordinate."""
    if not signatures:
        return False
    width = len(signatures[0])
    if any(len(signature) != width for signature in signatures):
        raise ValueError("all signatures must have the same width")
    return len(set(signatures)) == len(signatures)


def standard_power_of_two_calibration(n: int) -> dict[str, int | bool]:
    """Construct the standard n-bit partition family for N=2**n."""
    if n < 1:
        raise ValueError("n must be positive")
    N = 1 << n
    signatures = [bit_signature(vertex, n) for vertex in range(N)]
    return {
        "N": N,
        "width": n,
        "distinct_signature_count": len(set(signatures)),
        "covers_all_canonical_gneq_filters": covers_gneq_canonical_by_signatures(signatures),
        "capacity_lower_bound": minimum_binary_signature_width(N),
    }


if __name__ == "__main__":
    for n in range(1, 9):
        print(standard_power_of_two_calibration(n))
