# YM-S1c1a1 — Section-9 terminal-anchor / AF–IR transfer audit (R8)

**Authority:** `PROPOSAL_SHADOW_SOURCE_AUDIT / RETROSPECTIVE_R8_FINDING / NO_THEOREM_PROMOTION / ROOT_AUTHORITY_NONE`  
**Root:** `RAKL_math#5`, `OPEN_NO_SOLUTION_CERTIFICATE`  
**Parent repair:** `#166 / YM-S1c1a`  
**Successor repair:** `#171 / YM-S1c1a1`  
**Framework source of truth at freeze:** `SzeChunYiu/RAKL@bb30835f41dd5e02a427c3e53be6914732d66fd2`, method `3.0.0`, package `0.1.0`, constitution epoch `v3-authority-hardening-20260811`  
**Application base:** `b36058f8a90efe7d377df45feed15d4ec91e042c`, tree `4c3d416d6dd8e3feeb6311a8f845adb1ec68c2f1`  
**Fibre hash:** `72b95bbc806d50a55d0e2fb34aec7600f3e0b98442edba2738f861c587f49f14`

The active question was already prospectively named in issue #166: test Section 9 Theorems 9.3/9.4 as a *typed* repair candidate for the Section-10 AF/IR continuum-identification residual. The R8-specific durable fibre was persisted after the source observation, so the findings below remain retrospective within this R8 receipt. Issue #171 freezes only the successor repair and receives no backfilled discovery credit.

Primary mathematical source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026), especially Section 9, Theorems 9.3–9.4, equations (9.28)–(9.43). Publisher metadata: DOI `10.1002/prop.70097`. Parsed PDF text was available. Mandatory visual screenshot attempts for document pages 101–103 returned backend `Cache miss`; visual-page verification is therefore `CANNOT_CHECK`, not silently passed.

## 1. Theorem 9.3 drops the terminal comparison term

Theorem 9.3 states a scheme-universality bound of the form

`|S_k^A-S_k^B| <= C sum_{ell>=k} a_ell d(A,B)`,

where `a_ell=a_0 b^{-ell}`, and concludes that the difference vanishes as `k->infinity`.

Its proof defines increments

`Delta_ell^A = S_ell^A-S_{ell+1}^A`,

and obtains the one-step difference estimate

`|Delta_ell^A-Delta_ell^B| <= C# a_ell d(A,B)`  (9.33).

It then writes the exact telescoping identities (9.34)

`S_k^A = lim_{K->infinity}(S_K^A + sum_{ell=k}^{K-1} Delta_ell^A)`,

and similarly for `B`. When the two identities are subtracted, however, displayed equation (9.35) bounds `|S_k^A-S_k^B|` only by the increment-difference sum. The terminal comparison `S_K^A-S_K^B` has disappeared.

The direct algebra gives instead

`|S_k^A-S_k^B| <= limsup_{K->infinity}|S_K^A-S_K^B| + sum_{ell>=k}|Delta_ell^A-Delta_ell^B|`.

Thus summability of increment differences controls relative *drift across scales* but does not, by itself, fix the additive terminal offset between two schemes. A separate UV terminal anchor, common reference limit, or equivalent condition is required before (9.28) follows from the displayed telescope.

### Exact hostile control

Let `a_ell>0` be summable and set

`B_k = sum_{ell>=k} a_ell`,  
`A_k = 1 + sum_{ell>=k} a_ell`.

Then `Delta_ell^A=Delta_ell^B=a_ell`, so every increment-difference bound holds with zero right-hand side, yet `A_k-B_k=1` for every `k`. This falsifies only the generic inference “summable/equal increments imply equal terminal-normalized sequences.” It is not a Yang–Mills countermodel.

**Scoped source-proof result:** `THEOREM_9_3_DISPLAYED_TELESCOPE_OMITS_TERMINAL_ANCHOR_TERM`.

This is not a proof that the theorem is false: an earlier or separately proved boundary condition could repair it. The current bounded audit did not infer such a condition from intent.

## 2. Theorem 9.4 is conditional uniqueness, not an automatic terminal-anchor repair

Theorem 9.4 has a correct-looking fixed-scale uniqueness shape: at one scale, equality of the one-slice marginal and equality of the Markov kernel on a local core imply equality of the corresponding OS path measures. For the continuum statement it assumes, for every admissible scheme, weak convergence to a common slice marginal `rho` and strong convergence (after identification) to a common semigroup `T(·)` uniformly on compact physical-time intervals.

The proof then explicitly concludes scheme independence because both limiting objects `rho` and `T(·)` are independent of the scheme **by hypothesis**.

Accordingly, Theorem 9.4 can establish uniqueness *given* common limiting Markov data. It does not by itself derive the missing claim that the AF and IR constructions have the same limiting marginal and semigroup. Using it as a repair for Section 10 therefore requires a separate same-theory convergence theorem that supplies those common objects without circular dependence on Theorem 9.3's omitted terminal anchor.

**Scoped source/gluing result:** `THEOREM_9_4_CONDITIONAL_COMMON_LIMIT_UNIQUENESS_DOES_NOT_DERIVE_AF_IR_COMMON_LIMIT`.

## 3. DifferenceWitness: regulator/blocking scheme parameters are not automatically running RG trajectories

