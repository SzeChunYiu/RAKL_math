# NS-B1a3b1-C001 R2 — log-BMO zoom stability and Grujic v2 interface audit

**Authority:** `VERIFIED_REPRESENTATION_LEMMA / SOURCE_BOUND_INTERFACE_AUDIT / PROPOSAL_SHADOW / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`

## Exact result

Let
\[
\phi(\rho)=\frac1{|\log \rho|},\qquad 0<\rho<\tfrac12,
\]
and use the global local-BMO norm appearing in Grujic v2,
\[
\|f\|_{\mathrm{bmo}_\phi}
=\|f\|_\infty+
\sup_{x\in\mathbb R^3,\,0<\rho<1/2}
|\log\rho|\,
\fint_{B_\rho(x)}|f-c_{B_\rho(x)}|.
\]

For a zoom-in factor `0<r<=1`, translation `x0`, and
`f_r(y)=f(x0+r y)`, the norm is non-expansive:
\[
\|f_r\|_{\mathrm{bmo}_{1/|\log \rho|}}
\le
\|f\|_{\mathrm{bmo}_{1/|\log \rho|}}.
\]

Indeed, for every target ball `B_rho(y0)`, change of variables gives the exact identity
\[
\fint_{B_\rho(y_0)}|f_r-(f_r)_{B_\rho(y_0)}|
=
\fint_{B_{r\rho}(x_0+r y_0)}|f-f_{B_{r\rho}(x_0+r y_0)}|.
\]
Because `r rho < 1/2`, the source norm applies. Moreover
\[
|\log(r\rho)|=|\log r|+|\log\rho|\ge |\log\rho|,
\]
hence
\[
|\log\rho|\,\operatorname{MO}_{\rho}(f_r)
\le
\frac{|\log\rho|}{|\log(r\rho)|}\,[f]_{\mathrm{bmo}_\phi}
\le [f]_{\mathrm{bmo}_\phi}.
\]
The global `L^\infty` norm is unchanged by the affine bijection `y -> x0+r y`. The same calculation applies componentwise/vectorially to a direction field using the Euclidean norm.

This is a representation/transport lemma. It does **not** derive the log-BMO hypothesis from Navier–Stokes dynamics.

## Time and vorticity scaling

For the Navier–Stokes blow-up map
`omega_r(y,s)=r^2 omega(x0+r y,t0+r^2 s)` and
`xi_r(y,s)=xi(x0+r y,t0+r^2 s)` wherever the direction is defined.

If the source phase satisfies a uniform-in-time global `bmo_phi` bound on an interval `I`, then the same bound holds on the rescaled interval
`I_r={s: t0+r^2 s in I}`.

The global weak-Lorentz vorticity norm is also exactly critical:
\[
\|\omega_r(\cdot,s)\|_{L^{3/2,\infty}(\mathbb R^3)}
=
\|\omega(\cdot,t_0+r^2s)\|_{L^{3/2,\infty}(\mathbb R^3)}.
\]
Thus the **conditional** Grujic phase and Lorentz inputs are compatible with zoom-in. The obstruction is not loss under dilation.

## Primary-source signature audit — arXiv:2607.08866v2

Exact version: Zoran Grujic, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866v2, 13 July 2026.

Definition 2.1 restricts the target to a critical point singularity with a centered `O(|x|^-2)` vorticity profile, a scale-invariant or log-periodic shape factor, uniform boundedness, a critical gradient bound, and high-vorticity superlevel sets trapped in shrinking balls.

Definition 2.3 / equation (2) defines `bmo_phi` by a supremum over **all centers in R^3** and local radii `<1/2`. The phrase “local BMO” refers to the radius cutoff; it is not a bounded-domain hypothesis.

Theorem 4.1 assumes, uniformly near the first possible singular time, both
`omega in L_t^infty L_x^{3/2,infty}(R^3)` and
`xi in L_t^infty bmo_phi(R^3)`.
Its proof splits the commutator into near and far fields. The macroscopic strain and oscillation-tail terms explicitly use the global weak-Lorentz vorticity norm; the dyadic shell term uses phase information on expanding balls. Hence a local finite-`I` compactness statement does not discharge the consumer by itself.

Theorem 7.4 is a **pre-singularity regularity theorem**, not an ancient-solution Liouville theorem. It starts from a unique spatially analytic solution on `(0,T*)`, assumes the critical profile and global uniform bounds on `(T*-\epsilon,T*)`, chooses escape times, evolves forward by local analyticity, and closes with harmonic measure. An ancient Albritton–Barker limit cannot be inserted into that theorem by renaming variables.

