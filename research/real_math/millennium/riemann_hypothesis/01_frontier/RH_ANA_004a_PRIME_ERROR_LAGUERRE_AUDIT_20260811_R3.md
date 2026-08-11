# RH-ANA-004a — prime-error/Laguerre representation and root-strength audit (R3)

**Authority:** proposal/shadow route diagnostic; source-bound identities plus elementary derivation; same-context expert cell only; no RH theorem; no Li-sign theorem; no independent review; root authority none.

## Current-work reconciliation before routing

Current RAKL `main` was read first at method `3.0.0`, Git SHA `bb30835f41dd5e02a427c3e53be6914732d66fd2`. The newly available v3 `CurrentWorkCoverageReceipt` was used before this route was frozen. It recovered the pre-existing same-atom RH PR #118 that the earlier #147 fibre had omitted, and also selected the process diagnosis in #160. Therefore this cycle does **not** continue `RH-ANA-003b` as an independent child. It reconciles it under PR #118's `RH-ANA-004` as `RH-ANA-004a`.

The frozen fibre hash is `sha256:0a01b3e5c91c98896ec9ec5c336be9f097d15cdcf1ff7a0e72512dc7ecba1dab`; the current-work receipt canonical hash is `sha256:e9dc04a7dde68d87ad63e7cff9ca543ba4e37c95f0a96a901563aac6d35eec8a`; the memory-review hash is `sha256:84002154b00cd2f11cd7354328be1357a580921eea6cecb5870c1e4666ee35ca`; the pre-result trace ends at `RH-ANA-004a-E07`, `sha256:36be273c81128ce0b3b8f00e13f3d4c30dd30692e86fb166c0141637bc457d8b`.

## Exact source object

Primary source: Mark W. Coffey, *The Stieltjes constants, their relation to the eta_j coefficients, and representation of the Hurwitz zeta function*, arXiv:`0706.0343v2` (18 February 2009). Proposition 2 writes the crucial Li subsum as

`S_2(n) = S_gamma(n) + S_Lambda(n)`

with

`S_Lambda(n) = sum_{m>=1} [1-Lambda(m)]/m * L_{n-1}^{(1)}(log m)`.

The same source proves `S_gamma(n)=O(n)`. Its discussion then makes the strength boundary explicit: linear/sublinear growth of `S_Lambda` is RH-equivalent in this decomposition, and a polynomial bound on the oscillatory remainder `S_{2Lambda}` is a sufficient condition for RH. Thus a request to "prove an unconditional polynomial global bound for S_Lambda/S_{2Lambda}" is not a modest child lemma; it is already root-scale.

Coffey, arXiv:`math-ph/0505052v1`, Theorem 1 is retained as the exact Li/eta provenance tying `S_2` back to the Li coefficients. No finite Li prefix or numerical evaluation receives theorem authority.

## Exact discriminator 1 — Abel transform to the prime-number-theorem error

Let

`a_m = 1 - Lambda(m)`,

`A(x) = sum_{m<=x} a_m = floor(x) - psi(x)`,

and

`f_n(x) = x^{-1} L_{n-1}^{(1)}(log x)`.

For finite `X`, Abel summation gives the exact identity

`sum_{m<=X} a_m f_n(m) = A(X) f_n(X) - integral_1^X A(x) f_n'(x) dx`.

Using

`d/du L_{n-1}^{(1)}(u) = -L_{n-2}^{(2)}(u)`

and

`L_{n-1}^{(1)}(u) + L_{n-2}^{(2)}(u) = L_{n-1}^{(2)}(u)`,

we obtain

`f_n'(x) = -x^{-2} L_{n-1}^{(2)}(log x)`.

Hence

`sum_{m<=X} [1-Lambda(m)]/m L_{n-1}^{(1)}(log m)`

`= [floor(X)-psi(X)] X^{-1} L_{n-1}^{(1)}(log X)`

`  + integral_1^X [floor(x)-psi(x)] x^{-2} L_{n-1}^{(2)}(log x) dx`.

For each fixed `n`, the boundary term tends to zero under a standard quantitative PNT error. A primary explicit calibration is Johnston--Yang, arXiv:`2204.01980`, which gives an unconditional bound of the form `|psi(x)-x| <= C x (log x)^a exp(-c sqrt(log x))`; multiplication by the fixed-degree logarithmic polynomial and `x^{-1}` forces the boundary to zero. Therefore the source series admits the exact fixed-`n` representation

`S_Lambda(n) = integral_1^infinity [floor(x)-psi(x)] x^{-2} L_{n-1}^{(2)}(log x) dx`

or, with `x=e^u`,

`S_Lambda(n) = integral_0^infinity [floor(e^u)-psi(e^u)] e^{-u} L_{n-1}^{(2)}(u) du`.

This representation preserves the signed prime error; it does not apply a termwise absolute majorant.

## Exact discriminator 2 — Laguerre Laplace transform and the critical-line phase boundary

For `Re(s)>0`, define

`I_n(s) = integral_0^infinity e^{-s u} L_{n-1}^{(2)}(u) du`.

From the generating function

`sum_{k>=0} L_k^{(2)}(u) t^k = (1-t)^{-3} exp[-u t/(1-t)]`,

termwise integration for `|t|<1` yields

`sum_{k>=0} I_{k+1}(s) t^k = (1/s)(1-t)^{-2}(1-(1-1/s)t)^{-1}`.

Coefficient extraction gives the exact finite formula

`I_n(s) = n+1-s + s(1-1/s)^{n+1}`.

Now use a **single zero-mode only as a truncated-explicit-formula calibration**. In the Riemann--von Mangoldt explicit formula, a zero `rho` contributes `x^rho/rho` to `x-psi(x)`. In the `u`-variable its contribution to `[x-psi(x)]/x` is `(1/rho)e^{-(1-rho)u}`. Applying the exact transform gives

