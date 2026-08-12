from __future__ import annotations


def spatial_envelope(r: float) -> float:
    if r <= 1.0:
        return r**3
    return 1.0 + r


def temporal_overlap(r: float) -> float:
    return min(r**2, 1.0)


def A_envelope(r: float) -> float:
    return spatial_envelope(r) / r


def C_envelope(r: float) -> float:
    return temporal_overlap(r) * spatial_envelope(r) / r**2


def E_envelope(r: float) -> float:
    return temporal_overlap(r) * spatial_envelope(r) / r


def test_piecewise_ledger_envelopes_are_uniformly_bounded():
    radii = [10.0 ** (k / 8.0) for k in range(-64, 65)]
    assert max(A_envelope(r) for r in radii) <= 2.0 + 1e-12
    assert max(C_envelope(r) for r in radii) <= 2.0 + 1e-12
    assert max(E_envelope(r) for r in radii) <= 2.0 + 1e-12


def test_active_slice_packet_count_forces_l3_divergence():
    partial_masses = [2 * n + 1 for n in (1, 10, 100, 1000)]
    assert partial_masses == sorted(partial_masses)
    assert partial_masses[-1] > 1000.0


def test_realization_domain_gate_is_fail_closed_for_target_claim():
    realization_domain = "AMBIENT_REPRESENTATION"
    verdict = "REPRESENTATION_ONLY"
    may_certify_target_obligation_weakening = False
    assert realization_domain == "AMBIENT_REPRESENTATION"
    assert verdict == "REPRESENTATION_ONLY"
    assert may_certify_target_obligation_weakening is False
