# O9d12a2a1a1c — free-union quotient of cyclic intersection complexity

**Framework:** `SzeChunYiu/RAKL@a41a24b0061aa7e19d43732bf878ee5902465d23` (`rakl` package 0.1.0; no separate method-version manifest on current main).  
**Application base:** `SzeChunYiu/RAKL_math@bd36e1661053a07b53af8f0b8bdf44da7c9d677e`.  
**Authority:** proposal/shadow source-bound representation lemma; same-context review only; no root authority.

## Source binding

Primary source: Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (18 March 2025), `https://eccc.weizmann.ac.il/report/2025/033/`. Section 2.5 defines cyclic discrete complexity: union and intersection gates may occur cyclically, and `D^cyc_cap` counts only intersection operations. Lemma 16 gives convergence after at most the syntactic-sequence length. Theorem 30 states exactly `rho(A,B)=D^cyc_cap(A|B)` for nontrivial `A` and nonempty generator family `B`.

The source was freshly re-opened in this cycle, including the PDF statement of Theorem 30. No current 2026 circuit-lower-bound result is transported into this atom without an applicability map.

## Exact local lemma: free-union quotient

Let `Gamma` be finite, `A subset Gamma` nontrivial, and `B` a nonempty finite generator family. Let `U(B)` be the finite closure of `B` under unions, including every finite union of members of `B`.

**Lemma.**

`D^cyc_cap(A | B) = D^cyc_cap(A | U(B))`.

Consequently, by Cavalar–Oliveira Theorem 30,

`rho(A,B) = rho(A,U(B))`.

### Proof

The `<=` direction is immediate because `B subset U(B)`.

For the reverse direction, take a cyclic syntactic sequence over the enlarged generator family `U(B)` with `k` intersection operations. Each constant generator `C in U(B)` used by the sequence is a finite union of original generators from `B`. Replace that constant occurrence by an acyclic union tree over the corresponding members of `B`, and feed its output wherever `C` was used. These replacement gates are all unions, so the number of intersection operations remains exactly `k`. Their outputs are fixed sets equal to the original constants before the cyclic part is evaluated; therefore the fixed-point evaluation of the original cyclic gates is unchanged. Thus any `k`-intersection witness over `U(B)` yields a `k`-intersection witness over `B`, proving `D^cyc_cap(A|B) <= D^cyc_cap(A|U(B))`.

Combining both inequalities and Theorem 30 gives the cover-complexity equality.

## Falsifier/admission rule for the current lane

A proposed source-native scalar or representation is **not admissible as a direct lower-bound coordinate** merely because it is large on `(A,B)` if it can change under `B -> U(B)` with no compensating theorem. The counted complexity is unchanged by that transformation. Before target scoring, a candidate must therefore do at least one of:

1. factor through the free-union quotient;
2. prove a lower-bound theorem uniform over every free-union expansion of the generator presentation; or
3. explicitly minimize/canonicalize over the free-operation equivalence class.

This strictly generalizes a single cheap-target check: every target already in `U(B)` has zero cyclic intersection complexity and hence zero cover complexity, regardless of presentation-sensitive volume, entropy, generator multiplicity, or similar scores.

## What this rules out and what it does not

It rules out **presentation-sensitive score-first routes** that can be inflated by adding union-derived generators. It does not upper-bound `rho` for an explicit hard graph, does not show every scalar invariant fails, and does not constrain transformations that add genuinely new intersection power.

The result also does not solve the residual left by O9d12a2a1a1b. The root-facing task remains to find a quotient-respecting property of the shared `t`-intersection cyclic system, prove a universal bound in `t`, and establish a super-logarithmic value on an explicit graph.

## Expert cell (same context, not independent review)

- **Circuit lower bounds / barriers:** checked that the conclusion is scoped to the intersection-count measure and creates no unrestricted circuit lower bound.
- **Fusion/cyclic-complexity specialist:** checked the replacement construction against Section 2.5 semantics and Theorem 30.
- **Extremal combinatorics:** tested the all-free-union edge case and generator-presentation inflation.
- **Complexity-transfer specialist:** blocked any inference from this quotient lemma to a super-log explicit graph lower bound.
- **Adversarial construction specialist:** attempted to break the reverse inequality by cyclic dependence on a union-derived constant; replacement by an acyclic union tree leaves the constant semantic value unchanged.
- **Formal/provenance reviewer:** checked exact statement/success contracts and kept this as proposal/shadow evidence.
- **Gluing reviewer:** classified the remaining gap as local-to-root gluing: no quotient-respecting `<= f(t)` invariant with explicit super-log target has been supplied.

## Root status

`OPEN_NO_SOLUTION_CERTIFICATE`.
