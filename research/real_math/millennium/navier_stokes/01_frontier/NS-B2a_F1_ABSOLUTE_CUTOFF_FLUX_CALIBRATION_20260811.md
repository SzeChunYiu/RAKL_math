# NS-B2a — F=1 ancient-Euler absolute cutoff-flux calibration

**Atom:** `NS-B2a`  
**Cycle authority:** `RETROSPECTIVE_SOURCE_BOUND_ROUTE_DIAGNOSTIC / PROPOSAL_ONLY_V3_EXPERIENCE / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`  
**Framework source of truth inspected first:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`  
**Application base:** `SzeChunYiu/RAKL_math@a071ef22d2478b1603567a9e90202ec3ce99fb59`

## Chronology boundary

This cycle discovered the scaling discriminator before a fresh strict `NS-B2a` pre-candidate `MathContextFiber` was frozen. The result is therefore **retrospective learning evidence only**. It is preserved as a v3 `TaskEpisode`-style record and an `OBSERVED_ONLY` failure proposal. It receives zero prospective pre-candidate credit and cannot be promoted into a theorem candidate by backfilling chronology.

## Primary-source target

Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468v1 (28 June 2026).

Theorem 3.1 produces, under its stated Type-II scenario, an ancient pair `(u,p)` on `R^3 x (-infinity,0)` satisfying:

1. the weighted bound
   \[
   \sup_{a>0}\left[
      \sup_{-a^2<\tau<0}\frac{F(a)^2}{a}\int_{B(a)}|u|^2
      +\frac{F(a)^2}{a^2}\int_{Q(a)}|p|^{3/2}
      +\frac{F(a)}{a}\int_{Q(a)}|\nabla u|^2
   \right]<\infty;
   \]
2. the **Euler**, not Navier-Stokes, equations
   \[
   \partial_\tau u+u\cdot\nabla u+\nabla p=0,\qquad \nabla\cdot u=0;
   \]
3. the local energy inequality (3.7);
4. a source-defined nontriviality condition.

For the logarithmic example (2.10), the paper explicitly states `F(a)=1`.

Hence this branch supplies the scale-critical estimates
\[
A_u(R):=R^{-1}\sup_{-R^2<t<0}\int_{B(R)}|u|^2\lesssim 1,
\]
\[
E_u(R):=R^{-1}\int_{Q(R)}|\nabla u|^2\lesssim 1,
\qquad
D_p(R):=R^{-2}\int_{Q(R)}|p|^{3/2}\lesssim 1.
\]

## Exact discriminator

The issue-level rigidity hope is that some no-incoming-energy or far-field condition might combine with the ancient Euler local-energy inequality and nontriviality to force `u=0`.

Before inventing such a theorem, test the cheapest possible version:

> Do the **canonical absolute cutoff estimates themselves**, using only the `F=1` critical bounds above, acquire a positive power of `R` that makes the incoming boundary terms decay at expanding scales?

Choose a smooth nonnegative space-time cutoff `phi_R` supported in a parabolic cylinder of scale `2R`, equal to one on the corresponding inner cylinder, with
\[
|\partial_t\phi_R|\lesssim R^{-2},\qquad |\nabla\phi_R|\lesssim R^{-1}.
\]

### Local cubic control

Standard local interpolation on `B(2R)` gives
\[
\int_{Q(2R)}|u|^3
\lesssim
\left(\sup_t\int_{B(2R)}|u|^2\right)^{3/4}
\left(\int_{Q(2R)}(|\nabla u|^2+R^{-2}|u|^2)\right)^{3/4}
(R^2)^{1/4}.
\]

Under the scale-critical `A_u,E_u` bounds, the right-hand side is `O(R^2)`. Thus the dimensionless cubic quantity `R^{-2}\int_{Q(R)}|u|^3` stays `O(1)`.

### Time-cutoff contribution

Because
\[
\int_{Q(2R)}|u|^2
\le (4R^2)\sup_t\int_{B(2R)}|u|^2
=O(R^3),
\]
we obtain
\[
\left|\int |u|^2\partial_t\phi_R\right|
\lesssim R^{-2}O(R^3)
=O(R).
\]

### Cubic transport contribution

Using the cubic bound,
\[
\left|\int u\cdot\nabla\phi_R\,|u|^2\right|
\lesssim R^{-1}\int_{Q(2R)}|u|^3
=O(R).
\]

### Pressure transport contribution

By Hölder,
\[
\int_{Q(2R)}|p||u|
\le
\left(\int |p|^{3/2}\right)^{2/3}
\left(\int |u|^3\right)^{1/3}.
\]

Both integrals are `O(R^2)` in their natural powers, hence
\[
\left|\int u\cdot\nabla\phi_R\,2p\right|
\lesssim
R^{-1}\,O(R^{4/3})\,O(R^{2/3})
=O(R).
\]

### Normalized result

The natural localized kinetic-energy scale is itself `R`. Therefore every canonical **absolute** contribution above is only
\[
R^{-1}|T_R|=O(1).
\]

There is no positive power of `R` forcing these upper bounds to vanish as `R -> infinity`, and a dyadic sum of such scale-critical absolute charges has no finite total budget merely from these estimates.

## Scoped result

`F-NS-B2a-F1-ABSOLUTE-CUTOFF-FLUX-NONDECAY`

The `F(a)=1` bounds plus the canonical absolute local-energy cutoff estimate do **not** by themselves provide a decaying large-scale no-incoming-flux certificate.

This statement is deliberately narrow. It does **not** show that the actual signed flux is nonzero. It does **not** rule out:

- signed telescoping or cancellation;
- a monotonicity formula;
- annular energy tightness inherited from the Navier-Stokes prelimit;
- a selected sequence of radii/times with vanishing boundary flux;
- concentration-compactness/minimality producing orbit tightness;
- symmetry-specific Euler Liouville theorems;
- another source-valid Euler rigidity mechanism.

It only removes the naive inference `critical local bound -> decaying absolute boundary flux`.

## DifferenceWitness against the Type-I local-energy audit

Pending RAKL_math PR #54 reports a structurally related Type-I Navier-Stokes result: absolute local-energy shell terms are scale critical after normalization. That pending PR is **not canonical authority** here.

The common abstraction is:

> scale-critical local control can make every absolute shell/cutoff estimate locally finite without making the scale series summable.

The disanalogy is load-bearing:

- Type-I route: viscous Navier-Stokes, including dissipation and the viscous cutoff structure;
- present Type-II route: ancient Euler limit, where the parabolic backward-uniqueness and viscous mechanism are absent.

The present result is therefore re-derived from Seregin's source class rather than imported from PR #54.

## Local-to-global gluing obstruction

The local section supplied by Theorem 3.1 is strong enough to define an ancient nontrivial Euler object with scale-critical local control. The missing **gluing interface** to a global contradiction is not another local bound of the same homogeneity. It is an independently justified tail/interface statement, for example a prelimit-inherited annular tightness condition or a signed flux relation, together with an Euler Liouville theorem whose hypotheses match exactly.

Local control is therefore separated from global rigidity:

`Seregin local ancient-Euler section`
`-> [OPEN: tail/no-incoming-flux interface]`
`-> [OPEN: exact Euler rigidity theorem]`
`-> contradiction`.

## Next child

`NS-B2a1 — EULER_TAIL_TIGHTNESS_OR_SIGNED_FLUX`

Before any theorem candidate, freeze a fresh strict context and ask:

> Can the original Navier-Stokes blow-up sequence supply a content-bound annular/tail condition that survives the Euler scaling and weak limit—such as normalized annular energy/pressure/cubic flux tending to zero along expanding radii, or a signed/telescoping flux potential—without assuming the desired global compactness or rigidity conclusion?

The first hostile controls must include moving centers, profile leakage, multiple separated packets, pressure normalization, and loss of tail information under local weak convergence.

## Authority

`RETROSPECTIVE_SOURCE_BOUND_ROUTE_DIAGNOSTIC / OBSERVED_ONLY_FAILURE / PROPOSAL_ONLY_SEARCH_CONTROL / NO_MATHEMATICAL_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`
