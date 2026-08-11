# RH-ANA-004a source-interface erratum — selected truncation height versus Laguerre integral

**Authority:** append-only verification correction to the R3 shadow result; no mathematical/root authority.

This note **supersedes only** the paragraph in `RH_ANA_004a_PRIME_ERROR_LAGUERRE_AUDIT_20260811_R3.md` that informally wrote the transformed 2026 explicit-formula error as `(M/T) integral u^{1-omega} L_{n-1}^{(2)}(u) du`. That shorthand is too strong and must not be used.

Johnston--Cully-Hugill, arXiv:`2402.04272`, Theorem 1.2 states a truncated Riemann--von Mangoldt formula with an error bounded by `M x (log x)^{1-omega}/T` at **some** truncation ordinate `T* in [T,2T]`, subject to an admissibility condition involving `x` and `T`. The displayed theorem does not, merely from that statement, supply one common `T*` that can be inserted unchanged throughout an `x`-integration interval.

For any pointwise valid source decomposition

`psi(x) = x - Z(x,T*) + E(x,T*)`,

where `Z` is the finite zero sum and `E` is the actual remainder, the prime-error/Laguerre contribution is the exact functional

`- integral E(x,T*) x^{-2} L_{n-1}^{(2)}(log x) dx`,

with the integration domain restricted to points where the source formula and chosen truncation interface are valid. Only after this exact functional is written may a pointwise remainder bound yield a magnitude estimate such as

`<= (M/T) integral (log x)^{1-omega} x^{-1} |L_{n-1}^{(2)}(log x)| dx`.

Two distinct losses therefore have to be audited:

1. **selection/gluing:** whether a single finite zero set / truncation height can be chosen coherently over the integration interval, or whether an `x`-dependent `T*(x)` changes the zero-sum object under the integral;
2. **magnitude/cancellation:** if the remainder is replaced by its pointwise absolute bound, the Laguerre oscillation is discarded and a new `n`-uniformity loss may appear.

The same 2026 paper recalls the earlier fixed-`T` theorem (Theorem 1.1 there, from the authors' earlier explicit-formula work) with an `O(x log x/T)` remainder. That interface is asymptotically weaker but may be structurally easier to integrate because the truncation ordinate is not existentially reselected in the displayed formula. The next atom must compare these interfaces rather than silently treating the sharper selected-`T*` theorem as a fixed finite zero sum.

New typed failure family:

`F-RH-ANA-004a-TSTAR-SELECTION-TO-LAGUERRE-INTEGRAL` — **source-interface / gluing / verification**. A pointwise theorem with an existentially selected truncation ordinate cannot be substituted under the Laguerre integral as though it supplied one common finite zero set, absent a uniform selection theorem.

This correction strengthens, rather than closes, `O-RH-ANA-004a-TRUNCATED-LAGUERRE-ERROR-TRANSPORT`. `RH-ANA-004b` remains `CONTEXT_REQUIRED` and must explicitly choose and audit the fixed-`T` versus selected-`T*` source interface.

**Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`.
