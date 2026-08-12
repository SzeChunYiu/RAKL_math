# BSD A1a2 R15 same-context result review

**Authority:** source-bound retrospective hand lemma. **Independent mathematical review:** `0/3`. **Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.

## Statement reviewed

For the usual Kummer Selmer group of an elliptic curve `E/Q`,

```text
corank_Zp Sel(Q,E[p^infinity])
  = rank_Z E(Q) + corank_Zp Sha(E/Q)[p^infinity].
```

Thus, under exact Selmer corank two, Mordell-Weil rank two is equivalent to zero `p`-primary Sha corank, and in the cofinitely generated scope to finiteness of `Sha(E/Q)[p^infinity]`.

## Role-separated review

1. **Arithmetic-geometry lead:** accepts the Kummer exact sequence and Mordell-Weil tensor calculation; rejects any inference about the exact finite order of Sha.
2. **Selmer/Galois-cohomology lead:** accepts additivity of corank after Pontryagin duality for the usual Kummer local conditions; rejects transfer to strict or altered Selmer structures without a new proof.
3. **Analytic-BSD lead:** confirms that analytic order and Kurihara order remain upstream; this lemma does not prove their equality.
4. **Adversarial falsification lead:** verifies that finite torsion in `E(Q)` tensors to zero, positive Sha corank is the only additive slack, and no actual elliptic-curve infinite-Sha example is being claimed.
5. **Formal-methods lead:** finds the proof elementary and formalizable but notes that no proof-assistant receipt exists; authority remains hand proof.
6. **Novelty/research-value lead:** rejects novelty. Value is proof-DAG sharpening: an undifferentiated Mordell-Weil/Sha glue edge becomes one exact conditional criterion.
7. **Method-transfer/failure lead:** retains the mathematical lesson that exactness in an extension object does not imply exactness of a subobject until the quotient is controlled; warns this is scoped, not a global blacklist.

## Strongest objection

The phrase “Selmer corank two does not imply rank two” could be overread as an actual target counterexample. The proved statement is narrower: **the exact sequence alone does not license the implication**, because it contains the nonnegative `Sha[p^infinity]` corank term. No elliptic curve with positive divisible Sha is exhibited.

## Disposition

Accept the exact conditional lemma and DAG refinement. Reject strict context-first discovery credit, novelty, formal-proof credit, independent-review credit, Sha-finiteness, and every BSD-root or leading-term claim.

## Recursive pass 2 — boundary and cause audit

The second pass attacked four possible overclaims:

1. **Could finite Mordell-Weil torsion contribute to the tensor term?** No. For finite `T`, divisibility of `Q_p/Z_p` gives `T tensor Q_p/Z_p=0`; only the free rank contributes.
2. **Could corank zero still hide infinite `p`-primary Sha?** Not inside the stated cofinitely generated scope. Its Pontryagin dual is a finitely generated torsion `Z_p`-module and is therefore finite. The cofinite-generation qualifier remains explicit.
3. **Does a formal module countermodel prove an elliptic-curve counterexample?** No. It proves only logical non-sufficiency of the exact-sequence data. The result and lesson explicitly make no target existence claim.
4. **Does controlling `Sha[p^infinity]` finish refined BSD?** No. Even finiteness at this one prime leaves its exact order, other primary parts, the regulator, Tamagawa/local factors, torsion, real period and complex leading coefficient separately open.

No blocking concern survives within the scoped lemma. The strongest residual remains mathematical, not operational: derive `p`-primary Sha finiteness or an independent rank-two rational-point mechanism from admissible upstream hypotheses.
