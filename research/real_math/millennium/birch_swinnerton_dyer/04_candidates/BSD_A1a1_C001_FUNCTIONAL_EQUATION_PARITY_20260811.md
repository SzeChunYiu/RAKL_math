# BSD-A1a1-C001 — functional-equation parity lower bound for the anticyclotomic theta order

**Atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**Candidate:** `BSD-A1a1-C001`  
**Authority:** `SOURCE_BOUND_DERIVED_LOCAL_LEMMA / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`  
**Framework authority:** `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`

This candidate was generated only after the merged strict `BSD-A1a1` context, dual-memory review, same-context expert review and seven-event pre-candidate trace passed the current RAKL gate.

## Exact scoped statement

Let `p>3`, let `O` be the valuation ring used for the ordinary anticyclotomic construction, let
`Lambda = O[[Gamma^-]]` for `Gamma^- ~= Z_p`, and let `J` be its augmentation ideal. Let `*` be the involution induced by `gamma -> gamma^{-1}`.

Suppose a nonzero theta element `Theta in Lambda` satisfies

`Theta^* = + Theta * u`

with `u` a group-like element (hence `u == 1 mod J`). If

`r = ord_J(Theta)`

is finite, then `r` is even.

In the trivial-character Castella–Hsieh setup for an elliptic curve `E/Q` with good ordinary `p>3`, root number `+1`, and `L(E/K,1)=0`, the cited sources give a nonzero `Theta_{f/K}` and `r>0`. Chida–Hsieh's functional equation has sign `epsilon_p(f) epsilon(f)`. At a good prime `p`, `epsilon_p(f)=+1`; with root number `epsilon(f)=+1`, the sign is `+1`. Therefore

`ord_J Theta_{f/K} >= 2`.

This does **not** prove `ord_J Theta_{f/K}=2`.

## Derivation

Choose a topological generator `gamma` and write `T=gamma-1`, so `J=(T)`. The involution sends

`T -> gamma^{-1}-1 = (1+T)^{-1}-1 = -T + T^2 - T^3 + ...`.

Hence on the associated graded line `J^r/J^(r+1)`, the involution acts as multiplication by `(-1)^r`.

Write the first nonzero term of `Theta` as

`Theta = a_r T^r mod J^(r+1)`, with `a_r != 0`.

Because the group-like factor `u` has augmentation one,

`Theta*u = a_r T^r mod J^(r+1)`.

Passing the functional equation `Theta^*=Theta*u` to `J^r/J^(r+1)` gives

`(-1)^r a_r = a_r`.

Since `p>3`, `2` is a unit in `O`. The nonzero leading class therefore excludes odd `r`. Thus `r` is even.

Castella–Hsieh Section 5.3 separately states that `Theta_{f/K}` is nonzero (using Vatsal) and that `L(E/K,1)=0` implies `r>0` by interpolation. Combining the two statements yields `r>=2`.

## Source binding

1. **Chida–Hsieh**, *Special values of anticyclotomic L-functions for modular forms*, arXiv:1204.2427, Theorem B / Theorem 4.8:
   the theta element satisfies an inversion functional equation
   `Theta^* = epsilon_p(f) epsilon(f) Theta sigma_{N+}^{-1}` in the weight-two specialization; the group-like factor has augmentation one.
2. **Castella–Hsieh**, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum of Mathematics, Sigma 10 (2022), e12, DOI `10.1017/fms.2021.85`, Theorem 2.3 and Section 5.3:
   the trivial-character theta element is nonzero and, under their hypotheses with `L(E/K,1)=0`, its augmentation order is strictly positive.

No statement above identifies the complex `s`-order with the anticyclotomic `T`-order. The result uses the complex root sign only to fix the **parity sign** in a source functional equation.

## Hostile falsifiers

- **Sign `-1`:** the same graded calculation gives `(-1)^r=-1`, so the allowed parity is odd. The candidate is intentionally sign-sensitive.
- **`p=2`:** `2` is not a unit, so the contradiction for odd `r` fails. The registered setup has `p>3`.
- **`Theta=0`:** `ord_J` is not a finite leading-order invariant. Castella–Hsieh explicitly invoke nonvanishing.
- **Non-augmentation-one multiplier:** a scalar/unit with different residue could change the leading relation. The source factor is group-like and has augmentation one.
- **Different involution or multivariable deformation:** the proof is scoped to the one-variable anticyclotomic inversion involution.

All hostile cases are outside at least one registered precondition; none falsifies the scoped statement.

## Research consequence

The live residual is no longer merely “why is the `T`-order positive?” The source-functional-equation route already removes every odd positive order. Exact order two is now equivalent, within this route, to excluding the higher even cases

`ord_J Theta_{f/K} in {4,6,8,...}`.

Open child: `BSD-A1a1b-HIGHER-EVEN-ORDER-EXCLUSION`.

That child must receive a fresh context, method-transfer review, dual-memory review, same-context expert cell and pre-candidate trace before any candidate generation. Existing p-adic BSD/main-conjecture or derived-height statements must be classified by whether they import Selmer rank, positive Mordell–Weil rank, maximal height nondegeneracy, or root-equivalent arithmetic information.
