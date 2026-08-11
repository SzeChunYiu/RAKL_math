# NS-B1a3b1b1 source audit — finite-center context lift

Authority: `PROPOSAL_SHADOW_SOURCE_BINDING / NO_ROOT_AUTHORITY`.

## Primary consumer: Grujić arXiv:2607.08866v2

Current primary HTML checked 2026-08-11: `https://arxiv.org/html/2607.08866v2`.

- **Definition 2.1** defines a critical point singularity centered at one spatial point and states that, for high thresholds, `A_lambda(t)` is contained in one ball `B_R` with `R <= C lambda^-1/2` and time-independent `C`.
- **Theorem 4.1**, equation (8), gives for sufficiently small `R`
  `||alpha(.,t)||_{L^{3/2,infinity}(B_R)} <= C0/|log R|`, uniformly in time, with `C0` depending on the uniform global vorticity `L^{3/2,infinity}` and direction `bmo_{1/|log r|}` bounds.
- The proof uses a near-field ball `B_{2R}`, BMO averages/extensions, a translation-invariant Calderón–Zygmund commutator, and far-field annuli. Translating coordinates from the origin to `x0` translates all local balls/averages while preserving the global Lorentz and bmo suprema. Therefore the **localized estimate itself** is translation-covariant with the same uniform constant. This is a proof-level context lift; it does not change the theorem's stated critical-profile hypothesis.
- **Equations (23)-(25)** show the exact downstream consumer. The nonlinear stretching term is bounded by
  `||alpha||_{L^{3/2,infinity}(A_lambda)} ||omega_lambda||_{L^{6,2}}^2`, and equation (25) obtains smallness of the restricted `alpha` norm by containing `A_lambda` in the one shrinking ball and invoking Theorem 4.1.
- Equation (27) begins the linear-source estimate with the same restricted `alpha` norm. Thus fixed multiplicity propagates as a fixed constant loss in the displayed energy estimates rather than destroying the logarithmic decay.

The scoped question is therefore not whether the source *states* a finite-center theorem; it does not. The question is whether the proof interface that feeds equations (23)-(25) preserves its QoI under a finite union of translated local balls. The candidate proves that bounded-union statement separately.

## Primary producer: Albritton–Barker arXiv:1811.00502v2

Current primary abstract checked: `https://arxiv.org/abs/1811.00502`.

Albritton–Barker characterize local Type-I singularities through nontrivial mild bounded ancient solutions satisfying Type-I decay and prove a Liouville result under an `L^3` backward-sequence condition. This source remains the producer-side context. Nothing in this cycle upgrades its finite-`I`/Type-I information to a bounded finite-center high-vorticity cover, global vorticity `L^{3/2,infinity}`, or log-BMO direction control.

## Near-solved analogue: Barker arXiv:2111.14776v2

Current primary abstract checked: `https://arxiv.org/abs/2111.14776`.

Barker proves that a weak Leray–Hopf solution with a sequence of time slices uniformly bounded in velocity `L^{3,infinity}` by `M` has at most `O(M^20)` singular points at the terminal time. This is useful only as a structural finite-multiplicity analogue.

### DifferenceWitness

1. Barker's global velocity `L^{3,infinity}` hypothesis is different from and stronger/global relative to the local finite-`I` producer being audited here.
2. Finitely many terminal singular points do not imply a pre-singularity cover of every high-vorticity super-level set by balls of radius `O(lambda^-1/2)`.
3. Velocity `L^{3,infinity}` is not the same state coordinate as vorticity morphology.
4. Barker's result does not produce the global vorticity weak-`L^{3/2}` and direction log-BMO assumptions used by the Grujić consumer.

No theorem is transferred across this DifferenceWitness.

## Negative history retained

The preceding `NS-B1a3b1b` two-core hostile family established only that weak-`L^{3/2}` amplitude does not select a unique core. It did not show that a bounded finite-center cover is impossible for actual Navier–Stokes Type-I solutions. The present cycle uses that failure to relax the consumer interface rather than to claim a producer theorem.
