# O9d12a2a1a1d — zero-cost shattering control for quotient-respecting base richness

**Framework source of truth:** `SzeChunYiu/RAKL@38a530a52d863513db16052474b85e63fbb488cd` (`RAKL` method 3.0.0; package 0.1.0).  
**Application base:** `SzeChunYiu/RAKL_math@c48293364c6bdf7e0c5d93f5e01d889008c9eb61`.  
**Authority:** proposal/shadow route-pruning only; same-context review only; no theorem/root promotion authority.

## Why this atom

The previous current-main atom `O9d12a2a1a1b` showed that, for fixed `Lambda`, later source-defined closure dynamics factor pointwise through the full base state and shared rule system. Open draft PR #113 adds a proposal-only normalization warning: a lower-bound coordinate should survive free-union presentation changes because unions are uncharged in cyclic intersection complexity. This cycle asks the cheaper next question:

> Is surviving the free-union quotient sufficient for an **absolute base-richness** statistic to be bounded by the number of counted intersections, even in the exact graph generator family?

The candidate family is deliberately narrow: trace-family cardinality / entropy and VC dimension of the free-union base traces on the target. These are used as falsifiers only; no VC-dimension lower-bound theorem is assumed.

## Primary-source binding

Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033, 18 March 2025. Section 2.2.2 defines the graph discrete space with generator family `G_{N,N}` consisting of rows and columns. Section 2.5 defines cyclic discrete complexity and `D^cyc_cap` by counting only intersection operations in a cyclic syntactic sequence. Theorem 3 in the introduction, proved as Theorem 30 in Section 3.4, states for non-trivial `A` and non-empty `B` that cover complexity equals cyclic intersection complexity:

`rho(A,B) = D^cyc_cap(A | B)`.

A targeted current ECCC/arXiv scan was also run for a 2026 follow-up directly on this two-dimensional cover/cyclic-intersection framework. No directly applicable primary result was identified in that bounded scan; no absence claim beyond the search boundary is made.

## Exact zero-cost construction

Let `N >= 2`, `Gamma=[N]x[N]`, and `B=G_{N,N}={R_1,...,R_N,C_1,...,C_N}`. Take the non-trivial target

`A = R_1 = {(1,j): j in [N]}`.

Because `A` is already a generator, it requires **zero intersection operations**. Hence

`D^cyc_cap(A | B)=0`,

and by Cavalar–Oliveira Theorem 3 / Theorem 30,

`rho(A,B)=0`.

Let `U(B)` be the finite closure of `B` under unions, and define the free-base trace family on the target

`T_A = { C intersect A : C in U(B) }`.

### Lemma: the free-base trace shatters the whole target

`T_A = P(A)`.

**Proof.** The inclusion `T_A subseteq P(A)` is tautological. Conversely, let `S subseteq A`. Write `J_S={j in [N] : (1,j) in S}` and take

`C_S = union_{j in J_S} C_j`.

This is a union of generators, hence `C_S in U(B)`, and its restriction to the first row is exactly

`C_S intersect R_1 = S`.

Therefore every subset of `A` occurs as a zero-cost base trace. QED.

Consequently,

`|T_A| = 2^N`, `log_2 |T_A| = N`, and `VCdim(T_A)=N`.

Thus these absolute, free-union-quotient-respecting base-richness statistics are unbounded with `N` while the counted cyclic intersection cost is exactly zero. In particular, there is no finite function `f` for which either

`log_2 |T_A| <= f(D^cyc_cap(A|B))`

or

`VCdim(T_A) <= f(D^cyc_cap(A|B))`

holds uniformly over these graph-space instances.

## What failed, exactly

This falsifies only the candidate family **absolute richness of the zero-cost base trace on the target**. It does not show that VC/shattering ideas are globally useless, and it does not rule out a *relative* statistic measuring new distinctions introduced by counted intersections after conditioning on the free base.

The failure is local mathematical/representation failure of a candidate lower-bound coordinate. Separately, the local-to-root gluing obstruction remains open: no target-relative statistic `Phi` has yet been proved to satisfy a universal per-intersection bound and to take a super-logarithmic value on an explicit graph.

## Same-context expert cell

Seven role-separated passes were used, with no independent-review credit:

- **Circuit lower bounds / barriers:** verified that the result is route pruning only and gives no unrestricted circuit lower bound.
- **Cyclic discrete-complexity specialist:** checked that `A=R_1` is a generator and that `D^cyc_cap` charges intersections only under the cited source definition.
- **Extremal set-systems / VC specialist:** checked that selected column unions realize every subset of `R_1`, hence the full powerset and VC dimension `N`.
- **Transfer specialist:** kept the construction in the exact `G_{N,N}` graph context rather than relying on an arbitrary-generator counterexample.
- **Adversarial construction specialist:** checked `N>=2`, non-triviality of `A`, empty/full subset boundary cases, and the fact that no intersection is hidden in `C_S`.
- **Formal/provenance reviewer:** bound the claim to the current root/success contracts, current framework SHA, and the primary source.
- **Gluing reviewer:** separated the closed local candidate failure from the still-open universal accounting and explicit-target bridge.

## Episode -> diagnosis -> obstruction/lesson

**Episode observation:** the quotient-respecting trace family on `A=R_1` is already the full powerset at zero counted intersection cost.

**Diagnosis:** free-union quotient invariance is necessary for this lane but not sufficient; an absolute richness score can measure expressive capacity already present in the uncharged base.

**Proposal-only reusable obstruction/lesson:** before scoring any entropy, shattering, trace-count, rank-like, or other base-richness candidate, test whether the same quantity can be large on an exact `t=0` graph instance. A surviving candidate should be relative to the zero-cost base or come with a proved subtraction/conditioning theorem. This lesson is not counted as retained learning until a protected retention gate authorizes it.

## Next atom

Search only among **incremental/conditional** coordinates that vanish on the zero-cost base, then prove a legal one-intersection accounting inequality before evaluating an explicit graph. A natural next discriminator is whether adding one intersection-generated set can increase a suitably normalized trace/shattering potential by a universally bounded amount after arbitrary free unions.

## Root status

`OPEN_NO_SOLUTION_CERTIFICATE`.

No explicit super-logarithmic graph cover lower bound, unrestricted circuit lower bound for an NP-complete language, proof of `P != NP`, formal proof certificate, bounded novelty certificate, or independent mathematical review is produced.
