# BSD A1a1 R7 — generalized-Kato nonvanishing re-enters the localization residual

**Cycle:** `BSD-A1a1-KATO-LOCALIZATION-REENTRY-20260811-R7`  
**Active atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**Frozen fibre:** `sha256:788ae31fb787de32f0ab9b4a6e715c0a3092db5332e562dd1481ca29ed324375`  
**Authority:** source-bound theorem-cell diagnosis / proposal-shadow / same-context review only / no BSD root authority.

## Smallest discriminator

R6 showed that the audited even-sign `F=Q` mock-plectic theorem family has an intrinsic multiplicative-reduction entry condition, so it nominated good-ordinary generalized Kato classes as a representation rotation. R7 asks one narrower question: does that successor representation actually provide a route from exact complex analytic rank two to a nonzero arithmetic class without re-importing the previously isolated localization/positive-rank child `BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE`?

## Exact theorem cell

Castella, arXiv:2312.01481, Theorem 5.2.3 works under the paper's good-ordinary, residual, conductor/ramification and auxiliary `(K,chi)` hypotheses. If `L(E,s)` has positive even order at `s=1`, then

```text
kappa_p(E) != 0  ->  dim_Qp Sel(Q,V_pE) = 2.
```

Conversely, **assuming** the Selmer dimension is two,

```text
kappa_p(E) != 0  <->  loc_p : Sel(Q,V_pE) -> E(Q_p) tensor Q_p is nonzero.
```

The same theorem says that in this case `kappa_p(E)` spans the strict Selmer group `ker(loc_p)`. Remark 5.1.4 independently places the class in that strict kernel in the relevant vanishing/twist-nonvanishing setting. Thus the local nonzero witness cannot be `loc_p(kappa_p(E))`; it must be supplied by another, transverse ambient Selmer direction.

Combining the two theorem directions gives the scoped source-bound equivalence

```text
kappa_p(E) != 0
  <-> [dim_Qp Sel(Q,V_pE)=2  AND  loc_p != 0]
```

inside the exact source hypotheses. This is a theorem-cell composition, not a new BSD theorem.

## Diagnosis

The representation rotation changes the object but not the root-critical missing information. The route now reads

```text
ord_{s=1} L(E,s)=2
  -> ? [dim Sel = 2 plus a transverse nonzero p-local direction]
  -> kappa_p(E) != 0
  -> Selmer information
  -> ? Mordell-Weil/Sha/regulator/Tamagawa/torsion/complex-leading-term glue.
```

So generalized-Kato nonvanishing **re-enters `BSD-A1a2`** rather than bypassing it. This is a local compositional clarification plus a local-to-global route/gluing failure. It is not evidence that the generalized-Kato method is impossible; it identifies the exact missing interface in this theorem family.

## Counterexample-first controls

The cheapest invalid closure is to reverse `kappa!=0 -> dim Sel=2`; the source does not do this. The second invalid closure is to use `loc_p(kappa)!=0`; the source instead places `kappa` in `ker(loc_p)`. A third is to treat a p-adic height or leading-coefficient formula as an automatic nondegeneracy theorem. The current derived-height source arXiv:2308.10474 explicitly leaves the relevant order-of-vanishing step dependent on expected maximal non-degeneracy of the anticyclotomic p-adic height. Finally, current 2026 refined Kurihara/Kolyvagin special-element work is a different discrete/Selmer representation and is not silently substituted for the complex-rank-two generalized-Kato arrow.

## Root-coordinate ledger

The complex `s`-order remains the root coordinate. No Hida, cyclotomic, anticyclotomic, or p-adic order is substituted for it. The cycle proves no new statement about Tamagawa factors, torsion, Sha finiteness/order, the real regulator, archimedean period, extra/trivial zeros, or the full complex leading term. Even a one-prime Selmer theorem would leave those global obligations separate.

## Outcome and next discriminator

Outcome: `PARTIAL_SUCCESS / SOURCE_BOUND_ROUTE_REENTRY / NO_ROOT_CANDIDATE`.

The next useful search should not merely ask again whether generalized Kato classes are nonzero. It should ask for a current number-field theorem deriving the **transverse localization plus Selmer-dimension premise** from exact complex analytic rank two using assumptions genuinely weaker than algebraic rank two, Selmer rank two, p-adic BSD, equivalent main-conjecture strength, or p-adic regulator nondegeneracy. If bounded search continues to return only those arithmetic premises, rotate the carrier again rather than relabeling the residual.
