# NS-B2a1 source-tail inheritance audit

**Atom:** `NS-B2a1 — EULER_TAIL_TIGHTNESS_OR_SIGNED_FLUX`  
**Action:** `SOURCE_TAIL_INHERITANCE_AUDIT`  
**Pre-action receipt:** `sha256:58168d53d2982741d635fcd2436d4bc3d1f8691b6cc9c03b28ad352a6cb6c3e6`  
**Pre-action freeze commit:** `dbf0805599843a5c96c0d3a5942a751c393cd023`  
**Framework read:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@4838969ecc18a091da79a059b58b8568634289b7`  
**Authority:** source-bound route discriminator only; no Euler theorem candidate, no Navier–Stokes theorem, no root authority.

## Predeclared discriminator

The audit asked whether Seregin's Type-II Euler-scaled sequence carries either

1. a nonnegative annular/tail functional `T_k(R)` satisfying a source-backed estimate of the form

   `lim_{R→∞} limsup_{k→∞} T_k(R) = 0`,

   with the normalization needed for the `F(a)=1` branch; or
2. an exact signed local-energy-flux cancellation/telescoping identity that remains valid through the Euler limit and can replace nonnegative tail tightness.

The predeclared branch taken by the inspected evidence is **B: ONLY_LOCAL_COMPACTNESS_AND_CRITICAL_BOUNDEDNESS**. Branch C remains open rather than refuted.

## Primary-source observations

### Seregin 2026: what is actually inherited

In arXiv:2606.29468v1, the source scaling first gives the prelimit estimate (2.9), uniform for `0<a<1/λ`, on the weighted local energy, gradient and pressure quantities. The compactness step then extracts subsequences for which, for **each fixed `a>0`**, the scaled velocities converge strongly in local `L^{3ν}(Q(a))`, weak-star in `L_{2,∞}(Q(a))`, and the gradients converge weakly in `L_2(Q(a))`.

Theorem 3.1 produces an ancient Euler pair `(u,p)` on `R^3×(-∞,0)` with the scale-weighted bound (3.5), the Euler equation (3.6), local energy inequality (3.7), and nontriviality (3.8). In the logarithmic example immediately after the theorem the paper states `F(a)=1`. Thus the displayed kinetic-energy and gradient coordinates are scale critical rather than radius-decaying.

The inspected theorem/proof gives a **uniform upper bound** over scales and local convergence on every fixed cylinder. No explicit source estimate of the predeclared vanishing annular-tail form was identified in this route. The full-text audit also found no annular/tail statement that can simply be substituted for the missing witness.

This does not prove that Euler dynamics can never imply such a tail theorem. It identifies exactly what is not supplied by the displayed compactness and critical bounds themselves.

### Seregin 2025/2026: Liouville closure uses extra structure

The earlier Type-II note arXiv:2507.08733v2 makes the downstream interface explicit. Section 4 starts from an ancient Euler solution satisfying its baseline local energy inequality and scale bound, but its Liouville conclusions add further hypotheses. Proposition 4.1 is a self-similar-profile result with an extra growth restriction. The axisymmetric route adds higher derivative/time-derivative control, a pointwise velocity condition away from the symmetry axis, and a global vorticity-integrability condition before Proposition 4.2 obtains its conservation statement and zero-vorticity conclusion.

Accordingly, these results calibrate the intended architecture:

`Euler extraction + baseline scale bounds`  
`!=`  
`generic Euler rigidity`.

Every extra rigidity hypothesis must be independently inherited by the current `F(a)=1` branch.

## Exact quantifier/interface defect

Let `v_k` denote the Euler-scaled sequence. The source compactness has the logical shape

`for every fixed a, after subsequence extraction, v_k -> u on Q(a)`.

A tail statement has a different quantifier order, for example

`lim_{R→∞} limsup_{k→∞} T_k(R)=0`.

The former does not imply the latter without a uniform tightness/modulation estimate. The issue is not cosmetic notation: the large-radius limit is outside each fixed compactness cylinder, and translation is a noncompact symmetry.

### Critical-shell kinematic falsifier

The insufficiency of **local convergence plus the displayed critical scale charges**, considered as abstract analytic information, can be seen without constructing an Euler solution.

Choose a nonzero smooth compactly supported divergence-free field `φ` supported in `B(0,1/8)` and radii `R_k→∞`. Put

`x_k = (3/2) R_k e_1`,

`w_k(x,t) = R_k^{-1} φ((x-x_k)/R_k)`.

For every fixed bounded cylinder `Q(a)`, `w_k=0` there for all sufficiently large `k`, so `w_k→0` strongly locally. Yet the support lies in the annulus `B(2R_k)\B(R_k)` and

`(1/R_k) ∫ |w_k(x,t)|² dx = ||φ||²_2`,

while over a time interval of length `R_k²`,

`(1/R_k) ∫_{-R_k²}^0 ∫ |∇w_k|² dx dt = ||∇φ||²_2`.

Thus a packet can escape to spatial infinity while carrying order-one mass in exactly the critical kinetic-energy and spacetime-gradient normalizations. Adding a fixed compactly supported field `ψ` gives `ψ+w_k→ψ` locally, so even a nontrivial local limit does not remove the escaped critical packet.

**Scope of this falsifier:** `w_k` is not asserted to solve Euler or Navier–Stokes and is not a counterexample to Seregin's theorem. It falsifies only the inference

`fixed-cylinder convergence + critical scale-charge boundedness => global annular tightness`.

Any successful B2a rigidity route must therefore use additional PDE structure, a source-derived tightness/recentering mechanism, or a genuine signed-flux cancellation.

## Result

The strongest source-bound conclusion of this action is:

> The `F(a)=1` Type-II extraction supplies fixed-radius compactness and scale-critical boundedness, but these analytic ingredients do not by themselves establish the large-radius tail/no-incoming-energy property required by the proposed generic Euler-rigidity bridge. The missing interface is the stability of an annular/tail or signed-flux quantity under the double limit from the Navier–Stokes blow-up sequence to the ancient Euler field.

This is a **scoped gluing obstruction**, not a theorem of nonexistence.

## Residual opened

`O-NS-B2a1-DOUBLE-LIMIT-TAIL-INHERITANCE`

Exact residual:

> Define, from the original suitable-weak Navier–Stokes sequence and its Euler scaling, the weakest non-circular quantity whose source hypotheses prove either (i) uniform annular tightness through `lim_{R→∞} limsup_k`, or (ii) an exact signed local-energy-flux cancellation/telescoping law. Then prove that the property survives to the ancient Euler limit and matches every hypothesis of a specific Euler rigidity theorem.

Candidate generation remains blocked. The next prospective child should be chosen only after deciding between:

- `NS-B2a1a — PRELIMIT_ANNULAR_TIGHTNESS`, or
- `NS-B2a1b — SIGNED_EULER_FLUX_TELESCOPING`.

## Source anchors checked 2026-08-11

- Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468v1, especially (2.9), the fixed-`Q(a)` compactness step, Theorem 3.1 and the `F(a)=1` example.
- Gregory Seregin, *A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations*, arXiv:2507.08733v2, Sections 3–4, especially Propositions 4.1–4.2 and their added hypotheses.
- Gregory Seregin, *Remarks on Type II blowups of solutions to the Navier-Stokes equations*, arXiv:2304.04045, as a prior Euler-scaling calibration.

## What this changes

Before this action, the route-level residual was broad: "obtain Euler tail tightness or signed flux." After this action, the obstruction is pinned to a quantifier and topology mismatch:

`fixed-a compactness`  
`vs.`  
`uniform k large-radius tail control`.

That sharper interface prevents a premature Euler Liouville theorem search from merely assuming away the exact global information lost by local compactness.
