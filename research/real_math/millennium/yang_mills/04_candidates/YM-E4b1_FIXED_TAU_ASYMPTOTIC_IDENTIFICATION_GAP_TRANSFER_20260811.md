# YM-E4b1 — fixed-physical-time gap transfer without exact cross-cutoff isometries

**Parent:** `YM-E4b`, RAKL_math issue #126  
**Atom signature:** `YM-E4b1-FIXED-TAU-ASYMPTOTIC-IDENTIFICATION-GAP-TRANSFER`  
**Framework:** current `SzeChunYiu/RAKL@38a530a52d863513db16052474b85e63fbb488cd`, RAKL v3 architecture, package `0.1.0`  
**Frozen fibre:** `sha256:302f373474803e0c01ff66d94f89d3652d9545b89c22118c25eda9d7c74e31a3`  
**Chronology:** `RETROSPECTIVE_ONLY / PROPOSAL_SHADOW`; internal derivation began before a durable current-v3 pre-action receipt, so this result receives no strict prospective-discovery credit.  
**Authority:** `LOCAL_ABSTRACT_LEMMA_PROPOSAL / SAME_CONTEXT_VERIFICATION_ONLY / NO_SOURCE_REPAIR_CERTIFICATE / NO_CONTINUUM_YM_THEOREM / ROOT_AUTHORITY_NONE`.

## 1. Why this is the smallest useful child

The predecessor `YM-E4b` episode isolated a regulator-to-continuum gluing failure: the audited 2026 route moves from asymptotic inner-product control to exact cross-cutoff Hilbert-space isometries and then to strong semigroup/resolvent conclusions. The stored `YM-E2b` issue #92 separately warns that transfer gaps must be tracked in a fixed physical-time normalization rather than silently mixing a changing lattice time step with a physical Hamiltonian gap.

This child therefore asks only a sufficient-condition question. It does **not** attempt to prove that the Faizal–Shabir construction satisfies the conditions. The point is to determine whether exact regulator-to-continuum isometries are mathematically necessary for gap transport, or whether a weaker asymptotic comparison structure would suffice once a genuine strong semigroup intertwining estimate is proved.

The answer below is yes: exact isometries are unnecessary for this abstract step. The hard source-facing residual moves to proving asymptotic Hilbert comparison, vacuum compatibility, strong fixed-`tau` intertwining and a regulator/volume-uniform physical contraction bound in one and the same OS theory.

## 2. Fixed-`tau` asymptotic-identification gap-transfer lemma

Let `H` and `H_n` be Hilbert spaces. Let `J_n : H -> H_n` be bounded linear comparison maps satisfying, for every `u,v in H`,

`<J_n u, J_n v>_{H_n} -> <u,v>_H`.  (AI)

Let `Omega in H` and `Omega_n in H_n` be unit vectors such that

`||J_n Omega - Omega_n|| -> 0`.  (VAC)

Let `A >= 0` and `A_n >= 0` be self-adjoint operators with

`A Omega = 0`,  `A_n Omega_n = 0`,

and define the contraction semigroups

`T(t)=exp(-t A)`,  `T_n(t)=exp(-t A_n)`.

Fix one **physical** time `tau>0`. Assume strong comparison at that time:

`||T_n(tau) J_n u - J_n T(tau) u|| -> 0` for every `u in H`.  (INT)

Write

`P=|Omega><Omega|`, `Q=I-P`, `P_n=|Omega_n><Omega_n|`, `Q_n=I-P_n`.

Assume a uniform vacuum-orthogonal contraction bound in the same physical time coordinate:

`||T_n(tau) Q_n|| <= exp(-m tau)`  for all `n`, with one `m>0`.  (UGAP)

Then

`||T(tau) Q|| <= exp(-m tau)`,

and therefore

`sigma(A | QH) subset [m, infinity)`.

In particular, the continuum operator has no additional zero-energy state in `QH` and no spectrum in `(0,m)`.

### Proof

First show that the vacuum projections are compatible with the asymptotic comparison maps. For fixed `u in H`, set

`a_n=<Omega_n,J_n u>`.

By `(VAC)`, convergence of `||J_n u||`, and `(AI)`,

`|a_n-<Omega,u>|`

is bounded by

`||Omega_n-J_n Omega|| ||J_n u|| + |<J_n Omega,J_n u>-<Omega,u>| -> 0`.