## Exact producer/consumer comparison

The merged `NS-B1a3b` cycle already establishes that the registered finite-`I` compactness topology does not by itself transport a normalized-vorticity direction modulus. This R2 cycle resolves a different question:

`assumed global log-BMO phase control -> blow-up zoom`

is stable, but

`finite I -> assumed global log-BMO phase control`

remains open.

Likewise, the source's global `L^{3/2,\infty}` vorticity and far-field inputs are scale-compatible if already present, but the registered finite-`I` producer does not supply them as a global vorticity state-space certificate.

## Vorticity-zero endpoint

The direction `xi=omega/|omega|` is undefined at `omega=0`. The inspected v2 text calls it a unit vector field and takes its global `L^\infty` norm as one, but the source-text search in this cycle did not locate an explicit zero-set extension convention. This is recorded as an applicability obligation, not as a refutation of the paper: a transfer must bind a measurable extension/convention or use a theorem formulation whose geometry is restricted to the nonzero/high-vorticity set.

## Failure separation

**Local mathematical failure:** none in the zoom lemma; the representation transport succeeds.

**Producer/representation failure:** the finite-`I` package still lacks a proved map to the required global uniform phase object. This inherits, but does not enlarge, the merged `NS-B1a3b` derivative/normalization obstruction.

**Local-to-global/gluing failure:** Grujic's depletion estimate consumes global weak-Lorentz vorticity and nonlocal far-field information. Local compactness or bounded-cylinder control cannot be silently glued into those global hypotheses.

**State-space/source-signature failure:** Theorem 7.4 is pre-singularity/forward-analyticity/escape-time machinery, not an ancient Liouville theorem. A same-theory bridge would have to be proved separately if one wants to use it after blow-up extraction.

**Source-applicability warning:** the zero-vorticity convention for the global direction field is not explicit in the inspected v2 text.

## Episode -> diagnosis -> obstruction/lesson

**Episode:** `NS-B1a3b1-C001-R2` tested the prospectively frozen log-BMO zoom discriminator and exact source signature.

**Diagnosis:** the feared scale-loss is absent. The unresolved route is instead producer generation plus global/time/state-space gluing.

**Reusable obstruction/lesson:** when a conditional geometric consumer is scale-compatible, do not spend search budget inventing a compensating renormalization. Move upstream to prove the producer generates the consumer object, and separately bind any global/far-field and pre-singularity/ancient interfaces.

## Outcome and next atom

**Outcome:** `PARTIAL_SUCCESS / REPRESENTATION_BRIDGE_VERIFIED / PRODUCER_AND_GLUING_OPEN`.

The solved bounded subproblem is classified `representation` in the RAKL novelty taxonomy, structural rank `0`: it is an exact representation-transport identity, not a new Navier–Stokes theorem and not a novelty claim.

The next highest-information child is:

`NS-B1a3b1a — FINITE-I TO GLOBAL LOG-BMO/Lorentz PRODUCER TEST`

Question: can exact finite-`I` Navier–Stokes dynamics produce a uniform-in-time, scale-matched phase/amplitude certificate strong enough to imply the global `bmo_{1/|log r|}` and `L^{3/2,\infty}` inputs on the pre-singularity solution itself, without assuming derivative regularity, global vorticity tightness, or the desired geometry? Counterexample-first alternatives should include far-field packets, zero-vorticity phase instability, and moving-center/profile leakage.

The orthogonal sibling `NS-B1a4` pressure-temporal/no-recrossing remains open, as do global critical tightness and Type-II classification.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`. No Type-I exclusion, Type-II result, proof DAG closure, independent review, or root promotion is created.

## Source provenance

- Grujic v2 HTML: https://arxiv.org/html/2607.08866v2
- Grujic abstract/version record: https://arxiv.org/abs/2607.08866
- Albritton–Barker producer: https://arxiv.org/abs/1811.00502
- RAKL current framework subject: `fe47a12c4bad8253658baaf37e1300cab15d0823`
- RAKL_math cycle base: `9932f136c0e1cd689fd3dcd1ab5a5497fbbe9ebc`
- Pre-action receipt: `e48d16f0f14e066e6620d402a81ad1d5d7a47affb02a303600f38d507aacfd19`
