# RAKL P-versus-NP recursive research ledger — C034 through C040

**Execution date:** 2026-08-11  
**Root target:** prove `P = NP` or `P != NP` under standard definitions  
**Root authority:** `OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`  
**Current lane:** full semi-filter fusion covers, fractional successor to C024

This packet records completed recursion, exact finite certificates, repaired
failures, and the resulting strict residual. It does not claim a solution of
P versus NP.

---

## 1. Analytical expert cell

These are role-separated analytical passes, not independent external peer
review.

| Role | Background and delegated responsibility | Contribution |
|---|---|---|
| Cover-combinatorics lead | Semi-filters, fusion rules, closure systems | Proved full-union domination and witness-persistence transfer. |
| LP/optimization lead | Fractional packing/covering, primal-dual certificates | Built the fractional CEGIS and dual constraint-generation mechanisms. |
| Graph-structure lead | Bipartite graph realizability, row/column stars | Identified generator drift and constructed the extension chain. |
| Adversarial search lead | Exact finite saturation and counterexamples | Refuted both the constant-two ceiling and arbitrary extension monotonicity. |
| Literature/novelty lead | Equivalent terminology and prior-art search | Bound the general LP and fusion frameworks to prior work; retained novelty as unresolved. |
| Formal-assurance lead | Rational receipts, independent replay, authority labels | Checked every promoted finite claim against the full compressed rule space. |

Every constructive claim was passed to the falsification and exact-verification
roles before promotion. Every failed conjecture was retained as a failure
experience with a narrower repair.

---

## 2. Object frozen for this recursion

For a graph-cover instance `G`, let `F(G)` be its relevant full semi-filters and
let `P(U)` be the legal incomparable fusion pairs on the complement ground set
`U`. Define the fractional full-cover quantity

\[
\rho_{\mathrm{frac}}(G)
=
\min\left\{
\sum_{p\in P(U)}x_p:
 x_p\ge0,
 \ \sum_{p\text{ covers }\mathcal F}x_p\ge1
 \text{ for every }\mathcal F\in F(G)
\right\}.
\]

Its dual assigns nonnegative weights `y_F` to relevant semi-filters such that

\[
\sum_{\mathcal F:p\text{ covers }\mathcal F}y_{\mathcal F}\le1
\qquad\text{for every fusion pair }p,
\]

and maximizes `sum_F y_F`.

The exact computational loop was:

1. solve a restricted fractional master LP;
2. search by 0-1 MILP for an upward-closed relevant semi-filter whose weighted
   coverage is below one;
3. add the witness and repeat;
4. rationalize the final primal/dual candidates;
5. independently check exact rational loads and use integer-scaled separation
   for global primal feasibility when equality is claimed.

This is a finite exact-discovery mechanism. It does not by itself provide an
asymptotic theorem.

---

## 3. C034a — full-union domination

### Lemma

For every legal fusion pair `(E,H)` on ground set `U`, there is a legal pair
`(E',H')` such that

\[
E'\cup H'=U,
\qquad
E'\cap H'=E\cap H,
\]

and every semi-filter covered by `(E,H)` is covered by `(E',H')`.

### Proof

Let

\[
M=U\setminus(E\cup H).
\]

Partition `M=M_E disjoint_union M_H` and define

\[
E'=E\cup M_E,
\qquad
H'=H\cup M_H.
\]

If `(E,H)` covers an upward-closed semi-filter `F`, then `E',H' in F` by
upward closure, while

\[
E'\cap H'=E\cap H\notin F.
\]

Thus the extension covers every witness covered by the original rule.
Incomparability is preserved because the old exclusive elements remain
exclusive.

It follows that both integral and fractional optima may restrict without loss
to full-union pairs.

### Computational consequence

The number of all unordered incomparable rules on an `m`-element ground set is

\[
R_m=\frac{4^m-2\cdot3^m+2^m}{2},
\]

while the full-union rule count is

\[
S_m=\frac{3^m-2^{m+1}+1}{2}.
\]

| `m` | all rules `R_m` | full-union rules `S_m` |
|---:|---:|---:|
| 8 | 26,335 | 3,025 |
| 9 | 111,645 | 9,330 |
| 10 | 465,751 | 28,501 |
| 11 | 1,921,029 | 86,526 |

