# C043 first post-C042 residual-language split — pre-output freeze

**Parent:** `C042-ACTIVATION-QUOTIENT-GATE-v1`  
**Candidate:** `C043-FIRST-ROW-SPLIT-RESIDUAL-v1`  
**RAKL route:** latest-framework `SEARCH` through the scoped C042/C013 exact-neighborhood quotient episode  
**Root:** `OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`

## Object and quantity of interest

For the frozen C041 decoder and a parent level (n), define the canonical-MAGIC
UNSAT completion residual

\[
R_{n,p}=\{s\in\{0,1\}^n:\operatorname{Dec}(p\Vert s)
\text{ is canonical MAGIC long-form and UNSAT}\}.
\]

The special all-zero short-code contradiction remains separate.  Distinct
(R_{n,p}) are exactly distinct new-band complement row stars.  Dually, a
suffix is classified by the set of prefixes that accept it.  The full type
count must additionally account for every accumulated old band.

The bounded QoI is the first parent level after (n=12) where canonical UNSAT
words occupy more than one row label, followed by the exact prefix/suffix
residual classes, full (U_{n+1}) row/column twins, and the elementary
finite type-class upper bound on (ho(G_{n+1})).

## Frozen predictions

These values are frozen before executing the corroborating evaluator.

1. At word length 26, the only canonical parameter pairs are
   ((v,m)=(4,1),(5,1),(6,1),(7,1)), hence every canonical formula is SAT.
2. No canonical parameter pair has even encoded length 28.
3. The unique canonical parameter pair at length 30 is ((v,m)=(1,3)).
4. A one-variable clause is classified as
   (P=000), (N=111), or (T=) mixed sign.  A three-clause CNF is UNSAT
   exactly when its ordered clause list contains both (P) and (N).
5. Therefore the length-30 layer contains exactly

   \[
   8^3-2\cdot7^3+6^3=42
   \]

   canonical UNSAT words.
6. The 12-bit header is `111001011011`.  The equal split exposes the first
   three payload bits and therefore four active row labels

   ```text
   29402  29403  29406  29407
   ```

   corresponding to first-two-sign patterns (00,01,10,11).
7. The (00) and (11) residuals contain 17 suffixes each.  The (01) and
   (10) residuals are equal and contain four suffixes each.  The positive,
   negative and mixed residuals are pairwise distinct.  Hence the new band has
   exactly three nonempty row types.
8. Nonempty new suffix columns have exactly the three prefix-neighborhoods
   ({00}), ({11}), and ({00,01,10,11}), so the new band also has
   exactly three nonempty column types.
9. After fallback edges at parents 13--15 and every older band are included,
   neither new type collides with an old nonempty type.  Thus

   \[
   t^{\rm row}_{16}=t^{\rm column}_{16}=8.
   \]
10. The exact type-class rectangle construction gives only

    \[
    D_{\cap}(G_{16})\le 8,
    \qquad
    \rho(G_{16})\le 8.
    \]

## Proof obligations and falsifiers

1. Derive the complete parameter classifications at lengths 26, 28 and 30
   from the gamma/payload formula, including raw-odd plus zero-padding cases.
2. Prove the (P/N/T) criterion and the count 42 without using enumeration as
   truth authority.
3. Prove the four residual sizes and the equality
   (R_{15,29403}=R_{15,29406}).  One suffix in their symmetric difference
   refutes the prediction.
4. Exhibit witnesses separating the positive, negative and mixed residuals.
5. Prove the three suffix-neighborhood classes and rule out a fourth.
6. Account for all old bands and show fallback columns join the existing
   row-zero column class rather than creating a new type.
7. Prove new-band support prevents collision with every old nonempty row or
   column type.
8. Apply the type-class construction only in the upper-bound direction.

Allowed branches are `PARAMETER_CLASSIFICATION_FAILURE`,
`MIXED_PREFIX_SPLIT`, `THREE_RESIDUAL_COLLAPSE`, `OLD_TYPE_COLLISION`,
`EXACT_8_BY_8_TYPES`, and `CANNOT_CHECK`.

## Authority boundary

This is a finite symbolic discriminator.  It is not a quotient-cover optimum,
uniform type-growth theorem, recurrence, lower bound, circuit result, novelty
claim, or P-versus-NP certificate.  A larger quotient may still have a
constant multiplexed cover.  Computation can check the finite receipt but is
not the proof.

Only mathematical lemmas, explicit witnesses/counterexamples, broken
assumptions, transfer conditions and falsifiers earn saturation credit.  Git,
CI, schemas, hashes, implementation, solver behavior and runtime are assurance
only.
