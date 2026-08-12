# RH-ANA-003c — source-cutoff / independent-window gluing falsifier (R4)

**Candidate:** `C-RH-ANA-003c-INDEPENDENT-WINDOW-REORDERABILITY`  
**Outcome:** `REFUTED_ROUTE_LOCAL / PARTIAL_SUCCESS_REPRESENTATION_AND_GLUING`  
**Root authority:** `NONE`  
**Novelty authority:** `NONE`; the retained lemma is an elementary source-compositional representation fact, not a literature-novel theorem claim.

## Frozen chronology and source boundary

R4 candidate generation occurred only after the following proposal/shadow pre-candidate artifacts were frozen on `research/rh-ana003c-cutoff-gluing-r4-20260812`:

- `RH_ANA_003c_CONTEXT_FIBER_20260812_R4.json`, fibre hash `sha256:f8f65c468d80f321113e4752664a1fecd41ed9376df22f1462ff99d3fb739bed`;
- `RH_ANA_003c_RESEARCH_MEMORY_REVIEW_20260812_R4.json`, hash `sha256:4d3f0d3361160b06bcb5ac03846d72e1c4293fcb21ea61218878ece005b7e62c`;
- `RH_ANA_003c_EXPERT_CELL_PRE_CANDIDATE_20260812_R4.json`, hash `sha256:0b9726db241a1d580af59827c3f481afdb7ac1567882f05e57d12a071ab24663`;
- `RH_ANA_003c_PRE_CANDIDATE_TRACE_20260812_R4.json`, terminal event `RH-ANA-003c-E07`, hash `sha256:bc31cb846636bbd8881f7ab6e820a9d5b71707afe7fac5edd63502e757251e82`.

Current framework source of truth was read first as `SzeChunYiu/RAKL@b8f96b8c90745c6a7a6ed57bc55d90319db505f7`, method `3.0.0`. Current `RAKL_math` cycle base was `3cfc8a3b2ff6d981351d2f15421c8cc08048f74b`. The application framework pin is `4d78fd216dab0f9589a0c23f1140cdee00a33b98`, five commits behind current RAKL main; a compare audit found those five commits confined to Paper-2/Paper-5 benchmark/status artifacts, not the audited v3 core or `method_specs.py`. This does **not** turn pinned application CI into current-framework proof authority.

Current-work reconciliation explicitly retrieved RH PRs #80, #118 and #147 before routing. This repairs the prior XM011 process miss in which open same-atom work #118 had not been bound before a #147 route decision. Both remain shadow experience, not theorem authority.

## Primary-source binding

Mark W. Coffey, *The Stieltjes constants, their relation to the eta_j coefficients, and representation of the Hurwitz zeta function*, arXiv:`0706.0343v2` (25 Feb 2009), Proposition 1, equations (12)–(13), gives convergent natural-order moment series of the form

\[
\sum_{m\ge 1}\frac{1-\Lambda(m)}{m}(\log m)^k
\]

for fixed nonnegative integer `k`, through the stated identities with the Stieltjes/eta coefficients. Proposition 2, equations (15)–(17), defines

\[
S_\Lambda(n)=\sum_{m=1}^{\infty}\frac{1-\Lambda(m)}{m}L_{n-1}^{1}(\log m),\qquad n\ge1,
\]

and derives it from Proposition 1 and the finite power-series definition of the associated Laguerre polynomial. The proof around equation (48) makes this source lineage explicit.

The R4 result uses no unproved RH input and no numerical estimate as authority. Coffey `math-ph/0505052`, Voros `math/0506326`, Guth–Maynard (Annals of Mathematics 203 (2026), 623–675 / arXiv:`2405.20552`), Conrey–Farmer–Kwan–Lin–Turnage-Butterbaugh arXiv:`2508.11108`, and Bellotti–Trudgian–Yang arXiv:`2603.21490` were consulted for Li/zero-density/mollifier/zero-free route context, but are not needed for the fixed-`n` convergence proof below.

## Source-bound lemma: the Coffey `S_Lambda(n)` term series is conditional for every fixed `n`

For every fixed integer `n >= 1`, the series