Section 9 varies admissible regulator/blocking/counterterm parameters `(alpha,beta)` with a fixed scheme metric `d`. The Section-10 residual compares different running RG trajectories/states, including couplings and irrelevant polymer data `(g_k,K_k)` generated from different entry constructions. The common abstraction is “two scale-indexed constructions whose continuum limits are claimed identical,” but the non-preserved structure is load-bearing:

- a static admissible scheme parameter is not the same object as a running coupling/state;
- Section-9 one-scale Lipschitz constants are indexed by the scheme metric, while Section 10 needs a vanishing comparison between trajectory states;
- the OS one-slice marginals, quotient/Hilbert spaces, time normalization and continuum subsequence must be the same objects on both sides;
- gauge invariance/reflection positivity cannot be replaced by an untyped gauge-fixed or regulator-dependent surrogate.

A valid transfer must therefore exhibit explicit embeddings of the AF and IR constructions into the Section-9 admissible class and prove the needed constants/uniformity. Merely citing “universality” is not a typed bridge.

## 4. Same-context expert cell

1. **Constructive QFT / OS reconstruction:** Theorem 9.4 is useful only after common limiting `rho,T` are established on the same gauge-invariant OS source algebra/quotient. It cannot create those common data from a scheme label.
2. **Rigorous RG / renormalization:** The Section-9 scheme coordinates and Section-10 running trajectories need an explicit map. The previous `O(g_k^2)` harmonic-tail problem is not removed by re-labelling trajectory differences as scheme differences.
3. **Functional analysis / probability:** subtracting two telescoping identities necessarily retains the terminal boundary term. Conditional Markov uniqueness is distinct from convergence/equality of the data being glued.
4. **Gauge/physical-state specialist:** any terminal anchor must live in the same gauge-invariant Euclidean/OS theory and preserve reflection positivity, physical time, continuum subsequence, and state-space/null-quotient identity.
5. **Adversarial verifier:** the constant-offset/equal-increment control is an exact minimal falsifier of the missing step; it does not overreach to a Yang–Mills no-go statement.
6. **RAKL v3 assurance/metrology:** episode -> diagnosis -> successor obstruction/control remains separated; all records are proposal/shadow; same-context review earns zero independent-review credit.

## 5. Episode -> diagnosis -> obstruction/lesson separation

- **Episode:** `EP-YM-S1c1a1-R8-20260811`, bounded Section-9 repair-surface audit.
- **Diagnosis:** Theorem 9.3's displayed telescope omits the terminal comparison term, while Theorem 9.4 assumes the common limiting marginal/semigroup needed for scheme-independent continuum uniqueness.
- **Successor obstruction/control:** issue #171 freezes the prospective terminal-anchor + AF/IR typing obligation. It is application control, not a protected v3 obstruction promotion.
- **Reusable lesson:** none promoted. The proposal-only mathematical lesson is that summable differences of increments do not determine an additive terminal offset without an anchor.

Local mathematical failure: **NONE** — the elementary telescope and hostile control verify.  
Local source-proof failure: **YES** — the displayed proof of (9.28) omits the terminal term.  
Local-to-global/same-theory gluing failure: **YES** — Section 9 as written does not yet identify the AF and IR limiting theories.  
Representation/transfer failure: **YES** — scheme parameters and running RG trajectory data lack a typed applicability map.  
Retrieval failure: **NO** for parsed text.  
Visual verification/tooling: **CANNOT_CHECK** — mandatory PDF screenshots returned cache misses.

## 6. Novelty classification and saturation

The solved abstract subproblem (“what follows from the two telescoping identities plus an `l1` increment-difference bound?”) uses only standard algebra/triangle inequality and a finite exact hostile control. Under current RAKL v3 taxonomy it is defensibly **`RAKL_TRIVIAL`** if treated as a verified local subproblem; this classification grants no theorem novelty or root authority.

Proposal/shadow retained semantic deltas for this cycle are conservatively `KNOWLEDGE=1, OPERATOR=0, EXPERIENCE_PATTERN=0, OBSTRUCTION=1, RELATION=1, PATH=1, META_METHOD=0`. Raw issue/file/commit growth is not counted as learning. `KNOWLEDGE/OBSTRUCTION/RELATION/PATH` are reopened by the new terminal-anchor residual; no axis is declared globally saturated from one round.

## 7. Residual / next action

Outcome:

`PARTIAL_SUCCESS__SECTION9_TYPED_REPAIR_TESTED__THEOREM9_3_TERMINAL_TERM_MISSING__THEOREM9_4_COMMON_LIMIT_IS_HYPOTHESIS__AFIR_SAME_THEORY_GLUE_STILL_OPEN`

Residual:

`RES-YM-S1c1a1-TERMINAL-ANCHOR-OR-COMMON-LIMIT-PLUS-AFIR-TYPED-EMBEDDING`.

Next action under #171: seek a primary-source or fully proved terminal normalization/reference-scheme theorem that makes `lim_K|S_K^A-S_K^B|=0` (or an equivalent anchored comparison) legitimate, and simultaneously type the AF/IR trajectories into the same admissible OS/Markov data. If that cannot be bound, rotate to a direct stable-manifold/inter-trajectory convergence theorem rather than repeating the Section-9 increment calculation.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical reviews remain `0`; no formal/verifier/dependency/axiom/root promotion gate is claimed closed.