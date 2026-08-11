# BSD-A1a1b source audit — higher-even theta order as a derived-height / semisimplicity obstruction

**Atom under preparation:** `BSD-A1a1b-HIGHER-EVEN-ORDER-EXCLUSION`  
**Parent result:** `BSD-A1a1-C001`, pending exact-head application CI in the current replacement PR  
**Status:** `SOURCE_BOUND_CONTEXT_PREPARATION / NO_CHILD_CANDIDATE / ROOT_AUTHORITY_NONE`  
**Framework authority inspected:** `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`

This audit is deliberately pre-candidate. It does not assume the child atom has passed a fresh strict context/memory/trace gate, and it does not promote the parent parity result before exact-head CI.

## Exact residual

The parent route has reduced the anticyclotomic theta-order uncertainty to the higher-even cases. In the registered sign `+1` setting, the remaining question is whether one can exclude

`ord_J Theta_{f/K} >= 4`

from **exact complex analytic rank two plus admissibility hypotheses alone**, without importing positive Mordell–Weil rank, two-dimensional Selmer, p-adic BSD, an equivalent-strength main conjecture, or a maximal p-adic-height nondegeneracy assumption.

The bounded primary-source audit below asks what mathematical coordinate excess theta vanishing is actually measuring before any new theorem is proposed.

## Primary-source implication audit

### 1. Howard: higher p-adic derivatives are controlled by derived heights, and degeneracy detects non-semisimplicity

Benjamin Howard, *Derived p-adic heights and p-adic L-functions* (arXiv:1202.6343), constructs derived p-adic heights and relates them to higher derivatives of p-adic L-functions. The paper also relates degeneracy of the derived heights to failure of the Selmer module over a `Z_p`-extension to be semisimple as an Iwasawa module.

**Research consequence:** excess p-adic vanishing is not naturally a bare complex-analytic coordinate. In the available theory it is coupled to the depth of an arithmetic filtration / non-semisimplicity phenomenon.

**Non-consequence:** Howard does not prove that complex analytic rank two forces the required anticyclotomic semisimplicity or height nondegeneracy.

### 2. Castella–Hsieh: the theta order indexes the derived-height filtration itself

Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2* (Forum Math. Sigma 10 (2022), e12, DOI `10.1017/fms.2021.85`) make the dependency explicit.

They define a decreasing filtration

`Sel(K,V_pE)=S_p^(1) ⊇ S_p^(2) ⊇ ...`

with derived pairings

`h_p^(i): S_p^(i) × S_p^(i) -> (J^i/J^(i+1)) ⊗ Q_p`.

For `mathfrak r = ord_J Theta_{f/K}`, Theorem 5.3 places the generalised Kato class in `S_p^(mathfrak r)` and gives the leading-term identity through `h_p^(mathfrak r)`. In the rank-two Selmer argument of §5.4, the filtration can remain constant through an **even** depth `r>=2`; the associated Iwasawa module then has `J`-primary length reflecting that depth, and characteristic-ideal divisibilities compare it with `mathfrak r`.

**Research consequence:** after parity is fixed, excluding `mathfrak r>=4` is structurally an **upper-bound / nondegeneracy / semisimplicity** problem for the anticyclotomic arithmetic filtration, not merely another functional-equation problem.

**Critical boundary:** the source obtains useful upper comparisons by introducing Selmer-dimension/filtration data and characteristic-ideal divisibilities. Those are arithmetic inputs/outputs and cannot be silently inferred from the bare premise `ord_{s=1}L(E,s)=2`.

### 3. Castella–Hsu–Kundu–Lee–Liu: order-of-vanishing is reduced to maximal anticyclotomic height nondegeneracy in a related BDP setting

Castella, Hsu, Kundu, Lee and Liu, *Derived p-adic heights and the leading coefficient of the Bertolini–Darmon–Prasanna p-adic L-function* (arXiv:2308.10474), formulate a p-adic BSD statement for the BDP p-adic L-function. For their algebraic analogue, the order-of-vanishing statement follows from expected **maximal non-degeneracy** of an anticyclotomic p-adic height; when the Iwasawa–Greenberg main conjecture is known, their results determine the leading coefficient up to a p-adic unit.

**Transfer retained:** this is evidence that excess anticyclotomic vanishing is governed by a regulator/nondegeneracy coordinate.