\[
\sum_{m=1}^{\infty} a_{n,m},\qquad
 a_{n,m}:=\frac{1-\Lambda(m)}{m}L_{n-1}^{1}(\log m),
\]

converges in Coffey's natural `m` order but does **not** converge absolutely.

### Natural-order convergence

Use the finite polynomial identity

\[
L_{n-1}^{1}(x)=\sum_{k=0}^{n-1}{n\choose k+1}\frac{(-x)^k}{k!}.
\]

For fixed `n`, `S_Lambda(n)` is therefore a finite linear combination of the moment series in Coffey Proposition 1, and the same conclusion is stated directly in Proposition 2. Hence the natural source partial sums converge.

### Absolute divergence

The polynomial `L_{n-1}^{1}(x)` has degree `n-1` and leading coefficient

\[
\frac{(-1)^{n-1}}{(n-1)!}.
\]

Consequently there are constants `x_n>0` and `c_n>0` such that

\[
|L_{n-1}^{1}(x)|\ge c_n x^{n-1}\quad (x\ge x_n).
\]

Let

\[
E=\{m:\ m\text{ is even and is not a power of }2\}.
\]

The only even prime powers are powers of `2`, so `Lambda(m)=0` for every `m in E`. For sufficiently large `m in E`,

\[
|a_{n,m}|=\frac{|L_{n-1}^{1}(\log m)|}{m}
\ge c_n\frac{(\log m)^{n-1}}{m}.
\]

But

\[
\sum_{\substack{m\ge 2\\m\text{ even}}}\frac{(\log m)^{n-1}}m
=\frac12\sum_{r\ge1}\frac{(\log(2r))^{n-1}}r=\infty,
\]

whereas removing the powers of two subtracts only

\[
\sum_{j\ge1}\frac{(j\log2)^{n-1}}{2^j}<\infty.
\]

Therefore the absolute subseries over `E` diverges, and so

\[
\boxed{\sum_{m\ge1}|a_{n,m}|=\infty}\qquad\text{for every fixed }n\ge1.
\]

Together with natural-order convergence, this proves conditional convergence.

A calibration-only computation for `n=1,2,3,5` through cutoff `2*10^5` showed stable signed partial sums at `O(1)` scale while absolute partial sums continued to grow. No computation is used in the proof.

## Exact representation consequence: admissible windows must carry a summation witness

Let `1=M_0<M_1<M_2<...` be integer cutoffs tending to infinity, and define finite contiguous source-order shells

\[
W_j(n)=\sum_{M_j\le m<M_{j+1}}a_{n,m}.
\]

For every finite `J`,

\[
\sum_{j=0}^{J}W_j(n)=\sum_{m<M_{J+1}}a_{n,m}.
\]

Hence the **ordered** shell limit reproduces Coffey's source value. This is a legitimate local representation.

What fails is the stronger candidate assumption that the infinite collection of windows is automatically order-independent or can be glued after arbitrary independent bounding. Term-level absolute convergence is false. Therefore any later use of local windows must explicitly prove at least one appropriate gluing mechanism: preserve the original increasing-cutoff order; prove an independently sufficient block-level convergence/tail theorem; or justify a different summation method and prove that it returns the same source-defined `S_Lambda(n)`. A specially chosen block decomposition may have absolutely summable block sums even though the term series is conditional; R4 does not rule that out. It merely makes that property an obligation rather than a free consequence.

## Counterexample-first interpretation

The cheapest hostile control is internal to the exact arithmetic source: the positive-density family of even non-prime-power indices already forces divergence of the termwise absolute mass. No synthetic zeta zero set is needed for this representation test. The off-critical-quartet falsifier from R1/#118 remains a downstream regression test for any eventual all-index Li gluing theorem, but it does not prove the conditional-convergence lemma.

## Episode -> diagnosis -> obstruction / lesson

**Episode `EP-RH-ANA-003c-CUTOFF-GLUING-20260812-R4`:** the frozen candidate `C-RH-ANA-003c-INDEPENDENT-WINDOW-REORDERABILITY` was tested against Coffey's exact source series. Outcome: `REFUTED_ROUTE_LOCAL / PARTIAL_SUCCESS_REPRESENTATION_AND_GLUING`.

