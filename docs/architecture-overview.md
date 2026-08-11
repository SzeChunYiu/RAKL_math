# Architecture overview

## Authority split

`RAKL_math` is an application/evidence repository. `SzeChunYiu/RAKL` owns the
reusable runtime, assurance logic, schemas and research method. The application
test runner admits only the exact framework revision jointly recorded by the
`framework/RAKL` gitlink and `config/rakl-framework-pin.json`.

```text
pinned RAKL framework
        |
        v
RAKL_math context/candidate/evaluator chronology
        |
        +--> machine-readable evidence and tests
        |
        +--> scoped success/failure lesson
                  |
                  v
          separately evaluated RAKL PR
```

## Application layout

- `research/real_math/millennium/<problem>/` stores problem-local source,
  context, route, candidate, falsification, memory, review and trace artifacts.
- `research/real_math/millennium/cross_problem/` stores witnessed transfer
  studies. Similar vocabulary is not sufficient evidence for a bridge.
- `tests/math_applications/` exercises application receipts and pinned framework
  gates.
- `framework/RAKL` is the reproducible framework gitlink; it is not application
  evidence and does not replace a live freshness check against framework main.
- `tools/run_application_tests.py` requires the gitlink, machine config and
  checkout identity to agree, then verifies cleanliness before exposing its
  `src/` tree to the test process.

The application repository must not vendor or silently fork framework logic.
