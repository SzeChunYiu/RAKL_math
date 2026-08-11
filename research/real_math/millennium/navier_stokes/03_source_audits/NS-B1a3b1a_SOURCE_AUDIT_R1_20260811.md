# NS-B1a3b1a source audit — R1

Authority: `PROPOSAL_SHADOW_SOURCE_BINDING / NO_ROOT_AUTHORITY`.

## Exact producer source

Albritton–Barker, **On local Type I singularities of the Navier-Stokes equations and Liouville theorems**, arXiv:1811.00502v2 / J. Math. Fluid Mech. (2019), is the producer source. The registered local Type-I quantity is the supremum over subcylinders of the scale-invariant functionals `A+C+D+E`: time-essential-sup local velocity `L^2`, spacetime velocity `L^3`, pressure `L^{3/2}`, and spacetime gradient `L^2`. Theorem 1.1 connects a local Type-I singularity to a nontrivial mild bounded ancient solution with finite `I`. The source does **not** list a uniform time-slice vorticity `L^{3/2,∞}` norm or a logarithmic-BMO norm of normalized vorticity direction as an output of the finite-`I` bookkeeping itself.

The source also explicitly cautions that several Type-I formulations are not known to imply one another. Therefore no unstated norm equivalence is imported.

Primary provenance: arXiv `1811.00502v2`, Theorem 1.1 and definitions/equations (1.1)–(1.6). Verified against the primary PDF in this cycle.

## Exact consumer source

Z. Grujić, **Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations**, arXiv:2607.08866v2 (revised 2026-07-13), is the exact consumer. Its logarithmic-depletion theorem assumes uniform near-first-singular-time critical-profile information together with global `L_t^∞ L_x^{3/2,∞}` vorticity and global `L_t^∞ bmo_phi` vorticity direction for `phi(r)=1/|log r|`; the proof separates near and far Biot–Savart contributions. The later singularity-evasion theorem is a pre-singularity analyticity/escape-time result, not an ancient-solution Liouville theorem.

Primary provenance: arXiv `2607.08866v2`, Definition 2.1, the `bmo_phi` definition, Theorem 4.1, and the main analyticity/escape-time theorem. Verified against the primary arXiv HTML in this cycle.

## Scope conclusion

These two sources suffice for the present **signature falsifier**: the question is whether the numerical `A/C/D/E` quantities alone control the consumer norms. They do not suffice to decide whether the Navier-Stokes equation plus finite `I` yields those norms by additional PDE structure. That equation-specific implication remains open. Global Lorentz/far-field gluing and pre-singularity/ancient state-space matching are separate residuals.

No secondary literature is used as theorem authority in this atom.
