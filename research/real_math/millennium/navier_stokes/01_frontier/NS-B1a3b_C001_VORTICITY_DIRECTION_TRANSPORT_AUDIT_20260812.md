# NS-B1a3b-C001 — Vorticity-direction transport / geometric-depletion interface audit

**Date:** 2026-08-12  
**Authority:** `SOURCE_BOUND_INTERFACE_ROUTE_PRUNING / SAME_THEORY_GEOMETRY_CONSUMER_ACCEPTED / BARE_DIRECTION_TRANSPORT_BLOCKED / COMPUTATION_ANALYTIC_CALIBRATION_ONLY / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`

## Executive finding

The geometry lane is genuinely orthogonal to the global-tail obstruction found in `NS-B1a3`, but it has its own exact glue problem.

Lei–Ren–Tian (arXiv:2501.08976) supplies a same-theory, local suitable-weak **geometric regularity consumer**: if high-vorticity directions remain in a fixed double cone, the potential singularity is regular. Their Corollary 1.5 gives the sharp contrapositive range picture: at a singular point, the limiting high-vorticity direction set meets every great circle on `S^2`.

The Albritton–Barker Type-I blow-up package supplies the relevant **producer** of an ancient suitable-weak/mild bounded limit, but the registered compactness is velocity-strong locally with only weak derivative information from the local-energy bound unless a stronger derivative compactness theorem is added.

A fixed double-cone constraint on vorticity is **not weakly closed under that derivative-level topology**. An explicit smooth divergence-free calibration below has

`u_n -> u strongly in L3_loc`,

with uniformly bounded local gradients and `curl u_n` lying in one fixed double cone for every `n`, while the weak limiting vorticity points *outside* that double cone.

Therefore the shortcut

`finite-I blow-up compactness + geometric criterion => inherited ancient directional rigidity`

is not licensed by the currently registered producer topology. This does **not** invalidate Lei–Ren–Tian: their proof uses an additional equation-specific absolute-vorticity-flux mechanism before and through blow-up. It means that this extra mechanism, or another explicit vorticity-level transport certificate, cannot be silently replaced by bare velocity compactness.

## Exact same-theory geometry consumer

For a suitable weak solution on `Q(1)`, Lei–Ren–Tian Theorem 1.1 assumes that there are a unit vector `e`, `delta>0` and `M>0` such that at every regular point either

`|omega| <= M`

or

`|xi x e| <= 1-delta`,  with `xi=omega/|omega|`.

Then the solution is regular on the smaller cylinder. After rotation to `e=e3`, their equivalent formulation is a one-component domination

`|omega| <= C |omega_3| + M`.

Their Corollary 1.5 states that the limiting high-vorticity direction set meets every great circle exactly in the singular case. Thus the theorem is not evidence that a generic Type-I singularity is coherent; it states that **failure of sufficient directional spread is incompatible with singularity**.

This consumer is local suitable-weak and therefore does not require the global `L3(R3)` backward sequence, global pressure identification, or spatial-tail tightness blocked in `NS-B1a3`.

## Producer topology from the Type-I blow-up lane

The registered Albritton–Barker/local suitable-weak compactness passage gives, after rescaling and subsequence extraction on fixed cylinders,

- strong local `L3` convergence of velocity;
- weak local `L^{3/2}` convergence of pressure;
- uniform local-energy bounds, hence bounded gradients and subsequential weak derivative information;
- persistence of the selected singular core under the source hypotheses.

This is sufficient for the local velocity nonlinearity and suitable-weak limit. The vorticity direction, however, is the composite observable

`u -> curl u -> curl u / |curl u|`.

The first map loses a derivative; the second is nonlinear and singular at zero. A separate transport theorem is therefore required before a pointwise/range condition on `xi` can be treated as an inherited property of the ancient limit.

## Exact adversarial calibration: a fixed double cone can be lost in the weak vorticity limit

This calibration is **not a Navier–Stokes solution**. It tests only the functional-topological inference consumed by the proposed glue.

Fix constants `a,b>0` and define, on `R^3`,

