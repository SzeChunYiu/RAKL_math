# RAKL_math agent contract

`RAKL_math` is the mathematical-application repository. `SzeChunYiu/RAKL` is the reusable framework repository.

## Mandatory repository boundary

1. Write mathematical application state here: problem contracts, source packets, context fibers, problem/proof DAGs, routes, candidates, falsifiers, negative history, reviews, traces, problem-specific tests, and cross-Millennium transfer artifacts.
2. Do not write those application artifacts into `SzeChunYiu/RAKL`.
3. Reusable framework defects or improvements discovered during application work must be isolated into a framework issue/PR in `SzeChunYiu/RAKL` without moving problem evidence back into that repository.

## Framework authority and submodule

- `framework/RAKL` is a submodule convenience checkout of `SzeChunYiu/RAKL`.
- The submodule gitlink is a reproducibility pin, not automatic freshness. `config/rakl-framework-pin.json` mirrors that gitlink in a machine-readable contract, and CI requires exact equality.
- At the beginning of every active research cycle, determine current `SzeChunYiu/RAKL/main` and compare it with the submodule commit.
- If the submodule is stale, fetch/read current `RAKL/main` before applying framework rules. Never let a stale gitlink weaken or bypass a newer assurance gate.
- Updating the submodule pointer and machine-readable pin is dependency synchronization only. It is not proof, evidence, novelty, or research progress by itself.

## Application discipline

1. Read the accepted RAKL `skills/rakl-core/SKILL.md`, its manifest, always-loaded core files, and only workflow fragments required by the active atom.
2. Define object, quantity of interest, scope, context and evidence boundary before comparison or candidate generation.
3. Preserve candidate/evaluator chronology. Never backfill a pre-candidate gate after seeing a result; create a child atom when context changes.
4. Query success-derived tool memory and the failure lattice before candidate generation.
5. Treat LLM output as proposal-only and preserve nulls, refutations, failures and supersession lineage.

Product paths are `research/`, `tests/`, `tools/`, `schemas/` and `config/`. Do not copy reusable framework logic into this repository. An evidence-backed method lesson flows into a separately evaluated RAKL framework change; one application outcome does not authorize framework promotion.

## Required verification

Initialize the exact submodule and run the complete application suite through the pin-verifying runner:

```bash
git submodule update --init framework/RAKL
python tools/run_application_tests.py --framework framework/RAKL
```

The runner requires the framework path, committed gitlink and machine-readable pin to agree, and rejects dirty framework authority paths. Missing or mismatched evidence fails closed. Do not weaken a protected evaluator, frozen falsifier or framework gate to obtain a pass.

## Mathematical authority

Computation is not proof. Proof is not novelty. Same-context review is not independent review. A Millennium root closes only under the current RAKL root-solution gate and exact official problem contract.

Historical RAKL mathematical branches/issues/PRs are migration provenance only. Future mathematical application work belongs in this repository.
