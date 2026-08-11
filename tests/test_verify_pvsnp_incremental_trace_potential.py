from verifiers.verify_pvsnp_incremental_trace_potential import verify_universe

def test_incremental_trace_potential_n3():
    out = verify_universe(3)
    assert out == {"marginal_cases": 16384, "target_adjoin_invisible_cases": 1744}
