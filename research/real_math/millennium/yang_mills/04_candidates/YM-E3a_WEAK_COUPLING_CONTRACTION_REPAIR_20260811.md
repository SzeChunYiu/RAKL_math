# YM-E3a — weak-coupling contraction repair and coupled-domain audit

Authority: `PROPOSAL/SHADOW RESEARCH EVIDENCE ONLY`. This file grants no Yang–Mills theorem, no source repair beyond the elementary recurrence lemma below, no novelty authority, no independent-review credit, and no root authority.

## Frozen parent atom and chronology

Parent: RAKL_math issue #93 (`YM-E3a`), prospectively frozen before this cycle. Root: issue #5, state `OPEN_NO_SOLUTION_CERTIFICATE`.

Current framework was read directly from `SzeChunYiu/RAKL` `main` before mathematical work. Current observed framework subject for this cycle is `eeca4ea13ad7e2b2bc2fd4d7420ad05a81f654ca`, method `3.0.0`, package `0.1.0`, constitution epoch `v3-authority-hardening-20260811`. The application dependency pin on the cycle base remains older (`787c7e00af2a5877ccb715bc807ec14f52974e9c`) and is not silently rewritten; current-main v3 surfaces are used in proposal/shadow mode only.

The cycle-local fibre was not committed before the source observations below. Therefore the parent issue gives prospective *atom* binding, but this cycle claims no separate pre-action/preregistration credit for the particular source defects discovered during the audit. Negative chronology is preserved rather than backfilled.

## Exact primary-source surface

Primary manuscript: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 Jun 2026), 593-page PDF, https://arxiv.org/pdf/2606.19362 . Exact inspected selectors:

- main-text equations (5.6)–(5.12), Theorem 5.3, PDF pp. 574–575 in parsed indexing;
- equations (5.17)–(5.35), Theorems 5.4–5.7, PDF pp. 575–578;
- Section 10 equations (10.34)–(10.51), especially Theorem 10.4 and its proof, PDF pp. 115–120;
- Appendix A equations (A.34)–(A.60), especially Theorem A.9 and Lemma A.10, PDF pp. 588–592.

Visual verification succeeded for the Appendix pages containing (A.42)–(A.43) and (A.54)–(A.58). A screenshot request for the Section-10 page containing the end of the Theorem 10.4 proof returned a backend `Cache miss`; the parsed PDF text is available, but that page-level visual check is `CANNOT_CHECK`, not passed.

Secondary primary technical source inspected for the cited FRD support: D. C. Brydges, G. Guadagni, P. K. Mitter, *Finite Range Decomposition of Gaussian Processes*, arXiv:math-ph/0303013 / J. Stat. Phys. 115 (2004) 415–449. Its proved scope is finite-range decomposition of Gaussian-process covariances/resolvents. It is relevant to the covariance decomposition, but it does not by itself source-bind the manuscript's nonlinear four-dimensional non-Abelian polymer-RG contraction estimates.

Seiler's 1982 Lecture Notes in Physics 159 is cited by the manuscript but full technical text was not acquired in this cycle. Missing theorem-level detail is not reconstructed from memory.

## Local mathematical repair: `YM-E3a-C001`

The manuscript's Appendix A Lemma A.10 starts from

`x_{n+1} <= rho x_n + C x_n^2`, with `0 < rho < 1`, `C > 0`,

and closes its printed induction with the impossible positive-parameter condition `2 C r + C r^2 <= 0`. The parent issue #93 already records that defect.

A correct invariant-ball lemma is elementary:

**Lemma (invariant small ball).** Let `R > 0`, `0 < rho < 1`, `C > 0`. Suppose the recurrence estimate

`x_{n+1} <= rho x_n + C x_n^2`

is valid whenever `0 <= x_n <= R`. Choose `0 < r <= R` such that

`q := rho + C r < 1`.

Then every nonnegative trajectory with `x_0 <= r` obeys

`x_n <= q^n x_0 <= q^n r <= r`

for all `n >= 0`, and in particular `x_n -> 0` exponentially.

