from itertools import combinations


def all_subsets(universe):
    universe = tuple(universe)
    return tuple(
        frozenset(items)
        for size in range(len(universe) + 1)
        for items in combinations(universe, size)
    )


def upward_closure(seeds, universe):
    subsets = all_subsets(universe)
    return {
        candidate
        for candidate in subsets
        if any(seed.issubset(candidate) for seed in seeds)
    }


def full_closure(base, rules, universe):
    closure = set(base)
    changed = True
    while changed:
        changed = False
        for left, right in rules:
            if left in closure and right in closure:
                consequent = left & right
                for candidate in all_subsets(universe):
                    if consequent.issubset(candidate) and candidate not in closure:
                        closure.add(candidate)
                        changed = True
    return closure


def projected_fixpoint(base, rules):
    bits = [
        [left in base, right in base]
        for left, right in rules
    ]
    changed = True
    while changed:
        changed = False
        fired = [
            i for i, pair in enumerate(bits)
            if pair[0] and pair[1]
        ]
        for i in fired:
            consequent = rules[i][0] & rules[i][1]
            for j, (left, right) in enumerate(rules):
                if not bits[j][0] and consequent.issubset(left):
                    bits[j][0] = True
                    changed = True
                if not bits[j][1] and consequent.issubset(right):
                    bits[j][1] = True
                    changed = True
    empty = frozenset() in base or any(
        bits[i][0] and bits[i][1] and not (rules[i][0] & rules[i][1])
        for i in range(len(rules))
    )
    return tuple((left, right) for left, right in bits), empty


def projected_from_full(closure, rules):
    return tuple(
        (left in closure, right in closure)
        for left, right in rules
    ), frozenset() in closure


def test_coarse_fired_pair_vector_is_not_congruent():
    universe = frozenset({1, 2, 3})
    rules = (
        (frozenset({1, 2}), frozenset({2, 3})),
        (frozenset({2}), frozenset({1, 3})),
    )

    base_a = upward_closure(
        (frozenset({1}), frozenset({3})),
        universe,
    )
    base_2 = upward_closure(
        (frozenset({1, 2}), frozenset({2, 3})),
        universe,
    )

    active_a = tuple(left in base_a and right in base_a for left, right in rules)
    active_2 = tuple(left in base_2 and right in base_2 for left, right in rules)
    assert active_a == active_2 == (True, False)

    terminal_a = full_closure(base_a, rules, universe)
    terminal_2 = full_closure(base_2, rules, universe)
    assert frozenset() in terminal_a
    assert frozenset() not in terminal_2


def test_antecedent_membership_projection_matches_full_recurrence():
    universe = frozenset({1, 2, 3})
    subsets = tuple(item for item in all_subsets(universe) if item)

    # Deduplicate all upward-closed nonempty base states generated from nonempty seeds.
    bases = {}
    for seed_mask in range(1, 1 << len(subsets)):
        seeds = tuple(
            subsets[i] for i in range(len(subsets))
            if seed_mask & (1 << i)
        )
        closure = frozenset(upward_closure(seeds, universe))
        bases[closure] = set(closure)

    selected_rules = (
        (frozenset({1, 2}), frozenset({2, 3})),
        (frozenset({2}), frozenset({1, 3})),
        (frozenset({1}), frozenset({2})),
        (frozenset({1, 3}), frozenset({2, 3})),
        (frozenset({1, 2, 3}), frozenset({1, 3})),
    )

    rule_families = tuple(
        (selected_rules[i], selected_rules[j])
        for i in range(len(selected_rules))
        for j in range(len(selected_rules))
    )

    for base in bases.values():
        for rules in rule_families:
            terminal = full_closure(base, rules, universe)
            assert projected_fixpoint(base, rules) == projected_from_full(terminal, rules)
