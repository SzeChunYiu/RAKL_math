# BSD A1a1 R8 — prospective same-context expert cell

**Cycle:** `BSD-A1a1-BKS-RANK-INDEX-MISMATCH-20260812-R8`  
**Independent mathematical-review credit:** `0`.

The cell was frozen before accepting any bridge conclusion. All roles shared the same context and therefore count only as same-context adversarial review.

| Role | Background / delegated check | Finding |
|---|---|---|
| Analytic BSD lead | complex L-functions, analytic rank, exact root contract | `ord_(s=1)L(E,s)=2` is the only root-side rank datum permitted in this atom; algebraic rank cannot be silently substituted. |
| Euler-system/Iwasawa lead | Kato systems, augmentation filtrations, Perrin–Riou | In BKS, `r` is declared as `rank E(Q)` and controls `I^(r-1)/I^r` and `wedge^r`; theorem use must preserve that binding. |
| Gross–Zagier/Kolyvagin analogue lead | Heegner points, rank-one BSD mechanisms | The analytic-rank-one specialization is a near-solved analogue because external theorems supply `r=1`; that mechanism is absent from the audited rank-two cell. |
| Structural-transfer lead | analogy/transfer and DifferenceWitness audit | Common abstraction: target-indexed carriers cannot bootstrap the index. DifferenceWitness separates this from R7's localization carrier. |
| Adversarial falsifier | circularity, hidden-premise and theorem-direction checks | Falsified the shortcut `analytic rank 2 => use BKS r=2`; also rejected treating arbitrary-rank containment as analytic/algebraic rank equality. |
| Formal/source verifier | statement binding, quantifiers, hypotheses, provenance | Bound BKS pp.3–4 and Theorem 1.3 hypotheses; marked Conjecture 1.1(iii) as conjectural at arbitrary rank and integrality dependence on `BSD_p(E)`. |
| Local-to-global gluing lead | Selmer/MW/Sha/regulator/local factors | Local BKS theorem validity does not glue to full BSD; p-primary Sha, local torsion, regulator, Tamagawa, torsion, real period and complex leading coefficient stay separate. |

## Delegated discussion / resolution

The analytic lead proposed the most tempting composition: take analytic order two as the derivative order. The Euler-system and source-verifier roles vetoed it because the source defines the derivative order through algebraic `r`. The analogue lead showed exactly why rank one is not a counterexample to that veto: Gross–Zagier/Kolyvagin first establish the matching algebraic rank. The transfer lead then applied `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` only at the operator level, with a DifferenceWitness: R7 tested complex rank versus p-localization, whereas R8 tests complex rank versus an algebraic-rank-indexed filtration. The gluing lead confirmed that even a correctly instantiated derivative would not settle the refined leading term.

Consensus: no candidate generation; retain the source-bound representation mismatch and prune the direct BKS-rank-two shortcut. Root remains `OPEN_NO_SOLUTION_CERTIFICATE`.