**Authority:** `EXACT_DERIVED_LEMMA / NOVELTY_UNRESOLVED / ROOT_AUTHORITY_NONE`.

---

## 4. C034b — the constant-two conjecture is false

Earlier finite data through seven complement edges suggested that the C024
fractional relaxation might be universally at most two on graph-realizable
instances. Exact eight-edge search refuted that extrapolation.

Let

\[
\begin{aligned}
U_8=\{&(0,0),(1,2),(1,3),(2,2),(2,4),\\
      &(3,1),(3,3),(3,4)\}.
\end{aligned}
\]

The independently checked certificate proves

\[
\boxed{ho_{\mathrm{frac}}(U_8)=\frac{49}{24}>2.}
\]

### Exact receipt

- primal support: 21 full-union rules;
- dual support: 24 relevant semi-filters;
- exact primal and dual totals: `49/24`;
- all 26,335 original rules covered by the full-union domination reduction;
- all 3,025 full-union dual loads checked exactly;
- 12 relevant generator pairs checked by integer-scaled 0-1 MILP separation;
- minimum scaled primal coverage: 24 at denominator 24.

This changes the diagnosis of C024:

- the fractional relaxation is too weak on `NEQ`, where it collapses to a
  constant while the integral value is logarithmic;
- but it is **not** globally capped by that constant;
- it therefore remains a legitimate structural probe, although no asymptotic
  lower bound follows.

**Authority:** `EXACT_RATIONAL_FINITE_LP_CERTIFICATE / INDEPENDENT_VERIFIER / ROOT_AUTHORITY_NONE`.

---

## 5. C035–C036 — larger exact dual lower bounds

Define

\[
\begin{aligned}
U_9=\{&(0,0),(1,4),(2,2),(2,3),(3,2),\\
      &(3,4),(4,1),(4,3),(4,4)\}.
\end{aligned}
\]

An exact rational dual certificate with 15 supported semi-filters gives

\[
\boxed{ho_{\mathrm{frac}}(U_9)\ge\frac{21}{10}=2.1.}
\]

All 111,645 original fusion rules were checked exactly.

Next let

\[
U_{10}=U_9\cup\{(0,1)\}.
\]

A relevance-filtered parent-witness pool plus native child witnesses produced a
stronger rational dual:

\[
\boxed{ho_{\mathrm{frac}}(U_{10})
\ge\frac{62573}{29279}
\approx2.1371290003.}
\]

The independent verifier checked:

- all 44 dual witnesses are relevant upward-closed semi-filters;
- all 465,751 original rules;
- exact maximum rule load equal to one;
- strict improvement over `21/10` by

\[
\frac{10871}{292790}.
\]

These are global lower bounds. Equality is not claimed for `U_9` or `U_10`.

---

## 6. C037 — arbitrary complement extension is not monotone

The favorable extension chain suggested the conjecture

