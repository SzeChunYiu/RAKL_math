# H4d1c-e closed top-dimensional source-image certificate

**Date:** 2026-08-12  
**Atom:** `H4d1c-e`  
**Parent residual:** `O-H4D1C-TOTAL-WITNESS-NONVERTICAL-HODGE-BRANCH-COVERAGE`  
**Authority:** `SCOPED_SUFFICIENT_CERTIFICATE / PROPOSAL_SHADOW / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`

## Exact question

C004 established that enlarging a total-witness tangent space does not by itself enlarge the image in the Hodge-deformation base: new source directions may be vertical. The smallest remaining local question is therefore not how large the source tangent is, but when the **actual image germ** of a genuinely varying algebraic-witness incidence already fills one exact Hodge-locus component.

Fix a smooth-projective family locally near `s`, a flat rational class `alpha` (after a simply connected/local-system trivializing shrink), and one **reduced irreducible** local component `H` of the Hodge locus of `alpha` through `s`. The central witness is assumed already algebraic; this is a propagation subproblem and does not solve root initial algebraicity.

## Scoped source-image certificate

Let `pi : W -> H` be a local algebraic/analytic incidence source whose points parameterize actual algebraic-cycle witnesses. Write `L = (pi(W))_red` as an image germ at `s`. Assume:

1. **Exact same-class binding:** every witness over `t` has rational cycle class equal to the locally transported class `alpha_t`; no substitution by an unrelated effective class or by componentwise Hodge persistence is allowed.
2. **Closed image:** `L` is a closed reduced analytic/algebraic subgerm of `H`. A proper/projective incidence map is a standard way to obtain this property, but closedness is the actual hypothesis used below.
3. **One irreducible target component:** `H` is reduced and irreducible as a germ. For a reducible Hodge locus the test must be run component by component.
4. **Top-dimensional image:** `dim_s L = dim_s H`.

Then `L = H` as reduced germs.

### Proof

Because `L` is a closed reduced subgerm of the reduced irreducible germ `H`, if `L` were proper then its underlying closed analytic/algebraic subset would have strictly smaller dimension than `H`. This contradicts `dim_s L = dim_s H`. Hence `L=H` as reduced germs.

By exact same-class binding, every point of the local Hodge component is therefore in the image of at least one algebraic witness representing `alpha_t`. Thus the certificate gives **set-theoretic local branch coverage** for this conditional variational subproblem.

This proof is elementary dimension theory; the substantive future work is to construct a source for which the four hypotheses are true.

## Why this is stronger than the C004 tangent heuristic

C004's countermodel allows `T_w W` to grow while `im(d pi)` does not. The present certificate never infers target coverage from source tangent dimension. It works directly with the reduced image germ. In singular situations it can establish set-theoretic branch coverage even though no smooth local section or tangent-surjectivity statement has been proved.

Consequently this certificate does **not** prove equality of scheme structures, formal smoothness, infinitesimal lifting at all Artin orders, or existence of a holomorphic/algebraic section of `pi`.

## Adversarial boundary tests

- **Delete closedness.** A proper dense constructible/analytic subset can have the same dimension as `H`; full dimension alone does not force equality. This reopens the C004 failure in image form.
- **Delete irreducibility/component binding.** If `H=H1 union H2` with equally dimensional components, the closed subset `L=H1` has `dim L=dim H` but misses `H2`.
- **Delete exact-class binding.** A source may dominate `H` while its witnesses represent a different class `beta`; image coverage then says nothing about algebraicity of `alpha`.
- **Demand nonreduced/scheme-theoretic equality.** Equality of reduced germs does not control nilpotents or formal neighborhoods. This is deliberately outside the certificate and must be tested in a higher-Artin atom.
- **Ignore monodromy.** Away from a local trivialization, the phrase 'the same class alpha' can be path-dependent. The certificate is local and requires a fixed flat marking.
- **Replace a signed rational witness by separately persistent components.** C001 already showed that total Hodge tangency need not imply componentwise tangency because cancellations can occur. A source built from component tuples is admissible only if its own exact total-class equation and image hypotheses are independently proved.

