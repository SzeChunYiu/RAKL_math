# NS-B1a3b-C001 — Finite-I / vorticity-geometry state-space and closure interface audit

**Date:** 2026-08-11  
**Authority:** `SOURCE_BOUND_INTERFACE_ROUTE_PRUNING / PROPOSAL_SHADOW / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`  
**Frozen fibre:** `sha256:6dd7969ddde37ed9384dc40064927cdda8b1ba78a536791b21aa06298dbf0900`

## Candidate claim

The currently registered Albritton–Barker finite-`I` Type-I extraction package does **not by itself** satisfy the state-space and nonlinear-observable closure hypotheses used by the selected Giga–Miura vorticity-direction rigidity transfer. Therefore the direct composition

`AB finite I -> ancient limit -> Giga–Miura vorticity-direction rigidity`

is not licensed without an additional bridge. This is a bounded theorem-interface claim. It does not assert that no geometric-depletion route can work for finite-`I` solutions.

## Exact scaling interface

Normalize viscosity to `1`. Under Navier–Stokes parabolic scaling,

`u_lambda(x,t) = lambda u(lambda x, lambda^2 t)`,  
`p_lambda(x,t) = lambda^2 p(lambda x, lambda^2 t)`,  
`omega_lambda(x,t) = lambda^2 omega(lambda x, lambda^2 t)`.

Hence, at points where vorticity is nonzero, its direction

`zeta = omega / |omega|`

is amplitude-scale invariant:

`zeta_lambda(x,t) = zeta(lambda x, lambda^2 t)`.

This makes vorticity direction a natural geometric candidate. Scale invariance alone, however, does not give compactness or inheritance of `zeta` through a blow-up limit.

## Producer and consumer theorem signatures

### Producer: Albritton–Barker finite-I Type-I class

Albritton–Barker use a weak local Type-I quantity `I`, the supremum over parabolic cylinders of the scale-invariant local quantities `A+C+D+E`. Their Theorem 1.1 identifies a Type-I singularity in this sense with existence of a nontrivial mild bounded ancient solution with finite `I`.

Their discussion of stronger Type-I quantities explicitly includes

`c_infinity = sup_t sqrt(T*-t) ||u(t)||_L-infinity`

as a stronger condition from which the weak finite-`I` condition follows. The registered source does not license the reverse implication; indeed it emphasizes that boundedness of one standard Type-I quantity is not generally known to imply boundedness of the others.

At the suitable-weak compactness stage, the available passage is local: after subsequence extraction, velocity converges strongly in `L^3_loc`, pressure weakly in `L^{3/2}_loc`, with the derivative information at the energy/weak level needed for the suitable formulation. This is sufficient for local nonlinear passage and singularity persistence, but it is not a source theorem giving locally uniform convergence of vorticity.

### Consumer: Giga–Miura vorticity-direction geometry

Giga–Miura's whole-space Type-I mild hypothesis is the pointwise self-similar rate

`||u(t)||_L-infinity <= C0 (-t)^(-1/2)`.

Their Theorem 1.1 excludes blow-up when, in addition, vorticity direction is uniformly coherent on the registered high-vorticity sets. Their rescaling argument uses the `L^infinity` mild-solution structure and parabolic regularity to obtain local uniform bounds/convergence for derivatives and vorticity. That stronger convergence is what permits the high-vorticity alignment condition to pass to the nonzero limiting vorticity and collapse its spatial direction. The resulting lower-dimensional bounded ancient class is then consumed by a two-dimensional Liouville argument.

Thus the two appearances of “Type I” are not the same registered state space. A shared label is not an implication certificate.

## Exact limit-passage obstruction: normalized vorticity is not closed by the stated AB topology

The nonlinear observable

`u -> curl(u) / |curl(u)|`

is singular at zero vorticity and depends on derivatives. Strong local `L^3` convergence of velocity plus weak/bounded energy-level derivative control is not, as a matter of topology, enough to pass this observable.

A simple divergence-free calibration on any fixed bounded spatial region is

`w_n(x) = (0, n^{-1} sin(n x_1), 0)`.

Then

`w_n -> 0 strongly in L^3_loc`,

while

`curl w_n = (0,0,cos(n x_1))`

remains order one, has uniformly bounded local `L^2` norm, and its normalized direction alternates between `+e_3` and `-e_3` away from its zero set. Hence neither strong velocity convergence nor bounded first derivatives alone makes normalized vorticity direction compact.

This sequence is **not** asserted to solve Navier–Stokes. It is an adversarial functional-analytic falsifier of the proposed *topological inference*. Any Navier–Stokes-specific rescue must therefore add a dynamics theorem that supplies stronger vorticity compactness, excludes such oscillatory defect behavior, or replaces `zeta` by an exactly closed geometric functional.

## Why the solved Giga–Miura subclass remains valid

The interface failure does not refute or weaken the Giga–Miura result. Inside their stronger `L^infinity` Type-I mild class, the rescaled solutions enjoy the local derivative/vorticity compactness their proof requires. The vorticity-direction coherence condition can then be transferred on regions where the limiting vorticity is nonzero, and the spatially constant direction feeds their dimensional-reduction/Liouville step.

The lesson is scoped: **the stronger convergence belongs to the stronger producer state space and cannot be silently imported into the weak finite-`I` extraction.**

## Recent logarithmic geometric depletion

