# YM-E3a1 — invariant-ball repair of the weak-coupling quadratic recurrence

**Authority:** `PROPOSAL_SHADOW_LOCAL_MATHEMATICS_ONLY / ROOT_AUTHORITY_NONE`  
**Parent:** Yang–Mills root #5; prospective repair issue #93 (`YM-E3a`).  
**Framework used for this cycle:** `SzeChunYiu/RAKL@f5a6a11f089669a715d35bafa0a0c8affce929e3`, method `3.0.0`, package `0.1.0`.

## Exact local question

Faizal–Shabir Appendix A uses the norm recurrence

\[
x_{n+1}\le \rho x_n+C x_n^2,\qquad 0<\rho<1,\ C>0,
\]

only while the polymer activity stays in a local Banach ball. The printed Lemma A.10 omits a smallness hypothesis and its displayed induction closes with the impossible requirement `2Cr+Cr^2<=0` for positive `C,r`. The parent issue #93 prospectively froze the invariant-small-ball repair direction before this cycle.

This note asks only whether the deterministic recurrence stage can be repaired without leaving its validity domain, and whether that repair can already be glued to the same source data. It does **not** claim the FRD construction, weak-coupling entry theorem, asymptotic freedom, continuum existence, OS reconstruction, mass gap, or Millennium root.

## Primary-source packet and negative history

Primary source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1, 9 June 2026, `https://arxiv.org/pdf/2606.19362`.

Exact source surfaces consulted:

- main Theorem 5.3, PDF page 574, equations (5.6)–(5.12);
- Appendix A Theorem A.9 / Lemma A.10, PDF pages 589–592, equations (A.42)–(A.59);
- appendix references [3] Brydges–Guadagni–Mitter (2004) and [11] Seiler (1982), used by the manuscript for FRD/local-norm claims.

Negative history from #93 / PR #97 is preserved rather than re-minted: the Appendix A proof reaches `2Cr+Cr^2<=0` and then incorrectly says small positive `r` satisfies it. A screenshot recheck of PDF page 591 was attempted again in this cycle and returned backend `Cache miss`; parsed PDF text is available. A visual screenshot of main-text PDF page 574 **did** succeed and verifies the formulas quoted below.

## New source audit: the main-text contraction proof is not a clean repair

The same manuscript contains Theorem 5.3, which is structurally closer to the needed repair. It states the local expansion

\[
\Phi_{k+1}=L\Phi_k+Q(\Phi_k,\Phi_k),\qquad \|L\|\le\rho<1,\qquad \|Q(\Phi,\Phi)\|\le C\|\Phi\|^2,
\]

and explicitly chooses a small radius satisfying `Cr <= (1-rho)/2`. That is the correct *shape* of an invariant-ball condition. However, its printed proof contains a second arithmetic defect. Equation (5.11) displays

\[
\sum_{j=0}^{n-1}\rho^j\rho^{n-1-j}=n\rho^{n-1}
\le {1\over 1-\rho}\rho^{n-1}.
\]

The last inequality is false for arbitrary `n`: after cancelling the positive factor `rho^(n-1)` it asserts `n <= 1/(1-rho)`. For example `rho=1/2,n=4` gives `1/2 <= 1/4`, false. Thus Theorem 5.3's printed proof cannot itself be used as a verified repair of Appendix A.

There is a related inference defect in both locations. Theorem 5.3's displayed bound has a non-decaying additive term, and Appendix A's (A.59) has the same form. Such a bound alone does not imply the immediately asserted conclusion that the norm tends to zero exponentially. Exponential decay requires an additional strict contraction argument.

These are **local source-proof defects**. They do not show that the intended contraction statement is false.

## Correct deterministic lemma

### Lemma YM-E3a1-C001 (invariant-ball quadratic contraction)

Let `0<rho<1`, `C>0`, and let `r0>0`. Let `(x_n)_{n>=0}` be nonnegative. Assume the recurrence

\[
x_{n+1}\le \rho x_n+C x_n^2
\]

is valid whenever `x_n <= r0`. Choose `r_*` with

\[
0<r_*\le r_0,\qquad C r_* < 1-\rho,
\]

and assume `x_0<=r_*`. Set

\[
q:=\rho+C r_*<1.
\]

Then for every `n>=0`,

\[
0\le x_n\le q^n x_0\le r_*.
\]

In particular the recurrence remains inside its stated validity domain and `x_n -> 0` exponentially. Moreover, for every `n>=1`,

\[
x_n\le \rho^n x_0 + C r_*^2 {1-\rho^n\over 1-\rho}
\le \rho^n r_*+{C r_*^2\over 1-\rho},
\]

so the *shape* of Appendix (A.55) follows as a weaker estimate once the missing invariant-ball hypothesis is supplied.