**Proof.** If `x_n <= r`, then

`x_{n+1} <= (rho + C x_n)x_n <= (rho + C r)x_n = q x_n`.

Starting from `x_0 <= r`, induction gives `x_n <= q^n x_0 <= r`; hence the hypothesis domain is self-propagating and the same estimate applies at every step. Since `q < 1`, exponential convergence follows. QED.

This solves only the deterministic recurrence subproblem. Its defensible RAKL novelty class is `compositional`: a standard invariant-region contraction argument applied to the frozen source recurrence. No literature novelty is claimed.

## Fresh source-proof diagnosis 1: the displayed floor does not imply decay

Theorem A.9 / equation (A.59) gives

`||Phi_{K+n}|| <= rho^n r + C r^2/(1-rho)`.

For fixed positive `C,r` the displayed right-hand side has positive limit `C r^2/(1-rho)`. The next paragraph nevertheless says that `||Phi_{K+n}|| -> 0 exponentially` and uses that to infer `g_R -> 0`. The displayed estimate alone cannot support that inference. The corrected invariant-ball lemma above can supply exponential decay **if** the actual source-specific RG recurrence is valid on a ball satisfying `rho + C r < 1`.

The same logical shape occurs in main-text Theorem 5.3: the displayed bound (5.7) includes a nonzero `O(||Phi_k||^2)` floor, while the text then says the trajectory tends to zero exponentially. Again, a separately closed invariant-domain estimate is needed; the local lemma supplies the deterministic form but not the source-specific constants or RG map.

Failure ID: `F-YM-E3A-DISPLAYED-FLOOR-NO-DECAY-INFERENCE` (`LOCAL_MATHEMATICAL/SOURCE_PROOF`, proposal/shadow).

## Fresh source-proof diagnosis 2: rectangular polydisc cannot yield the asserted beta domination

Section 10 is more structurally appropriate than Appendix A because it separates the marginal coupling `g_k` from the irrelevant polymer activity `K_k`. Theorem 10.4 states a remainder estimate of the form

`|R_k| <= c2 |g_k|^5 + c3 |g_k| ||K_k|| + c3 ||K_k||^2`  (10.41)

on a rectangular polydisc `|g| <= epsilon_*`, `||K|| <= delta_*`, with positive `epsilon_*`, `delta_*`. The proof then says the mixed and pure-irrelevant terms can be dominated by `(1/2) beta_0 g_k^3` throughout that polydisc, yielding (10.42).

That uniform implication is false for any positive rectangular radii on the displayed inequalities alone. Fix any `0 < kappa <= delta_*` and let `g -> 0`. Then `c3 kappa^2` stays positive while `(1/2) beta_0 |g|^3 -> 0`. Equivalently, even at `g=0` with nonzero `K`, the pure-irrelevant remainder allowed by (10.41) is positive while the proposed cubic budget is zero. The mixed term similarly requires `||K|| = O(g^2)` to be uniformly absorbable into a cubic decrement.

This does **not** refute the possibility of a valid weak-coupling stable manifold. It changes the required geometry: independent rectangular smallness is insufficient; a coupled domain such as

`||K|| <= A g^2`

(or a stronger source-derived relation) is needed before the cubic beta decrement can dominate the mixed remainder.

Failure ID: `F-YM-E3A-RECTANGULAR-POLYDISC-BETA-DOMINATION` (`LOCAL_MATHEMATICAL`).

Diagnosis ID: `DX-YM-E3A-WEDGE-REQUIRED`.

## Reusable obstruction candidate: constant compatibility for a coupled wedge

The manuscript's irrelevant-sector estimate has the shape

`||K'|| <= theta ||K|| + c1 g^2`, `0 < theta < 1`.

If a repair uses a wedge `||K|| <= A g^2`, then asymptotic invariance requires, at minimum and up to the small change from `g` to `g'`,

`theta A + c1 <~ A`, hence `A >~ c1/(1-theta)`.

