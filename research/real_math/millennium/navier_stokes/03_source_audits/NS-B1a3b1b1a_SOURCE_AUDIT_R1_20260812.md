# NS-B1a3b1b1a source audit — Barker finite terminal singular points versus critical finite-center vorticity morphology

**Authority:** source-bound proposal/shadow transfer audit only. No theorem/root promotion; independent mathematical review credit `0/3`.

## Frozen target

Issue #180 froze the discriminator before this source-proof inspection. The source side is Tobias Barker, *Higher integrability and the number of singular points for the Navier-Stokes equations with a scale-invariant bound*, arXiv:2111.14776v2. The target side is the finite-center version of the morphology coordinate registered in issue #153 and motivated by Zoran Grujić, arXiv:2607.08866v2: on preterminal slices and for large vorticity level `lambda`, cover the vorticity super-level set by a fixed finite number of balls with `R_lambda <= C lambda^{-1/2}`. The separate global weak-`L^{3/2}` vorticity-amplitude and logarithmic-BMO direction assumptions remain separate consumer inputs.

## Exact Barker source theorem

Barker Theorem 2 considers a weak Leray-Hopf solution on `R^3 x (-1,infinity)` that first blows up at `t=0`. If there is a sequence `s_n ↑ 0` with `sup_n ||v(.,s_n)||_{L^{3,infinity}} = M < infinity`, the terminal singular set

`Sigma = {x : (x,0) is a singular point}`

has at most `C_univ M^20` elements. This is a terminal singular-set **cardinality** theorem in a global velocity-critical state space.

## Proof-interface inspection

The proof of Theorem 2 fixes an arbitrary finite subset `{x_1,...,x_L}` of the terminal singular set. It then chooses a backward time `s_n` late enough that the distinct terminal points are separated by at least `2 sqrt(-s_n)`. With `lambda_scale = sqrt(-s_n)`, Barker performs the exact Navier-Stokes rescaling and obtains a global countably additive spacetime bound for the rescaled velocity/pressure from the `L^{3,infinity}` slice assumption and Lemma 1. The rescaled terminal singular points have pairwise disjoint unit balls. Proposition 3 (CKN epsilon-regularity) forces a fixed positive spacetime mass in each such unit ball, and countable additivity bounds the number of balls, hence `L <= C M^20`.

The decisive observation for the frozen transfer test is that the proof scale is chosen from **backward time and pairwise separation of already selected terminal singular points**. The proof does not introduce a vorticity threshold `lambda_vort`, does not estimate `dist(A_lambda_vort(t), Sigma)`, and does not derive a level-dependent radius law `R_lambda_vort = O(lambda_vort^{-1/2})` on preterminal slices. CKN epsilon-regularity is used here as a lower spacetime-mass certificate at each terminal singular point after rescaling, not as a quantitative high-vorticity morphology theorem.

Barker also states explicitly that this proof does not use backward uniqueness, unique continuation, or quantitative Carleman inequalities. Pressure remains load-bearing in the countably additive spacetime bound and epsilon-regularity input.

## Transfer verdict

`SCOPED_TRANSFER_REJECTED / CARDINALITY_DOES_NOT_SUPPLY_CRITICAL_RADIUS_MODULUS`.

The source theorem supplies one useful target coordinate under stronger/different hypotheses: a finite upper bound on the number of **terminal singular points**. In the inspected theorem/proof, it does **not** supply the quantitative preterminal vorticity-superlevel morphology needed by the frozen target. In particular, the following inference is not licensed by the source:

`#Sigma <= N0  ==>  A_lambda(t) subset union_{j<=N0} B(x_j(t), C lambda^{-1/2})`.

This is a transfer/interface result about what the cited theorem proves; it is not an impossibility theorem saying no NSE argument can ever derive such a cover.

## Separate unresolved interfaces

1. **Terminal-to-preterminal gluing.** A finite terminal singular set is not yet a controlled family of preterminal high-vorticity centers with a quantitative radius law.
2. **Far-field/global super-level gluing.** Pointwise regularity away from finitely many terminal singular points does not, without an additional uniform tail argument, provide a global high-vorticity super-level cover on the noncompact whole space.
3. **Velocity-to-vorticity state transfer.** Barker's backward-sequence `L^{3,infinity}` velocity hypothesis/conclusion does not itself provide the target global weak-`L^{3/2}` vorticity amplitude or logarithmic-BMO direction control.
4. **Pressure/local-energy interface.** Pressure and spacetime integrability are used in the source counting proof; they cannot be silently discarded when attempting producer-side transfer.
5. **Limit/state-space interface.** This audit uses the source theorem directly and proves no transport of its conclusion through an Albritton-Barker ancient-limit passage. Weak/strong convergence and source-family compatibility remain separate.
6. **Backward uniqueness.** Not invoked by the audited Barker proof and not available as a repair unless its exact terminal/exterior hypotheses are separately produced.
7. **Type II.** Untouched.

## DifferenceWitness

The source and target share finite exceptional spatial centers and critical NSE scaling, but differ in the load-bearing coordinate: Barker controls terminal **cardinality**, whereas the target requires a preterminal **quantitative level-to-distance modulus** with exponent `1/2` for vorticity. That difference is precisely the old-failure regression forced by prior RAKL local-to-global/morphology experience.

## Source anchors

- Tobias Barker, arXiv:2111.14776v2: Theorem 2; Section 4, Proposition 3, Lemma 1, proof of Theorem 2, equations (62)–(70); Introduction discussion of proof ingredients/non-use of backward uniqueness.
- Zoran Grujić, arXiv:2607.08866v2: Definition 2.1; Theorem 4.1 and the localized stretching/absorption step associated with the critical `R <= C lambda^{-1/2}` morphology.
- RAKL_math issue #180: prospectively frozen success/failure contract and discriminator.

No numerical computation is used as mathematical proof.
