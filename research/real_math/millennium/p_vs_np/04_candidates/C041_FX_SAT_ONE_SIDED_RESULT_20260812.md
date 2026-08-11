# C041-FX-SAT-ONE-SIDED-v1 — exact first-gate result

**Frozen candidate commit:** `4627ae32e2d3660a86cc12d327592577adc25e5f`  
**Receipt:** `05_falsification/C041_FX_SAT_EXACT_GATE_RECEIPT_20260812.json`  
**Root status:** `OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`

## Exact mathematical result

Order the child complement as

\[
u_0=(0,0),\quad u_1=(0,4),\quad u_2=(1,2),\quad
u_3=(2,1),\quad u_4=(2,2).
\]

The frozen (n=2\to3) rule adds exactly (u_1=(0,4)).

### 1. The square seed is re-certified

The (3\times3) C037 parent and its embedding into the (4\times4) square
have the same 19 relevant semi-filters.  The old exact primal and dual
certificates remain feasible with common value

\[
\rho_{\mathrm{frac}}(U_2)=\frac32.
\]

This verifies the empty-fibre lemma on the registered seed: graph edges using
the added empty-star row or column cannot create a relevance witness, while
all old witnesses remain.

### 2. Relevance persistence succeeds

All three positive-weight parent dual supports have relevant cylinder lifts in
the child.  Every child full-union pair has lifted load at most one, with exact
maximum one.  Thus the frozen instance satisfies the C038 transfer premises;
the old mass (3/2) remains feasible.

### 3. Fresh augmentation is exactly zero

With the lifted parent mass fixed, the complete child residual LP contains 787
relevant semi-filters.  Its exact optimum is

\[
\boxed{\delta_2^*=0}.
\]

The zero certificate has a short mathematical description.  The two saturated
full-union pairs

\[
\begin{aligned}
p_1&=(\{u_0,u_1\},\{u_2,u_3,u_4\}),\\
p_2&=(\{u_0,u_2\},\{u_1,u_3,u_4\})
\end{aligned}
\]

each have residual capacity zero under the lifted parent dual, and together
cover every one of the 787 child-relevant semi-filters.  Assigning residual
dual weight one to each gives objective zero.  Since the residual packing is
nonnegative and (z=0) is feasible, primal and dual values coincide at zero.

The exact branch is therefore `ZERO_AUGMENTATION`.

## Correct polarity

This result **does refute** positive additive augmentation at the frozen first
step while retaining the exact lifted parent weights.

It **does not prove** that the reoptimized child optimum equals (3/2), that a
later magic-coded step has zero augmentation, that the whole family has bounded
fractional complexity, or that the proposed NP-completeness lemma fails.  The
small gate exercises the all-zero short code and has no asymptotic authority.

The mathematical lesson is sharper than a software or solver observation:

> Relevance preservation and lifted feasibility do not create residual dual
> capacity.  A small family of already saturated legal pairs can cover the
> entire child relevance class, forcing every nonnegative fresh coordinate to
> zero.

The next mathematical discriminator is a first-magic-level symbolic attack:
search for a bounded quotient, one-sided multiplexing cover, or compiled
intersection cover before any larger LP.  Changing the short code after seeing
this zero would be post-result rescue and is forbidden.

## Hostile-review repair of the language bridge

Same-context hostile review found a separate mathematical defect in the frozen
helper algorithms: a gamma-coded formula may declare exponentially many unused
variables, so the displayed full assignment is not polynomially balanced and
enumeration over all declared variables is not (2^{O(n)}).  That failure is
preserved as `F-C041-DECLARED-VARIABLE-WITNESS-BLOWUP`.

`C041_FX_SAT_SPARSE_BRIDGE_REPAIR_20260812.md` replaces only the proof
algorithm, not the decoder or language.  Satisfiability depends solely on the
variables occurring in literal slots.  Restriction of a full satisfying
assignment to this support and arbitrary extension of a sparse satisfying
assignment prove extensional equivalence.  The support has size (O(n)) on
canonical inputs and size one on either fixed fallback.  A follow-up hostile
pass accepts the repaired polynomial NP verifier, the (2^{O(n)}) complement
decider, and the correctly directed linear-overhead reduction
(3\mathrm{SAT}\le_m^p L_G).  Thus the narrowly defined associated graph
language is NP-complete.

This closes only the language-coordinate bridge.  It does not change
\(\delta_2^*=0\), prove any later increment, or supply a circuit lower bound.
Both reviews are internal same-context mathematical review, not independent
peer review.
