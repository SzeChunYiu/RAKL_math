# RH-ANA-003 result — exact odd-integer resummation localizes the arithmetic sign residual

**Candidate:** `CAND-RH-ANA-003-COFFEY-ODD-RESUMMATION-AUDIT`  
**Verdict:** `SOURCE_BOUND_REPRESENTATION_LOCALIZATION / PARTIAL_SUCCESS`  
**Novelty:** `PRIOR_ART_RETRIEVAL_NOT_NEW_THEOREM`  
**Root authority:** `NONE`

## Result

For the exact zeta-value/binomial component

```text
S1(n) = sum_{j=2}^n (-1)^j binom(n,j) (1-2^{-j}) zeta(j),
```

Coffey's arithmetic treatment permits the exact rewrite

```text
S1(n) = sum_{q odd>=1} [ (1-1/q)^n - 1 + n/q ].
```

The derivation is elementary once the primary-source representation is fixed:

1. `(1-2^{-j})zeta(j)=sum_{q odd>=1}q^{-j}` for `j>=2`.
2. The `j`-sum is finite, and each odd-`q` Dirichlet series is absolutely convergent, so interchange is legitimate.
3. The binomial theorem gives
   `sum_{j=2}^n (-1)^j C(n,j)q^{-j}=(1-1/q)^n-1+n/q`.
4. Bernoulli's inequality gives `(1-1/q)^n >= 1-n/q`, hence every summand is nonnegative.
5. The summand is `O_n(q^{-2})`, so the resulting odd-integer series converges.

Thus `S1(n)>=0` for every integer `n>=1`.

## Falsifiers run

- `n=1`: both sides are zero.
- `n=2`: each odd-`q` summand equals `q^{-2}`, matching the one retained binomial term.
- exact rational finite-`q` algebra is regression-tested in `tests/math_applications/test_rh_ana_003_odd_resummation.py`.
- the test explicitly distinguishes the signed sum from a coefficientwise absolute-value surrogate.
- no finite truncation is promoted to an all-index result.

## What this eliminates from the active search

The original zeta-value/binomial family is not the first unknown sign bottleneck. Searching for a new coefficientwise bound on it is low-information because its exact cancellation is already known and produces a nonnegative representation.

The arithmetic formula should instead be organized as

```text
lambda_n = E_n + A_n + S1(n),

E_n = -sum_{j=1}^n C(n,j) eta_{j-1},
A_n = 1 - (gamma + log(4*pi))n/2,
S1(n) >= 0.
```

The remaining research question is not whether `S1` is positive. It is whether `E_n` admits a cancellation-preserving, zeta-specific, unconditional all-`n` representation or estimate strong enough to control the total without importing RH-equivalent information.

## What this does not show

- no new theorem beyond cited prior art;
- no new lower bound for `lambda_n`;
- no bound for `eta_j` or `E_n`;
- no new zero-free region;
- no prime-by-prime positivity statement;
- no evidence that an eta-based route will succeed;
- no progress toward root promotion of RH.

## Research-method consequence

The cycle supports a scoped search heuristic: **preserve exact cancellation before bounding**. In cancellation-heavy explicit formulas, a termwise absolute-value estimate can destroy the very structure required to see the correct residual. This heuristic remains proposal-level until it transfers successfully in other registered contexts.
