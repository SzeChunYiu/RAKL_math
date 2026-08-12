# YM-C1a R12 — continuum tightness / Hilbert compactness source audit

**Authority:** proposal/shadow source audit only. No Yang–Mills theorem, root promotion, protected lesson/obstruction, novelty promotion, or independent-review credit.

**Root:** #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Child:** #220 (`YM-C1a-CONTINUUM-TIGHTNESS-HILBERT-COMPACTNESS-COVARIANCE-REALIZATION-SAME-OS-SOURCE`)  
**Primary source:** Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 Jun 2026).

## Chronology boundary

The load-bearing compactness/realization observations below were made before issue #220 and the durable R12 fibre were written. They therefore receive **zero strict prospective-discovery credit**. After the fibre freeze, only the registered source-repair action was executed: bounded same-primary-source searches for an explicit compact-embedding / Rellich / Minlos / nuclear-space / compact-containment repair and citation tracing for the source-named Mitoma route. Current RAKL invention-last routing remains `CANNOT_CHECK`; no new mathematical repair candidate is promoted.

## Observation A — bounded second moments do not imply tightness in the same infinite-dimensional Hilbert space

The embedded companion Theorem 3.7 (PDF pp. 477–478) states tightness of `Law(iota_k[O])` on `H^{-s}(T^4)` and says:

> “By Lemma 3.5, the laws have uniformly bounded second moments, which implies tightness of each marginal…”

The implication is false in an infinite-dimensional Hilbert space without an additional compact-containment mechanism. Let `H = ell^2` and let `X_k=e_k` deterministically for an orthonormal sequence. Then `E||X_k||^2=1` for all `k`, but `{delta_{e_k}}` is not tight: for any `epsilon<1`, a compact set carrying at least `1-epsilon` mass for every `delta_{e_k}` would have to contain every `e_k`, impossible because `{e_k}` has no convergent subsequence.

The same logical step appears in Appendix Theorem A.2 on `H^{-r}(R^4)`: equation (A.18) controls probability outside a norm ball and immediately concludes tightness in the same Hilbert space. Norm balls are not compact in an infinite-dimensional Hilbert space, so this conclusion does not follow from the displayed estimate.

**Scoped conclusion:** the displayed Hilbert-space Prokhorov arguments do not establish the claimed tightness. This is not a proof that the Yang–Mills field family is non-tight; a stronger-space compact embedding, weighted/local compactness, or a valid nuclear-space route could repair the extraction.

## Observation B — covariance operator norm is conflated with the mean-square Hilbert norm / trace

Main §7.1 derives a bounded covariance bilinear form for smeared fields from exponential clustering, then says that taking a supremum over unit `H^s` tests gives

`sup_k E ||iota_k[O]||_{H^{-s}}^2 < infinity`  (7.4).

That inference interchanges a supremum and expectation. For an `H`-valued random vector `Y` with covariance `Q`,

`sup_{||g||=1} E |<Y,g>|^2 = ||Q||_op`,

while

`E||Y||^2 = Tr(Q)`

when the latter is finite. These are not equal in general. Even in `R^2`, if `Y=e_1` or `e_2` with probability `1/2`, then `E||Y||^2=1` while the unit-vector supremum is `1/2`.

Appendix (A.16)–(A.17) makes the same issue explicit. From

`E|<X_k,J^{-r}g>|^2 <= C_2 ||g||_2^2`

it invokes “Riesz representation in the Bochner space” to produce `Y_k in L^2(Omega;L^2)` and writes

`E||Y_k||_2^2 = sup_{||g||_2<=1} E|<X_k,J^{-r}g>|^2`.

The input only says that `g -> <X_k,J^{-r}g>` is a bounded operator `L^2 -> L^2(Omega)`. A Bochner `L^2(Omega;L^2)` representing vector entails Hilbert-Schmidt/trace-type control; bounded operator norm alone is insufficient. The displayed equality also identifies a Hilbert-Schmidt/trace quantity with an operator norm.

**Scoped conclusion:** (7.4) and (A.17) are not established by the displayed covariance bounds. This is an upstream realization/norm issue separate from the later noncompact-ball tightness issue.

## Source-named repair coordinate found after the freeze

The bounded post-freeze search found no `compact embedding`, `Rellich`, `Minlos`, or `compact containment` statement in the source. It did recover the source's own alternative in main §7.1: after the Hilbert-space argument, the paper says an alternative is Mitoma's criterion on the dual of a nuclear space; Theorem 7.1 then uses scalar projection tightness and attributes `S'(R^4)` tightness to Mitoma.

This is a materially narrower repair coordinate. The scalar smeared-field second-moment estimate can plausibly be sought directly from the covariance bound (7.2)–(7.3), without first manufacturing `E||iota_k||_{H^{-s}}^2`. But the exact cited primary theorem is Mitoma, *Annals of Probability* 11 (1983), 989–999, whose title is explicitly about `C([0,1];Y')` and `D([0,1];Y')`. In this runtime the primary Project Euclid/Mathdoc full text could not be acquired. Therefore the static-law / constant-path embedding, exact topology, measurability/Radon hypotheses, and applicability to the paper's thermodynamic-limit fields remain `CANNOT_CHECK`; they are not reconstructed from memory.

