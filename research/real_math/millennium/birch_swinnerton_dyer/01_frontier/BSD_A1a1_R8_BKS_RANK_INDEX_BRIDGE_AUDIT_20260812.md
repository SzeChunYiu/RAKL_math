# BSD A1a1 R8 — BKS rank-index bridge audit

**Cycle:** `BSD-A1a1-BKS-RANK-INDEX-MISMATCH-20260812-R8`  
**Atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**Route signature:** `KATO_DARMON_DERIVATIVE_ALGEBRAIC_RANK_INDEX_MISMATCH`  
**Authority:** proposal/shadow only; no BSD root authority.

## Exact root-facing question

Assume only the root-side datum `ord_(s=1) L(E,s)=2` for an elliptic curve `E/Q`. Can the generalized Perrin–Riou / Darmon-derivative formalism of Burns–Kurihara–Sano (BKS) produce a rank-two arithmetic carrier without first assuming or proving `rank E(Q)=2`?

## Primary-source binding

Primary source: David Burns, Masato Kurihara, Takamichi Sano, *On derivatives of Kato's Euler system for elliptic curves*, arXiv:1910.07404v2 (17 Apr 2020), pp. 3–4, Introduction §1.2.1–1.2.2.

Exact scope read from the source:
- BKS write `r` for **the rank of `E(Q)`**, assume `r>0`, no `p`-torsion in `E(Q)`, and finiteness of the `p`-primary Tate–Shafarevich group.
- Their Bockstein regulator has source `wedge^r H^1` and target augmentation quotient `I^(r-1)/I^r`.
- Generalized Perrin–Riou Conjecture 1.1(i) predicts the Kato norm lies in augmentation degree `I^(r-1)`; Theorem 1.3 proves this containment under `p>3`, p-primary Sha finiteness over `F` and `Q`, a large-image condition, and absence of local `p`-torsion at primes in `S`.
- Conjecture 1.1(iii), the leading-term formula, is not proved in arbitrary rank in the audited theorem cell.
- BKS state that the integrality assertion 1.1(ii) follows when the `p`-part of BSD is valid.
- When **analytic rank is one**, Gross–Zagier/Kolyvagin imply `r=1`; BKS explicitly use that external rank identification before simplifying the conjecture.

Source provenance:
- arXiv identifier/version: `1910.07404v2`; PDF inspected visually on pages 3–4 and text-bound to the same pages.
- Current bounded frontier controls: Burungale–Skinner–Tian–Wan, arXiv:2409.01350 (zeta-element applications include BSD in analytic rank 0/1); Castella–Sano, arXiv:2601.14504 (refined Kurihara/Kolyvagin nonvanishing in a distinct p-adic/discrete carrier).
- Completeness claim: **none**. This was a bounded current primary-source audit, not a proof of literature completeness.

## Counterexample-first falsification

Cheap proposed inference:
`ord_(s=1)L(E,s)=2  =>  set r=2 in BKS  =>  rank-two Kato/Darmon derivative`.

**Rejected.** The first BKS occurrence fixing `r` binds it to the unresolved target `rank E(Q)`. The augmentation order `r-1`, exterior degree `r`, and Bockstein regulator are therefore target-indexed. Rebinding `r` to analytic rank would change the theorem's semantics.

The proved arbitrary-rank containment is valuable **conditional on the algebraic rank parameter and source hypotheses**, but it does not establish the equality between complex analytic order and that parameter. In analytic rank one the index mismatch is removed by Gross–Zagier/Kolyvagin; that is a transfer disanalogy, not evidence that rank two follows.

## Local theorem versus gluing

Local mathematical failure: **false**. BKS's theorem cell is internally useful and source-bound.

Root-facing gluing failure: **true**. The route needs an independent bridge
`ord_(s=1)L(E,s)=2 -> rank E(Q)=2`
(or a strictly weaker theorem that determines the correct arithmetic filtration degree) before the BKS rank-two derivative object can even be instantiated root-faithfully. Using BSD, Selmer-rank-two, regulator nondegeneracy, or `BSD_p(E)` for that purpose would import target-strength arithmetic information.

Even after a valid BKS derivative is available, full BSD still separately requires Sha, Tamagawa/local factors, torsion, real period, regulator, and exact complex leading-term control.

## Hypothesis / coordinate ledger

- Tamagawa/local factors: untouched global glue.
- torsion: BKS includes a no-`p`-torsion condition in the theorem cell; global torsion factor remains unresolved.
- regulator: Bockstein regulator present; no complex regulator nondegeneracy inferred.
- Sha: p-primary finiteness appears in BKS scope; full Sha finiteness/order remains unresolved.
- extra/trivial zeros: not used to close this cycle.
- complex vs p-adic/discrete faithfulness: preserved; no augmentation degree, p-adic derivative, Selmer rank, or Kurihara/Kolyvagin discrete coordinate was substituted for complex `s`-order.
- low-rank transfer: analytic-rank-one success explicitly quarantined from rank two/arbitrary rank.

## Outcome

`PARTIAL_SUCCESS_ROUTE_PRUNED_NO_ROOT_CANDIDATE`.

The BKS representation does not furnish an analytic-rank-two bootstrap: its higher derivative order is parametrized by algebraic Mordell–Weil rank. The smallest residual is now:

`COMPLEX_ANALYTIC_RANK2_TO_ROOT_FAITHFUL_ARITHMETIC_INDEX_WITHOUT_TARGET_RANK_ASSUMPTION`.

This does **not** prove impossibility of all Kato-derivative approaches. It prunes this direct substitution/composition and tells the next cycle to search only for a source-bound theorem that determines the arithmetic index from weaker complex analytic data, or to rotate representation again.