"""Finite calibration only for O9d12a2a1a1e; not a proof oracle."""
from itertools import combinations

def powerset(universe):
    u = tuple(universe)
    return [frozenset(c) for r in range(len(u) + 1) for c in combinations(u, r)]

def union_closure(family):
    out = {frozenset()}
    for s in family:
        out |= {x | s for x in tuple(out)}
    return out

def traces(family, target):
    return {x & target for x in union_closure(family)}

def verify_universe(n=3):
    universe = frozenset(range(n))
    subsets = powerset(universe)
    marginal_cases = 0
    invisible_cases = 0
    for mask in range(1 << len(subsets)):
        family = {subsets[i] for i in range(len(subsets)) if (mask >> i) & 1}
        for target in subsets:
            before = traces(family, target)
            for added in subsets:
                after = traces(family | {added}, target)
                assert len(before) <= len(after) <= 2 * len(before)
                marginal_cases += 1
            if universe in union_closure(family):
                assert traces(family | {target}, target) == before
                invisible_cases += 1
    return {"marginal_cases": marginal_cases, "target_adjoin_invisible_cases": invisible_cases}

if __name__ == "__main__":
    print(verify_universe(3))