`(1/rho) I_n(1-rho) = n/rho + 1 - (1-1/rho)^{-n}`.

The exponential factor has base

`|(1-1/rho)^{-1}| = |rho|/|rho-1|`.

Consequently

`|(1-1/rho)^{-1}| > 1  iff  Re(rho)>1/2`,

`=1  iff  Re(rho)=1/2`,

and `<1` on the reflected side. This is an exact structural discriminator for a single mode. It does **not** justify an unregulated exchange of the infinite zero sum with the Laguerre integral and does not assert that any off-line zeta zero exists.

The algebraic identities were checked independently by the special-functions and adversarial-audit roles and calibrated for `n=1,...,5` in SymPy. The finite checks are not proof; the proof is the Laguerre generating-function calculation above.

## Current explicit-formula source and the next non-root-equivalent coordinate

Current primary source: Daniel R. Johnston and Michaela Cully-Hugill, arXiv:`2402.04272`, current version dated 22 March 2026. Their Theorem 1.2 gives, for an admissible `T* in [T,2T]` and stated `x,T` ranges,

`psi(x) = x - sum_{|gamma|<=T*} x^rho/rho + O*( M x (log x)^{1-omega}/T )`.

Transporting this **finite-height error term** through the prime-error/Laguerre representation produces the explicit error functional

`(M/T) integral_0^{log X} u^{1-omega} L_{n-1}^{(2)}(u) du`

before any absolute-value majorization, plus the finite-`X` Abel boundary and the `floor(x)-x` term. A safe theorem must preserve its sign/cancellation structure or else prove a uniform magnitude estimate with the correct `n,X,T` dependence.

Dunster--Gil--Segura, arXiv:`1705.01190`, provides uniform large-degree Laguerre asymptotics across unbounded real/complex `x`; this is a useful special-function analogue. It does not by itself control the arithmetically weighted prime-error integral or license summing a fixed-`x` Fejer asymptotic over all prime powers.

This localizes the next atom:

`RH-ANA-004b — TRUNCATED_LAGUERRE_EXPLICIT_FORMULA_TRANSPORT`.

Its success contract is deliberately finite/truncated: derive an exact `X,T,n` decomposition of the prime-error/Laguerre integral using a current truncated explicit formula; audit every boundary, floor term, zero-mode sum and error functional; then test whether any bound survives for a non-root-equivalent window. No global polynomial `S_Lambda` theorem is assumed or requested.

## Expert-cell synthesis

The **analytic-number-theory lead** verified the exact Abel-summation object `A(x)=floor(x)-psi(x)` and required the floor term and boundary contribution to remain explicit. The **Li/positivity specialist** used Coffey's own discussion to reject global polynomial `S_Lambda/S_{2Lambda}` growth as a weak child contract because it is already RH-sufficient/root-scale. The **special-functions lead** verified the derivative identity and Laplace transform and rejected fixed-`x` Fejer asymptotics as an infinite-prime-sum theorem. The **explicit-formula/zero-density lead** accepted a single zero mode only as a calibration inside a truncated explicit formula and bound the next route to the current `x,T` theorem. The **adversarial proof auditor** checked the phase boundary `|rho|/|rho-1|` and separated single-mode algebra from global zero-sum gluing. The **RAKL v3 provenance/metrology lead** used the current-work receipt to reconcile #118/#147 before routing and grants zero independent-review credit to this same-context cell.

## Episode -> diagnosis -> obstruction/lesson separation

**Episode:** `EP-RH-ANA-004a-PRIME-ERROR-KERNEL-20260811-R3` records the observed route and verification only.

**Diagnosis:** `D-RH-ANA-004a-GLOBAL-SLAMBDA-BOUND-ROOT-SCALE` — the previously tempting global bound search is badly decomposed as a child because Coffey's own source makes polynomial growth root-sufficient, while the exact Abel/Laguerre representation shows why the component retains zero-location sensitivity.

**Obstruction:** `O-RH-ANA-004a-TRUNCATED-LAGUERRE-ERROR-TRANSPORT` — the open weaker coordinate is to transport finite explicit-formula error/boundary terms through the `n`-dependent Laguerre kernel with controlled `X,T,n` quantifiers and without destroying cancellation.

**Lesson:** `L-RH-ANA-004a-ROOT-STRENGTH-AUDIT-BEFORE-GLOBAL-BOUND` — before searching a global asymptotic bound for a reformulated root-facing component, check whether the bound is already known equivalent/sufficient for the root; if so, re-atomize to a finite/truncated bridge obligation.

## Typed failures and negative history

`F-RH-ANA-004a-GLOBAL-POLYNOMIAL-BOUND-AS-CHILD` is a **decomposition/meta-policy** failure, not a mathematical refutation: the child success contract was nearly the root itself.

`F-RH-ANA-004a-FIXED-X-FEJER-TO-PRIME-SUM` is a **gluing/verification** failure family: a fixed-`x` Laguerre asymptotic cannot be summed over the infinite prime-power support without a uniform arithmetic tail theorem.

The prior process failure `F-XM011-RH-CURRENT-WORK-COVERAGE-MISS` is linked rather than repeated: current RAKL's `CurrentWorkCoverageReceipt` changed the action before routing by recovering #118 and forcing the `RH-ANA-004` / `RH-ANA-003b` reconciliation.

## Source-family completeness boundary

The bounded search consulted Coffey's two primary Li/eta sources, the live RH application routes #80/#118/#147, current truncated explicit-formula work, current zero-free/PNT-error calibration, and a uniform Laguerre asymptotic source. No claim of exhaustive literature novelty is made. No later source found in this bounded search is treated as an unconditional global `S_Lambda` closure theorem.

**Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`.
