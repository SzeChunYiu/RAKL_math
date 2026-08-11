"""Finite regression for O9d12a2a1a1b fixed-Lambda factorization.

This checks transcription of the source recurrence on planted finite worlds only.
Computation is not proof and grants no P-vs-NP or novelty authority.
"""
from itertools import combinations


def powerset(u):
    u = tuple(u)
    return {frozenset(c) for r in range(len(u)+1) for c in combinations(u, r)}


def upward(seed, omega):
    return {c for c in omega if any(s <= c for s in seed)}


def direct_round(state, rules, omega):
    new = set(state)
    for e, h in rules:
        if e in state and h in state:
            new.add(e & h)
    return upward(new, omega)


def projected_round(bits, rules, omega):
    tmp = dict(bits)
    for e, h in rules:
        c = e & h
        if bits[e] and bits[h]:
            tmp[c] = True
    return {c: any(tmp[d] for d in omega if d <= c) for c in omega}


def test_source_set_closure_matches_pointwise_projection():
    omega = powerset({0, 1, 2})
    rules = ((frozenset({0, 1}), frozenset({1, 2})),
             (frozenset({0, 2}), frozenset({1, 2})))
    seed = {frozenset({0}), frozenset({2})}
    direct = upward(seed, omega)
    bits = {c: c in direct for c in omega}
    for _ in range(4):
        direct = direct_round(direct, rules, omega)
        bits = projected_round(bits, rules, omega)
        assert {c for c, active in bits.items() if active} == direct


def test_equal_complete_base_vectors_remain_equal():
    omega = powerset({0, 1})
    rules = ((frozenset({0}), frozenset({1})),)
    base = upward({frozenset({0})}, omega)
    left = {c: c in base for c in omega}
    right = dict(left)
    for _ in range(3):
        left = projected_round(left, rules, omega)
        right = projected_round(right, rules, omega)
        assert left == right
