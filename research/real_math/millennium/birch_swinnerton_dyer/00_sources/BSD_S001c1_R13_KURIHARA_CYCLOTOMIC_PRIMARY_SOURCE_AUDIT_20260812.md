# BSD S001c1 R13 primary-source audit — Kurihara / cyclotomic / complex order coordinates

Authority: `PROPOSAL_SHADOW_ONLY`  
Root: `OPEN_NO_SOLUTION_CERTIFICATE`  
Cycle: `BSD-S001c1-KURIHARA-CYCLOTOMIC-ORDER-AUDIT-20260812-R13`  
Framework: RAKL method `3.0.0` at `44058e21e16b085b421638fadad5086e31472f0f`  
Application causal base: `58de5548d337d4ea3c83b5fcde6ed5c6aee3f2e0`

## Load-bearing primary source

Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, arXiv:2203.12159v6 (last revised 2025-05-14; final version, to appear in American Journal of Mathematics).

Selectors checked:
- Theorem 1.9 / the main structure theorem for Selmer groups and Kurihara numbers: under the stated semistable/surjectivity/Manin-constant hypotheses and finite Kurihara order, the discrete Kurihara order determines the `Z_p`-corank of the classical `p^infinity` Selmer group. With finiteness of `Sha[p^infinity]`, the rank and exact `p`-primary Sha structure can additionally be read off.
- Corollary 1.13 / parity application: the Selmer corank and the complex analytic vanishing order agree only modulo two at this level.
- Corollary 1.14 / computational upper bound: nonzero Kurihara data at a square-free product `n` gives an upper bound on Mordell-Weil rank in terms of `nu(n)`; this is a discrete witness, not a consequence of complex analytic order two.
- Section 1.9 comparison with classical and `p`-adic BSD: the higher-rank rank part of classical BSD is not established. Kato's one-sided Euler-system/Iwasawa result bounds Selmer corank by the order of the **cyclotomic p-adic L-function** at the trivial character. Equality invokes stronger input (full/main-conjecture-type equality together with nondegeneracy of the `p`-adic height and finiteness of `Sha[p^infinity]` in the comparison discussed there).

Visual verification:
- Primary PDF pages containing the parity/discrete upper-bound discussion and the classical-vs-p-adic BSD comparison were visually inspected in this run.
- Numerical examples are calibration only and grant no theorem authority.

## Exact coordinate cut

Three order coordinates must remain distinct unless an explicit theorem translates them:

1. complex coordinate: `r_C = ord_{s=1} L(E,s)`;
2. cyclotomic `p`-adic coordinate: `r_p = ord_{X=0} L_p(E,X)` (with the relevant normalization/reduction hypotheses exposed);
3. discrete coordinate: `r_K = ord(Kurihara)` for Kim's collection of Kurihara numbers.

The source supports, in its exact scope, a strong arithmetic identity of the form `r_K = corank_Zp Sel(Q,E[p^infinity])`, a parity relation with `r_C`, and a one-sided route from Selmer corank to `r_p`. It does **not** supply `r_C=2 => r_K=2` or `r_C=2 => r_p<=2` in arbitrary rank.

## Falsified shortcut

The shortcut

`ord_{s=1} L(E,s)=2  =>  corank_Zp Sel(Q,E[p^infinity]) <= 2`

cannot be justified by citing Kato's standard upper-bound statement alone: the load-bearing analytic quantity in that bound is the cyclotomic `p`-adic vanishing order, not the complex `s`-order. Any use of that shortcut must first provide an independent, source-valid complex-to-cyclotomic order comparison.

## Residual

`COMPLEX_TAYLOR_ORDER_TO_DISCRETE_KURIHARA_ORDER_EXACT_COMPARISON_OPEN`

with the explicit alternative subedge

`COMPLEX_S_ORDER_2_TO_CYCLOTOMIC_PADIC_X_ORDER_LE2_OPEN`.

Even closing either rank-two order edge would not close the refined BSD leading term: Mordell-Weil identification, Sha finiteness/order, regulator, Tamagawa factors, torsion, real period, and exact complex leading-term gluing remain separately gated.

No theorem, novelty, root promotion, or independent-review credit is claimed.
