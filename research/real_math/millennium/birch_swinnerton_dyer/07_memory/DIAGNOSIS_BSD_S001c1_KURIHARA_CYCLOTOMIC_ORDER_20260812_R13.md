# DG-BSD-S001C1-R13-THREE-ORDER-COORDINATE-CUT

Authority: `PROPOSAL_SHADOW_DIAGNOSIS_ONLY`  
Cycle: `BSD-S001c1-KURIHARA-CYCLOTOMIC-ORDER-AUDIT-20260812-R13`  
Episode: `EP-BSD-S001C1-R13-KURIHARA-CYCLOTOMIC-ORDER-AUDIT-20260812`  
Existing obstruction retained: `BSD-S001c1-KURIHARA-TAYLOR-COMPARISON`  
Root: `OPEN_NO_SOLUTION_CERTIFICATE`

## Diagnosis

The active residual is not merely “find a better Euler system.” It is a coordinate-faithful comparison problem among three non-identical notions of order:

- `r_C = ord_{s=1} L(E,s)`, complex Taylor order;
- `r_p = ord_{X=0} L_p(E,X)`, cyclotomic `p`-adic order at the trivial character;
- `r_K = ord(Kurihara)`, the discrete modular-symbol/Kolyvagin-system order used in Kim's structural theorem.

The current primary theorem cell gives a strong exact arithmetic relation `r_K = corank Sel_p` in its scope, and the standard one-sided Kato route bounds Selmer through `r_p`. The direct complex relation available in the same source family is parity rather than exact arbitrary-rank equality. Consequently, complex analytic rank two does not supply a source-valid Selmer upper bound of two unless one first proves an independent translation such as `r_C=2 => r_p<=2` or directly `r_C=2 => r_K=2`.

## Local versus gluing failure

Local mathematical failure: **none identified** in the scoped Kim theorem cell.

Gluing failure 1: `r_C -> r_p` is unlicensed at exact order two.  
Gluing failure 2: `r_C -> r_K` is unlicensed at exact order two.  
Gluing failure 3: even exact rank/Selmer information does not automatically glue Sha, regulator, Tamagawa, torsion, period and the exact complex leading term.

## What this diagnosis is not

It is not a proof that no such comparison theorem exists.  
It is not a new obstruction family: it sharpens the already active `BSD-S001c1-KURIHARA-TAYLOR-COMPARISON`.  
It is not a literature-novelty claim.  
It does not promote a lesson, tool, motif, or root theorem.

## Next discriminator

A candidate source must expose all hypotheses and prove one of:
1. an exact complex-to-discrete order comparison strong enough to force `r_K=2` from `r_C=2`; or
2. an exact complex-to-cyclotomic order upper comparison strong enough to combine with the one-sided Selmer bound without assuming p-adic BSD, height nondegeneracy, Sha finiteness, analytic-rank equality, or equivalent root-strength input.

Otherwise this fibre remains open and should not be replaced by another representation that merely renames the missing comparison edge.
