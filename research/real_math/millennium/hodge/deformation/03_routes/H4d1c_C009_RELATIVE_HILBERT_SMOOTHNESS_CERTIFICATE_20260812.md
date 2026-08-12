# H4d1c-C009 — relative Hilbert smoothness is a sufficient integrability producer

**Authority:** `PROPOSAL_SHADOW / CONDITIONAL_LOCAL_CERTIFICATE / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.

## Exact local consumer

Fix a smooth-projective complex family over a local base `S`, one locally marked rational class `alpha`, and one reduced irreducible local Hodge-locus branch `H -> S`. Suppose an exact signed-`Q` witness incidence `pi: W -> H` has already been constructed with:

1. every point of `W` representing the exact transported class `alpha_h`;
2. `pi` proper; and
3. near a selected central witness `w0`, `W` is obtained by base change from a finite fibre product over `S` of fixed-polynomial relative Hilbert factors `H_i -> S` through selected component points `z_i`.

The exact question is which local hypothesis on those factors is sufficient to feed merged C007's proper-plus-smooth image certificate.

## Scoped certificate

Assume each relative Hilbert morphism `H_i -> S` is **smooth at `z_i`**. Then their finite fibre product

`P = H_1 x_S ... x_S H_r -> S`

is smooth at the tuple `z=(z_1,...,z_r)`.

Proof: for two factors, `H_1 x_S H_2 -> H_1` is the base change of the smooth map `H_2 -> S`, hence is smooth near the tuple; composing with the smooth map `H_1 -> S` gives smoothness over `S`. Iterate. Smoothness is local on the source, so pointwise hypotheses suffice after shrinking. Base change along `H -> S` preserves smoothness, hence the induced exact-class incidence is smooth at `w0`.

Now use the separate image guards. A smooth morphism is open near `w0`; a proper morphism has closed image. Since the target branch `H` is irreducible, the image is a closed subset containing a nonempty open subset, hence equals `H`.

Therefore:

> **Conditional local branch-coverage certificate.** An exact-class proper incidence built from relative Hilbert factors covers the entire chosen irreducible Hodge branch if all of its load-bearing relative Hilbert factors are smooth over the ambient deformation base at the selected tuple.

This is a composition of standard smoothness/properness facts with the already merged C007 image certificate. It is not a new theorem about Hodge classes.

## Counterexample-first boundary audit

The certificate survives the registered base-change/product/properness attacks. Four tempting weakenings do not receive authority:

1. **Selected-point tangent surjectivity.** C007's cusp already shows this can be nonintegrable at a singular source.
2. **Necessity of selected-point rank.** C006's ramified map already shows full image can coexist with zero derivative at the selected point.
3. **Smoothness of the fixed-fibre Hilbert scheme.** This is not the same datum as smoothness of the relative map `H_i -> S`. The latter must lift ambient-base directions. No inference is made from fibrewise smoothness alone.
4. **Bare `H^1(N)=0` slogan.** For regular embeddings, normal-sheaf cohomology is a standard deformation/obstruction interface, but this packet does not treat a bare vanishing as a universal relative-smoothness theorem. A future source route must bind the exact relative obstruction map and hypotheses that put every ambient Hodge-branch direction into the liftable locus.

The fourth guard matters operationally: otherwise the route would simply relabel the old Hodge-versus-geometric lifting problem as an "unobstructed component" assumption.

## Source-family calibration

Kloosterman's complete-intersection-on-hypersurface setting is a genuine positive control: the flag-Hilbert geometry reaches a varying hypersurface locus and the relevant Hodge locus is smooth at the reference point. Nishinou gives another positive but differently typed control for divisor maps under semiregularity. Both are rejected as general transfers because their enabling hypotheses are exactly the kind of source-specific lifting structure missing in the arbitrary signed-rational-cycle problem.

Ciliberto–Flamini–Galati–Knutsen provides a primary regular-embedding deformation-theory interface; Nasu's 2026 examples provide a hostile reminder that Hilbert/flag deformation spaces can be obstructed or nonreduced. These sources support keeping relative smoothness as a checked producer rather than a default assumption.

## Diagnosis and new residual

C008 (open draft/shadow) had sharpened the local residual to "smoothness or direct dominance" after proposing an exact-class proper Hilbert source. C009 decomposes the smoothness horn into a reusable but deliberately strong producer:

`FACTORWISE_RELATIVE_HILBERT_SMOOTHNESS`
`=> COUPLED_RELATIVE_SMOOTHNESS`
`=> NONEMPTY_OPEN_IMAGE`
`+ PROPERNESS + IRREDUCIBLE_TARGET`
`=> FULL_BRANCH_IMAGE`.

The surviving local obstruction is:

`O-H4D1C-RELATIVE-HILBERT-SMOOTHNESS-OR-COUPLED-DOMINANCE`.

A future cycle should attack the smallest source-specific instance: either prove the actual relative Hilbert lifting obstruction vanishes for a defensible class of signed-`Q` representatives, or construct a genuinely coupled total-cycle incidence whose image is dominant without requiring factorwise smoothness.

## Local versus gluing obligations

**Local mathematical:** relative witness smoothness/integrability or direct dominance; exact signed-`Q` class binding; source-family completeness.

**Local-to-global/gluing:** monodromy beyond the local marking, singular degeneration/specialization, continuation across Hodge components, and any bridge from a conditional central algebraic witness to arbitrary root initial algebraicity.

None of the gluing obligations is discharged here.
