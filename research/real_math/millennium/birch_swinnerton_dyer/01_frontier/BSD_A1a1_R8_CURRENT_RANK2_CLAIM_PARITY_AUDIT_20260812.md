# BSD A1a1 R8 — current analytic-rank-two claim parity audit

**Cycle:** `BSD-A1a1-CURRENT-RANK2-CLAIM-PARITY-AUDIT-20260812-R8`  
**Atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**Authority:** proposal/shadow route audit only; no BSD proof, disproof, root certificate, or independent-review credit.

## Exact discriminator

A March 2026 author-uploaded preprint by Wang Xiong claims analytic-rank-two BSD using “definite anticyclotomic Iwasawa theory.” Before inspecting its downstream Euler-system and leading-term chain, R8 tested the first structural premise: whether its Heegner splitting hypothesis is compatible with its stated root sign and definite quaternionic vertex.

The preprint's Definition 6.1 requires every prime `ell | N` to split in the imaginary quadratic field `K`, while Proposition 6.3 and the subsequent definite/indefinite table assert this yields root sign `+1` and the definite case.

## Primary-source falsification

Howard's *Bipartite Euler Systems* gives, in this exact elliptic-curve/imaginary-quadratic setting,

`sign L(E/K,s) = - epsilon(N)`,

where `epsilon` is the quadratic character of `K`. If every prime dividing `N` splits, each local character value is `+1`, hence `epsilon(N)=+1` and the sign is `-1`. Howard identifies this as the **indefinite** vertex; `epsilon(N)=-1` is the **definite** vertex.

The quaternionic parity says the same thing. Under the all-split Heegner hypothesis, `N^- = 1`: there are zero finite inert conductor primes, so the quaternion algebra relevant to the base form is indefinite at infinity. Adding one inert level-raising prime toggles to the opposite, definite vertex; it does not make the original all-split form definite.

Nguyen's current anticyclotomic congruence theorem is explicitly in the indefinite setting and has the corresponding rank-one Iwasawa/Selmer object. Castella–Grossi–Lee–Skinner likewise formulate the all-split Heegner setting with rank-one anticyclotomic Selmer structure. These primary sources therefore agree with Howard's typing and disagree with the audited preprint's base sign/vertex assignment.

## Result

The audited proof route is **refuted as written at its foundational sign partition**:

```text
all ell|N split in K
=> epsilon(N)=+1
=> sign(E/K)=-1
=> indefinite vertex,
```

not sign `+1`/definite as claimed.

This is a source-local mathematical contradiction in the proposed proof composition. It is enough to stop the downstream audit under the counterexample-first policy. It does **not** refute BSD, establish that no corrected proof exists, or support a literature-wide nonexistence claim.

## Local versus global status

Local result: the sign/quaternion classification in the current proof claim fails the primary-source consistency check.  
Local-to-global result: downstream definite-Iwasawa, congruence, Selmer, and leading-term arrows cannot be glued to this incoherent base vertex without a corrected theorem-level reconstruction.  
Global BSD residual: unchanged — exact complex analytic rank two still lacks a verified general route to Mordell–Weil rank two and the full leading term, and arbitrary-rank BSD remains open.

## Hypothesis ledger

`Tamagawa`, `torsion`, `regulator`, `Sha`, real period, and full complex leading-term factors were not reached and remain open global-gluing coordinates. Extra/trivial zeros were not used. Complex-versus-p-adic coordinate faithfulness was preserved: no p-adic order or Iwasawa characteristic was substituted for the complex `s`-order. The failure precedes those coordinates.

## Sources

- Wang Xiong, DOI `10.13140/RG.2.2.14539.86569`, Definition 6.1 / Proposition 6.3 / Section 6.4; author-uploaded preprint, not treated as authoritative.
- Benjamin Howard, arXiv:`1202.6353`, sign and definite/indefinite partition.
- Chan-Ho Kim/Nguyen-context current anticyclotomic congruence source audited as arXiv:`2510.12890`, indefinite rank-one theorem cell.
- Castella–Grossi–Lee–Skinner, arXiv:`2008.02571`, all-split Heegner hypothesis and rank-one anticyclotomic Selmer typing.

Root remains `OPEN_NO_SOLUTION_CERTIFICATE`.