`u_n(x) = (0, -(b/n) cos(n x_1), -(a/2)x_1 + (a/(4n)) sin(2n x_1)).`

Each `u_n` is smooth and divergence free. On every fixed compact set,

`u_n -> u := (0,0,-(a/2)x_1)`

uniformly, hence strongly in local `L3` (indeed in every finite local `Lp`). The gradients are uniformly locally bounded. A direct curl calculation gives

`omega_n = curl u_n = (0, a sin^2(n x_1), b sin(n x_1)).`

The limiting field has

`omega = curl u = (0,a/2,0)`,

and `omega_n` converges weakly to `omega` locally.

For every `n`, the horizontal component relative to `e3` satisfies

`|omega_{n,h}| = a sin^2(n x_1) <= (a/b) |omega_{n,3}|`.

Consequently every nonzero `omega_n` lies in the **same fixed double cone** about `+/-e3`. More explicitly,

`|xi_n x e3| <= kappa/sqrt(1+kappa^2) < 1`,  where `kappa=a/b`.

At the zeros of `omega_n`, the low-vorticity alternative in the geometric criterion is available. Yet the weak limiting vorticity is horizontal:

`omega=(0,a/2,0)`, so `|xi x e3|=1` wherever the limit direction is defined.

Thus even

`strong velocity convergence + uniform local H1-type control + fixed double-cone membership of every approximating vorticity`

does **not** imply fixed double-cone membership of the weak limiting vorticity.

The mechanism is branch mixing: the double cone is the union of two opposite cone branches and is nonconvex. Oscillation between the `+e3` and `-e3` branches can weakly average into a transverse vector. This is a sharper obstruction than the generic statement “derivatives may oscillate.”

## Diagnosis ledger

### Episode observation

The registered velocity/local-energy compactness output does not decide the vorticity-direction range consumed by the selected geometric regularity theorem.

### Competing diagnoses

1. **Derivative-loss / weak-closure diagnosis — SUPPORTED.** Strong local velocity convergence does not yield strong vorticity convergence; the calibration keeps gradients uniformly bounded while producing an order-one oscillatory curl.
2. **Nonconvex branch-mixing diagnosis — SUPPORTED and more specific.** A two-sided double cone is not weakly closed; opposite oriented branches can mix into a transverse weak limit.
3. **Normalization/high-vorticity-set instability — SUPPORTED AS SECONDARY.** `xi=omega/|omega|` is singular at zero and moving superlevel sets are not controlled by weak vorticity convergence.
4. **Far-field pressure diagnosis — REJECTED AS PRIMARY FOR THIS CHILD.** The selected Lei–Ren–Tian consumer is local; global pressure/tail control is not its theorem-input requirement.
5. **Noncompact translation/dilation diagnosis — DEFERRED.** Those symmetries remain relevant to global critical elements, but the fixed-cylinder derivative transport already fails before that stage.
6. **Backward-uniqueness diagnosis — NOT INVOKED.** Geometry bypasses rather than discharges the unique-continuation hypotheses recorded in `NS-B1a3`.
7. **Equation-change diagnosis — NOT INVOKED.** No stationary Leray-profile theorem is used here; a general ancient solution remains time dependent.

## Scoped obstruction

`O-NS-B1a3b-VORTICITY-DIRECTION-TRANSPORT-INTERFACE`

> The current Type-I producer supplies local velocity compactness and weak derivative control, while the selected geometry consumer requires a nonlinear, derivative-defined directional-range condition. Because the two-sided cone is nonconvex and can be destroyed by weak branch mixing, a valid glue requires an additional equation-specific vorticity-level transport certificate.

This obstruction is falsified by any source-valid theorem that supplies enough compactness/structure to pass the exact geometric hypothesis for the relevant Navier–Stokes rescalings.

It is **not** a theorem that vorticity geometry cannot rule out Type-I singularities.

## What would be a sufficient transport certificate?

Several interfaces would be logically adequate, if proved from the active hypotheses:

