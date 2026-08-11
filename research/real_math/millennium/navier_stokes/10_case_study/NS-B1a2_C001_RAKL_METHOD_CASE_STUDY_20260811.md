# RAKL_METHOD_CASE_STUDY — NS-B1a2-C001

**Scope:** one proposal/shadow RAKL v3 research episode. No theorem, Type-I exclusion, novelty, independent-review, or Clay-root authority.

## Framework adoption

This cycle read current `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466` before application work. PR #121 is now merged and v3 authority-sensitive transitions require protected content attestations rather than caller-supplied IDs, booleans, enums or `verified` flags. The application submodule remains pinned to `15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`, so current-v3 behavior was inspected directly and the application records below remain **proposal/shadow telemetry**. No protected authority attestation is asserted.

## Research method used

The cycle followed the previous `NS-B1a1` scale-charge route pruning. Rather than proposing a new regularity theorem immediately, it selected one remaining family from that residual: compactness/minimality plus rigidity in self-similar time.

The exact bridge under audit was:

`finite-I Type-I ancient class`
`-> renormalized-orbit compactness/minimality`
`-> one late slice with small scaling-generator drift`
`-> source-valid approximate-self-similarity regularity criterion`.

Pineau–Vicol v2 supplied the downstream discriminator. Their Theorem 1.9 requires a local pointwise Type-I velocity bound, a fixed-annulus pressure bound, and one sufficiently late slice with small self-similar-time derivative; Remark 1.11 weakens only the derivative norm coordinate.

## Expert cell and delegated checks

Seven same-context roles were frozen before the result:

1. Type-I/ancient-solution PDE lead — exact Albritton–Barker class and Liouville triggers.
2. Renormalized-dynamics/concentration-compactness lead — compactness versus convergence and modulation.
3. Local-energy/pressure lead — pressure and pointwise-interface inheritance.
4. Vorticity/weighted-energy lead — whether an actual dissipative defect exists.
5. Adversarial dynamical-systems lead — compact recurrent orbit and periodic near-misses.
6. Formal-methods/assurance lead — chronology and protected-v3 authority boundary.
7. Novelty/research-value lead — source scope and route-pruning value.

All seven selected the compactness-to-small-drift hostile audit and blocked theorem generation beforehand.

## Prior experience that changed routing

- `F-NS-B1a-C001-PRESSURE-SUMMABILITY` prevented another pressure-tail divergence route.
- `F-NS-B1a1-C001-SCALE-NEUTRAL-CHARGE` prevented treating the standard local-energy ledger as a finite log-scale budget.
- `F-C024-FRACTIONAL-INTEGRALITY-GAP` again motivated checking the assembly map rather than strengthening a local surrogate.
- `SOURCE-GAP-2606.07875-TERMINAL-SCALE` prevented a smallest-scale/well-foundedness shortcut.
- `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` supplied the reusable source-surrogate/root-bridge/falsifier pattern.

The observable pre-memory temptation was “try concentration compactness/minimal orbit, then use near-self-similarity.” After memory review, the action changed to “first falsify whether compactness itself can produce the required near-stationary slice.”

## What worked

The audit separated three statements that are easy to conflate.

First, a precompact orbit need not have small instantaneous drift: `z(s)=(cos s,sin s)` has compact range and unit speed forever.

Second, a bounded trajectory can have a small long-time **vector average** of its derivative because endpoint increments divide by the averaging time, but cancellation does not control the average derivative norm or produce a small-norm time slice.

Third, time averaging the nonlinear Navier–Stokes equation does not produce the stationary Leray equation unless the fluctuation/Reynolds stress is controlled.

A formal Gaussian-weighted velocity-energy calibration also shows sign-indefinite convection and pressure contributions, so the most naive fixed Gaussian energy is not automatically the missing Lyapunov budget.

Pineau–Vicol's exact DSS/RDSS formulation provides a source-valid structural near-miss: periodic self-similar-time profiles are a real scenario class, and their RDSS exclusion requires restricted parameter regimes including small period in the relevant cases.

## What failed

The route

`precompact/recurrent renormalized orbit`
`-> compactness or long-time averaging alone`
`-> one-slice small ||partial_s U||`

failed as a logical bridge.

This is not a Navier–Stokes counterexample and not a refutation of concentration compactness. It says a concentration-compactness route needs **one more dynamics-specific coordinate**: finite variation, a coercive Lyapunov defect, asymptotic regularity, no-recurrence, controlled modulation, or a direct estimate of the scaling generator.

## Failure taxonomy

- mathematics-local: `NO` — no source-valid Navier–Stokes estimate was refuted;
- retrieval: `NO` — the Pineau–Vicol v2 criterion and prior memory materially changed the action;
- decomposition: `NO` — the compactness-to-drift interface was isolated before theorem generation;
- representation: `YES` — compactness/average endpoint motion was being asked to stand in for instantaneous generator smallness;
- verification: `NO` — the logical controls, nonlinear averaging identity and source interface were checked;
- tooling/framework freshness: `PARTLY` — current framework is newer than the application submodule pin;
- gluing/local-to-global: `YES` — primary failure category is the missing bridge from an orbit-level certificate to a one-slice rigidity trigger.

## Seven-axis retained novelty

Proposal/shadow retained novelty for this cycle:

- `KNOWLEDGE +1` — explicit separation of orbit compactness, vector-average drift and one-slice generator norm;
- `OPERATOR +0` — reused the existing root-bridge hostile-audit method;
- `EXPERIENCE_PATTERN +1` — another case where a local/global surrogate does not supply the exact root-critical interface;
- `OBSTRUCTION +1` — compactness/averaging alone cannot force Pineau–Vicol generator smallness;
- `RELATION +1` — bound periodic/RDSS renormalized dynamics to the compactness-versus-stationarity distinction;
- `PATH +1` — route pivots to finite variation/Lyapunov/no-recurrence/direct generator control;
- `META_METHOD +0` — no framework method promotion.

Reopened axes: `OBSTRUCTION`, `RELATION`, `PATH`.

## Novelty class

`TRANSFER_NOVEL`, structural rank `0`, for the route-pruning subproblem only. The cycle reused an existing cross-problem bridge audit and elementary dynamical controls in a new PDE interface. No new primitive research operator or Navier–Stokes theorem is claimed.

## Residual / next atom

`NS-B1a3`: search for the weakest sign-controlled or finite-variation self-similar-time defect that is genuinely inherited from the finite-`I` Type-I ancient class and can force `liminf` one-slice drift smallness. If no such defect is controlled, record that failure and rotate to an orthogonal source-valid Liouville trigger.

The pointwise-Type-I velocity and fixed-annulus pressure prerequisites of Pineau–Vicol Theorem 1.9 remain separate interface obligations already overlapping `NS-B1b1`; this lane should link rather than duplicate them.

## Framework-improvement hypothesis

The newly merged v3 authority hardening resolves a major earlier weakness: authority-sensitive transitions no longer accept caller declarations as sufficient. The application still lacks a synchronized, machine-readable framework-freshness receipt and canonical per-cycle v3 state materialization. Consequently pre/post `RAKLV3State` fingerprints and protected authority resolution cannot yet be measured directly from `RAKL_math`.

Framework hypothesis remains: application CI should bind exact current-framework adoption or explicitly label a run as historical-pin/shadow, and should expose a canonical telemetry adapter that can materialize `RAKLV3State` fingerprints without letting application data mint authority.
