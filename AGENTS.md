# RAKL_math agent contract

`RAKL_math` is the mathematical-application repository. `SzeChunYiu/RAKL` is the reusable framework repository.

## Mandatory repository boundary

1. Write mathematical application state here: problem contracts, source packets, context fibers, problem/proof DAGs, routes, candidates, falsifiers, negative history, reviews, traces, problem-specific tests, and cross-Millennium transfer artifacts.
2. Do not write those application artifacts into `SzeChunYiu/RAKL`.
3. Reusable framework defects or improvements discovered during application work must be isolated into a framework issue/PR in `SzeChunYiu/RAKL` without moving problem evidence back into that repository.

## Framework authority and submodule

- `framework/RAKL` is a submodule convenience checkout of `SzeChunYiu/RAKL`.
- The submodule gitlink is a reproducibility pin, not automatic freshness.
- At the beginning of every active research cycle, determine current `SzeChunYiu/RAKL/main` and compare it with the submodule commit.
- If the submodule is stale, fetch/read current `RAKL/main` before applying framework rules. Never let a stale gitlink weaken or bypass a newer assurance gate.
- Updating the submodule pointer is dependency synchronization only. It is not proof, evidence, novelty, or research progress by itself.

## Mathematical authority

Computation is not proof. Proof is not novelty. Same-context review is not independent review. A Millennium root closes only under the current RAKL root-solution gate and exact official problem contract.

Historical RAKL mathematical branches/issues/PRs are migration provenance only. Future mathematical application work belongs in this repository.
