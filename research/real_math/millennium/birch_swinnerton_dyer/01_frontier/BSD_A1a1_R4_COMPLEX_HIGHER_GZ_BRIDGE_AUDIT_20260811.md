# BSD A1a1 R4 — complex higher-Gross–Zagier bridge audit

**Cycle:** `BSD-A1a1-COMPLEX-HIGHER-GZ-20260811-R4`  
**Canonical atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**RAKL_math base:** `812addd25a7f34d3c6272143e21d5d7db34539aa`  
**Prospective preaction head:** `8b7d561641c1374ac56088c582b8282cdcd8e01e`  
**Framework at preaction freeze:** `SzeChunYiu/RAKL@eca9697cdd86cf97890815ece8d5776bbb294c3f`, method `3.0.0`  
**Latest framework observed after the search:** `SzeChunYiu/RAKL@559e4b1dbbd209818f88ded0933e4d7b256b9011`; the intervening diff does not modify `src/rakl/method_specs.py`, `RAKL_VERSION.json`, the mathematical-research workflow, or the v3 experience substrate.  
**Execution pin in RAKL_math:** `787c7e00af2a5877ccb715bc807ec14f52974e9c` (stale; provenance only, no gate exemption)  
**Frozen fibre:** `sha256:385d587cb9ab74512adc3fed98e00df9a804c37fd327539c2cea449a97b5417d`  
**Authority:** `SOURCE_BOUND_ROUTE_ONTOLOGY_REFINEMENT / NO_MATHEMATICAL_CANDIDATE / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`.

## Exact question

The prior plectic cycle left the first root-facing arrow open:

```text
ord_{s=1} L(E,s)=2
   -> nonzero root-faithful plectic/global class or rank-two regulator
   -> p-primary/Mordell-Weil information.
```

R4 froze a narrower discriminator before execution: locate a **number-field, weight-two elliptic-curve theorem** whose input is the exact complex second-order vanishing/second complex central derivative and whose output is a nonzero arithmetic object strong enough to feed a proved rank bridge, without assuming Mordell-Weil rank two, Selmer rank two, finite Sha, p-adic BSD, or equivalent arithmetic strength.

## Counterexample-first source classification

The bounded primary-source search exposed an important terminology collision. “Higher Gross–Zagier” is not one coordinate.

| Meaning of “higher” | Primary source found | What is actually proved | Why it does not close A1a1 |
|---|---|---|---|
| **Higher complex derivative order** | Yun–Zhang, arXiv:1512.02683 | over function fields, an `r`-th central derivative is identified with a Heegner–Drinfeld self-intersection | correct derivative-order abstraction, wrong global arithmetic geometry; no number-field transfer theorem |
| **Higher weight / higher-cycle codimension** | Lilienfeldt–Shnidman, arXiv:2408.04375; Du–Peng, arXiv:2603.15795v1 | a central derivative is represented by a Beilinson–Bloch/global height pairing of generalized/higher Heegner cycles | number-field arithmetic intersection, but the located formula is the first-central-derivative Gross–Zagier direction, not complex derivative order two for `E/Q` |
| **Higher p-adic deformation derivative order** | Ishikawa, arXiv:1409.8584 | a second derivative of a two-variable p-adic L-function along a Hida-family coordinate is a squared p-adic logarithm of a global point | derivative order two but wrong analytic coordinate; it cannot be identified with `d^2/ds^2 L(E,s)|_{s=1}` without a separate comparison theorem |

The current March-22-2026 manuscript of Castella–Hsieh, arXiv:1809.09066, supplies the strongest target-near number-field check. Its motivating analytic condition is explicitly replaced by an **algebraic counterpart**. Darmon–Rotger's equivalence between generalized-Kato nonvanishing, Selmer dimension two, Mordell–Weil rank two, and analytic order two is presented as a conjecture, and the source explicitly identifies rank two `iff` analytic order two with the rank-two BSD conjecture. Theorem A proves a generalized-Kato/strict-Selmer equivalence under stated auxiliary hypotheses; Corollary B gets generalized-Kato nonvanishing after assuming Mordell–Weil rank two and finite `p`-primary Sha. Thus this source cannot be reversed into the desired analytic-rank-two bridge.

## Solved analogue and DifferenceWitness

**Solved analogue.** Yun–Zhang gives exactly the structural pattern the target search was previously missing: a genuine **higher complex derivative order** is represented by a higher arithmetic-intersection object.

**Shared abstraction**
- a central L-function vanishes to prescribed order;
- derivative order is encoded by a geometric/arithmetic cycle with matching “higher” structure;
- nontrivial intersection data is the candidate arithmetic carrier of the leading term.

**DifferenceWitness**
- source is a global function field, not a number field;
- the arithmetic geometry uses Drinfeld shtukas, Frobenius, and Heegner–Drinfeld cycles;
- the target is a modular elliptic curve over `Q` and must ultimately identify `E(Q)`, the real regulator, local/Tamagawa/torsion factors and Sha;
- no theorem found transports the Shtuka intersection identity to the number-field target;
- therefore only the **representation/search principle** transfers: search for a number-field object carrying complex derivative order two, not for another p-adic derivative surrogate.

This is transfer evidence, not theorem authority.

## Gluing audit

Local mathematical and gluing failures remain separate.

**Local/source-level mathematical residual:** the bounded number-field source set contains first-complex-derivative height formulas and p-adic second-derivative formulas, but no theorem was located in the exact target cell `number field + weight two + complex s-derivative order two + root-faithful arithmetic output`. This is not a literature-wide nonexistence result.

**Local-to-global/gluing residual:** even if an arithmetic-intersection object for the complex second derivative were constructed, the BSD route still requires a same-theory theorem identifying its nonvanishing/determinant with the Mordell–Weil rank/regulator and controlling Sha/local corrections. The plectic/generalized-Kato downstream theorems do not automatically provide that comparison.

## Expert-cell post-result consensus

The complex-L lead accepts the Yun–Zhang result only as a derivative-order analogue. The arithmetic-geometry lead rejects higher-weight first-derivative formulas as rank-two closure. The plectic/Iwasawa lead rejects p-adic second derivatives as complex coordinates. The adversarial lead treats Castella–Hsieh's conjecture/theorem split as a decisive near-miss falsifier. The formal/provenance lead preserves the stale execution pin and current-framework drift without rewriting chronology. The ontology/transfer lead retains the three-axis normalization of “higher” because it changes future query routing.

No role grants independent-review credit.

## Outcome and residual transformation

**Before**

```text
find a proved complex-to-plectic nonvanishing/leading-term theorem.
```

**After**

```text
normalize "higher Gross-Zagier" by:
  (complex derivative order,
   weight/cycle codimension,
   p-adic deformation coordinate).

The target cell is:
  number field
  + weight-two elliptic curve
  + complex s-derivative order two
  + root-faithful arithmetic output.

A solved higher-complex-derivative/intersection pattern exists over function fields,
while located number-field near-matches occupy adjacent cells.
Need either:
  A. a number-field theorem in the target cell, then a same-theory arithmetic-faithfulness bridge; or
  B. a proved comparison identifying an existing plectic/generalized-Kato object with that complex higher-derivative arithmetic carrier.
```

This is a **material ontology/representation route refinement**, not a new BSD theorem. No candidate, invariant, lesson promotion, reusable tool promotion, or root certificate is created.

**Route-diagnostic novelty class:** `ontology` (with a witnessed `transfer` analogue).  
**BSD theorem novelty class:** not applicable; no solved BSD subproblem.

Root remains `OPEN_NO_SOLUTION_CERTIFICATE`.
