# RH-ANA-003 primary-source packet — exact arithmetic cancellation localization

**Atom:** `RH-ANA-003`  
**Root:** Riemann Hypothesis  
**Authority:** `SOURCE_BOUND_ARITHMETIC_REPRESENTATION / NO_ROOT_AUTHORITY`  
**Framework inspected:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@6557b1b25fa839fe71aba8047c958d5da892edd8`

## Question

RH-ANA-002 ruled out a repetition of the manifestly-positive Suzuki norm route at the audited source boundary. RH-ANA-003 asks a different question: in an exact arithmetic expression for the Li coefficients, which term family is genuinely sign-sensitive after exact cancellation is preserved?

## Exact arithmetic coordinate

Bombieri--Lagarias and Coffey write the Li coefficients in a form containing the Laurent coefficients `eta_j` of `-zeta'/zeta` at `s=1`, an explicit affine term, and a binomial zeta-value contribution. Using the sign convention already frozen in RH-ANA-002,

```text
lambda_n = - sum_{j=1}^n binom(n,j) eta_{j-1}
           + 1 - (gamma + log(4*pi)) n/2
           + S1(n),

S1(n) = sum_{j=2}^n (-1)^j binom(n,j) (1-2^{-j}) zeta(j).
```

The present cycle does not infer the sign of `lambda_n`; it isolates the sign structure of `S1(n)` exactly.

## Coffey resummation

For integer `j>=2`,

```text
(1-2^{-j}) zeta(j) = sum_{q >= 1, q odd} q^{-j}.
```

Because the `j`-sum is finite and each `q^{-j}` series is absolutely convergent for `j>=2`, interchange gives

```text
S1(n)
 = sum_{q odd>=1} sum_{j=2}^n (-1)^j binom(n,j) q^{-j}
 = sum_{q odd>=1} [ (1-1/q)^n - 1 + n/q ].
```

For `q>=1`, let `x=1/q`. Bernoulli's inequality gives `(1-x)^n >= 1-nx` for integer `n>=1`, so every bracket is nonnegative. The large-`q` expansion is `n(n-1)/(2q^2)+O_n(q^{-3})`, hence the odd-integer series converges.

Therefore

```text
S1(n) >= 0  for every integer n>=1.
```

This is **not a new theorem**. Coffey's 2005 paper already records the exact rearrangement and uses it in the analysis of the Li coefficients. The research value here is source retrieval and route localization: the zeta-value/binomial family does not need a new all-`n` sign estimate once it is represented in its cancellation-preserving form.

## Why this changes the active residual

The pre-existing RH-ANA-003 description treated the arithmetic formula as broadly cancellation-heavy. That was too coarse for search control. The exact Coffey representation separates one family cleanly:

```text
known nonnegative S1(n)
+ explicit affine term
+ eta/Laurent binomial transform
= lambda_n.
```

The next sign-sensitive coordinate is therefore

```text
E_n := - sum_{j=1}^n binom(n,j) eta_{j-1},
```

considered together with the explicit affine term. Any future proof attempt must control `E_n` in a way that is genuinely uniform in `n` and does not merely import RH-equivalent zero-location or growth information.

## Hostile methodological check

Applying a triangle inequality to the original alternating zeta-value sum before resummation destroys the exact binomial cancellation. Such a bound may be mathematically true but can be qualitatively useless for the root sign question. The preferred operation is therefore:

```text
exact transform -> expose sign/cancellation -> bound the residual
```

rather than

```text
take absolute values termwise -> attempt to recover cancellation afterward.
```

This is a representation-selection result, not an RH result.

## Zero-free-region calibration

Francis C. S. Brown, *Li's criterion and zero-free regions of L-functions*, J. Number Theory 111 (2005), 1--32, DOI `10.1016/j.jnt.2004.07.016`, proves in a general Li-criterion setting that finite collections of Li-type inequalities imply bounded zero-free information and conversely that zero-free regions imply a corresponding finite collection of inequalities.

Pedro Freitas, *A Li-Type Criterion for Zero-Free Half-Planes of Riemann's Zeta Function*, J. London Math. Soc. 73 (2006), 399--414, DOI `10.1112/S0024610706022599`, constructs Li-type real functions giving necessary and sufficient conditions for zero-free strips inside the critical strip.

These sources are retained as calibration: partial Li information can encode partial zero-free information, but it does not license all-index positivity or RH.

## Primary anchors

- X.-J. Li, *The Positivity of a Sequence of Numbers and the Riemann Hypothesis*, J. Number Theory 65 (1997), 325--333, DOI `10.1006/jnth.1997.2137`.
- E. Bombieri and J. C. Lagarias, *Complements to Li's Criterion for the Riemann Hypothesis*, J. Number Theory 77 (1999), 274--287, DOI `10.1006/jnth.1999.2392`.
- M. W. Coffey, *Toward Verification of the Riemann Hypothesis: Application of the Li Criterion*, Math. Phys. Anal. Geom. 8 (2005), 211--255, DOI `10.1007/s11040-005-7584-9`, arXiv `math-ph/0505052`.
- F. C. S. Brown, *Li's criterion and zero-free regions of L-functions*, J. Number Theory 111 (2005), 1--32, DOI `10.1016/j.jnt.2004.07.016`.
- P. Freitas, *A Li-Type Criterion for Zero-Free Half-Planes of Riemann's Zeta Function*, J. London Math. Soc. 73 (2006), 399--414, DOI `10.1112/S0024610706022599`.
- J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, Ann. Inst. Fourier 57 (2007), 1689--1740, arXiv `math/0404394`.
- A. Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis*, Math. Phys. Anal. Geom. 9 (2006), 53--63, arXiv `math/0506326`.

## Boundary

No statement in this packet proves a new inequality for the `eta_j`, an all-`n` lower bound for `lambda_n`, a new zero-free region, or RH. Coffey's exact positive resummation is prior art. The retained result is a source-bound representation refinement that narrows the next research atom.