All hostile tests preserve the root coefficient/category boundary and show why none of the four hypotheses is dispensable in the stated form.

## Primary-source calibration and disanalogies

Cattani--Deligne--Kaplan prove algebraicity of the locus where a fixed Hodge class remains Hodge in a smooth projective family. This supports treating the Hodge locus as a geometric target, but it does not construct algebraic-cycle witnesses.

Kloosterman's complete-intersection-on-hypersurface theorem has the closest solved-class shape. It studies a flag Hilbert source of pairs `(Y,Z)`, computes the dimension of the hypersurface locus reached by such pairs, and proves in that special complete-intersection setting that the relevant Hodge locus is smooth at `Y` and is contained in the locus of hypersurfaces containing a complete intersection of the specified multidegree. This is precisely the kind of **source-image completeness statement** that C004 says is needed. It is a special-family theorem, not a transfer to arbitrary rational Hodge classes.

Buchweitz--Flenner's semiregularity theory is a second positive deformation analogue: semiregularity has consequences for Hilbert schemes and the variational Hodge conjecture. It was retrieved but rejected as a general root transfer because its coherent-module/subspace hypotheses do not by themselves supply a coupled source for an arbitrary signed rational cycle.

Primary sources consulted:

- E. Cattani, P. Deligne, A. Kaplan, *On the locus of Hodge classes*, arXiv:alg-geom/9402009.
- R. Kloosterman, *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space*, arXiv:2104.14845.
- R.-O. Buchweitz, H. Flenner, *A semiregularity map for modules and applications to deformations*, arXiv:math/9912245.

## Same-context expert cell

**VHS/Hodge-locus lead.** Freeze one reduced irreducible component and one locally flat class before comparing dimensions; otherwise component switching or monodromy can fake coverage.

**Hilbert/Chow deformation lead.** The right consumer is the closed image in the base. Proper/projective source geometry is useful because it can certify closedness, but properness is not itself a dimension or class-binding certificate.

**Algebraic-cycle coefficient lead.** A rational signed tuple can be used only with a proved total-class identity. No componentwise Hodge-persistence inference is imported from the total class.

**Deformation/formal lead.** Reduced image equality is strictly weaker than scheme-theoretic or higher-Artin lifting. Formal smoothness, compatible thickenings and algebraization remain separate atoms.

**Variational-analogue lead.** Kloosterman is selected because its flag-incidence theorem controls the varying ambient base; Buchweitz--Flenner is retained only as a semiregularity-shaped analogue with a coefficient/object disanalogy.

**Adversarial verification/RAKL lead.** Deleting closedness, irreducibility, class binding or reduced-scope discipline gives immediate counterexamples. The lemma is therefore a scoped sufficient certificate, not a theorem-generation shortcut. This same-context review receives zero independent-review credit.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS / VERIFIED_SCOPED_SUFFICIENT_CERTIFICATE`.

The prior residual is not globally solved; it is transformed into the sharper source-specific obstruction `O-H4D1C-SAME-CLASS-CLOSED-TOPDIM-SOURCE-IMAGE`: construct, for a nontrivial varying smooth-projective family and an exact signed rational class, a witness incidence whose reduced image in each target Hodge component is closed and top-dimensional while preserving exact class identity.

If such a certificate is obtained, the next frozen atom must separately test higher Artin order/formal compatibility and then algebraization. Monodromy beyond the local marking, singular degeneration/specialization, global continuation/domination, and root initial algebraicity remain open.

This cycle resolves a **local source-image sufficiency lemma**. It does not repair global gluing, does not provide a general witness source, and does not alter root status `OPEN_NO_SOLUTION_CERTIFICATE`.
