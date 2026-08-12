# NS-B1a3b1b source audit — critical-point morphology interface

Authority: `PROPOSAL_SHADOW_SOURCE_BINDING / NO_ROOT_AUTHORITY`.

## Current primary consumer

Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866v2, revised 13 July 2026, was checked against the current primary arXiv HTML after the verification target was frozen.

The source distinguishes the **critical point singularity profile** from mere critical Lorentz membership. Definition 2.1 specifies a potential finite-time profile centered at one spatial point, writes the vorticity magnitude as

`omega(x,t) = Phi(x,t) |x|^-2`,

assumes the core shape factor is scale-invariant or log-periodic with the stated critical gradient control, and obtains the large-threshold containment

`A_lambda(t) subset B_R`, with `R <= C lambda^-1/2`,

with `C` independent of time. Theorem 4.1 then assumes that the vorticity **conforms to that critical concentration profile**, saying *in particular* that it belongs uniformly in time to `L^{3/2,infinity}`; it separately assumes the uniform log-weighted BMO direction condition. The proof then localizes the commutator on precisely the shrinking ball supplied by the profile.

Primary selectors: arXiv HTML v2, Definition 2.1 (profile, shape factor, super-level containment), Theorem 4.1 (profile assumption and `in particular` weak-Lorentz membership), and the near/far source split immediately after Theorem 4.1.

**Typed implication exposed by the source:**

`critical-point profile  =>  weak-L^{3/2} amplitude`

is source-stated, while the reverse implication is neither stated nor used as an equivalence. The one-center morphology is therefore an independent producer coordinate unless another theorem supplies it.

## Producer boundary

Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502v2 / J. Math. Fluid Mech. 21 (2019) 43, remains the registered producer. Its primary abstract was rechecked: Type-I singularities are related to non-trivial mild bounded ancient solutions satisfying a Type-I decay condition, and the Liouville theorem uses a global `L^3` bound along a backward time sequence. The exact finite-`I` definitions/Theorem 1.1 binding already present on current `RAKL_math/main` is reused; no new norm equivalence is imported here.

Nothing in the bounded producer/consumer source packet checked for this atom was located that identifies every finite-`I` ancient limit with Grujić's one-center `Phi |x|^-2` source family. This is **not** a literature-wide nonexistence claim: source-family completeness is not measurable from the bounded search.

## Bounded adjacent-source search

A targeted arXiv search for Type-I/finite-`I` ancient solutions combined with one-center `|x|^-2` vorticity morphology returned Albritton–Barker and adjacent local-singularity/criticality works, but no exact theorem with the frozen producer and consumer signatures. Coverage completeness is `CANNOT_MEASURE`.

## Scope conclusion

This child may test only whether weaker critical-amplitude/divergence-free information can manufacture the one-center morphology. A negative result does **not** refute a Navier–Stokes-equation-specific implication from finite `I`, does not refute Grujić's conditional theorem, and does not solve the separate log-BMO direction, global far-field, ancient/pre-singularity state-space, or Type-II obligations.