**Diagnosis `D-RH-ANA-003c-CONDITIONAL-SOURCE-CANCELLATION`:** the full source value exists through signed natural-order cancellation, while the absolute term mass diverges for every fixed Li index. The proposed decomposition was over-authorized by silently upgrading conditional source convergence to order-independent convergence.

**Obstruction `O-RH-ANA-003c-SUMMATION-METHOD-BOUNDARY`:** an infinite local-window programme cannot promote separately estimated pieces to the Coffey `S_Lambda` value without a source-order / block-tail / equivalent-summation witness. This is a representation-and-gluing obstruction, not evidence that no useful localized decomposition exists.

**Candidate lesson `L-RH-ANA-003c-SYNCHRONIZE-CUTOFF-BEFORE-LOCAL-BOUND`:** before estimating local pieces of a cancellation-defined analytic source, bind the summation method and prove the local-to-global assembly law; do not inherit rearrangement authority from notation. Proposal/shadow only.

**Candidate motif `M-RH-ANA-SUMMATION-ORDER-SENSITIVE-GLUING`:** `conditional source object + local partition => gluing requires an explicit order/tail witness`. Proposal/shadow only.

## Failure separation

**Local mathematical failure — `F-RH-ANA-003c-ABSOLUTE-CONVERGENCE-FALSE`:** the candidate assertion of termwise absolute convergence is false for every fixed `n`.

**Local representation failure — `F-RH-ANA-003c-ORDER-INDEPENDENT-WINDOW-SEMANTICS`:** arbitrary order-independent infinite window semantics do not follow from Coffey's representation.

**Local-to-global/gluing failure — `F-RH-ANA-003c-UNWITNESSED-WINDOW-GLUE`:** independently proved local window bounds do not by themselves identify the global source value unless the ordered limit, a block-tail theorem, or an equivalent summation method is certified.

No theorem about a synchronized dyadic shell sequence, an `n`-dependent moving cutoff, partial summation, a mollifier/resonance insertion, or a proper one-sided block condition is refuted.

## Saturation / route rotation

- `KNOWLEDGE`: reopened by the exact conditional-vs-absolute source classification; retained one source-bound representation fact.
- `OPERATOR`: naive termwise absolute-majorant / arbitrary-reordering operator is flattened; synchronized cutoff and source-bound partial summation reopen.
- `EXPERIENCE_PATTERN`: reopened because R2 cancellation loss and R4 source-order loss share cancellation sensitivity but occur at different interfaces.
- `OBSTRUCTION`: reopened with `O-RH-ANA-003c-SUMMATION-METHOD-BOUNDARY`.
- `RELATION`: reopened at the local-window -> global-source gluing edge.
- `PATH`: arbitrary independent windows flattened; synchronized moving-cutoff/tail path reopened.
- `META_METHOD`: framework hypothesis opened but not counted as learned/promoted method content.

Defensible RAKL novelty class: `REPRESENTATION` with a `COMPOSITIONAL` derivation. This labels the route delta only; it is not a claim of literature novelty.

## New residual

`RH-ANA-003d — SYNCHRONIZED_MOVING_CUTOFF_TAIL`

Choose a source-bound increasing cutoff `X(n)` (or a fixed ordered shell family whose endpoint is coupled to `n`) and formulate the smallest tail or signed-shell obligation that:

1. preserves Coffey's natural `m`-order exactly;
2. has an explicit block-tail / limit-order certificate and `n`-uniform Laguerre control;
3. is strictly weaker, under a fresh obligation-strength audit, than polynomial boundedness of the full `S_Lambda`;
4. changes the Li lower-bound ledger only after an explicit local-to-global proof;
5. survives the R1/#118 single-off-critical-quartet regression and does not reduce to finite-prefix, density-only, termwise absolute-majorant, or full-remainder polynomial control.

The next candidate is blocked until a fresh child fibre/memory/review/trace packet freezes the cutoff scale and the exact gluing interface.

**Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical review credit `0`.
