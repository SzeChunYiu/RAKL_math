# H4d1c-C010 — ambient smoothness is not necessary for branch coverage

**Authority:** `PROPOSAL_SHADOW / VERIFIED_SCOPED_ALGEBRAIC_NONIMPLICATION / NO_HODGE_THEOREM / ROOT_AUTHORITY_NONE`.

## Exact consumer and attempted implication

The local variational consumer is the base-changed witness incidence

`pi_H : W_H := W x_S H -> H`,

where `S` is an ambient deformation base and `H -> S` is one locally marked reduced irreducible Hodge branch. C009/PR #350 records a safe sufficient construction pattern: if suitable relative Hilbert factors are smooth over the ambient base, their coupled source remains smooth after Hodge-branch base change. C010 asks only whether ambient smoothness should also be treated as a **necessary** routing target.

Attempted implication under audit:

`branch-restricted smooth/full consumer W_H -> H  =>  ambient W -> S smooth`.

## Exact hostile algebraic world

Let

`A = C[x,y]`, `S = Spec(A)`, `B = A/(x) = C[y]`, and `H = W = Spec(B)`.

Let `i: H = W -> S` be the closed immersion cut out by `x`.

### 1. The ambient map is not smooth

The sequence of `A`-modules

`0 -> A --x--> A`

is injective. Tensor with `B=A/(x)`. Multiplication by `x` on `B` is zero, so the resulting map

`B --0--> B`

is not injective. Hence `B` is not flat over `A`. Smooth morphisms are flat, so `i:W->S` is not smooth.

This is stronger than a tangent-rank complaint: the ambient morphism itself fails the flatness necessary for smoothness.

### 2. The branch-restricted map is the identity

Base-change `i` along the same closed branch `H->S`:

`W_H = W x_S H = Spec(B tensor_A B)`.

Because both copies of `B` are `A/(x)`, multiplication gives

`B tensor_A B ~= B`.

Under this identification, `pi_H:W_H->H` is the identity of `H`. Therefore `pi_H` is smooth and its image is all of the irreducible branch `H`. The ambient closed immersion is proper, and properness is preserved by base change, so this hostile world also keeps the C007 image-closure guard.

## Scoped conclusion

`AMBIENT_RELATIVE_SMOOTHNESS_OVER_S` is **not a necessary condition** for smooth/full branch-restricted consumer geometry. C009's ambient relative-Hilbert smoothness criterion remains a valid strong sufficient pattern; what is pruned is using it as a necessary search filter for the Hodge branch.

The root-aligned successor obstruction is therefore

`O-H4D1C-BRANCH-RELATIVE-SMOOTHNESS-OR-DIRECT-DOMINANCE`:

for an exact signed-`Q` witness source, prove smoothness/integrability of the **base-changed** map `W_alpha x_S H -> H` at a useful point together with proper/component binding, or bypass smoothness and prove the actual branch image directly.

## Hodge boundary

This hostile world is not claimed to be a Hodge witness incidence. It proves only a morphism-theoretic nonimplication needed to prevent overconstraining the search. It does not construct an algebraic representative of an arbitrary rational Hodge class and does not discharge exact signed-`Q` class identity, source-family completeness, higher-order/formal lifting, algebraization/effectivity, monodromy, singular degeneration/specialization, completion descent, global continuation, or root initial algebraicity.

The local mathematical failure here is an **overstrong representation/routing condition**. It is not a local-to-global gluing failure; properness, monodromy, degeneration and global continuation remain separately open gluing coordinates.

## Source controls

- Stacks Project, Section 29.35: smooth morphisms are flat and smoothness is stable under base change.
- Kloosterman, arXiv:2104.14845: positive complete-intersection variational-Hodge calibration only.
- Nishinou, arXiv:2009.01651: positive semiregular divisor-map calibration only.
- Nasu, arXiv:math/0505413: hostile Hilbert-obstruction context only.

No literature source is used to infer the general Hodge conjecture.
