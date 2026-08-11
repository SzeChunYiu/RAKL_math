# O9d12a2a1a1b — fixed-Λ global closure factorization audit

**Date:** 2026-08-11  
**Framework source of truth:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@24194bba4c88cc4be19dad03d59bfa79599d5ee9`  
**Authority:** `SOURCE_BOUND_REPRESENTATION_ROUTE_PRUNING / SAME_CONTEXT_REVIEW_ONLY / NO_LOWER_BOUND_CANDIDATE / ROOT_AUTHORITY_NONE`

## Question

The parent line asked whether, after witness-local activation has been quotiented by a sufficient source projection, a **global** incidence/correlation statistic of the Theorem-24 closure can expose new lower-bound information.

Before defining such a statistic, this cycle asks the cheaper interface question:

> For a fixed integral pair family `Λ`, does the source recurrence itself create any new distinction between witnesses beyond the full source-defined base incidence vector?

## Primary source

Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (18 March 2025), especially Theorem 24, Claim 27, equations (6)–(8), and Theorem 30.

The paper defines, for `U=A^c` and a fixed pair family `Λ`, the minimal preservation family `G_w` above each witness `w`. The base rule inserts generator traces and all supersets. The propagation rule inserts `E_i∩H_i` and all supersets whenever both antecedents are present. Claim 27 binds `∅∈G_w` exactly to `w∈A`.

For the global construction, the paper uses the finite multiset

`Ω = B_U ∪ {E_i} ∪ {H_i} ∪ {H_i∩E_i} ∪ {∅}`

and defines `S_C^j` as the witnesses whose `G_w` contains `C` before propagation stage `j`. Its equations (6)–(8) give the exact recurrence from generator incidence, pair intersections, and upward closure. Theorem 30 later identifies cover complexity exactly with cyclic intersection complexity.

## Exact local lemma: pointwise factorization

For fixed `Λ` and `Ω`, write

`x_w^j(C) = 1[w ∈ S_C^j]`.

Let the base vector `x_w^1` contain all source-defined coordinates indexed by `Ω`. Then equations (6)–(8) imply the pointwise Boolean recurrence

`y_w^j(C) = x_w^(j-1)(C) OR OR_{i: E_i∩H_i=C} (x_w^(j-1)(E_i) AND x_w^(j-1)(H_i))`

followed by

`x_w^j(C) = OR_{C'⊆C} y_w^j(C')`.

Hence, for fixed `Λ`, `Ω`, and inclusion relation, the entire trajectory of one witness is a deterministic function of its base vector.

**Corollary.** If `x_u^1 = x_v^1`, then `x_u^j = x_v^j` for every later stage `j`.

### Proof

The displayed equations are the source recurrence evaluated pointwise at a fixed witness. Equality at stage `j-1` gives equality of every conjunction and disjunction defining `y^j`, and the same fixed inclusion relation then gives equality of every `x^j`. Induction on `j` proves the claim.

This is a source-exact representation lemma, not a circuit lower bound and not a new theorem about `ρ`.

## Falsifier result

The proposed global-dynamics DifferenceWitness

`same full source base state / different later closure trajectory`

is impossible for fixed `Λ`.

This does **not** say that global closure incidence is useless. It says that any useful global statistic must obtain its lower-bound force from a coordinate already present in, or constraining, the **shared rule system/base incidence**—for example, a theorem that every `t`-pair cyclic system has bounded value—rather than from an emergent later-stage interaction between witnesses.

The result therefore sharpens the open residual:

> Identify a source-native property of the shared `t`-pair cyclic construction or cover family that has a proved upper bound as a function of `t`, remains nontrivial on cheap/multiplexed controls, and is super-logarithmic on an explicit graph.

Theorem 30 makes this the root-facing coordinate: `ρ(A,B)` is exactly the minimum cyclic intersection complexity. Merely computing entropy, rank, state count, or correlation of a fixed-`Λ` closure trajectory does not lower-bound `t` unless a separate theorem bounds that statistic for all `t`-rule systems.

## Current-literature scan

A fresh ECCC scan found active 2026 progress on other circuit-lower-bound fronts, including Ren–Williams on near-maximum lower bounds for `E^prMA/_1`, Raz on natural-proof barriers for linear functions, and Chen–Tal–Wang on depth-2 threshold circuits. These results were **not transported** into this atom: no target-specific map or DifferenceWitness connects their range-avoidance/threshold/linear-function coordinates to the Cavalar–Oliveira fixed-`Λ` cover recurrence.

## Root status

`OPEN_NO_SOLUTION_CERTIFICATE`.

No explicit super-logarithmic full-cover lower bound, unrestricted circuit lower bound for an NP-complete language, `P != NP` proof, novelty certificate, formal proof certificate, or independent review is produced.
