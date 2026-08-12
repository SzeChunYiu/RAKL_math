# YM-E2a1 — fixed-physical-time RG defect-margin constant-lineage audit

**Parent:** `YM-E2a`, RAKL_math issue #73  
**Root:** RAKL_math issue #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Atom signature:** `YM-E2a1-FS-BLOCK-FACTOR-DEFECT-MARGIN-CONSTANT-LINEAGE`  
**Framework:** `SzeChunYiu/RAKL@f224d91d9fbd2844a89921ca4a30b77a7954ecd2`, method `3.0.0`, package `0.1.0`  
**Application base:** `SzeChunYiu/RAKL_math@696da1ba2f17c7d1859e96338fb98d489c3311c7`  
**Pre-action receipt:** `YM-E2a1-PRE-ACTION-20260811T1937Z`, sha256 `d40544165a6472c62eca4f959e8a5676187dc58915cc09f913a827168dd77fa6`  
**Authority:** `PROPOSAL_SHADOW / EXACT_LOCAL_BUDGET_LEMMA / SOURCE_CONSTANT_LINEAGE_AUDIT / SAME_CONTEXT_REVIEW_ONLY / NO_SOURCE_REPAIR_CERTIFICATE / NO_ROOT_AUTHORITY`.

## 1. Chronology boundary and exact discriminator

The parent observation in issue #73 is retrospective: Faizal–Shabir's fixed-physical-time gap-persistence route needs a strict total-defect margin, not merely a finite defect sum. The current child gives no prospective credit for noticing that fact. Prospective credit is restricted to the bounded discriminator frozen in the pre-action receipt: locate a same-theory source-valid constant chain proving

`sum_k epsilon_k < delta_0`

with the exact block-factor/FRD/collar/volume dependencies, or identify the first missing quantitative interface. A finite sum, or an assertion that a large block factor is enough without the comparison constants, does not satisfy this discriminator.

Primary source audited: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026).

## 2. Exact local budget lemma

Let nonnegative defects satisfy

`Delta_{k+1} >= Delta_k - epsilon_k`.

Then for every `n>=1`,

`Delta_n >= Delta_0 - sum_{j=0}^{n-1} epsilon_j`.

This is immediate by iteration. Therefore this telescoping route yields a regulator-uniform positive lower bound only after a separate certificate of the form

`sum_{j>=0} epsilon_j < Delta_0`.

Finiteness alone is insufficient: `Delta_0=1` and defects `(3/5,3/5,0,...)` are nonnegative and summable, yet the telescoping lower bound becomes negative after two steps.

If only a geometric envelope

`epsilon_k <= C theta^k`, `0<theta<1`,

is available, a sufficient certificate is

`C/(1-theta) < Delta_0`.

Making `theta` small is not by itself enough unless the source also controls the prefactor `C` and the initial reserve `Delta_0` under the same parameter choice.

These are elementary/compositional facts. The exact-arithmetic test committed with this cycle is calibration only; the proof is the displayed inequality.

## 3. What the source actually supplies on the audited route

### Proposition 5.5: summability, but no displayed margin comparison

Proposition 5.5 derives a geometric defect estimate of the shape

`epsilon_k <= C theta^k`, `theta in (0,1)`,

from polymer/locality control after choosing a sufficiently large block factor. The proof obtains an exponential range estimate and then concludes absolute summability. On the inspected statement/proof surface, the constants are not subsequently compared to the initial strong-coupling spectral reserve by an explicit inequality such as `C/(1-theta) < delta_0`.

### Theorem 5.6: the missing strict inequality is acknowledged inside the proof

Theorem 5.6 defines a limiting lower bound as `Delta_* = Delta_0 - sum epsilon_k` and states it is positive after citing summability. But a finite series need not be smaller than `Delta_0`. The proof later explicitly says that, if needed, one may assume `sum epsilon_k < Delta_0`. Thus the strict relative budget is the load-bearing additional condition; it is not a consequence of summability alone.

### Corollary D.5: the proof uses the correct stronger condition

Appendix D's fixed-physical-time formulation is clearer. Corollary D.5 iterates

`Delta_{k+1,L} >= Delta_{k,L} - epsilon_k`

from a uniform initial lower bound `Delta_{0,L} >= delta_0>0`, and its proof explicitly requires `sum epsilon_k < delta_0`, saying this is guaranteed in the construction for sufficiently large block factor. The audited source surface therefore contains the correct logical condition, but the present cycle did not locate an explicit quantitative chain from the earlier constants to that strict comparison.

### Section 8 collar estimate exposes a useful first-term/tail split

A later route chooses a collar `w(k)=floor(c b^k)` with fixed `c>0` and obtains a superexponential defect envelope of the shape

`epsilon_k <= C' exp(-gamma w(k))`.

For this displayed envelope, the `k=0` upper bound is

`C' exp(-gamma floor(c))`,