**Disanalogy:** the BDP p-adic L-function and its Selmer conditions are not literally the Castella–Hsieh theta element used in `BSD-A1a1`. No theorem authority transfers from one object to the other without a source bridge.

### 4. Sano: anticyclotomic p-adic BSD leading terms can follow from main-conjecture strength input

Takamichi Sano, *Derived Bockstein regulators and anticyclotomic p-adic Birch and Swinnerton-Dyer conjectures* (arXiv:2308.08875), proves descent formalisms in which anticyclotomic p-adic BSD-type statements follow from appropriate Iwasawa main conjectures up to p-adic units.

**Research consequence:** a main-conjecture route can control order/leading information, but it must be treated at its actual arithmetic strength. It is not an analytic-rank-two-only bridge by default.

## Competing diagnoses for `ord_J Theta>=4`

1. **Derived-height degeneracy:** lower derived pairings vanish too deeply, so the first nonzero arithmetic regulator appears at a higher even filtration level.
2. **Iwasawa non-semisimplicity:** the `J`-primary structure of the anticyclotomic Selmer module has longer blocks than the exact-order-two route requires.
3. **Characteristic-ideal excess:** the theta element carries additional `J`-power not ruled out by the available one-sided main-conjecture divisibilities.
4. **Representation-coordinate mismatch:** exact order two in the complex `s` direction simply does not determine the character-direction `J`-order without a new comparison theorem.

The inspected sources support these as plausible structural diagnoses; they do **not** establish that all possible mechanisms have been exhausted.

## Route-strength matrix

| Proposed route to exclude `mathfrak r>=4` | What it supplies | Hidden/explicit extra strength | Current disposition |
|---|---|---|---|
| Functional equation alone | parity of `mathfrak r` | none beyond its source hypotheses | exhausted after C001; cannot upper-bound |
| Bare interpolation | `mathfrak r>0` from central vanishing | no exact directional derivative comparison | insufficient |
| Derived-height nondegeneracy | forces earlier nonzero filtration pairing | arithmetic regulator hypothesis | promising only if nondegeneracy is independently derived |
| `dim Sel=2` + filtration analysis | strong restriction on possible filtration shape | essentially the arithmetic rank-two/Selmer coordinate sought downstream | circular for the analytic-to-arithmetic root direction |
| Iwasawa/main-conjecture equality | characteristic-ideal/order control | deep arithmetic theorem; target-specific hypotheses | usable only after strength audit, not as free analytic input |
| p-adic BSD leading-term formula | exact order/regulator package | BSD-type arithmetic data | root-adjacent/conditional, not a first bridge |

## Smallest high-information next question

The child atom should be re-represented from

> “find an upper bound `ord_J Theta<=2`”

to

> **“does exact complex analytic rank two force the first relevant anticyclotomic derived-height/regulator layer to be nondegenerate (equivalently, rule out the Iwasawa non-semisimplicity responsible for deeper even theta order), under hypotheses weaker than BSD/Selmer-rank-two/main-conjecture input?”**

That question exposes the missing coordinate rather than hiding it inside theta notation.

## Cheapest discriminators before child candidate generation

1. Search primary literature for a theorem deriving maximal anticyclotomic derived-height nondegeneracy from **complex analytic rank alone**; classify every hypothesis.
2. Search for a source theorem giving an upper bound on `ord_J Theta` from complex Rankin–Selberg/automorphic information without invoking Selmer rank or a characteristic-ideal equality.
3. Construct a logical implication table for all uses of `dim Sel`, positive Mordell–Weil rank, Sha finiteness, main conjectures, and p-adic BSD; reject any route that imports the desired arithmetic conclusion under a renamed condition.
4. Treat numerical rank-two curves only as calibration: they may falsify an overgeneralized claim but cannot prove the universal bridge.

## Bounded-search conclusion

In the primary sources inspected in this cycle, **no direct theorem was found** that derives the needed higher-even-order exclusion from exact complex analytic rank two alone. The available order-control mechanisms pass through derived-height nondegeneracy, Selmer/Iwasawa semisimplicity, characteristic-ideal/main-conjecture input, or p-adic BSD-type structure.

This is a source-bound route classification, **not an impossibility theorem and not a novelty claim**. A fresh strict `MathContextFiber`, dual-memory review, expert-context review and hash-chained pre-candidate trace are still required before `BSD-A1a1b` can generate any mathematical candidate.
