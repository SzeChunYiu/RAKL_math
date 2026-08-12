# H4d1c-f C006 — ramification audit of pointwise differential proxy

**Cycle:** `H4d1c-C006-RAMIFICATION-PROXY-AUDIT`  
**Authority:** `VERIFIED_SCOPED_PROXY_NOGO / PROPOSAL_SHADOW / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`

## Exact consumer and question

The local H4d1c consumer is the actual image of a same-class algebraic-witness incidence in one locally marked Hodge-locus branch. C004 already showed that enlarging the witness tangent space need not enlarge the target image, because new source directions may be vertical. C006 asks a different boundary question: if the actual image germ does cover the target germ, must the differential at the selected central witness be surjective?

## Exact counterexample

Work over `Q` (and therefore after base change over `C`). Let

`pi : A^1_t -> A^1_u`,  `u = t^2`,

and select `t=0`, mapping to `u=0`.

The affine ring map is

`Q[u] -> Q[t]`,  `u |-> t^2`.

It is injective. Hence the affine scheme-theoretic image is `Spec(Q[u])` itself: the kernel defining the image is zero. Thus the actual scheme-theoretic image, and a fortiori the reduced image germ at `u=0`, is the whole target.

At the selected point the induced cotangent map is

`(u)/(u^2) -> (t)/(t^2)`,  `u mod u^2 |-> t^2 mod t^2 = 0`.

Therefore the dual tangent map `d pi_0` is the zero map. It is not surjective.

So **full target image does not imply selected-point differential surjectivity**. Ramification can make the first-order map under-report the nonlinear image.

## What this changes

The route

`reduced image-germ coverage => d pi_w surjective at the chosen central witness`

is pruned. Pointwise differential surjectivity may still be a useful *sufficient* certificate under separately stated smooth/submersion hypotheses, and generic rank may still control image dimension on suitable loci. It is not a necessary condition at an arbitrary selected witness.

The consumer-aligned successor is therefore to prove actual image geometry directly—e.g. exact-class binding plus closed/proper image and target-component/top-dimensionality—or to prove a source-specific generic/nonramified condition at a suitably chosen witness. This sharpens, but does not prove, the open C005 source-image program.

## Hodge and gluing boundaries

This abstract morphism is **not** an actual Hodge-incidence construction. It does not show that an arbitrary rational Hodge class has an algebraic witness, does not construct a coupled signed-`Q` family, and does not close higher-Artin lifting, algebraization/effectivity, completion-to-branch descent, monodromy, degeneration/specialization, or global continuation.

The failure is local mathematical/representation/proxy failure. No local-to-global gluing step failed in this episode; those obligations remain independently open.

## Verification controls

The ring-kernel computation is the proof of full affine scheme-theoretic image; the cotangent computation is the proof of zero differential. Stacks Project §29.6 / tag `01R5` is the primary external control for the affine scheme-theoretic image formula, and tag `056B` controls the reduced-source/reduced-closure relation.

Same-context expert-cell review: six roles; independent mathematical-review credit `0/3`.