For the mixed beta remainder `c3 |g| ||K||` to fit inside the manuscript's chosen half-beta budget `(beta_0/2)|g|^3`, one needs approximately

`c3 A < beta_0/2`.

Thus a source-valid wedge repair needs a nonempty compatibility window, schematically

`c1/(1-theta) < A < beta_0/(2 c3)`,

plus control of the `K^2` and `g^5` terms and proof that the full RG map preserves the wedge. The inspected source text supplies positive constants but no bound establishing this compatibility window. This is the smallest new source-facing discriminator.

Obstruction ID: `O-YM-E3A-WEDGE-CONSTANT-COMPATIBILITY` (`PROPOSAL/SHADOW`; not promoted as a universal RAKL lesson).

This obstruction is analogous to RAKL_math #73's relative defect-budget pattern: absolute smallness is insufficient unless the defect fits inside the *available margin*. DifferenceWitness: #73 concerns lattice spectral-gap transport; here the budget is the cubic asymptotic-freedom decrement and an invariant two-coordinate RG domain.

## Source-family / representation / gluing audit

The main text's Section 10 decomposition `(g,K)` avoids conflating a marginal coupling with a strictly irrelevant sector. The appendix and Theorem 5.3 use a coarser one-norm contraction presentation. For any repaired route, the application must bind which representation is authoritative, prove the transition between `Phi` and `(g,K)`, and show that the repaired weak trajectory is the *same theory/subsequence* used by the OS reconstruction and universality claims. Local recurrence decay is not by itself a continuum existence theorem, OS reconstruction theorem, universality theorem, or mass-gap theorem.

The manuscript also defines an operational renormalized coupling in (5.33) and asserts a two-sided relation to the polymer norm in (5.34). That relation was noted rather than discarded: it prevents a false claim that the source contains no `Phi -> g_R` bridge. Its theorem-level source proof remains part of downstream verification.

## Same-context expert cell

Seven role-separated passes were used, all sharing the same evidence context and therefore receiving **zero independent-review credit**:

1. Constructive RG/polymer norms — checked recurrence domains, irrelevant-sector contraction, and invariant-region geometry.
2. Asymptotic freedom/RG dynamics — checked marginal coupling scaling, cubic decrement, and coupled-domain requirements.
3. Constructive QFT/OS — kept local weak-RG repair separate from continuum measure, OS reconstruction, and mass-gap promotion.
4. Gauge-theory representation — checked the distinction between `Phi`, `(g,K)`, and operational `g_R`.
5. Adversarial mathematics — supplied the `g -> 0`, fixed-nonzero-`K` hostile witness and checked the invariant-ball proof.
6. Formal/provenance assurance — preserved exact selectors, missing-source boundaries, screenshot failure, and chronology.
7. RAKL v3 metrology — separated episode, diagnosis, failure and obstruction; audited saturation/novelty and authority gates.

Consensus: `YM-E3a-C001` is a valid local deterministic repair; the source-level asymptotic-freedom route remains blocked at the coupled-domain/constant-compatibility interface and at primary theorem source-binding. Same-context consensus is not independent review.

## Outcome and next action

Outcome: `PARTIAL_LOCAL_REPAIR_PLUS_NEW_SOURCE_ROUTE_OBSTRUCTION`.

Residual before: invalid Appendix A.10 induction; unbound invariant domain; source-specific propagation to AF/universality unresolved.

Residual after: recurrence subproblem closed under explicit `rho + C r < 1`; source route sharpened to (i) establish a coupled stable wedge or equivalent invariant relation between `K` and `g`, (ii) prove a compatible constant window for `theta,c1,c3,beta_0`, (iii) bind those constants to the actual non-Abelian FRD/polymer map from primary mathematical sources, (iv) repair/verify bare-coupling entry without circularity, and (v) glue the resulting trajectory to the same continuum OS theory. The perturbative beta coefficient remains separate unless its rigorous nonperturbative remainder control is source-bound.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical reviews = `0`. No root/gate/proof-DAG/verifier/axiom/isolated-review promotion is attempted.
