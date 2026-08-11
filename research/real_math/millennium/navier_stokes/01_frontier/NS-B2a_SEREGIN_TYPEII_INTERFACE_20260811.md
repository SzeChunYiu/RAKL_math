# NS-B2a — Seregin Type-II ancient-Euler rigidity interface

## Frozen question

Can the Type-II branch isolated in Seregin arXiv:2606.29468v1 be eliminated by proving a **target-inherited far-field condition** and an **Euler-native rigidity theorem** for the exact ancient limit class?

Context packet hash: `sha256:a480d04f46ad09b5db95a45fb85d35edfcfc2e8afa22e3fc41fa73ee4ed191f9`.

## Why this lane is orthogonal

The Type-I lane keeps a viscous ancient Navier–Stokes equation and asks for an anti-replication/global-trace bridge. This Type-II lane has a scaling whose viscosity coefficient tends to zero. The blow-up profile is therefore governed by Euler. Any Type-I parabolic backward-uniqueness mechanism is a method-transfer disanalogy, not a closure theorem.

## Required profile and limit passage

The registered profile is a nontrivial ancient incompressible Euler solution obtained from Seregin's F=1 Type-II sequence. The limit passage is licensed only in the local topologies and pressure normalization established by the source. The profile must retain `(3.5)`, the local-energy inequality, and source nontriviality `(3.8)`.

The application must not silently add:

- finite total kinetic energy;
- global `L^3`, `L^p`, or vorticity integrability;
- spatial decay;
- self-similarity/DSS/periodicity;
- almost-periodicity modulo translations/dilations;
- global pressure normalization.

## Retrospective calibration

From the gradient and A-parts of `(3.5)`, one can choose `τ_a∈(-a^2,-a^2/2)` so that

`∫_{B(a)} |∇u(τ_a)|² <= C/a`,  
`∫_{B(a)} |u(τ_a)|² <= C a`.

Consequently the mean is `O(a^-1)` and Sobolev–Poincaré gives

`||u(τ_a)-ū_{B(a)}||_{L^6(B(a))} <= C a^-1/2`.

For each fixed `R`, `||u(τ_a)||_{L^6(B(R))} -> 0` and hence local `L^3(B(R)) -> 0` while `τ_a -> -∞`.

This observation predates the context freeze. It is retained only as source calibration and has **zero strict candidate credit**.

## Exact missing bridge

The desired next theorem interface is:

> A Seregin-F=1 ancient Euler profile satisfying the exact source bounds and local-energy inequality, together with a no-incoming-energy/far-field-tightness property proved to pass from the original suitable weak Navier–Stokes blow-up sequence through the Type-II scaling, is identically zero.

To make this valid, two proofs are required:

1. **Inheritance:** formulate the weakest pressure-aware tail/flux quantity on the rescaled Navier–Stokes approximants that is uniform as `f(λ)->0`, then prove it passes to the Euler limit.
2. **Rigidity:** prove that this inherited quantity plus `(3.5)` and backward expanding-ball smallness rules out all nonzero ancient Euler profiles in the class.

## Adversarial status

A compactly supported steady Euler flow is not in the F=1 class unless trivial: the time-integrated gradient term grows like `a²`, so `(1/a)` times that term grows like `a`. This rejects a tempting direct falsifier but does not prove the desired rigidity theorem.

## Promotion status

`ROOT_AUTHORITY_NONE`. No new theorem candidate is claimed. The packet is a source-bound classification and exact-obligation milestone.
