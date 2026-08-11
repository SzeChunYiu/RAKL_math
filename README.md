# RAKL Math

`RAKL_math` is the application/research repository for mathematical discovery performed with the RAKL framework.

## Repository split

- **`SzeChunYiu/RAKL`** owns the reusable research framework: assurance architecture, mathematical-research runtime/API, schemas, proof/evidence machinery, research memory, failure lattice, metacognition, breakthrough-learning controls, workflows, and framework self-research.
- **`SzeChunYiu/RAKL_math`** owns mathematical applications of that framework: Millennium-problem workspaces, problem contracts, source packets, context fibers, proof/problem DAGs, candidates, falsifiers, negative history, reviews, traces, and cross-problem mathematical transfer research.

Mathematical research in this repository must treat the current `main` of `SzeChunYiu/RAKL` as the framework source of truth. For reproducible execution, the accepted revision observed from that branch is frozen in both the `framework/RAKL` gitlink and `config/rakl-framework-pin.json`; pin changes require review and a complete application-suite rerun. A local research artifact never overrides or weakens a framework gate.

## Framework submodule

`framework/RAKL` is a Git submodule pointing back to `SzeChunYiu/RAKL`. It gives application sessions a local framework checkout while preserving the repository boundary. The machine-readable config mirrors the gitlink, and the test runner rejects disagreement.

The gitlink is a reproducibility pin, **not** a guarantee that the framework is current. At the beginning of an active research cycle, compare the submodule commit with current `SzeChunYiu/RAKL/main`. If they differ, use/fetch the current framework `main` for authority before applying assurance or discovery rules. A submodule-pointer update is dependency synchronization, not mathematical evidence.

Typical clone setup:

```bash
git clone --recurse-submodules https://github.com/SzeChunYiu/RAKL_math.git
```

## Initial portfolio

The active portfolio is the six unsolved Millennium Prize Problems:

- P versus NP
- Riemann Hypothesis
- Navier–Stokes existence and smoothness
- Yang–Mills existence and mass gap
- Hodge Conjecture
- Birch and Swinnerton-Dyer Conjecture

A cross-Millennium lane studies transferable success/failure structure without treating superficial similarity as mathematical evidence.

## Authority boundary

This repository is a research workspace, not a certificate of solved open problems. Computation is not proof; proof is not novelty; same-context review is not independent review. Root claims must satisfy the current RAKL root-solution gates in the framework repository.

## Migration provenance

The application workspace was migrated from `SzeChunYiu/RAKL/research/real_math` and active mathematical-research branches. The original Git history remains available in `SzeChunYiu/RAKL`; migrated snapshots retain source repository/ref provenance so chronology is not silently rewritten.

## Verification

Initialize and test against the exact framework gitlink/config pin:

```bash
git submodule update --init framework/RAKL
python tools/run_application_tests.py --framework framework/RAKL
```

See `docs/development.md` for the fail-closed checkout requirements.
