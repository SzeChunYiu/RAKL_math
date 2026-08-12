# C046R fallback-aware four-pair repair

**Authority:** `PROPOSAL_SHADOW_RETROSPECTIVE_VERIFICATION_ONLY`  
**Framework:** `SzeChunYiu/RAKL@43897d3afaf0038385102d5acc64793c05ec40f0`, method `3.0.0`  
**Application base:** `RAKL_math@ec8a9eb5eeedaaf1d3f497a8688384256a2079e0`  
**Frozen actual fibre:** `sha256:4359003a6565cd8db6934f404f8380b5a07b2233d64c381464da245ea71c2c70`  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`

## Scope and source binding

This cycle resolves only the local residual opened by PR #243: whether the exact all-zero decoder fallback edge at G17 destroys the four-pair upper-cover witness claimed in C045. The cover semantics remain bound to Cavalar--Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (18 March 2025), Definitions 18--21 and Theorem 22. In particular, a semi-filter is upward closed and excludes the empty set; being above a graph cell forces its row/column generator traces into the semi-filter; and a disjoint pair `(E,H)` covers such a cell whenever the two generator traces are contained on opposite sides, because preservation would force the empty intersection into the semi-filter. The primary source is the official ECCC report/PDF; the repository-local pinned source was previously recorded at blob `8dfe370a6bf687eb33ebf52eaaf9308e1bdf0230`.

The frozen application decoder is `04_candidates/C041_fx_sat_one_sided.py`, blob `fcc4814dd618da96ef9bb8144a4783a0a6e886e1`. PR #243 correctly observes that the full G17 complement contains the fallback edge

`f = (0,65536)`

in addition to the embedded U16 and the ten canonical length-32 MAGIC UNSAT edges classified in C045. Thus C045's full row-projection-disjointness statement is false as written. The question here is whether its numerical upper bound can nevertheless be repaired.

## Inputs from the prior exact witnesses

Let `U_o=U16`, let `U_m` be the ten canonical MAGIC complement edges listed in C045, and let `f` be the singleton fallback edge. Thus

`U17 = U_o disjoint_union U_m disjoint_union {f}`

as edge ground sets, although their row projections are not disjoint because `f` shares row 0 with `U_o`.

C044 supplies three disjoint pairs `(E^o_j,H^o_j)`, `j=1,2,3`, lifting its exact G16 quotient witness. Its nonempty old row-star signatures are

`0:EEE, 1:EHE, 2:EHX, 4:EEH, 5:HEE, 6:HEH, 7:HHH`,

where quotient labels represent the exact old twin classes. In particular row 0 is contained in the E side at all three coordinates, while every other active old row class has at least one H coordinate.

C045 supplies three disjoint pairs `(E^m_j,H^m_j)` on the ten-edge MAGIC block. These remain correct as a local subblock witness; PR #243 does not invalidate that classification or code.

## The repaired four pairs

For `j=1,2,3`, define

`E_j = E^o_j union E^m_j union {f}`,

`H_j = H^o_j union H^m_j`.

Define the fourth pair by

`E_4 = U_o union {f}`,

`H_4 = U_m`.

Each pair is disjoint. For the first three pairs, old and MAGIC grounds are disjoint, the local pair sides are disjoint, and `f` is placed only on the E side. The fourth pair is disjoint because `U_o`, `U_m`, and `{f}` are disjoint edge sets.

## Proof that every relevant G17 graph cell is covered

It is enough to consider cells whose row and column complement traces are both nonempty. If either trace is empty, Definition 19 would force the empty set into any semi-filter above the cell, contradicting Definition 18, so no above semi-filter exists.

### 1. Old-old relevant cells

For an old active row other than row 0, neither its row trace nor any old column trace contains `f`; its C044 separating coordinate therefore survives unchanged among pairs 1--3.

For row 0, the row trace changes from its old trace `S_0` to `S_0 union {f}`. C044 gives row 0 signature `EEE`, so `S_0 subseteq E^o_j` for all `j=1,2,3`. Since `f` was also put into every `E_j`, the enlarged row-zero trace remains E-contained in all three coordinates. Old column traces are unchanged. Therefore every old row-zero graph cell keeps the same C044 separating coordinate it had before the fallback edge was added.

### 2. MAGIC-MAGIC relevant cells

The fallback edge uses row 0 and fresh column 65536, neither of which is a canonical MAGIC endpoint in the ten-edge block. Consequently every MAGIC row and MAGIC column trace is unchanged. C045's local three-pair code therefore continues to separate every relevant graph cell internal to the MAGIC endpoint sets.

### 3. Old-MAGIC and MAGIC-old cross cells

Every nonempty old trace is contained in `E_4=U_o union {f}`; this includes the enlarged row-zero trace. Every MAGIC trace is contained in `H_4=U_m`. Hence pair 4 separates every relevant old/MAGIC cross cell in either orientation.

### 4. Cells incident to the fallback column

The complement trace of fresh column 65536 is exactly `{f}`, which is contained in `E_j` for all `j=1,2,3` and in `E_4`.

For a MAGIC row, its trace lies in `U_m=H_4`, so pair 4 separates the cell.

For old row 0 the cell `(0,65536)` is `f` itself and is not a graph cell.

For any other active old row class, C044's signature list shows at least one coordinate `j` with signature H. Its entire row trace is therefore contained in `H_j`, while the fallback-column trace `{f}` is contained in `E_j`. That coordinate separates the cell.

These cases exhaust all relevant cells. Hence the four displayed disjoint pairs generator-separate every semi-filter that can be above a G17 graph cell.

## Theorem — repaired finite upper bound

Under the exact frozen C041 recursion and the C043--C045 local witness facts,

`rho(G17,G_131072,131072) <= sigma(G17) <= 4`.

The fallback correction therefore invalidates C045's *block-separability proof*, but it does **not** invalidate the four-pair upper bound itself. The upper bound survives by a different gluing argument: the bridge edge is absorbed into the EEE codeword of the old row-zero star and into the old side of the block separator.

A bounded quotient-cell enumeration of the exact 10-cell old quotient, the ten MAGIC edges, and `f` checked all `15 x 14 - 21 = 189` active non-complement cells and found a separating coordinate among the four proposed pairs for every one. This is a falsification/calibration check only; the preceding case proof is the mathematical argument.

## Episode -> diagnosis -> reusable obstruction/lesson

**Episode outcome.** `SOLVED_LOCAL_UPPER_COVER_REPAIR`: the reopened G17 four-pair upper bound is restored with full fallback support included.

**Diagnosis.** The PR #243 correction exposed a genuine representation/gluing defect in C045, but the missing bridge edge is non-load-bearing for this particular cover code. The local mathematical correction was real; the downstream numerical inequality happened to survive through a different witness.

**Reusable obstruction/lesson proposal.** A cross-component complement edge is not by itself evidence of coercive cover growth. A singleton bridge can be zero-cost absorbable when its old endpoint star is monochromatic across the inherited local coordinates, the new singleton column can be given the same codeword, and the block separator can place the bridge on that old side. To force new cover resources, a later coupling must be **code-incompatible**, not merely incidence-coupled.

This lesson is proposal/shadow only. It does not claim every fallback edge at later levels is absorbable, and it does not promote a framework rule.

## Local versus gluing residuals

The local G17 upper-cover residual is closed. The following remain open and are not conflated with it:

- no uniform theorem that all future fallback edges are cover-neutral;
- no lower bound on `rho(G17)` or on any later `rho(G_n)`;
- no recurrence forcing cover growth;
- no circuit-size lower bound;
- no bridge to `SAT notin P/poly` or `P != NP`;
- no independent mathematical review (`0/3`).

C046 separately proves that canonical MAGIC prefix rows stay in the high half while all complement rows of the frozen one-sided recursion stay in the low half. Combining that negative history with the present G17 repair makes further same-family searches for a *canonical* row-collision a saturated route. The next research action should rotate to a different support/operator family rather than scan later levels for the forbidden canonical collision. Any such operator change must first preserve the exact NP-language/reduction contract and be tested against C041A zero-augmentation, C041B tight-intersection absorption, C043 twin ceilings, and C044 multiplexing.

## Novelty and authority

The solved local subproblem is defensibly `compositional` with a `representation` secondary class: it composes the C044 and C045 codes with a new fallback assignment and corrected gluing case split. Protected retained novelty is zero on all seven RAKL axes until protected gates authorize otherwise. Same-context expert review is not independent review. Root status remains `OPEN_NO_SOLUTION_CERTIFICATE`.
