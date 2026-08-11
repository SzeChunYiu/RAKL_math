# Same-context expert review — RH-ANA-003

**Scope:** strict pre-candidate review of the arithmetic Li-coefficient representation.  
**Independence:** role-separated same-context AI review only. This is **not** independent mathematical review and grants no root authority.  
**Framework:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`.

## Domain / analytic-number-theory lead

**Evidence inspected.** Li criterion; Bombieri--Lagarias arithmetic formula as already bound in RH-ANA-002; Coffey 2005; Brown 2005; Freitas 2006; prior RH-ANA-001/002 negative history.

**Finding.** The Coffey resummation is exact and source-relevant. With

```text
S1(n)=sum_{j=2}^n (-1)^j C(n,j)(1-2^{-j})zeta(j),
```

one may use `(1-2^{-j})zeta(j)=sum_{q odd}q^{-j}` and the binomial theorem to obtain

```text
S1(n)=sum_{q odd>=1}[(1-1/q)^n-1+n/q] >= 0.
```

This does not prove Li positivity because the eta/Laurent binomial term and affine term remain.

**Strongest objection.** Calling this "prime positivity" would be false; the resummation is over odd integers. Calling the identity novel would also be false because Coffey records it.

**Vote:** ACCEPT as source-bound representation localization; BLOCK any theorem/RH promotion.

## Analogy / method-transfer lead

**Finding.** The useful transfer is the cancellation-preserving-transform principle: do not take absolute values before exposing an exact transform that retains alternating cancellation. The analogy is structural only.

**Strongest objection.** A representation that makes one component positive can still move the real obstruction into the residual. The next atom must explicitly preserve the total arithmetic identity.

**Vote:** ACCEPT with target-specific residual tracking.

## Adversarial falsification lead

**Checks required.** Verify the sign convention; test `n=1` where `S1(1)=0`; test `n=2` where the resummed summands are nonnegative; justify sum interchange; check convergence at large odd `q`; reject any finite truncation as all-index evidence.

**Finding.** The algebraic sign claim survives these checks. For `n>=1`, Bernoulli gives `(1-1/q)^n-1+n/q>=0`; for fixed `n`, the bracket is `O(q^{-2})`.

**Strongest objection.** The positive term can be asymptotically large while the eta transform remains negative; nothing here bounds the latter. Any next step that estimates `eta_j` coefficientwise must be tested for cancellation loss.

**Vote:** ACCEPT the local rewrite; REVISE the search target to eta/Laurent control.

## Formal-methods lead

**Formalizable obligations.** The finite-binomial identity can be checked exactly over rationals for arbitrary finite `n,q`; Bernoulli positivity is elementary; the analytic interchange follows because the outer `j` set is finite and each `j>=2` odd-integer Dirichlet series converges absolutely.

**Trust boundary.** A finite test suite verifies implementation/algebra examples, not the theorem for every `n`; the general proof is the source-bound binomial/Bernoulli argument.

**Vote:** ACCEPT as checker-friendly algebraic subclaim; no proof authority beyond the stated identity.

## Novelty / research-value lead

**Prior-art judgment.** The resummation is Coffey prior art. No mathematical novelty claim is admissible.

**Research value.** It is nevertheless consequential for RAKL search control because the current RH-ANA-003 residual was too coarse: one whole cancellation family can be retired from active sign uncertainty, and the next atom can focus on the eta/Laurent transform instead of inventing a new bound for `S1(n)`.

**Vote:** ACCEPT as retrieval/representation progress; BLOCK novelty language.

## Joint bounded recommendation

Proceed only with the following candidate-free source audit: bind the exact Coffey resummation, run algebraic hostile checks, record `S1(n)>=0` as known source knowledge, and open a child atom for the eta/Laurent binomial transform. Do **not** propose an RH inequality, eta conjecture, mollifier, resonance scheme, or prime truncation in this cycle.

**Unresolved uncertainty:** whether the eta/Laurent transform admits a cancellation-preserving representation with an unconditional all-`n` estimate strictly weaker than RH remains open.
