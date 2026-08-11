# NS-R001d source packet — projected advection/depletion bridge

Authority: `PRIMARY_SOURCE_CONTEXT / PRE_CANDIDATE / NO_THEOREM_CANDIDATE / ROOT_AUTHORITY_NONE`.

## Framework observation

This cycle evaluated the current framework at `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`.
The `RAKL_math` submodule remains pinned at `7853ec0c4ff8f862359835bca1af1d934bfbd887`; the active cycle read current RAKL directly, as required. The current framework keeps the strict context/memory/trace gate and additionally quarantines application-to-framework lesson imports as proposal-only. No framework mutation is attempted from this application lane.

## Root source

Charles L. Fefferman, *Existence and Smoothness of the Navier–Stokes Equation*, official Clay Mathematics Institute Millennium problem description.

This atom remains inside the positive regularity route. A conditional criterion, a static no-go screen, or a new scale-invariant diagnostic is nonterminal.

## Primary technical source: Miller v2 / 2026

Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2, revised 13 April 2026; journal reference *Pure and Applied Analysis* 8 (2026), 247–270.

For `S = nabla_sym u`, `omega = curl u`, and the orthogonal strain-space projection `P_st`, Miller rewrites the strain dynamics as a globally regular strain-vorticity interaction model plus

`R = P_st((u·nabla)S + S^2 + (3/4) omega⊗omega)`.

Load-bearing source statements used here:

1. Theorem 1.3: `<-Delta S, omega⊗omega> = 0` for the stated strain class.
2. The strain-vorticity interaction model is globally regular for all `L2_st` strain data (Theorem 1.2).
3. Theorem 1.8 gives an exponential `H1` strain estimate controlled by a scale-critical time integral of the projected remainder.
4. Theorem 1.9: if an `H3_df` mild Navier–Stokes solution has finite maximal time, then

   `limsup_{t -> T_max} ||R(t)||_2 / ||-Delta S(t)||_2 >= 1`.

These are conditional/perturbative criteria. The paper does **not** prove that finite kinetic energy forces the remainder ratio below one.

## Structural analogy source

Victor Gardner, Kyle L. Liss, Jonathan C. Mattingly, *A pathwise approach to the enhanced dissipation of passive scalars advected by shear flows*, arXiv:2410.05657 (2024).

The only retained transfer is structural: advection can be neutral in a coarse `L2` energy pairing while changing derivative/trajectory structure so diffusion becomes more effective. The target disanalogies are decisive: Navier–Stokes self-advection is coupled to the transported state, strain has quadratic production, and pressure/`P_st` are nonlocal.

## Exact scaling audit

True Navier–Stokes scaling: `u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`.

Then, in three dimensions,

- `S_lambda`, `omega_lambda` scale pointwise as `lambda^2`;
- `-Delta S_lambda` and each term inside `R_lambda` scale pointwise as `lambda^4`;
- both `||-Delta S_lambda||_2` and `||R_lambda||_2` scale as `lambda^(5/2)`;
- `Q=||R||_2/||-Delta S||_2` is scale invariant.

The first discriminator therefore must not be a dimensionally mismatched proxy.

## Pre-candidate discriminator selected

Before proposing a theorem, test the narrower claim:

> Can kinetic energy plus incompressibility and smooth decay bound `Q` at a single initial-data snapshot?

The test must use a smooth rapidly decaying divergence-free seed, must bind the projection through an exact strain-space pairing, and must keep kinetic energy fixed while concentrating spatial scale.

A negative result only rejects **energy-only snapshot control**. It leaves positive-time, time-integrated, frequency-local, pressure-mediated, or other exact-trajectory mechanisms open.
