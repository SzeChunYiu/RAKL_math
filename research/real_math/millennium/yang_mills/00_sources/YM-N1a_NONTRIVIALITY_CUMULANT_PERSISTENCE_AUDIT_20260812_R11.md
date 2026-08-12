# YM-N1a R11 — nontriviality / cumulant-persistence source audit

**Authority:** proposal/shadow source audit only. No theorem, root promotion, protected lesson/obstruction, or independent-review credit.

**Root:** #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Child:** #205 (`YM-N1a-NONTRIVIALITY-CUMULANT-PERSISTENCE-OBSERVABLE-NORMALIZATION-SAME-CONTINUUM-SOURCE`)  
**Primary source:** Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1.

## Chronology boundary

The two load-bearing source inconsistencies below were noticed before the durable R11 fibre was written. They are preserved as retrospective source observations and receive zero strict prospective-discovery credit. After the fibre freeze, only the registered pre-candidate action was executed: a bounded search of the same primary source for an explicit observable/source-renormalization or alternative nontriviality theorem. Current RAKL semantic-shortcut routing remained `CANNOT_CHECK`, so no new repair candidate was generated.

## Observation A — Theorem 10.4 cannot obtain its stated beta-uniform positive floor from the displayed expansion

Theorem 10.4, page 75, states that there exist `beta_0>0` and `c_*>0`, depending only on `N` and `chi_sigma`, such that for **all** `0<beta<=beta_0` and all scales `k`,

`|kappa_4^(k)(x1,x2,x3,x4)| >= c_*`,

uniformly in spatial volume. Its proof then identifies the leading nonvanishing connected surface weight as `A_N beta^6`; all other connected contributions are `O(beta^7)`. On page 76 it sets

`c_* := (1/2) A_N beta_0^6 > 0`

and asserts the same lower bound for `0<beta<=beta_0`.

This uniformization has the wrong beta dependence. The displayed leading term tends to zero as `beta -> 0`. A lower bound of order `beta^6` can yield, after a sufficiently small-beta remainder estimate, a statement of the schematic form `|kappa_4(beta)| >= c beta^6` for each beta in a small interval; it cannot yield a beta-independent strictly positive floor over the punctured interval `(0,beta_0]` without additional structure. In particular, the source's chosen `c_*=(1/2)A_N beta_0^6` does not follow for beta smaller than beta_0.

**Scoped conclusion:** Theorem 10.4's displayed proof does not establish the stated beta-uniform positive cumulant floor. Since the proof immediately uses that floor to pass non-Gaussianity to a continuum subsequence, the nontriviality interface needs a corrected coupling quantifier and observable/trajectory binding. This is not an impossibility result for continuum nontriviality.

## Observation B — Theorem 10.5 drops the geometric decay of the initial cumulant

Theorem 10.5, pages 76–77, assumes a one-step RG Lipschitz constant `rho<1`, a nonzero initial fourth cumulant, and summable reblocking errors. It states equation (10.26)

`a_k >= c_0 rho^(k-k0) - sum_{j=k0}^{k-1} rho^(k-1-j) delta_j`

and then says "hence" `liminf a_k >= c_0 - sum delta_j > 0`.

The proof makes the recurrence explicit. It writes the source generator normal form

`E_{k+1}(t)=E_k(s_k t)+r_k(t)`, `(10.28)`

then differentiates four times to obtain

`kappa_4^(k+1)=s_k^4 kappa_4^(k)+eta_k`, `|eta_k|<=delta_k`, `(10.31)`

sets `rho := inf s_k^4`, and derives

`a_{k+1} >= rho a_k-delta_k`, `(10.33)`

followed by the geometric iteration `(10.34)`. If `rho<1`, the initial positive term `rho^(k-k0)a_k0` tends to zero. Summability of `delta` does not restore the missing `c_0`; equation (10.35)'s positive floor is therefore not a consequence of (10.34). The simplest zero-error specialization with constant `s in (0,1)` gives exact decay `kappa_{k+1}=s^4 kappa_k` and hence a vanishing cumulant.

**Scoped conclusion:** Theorem 10.5 as displayed needs an additional normalization/persistence hypothesis—for example a source-defined renormalized observable coordinate with an exactly controlled accumulated self-overlap—or a different nontriviality theorem. The current source text does not close this through equations (10.28)–(10.35).

## Prospective same-source repair search

The post-freeze bounded search found one potentially relevant coordinate elsewhere in the same source. On page 23 of a later internal part, the source restricts to a finite generating set of gauge-invariant local observables and, when derivatives occur, introduces a multiplicative normalization

`O_k^ren := Z_O(k) O_k`, `(3.61)`

with `Z_O(k)` chosen so that a **uniform second-moment upper bound** holds. The text says existence follows from scale-uniform locality/clustering and FRD, with a pointer to Appendix E.

That occurrence does not yet repair either nontriviality theorem:

- a second-moment upper bound does not imply a nonzero fourth-cumulant lower bound;
- a full-text search found no second occurrence of `Z_O(k)` / `O_k^ren` that binds it to Theorem 10.5's `s_k` product or to Theorem 10.4's beta dependence;
- the inspected Appendix E is titled **OS Limits, Spectral Measures, and Tauberian Gap** and begins with the OS quotient/semigroup construction; on the bounded inspected surface it does not provide an explicit theorem establishing the required `Z_O(k)` fourth-cumulant persistence or source-coordinate pushforward.

Thus the normalization is a **possible repair coordinate**, not a source-bound repair.

## Same-theory gluing obligations

A valid repair must not stop at a lattice recurrence. It must bind one fixed physical, gauge-invariant continuum observable to a lattice family, including any multiplicative/mixing renormalization; prove a nonzero connected cumulant for that family with constants uniform in volume, lattice spacing, regulator and relevant RG range; pass that cumulant on the same continuum subsequence; and show the limiting observable belongs to the same gauge-invariant OS source algebra/quotient used to reconstruct the continuum state. Strong-coupling plaquette variables, derivative-renormalized fields, and fixed-physical smeared observables are not interchangeable without an explicit typed map.

## Expert-cell disposition

1. **Constructive QFT / OS reconstruction:** blocks the continuum inference until the nonzero cumulant is attached to the same OS source family and subsequence.
2. **Rigorous RG / polymer expansion:** separates cluster-expansion positivity from observable normalization under repeated blocking; a contractive self-overlap is not persistence.
3. **Lattice gauge theory:** flags the coupling quantifier in Theorem 10.4; a `beta^6` leading term cannot support a beta-independent floor down to beta zero.
4. **Functional analysis / recurrence audit:** rejects the passage from (10.34) to (10.35) under `rho<1` without extra structure.
5. **Formal proof / quantifier audit:** keeps beta, scale, volume, lattice spacing, regulator and subsequence quantifiers separate.
6. **Adversarial source / RAKL assurance:** classifies both findings as scoped source-proof/normalization failures and keeps root authority at none.

These are same-context roles, not isolated mathematical review.

## Residual

`RES-YM-N1a-FIXED-PHYSICAL-RENORMALIZED-OBSERVABLE-NONZERO-CONTINUUM-CUMULANT-SAME-OS-SOURCE`

The next admissible action is source acquisition/binding under issue #205. Missing primary mathematical detail remains `BLOCKED/UNKNOWN`; do not reconstruct a composite-operator renormalization theorem from memory.
