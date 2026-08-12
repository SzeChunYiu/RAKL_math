# BSD S001c1 R13 seven-role same-context expert cell

Cycle: `BSD-S001c1-KURIHARA-CYCLOTOMIC-ORDER-AUDIT-20260812-R13`  
Authority: `SAME_CONTEXT_REVIEW_ONLY`; independent mathematical-review credit: `0/3`.

## 1. Complex-L / Gross–Zagier role
Kim's discrete structural theorem is not an arbitrary-rank proof of the classical analytic-rank equality. The source's direct complex comparison in the relevant application layer is parity, while the rank-zero/low-rank consequences remain special cases. Exact complex analytic rank two therefore cannot be promoted to exact discrete order two from this source.

## 2. Cyclotomic Iwasawa / p-adic L-function role
The one-sided Kato inequality compares Selmer size/corank with the cyclotomic `p`-adic L-function order. The variable is the cyclotomic Iwasawa coordinate, not the complex `s` variable. Turning analytic rank two into an upper bound of two requires a separate complex-to-`p`-adic order theorem. Equality/leading-term statements in the p-adic BSD direction require stronger assumptions and are not an admissible root bridge when those assumptions contain the desired arithmetic conclusion in equivalent strength.

## 3. Selmer / Euler-system role
Kim's Kurihara-order theorem is a strong exact discrete-to-Selmer statement under its own hypotheses. R12 already removed the `p^infinity` versus `V_p` coefficient mismatch for the usual Selmer structures. However, composing R12/R9 with the Kurihara theorem to obtain a rank-two lower bound is permitted only after exact common-curve, common-prime and local/hypothesis compatibility is checked; this cycle does not silently perform that composition.

## 4. BSD leading-term / local-factor role
Even exact Selmer corank two would not prove the full BSD formula. Finiteness and exact order of Sha, regulator nondegeneracy/value, Tamagawa factors, torsion, period normalization and the complex leading coefficient remain distinct. Kim's rank extraction from the discrete Selmer structure uses additional Sha-finiteness input where stated.

## 5. Representation and DifferenceWitness skeptic
`r_C=ord_s L`, `r_p=ord_X L_p`, and `r_K=ord(Kurihara)` are different coordinates. Shared language such as “order of vanishing” is not an identity witness. Interpolation of values at characters does not by itself transport a second complex derivative or exact order. The DifferenceWitness is the deformation direction and coefficient/measurement object: complex spectral parameter versus cyclotomic character versus a discrete modular-symbol/Kolyvagin-system index.

## 6. Source/provenance and falsification role
Only primary-source claims were granted technical authority. The decisive hostile test was to inspect what analytic variable appears in the alleged upper-bound route. It is cyclotomic `p`-adic, so a direct complex-rank-two upper-bound shortcut fails source binding. Two load-bearing PDF pages were visually inspected; numerical material was not used as proof.

## 7. RAKL v3 / formal-gate role
Current RAKL_math memory changed the bounded route: a prospectively stated localization-first preference was displaced by the current DAG's active `BSD-S001c1-KURIHARA-TAYLOR-COMPARISON`. This is observed memory-conditioned routing, not valid causal uplift, because the pre-memory prior was frozen before the current application fibre was fully rebound and therefore has a different fibre identity. Same-context review is not independent review. No authority-promotion surface is invoked.

## Cell consensus
Outcome: `SOURCE_BOUND_THREE_ORDER_COORDINATE_CUT__ROOT_OPEN`.

Local mathematical result status: the discrete-to-Selmer theorem cell is valid in its source scope.  
Local-to-global/gluing status: failed at the complex `s` -> cyclotomic `X` / discrete Kurihara order interface, and again at the full BSD leading-term interface.  
Root: `OPEN_NO_SOLUTION_CERTIFICATE`.

Next discriminator: find an exact primary theorem that, under hypotheses strictly weaker than or independent of the desired BSD rank-two conclusion, supplies either `r_C=2 => r_K=2` or enough complex-to-cyclotomic control to force `r_p<=2`; otherwise keep the current obstruction open and rotate only after this source family is saturated.
