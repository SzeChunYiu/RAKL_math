# C042 activation-threshold and quotient gate — pre-output freeze

**Parent:** `C041-FX-SAT-ONE-SIDED-v1`  
**Status:** same-context mathematical proposal frozen before executable gate output  
**Root:** `OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`

## Object and QoI

For the frozen decoder, distinguish three events for an even cross word:

1. the eight-bit MAGIC prefix fits;
2. a canonical long-form 3CNF parses;
3. a canonical long-form UNSAT 3CNF exists.

The quantity of interest is the first parent level (n) at which each event
can affect (U_{n+1}), followed by the exact row/column twin quotient and a
source-valid upper cover of the first syntax child (G_9) and first
UNSAT-capable child (G_{13}).

## Frozen proposed theorem

Let

\[
g(t)=2\lfloor\log_2t\rfloor+1,
\quad w(v)=\lfloor\log_2v\rfloor+1,
\]

and let the unpadded canonical length be

\[
L_0(v,m)=8+g(v)+g(m)+3m(1+w(v)).
\]

The even canonical length is (L=L_0+(L_0\bmod2)).

The predictions frozen for falsification are:

- MAGIC first fits at length 8 ((n=4)) but cannot parse a formula;
- canonical syntax first occurs at length 16 ((n=8)), exactly for
  ((v,m)=(1,1)), and every such formula is SAT;
- canonical UNSAT first occurs at length 24 ((n=12)), exactly for
  ((v,m)=(1,2));
- the two ordered minimum UNSAT words encode the opposing one-variable
  clauses in the two possible orders;
- the all-zero contradiction is a separate fixed fallback and is never counted
  as magic-coded semantic activation.

## Frozen structural predictions

Write (W_n\subseteq[2^n]^2) for UNSAT cross words.

- (W_n=\{(0,0)\}) for (2\le n\le11).
- (W_{12}=\{(0,0),(3674,1407),(3674,4053)\}).
- (U_9) has four row and four column twin types and is a blow-up of the
  four-edge seed quotient.
- (U_{13}) has five row and five column twin types and is a blow-up of a
  five-edge quotient.

The exact quotient full-cover numbers are deliberately left **unknown before
execution**.  The evaluator may return a finite integer upper bound through
the C013 quotient-lift theorem or `CANNOT_CHECK`.  No finite outcome supplies a
uniform quotient bound.

## Proof obligations and controls

1. Prove the length-24 lower bound from the necessity (m\ge2) for UNSAT.
2. Classify every equality case and preserve formula-order multiplicity.
3. Verify exact cross-word polarity (`UNSAT` enters (U), `SAT` remains in
   (G)).
4. Build row and column types from exact complement neighborhoods.
5. Prove the full graph is a blow-up of the displayed quotient before lifting
   an upper cover.
6. Keep `rho <= D_intersection` and quotient-lift arrows in the upper-bound
   direction.
7. Preserve the C024 fractional-correlation warning and the C041 fixed-lift
   zero result; neither is an asymptotic upper bound.

Allowed branches are `PREFIX_ONLY_NO_SEMANTIC_SIGNAL`,
`SYNTAX_ONLY_ALL_SAT`, `FIRST_UNSAT_COMPRESSED`,
`FINITE_QUOTIENT_UPPER_BOUND`, `PROPOSED_THRESHOLD_REFUTED`, and
`CANNOT_CHECK`.

The method lesson under evaluation is mathematical: a parser or representation
can activate strictly before it can express the obstruction relevant to the
proof.  Software execution, hashes, CI, and runtime receive zero saturation
credit.
