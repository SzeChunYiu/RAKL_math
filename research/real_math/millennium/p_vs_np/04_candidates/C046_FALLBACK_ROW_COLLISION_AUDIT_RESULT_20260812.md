# C046 fallback-row collision audit result

**Authority:** `PROPOSAL_SHADOW_RETROSPECTIVE_VERIFICATION_ONLY`  
**Framework:** `SzeChunYiu/RAKL@43897d3afaf0038385102d5acc64793c05ec40f0`, method `3.0.0`  
**Application base:** `RAKL_math@ac8c0745be8aed791a446fd55fcf5154cac01962`  
**Frozen verification fibre:** `sha256:5668fefcaac17e6eb27123db44f0e2dc53c25e8035c87d5aa29cfb68d264507f`  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`

## Chronology boundary

The decisive observation was formed after reading current C045 and the frozen decoder but before the durable C046 verification fibre was committed. This result is therefore a retrospective truth/consistency audit only. It receives no strict prospective RAKL discovery credit and does not backfill chronology.

## Exact decoder lemma

For every parent level `n >= 2`, the frozen one-sided decoder gives a deterministic fallback complement edge at the next level:

`(0, 2^n) in U_{n+1}`.

Indeed, `cross_word(n,0,0)=0^(2n)`. The first exceptional branch of `decode_formula` maps every all-zero even word to the frozen `CONTRADICTION`, whose two clauses are opposite repeated unit clauses and hence are unsatisfiable. Therefore `complement_contains(n+1,0,2^n)` is true.

Moreover `(0,0) in U_2` by the frozen seed, and the top-left recursive branch preserves that edge at every later level. Thus row `0` belongs to `Rows(U_n)` for every `n >= 2`. Consequently

`0 in Rows(U_n) intersect Rows(U_{n+1} \ U_n)`

for every extension. Full-complement row-projection collision is therefore present at every step through the decoder fallback, independently of the canonical MAGIC batch.

This is a direct hand proof from the frozen application object. Finite execution is retained only as calibration.

## G17 DifferenceWitness against C045 as written

At `n=16`, the missing fallback edge is exactly

`f16 = (0,65536)`.

Current C045 correctly classifies ten **canonical MAGIC long-form** length-32 UNSAT words and correctly gives an explicit local three-pair code for that ten-edge canonical block. However, C045 Theorem 2 additionally states that the **full** G17 complement is exactly the embedded `U16` plus those ten edges, and uses full old/new row- and column-projection disjointness in its block-gluing argument. That full-complement statement is false as written because `f16` is an additional cross complement edge and its row `0` is already active in `U16`.

This is not a refutation of the ten-word canonical classification. It is a representation/decomposition error: `canonical MAGIC batch` and `all newly created complement support` were conflated after C043 had explicitly tracked the row-zero fallback separately.

## Which C045 claims survive this audit

1. **Survives:** the exact ten-word classification of canonical MAGIC long-form length-32 UNSAT formulas.
2. **Survives locally:** the three-pair generator-separating code for those ten canonical edges.
3. **Fails as written:** the statement that the full G17 complement equals `U16` plus only those ten edges.
4. **Fails as written:** full old/new row-projection disjointness at G17.
5. **Needs a new proof:** `rho(G17) <= sigma(G17) <= 4`. This inequality is not shown false here, but C045's displayed block-partition proof omits `f16`; it must be re-established with a fallback-aware cover or downgraded.
6. **Needs repair:** the C045 routing lesson cannot search for the first *any* row-projection collision, because the fallback supplies one at every level. The meaningful discriminator must explicitly quotient, absorb, or otherwise prove cover-neutral the deterministic fallback before asking when a canonical MAGIC batch first creates load-bearing coupling.

## Local versus gluing status

**Local mathematical result:** the fallback-edge lemma and the G17 DifferenceWitness are closed by direct proof.

**Local representation failure:** C045's full-complement partition omitted a source-defined decoder branch.

**Local-to-global/gluing failure:** no fallback-aware four-pair cover is proved here; no uniform cover-neutrality lemma for the fallback is proved; no recurrence, circuit lower bound, or P-vs-NP bridge follows.

## Revised next atom

Replace the unfrozen C046 future-length search by the smaller repair atom:

> `O9d12a2a1b-C046R`: bind the full decoder support at G17, including `(0,65536)`, and decide whether the C044/C045 constant-cover construction extends legally. If it does, freeze a precise fallback-normalized quotient/absorption rule before searching for the first canonical MAGIC row collision. If it does not, isolate the exact cover obstruction created by the fallback leaf.

A future search for canonical-row collision is licensed only after this fallback normalization is proved, not assumed.

## Novelty and authority

The solved subproblem is defensibly `representation` with a `compositional` proof: exact decoder branch + recursive seed preservation + C045 statement comparison. It remains proposal/shadow only. Protected retained novelty is zero on all seven RAKL saturation axes pending protected promotion. Same-context expert review is not independent review (`0/3`).