which does not improve merely by increasing `b` when `c,C',gamma` are held fixed. Increasing `b` does suppress the later tail. Consequently, this displayed estimate alone cannot certify an arbitrarily small total defect budget by the phrase “take the block factor large”; one also needs a source-valid control of the first defect/prefactor, or an admissible choice of `c` (or other constants) that is proved compatible with the same construction. This is a statement about the strength of the displayed certificate, not a lower bound on the actual defect and not an impossibility theorem.

### Initial gap constant is positive but not quantitatively matched here

The strong-coupling entry supplies a positive initial transfer/Hamiltonian gap depending on the coupling and gauge-group data. On the inspected source surfaces, this positive quantity is not linked by an explicit displayed inequality to the defect constants above. That missing relation is the first unresolved constant-lineage interface for this route.

## 4. Counterexample-first falsifiers

The bounded discriminator used two cheap controls.

1. **Summability control:** `Delta_0=1`, `epsilon=(3/5,3/5,0,...)`. This falsifies any inference `sum epsilon_k<infinity => Delta_0-sum epsilon_k>0`.
2. **Tail-only control:** for an envelope `C' exp(-gamma floor(c b^k))` with fixed `c,C',gamma`, changing `b` leaves the displayed `k=0` upper bound unchanged. This falsifies the claim that tail acceleration alone proves the strict total-margin inequality.

Neither control is a Yang–Mills counterexample. They test the logical interfaces used by the source route.

## 5. Same-context expert cell

These are role-separated passes sharing the same evidence and are **not independent review**.

- **Constructive QFT / OS reconstruction:** kept the atom on the fixed-`tau` route. Verdict: this avoids the variable-lattice-step normalization defect in #92, but any eventual spectral result must still live in the same OS Hilbert family handled by #126/#133.
- **Transfer-spectrum analyst:** verified the telescoping lemma and the distinction between a dimensionless fixed-time transfer gap and the physical Hamiltonian gap. Verdict: a positive transfer bound is useful only after the strict defect margin is certified.
- **Constructive RG / FRD analyst:** traced the geometric/superexponential envelopes and parameter dependence. Verdict: summability/tail decay does not expose the missing comparison between first defect/prefactor and `delta_0`.
- **Lattice-gauge / source-provenance analyst:** checked that a positive strong-coupling starting gap exists in the source but found no audited displayed constant chain comparing it to the full RG loss on this route.
- **Adversarial verifier:** ran the finite-sum and first-term/tail controls. Verdict: both reject the unsupported logical upgrades while leaving stronger source-specific estimates possible.
- **RAKL v3 assurance / metrology:** prior `YM-E4b2b`/draft PR #140 was retrieved before choosing this atom and caused a rotation away from a saturated D.5-generic-inference route. Episode, diagnosis, obstruction and any lesson remain separate; all new records are proposal/shadow.

## 6. Local result versus local-to-global gluing

**Local mathematical outcome: `PARTIAL_SUCCESS`.** The exact quantitative obligation for the telescoping persistence route is isolated and verified: summability is insufficient; a strict relative total budget is required. The first-term/tail split shows why tail acceleration alone is not the missing certificate.

**Same-theory source/gluing outcome: `BLOCKED`.** This cycle did not source-bind a complete inequality proving that the actual RG defect constants satisfy the strict margin against the actual initial strong-coupling gap, uniformly in the required volume/regulator family. The source may contain stronger estimates outside the bounded audited surfaces, or the route may be repairable by an independent same-theory argument; neither is inferred.

The following remain separate downstream obligations and are not collapsed into this atom:

- variable-lattice versus fixed-physical-time normalization: #92;
- weak-coupling contraction and bare-coupling escape: #93 and #69;
- same-theory OS quotient/comparison and contraction semigroup: #126/#133;
- dense gauge-invariant source family/common rate: #109 and PR #62;
- physical spectral identification, continuum existence/nontriviality, UV/asymptotic freedom, and root proof/review gates.

A confinement or correlation-decay statement is not promoted to a full spectral gap here, and no numerical result carries proof authority.

## 7. Residual and next discriminator

The source-facing residual is now narrower:

> Produce an explicit, same-theory constant-dependency certificate for the fixed-`tau` RG route that bounds the **first defect plus tail** and proves it is strictly below the initial strong-coupling gap, with exact dependence on block factor, collar/range parameters, coupling, volume and regulator sequence.

Acceptable closure paths include: (i) a direct source-bound inequality `sum epsilon_k < delta_0`; (ii) a first-term/tail split whose constants visibly give the strict margin; or (iii) an independent fixed-`tau` spectral persistence theorem that bypasses this additive budget while preserving the same OS Hilbert/source/regulator family.

Until one of these is verified, `YM-E2a` remains open and root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.

## 8. RAKL novelty and method status

The local budget lemma is elementary and was not subjected to a protected novelty search. Under the current v3 novelty contract its authority class is therefore `UNRESOLVED`; structurally it is at most `RAKL_TRIVIAL/compositional` rather than operator-, representation-, or ontology-novel. No theorem-novelty claim is made.

This cycle's methodological value is route discrimination: stored experience prevented a duplicate D.5 generic-inference cycle and redirected effort to a distinct quantitative spectral/RG obstruction.
