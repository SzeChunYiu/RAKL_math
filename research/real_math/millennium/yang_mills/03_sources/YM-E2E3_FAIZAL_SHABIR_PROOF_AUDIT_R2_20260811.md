# YM-E2/E3 retrospective source-proof audit R2 — Faizal–Shabir 2026

**Date:** 2026-08-11  
**RAKL framework inspected first:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**RAKL_math base:** `6557b1b25fa839fe71aba8047c958d5da892edd8`  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE` under `SzeChunYiu/RAKL_math#5`  
**Authority:** `RETROSPECTIVE_PRIMARY_SOURCE_PROOF_AUDIT / SAME_CONTEXT_INTERNAL_REVIEW / NO_MATHEMATICAL_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

## Scope and chronology

This cycle re-audits the 2026 claimed full solution by Mir Faizal and Arshid Shabir:

- Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1, 9 June 2026, <https://arxiv.org/abs/2606.19362>.
- Published version: *Fortschritte der Physik* 74(4), e70097, DOI `10.1002/prop.70097`.

The prior RAKL_math audit already isolated a gap-margin obligation: summability of nonnegative defects does not by itself imply that their total is less than the initial gap. That observation is preserved in `F-YM-E2-SUMMABLE-DEFECT-POSITIVE-GAP-BUDGET` and prospective issue #73 (`YM-E2a`).

The two proof defects below were noticed **before** a fresh strict packet for them was frozen. They are therefore permanently retrospective source-audit evidence. No context-first candidate chronology is backfilled. The only prospective objects created in this cycle are the repair questions in issues #92 and #93.

## Finding 1 — main-text physical-gap step scaling uses two unsupported uniformizations

### Exact source chain

Theorem 5.4 defines the physical spectral gap at scale `k` by

\[
\Delta_k=-a_k^{-1}\log \lambda_2(T_k)
\]

and states a step inequality `Delta_{k+1} >= Delta_k - epsilon_k` with `epsilon_k <= C theta^k`.

From its interlacing estimate the proof obtains

\[
e^{-a_{k+1}\Delta_{k+1}}
\le e^{-b a_k\Delta_k}+\|E_k\|,
\qquad a_{k+1}=b a_k,
\]

and then the exact lower bound

\[
\Delta_{k+1}\ge
\Delta_k-\frac{e^{a_{k+1}\Delta_k}}{a_{k+1}}\|E_k\|.
\tag{FS-5.36}
\]

These are source equations (5.34)–(5.36), arXiv PDF around pp. 52–53.

The next paragraph makes two additional moves:

1. from `lambda_2(T_k) in [0,1)` it obtains `Delta_k in [0,infinity)` and then asserts
   \[
   e^{a_{k+1}\Delta_k}\le e^{a_{k+1}};
   \]
2. because `(a_k)` is geometric with ratio `b`, it calls `a_{k+1}` uniformly comparable to `1`, yielding scale-independent bounds on both `a_{k+1}^{-1}` and `e^{a_{k+1}}`.

These steps are then used to turn the exact loss in (FS-5.36) into `C theta^k`.

### Cheap hostile checks

The first implication does not follow from the displayed hypothesis. Nonnegativity of `Delta_k` supplies no upper bound. For example, at `a_{k+1}=1`, `Delta_k=2` gives `e^{a Delta}=e^2>e`.

The second uniformity statement also does not follow from an unrestricted geometric recursion `a_{k+1}=b a_k` with `b>1` and fixed `a_0>0`; then `a_k=b^k a_0` grows without a `k`-independent upper bound.

Therefore the **written proof of the main-text Theorem 5.4 does not establish its claimed scale-independent geometric defect bound without additional normalization/range hypotheses**.

This is a proof defect, not an impossibility theorem. A finite physical scale range, a different normalization, or a sharper use of the exact logarithmic inequality could conceivably repair it.

### Why Appendix D matters but does not silently repair the main text

Appendix D explicitly changes coordinates. It starts:

> fixed physical time step `tau > 0`

and sets

\[
T_{k,L}=e^{-\tau H_{k,L}},
\]

then defines the bounded transfer-gap coordinate

\[
\delta_{k,L}=1-\|T_{k,L}|_{Q_{k,L}}\|\in(0,1].
\]

In this fixed-`tau` coordinate, Theorem D.4 obtains the additive transport
\[
\delta_{k+1,L}\ge\delta_{k,L}-\epsilon_k
\]
without the factor `e^{a_{k+1} Delta_k}/a_{k+1}`.

That is a plausible repair route, but it is **not the same displayed argument** as Theorem 5.4. A root-facing use must bind the variable-lattice one-step family and the fixed-physical-time family to the same OS/Hamiltonian continuum object, with exact scale and limit quantifiers. Moreover Corollary D.5 still needs the already-open relative condition
\[
\sum_k\epsilon_k<\delta_0,
\]
which is the subject of issue #73.

Prospective repair atom: **#92 `YM-E2b`**.

## Finding 2 — Appendix A weak-coupling contraction induction closes with an impossible inequality

### Exact source chain

Theorem A.9 is the source's weak-coupling entry/contraction theorem. Its Step 3 reduces the polymer norm to the deterministic recurrence

\[
x_{n+1}\le \rho x_n+C x_n^2,\qquad 0<\rho<1,\ C>0.
\]

Lemma A.10 then claims

\[
x_n\le \rho^n r+\frac{C}{1-\rho}r^2.
\tag{FS-A.55}
\]

The proof defines the right-hand comparison sequence and, at its final induction step, obtains a factor `1 + 2Cr + Cr^2`. It then requires

\[
2Cr+Cr^2\le0
\tag{FS-A.58-condition}
\]

and states that this is satisfied by taking positive `r` sufficiently small.

For every `C>0` and `r>0`,
\[
2Cr+Cr^2=Cr(2+r)>0.
\]
Thus the printed condition cannot hold and the written induction does not close.

The lemma as literally stated also has no invariant-ball/smallness condition beyond `x_0<=r`. A simple recurrence-equality hostile world illustrates why such a condition matters: with `rho=1/2`, `C=1`, `r=1`, one gets `x_0=1`, `x_1=3/2`, `x_2=3`, while the claimed `n=2` upper bound is `9/4`.

That counterexample is to **Lemma A.10 as stated**, not directly to the intended small-polymer application. The RG quadratic estimate immediately before Theorem A.9 is itself stated only inside a small norm ball. A corrected invariant-ball argument may therefore repair the intended theorem if its constants and entry step are source-bound consistently.

### Downstream scope

The source immediately applies Lemma A.10 to `x_n=||Phi_{K+n}(beta_K)||` to obtain the contraction estimate in Theorem A.9, and then uses exponential decay of this norm to state nonperturbative asymptotic freedom and identification with the claimed continuum limit.

Therefore the written weak-coupling/asymptotic-freedom proof chain contains a local proof gap. This does **not** establish that no corrected weak-coupling construction exists.

Prospective repair atom: **#93 `YM-E3a`**.

## Relation to prior failure memory

Selected prior memory:
- `F-YM-E2-SUMMABLE-DEFECT-POSITIVE-GAP-BUDGET`
- prospective child `YM-E2a` / issue #73

Rejected as causal explanation:
- `YM-E1a1a0` Bałaban averaging-source blocker. It concerns missing primary block definitions, not the algebra of this claimed solution.
- `F-YM-E1A1-FINITE-LOOP-GEOMETRY-CLOSURE`. It is a separate operator-basis compression failure.
- `F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE`. It is a spectral observability failure.

The prior `YM-E2` memory materially changed the search policy: instead of re-reading the claimed result at the headline level, the cycle followed the exact defect-transport proof chain and compared the main-text physical-gap normalization with Appendix D's fixed-`tau` formulation. No prospectively frozen pre-memory action ranking exists, so a causal effect size cannot be claimed.

## Same-context expert cell

These are role-separated analytical passes, **not independent peer review**.

| Lens | Background / delegated question | Finding / vote |
|---|---|---|
| Constructive QFT / OS | Euclidean positivity, transfer semigroup, continuum reconstruction | Main-text and Appendix-D transfer coordinates must be explicitly identified before either can carry root gap authority. **REVISE** |
| Transfer-operator spectral theory | `T=e^{-tH}`, transfer vs Hamiltonian gaps, scale normalization | Equation (5.36) is exact as displayed, but the next exponential uniformization needs an upper gap/scale bound not supplied there. **BLOCK current proof use** |
| Constructive RG / scaling | blocking factor, lattice spacing, finite-range defects | A geometric coarse spacing is not uniformly bounded for unrestricted `k`; finite-range/physical-scale scope must be explicit. **BLOCK current proof use** |
| Nonlinear dynamics / asymptotic freedom | invariant small balls and quadratic recurrences | Lemma A.10's printed closing inequality is impossible for positive `C,r`; a corrected invariant-domain lemma is required. **BLOCK current A.9 proof use** |
| Adversarial mathematical physics | cheapest counterworlds and hidden quantifiers | `Delta>1`, unbounded geometric `a_k`, and the recurrence example refute the unsupported intermediate statements at their literal scope. **BLOCK** |
| Formal methods / assurance | statement binding, dependency and chronology | Findings are retrospective; #92/#93 begin only the repair questions. No candidate or theorem authority. **ACCEPT scoped audit** |
| Novelty / source audit | prior art vs correction significance | These are source-proof diagnostics of a 2026 claimed solution, not new Yang–Mills theorems. Preserve exact source scope and avoid “paper disproved” language. **ACCEPT narrow reporting** |

### Cross-lens synthesis

Consensus is narrow:
1. the two written proof steps above are invalid at their displayed scope;
2. both may be repairable with additional hypotheses or a different formulation;
3. no current root-solution certificate may rely on these steps without the repairs;
4. #73 remains unchanged as the prospectively frozen relative-defect-budget atom;
5. #92 and #93 are separate prospective repair atoms because they concern different proof interfaces.

## RAKL method case classification

- **Episode:** exact primary-source proof audit of a 2026 claimed full solution.
- **Diagnosis 1:** main-text gap step-scaling proof has an unsupported scale/gap uniformization.
- **Diagnosis 2:** weak-coupling recurrence lemma has a broken induction and missing invariant-domain condition.
- **Obstructions:** #92 and #93 freeze the two repair questions.
- **Lesson:** none promoted. One cycle is not sufficient to mint a reusable framework lesson.
- **Failure category:** source-proof / representation-normalization / gluing-to-root.
- **Problem novelty class:** `UNRESOLVED`; no verified Yang–Mills solution/subsolution is promoted.
- **Root authority:** none.

## Next action

Do **not** continue theorem invention from the claimed solution as though the gap and weak-coupling chains were closed.

The highest-information next checks are now split:
- #73: prospective quantitative total-defect margin in the fixed-`tau` route;
- #92: prospective same-theory normalization/limit bridge from variable lattice step to fixed physical time;
- #93: prospective corrected weak-coupling recurrence plus source-bound invariant-domain constants.

Each child must begin with fresh current-RAKL context, transfer/disanalogy, dual memory, expert review and trace before any repair candidate is generated.
