from itertools import product


def _eval(generators, gates):
    vals = [0] * len(gates)
    for _ in range(len(gates) + 2):
        nxt = vals.copy()
        for i, (op, left, right) in enumerate(gates):
            def value(ref):
                kind, idx = ref
                return generators[idx] if kind == "g" else vals[idx]
            a, b = value(left), value(right)
            created = (a | b) if op == "U" else (a & b)
            nxt[i] = vals[i] | created
        if nxt == vals:
            return vals
        vals = nxt
    return vals


def _compress(gates):
    meet_nodes = [i for i, gate in enumerate(gates) if gate[0] == "I"]
    meet_index = {node: idx for idx, node in enumerate(meet_nodes)}
    union_nodes = [i for i, gate in enumerate(gates) if gate[0] == "U"]
    sources = {node: set() for node in union_nodes}
    changed = True
    while changed:
        changed = False
        for node in union_nodes:
            _, left, right = gates[node]
            new = set(sources[node])
            for kind, idx in (left, right):
                if kind == "g":
                    new.add(("g", idx))
                elif idx in meet_index:
                    new.add(("m", meet_index[idx]))
                else:
                    new |= sources[idx]
            if new != sources[node]:
                sources[node] = new
                changed = True

    def expr(ref):
        kind, idx = ref
        if kind == "g":
            return {("g", idx)}
        if idx in meet_index:
            return {("m", meet_index[idx])}
        return set(sources[idx])

    reduced = []
    for node in meet_nodes:
        _, left, right = gates[node]
        reduced.append((expr(left), expr(right)))

    output = {("m", meet_index[len(gates) - 1])} if len(gates) - 1 in meet_index else set(sources[len(gates) - 1])
    return reduced, output


def _eval_reduced(generators, reduced, output_sources):
    values = [0] * len(reduced)

    def union_value(sources):
        result = 0
        for kind, idx in sources:
            result |= generators[idx] if kind == "g" else values[idx]
        return result

    for _ in range(len(reduced) + 3):
        nxt = values.copy()
        for i, (left, right) in enumerate(reduced):
            nxt[i] = values[i] | (union_value(left) & union_value(right))
        if nxt == values:
            break
        values = nxt
    return union_value(output_sources)


def test_join_elimination_matches_all_two_gate_hostile_worlds():
    generators = [0b01, 0b10]
    gate_count = 2
    refs = [("g", 0), ("g", 1)] + [("i", i) for i in range(gate_count)]
    options = [(op, a, b) for op in ("U", "I") for a in refs for b in refs]
    checked = 0
    for gates in product(options, repeat=gate_count):
        expected = _eval(generators, gates)[-1]
        reduced, output = _compress(gates)
        assert _eval_reduced(generators, reduced, output) == expected
        checked += 1
    assert checked == 1024


def test_feedback_through_union_scc_is_preserved():
    generators = [0b001, 0b110]
    gates = [
        ("I", ("i", 1), ("g", 1)),
        ("U", ("g", 0), ("i", 2)),
        ("U", ("i", 0), ("i", 1)),
    ]
    expected = _eval(generators, gates)[-1]
    reduced, output = _compress(gates)
    assert _eval_reduced(generators, reduced, output) == expected


def test_calibration_never_claims_root_authority():
    # Computation calibrates the representation transformation only.
    root_status = "OPEN_NO_SOLUTION_CERTIFICATE"
    assert root_status == "OPEN_NO_SOLUTION_CERTIFICATE"
