# C041S1 — syntactic MAGIC reachability is not semantic MAGIC activation

**Status:** solved local discriminator, proposal/shadow only.  
**Parent candidate:** `C041-FX-SAT-ONE-SIDED-v1`.  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.  
**Active atom:** `O9d12a2a1b-C041S1`.

## Exact local statement

For the frozen C041 canonical long-form encoder, before even-parity padding the length for a 3CNF with `v>=1` declared variables and `m>=1` clauses is

\[
L_0(v,m)=8+|\gamma(v)|+|\gamma(m)|+3m(1+\operatorname{bitlength}(v)).
\]

The canonical word is padded by one terminal zero only when `L_0(v,m)` is odd.

1. The first syntactically reachable MAGIC long form has `(v,m)=(1,1)` and even length `16`, so the first parser-reachable old level is `n=8`.
2. Every one-clause 3CNF over one variable is satisfiable. Therefore the `n=8 -> 9` transition has **no MAGIC-coded UNSAT complement point**. Its only decoder-induced UNSAT point is the separate all-zero short contradiction.
3. The first semantically active MAGIC-coded UNSAT formulas occur at `(v,m)=(1,2)`, whose canonical length is exactly `24`; hence the first semantically active old level is `n=12`, transition `n=12 -> 13`.
4. At `(v,m)=(1,2)`, a three-literal clause is falseable only when all three literals have one sign. The conjunction is UNSAT exactly for the two ordered sign patterns `(+++,---)` and `(---,+++)`.
5. The 12-bit header is `111001011010`, so both minimal MAGIC-coded UNSAT words share old row `r*=3674`. Their 12-bit payload offsets are `010101111111=1407` and `111111010101=4053`. Thus the two genuinely new MAGIC complement points in `U_13` are

\[
(3674,5503),\qquad (3674,8149).
\]

They form a two-edge star on a previously unused old row and two fresh child columns. This incidence component is disjoint from `U_12`. The separate all-zero point `(0,4096)` attaches to the existing row-zero component.

## Proof

For positive integers, `|gamma(t)|=2 floor(log2 t)+1`. The length formula is monotone enough at the bottom of the parameter range that `(1,1)` is the unique minimum: it gives `8+1+1+6=16`; `(2,1)` already has unpadded length `21` and canonical length `22`, while `(1,2)` has length `24`. Therefore every 16-bit canonical MAGIC word has exactly one one-variable clause.

With one variable, an all-positive clause is satisfied by `x=true`, an all-negative clause by `x=false`, and any mixed-sign clause is tautological. So no one-clause formula is UNSAT. At two clauses, UNSAT requires one clause to force `x=true` and one to force `x=false`; hence exactly the two ordered patterns above. Substituting the frozen bit encoding gives the displayed header, payloads and coordinates.

The claim about incidence is direct: before level 12 every cross-layer complement addition outside the seed is the all-zero short contradiction on row 0. The seed uses rows 0,1,2. Hence row 3674 has no incident complement point in `U_12`; columns 5503 and 8149 are new child columns.

## Verification and falsification

A deterministic calibration independently enumerated all eight one-clause sign patterns and all 64 ordered two-clause sign pairs. It found zero UNSAT one-clause formulas and exactly the two UNSAT two-clause formulas above, and recomputed row/payload integers and child columns exactly. This computation checks the finite arithmetic; the preceding combinatorial argument is the mathematical proof.

The counterexample-first falsifier succeeds against the previous coarse discriminator: “first MAGIC level” at `n=8` is only **syntactic activation**, not predicate-changing activation.

## What this does not prove

This result does not prove positive or zero residual augmentation at `n=12`, does not prove a quotient or multiplexing cover, does not establish any recurrence or asymptotic rate, and does not strengthen the root. In particular, a two-edge isolated complement component need not imply any factorization of the relevant-semi-filter cover problem.

## Routing consequence

The next high-information action is therefore **not** a large LP at `n=8` and not a parser-reachability screen. It is a symbolic one-sided multiplexing/neighbourhood-quotient/compiled-cover attack on the exact `n=12 -> 13` geometry, with relevance and lifted-pair slack re-audited before any augmentation claim.

RAKL novelty-class label for the solved local discriminator: `representation` (proposal/shadow classification only; not a novelty certificate).
