# C034b U8 retrospective replay — same-context hostile review

**Reviewed head:** `af38a473d48cbd89753c1324946986b10b3a7c5c`  
**Exact result commit:** `b23a081eb875f6492172e6a93b2fa9bdef0deb67`  
**Review type:** role-separated same-context hostile assurance; **not** independent peer review  
**Verdict:** `NO_BLOCKER`

The reviewer independently reran the focused replay test: `5 passed`.

## Soundness findings

1. Every full semi-filter restricts to a monotone Boolean assignment on the
   35-mask certificate subposet with the empty mask false and a relevant
   row-star/column-star pair true. A returned restricted falsifier extends by
   upward closure without changing tracked zeros. The exhaustive separator and
   its cutoff at scaled forced cost 24 are therefore sound for the registered
   primal certificate.
2. The verifier enumerates exactly
   `(3^8 - 2^9 + 1)/2 = 3025` unordered incomparable full-union pairs. Every
   supported dual semi-filter is checked for nonempty proper masks, antichain
   structure and relevance; exact integer-scaled rule load is at most 24.
3. Matching exact primal and dual totals `49/24` certify only the reconstructed
   finite full-union LP. The C034a extension to all original rules remains a
   desk-checked dependency and is not promoted by this replay.
4. The coordinate-minimal ambient is `4 x 5`. The executable `5 x 6` padded
   world confirms that extra zero complement stars generate no relevant pair
   and leave the finite evaluator unchanged.
5. The receipt preserves the missing original bundle and external
   `CANNOT_CHECK`: regenerated support counts are 17 primal / 20 dual rather
   than the ledger-reported 21 / 24, and are explicitly classified as a
   different matching certificate representation, not recovery of the
   reported certificates.
6. Proof, theorem, asymptotic, novelty, root, independent-review and strict
   context-first discovery authority all remain denied.

## Nonblocking note

`minimum_scaled_primal_coverage` is populated from supported dual witnesses
rather than directly from the generator-separation list. This is justified in
the exact receipt because a legal relevant supported witness has coverage 24
and exhaustive separation proves every relevant witness has coverage at least
24.

