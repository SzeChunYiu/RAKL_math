# RH-ANA-003b — whole-prime-component root-strength audit (R3)

**Authority:** proposal/shadow only; exact source-bound decomposition audit; no RH theorem, no Li-sign theorem, no novelty claim, no promotion.

## Question

The predecessor residual asked whether Coffey's cancellation-preserving component
`S_Lambda(n)` could be bounded strongly enough to control every Li coefficient.
Before searching for such a bound, this cycle tests a cheaper discriminator:
**would a subexponential bound on the whole `S_Lambda` already carry RH strength?**

## Primary-source packet

1. Coffey, arXiv:`math-ph/0505052`, Theorem 1 and Eq. (16):
   `lambda_n = S_2(n) + S_1(n) + 1 - n(γ+log π+2 log 2)/2`,
   with `S_2(n)=-sum_{m=1}^n binom(n,m) eta_{m-1}`.
   Theorem 2 plus the stated upper bound give
   `S_1(n) = (n/2) log n + O(n)`.

2. Coffey, arXiv:`0706.0343`v2, Proposition 2:
   `S_2(n)=S_gamma(n)+S_Lambda(n)`,
   `S_Lambda(n)=sum_{m>=1}(1-Lambda(m))/m * L_{n-1}^1(log m)`,
   and `S_gamma(n)=O(n)`.
   This is a structured `[1-Lambda(m)]` Laguerre sum; it is not replaced here
   by a termwise-positive prime sum.

3. Lagarias, arXiv:`math/0404394`v4, Theorem 1.1 and the paragraph following it:
   the Li coefficient is a polynomial-size archimedean term minus an incomplete
   Li coefficient plus `O(sqrt(n) log n)`; if RH fails, the incomplete Li term is
   sometimes of exponential size in `n`, a phenomenon explicitly noted there
   for the Riemann zeta function via Bombieri--Lagarias Theorem 1(c).

A bounded current-literature search was also run on 2026-08-11 for later Li
representations / explicit-formula bounds. No newer primary source found in that
search superseded these exact identities. Non-primary claimed proofs and
unrelated explicit-formula error-term papers were rejected as authority for this atom.

## Exact algebraic reduction

Combining the two Coffey identities,

`lambda_n = S_Lambda(n) + S_gamma(n) + S_1(n)
            + 1 - n(γ+log π+2 log 2)/2`.

Using `S_gamma(n)=O(n)` and the two-sided bound
`S_1(n)=(n/2)log n+O(n)` gives

`lambda_n = S_Lambda(n) + (n/2)log n + O(n)`.        (R3.1)

Thus `lambda_n-S_Lambda(n)` is unconditionally subexponential.

Now suppose the proposed local target were an unconditional whole-component
bound

`S_Lambda(n)=exp(o(n))`.                              (R3.2)

Equation (R3.1) would imply `lambda_n=exp(o(n))`. Lagarias' false-RH
exponential alternative says that when RH fails the relevant incomplete Li
coefficient is sometimes exponential in `n`; by Theorem 1.1 the full Li
coefficient then differs from that exponential term only by polynomial-size
terms. Therefore (R3.2) excludes failure of RH.

Conversely, under RH Lagarias gives polynomial Li growth, while (R3.1) has only
polynomial deterministic remainder; hence the whole `S_Lambda` is
subexponential. Subject to the cited source theorem's zeta specialization, the
target `S_Lambda(n)=exp(o(n))` is therefore **RH-strength**, not a safely weaker
supporting lemma.

This statement is a route-strength equivalence/implication audit. It neither
proves (R3.2) nor RH.

## Expert-cell review (same context, not independent)

- **E-ANT (zeta/Li):** accepted (R3.1) from the exact Coffey formulas and rejected
  treating all-index whole-`S_Lambda` subexponentiality as routine prime-side control.
- **E-PRIME (von Mangoldt/explicit formula):** emphasized that
  `[1-Lambda(m)] L_{n-1}^1(log m)/m` already packages delicate integer/prime-power
  cancellation; source identity must stay intact.
- **E-ASYM (asymptotics):** verified that adding/subtracting `O(n log n)` cannot
  hide an exponential-versus-subexponential discriminator.
- **E-FALS (adversarial):** used the root-strength test as the falsifier for the
  proposed “bound the whole component first” decomposition.
- **E-VERIFY (formal logic):** separated source theorems, elementary substitution,
  and the root-strength inference; no positivity or sign claim was inserted.
- **E-RAKL (v3):** current v3 explicitly makes experience/routing transitions
  authority-inert and reserves scientific authority for certificate-bound transitions;
  no authority transition is invoked here.

These are six same-context roles only and provide zero independent-review credit.

## Failure separation

**Decomposition failure — `F-RH-ANA-003b-WHOLE-SLAMBDA-SUBEXP-ROOT-STRENGTH`.**
Treating `S_Lambda=exp(o(n))` (or any polynomial bound) as a smaller local
subproblem collapses the decomposition: success would already exclude the
false-RH exponential Li alternative.

**Gluing failure — `F-RH-ANA-003b-SLAMBDA-BOUND-AS-SUPPORT-LEMMA`.**
The whole-component bound cannot be glued as merely supportive evidence and then
promoted separately; the exact decomposition carries it directly to a
root-strength global statement.

No local mathematical contradiction in Coffey's decomposition is alleged.

## New residual

`RH-ANA-003c — PRIME_KERNEL_NONCIRCULAR_DECOMPOSITION`

Construct or source-bind a decomposition of `S_Lambda(n)` (or an equivalent
finite-place object) into pieces whose proposed **local** control has a
DifferenceWitness proving it is strictly weaker than whole-component
subexponentiality/RH. The root-sensitive remainder must remain explicit. Any
candidate bound must first pass a strength audit showing that the candidate
alone does not imply subexponential Li growth, Li positivity, a zero-free
critical-strip statement equivalent to RH, or the exclusion of all off-line zeros.

**Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`.