Grujic, arXiv:2607.08866, supplies a recent near-analogue in which logarithmic regularity of vorticity direction is combined with a critical-point/Lorentz-scale vorticity concentration framework to control vortex stretching. The additional concentration and geometric hypotheses are not derived from AB finite `I` in this cycle. It is therefore retained as a vocabulary/method analogue, not a bridge certificate.

## Pressure localization and far field

This child does not repair the independent `NS-B1a3a` global-tail problem. AB local pressure localization is adequate for local suitable compactness and persistence, but a vorticity-direction condition on intense-vorticity sets does not automatically identify the global harmonic/far-field pressure component or establish global critical tightness. The pressure/far-field interface stays separately open.

## Noncompact symmetries

Translation and dilation profile leakage recorded in `NS-B1a3` remains valid scoped experience. It is not the load-bearing obstruction in this child: the present obstruction already appears at the local derivative/normalized-observable interface. If a future geometric quantity is formulated globally, translation/dilation tightness must be audited again rather than inherited automatically.

## Backward uniqueness and equation-class audit

No backward-uniqueness theorem is invoked here. A future use must verify the selected theorem's exact terminal-time, exterior/global, coefficient/regularity and domain hypotheses for the actual ancient vorticity equation.

Likewise no stationary Leray-profile theorem is substituted for a general time-dependent ancient solution. Passing to exact self-similar variables changes the equation by introducing drift/dilation terms; a theorem for stationary profiles remains confined to that changed equation/class unless exact self-similarity has separately been proved.

## Type-I versus Type-II

Everything in this cycle is conditional on a Type-I blow-up class. It does not classify Type-II blow-up. The AB finite-`I` class and the Giga–Miura `L^infinity` self-similar class are already materially different Type-I state spaces; Type-II requires a different normalization/classification program.

## Falsifier / verification contract

The route-pruning claim is overturned by either of the following source-valid achievements:

1. a theorem proving that every AB finite-`I` object relevant to the blow-up extraction satisfies the Giga–Miura `L^infinity` self-similar Type-I bound with the regularity needed by their compactness step; or
2. a theorem defining an exact vorticity/geometric observable `G` which is controlled in the finite-`I` class, sequentially closed under the actual AB extraction topology, robust at/near zero vorticity, and sufficient for a theorem-matched ancient-solution rigidity result.

Verification performed in this cycle was theorem-signature binding, scaling audit, convergence-topology comparison, the explicit high-frequency divergence-free closure calibration, and separation of pressure/far-field, unique-continuation and equation-change interfaces. No numerical evidence was used.

## Episode -> diagnosis -> obstruction / lesson

**Episode observation.** The finite-`I` blow-up package reaches an ancient solution through local suitable-weak compactness, while the selected geometry theorem is proved in a stronger `L^infinity` Type-I mild state space with local-uniform derivative/vorticity compactness.

**Bounded diagnosis.** There are two distinct missing interfaces: (i) a Type-I state-space implication, and (ii) sequential closure of normalized vorticity direction under the producer topology. The high-frequency calibration supports the second diagnosis as a topological obstruction; it is not a Navier–Stokes counterexample.

**Proposed scoped obstructions.** `O-NS-B1a3b-TYPE-I-STATE-SPACE` and `O-NS-B1a3b-DIRECTION-COMPACTNESS` record the exact producer/consumer mismatches. They do not globally blacklist geometric depletion.

**Proposed lesson, not consolidated.** `L-NS-B1a3b-CHECK-STATE-SPACE-AND-OBSERVABLE-CLOSURE`: before transferring a rigidity theorem, normalize similarly named blow-up classes and prove that every nonlinear observable consumed by the rigidity theorem is closed under the exact producer compactness topology.

## Scoped failure normalization

- `F-NS-B1a3b-TYPE-I-STATE-SPACE-MISMATCH` — the weak AB finite-`I` class is not the registered Giga–Miura `L^infinity` Type-I class; no reverse implication is supplied by the selected sources.
- `F-NS-B1a3b-VORTICITY-DIRECTION-NONCLOSURE` — the stated AB local velocity/energy compactness does not by topology alone pass `curl u / |curl u|`.

These are scoped experience records. Neither is a proof that no alternative equation-specific geometry estimate exists.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS / SOURCE_BOUND_INTERFACE_ROUTE_PRUNING`.

**Failure category:** `STATE_SPACE_AND_NONLINEAR_OBSERVABLE_CLOSURE_INTERFACE`.

**Residual before:** a broad orthogonal suggestion to test whether vorticity-direction/geometric depletion can be inherited by the finite-`I` ancient class and then trigger rigidity.

**Residual after:** open `NS-B1a3b1` for a scale-critical geometric defect functional `G` satisfying all four conditions: (i) dynamics supplies/control of `G` from finite `I` or an independent estimate; (ii) `G` is sequentially closed under the actual AB extraction; (iii) `G` is robust near `omega=0`; and (iv) `G` feeds an exactly matched ancient Liouville/rigidity theorem. The independent `NS-B1a3a` global critical-tail/state-space child remains open, and Type-II remains untouched.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`.

No Type-I exclusion for the full finite-`I` class, Type-II classification, global regularity proof, proof certificate, novelty certificate, or independent mathematical review is created by this audit.

## Primary-source provenance

- Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502.
- Yoshikazu Giga and Hideyuki Miura, *On vorticity directions near singularities for the Navier-Stokes flows with infinite energy*, Hokkaido University Preprint Series 956, DOI 10.14943/84103.
- Zoran Grujic, *Vorticity direction as a geometric depletion mechanism at criticality*, arXiv:2607.08866 (recent preprint; near-analogue only in this cycle).
