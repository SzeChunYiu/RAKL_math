# BSD A1a1 R6 — intrinsic entry interface for the even-sign mock-plectic route

**Cycle:** `BSD-A1a1-PLECTIC-APPLICABILITY-20260811-R6`  
**Atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**Frozen fibre:** `sha256:5ba3279d73bed3a4dfbb4d7cd6f10a9f5e6680473890d9d93311fb194feb1dae`  
**Current RAKL semantic authority rechecked:** `bf94d16847971069912501e9a63f0e97a1e3e159`, method `3.0.0`.  
**Authority:** source-bound route applicability / proposal-shadow / same-context review only / no root authority.

## Question

R5 moved exact complex order two from `E/Q` to `E/K` conditionally on a nonzero complementary quadratic twist. Its next residual mixed two logically different kinds of hypotheses: coordinates intrinsic to the fixed elliptic curve `E`, and coordinates selectable by the auxiliary imaginary quadratic field `K`. R6 asks whether the currently audited `F=Q` even-sign plectic/mock-plectic path already requires an intrinsic local interface before any `K` optimization can matter.

## Primary-source discriminator

Fornea's current *Plectic Heegner classes* sets the functional-equation sign for an incoherent set `S` by `epsilon(A/E) = (-1)^(|S|+1)`. The same introduction says that for `F=Q`, an incoherent `S` contains at most one prime. Hence the sign `+1` branch relevant to exact even order two forces `|S|=1`, so `S={p}`. The `S=empty` specialization is instead the classical-Heegner-point branch and has the opposite sign in this typing.

For `F=Q, S={p}`, Fornea's comparison theorem recovers mock plectic invariants and defines the local sign according to whether `A/Q_p` has split or non-split **multiplicative** reduction. Fornea–Gehrmann's mock-plectic Iwasawa theorem states the same intrinsic condition directly: the elliptic curve has multiplicative reduction at the inert prime `p`.

Therefore:

```text
exact complex rank 2 over Q
  -> [R5 conditional base change] exact complex rank 2 over K
  -> [R6 entry test] audited even-sign F=Q mock-plectic branch
       requires an E-intrinsic multiplicative-reduction prime p
  -> auxiliary K can choose inert/split behaviour and complementary twists
       but cannot manufacture E's reduction type
  -> downstream plectic nonvanishing remains open.
```

This is not an impossibility theorem for plectic methods. It scopes one current theorem family.

## Counterexample-first checks

The cheapest repair, `S=empty`, fails the exact sign/role discriminator: under the source sign formula it is the sign `-1` branch, and the source identifies it with classical Heegner points. A good/additive `p` does not instantiate the audited mock-plectic comparison: the source's `S={p}` local sign is defined from split/non-split multiplicative reduction, while Fornea–Gehrmann explicitly assumes multiplicative reduction. Finally, selecting `K` may control inertness/splitting and twist nonvanishing, but it does not change the reduction type of the fixed `E/Q`.

## Successor representation

Castella's *Nonvanishing of generalised Kato classes and Iwasawa main conjectures* supplies a useful near-match with a different local interface: positive even analytic rank and a prime `p>3` of **good ordinary** reduction. But its proved direction is `kappa_p(E) != 0 -> dim Sel = 2`, with the converse tied to a localization condition; it does not close `analytic rank 2 -> kappa_p(E) != 0`. Thus this is a representation rotation, not root progress.

## Local versus gluing status

The R5 local base-change lemma remains intact. The new failure is a composition/gluing failure: a valid complex-coordinate transport does not glue to the audited plectic theorem family for the arbitrary-root contract unless the intrinsic entry interface is separately established. The global Mordell–Weil/Sha/regulator/Tamagawa/torsion/complex-leading-term obligations remain untouched.

## Next discriminator

Do not spend another round optimizing `K` for the arbitrary-`E` root path before an intrinsic-compatible arithmetic carrier has been selected. Search for a number-field, weight-two, exact-complex-rank-two bridge to a nonzero arithmetic class or regulator that does not assume the target rank/Selmer/BSD-strength conclusion. Good-ordinary generalised Kato classes are one controlled representation candidate; their nonvanishing arrow is the falsifier target, not an assumption.
