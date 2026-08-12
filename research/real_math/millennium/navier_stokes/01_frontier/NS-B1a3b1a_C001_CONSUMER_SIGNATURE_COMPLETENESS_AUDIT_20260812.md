# NS-B1a3b1a-C001 — Consumer-signature completeness audit

**Authority:** proposal/shadow route-refinement only. No Navier–Stokes theorem, no root authority.

## Root and atom binding
Root `NS0` remains `OPEN_NO_SOLUTION_CERTIFICATE`; this child is the Type-I producer/consumer interface `NS-B1a3b1a`. Frozen fibre: `sha256:decd36dc90f6fc12b0895410942baf84177d9245279452b1b845ae92cbf2a2d7`. Current framework: RAKL v3 `3.0.0`, package `1.2.0`, method spec `3.0`, Git `3e3ab453e6a3dd4bc8c0a9fa85e6327b363aeb17`. RAKL_math base: `a7301f0f0e2cab2750ac6e923efe18b5750b5af6`.

## Counterexample-first success-contract test
The inherited child asks whether finite-I dynamics can produce two global, uniform-in-time objects: weak-`L^{3/2}` vorticity and log-weighted-BMO vorticity direction. Before attempting that producer estimate, grant both outputs hypothetically and ask whether the selected Grujic v2 consumer is then invokable.

It is not. Grujic v2 Definition 2.1 defines the critical point singularity through `omega(x,t)=Phi(x,t)|x|^-2` and assumes `Phi` is scale-invariant or log-periodic at the core with `|grad Phi| <= C|x|^-1` uniformly in time. Theorem 4.1 assumes that critical concentration profile uniformly near the first possible singular time, in addition to global uniform weak-`L^{3/2}` vorticity and global uniform `bmo_{1/|log r|}` direction. Theorem 7.4 carries the same profile into a pre-singularity analyticity/escape-time endgame.

Therefore `finite I -> [global weak-L^{3/2} omega + global log-BMO xi] -> Grujic consumer` has an unbound theorem hypothesis even if the bracketed producer step were solved.

## Derivative-order / scaling audit
For `Phi=|x|^2 omega`, `grad Phi = 2 x omega + |x|^2 grad omega`. The shape-gradient condition is therefore a vorticity-derivative-level input. Albritton–Barker finite `I` is built from local scale-normalized `A+C+D+E`, with `E` controlling a spacetime integral of `|grad u|^2`. No registered edge upgrades that first-velocity-derivative spacetime control to the pointwise/uniform `grad omega`/`grad Phi` signature. This is a DifferenceWitness, not a proof of impossibility.

The scale check does not produce a contradiction: the Grujic profile assumptions are deliberately critical. The obstruction is instead *signature strength*—derivative order, pointwise profile class, globality, uniformity in time, and first-singular-time state space—not a units mismatch.

## Expert-cell synthesis
The PDE/epsilon-regularity specialist found no source-bound finite-I edge to the omitted point-profile derivative condition. The harmonic-analysis/vorticity specialist classified the omission as derivative-order/representation rather than mere scaling. The concentration-compactness specialist kept global Lorentz/BMO/tail gluing separate from the local profile-shape issue. The source/verifier specialist failed the consumer-input closure gate because the child success contract omits a theorem hypothesis. These are same-context roles only and provide `0/3` independent mathematical reviews.

## Outcome and routing
This is a **material decomposition/source-signature route refinement**, not a regularity result. Pruned as currently stated: “prove only the two named global norms, then invoke Grujic v2.” Live routes are: (1) strengthen the producer contract to the full critical-profile/shape-gradient/global/time/state-space signature, but only if a genuinely new equation-specific derivative mechanism appears; (2) search for a source-valid conditional theorem whose exact hypotheses are exhausted by attainable producer outputs; (3) rotate to pressure-temporal/no-recrossing, global critical-tightness, or another source-valid rigidity lane. Prior derivative-loss memory makes (2) or an orthogonal lane higher priority than re-entering (1).

## Nonpromotion
This audit does not show finite `I` cannot dynamically imply the omitted profile, does not establish or validate Grujic v2, does not exclude Type-I singularities, leaves Type-II untouched, and leaves the Clay root open.