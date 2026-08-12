# RH-ANA-003b — full \(S_\Lambda\) polynomial-smallness root-coupling audit (R3)

**Authority:** source-bound compositional route lemma / proposal-shadow TaskEpisode evidence / same-context expert synthesis / no independent mathematical review / no RH proof / no literature-novelty claim / root authority none.

## Frozen chronology

No R3 mathematical candidate was opened before the following artifacts were committed on `research/rh-ana003-prime-tail-v3-20260811`:

- `RH_ANA_003b_CONTEXT_FIBER_20260811_R3.json`, fibre hash `sha256:352f3b5356058131707a52f85d024207871511e43ecc8eadc24333d2ec531b0e`;
- `RH_ANA_003b_RESEARCH_MEMORY_REVIEW_20260811_R3.json`, artifact hash `sha256:8b2937ae570ea2bfe901d955d9dd3f8dbb3c1cc88532ef212f49d076c01d10e3`;
- `RH_ANA_003b_PRE_CANDIDATE_TRACE_20260811_R3.json`, final event `RH-ANA-003b-E07`, hash `sha256:767dbfd6e1bad2328dd7a36e21b7b242b9b137a0522ee54e46ddf97a8ff631ff`.

Current framework source of truth was read first as `SzeChunYiu/RAKL@e10abeda6a9f1b22f7a0846745ce342131a17e33`, method `3.0.0`. Current application main at cycle start was `SzeChunYiu/RAKL_math@9c2cebe8d5a2b1381af5a40cbea86a6826e7210a`. The work branch was behind current application main and therefore remains shadow evidence only.

## Exact primary-source binding

### Coffey: the prime/Laguerre remainder is the whole oscillatory \(S_2\) remainder modulo a tame Stieltjes term

Mark W. Coffey, *The Stieltjes constants, their relation to the \(\eta_j\) coefficients, and representation of the Hurwitz zeta function*, arXiv:`0706.0343v2` (25 Feb 2009), Proposition 2, equations (14)–(17), defines

\[
S_2(n)=-\sum_{m=1}^n {n\choose m}\eta_{m-1}
\]

and proves

\[
S_2(n)=S_\gamma(n)+S_\Lambda(n),
\]

where

\[
S_\Lambda(n)=\sum_{m=1}^{\infty}\frac{1-\Lambda(m)}{m}
L_{n-1}^{1}(\log m)
\]

and \(S_\gamma(n)=O(n)\). The source also writes the \(m=1\) term separately as \(n+\sum_{m\ge2}\cdots\).

Mark W. Coffey, *Toward verification of the Riemann hypothesis: Application of the Li criterion*, arXiv:`math-ph/0505052v1` (19 May 2005), Theorem 1, equation (10), gives

\[
\lambda_n
= S_2(n)+S_1(n)+1-\frac n2(\gamma+\log\pi+2\log2).
\]

Its Theorem 2 and the displayed companion upper bound give

\[
S_1(n)=\frac n2\log n+O(n).
\]

Combining these exact source statements yields the unconditional target-domain relation

\[
\boxed{\lambda_n-S_\Lambda(n)=\frac n2\log n+O(n).}
\tag{R3.1}
\]

No prime-number-theorem heuristic or numerical fit is used in (R3.1).

### Voros: RH-false Li behavior is exponentially non-tempered

André Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis*, arXiv:`math/0506326v2` (25 Jan 2006), gives the asymptotic alternative (17)–(18). In the RH-true case,

\[
\lambda_n=\frac n2(\log n-1+\gamma-\log 2\pi)+o(n).
\]

In the RH-false case, the paper derives by a Darboux argument that off-critical zeros give contributions \(z_k^{-n}\) with \(|z_k|<1\); consequently \(\lambda_n\) oscillates between exponentially growing values of both signs. The paper explicitly labels the resulting dichotomy as an asymptotic criterion equivalent to RH.

Jeffrey C. Lagarias, *Li Coefficients for Automorphic L-Functions*, arXiv:`math/0404394v4`, is used only as an independent structural cross-check: it likewise records that when the relevant RH fails, the incomplete/finite-place Li term is sometimes of exponential size in \(n\). No term-by-term identification between Coffey's \(S_\Lambda\) and Lagarias's finite-place normalization is assumed.

## Candidate C-RH-ANA-003b-POLYNOMIAL-SLAMBDA-STRENGTH

Test the family

\[
\exists A,C,N_0\quad |S_\Lambda(n)|\le Cn^A\qquad(n\ge N_0).
\tag{R3.2}
\]

The purpose is **not** to prove (R3.2). The purpose is to classify whether (R3.2) is a strictly weaker intermediate target.

### Derived route lemma

Under Coffey's exact definition of \(S_\Lambda\),

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
S_\Lambda(n)\ \text{is polynomially bounded}.}
\tag{R3.3}
\]

**Proof.**

1. If RH holds, Voros gives \(\lambda_n=O(n\log n)\). Equation (R3.1) gives \(\lambda_n-S_\Lambda(n)=O(n\log n)\). Hence \(S_\Lambda(n)=O(n\log n)\), so it is polynomially bounded.

2. Conversely, suppose \(S_\Lambda(n)\) is polynomially bounded. Equation (R3.1) then makes \(\lambda_n\) polynomially bounded. If RH were false, Voros's rigorous Darboux alternative would force exponentially growing oscillatory subsequences of \(\lambda_n\), contradicting polynomial boundedness. Therefore RH holds. \(\square\)

This is a **composition of primary-source results and elementary growth comparison**, not a claim of a new RH theorem. It is used here to classify the research obligation. A bounded novelty search for the exact phrase/criterion did not find an exact prior statement, but that search is not exhaustive and supplies no novelty certificate.