\[
U\subseteq U'
\quad\Longrightarrow\quad
\rho_{\mathrm{frac}}(U')\ge\rho_{\mathrm{frac}}(U).
\]

The updated RAKL counterexample-first gate was run before promoting this idea.
A complete canonical search through six complement edges found nine strict
decreases.

A smallest nondegenerate example is:

\[
U=\{(0,0),(2,1),(1,2),(2,2)\},
\]

and

\[
U'=U\cup\{(1,1)\}.
\]

Both associated graphs are nonempty, but exact primal-dual receipts give

\[
\boxed{ho_{\mathrm{frac}}(U)=\frac32,
\qquad
\rho_{\mathrm{frac}}(U')=1.}
\]

The strict drop is `1/2`.

### Mechanism of failure

Adding an incident complement edge changes an old row star and/or column star.
A cylinder-lifted old semi-filter can cease to contain any relevant new
generator pair. In the counterexample, only two of the three parent dual
witnesses remain relevant after lifting.

**Authority:** `EXACT_RATIONAL_FINITE_COUNTEREXAMPLE / INDEPENDENT_VERIFIER / ROOT_AUTHORITY_NONE`.

---

## 7. C038 — the correct witness-persistence transfer theorem

The failed monotonicity conjecture was repaired at the exact level where it
breaks.

Let the old ground set be `U`, the new ground set be `U' superset U`, and define
the cylinder lift of an old semi-filter `F` by

\[
\widehat F=\{S'\subseteq U':S'\cap U\in F\}.
\]

### Transfer lemma

Let `y_F` be any feasible dual solution in the old instance. If every
`widehat F` in its support is relevant in the new instance, then the same
weights on the lifted witnesses are dual-feasible in the new instance.
Therefore

\[
\rho_{\mathrm{frac}}(\text{new})
\ge
\sum_F y_F.
\]

### Proof

For a new pair `(E',H')`, let

\[
E=E'\cap U,
\qquad
H=H'\cap U.
\]

Cylinder membership gives

\[
E'\in\widehat F\iff E\in F,
\qquad
H'\in\widehat F\iff H\in F,
\]

and

\[
E'\cap H'\in\widehat F
\iff
E\cap H\in F.
\]

Thus the new pair covers `widehat F` exactly when its projection covers `F`.
If this occurs, the projected pair is automatically nonempty and incomparable;
otherwise its intersection would equal one of its members and belong to `F`.
Every new rule load is therefore an old legal rule load, or zero, and is at
most one.

### Corollary

Adding a complement edge on a fresh row and fresh column leaves all old row and
column stars unchanged, so every old relevant semi-filter has a relevant
cylinder lift. Fractional cover complexity is nondecreasing under that
restricted extension.

### Regression checks

- C037 decreasing extension: only `2/3` old dual witnesses persist;
- `U_8 -> U_9`: all `24/24` exact parent dual witnesses persist;
- `U_9 -> U_10`: all `15/15` supported parent witnesses persist;
- `U_10 -> U_11` below: all `44/44` supported parent witnesses persist.

**Authority:** `EXACT_DERIVED_TRANSFER_LEMMA / FINITE_REGRESSION_CHECKS / NOVELTY_UNRESOLVED / ROOT_AUTHORITY_NONE`.

---

## 8. C039–C040 — a three-step certified amplification chain

The eight-edge graph embeds into the nine-edge graph by the row map

```text
0 -> 0
1 -> 2
2 -> 3
3 -> 4
```

with columns fixed, followed by adding `(1,4)`.

Then

\[
U_{10}=U_9\cup\{(0,1)\}.
\]

For the next step, a complete tournament over all 15 unused internal positions
in the `5 x 5` ambient matrix found that only `(1,0)` preserved all 44 witnesses
in the certified `U_10` dual. Set

\[
U_{11}=U_{10}\cup\{(1,0)\}.
\]

The small witness pool transferred the parent lower bound but produced no new
mass. Expanding to 516 relevant witnesses made a direct 86,526-constraint dual
LP stall. This was treated as a solver-representation failure, not a
mathematical failure.

A dual constraint-generation repair started with a small set of rule
constraints, repeatedly added every violated rule, and terminated after four
rounds. Rationalization and an independent exact verifier produced

\[
\boxed{ho_{\mathrm{frac}}(U_{11})
\ge
\frac{917741}{428806}
\approx2.1402242506.}
\]

The exact strict increment over the `U_10` certificate is

\[
\frac{38860901}{12555010874}>0.
\]

The verifier checked all 86,526 full-union rules exactly. By C034a, these
represent and dominate all 1,921,029 original rules.

### Certified sequence

\[
\frac{49}{24}
<
\frac{21}{10}
<
\frac{62573}{29279}
<
\frac{917741}{428806}.
\]

The successive certified increments are

\[
\frac{7}{120},
\qquad
\frac{10871}{292790},
\qquad
\frac{38860901}{12555010874}.
\]

This is a finite chain of strict lower-bound amplification, not a proof that
the sequence continues indefinitely.

**Authority:** `EXACT_FINITE_CERTIFICATE_CHAIN / NO_ASYMPTOTIC_CLAIM / ROOT_AUTHORITY_NONE`.

---

## 9. Failure learning retained in the lattice

| Failure | What failed | Atomic lesson | Repair |
|---|---|---|---|
| `F-C034-PROCESS-GATE-DELAY` | Exploration started before updated schema artifacts were materialized | Truth receipts and process-compliance claims are separate | C037 and C040 were restarted with frozen pre-candidate context, memory, and hash-chained traces |
| `F-C034-FINITE-OVERGENERALIZATION` | `rho_frac <= 2` extrapolated from all instances through seven edges | Small finite saturation does not establish a universal ceiling | Exact eight-edge search and counterexample preservation |
| `F-C036-GENERATOR-DRIFT` | Old witnesses were lifted without rechecking relevance | Ground-set inclusion does not preserve graph-generated constraints | C038 witness-support persistence theorem |
| `F-C037-ARBITRARY-EXTENSION-NONMONOTONE` | Raw one-edge extension monotonicity | Incident additions can remove old LP constraints | Separate persistence from augmentation |
| `F-C035-BATCH-WORKER-HANG` | One degenerate solver worker blocked a batch | Missing outputs are not negative mathematical results | Per-instance checkpoints and sequential fallback |
| `F-C040-FULL-DUAL-LP-STALL` | Direct 516-by-86,526 dual LP stalled | Solver representation can be the bottleneck | Exact-equivalent rule-constraint generation converged in four rounds |

The central conceptual correction is:

> A recursive amplification step has two independent obligations: preserve the
> old certified dual support, and create additional feasible dual mass.

C038 solves the first obligation conditionally. C039–C040 give three finite
examples of the second. A uniform recurrence remains open.

---

## 10. Prior-art boundary

The general fusion/full-cover definitions and their circuit-lower-bound
transference are due to Cavalar and Oliveira. Fractional covering LPs and their
dual use in communication complexity are established methodology, notably in
Karchmer, Kushilevitz, and Nisan.

Targeted searches under fusion-pair, semi-filter, cylinder-lift, full-union,
rule-domination, and graph-extension vocabulary did not locate the exact C034
full-union lemma, the C037 monotonicity counterexample, or the C038
witness-persistence specialization. A negative search is not a novelty proof.
Every such item remains `NOVELTY_UNRESOLVED` pending broader expert review.

---

## 11. Exact root impact

The present results establish that the C024 fractional successor has more
structure than its `NEQ` failure suggested. They provide:

- a strict rule-space compression theorem;
- an exact graph-realizable value above two;
- an exact conditional transfer theorem;
- a three-step explicit chain of strictly improving rational lower-bound
  certificates;
- a precise explanation of why arbitrary graph extension can fail.

They do **not** establish:

- that `rho_frac` is unbounded;
- a super-logarithmic full-cover lower bound;
- a relation bounding integral cover complexity strongly enough for the root;
- an explicit NP language of superpolynomial circuit complexity;
- `P != NP` or `P = NP`.

The active strict residual is now:

\[
\boxed{
\text{Construct a uniform relevance-preserving graph extension and prove a
positive cumulative dual-mass recurrence for arbitrarily many steps, or prove
an obstruction to such recurrence.}
}
\]

The root remains

```text
OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE
```

---

## 12. Main reproducibility artifacts

### Exact mathematical statements

- `C034_full_union_domination.md`
- `C038_witness_persistence_transfer.md`
- `C039_fractional_amplification_chain.md`

### Exact certificates and independent receipts

- `C034_exact_optimum_m8_type111_fullunion.json`
- `verify_c034_exact_optimum.py`
- `verify_c034_exact_optimum_receipt.json`
- `C035_m9_type19_21over10_dual.json`
- `verify_c035_m9_21over10.py`
- `verify_c035_m9_21over10_receipt.json`
- `C036_child06_exact_improvement.json`
- `verify_c036_child06.py`
- `verify_c036_child06_receipt.json`
- `C037_monotonicity_counterexample.json`
- `verify_c037_monotonicity.py`
- `verify_c037_monotonicity_receipt.json`
- `C040_child_exact_improvement.json`
- `verify_c040_child.py`
- `verify_c040_child_receipt.json`

### RAKL process and memory

- `C037_MATH_CONTEXT_FIBER_20260811.json`
- `C037_RESEARCH_MEMORY_REVIEW_20260811.json`
- `C037_RESEARCH_TRACE_20260811.json`
- `C040_MATH_CONTEXT_FIBER_20260811.json`
- `C040_RESEARCH_MEMORY_REVIEW_20260811.json`
- `C040_RESEARCH_TRACE_20260811.json`
- `RAKL_PvsNP_failure_lattice_C034_C040.json`
- `RAKL_PvsNP_DAG_delta_C034_C040.yaml`