Even if that source binding succeeds, it must still show that the limiting laws and Schwinger functionals use the same gauge-invariant observable normalization, positive-time algebra, reflection-positive state and continuum subsequence required for OS reconstruction. The repair cannot silently switch from the finite generating set or from the fixed-physical renormalized observable family required by #205.

## Same-context expert cell

1. **Constructive QFT / OS reconstruction:** a distributional compactness repair must land on the same positive-time gauge-invariant source algebra and the same continuum subsequence; otherwise OS positivity and the later Hamiltonian claim are not glued.
2. **Infinite-dimensional probability / nuclear spaces:** the orthonormal Dirac-law control rejects moment-bound ⇒ Hilbert-tightness. Mitoma is a source-named alternative, but theorem-level static/topology binding is presently unavailable.
3. **Functional analysis / Sobolev theory:** (7.4) and (A.17) conflate covariance operator norm with trace/mean-square norm; a bounded covariance operator is not automatically Hilbert-Schmidt/trace class.
4. **Rigorous RG / observable renormalization:** `Z_O(k)` supplies at most the stated pairing/second-moment normalization. It does not by itself produce compact containment or the nonzero fixed-physical cumulant needed by #205.
5. **Lattice gauge / limit analysis:** the `R^4` thermodynamic limit introduces translation/volume leakage that must be audited independently of local regularity and lattice-spacing estimates.
6. **Formal proof / quantifier audit:** Theorem 3.7, main (7.4), Appendix (A.17), and (A.18) are distinct local failures. No source-wide impossibility conclusion follows.
7. **Adversarial source / RAKL metrology:** bounded repository search found no stored duplicate of this tightness/trace obstruction. #138 uses tightness as a premise and is now dependency-warned rather than counted as a duplicate. Same-context expert agreement earns zero isolated-review credit.

## Analogue / disanalogy audit

- `delta_{e_k}` shares exactly the moment-bound/tightness implication but is not a Yang–Mills model. It falsifies only the generic inference.
- The finite-dimensional covariance example cleanly separates trace from operator norm but does not reproduce infinite-dimensional realization failure; it is a typing control.
- Mitoma's distribution-valued tightness theorem is structurally aligned with the source's alternative route, but the path-space/static-space mapping and exact topology have not been primary-source bound. It remains a repair coordinate, not a transferred theorem.

## Failure and residual separation

**Episode:** `EP-YM-C1a-R12-20260812` records this one source-repair cycle.

**Diagnosis:** `DG-YM-C1a-R12-TIGHTNESS-REALIZATION-SHADOW` — supported local proof/interface diagnosis: the displayed Hilbert tightness and covariance-to-Hilbert-norm steps are invalid generically, while a source-named `S'` route remains unresolved.

**Scoped failures:**
- `FS-YM-C1a-HILBERT-MOMENT-NONCOMPACT-R12-SHADOW`
- `FS-YM-C1a-COVARIANCE-BOCHNER-TRACE-R12-SHADOW`

**Obstruction:** `O-YM-C1a-CONTINUUM-TIGHTNESS-REALIZATION-R12-SHADOW` — the current packet does not yet supply a verified compactness/realization theorem that produces the same continuum OS source/state.

**Lesson:** none minted. The exact repair is not yet verified.

**Residual before:** `RES-YM-CONTINUUM-EXISTENCE-TIGHTNESS-AND-SAME-OS-SUBSEQUENCE-UNVERIFIED`.

**Residual after:** `RES-YM-C1a-PRIMARY-MITOMA-STATIC-S_PRIME-TIGHTNESS-OR-COMPACT-CONTAINMENT-PLUS-SAME-OS-SOURCE-BINDING`.

## Verification status

- Primary PDF parsed-text binding: PASS for the cited equations/theorems.
- Visual PDF verification: 7 attempts, 2 successes (PDF pages 477 and 80), 5 backend cache-miss failures (478, 537, 538 twice, 79).
- Primary Mitoma theorem detail: `CANNOT_CHECK` — bibliographic identity/source citation found, but full primary theorem text inaccessible in this runtime.
- Candidate generation: BLOCKED / `CANNOT_CHECK`.
- Formal verifier / dependency / axiom audit: not run; no theorem candidate exists.
- Independent mathematical reviews: `0/3`.
- Root: `OPEN_NO_SOLUTION_CERTIFICATE`.

## Framework-improvement hypothesis

No new protected framework claim is warranted. Measurement-only hypothesis: when a source claims tightness in an infinite-dimensional space, a future routing/checklist operator could explicitly distinguish **bounded-set control** from **compact containment** and **operator covariance norm** from **trace/Hilbert-Schmidt control** before allowing a continuum-extraction route. This is an application-derived hypothesis only; no RAKL version change or tool promotion is claimed.
