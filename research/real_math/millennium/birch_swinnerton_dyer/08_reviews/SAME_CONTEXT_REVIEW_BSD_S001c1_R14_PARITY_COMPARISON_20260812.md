# BSD S001c1 R14 — same-context expert review

Authority: `SAME_CONTEXT_PROSPECTIVE_REVIEW / 0_OF_3_INDEPENDENT_MATHEMATICAL_REVIEWS`  
Cycle: `BSD-S001c1-R14-PARITY-COMPARISON-20260812`  
Frozen fibre: `sha256:07526440f35e0b4fe0c175770dbeca0280613b593667609e14dae257524fa3a6`

This cell is role-separated but not independent review: all seven roles share the same frozen context and source packet. Their purpose is adversarial decomposition, not authority promotion.

## Expert cell and delegation

1. **Complex analytic number theorist — functional equation/parity lead.** Background: modular elliptic-curve L-functions, root numbers, analytic order. Delegated question: does a proved parity theorem connect the exact complex order to the same p-primary Selmer coordinate without assuming BSD rank equality? Finding: Dokchitser–Dokchitser gives p-parity for every E/Q and every p, so a genuine mod-2 analytic-to-Selmer edge is available.

2. **Euler-system/Iwasawa specialist — Kurihara/Kato lead.** Background: Kato zeta elements, Kolyvagin systems, cyclotomic Iwasawa theory. Delegated question: is the Kurihara order genuinely an independently defined discrete coordinate and when does it equal classical p-infinity Selmer corank? Finding: Kim's Theorem 1.9 supplies exact structural recovery under its explicit theorem-cell hypotheses; current Kim–Pollack strengthens the discrete reconstruction but deliberately remains insensitive to analytic rank.

3. **Selmer/cohomology specialist — coordinate-identity lead.** Background: Bloch–Kato/classical Selmer structures, p-primary corank. Delegated question: are the parity theorem and the Kurihara theorem talking about the same Selmer coordinate? Finding: yes at the scoped classical p-infinity Selmer level used in the composition; no silent p-infinity/Vp or strict/classical substitution is needed for the parity lemma itself.

4. **Arithmetic geometer — BSD-factor/gluing lead.** Background: Mordell–Weil, Sha, Neron–Tate regulator, Tamagawa/local factors. Delegated question: what does the mod-2 relation actually buy at root strength? Finding: it does not identify Mordell–Weil rank or the refined leading term. Sha, regulator, Tamagawa, torsion and period obligations remain separate; fixed-p parity cannot close them.

5. **Proof/circularity auditor — hostile-model lead.** Background: theorem-direction auditing, premise-strength checks. Delegated question: can parity plus known lower bounds force equality? Falsifier: integer orders 2 and 4 have identical parity. Finding: R9 lower bound plus parity restricts rank-two Kurihara order to an even integer >=2, but does not exclude 4,6,... . Any claimed equality without a same-coordinate magnitude bound is invalid.

6. **Source-provenance specialist — primary-literature lead.** Background: theorem-version and selector verification. Delegated question: are claims anchored to current primary sources rather than secondary summaries? Finding: Annals 2010 Dokchitser–Dokchitser, arXiv:2203.12159v6 Kim, and arXiv:2505.09121 Kim–Pollack were checked. The bounded search did not find an arbitrary-rank same-coordinate magnitude theorem; this is not a nonexistence or novelty certificate.

7. **RAKL v3 metrology/gate reviewer — method/authority lead.** Background: v3 pre-action receipt, TaskEpisode, saturation and proof gates. Delegated question: did memory change routing and are authority boundaries preserved? Finding: yes: the prospective receipt freezes a direct-equality search as the pre-memory/pre-gate preference and a parity-first discriminator as the RAKL-conditioned action. `epistemic_sufficiency` was inspected but is not authorized to decide an open BSD claim. Proposal/shadow authority only; independent review credit remains zero.

## Cross-role discussion

The analytic and Selmer roles agree that the two theorem edges compose on the same E/Q and the same classical p-primary Selmer coordinate. The Iwasawa specialist confirms that this produces an actual **complex/discrete relation**, not merely another arithmetic reconstruction. The arithmetic geometer and proof auditor object to calling this an equality bridge: parity is a quotient of the integer-order problem, and the hostile `2 versus 4` witness survives. The provenance specialist confirms that the 2026 discrete frontier does not supply the missing magnitude comparison in the audited statements. The RAKL reviewer therefore routes the outcome as a scoped compositional success plus a still-open gluing residual, not as a candidate root proof.

## Consensus

Source-bound scoped lemma:

`ord_Kur(E,p) ≡ ord_{s=1} L(E,s) (mod 2)`

whenever Kim's exact Kurihara-order/classical-Selmer theorem applies at `(E,p)`.

Rank-two scoped corollary, when the R9 Zhang and R14 Kim theorem cells overlap:

`ord_{s=1}L(E,s)=2  =>  ord_Kur(E,p) in {2,4,6,...}`.

The root remains `OPEN_NO_SOLUTION_CERTIFICATE`. Next discriminator: source or derive a noncircular **same-coordinate magnitude bound** between discrete Kurihara order and complex Taylor order which, combined with the parity edge, forces equality; otherwise rotate to a representation carrying magnitude rather than parity alone.