### Proof

Assume inductively that `x_n<=r_*`. Since the recurrence is then licensed,

\[
x_{n+1}\le (\rho+C x_n)x_n\le (\rho+C r_*)x_n=q x_n.
\]

Because `q<1`, this implies `x_{n+1}<=x_n<=r_*`. The base case is `x_0<=r_*`, so induction gives both invariance of the ball and `x_n<=q^n x_0` for all `n`.

For the weaker Appendix-style estimate, iterate the original recurrence exactly:

\[
x_n\le \rho^n x_0+C\sum_{j=0}^{n-1}\rho^{n-1-j}x_j^2.
\]

The already-proved invariance gives `x_j^2<=r_*^2`, hence

\[
x_n\le\rho^n x_0+C r_*^2\sum_{j=0}^{n-1}\rho^{n-1-j}
=\rho^n x_0+C r_*^2{1-\rho^n\over 1-\rho}.
\]

This proves the claim. `QED`.

### Boundary case

The strict inequality is necessary for this simple exponential conclusion. If `C r_*=1-rho`, then `q=1`; the equality recurrence with `x_0=r_*` has the constant solution `x_n=r_*`. Thus a source-facing asymptotic-freedom argument must enter a **strictly smaller** ball, not merely the closed threshold.

## Same-source gluing audit

The deterministic propagation problem is solved under `C r_* < 1-rho`. Source gluing is only partial:

1. Appendix (A.43) states the quadratic estimate on a local ball. Any already-valid estimate on radius `r0` remains valid on a smaller `r_*`, with the same `rho,C`; this part is purely monotone domain restriction.
2. Appendix Step 2, especially (A.51)–(A.52), says the tuned `||Phi_K(beta_K)||` can be made as small as desired by taking `K` large. If that source step is valid with its displayed constants and hypotheses, it can target `r_*<min{r0,(1-rho)/C}` and Lemma C001 repairs the later propagation without circularly leaving the domain.
3. This cycle did **not** re-prove or primary-source-bind the manuscript's FRD assertion that one has the required nonperturbative Yang–Mills Banach map with scale-uniform `rho<1,C<infinity`, nor the full tuning argument that reaches the prescribed smaller radius. The manuscript cites BGM 2004 and Seiler 1982 for general FRD/constructive ingredients, but no exact theorem from those sources was acquired in this cycle that supplies this Yang–Mills-specific nonlinear RG map and constants. Under the source-detail rule, that interface remains `BLOCKED` rather than reconstructed from memory.
4. Even a complete repair of A.9 would remain separate from the already-recorded bare-coupling escape issue #69, gap-transport issues #73/#92, OS/quotient/source-completeness issues #126/#133/#109, continuum existence/nontriviality, and the root gates.

Hence the outcome is:

`LOCAL_MATHEMATICAL_REPAIR_PROVED / SOURCE_SPECIFIC_FRD_ENTRY_AND_CONSTANT_BINDING_BLOCKED / ROOT_OPEN`.

## Same-context expert cell findings

These role-separated passes share the same context and count as **zero independent mathematical reviews**.

- **Nonlinear discrete dynamics:** the invariant-ball proof above is sufficient; strict `Cr_*<1-rho` gives a stronger `q^n` estimate and exposes the equality-case hostile control.
- **Constructive RG / polymer norms:** shrinking a valid local ball is type-safe, but one must preserve the same norm and constants and separately prove entry into the shrunk ball. The local recurrence cannot license itself after an iterate leaves its domain.
- **Constructive continuum QFT:** the result is only a local weak-coupling RG propagation lemma. It does not establish continuum measures, gauge/OS reconstruction, nontriviality, or a physical gap.
- **Primary-source mathematical physics:** the main-text Theorem 5.3 does contain the correct smallness *shape*, but its equation (5.11) is algebraically invalid and therefore cannot be cited as a verified proof of the repair. Exact source-specific FRD constants remain unbound.
- **Adversarial proof review:** the constant-floor estimates do not imply decay; the strict threshold and same-domain induction are essential. Equality at the threshold gives a fixed-point countercontrol.
- **RAKL v3 assurance/metrology:** classify the local proof separately from source/gluing residuals; same-context review is not independent; no protected lesson/obstruction/root promotion follows.

## Residual / next action

The smallest next source-facing discriminator is now exact: acquire a primary mathematical theorem for the **same Yang–Mills FRD/polymer norm** that supplies the local nonlinear RG estimate with scale-uniform `rho<1,C` and validate the tuning step into a prescribed `r_*<min{r0,(1-rho)/C}`. If that cannot be source-bound, keep the weak-coupling/asymptotic-freedom bridge blocked. Do not spend another cycle re-proving the scalar recurrence.
