# RH-ANA-003 primary-source packet — finite-place / incomplete-Li cut

**Atom:** `RH-ANA-003`  
**Authority:** `PRIMARY_SOURCE_CONTEXT / PRE_CANDIDATE / NO_RH_AUTHORITY`  
**Framework read:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@8a608f340d47b4b6ae612275b0595faf6b804432`  
**Checked:** 2026-08-11

## 1. Exact target boundary

The root remains the Clay/Bombieri Riemann Hypothesis. `RH-ANA-003` is a representation/bridge child only. It asks where an exact prime/archimedean representation of the Li coefficients first becomes root-sensitive when one demands an unconditional estimate uniform in the coefficient index `n`.

No finite zero verification, finite Li computation, zero-density estimate, explicit formula, or positive surrogate is promoted to RH.

## 2. Bombieri–Lagarias

Primary publication:

- Enrico Bombieri and Jeffrey C. Lagarias, *Complements to Li's Criterion for the Riemann Hypothesis*, Journal of Number Theory 77 (1999), 274–287, DOI `10.1006/jnth.1999.2392`.

Source-level fact used here: Li's criterion is generalized to symmetric multisets, and the Li coefficients are represented arithmetically through the Guinand–Weil explicit formula. This source licenses the use of exact Li/Weil arithmetic representations but does not make their signed prime-side pieces termwise positive.

## 3. Lagarias 2007 finite-place / incomplete-Li boundary

Primary publication:

- Jeffrey C. Lagarias, *Li Coefficients for Automorphic L-Functions*, Annales de l'Institut Fourier 57 (2007), 1689–1740, arXiv `math/0404394v4`, DOI `10.5802/aif.2311`.

Section 6 defines the incomplete Li coefficient
\[
\lambda_n(T,\pi)=
\sum_{\rho\in Z(\pi),\,|\operatorname{Im}\rho|\le T}
\left[1-\left(1-\frac1\rho\right)^n\right].
\]

Theorem 6.1 gives, for an irreducible cuspidal unitary automorphic representation,
\[
S_f(n,\pi)
=
\lambda_n(\sqrt n,\pi^\vee)
+
O_\pi(\sqrt n\log n),
\]
and then states separately that **if RH holds for \(L(s,\pi)\)**,
\[
\lambda_n(\sqrt n,\pi^\vee)=O_\pi(\sqrt n\log n).
\]

This is the key source boundary for this atom. The first formula localizes the finite-place contribution to a truncated zero-power sum plus a controlled error. The second smallness statement is RH-conditional and must not be imported as an unconditional bridge.

Lagarias' Section 5 supplies an unconditional archimedean asymptotic of the form
\[
S_\infty(n,\pi)
=
\frac{N}{2}n\log n + C_1(\pi)n + O_\pi(1)
\]
at the registered level. Thus, in this decomposition, the hard sign/uniformity coordinate is not merely the deterministic archimedean main term.

## 4. Radial sensitivity of Li powers

For the classical Li transform
\[
q(\rho)=1-\frac1\rho=\frac{\rho-1}{\rho},
\qquad
\rho=\beta+i\gamma,
\]
one has
\[
|q(\rho)|^2
=
\frac{(\beta-1)^2+\gamma^2}{\beta^2+\gamma^2}
=
1+\frac{1-2\beta}{\beta^2+\gamma^2}.
\]

Therefore `Re(rho)=1/2` is exactly the unit-modulus radial boundary for this factor. If `beta<1/2`, then `|q(rho)|>1`; the functional-equation partner has the reciprocal radius. This algebra explains why a rare off-line defect can be exponentially amplified in the power index even when ordinary zero-counting remains unchanged.

This calculation is a logical calibration. It is not evidence that zeta has such a zero.

## 5. Palojärvi 2018 as a rare-outlier calibration

Primary preprint:

- Neea Palojärvi, *Explicit zero-free regions and a \(\tau\)-Li-type criterion*, arXiv `1807.01506`.

The paper studies
\[
\lambda_F(n,\tau)
=
\lim_{t\to\infty}
\sum_{|\operatorname{Im}\rho|\le t}
\left[1-\left(\frac{\rho}{\rho-\tau}\right)^n\right]
\]
under explicit zero-count assumptions. Theorems 3.1 and 3.3 connect finite intervals of Li-type signs to exclusion/detection of zeros outside radial regions
\[
\left|\frac{\rho}{\rho-\tau}\right|<R.
\]

The paper explicitly separates high-imaginary-part and low-imaginary-part zero contributions and later treats a one-off-region-zero case. It therefore supports the structural distinction used here:

```text
zero count / density
!=
radial envelope / outlier control.
```

It does **not** supply RH and is not used as one.

## 6. Historical caution on finite Li / zero-free-region converses

Palojärvi notes that Brown's 2005 converse direction relied on a lemma with errors and that one of the errors remained unrepaired in that line of proof. This is relevant method history: finite Li-sign / zero-free-region implications need exact source verification and cannot be inferred from a familiar theorem label.

## 7. Current source-bounded residual

The source packet supports the following pre-candidate localization:

1. the archimedean main contribution has a source-proved unconditional asymptotic;
2. the finite-place contribution is tied to an incomplete Li power sum at height \(\sqrt n\), up to a controlled error;
3. the small incomplete-Li bound quoted by Lagarias is RH-conditional;
4. aggregate zero counting controls how many terms occur but does not by itself force their Li radial factors to have modulus one;
5. any candidate based only on zero count/density must therefore be hostile-tested against one permitted radial outlier before it is treated as a uniform Li-tail mechanism.

The unresolved mathematical question is whether zeta-specific arithmetic cancellation, a weighted horizontal-displacement theorem, or another strictly weaker uniform condition can control the finite-place term without already assuming an RH-equivalent zero-location statement.

## 8. Evidence boundary

This packet is context evidence only. It licenses no new inequality, no zero-free theorem, no Li positivity statement, and no RH claim. A materially new mathematical candidate remains forbidden until the fresh context fiber, expert review, dual-memory review, and hash-chained pre-candidate trace are frozen.
