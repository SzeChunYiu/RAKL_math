# NS-B1a3b1b pre-candidate same-context expert cell — R1

**Authority:** SAME_CONTEXT_INTERNAL_REVIEW / PROPOSAL_SHADOW_ONLY / INDEPENDENT_REVIEW_CREDIT_0_OF_3  
**Framework subject:** `SzeChunYiu/RAKL@812e9cf18345ef430f0a4cc3ff78f93d7f18ed22` (`method_version=3.0.0`)  
**Application base:** `SzeChunYiu/RAKL_math@dc83b72201cb58844b2bdc76117e4dcb9190211d`  
**Atom:** `NS-B1a3b1b` / issue #137

This cell reviewed the frozen problem signature before the registered mathematical discriminator. It may block or redirect a candidate, but it cannot grant independent-review, theorem, novelty, lesson, tool, gluing, or root authority.

## Roles and delegated attacks

1. **3D Navier–Stokes PDE / vorticity analyst.** Audit the exact vorticity identity, sign conventions, vortex-stretching term, and whether the global smooth-decaying model is genuinely more favorable than the localized suitable-weak setting.
2. **Critical-scaling / endpoint analyst.** Track dimensions under parabolic scaling and test the endpoint profile `y(t)=a(T-t)^(-1/2)` for integrability, blow-up, and scale invariance.
3. **Harmonic-analysis analyst.** Audit the Biot–Savart/Calderón–Zygmund step `||S||_2 <= C||omega||_2`, the `L4` Gagliardo–Nirenberg interpolation, Young exponents, and derivative loss.
4. **ε-regularity / Type-I interface analyst.** Bind Pineau–Vicol v2 Theorem 1.9 and Proposition 9.5 as downstream consumers only; verify that one-slice small rescaled enstrophy is not silently assumed.
5. **Adversarial falsification analyst.** Prefer a scalar hostile trajectory that satisfies every consequence actually derived from the proposed proof architecture while violating its desired trace conclusion. Enforce the disclaimer that a scalar trajectory is not an NSE solution.
6. **Local-to-global / pressure analyst.** Keep local cutoff/pressure/far-field issues separate. Failure already in the favorable global identity is local proof-architecture failure; failure introduced only by cutoffs is a gluing/localization issue.
7. **RAKL v3 assurance / metrology analyst.** Check current-framework subject, noncanonical retrieval authority, prospective receipt, episode→diagnosis→lesson separation, all seven saturation axes, and `CANNOT_MEASURE` fields.

## Pre-candidate discussion and consensus

The PDE and harmonic-analysis roles agree that the cheapest equation-specific test is the classical global enstrophy route, because localizing it can only add cutoff/transport/pressure obligations. The scaling role requires the scalar closure to be compared against the Type-I exponent before any Grönwall language is accepted. The ε-regularity role rejects using Pineau–Vicol's one-slice hypothesis as an input: it is the consumer-side success condition this atom is trying to produce. The adversarial role registers `y_a(t)=a(T-t)^(-1/2)` as the first falsifier. The local-to-global role requires any local cutoff failure to be recorded separately from the scalar endpoint result. The RAKL role marks PR #131's episode as `PENDING`: it changed priority toward an NSE-specific upgrade but cannot carry canonical authority.

**Decision:** authorize exactly the predeclared scalar enstrophy discriminator. Do not search for a new geometric criterion until this smallest closure has been verified or falsified.