Hence

`Q_n J_n u - J_n Q u`

`= <Omega,u> J_n Omega - a_n Omega_n`,

so

`||Q_n J_n u - J_n Q u|| -> 0`.  (PROJ)

Now use contraction of `T_n(tau)`, `(PROJ)`, and `(INT)` applied to `Qu`:

`||T_n(tau) Q_n J_n u - J_n T(tau) Q u||`

is at most

`||Q_n J_n u-J_n Q u||`

`+ ||T_n(tau)J_n Q u-J_n T(tau)Q u|| -> 0`.

By `(AI)`, `||J_n w|| -> ||w||` for every fixed `w in H`. Therefore

`||T(tau)Q u||`

`= lim_n ||T_n(tau) Q_n J_n u||`

`<= exp(-m tau) lim_n ||Q_n J_n u||`

`= exp(-m tau) ||Q u||`.

Taking the supremum over `u` proves

`||T(tau)Q|| <= exp(-m tau)`.

Because `Omega` is a zero-energy eigenvector of the self-adjoint `A`, `P` and `Q` reduce `A`, and on `QH`

`T(tau)=exp(-tau A)`.

The spectral theorem gives

`||exp(-tau A)|_{QH}|| = exp(-tau inf sigma(A|QH))`.

The preceding norm bound therefore forces

`inf sigma(A|QH) >= m`,

which is the claimed spectral exclusion. `QED`.

## 3. Dense-core variant and its boundary

If `(INT)` is known only on a dense set `D subset H`, it extends to all `H` provided the `J_n` are defined on all of `H` with one uniform operator bound `sup_n ||J_n||<infinity`. Indeed, approximate `u` by `d in D` and use contraction of both semigroups:

`||T_n(tau)J_nu-J_nT(tau)u||`

`<= 2 sup_n||J_n|| ||u-d|| + ||T_n(tau)J_nd-J_nT(tau)d||`.

This does **not** repair a source in which the comparison maps are only algebraically defined on a dense source domain and have not been shown closable/extendible with a regulator-uniform bound. Establishing that extension is precisely a remaining Hilbert-space gluing obligation.

## 4. What the lemma does and does not remove

The lemma removes one unnecessary requirement at the abstract operator level: **exact isometric identifications `H -> H_n` are not needed**. Pointwise asymptotic preservation of inner products, convergence of the vacuum vector, and genuine strong semigroup intertwining at one fixed physical time are enough to transport a uniform gap bound.

It does **not** derive `(AI)`, `(VAC)`, `(INT)` or `(UGAP)` from Euclidean covariance, clustering, weak matrix-element convergence, RG summability, or matching source labels. Those implications require separate proofs in the exact regulator-dependent OS quotient spaces. In particular:

- weak matrix-element convergence cannot replace `(INT)`;
- a source-family estimate cannot replace the full `Q_n` operator bound unless density/common-rate hypotheses are separately proved and bound to the same theory (`#109`, PR `#62`);
- a fixed-cutoff or strong-coupling gap does not give `(UGAP)` along a continuum path without volume/regulator and physical-unit uniformity;
- `tau` is a fixed physical time. Replacing it silently by a changing lattice spacing `a_n` changes the statement and reopens the normalization problem in `#92`;
- the maps `J_n` must compare the **same physical continuum theory** with its regulators. The lemma does not identify that theory or prove gauge/null-space compatibility.

## 5. Counterexample-first falsification

The same-context adversarial cell tested the hypotheses by deletion.

1. **Weak instead of strong intertwining.** Uniformly bounded positive self-adjoint operators can converge weakly without strongly converging. The predecessor `YM-E4b` rank-one hostile control therefore still blocks any attempt to weaken `(INT)` to matrix elements alone.
2. **No uniform physical gap.** Take a fixed two-dimensional space with `A_n=diag(0,1/n)` and `J_n=I`. Then `T_n(t)` converges strongly to the identity semigroup, every finite `n` has a positive gap, but no common `m>0` satisfies `(UGAP)`; the limiting gap is zero.
3. **No vacuum compatibility.** Without `(VAC)`, the projections `Q_n` need not approximate the continuum vacuum complement, so a contraction estimate can be imposed on the wrong sector.
4. **Source-restricted control.** A low-energy state orthogonal to the controlled source family survives exactly as in `F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE`; source decay alone does not imply `(UGAP)` on all of `Q_nH_n`.
5. **Changing time coordinate.** A bound written for `T_n(a_n)` cannot be interpreted as the fixed-`tau` hypothesis without the exact relation between `a_n`, physical time and `A_n`. The root invariant `E=-a^{-1}log(lambda)` remains binding.
6. **Wrong continuum identification.** Even perfect operator convergence under comparison maps to a different quotient/subsequence/theory does not close the Yang–Mills root. Same-theory OS and gauge compatibility are separate gluing data.

