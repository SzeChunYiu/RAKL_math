# H4d1c-b fixed-component fibre-product coupling audit

**Date:** 2026-08-12  
**Atom:** `H4d1c-b`  
**Parent residual:** `H4d1c-INDEPENDENT-HODGE-TO-WITNESS-TANGENT-SURJECTIVITY-MECHANISM`  
**Authority:** `SCOPED_FIRST_ORDER_REPRESENTATION_ROUTE_PRUNING / PROPOSAL_SHADOW / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`

## Exact question

Fix the rational smooth-projective H4d1c context and an already algebraic denominator-cleared signed witness whose selected component identities are held fixed. For local witness charts

`pi_i: W_i -> T`

over the same fixed local Hodge-locus branch `T`, a natural attempt to repair componentwise cancellation is to package the selected components simultaneously:

`W^x := W_1 x_T ... x_T W_m`.

Can this coefficient-preserving fibre-product coupling have a larger first-order image in `T` than the separate component witness problems?

## Scoped non-expansion lemma

Let `w=(w_i)` be the selected point of `W^x` over `s0`, and let `pi^x:W^x->T` be the common projection. Work with ordinary tangent spaces of the frozen local scheme/algebraic-space charts at complex points.

Then

`im(d pi^x_w) = intersection_i im(d pi_i|_{w_i})`.

### Proof

Use the dual-number definition of tangent vectors. A tangent vector of `W^x` at `w` is a map from `D=Spec(C[epsilon]/epsilon^2)` to the fibre product reducing to `w`. Composing with every projection gives tangent vectors `tau_i` of `W_i` at `w_i`. Because the square defining the fibre product commutes, all `pi_i o tau_i` are the same tangent vector `v` of `T`. Hence every vector in `im(d pi^x_w)` belongs to every `im(d pi_i|w_i)`.

Conversely, let `v` belong to every component image. Choose a tangent lift `tau_i` in each `W_i` with `d pi_i(tau_i)=v`. The corresponding dual-number maps all have the same composite `D->T`. The universal property of the fibre product therefore gives a unique map `D->W^x` inducing the tuple `(tau_i)`, and its image under `d pi^x` is `v`. This proves the reverse inclusion.

No smoothness or dimension count is used. The proof is only a first-order functor-of-points statement in the frozen representable local category.

## Consequence for H4d1c

A fixed-component fibre product is **bookkeeping coupling**, not a new source of base tangent directions. Postcomposing the tuple with addition, signs, or rational coefficient bookkeeping while leaving the base projection unchanged cannot enlarge its base tangent image.

Combined only as search guidance with the proposal/shadow H4d1c-a cancellation episode, this prunes the following repair: “total-class Hodge tangency is larger than componentwise tangency, so synchronize the fixed selected component witness spaces and hope the coupled tuple reaches the extra directions.” The synchronized tuple reaches exactly the intersection of the component witness images.

The route is **not** globally impossible. A genuinely different witness representation can escape the lemma if it does not factor as fixed selected component charts over `T`: examples of structural escape hatches include a single Picard-type object, a source-specific flag/incidence construction, an algebraic correspondence producing a total witness, or a moduli mechanism allowing the decomposition itself to change. Each requires a fresh frozen category and source-bound tangent audit.

## Primary-source controls

- Stacks Project, Tag `0B28`, *Tangent spaces*: current definition via dual-number points and induced tangent maps.
- Stacks Project, Tag `001U`, *Fibre products*: universal property used in the reverse inclusion.
- Cattani–Deligne–Kaplan, `arXiv:alg-geom/9402009`: base-side locus where a fixed class remains Hodge; not a witness-lifting theorem.
- Nishinou, `arXiv:2009.01651`: positive semiregular relative-deformation control in its divisor-map category; rejected as a general H4d1c transfer.
- Kloosterman, `arXiv:2104.14845`: positive special-family control where explicit flag-Hilbert geometry supplies a genuine witness/Hodge-locus comparison rather than mere tuple synchronization.

The non-expansion lemma itself is the elementary dual-number/fibre-product argument above; the Hodge sources control transfer scope.

## Adversarial boundary audit

The statement does not cover stacky tangent automorphism data without a separate 2-fibre-product analysis; it does not model rational equivalence as a fine moduli problem; it fixes selected components and therefore does not cover splitting, collision, replacement, or changing decomposition; and it is first-order only. None of higher Artin compatibility, formal algebraization, rational coefficient/category preservation beyond the frozen tuple, monodromy, singular degeneration, global continuation, or initial algebraicity is advanced.

## Same-context expert cell

The algebraic-cycle/witness-moduli specialist proved the fibre-product tangent interface; the VHS specialist checked that total-class Hodge tangency must not be silently replaced by component persistence; the correspondence/Lefschetz specialist separated genuine new representations from bookkeeping coupling; the deformation specialist kept H4d1b tangent reachability binding; the adversarial verifier tested both inclusions and scope boundaries; and the RAKL auditor enforced proposal/shadow authority and telemetry. These are same-context passes and count as **zero independent mathematical reviews**.

## Local versus gluing diagnosis

This is a **local first-order representation-transfer failure before gluing**. No local-to-global theorem was attempted, so no gluing failure is recorded. Higher-order/formal/algebraic/global interfaces remain independent residuals.

## Outcome

`PARTIAL_SUCCESS / FIXED_COMPONENT_COUPLING_ROUTE_PRUNING`.

The next high-information child should test a **genuinely total witness representation** whose base projection does not factor through the fixed-component fibre product. A candidate must state exactly what new moduli object or correspondence creates additional tangent directions and why its coefficient/category semantics match the rational Hodge branch.

Root rational Hodge Conjecture status remains `OPEN_NO_SOLUTION_CERTIFICATE`.