1. **Strong local vorticity convergence.** If `omega_n -> omega` strongly in a suitable local space, one can extract almost-everywhere convergence and pass membership in a fixed closed cone away from the zero set, with the shrinking low-vorticity threshold handled explicitly.
2. **Single-branch/orientation compactness.** Weak convergence can preserve membership in a closed convex cone, but the Lei–Ren–Tian double cone has two branches. A source-valid mechanism preventing `+/-` branch mixing, or controlling an oriented/flipped vorticity with its sign transitions, could repair the interface.
3. **Measure/Young-measure control.** A proof that the vorticity Young measure is supported on one branch or has no transverse barycentric defect would address exactly the calibration above.
4. **Source-native flux transport.** Lei–Ren–Tian work with an absolute-vorticity flux and a modified/flipped vorticity. A theorem showing that the relevant flux measure has the needed tightness, lower-semicontinuity and local decay under the Type-I rescalings would avoid asking raw `xi` to be compact.
5. **Direct pre-limit geometry.** If the finite-I dynamics itself forces high-vorticity directions into a forbidden cone/range configuration at some singular scale, Lei–Ren–Tian can be applied to the original suitable weak solution. This bypasses the ancient-direction transport problem entirely.

None of these certificates is supplied by the current cycle.

## Relation to the Lei–Ren–Tian proof

There is no conflict with the source theorem. Their direction restriction is an input on the pre-limit suitable weak solution. They then exploit the Navier–Stokes vorticity equation, local absolute-vorticity flux, and De Giorgi decay to obtain the contradiction. The current calibration shows why that equation-specific machinery is mathematically meaningful: bare weak derivative compactness would not preserve the nonconvex directional restriction by itself.

Accordingly, the source-native absolute-flux variable is a higher-value next interface than attempting to carry pointwise `xi` through the Albritton–Barker compactness by assertion.

## Type-I / Type-II and orbit-class audit

- The result is conditional on the Type-I finite-control lane and does not classify Type-II blow-up.
- It neither forces nor excludes exact backward self-similarity, DSS behavior, or genuinely nonperiodic ancient dynamics.
- It does not construct a minimal critical element and does not repair the global critical-tightness prerequisite from `NS-B1a3`.
- It does identify a local route that avoids that global prerequisite, provided a geometric input or stable flux observable can actually be derived.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS / SOURCE_BOUND_GEOMETRY_ROUTE_PRUNING_AND_REFACTORING`.

**Residual before:** reopen vorticity-direction/geometric depletion as an orthogonal alternative after the global critical-element glue was blocked.

**Residual after:** the geometry family splits into two exact descendants:

- `NS-B1a3b1`: **vorticity-flux / branch-compactness certificate** — determine whether finite-I dynamics supplies a source-valid oriented/flux observable stable enough under blow-up to replace raw direction transport;
- `NS-B1a3b2`: **direct pre-limit great-circle/cone contradiction** — search for an equation-specific consequence of finite-I that forces directional range to omit a great circle (or otherwise activates an exact local geometry theorem) without first passing `xi` to an ancient limit.

Global critical tightness (`NS-B1a3a`) remains independently open. Type-II remains open.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`.  
**Root authority:** `NONE`.

No Type-I exclusion, Type-II classification, global regularity theorem, formal proof certificate, independent review, or root promotion is created here.

## Primary-source provenance

- Zhen Lei, Xiao Ren, Gang Tian, *A geometric characterization of potential Navier-Stokes singularities*, arXiv:2501.08976: Theorem 1.1, Corollaries 1.5–1.6, Definition 2.2, and the absolute-vorticity-flux / blow-up / De Giorgi mechanism described in Sections 1–4.
- Dallas Albritton, Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502 / J. Math. Fluid Mech. 21 (2019), 43: Type-I ancient-solution equivalence and local compactness package.
- Yoshikazu Giga, Hideyuki Miura, *On vorticity directions near singularities for the Navier-Stokes flows with infinite energy*, Hokkaido University Preprint Series 956 (2010), later Commun. Math. Phys. 303 (2011): analogue family only in this cycle.
- Zoran Grujic, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866 (2026): recent orthogonal analogue with additional concentration and weighted-BMO hypotheses.