A stronger-looking target such as \(S_\Lambda(n)=O(n\log n)\) is therefore also RH-strength: proving it unconditionally would already prove RH. The R3 cycle must not route toward such a global bound as though it were a subordinate lemma.

## Counterexample-first interpretation

The hostile world is simply the source-authorized `RH false` branch. In that branch, \(\lambda_n\) has exponential excursions, while the complement \(\lambda_n-S_\Lambda(n)\) is polynomial-size by (R3.1). Subtracting a polynomial-size term cannot erase an exponentially growing subsequence. Thus the full \(S_\Lambda\) remainder necessarily carries the root-sensitive exponential mode.

This resolves the R2 question "is \(S_\Lambda\) a genuinely prime-side signed component or merely a relabeling of the original obstruction?" in a precise sense:

- it **is** a genuine exact prime/Laguerre representation;
- but **global polynomial smallness of the entire component is not a weaker bridge**. The whole component still contains the root-sensitive mode.

## Same-context expert-cell synthesis

1. **Analytic-number-theory / explicit-formula lead:** accepted Coffey equations (14)–(17) and equation (10); verified that the only derived algebra is substitution and collection of \(O(n)\) terms.
2. **Li/Weil criterion specialist:** classified polynomial boundedness of full \(S_\Lambda\) as root-equivalent by (R3.3), so it cannot be assigned subordinate-lemma status.
3. **Prime-sum / Laguerre analyst:** rejected the label "small prime remainder" as a routing prior; the infinite Laguerre-weighted \([1-\Lambda(m)]\) sum is globally root-sensitive.
4. **Asymptotic complex-analysis specialist:** checked the polynomial/exponential separation; a polynomial complement cannot cancel Voros's RH-false exponential subsequence.
5. **Adversarial falsification specialist:** selected the RH-false branch itself as the strongest hostile control, eliminating the need for a toy sequence.
6. **Formal verification / provenance lead:** kept Coffey, Voros, and Lagarias statements separately bound; Lagarias remains a cross-check rather than an equality bridge.
7. **RAKL v3 metrology / novelty lead:** records a compositional/representation route result only, with zero independent-review credit and no root authority.

These are seven role-separated passes in one context. They are **not** seven independent reviews.

## Episode -> diagnosis -> obstruction/lesson

**Episode observation:** candidate `C-RH-ANA-003b-POLYNOMIAL-SLAMBDA-STRENGTH` was tested against the exact source decomposition and the RH-false asymptotic branch. Outcome: `PARTIAL_SUCCESS_ROUTE_PRUNING`.

**Diagnosis `D-RH-ANA-003b-TAME-COMPLEMENT-RETAINS-ROOT-MODE`:** subtracting the tame \(O(n\log n)\) complement from the Li sequence leaves a remainder that necessarily carries any RH-false exponential mode. Calling that remainder "prime-side" does not reduce logical strength.

**Obstruction `O-RH-ANA-003b-FULL-REMAINDER-ROOT-COUPLING`:** any proposed global two-sided polynomial bound on the *entire* Coffey \(S_\Lambda\) is already RH-equivalent and therefore cannot serve as a strictly weaker intermediate lemma.

**Candidate lesson `L-RH-ANA-003b-AUDIT-OBLIGATION-STRENGTH-BEFORE-BOUND`:** before proving a hard estimate on a residual obtained by subtracting a tame main term, test whether the residual still carries the full root-false asymptotic mode. This lesson remains proposal/shadow and has no reusable authority.

**Candidate motif `M-RH-ANA-ROOT-SENSITIVE-REMAINDER`:** `tame complement + root-sensitive global quantity => residual retains root-sensitive mode`.

## Failure separation

**Local representation/decomposition failure — `F-RH-ANA-003b-FULL-SLAMBDA-POLYNOMIAL-SMALLNESS-ROOT-COUPLED`:** the method target "prove a global polynomial bound for full \(S_\Lambda\) as a weaker prime-side lemma" is mis-scoped. The estimate itself is not false; it is RH-equivalent.

**Local-to-global/gluing failure — `F-RH-ANA-003b-PRIME-REMAINDER-AS-WEAKER-BRIDGE`:** gluing a hypothetical global polynomial \(S_\Lambda\) certificate into the Li identity closes the root-sensitive asymptotic alternative immediately; it cannot be credited as a local bridge independent of root closure.

No local mathematical theorem about a proper prime window, one-sided kernel contribution, mollifier, resonance form, or zero-density estimate is refuted here.

## Saturation / rotation

The following family is flattened for this representation:

- full-\(S_\Lambda\) two-sided polynomial smallness;
- full-\(S_\Lambda\) \(O(n\log n)\) smallness;
- PNT/partial-summation searches whose declared goal is only to obtain such a global bound.

The path reopens only after **strict decomposition** of \(S_\Lambda\) into proper source-bound subcomponents whose individual obligations do not already imply polynomial boundedness of the whole remainder.

## New residual

`RH-ANA-003c — LOCALIZED_ONE_SIDED_PRIME_DISCRIMINATOR`

> Construct a source-bound decomposition \(S_\Lambda(n)=\sum_j S_{\Lambda,j}(n)\) (for example by prime/logarithmic scale or a rigorously justified Laguerre-kernel partition), and identify the smallest one-sided or cancellation-preserving sub-obligation that is (i) strictly weaker than polynomial boundedness of the full \(S_\Lambda\), (ii) strong enough to change the Li lower-bound ledger after gluing, and (iii) accompanied by a DifferenceWitness against finite-prefix, zero-density-average, and absolute-majorant failures.

Before any candidate under RH-ANA-003c, freeze a new fibre and audit kernel partition convergence, \(n\)-uniformity, source/zero duality, and whether the proposed local condition secretly reconstructs the full RH-equivalent remainder.

**Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`.
