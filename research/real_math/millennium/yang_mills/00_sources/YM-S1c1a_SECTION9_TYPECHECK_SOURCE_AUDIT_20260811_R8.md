# YM-S1c1a R8 — Section 9 universality applicability type-check

**Cycle:** `YM-S1c1a-SECTION9-TYPECHECK-20260811-R8`  
**Root:** RAKL_math #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Parent:** #69; **active repair atom:** #166 / `YM-S1c1a`  
**Authority:** `PROPOSAL_SHADOW / PRIMARY_SOURCE_APPLICABILITY_AUDIT / SAME_CONTEXT_REVIEW_ONLY / NO_THEOREM / NO_ROOT_AUTHORITY`

## Frozen discriminator

R7 left one narrow repair possibility before inventing a new AF/IR comparison: determine whether Section 9 Theorems 9.3/9.4 already provide a type-correct, same-theory vanishing comparison for the two Section-10 trajectories. The discriminator is not “does the paper say universality?” but whether the exact Section-9 hypotheses are mapped to the AF and IR objects used in Theorem 10.8.

Primary source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1, 9 June 2026. Selectors below refer to the arXiv v1 PDF.

## What Section 9 actually types

At pp. 95–96, Section 9 states its object as a fixed admissible class of lattice regularizations and reflection-positive blockings. It then explicitly defines an admissible regulator by two ingredients:

- `Π_α = f_α(D)`, with `α` describing the slice-projector profile;
- `B_β`, a reflection-positive finite-range block map, with `β` parametrizing the blocking.

See §9, around (9.1), pp. 95–96.

The admissible metric is not merely a declaration of finite distance. Equation (9.3) requires an explicit scale-decaying response

`||Π_α-Π_α'|| <= L_0 a_k d(α,α')`,
`||B_β-B_β'|| <= L_0 a_k d(β,β')`.

Theorem 9.1 propagates this to the one-step OS kernels, again with an explicit `a_k` factor; see (9.6), pp. 96–98.

Theorem 9.3 then compares two admissible **scheme pairs** `(α,β)` and `(α',β')` and obtains

`|S_k^(α,β)-S_k^(α',β')| <= C sum_{ell>=k} a_ell [d(α,α')+d(β,beta')]`.

Since `a_ell=a_0 b^(-ell)`, this tail tends to zero. The vanishing is therefore carried by the `a_ell` modulus, not by finite parameter distance alone. See Theorem 9.3 and (9.28), pp. 101–103.

Theorem 9.4 is conditional in a different way. At a fixed scale, equality of the OS path measures follows when the one-slice marginals and kernels agree (`rho_k=tilde rho_k`, `K_k=tilde K_k` on a core). In the continuum formulation, uniqueness is determined by a common limiting pair `(rho,T)`. The proof later says scheme-independence follows because the limit `rho` and limiting semigroup `T` are independent of `(α,β)` **by hypothesis**. See Theorem 9.4, pp. 104–106, especially the discussion around (9.40)–(9.42).

Thus Markov uniqueness propagates equality once the one-slice state/semigroup data have been identified; it does not itself create that identification.

## What Section 10 changes

Section 10 separately parameterizes the running effective theory by `(g_k,K_k)`, where `g_k` is the scale-dependent gauge coupling and `K_k` the irrelevant polymer activity; see (10.3)–(10.6), pp. 109–110.

Theorem 10.8 then compares an AF continuum family and an IR-transported family on a common sequence of lattices and common hyperplane geometry. It asserts both sequences are admissible and invokes a single-scale Lipschitz property for two one-slice data sets denoted `α,α'`, saying their distance is finite in the FRD metric and the constant is controlled up to the scaling factor `a_k`; see (10.77)–(10.79), p. 127.

This is the exact type boundary. Section 10's notation could be intended to broaden the Section-9 admissible metric from regulator/block parameters to generic one-slice effective data. However, on the inspected source surface there is no displayed field-by-field map

`AF trajectory (g_k,K_k, regulator data) -> Section-9 admissible coordinate`,
`IR trajectory (g_k,K_k, regulator data) -> Section-9 admissible coordinate`

together with verification of the same metric assumptions and the crucial `O(a_k)` modulus uniformly in `k`.

That absence is an **under-typed applicability interface**, not a proof that no such map can exist.

## Why the Section-9 theorem is not yet a repair certificate

Three logically distinct routes would repair the interface:

1. **Typed Section-9 embedding.** Extend or instantiate the admissible coordinate space so both AF and IR trajectories lie in it, and prove the Section-9 single-scale `O(a_k)` response uniformly along the two paths.
2. **Direct vanishing inter-trajectory estimate.** Prove a same-theory estimate such as
   `|S_AF,k-S_IR,k| <= C sum_{ell>=k} a_ell d_ell`
   with a uniformly bounded `d_ell`, or another source-valid tail tending to zero.
3. **Independent common-limit data.** Prove that the two one-slice marginals and semigroups converge to the same `(rho,T)` and only then invoke Theorem 9.4.

The displayed Theorem-10.8 recursion from R7,
`D_(k+1) <= D_k + C epsilon_k`, `sum epsilon_k < infinity`,
does none of these by itself. Equations (10.80)–(10.81), p. 128, yield bounded cumulative drift; the subsequent statement that a finite initial Lipschitz distance can be absorbed into a summable error does not provide a vanishing right-hand side.

## Counterexample-first controls

- **Finite distance is not a vanishing modulus.** If `d_k=1`, a bound of order `C d_k` stays `O(1)`. Theorem 9.3 succeeds because the source supplies the extra `a_k` factor.
- **Conditional Markov uniqueness is not an identification theorem.** Two stationary Markov systems can satisfy positivity/locality/Markov structure while having different invariant marginals or transition kernels. Theorem 9.4 explicitly requires equality/common limiting data.
- **R7 recurrence control remains active.** `D_k=1`, `epsilon_k=0` satisfies `D_(k+1)<=D_k+C epsilon_k` and summability but does not tend to zero.

These controls falsify inference forms only. They are not Yang–Mills counterexamples.

## Same-context expert cell

Six role-separated passes were used: lattice gauge/rigorous RG; constructive QFT/OS; dynamical systems/asymptotics; adversarial falsification; formal methods/provenance; novelty/source history. Consensus: the source presently lacks a **typed applicability witness** from the AF/IR trajectory coordinates to the Section-9 universality coordinates, but the notation in Section 10 is broad enough that the correct classification is `MISSING_TYPED_APPLICABILITY_WITNESS`, not categorical inapplicability. Same-context review earns zero independent-review credit.

## Local versus gluing result

Local source extraction of the Section-9 and Section-10 statements succeeded. The failure is at the local-to-global interface: the theorem hypotheses for regulator universality have not been shown to bind the two same-theory AF/IR trajectory objects strongly enough to force equality of limits.

**Outcome:** `PARTIAL_SUCCESS__SECTION9_REPAIR_SURFACE_TYPED__AFIR_TRAJECTORY_TO_SCHEME_APPLICABILITY_NOT_ESTABLISHED`

**Residual:** `RES-YM-S1c1a-R8-TRAJECTORY-TO-SECTION9-SCHEME-EMBEDDING-OR-VANISHING-INTERTRAJECTORY-ESTIMATE`

No protected lesson, obstruction, theorem, tool, motif or scientific-authority transition is created. Root #5 remains open.
