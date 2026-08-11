# BSD-A1a1 plectic bridge audit — richer representation does not yet close the rank-two interface

**Active canonical atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**RAKL_math base:** `6557b1b25fa839fe71aba8047c958d5da892edd8`  
**Current RAKL framework:** `bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Current application execution pin:** `bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Frozen A1a1 context:** `sha256:385d587cb9ab74512adc3fed98e00df9a804c37fd327539c2cea449a97b5417d`  
**Authority:** `SOURCE_BOUND_REPRESENTATION_ROTATION_AUDIT / SAME_CONTEXT_REVIEW_ONLY / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`

## Why this cycle is not another theta-order literature scan

The previous current-frontier cycle established that recent anticyclotomic main-conjecture results strengthen nearby p-adic machinery without supplying the exact cross-direction implication

```text
ord_{s=1} L(E,s)=2
    -> exact anticyclotomic T/J-order or regulator nondegeneracy.
```

Repeating the same scalar-order search would have low information value. This cycle therefore executes the registered alternative: rotate to a richer higher-rank arithmetic representation and ask whether it removes the missing interface rather than merely renaming it.

The representation family tested is the 2023--2026 plectic Heegner / mock-plectic / Hida--Rankin p-adic L-function programme. No new canonical child atom is allocated in this cycle. Current framework issue `SzeChunYiu/RAKL#142` records a live risk of concurrent human-readable atom identity collisions, so the active canonical identity remains `BSD-A1a1` until any future child is content-bound/reserved under a separately governed identity procedure.

## Source-bound theorem/conjecture cut

### 1. Fornea 2026 constructs a genuinely richer arithmetic object

Michele Fornea, *Plectic Heegner classes*, arXiv:2603.28327, constructs partially global Galois-cohomology classes under stated hypotheses. Theorem A is a construction theorem. In the comparison section, Theorem B recovers mock plectic invariants in the `F=Q`, one-p-adic-place setting by a partial-Frobenius eigenspace projection, while Theorem C recovers plectic Heegner points through localization in the appropriate setting.

This is relevant to A1a1 because it supplies a richer object than one scalar augmentation order. It packages local/global cohomology and admits comparison maps to previously studied higher-rank invariants.

However, the paper itself separates construction/comparison theorems from arithmetic-significance conjectures. Section 1.2 is explicitly titled **Conjectures**. Conjecture 1.9 formulates the analytic-rank/nonvanishing significance of the plectic class, and Conjecture 1.10 formulates the expected determinant/wedge relation to Mordell--Weil points when the algebraic rank is large enough. Therefore the source does not prove the root-facing implication from complex analytic rank to the required global plectic nonvanishing/determinant statement.

### 2. Fornea--Gehrmann proves a strong downstream implication, but assumes the missing nonvanishing

Fornea--Gehrmann, *Iwasawa theory and mock plectic points*, arXiv:2311.03100v2, proves under its technical hypotheses that for an elliptic curve over `Q` of even analytic rank at least two and multiplicative reduction at an inert prime `p`, **nonvanishing of the mock plectic invariant** `Q_K` implies `p`-Selmer rank two. The proof uses one inclusion of Perrin--Riou's Heegner-point main conjecture obtained from bipartite Euler systems.

The logical direction is therefore

```text
Q_K != 0  ->  p-Selmer rank = 2,
```

inside the stated arithmetic setting. Exact complex analytic rank two is part of the ambient setup, but the theorem does not derive `Q_K != 0` from that analytic-rank input. The route moves the live missing bridge to plectic nonvanishing; it does not close it.

### 3. Hernández--Molina gives a p-adic derivative-to-plectic theorem

Víctor Hernández and Santiago Molina, *Plectic points and Hida-Rankin p-adic L-functions*, arXiv:2202.12573v2 (revised 3 July 2026), constructs two-variable anticyclotomic p-adic L-functions and proves a p-adic Gross--Zagier formula computing higher derivatives of Hida--Rankin p-adic L-functions in terms of plectic points.

This is the strongest positive bridge located in the representation family:

```text
higher Hida--Rankin p-adic derivatives
    -> plectic points.
```

But two boundaries remain explicit in the source abstract. First, the relevant derivative is a p-adic/Hida--Rankin deformation coordinate, not the bare complex `s`-Taylor order of `L(E,s)` at `s=1`. Second, the interpretation of plectic points as p-adic regulators of Mordell--Weil bases in the higher-rank setting is described as conjectural. Thus this theorem supplies valuable downstream structure but does not license

```text
complex analytic rank 2
    -> nonzero plectic point/class
    -> rank 2 over Q
```

without another comparison/nonvanishing theorem.