All controls are analytic/calibration checks; no numerical experiment is used as proof.

## 6. Same-context expert-cell verdicts

These are role-separated passes sharing one context and do not count as independent review.

- **Constructive QFT / OS:** accepts the abstract use of contraction semigroups; no exact OS isometry is assumed. Blocks source application until the regulator-dependent OS quotient maps and vacuum are actually constructed.
- **Functional analysis / spectral convergence:** accepts `(PROJ)` and the fixed-`tau` norm passage under `(AI)+(VAC)+(INT)`. Emphasizes that `(INT)` is the load-bearing strong convergence hypothesis and is not implied by weak matrix elements.
- **Lattice gauge spectral:** accepts the spectral conclusion only in a fixed physical-time normalization; selects #92 as directly relevant prior experience.
- **RG / continuum:** blocks gluing because no uniform-in-volume/regulator proof of `(UGAP)` along the continuum trajectory is established here.
- **Adversarial verification:** deletion tests above confirm that the main hypotheses are logically load-bearing and keep source completeness and vacuum-sector identification separate.
- **RAKL v3 assurance / metrology:** classifies the solved abstract subproblem as `RAKL_TRIVIAL` (compositional use of asymptotic inner-product control, semigroup contraction and spectral calculus); no lesson, operator, motif, theorem promotion or root authority is minted.

## 7. Local success versus gluing failure

**Local mathematical outcome:** `PARTIAL_SUCCESS`. The abstract sufficient-condition lemma is proved in the frozen context and removes exact cross-cutoff isometry from the list of logically necessary assumptions for this substep.

**Local-to-global/gluing outcome:** `BLOCKED`. The source-facing application still must prove, in one same-theory OS family:

1. a typed regulator-to-continuum comparison map with `(AI)` on a domain sufficient for completion;
2. `(VAC)` for the physical vacuum sector;
3. strong fixed-`tau` semigroup intertwining `(INT)`, or a source-valid theorem implying it in the varying-Hilbert setting;
4. a volume/regulator-uniform physical contraction `(UGAP)` with one `m>0`;
5. compatibility with gauge-invariant null quotients and the separate source-family completeness obligation;
6. continuum existence, nontriviality, ultraviolet/asymptotic-freedom and all remaining root obligations.

The residual is therefore narrower but still root-critical.

## 8. Source boundary and current primary literature

Current primary sources were checked at the claim/structural level before retaining this cycle:

- Faizal–Shabir, arXiv:`2606.19362`, submitted 9 June 2026, currently states a reflection-positive SU(N) construction with a transfer operator, uniform gap, RG transport, continuum clustering and OS reconstruction. This cycle does not treat the abstract as proof and does not re-use prior un-screenshotted PDF parsing as fresh theorem verification.
- Osterwalder–Seiler, *Annals of Physics* 110 (1978), DOI `10.1016/0003-4916(78)90039-8`, gives the primary lattice structural benchmark: physical positivity for lattice Schwinger functions implies a positive self-adjoint transfer matrix and their strong-coupling result is an infinite-volume lattice result, not the 4D continuum root.
- Kuwae–Shioya, *Communications in Analysis and Geometry* 11 (2003), DOI `10.4310/CAG.2003.v11.n4.a1`, is retained only as a varying-Hilbert representation analogue. No theorem from it is invoked in the proof above.

## 9. Root disposition and next discriminator

`RAKL_math#5` remains `OPEN_NO_SOLUTION_CERTIFICATE`.

The next high-information discriminator is source-specific and should be prospectively receipt-bound **before** execution: determine whether the actual regulated OS source maps in the 2026 construction can be upgraded, without exact isometries, to a uniformly bounded comparison family satisfying `(AI)+(VAC)` and fixed-`tau` strong semigroup intertwining `(INT)` on a dense core; if not, isolate the first exact missing estimate rather than replacing it by a same-space theorem.