## The exact relation matrix after representation rotation

| Arrow | Status in audited sources | Root-facing problem |
|---|---|---|
| construct plectic Heegner class | theorem | object exists under special hypotheses |
| plectic class -> mock plectic invariant / plectic point | theorem under comparison hypotheses | projection/localization may lose global information |
| higher Hida--Rankin p-adic derivative -> plectic point | theorem | derivative coordinate is p-adic, not bare complex `s` |
| nonzero mock plectic invariant -> p-Selmer rank two | theorem under hypotheses | nonvanishing is an input |
| complex analytic rank -> plectic-class nonvanishing/significance | conjectural in Fornea 2026 family | this is the missing root-facing arrow |
| plectic object -> Mordell--Weil determinant/regulator at required global scope | conjectural in the source family | still needs algebraization/global arithmetic identification |

The key result of this cycle is therefore not “plectic methods fail.” They provide a richer and more structured near-solved context than scalar theta order. The source-bound conclusion is narrower:

> The audited plectic route relocates, but does not remove, the analytic-to-arithmetic rank-two obstruction. The unresolved arrow is now visible as complex-analytic-rank-to-plectic-nonvanishing / regulator-faithfulness, while downstream plectic-to-Selmer and p-adic-derivative-to-plectic implications are substantially stronger.

## Seven-role same-context expert cell

These are role-separated AI analytical passes in one context and create no independent-review credit.

1. **Complex L/Rankin--Selberg lead.** Guards the distinction between the complex `s` variable and Hida/anticyclotomic p-adic deformation variables. Verdict: no audited theorem transports bare complex rank two into plectic nonvanishing.
2. **Plectic arithmetic-geometry lead.** Audits construction, localization/projection and global-vs-local content of plectic classes. Verdict: richer representation is real and useful, but arithmetic significance is still conjectural at the critical point.
3. **Iwasawa/Euler-system lead.** Audits Fornea--Gehrmann implication strength. Verdict: `Q_K != 0 -> p-Selmer rank 2` is a strong downstream theorem; using it in reverse would be invalid.
4. **Heights/regulators lead.** Audits whether a proved determinant/nondegeneracy theorem closes the bridge. Verdict: regulator interpretation remains conjectural in the audited plectic source family.
5. **Adversarial gluing lead.** Demands a typed chain from complex rank through plectic nonvanishing to global arithmetic rank. Verdict: the first root-facing arrow remains open; richer objects do not grant automatic faithfulness.
6. **Formal RAKL/provenance lead.** Confirms current RAKL semantic authority and RAKL_math execution pin now both equal `bd1a2768...`; historical artifact-local bindings remain immutable. No new child atom identity is allocated because concurrent identity-collision semantics are not yet a protected runtime primitive.
7. **Frontier/novelty lead.** Distinguishes genuinely new 2026 plectic source knowledge from a new BSD theorem. Verdict: retain the source/relationship novelty, not a theorem/path promotion.

## Falsifier and result

The cheapest source-level falsifier for the hypothesis “a plectic representation already repairs A1a1” is to locate, in the same theorem chain, a proved implication whose input is exact complex analytic rank two and whose output is nonzero plectic class/point or a nondegenerate rank-two global regulator, without importing algebraic/Selmer rank two, p-adic BSD, or equivalent arithmetic strength.

The audited sources do not provide such an implication. The closest positive statements either start from p-adic derivatives, assume plectic nonvanishing, or state the analytic-rank significance as a conjecture.

## Residual transformation

**Before:**

```text
find an exact complex-s -> anticyclotomic order/regulator theorem,
or show the scalar-order path imports root-strength arithmetic data.
```

**After:**

```text
the scalar representation can be rotated to a plectic class/point representation,
but the root-critical missing arrow remains:
complex analytic rank two
  -> proved nonzero root-faithful plectic class/point or regulator determinant.
```

This is a narrower and better localized interface. It makes clear that future work should not merely invent another scalar order. The next high-information source question is whether any proved complex Gross--Zagier / higher Gross--Zagier / explicit-reciprocity statement supplies this nonvanishing in the exact weight-two elliptic-curve setting under assumptions weaker than the desired rank conclusion.

## Authority and stopping decision

No mathematical candidate, lemma, new invariant, reusable lesson, tool promotion, or root claim is generated. No literature-wide nonexistence claim is made. The BSD root remains `OPEN_NO_SOLUTION_CERTIFICATE`.

Because the plectic representation produced a genuinely different discriminator but did not close the interface, the admissible next cycle should audit the exact complex-to-plectic nonvanishing bridge rather than repeat scalar anticyclotomic order searches.