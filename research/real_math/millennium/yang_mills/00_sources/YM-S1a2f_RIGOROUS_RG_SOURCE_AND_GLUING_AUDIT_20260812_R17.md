# YM-S1a2f R17 — rigorous RG source and gluing audit

Authority: **proposal/shadow only**. This file is source evidence and diagnosis, not a theorem, lesson promotion, independent review, continuum construction, or root certificate.

## Exact atom

- Atom: `YM-S1a2f`
- Issue: #283
- Signature: `YM-S1a2f-RIGOROUS-RG-WEAK-UV-TO-STRONG-IR-SAME-THEORY-SPECTRAL-TRANSPORT`
- Parent residual: #269 / R15 showed that the microscopic SZZ strong-coupling theorem domain does not overlap the asymptotically-free bare-coupling tail. Concurrent PRs #256/#258 already occupy the fixed-cutoff OS/transfer spectral fibre.
- Question frozen prospectively in `10_case_study/YM-S1a2f_PRE_CANDIDATE_FIBRE_MEMORY_20260812_R17.json` before this source conclusion was written.

## Primary-source family actually inspected

### Balaban 4D lattice-gauge RG family

1. T. Bałaban, *Renormalization group approach to lattice gauge field theories. I. Generation of effective actions in a small field approximation and a coupling constant renormalization in four dimensions*, Commun. Math. Phys. **109** (1987), 249–301, DOI `10.1007/BF01215223`.
   - Publisher abstract: four-dimensional pure gauge theory; **analysis restricted to a small-field approximation**; constructs localized effective actions, beta functions, and recursive coupling-constant RG equations.
2. T. Bałaban, *Renormalization group approach to lattice gauge field theories. II. Cluster expansions*, Commun. Math. Phys. **116** (1988), 1–22, DOI `10.1007/BF01239022`.
   - Publisher abstract: the fluctuation integral from Part I is put in an exponentiated cluster expansion and the inductive assumptions are preserved, completing the **small-field** effective-action construction.
3. T. Bałaban, *Convergent renormalization expansions for lattice gauge theories*, Commun. Math. Phys. **119** (1988), 243–285, DOI `10.1007/BF01217741`.
   - Publisher abstract: introduces complete effective densities including large-field domains and shows the RG transformations preserve their form; the abstract says this yields convergent expansions in the superrenormalizable case.
4. T. Bałaban, *Large field renormalization. I. The basic step of the R operation*, Commun. Math. Phys. **122** (1989), 175–202, DOI `10.1007/BF01257412`.
   - Publisher abstract: the R-operation handles expressions connected with **large-field regions** in order to remove the main obstacle to ultraviolet stability of four-dimensional gauge field theories.
5. T. Bałaban, *Large field renormalization. II. Localization, exponentiation, and bounds for the R operation*, Commun. Math. Phys. **122** (1989), 355–392, DOI `10.1007/BF01238433`.
   - Publisher abstract: completes the proof of **ultraviolet stability of four-dimensional pure gauge field theories**.

Exact publisher surfaces inspected: Springer/CMP records for all five papers; Rutgers open metadata was used only to reach/cross-check the same DOI/title/abstract records. No theorem stronger than the inspected primary source surface is imputed.

### Current claim-family falsifier

Jonathan J. Wilson, *Rigorous Construction of Four-Dimensional Yang–Mills Quantum Field Theory Via Gribov–Zwanziger Quantization and Renormalization Group Analysis: Measure-Theoretic Foundations, Spectral Properties, and the Mass Gap*, March 15, 2026 version, SSRN abstract `6419219`; author-uploaded full-text indexing also exposed the January/March 2026 manuscript text.

This source is important because it is a direct potential falsifier: it claims a small-coupling continuum Yang–Mills construction, Balaban RG, OS reconstruction, and a mass gap. The bounded audit therefore did not reject it merely because Clay still lists the problem as open.

The inspected manuscript text contains both:

- an earlier `Theorem 8.16` labelled “Balaban’s Renormalization Group for Gauge Theories” that asserts a continuum observable error of the form `|<O>_{a_K}-<O>_cont| <= C_O a_K^2 |log a_K|^nu`, followed by use of that assertion in later GZ continuum estimates; and
- a later Section 37, **“Research Roadmap: Closing the Remaining Nonperturbative UV Renormalization Layer”**, which states that the current manuscript gives an infrared-to-intermediate-scale construction under inputs and that a complete Clay-level solution still requires nonperturbative UV renormalization, including a quantitative one-step beta-function remainder and a controlled UV trajectory / continuum limit / universality layer.

The runtime could not fetch the SSRN PDF directly (HTTP 403), but the author-uploaded indexed full text exposed the relevant sections and equations. This is recorded as a retrieval limitation, not hidden as a mathematical conclusion.

## R17 mathematical/source diagnosis

### D1 — “large field” is not “strong coupling”

The Balaban titles can induce a dangerous representation shortcut. On the inspected primary surfaces, “large field renormalization” refers to **large-field configuration regions inside the R-operation used to prove ultraviolet stability**. It does **not** state a theorem that the running coupling has entered the SZZ strong-coupling domain. Therefore the phrase `large field` cannot be used as the missing weak-coupling-to-strong-coupling bridge.

This is a semantic/type correction with mathematical consequences: field-amplitude sector and coupling-regime coordinate are distinct.

### D2 — the examined Balaban source family does not source-bind the R15 successor obligation

The source family does establish genuine rigorous RG structure: one-step effective actions, beta/coupling recursion in a small-field approximation, large-field control, and 4D ultraviolet stability. But the inspected theorem surfaces do not bind the conjunction required by #283:

`weak bare AF trajectory -> controlled strong effective scale -> same gauge-invariant OS/transfer spectral observable -> regulator-uniform physical mass normalization`.

In particular, no inspected primary Balaban statement supplies a theorem transporting a transfer-matrix spectral gap or SZZ-type covariance rate through the RG flow to the same continuum OS theory, and no inspected statement gives the needed uniform `m_lat(a)/a >= m_* > 0` conclusion.

This is **not** a theorem that no such result can exist. It is a bounded applicability result for the inspected primary family.

### D3 — the current 2026 claim-family is internally non-closing on the exact UV coordinate

The current Wilson manuscript is not ignored: its own Section 37 explicitly labels nonperturbative UV renormalization and the controlled UV trajectory/continuum/universality layer as remaining work needed for a complete solution. That later scope statement prevents using the manuscript’s earlier `Theorem 8.16` continuum-error attribution as an already-closed certificate for #283 without an independent proof of the UVR obligations.

The key source-binding issue is especially sharp: Balaban’s inspected 1987/1989 primary descriptions are small-field/effective-action and ultraviolet-stability results, while the 2026 manuscript attributes to “Balaban’s Theorem 8.16” a quantitative continuum-correlator error and then later says the nonperturbative UV trajectory still must be constructed. The safe conclusion is `CANNOT_CHECK/CANNOT_PROMOTE` for that continuum bridge, not theorem transfer.

## Counterexample-first / hostile controls

1. **Coordinate collision:** a configuration can be in a “large-field region” while the bare/running coupling remains perturbatively small; therefore `large field` does not logically imply `strong coupling`.
2. **Ultraviolet-stability control:** a uniform bound on a partition function/effective density across cutoff scales can hold without a positive spectral gap or without a theorem transporting a particular OS source family; UV stability alone is not the target spectral statement.
3. **Scaling control:** any fixed-cutoff spectral edge `delta(a)>0` can still satisfy `delta(a)/a -> 0`; a same-theory RG construction must bind physical normalization, not just positivity at every regulator.
4. **Current-preprint self-scope control:** if a manuscript explicitly lists construction of the controlled UV trajectory/continuum limit as remaining, an earlier theorem label cannot be treated as a root-level continuum certificate without resolving that internal dependency.

## Same-context expert cell synthesis

- **Rigorous lattice-gauge RG:** Balaban supplies a serious UV RG framework; the inspected result type is ultraviolet stability/effective-action control, not an identified SZZ-regime entry theorem.
- **OS/transfer spectral:** RG equality of partition functions/effective densities is not by itself a proof that a chosen one-step transfer operator, OS null quotient, spectral projector, or physical-time gap is preserved. A source-bound observable intertwiner/semigroup statement is still required.
- **Asymptotic-freedom/coupling normalization:** the direction `weak UV -> larger IR coupling` is physically expected, but the present atom requires a rigorous controlled trajectory all the way to the theorem domain used for the spectral input; a beta-function asymptotic or local recursion is insufficient without the uniform remainder/domain theorem.
- **Constructive probability/Gibbs:** large-field suppression controls configuration tails and polymer errors; it should not be conflated with strong coupling of the measure.
- **Adversarial mathematical physicist:** the strongest falsifier located is Wilson 2026, but its Section 37 itself preserves the UVR gap, so it does not close the atom on the inspected text.
- **Primary-source/provenance:** Balaban conclusions are restricted to what the publisher primary records state; inaccessible/full-text coordinates are not silently filled from memory.
- **RAKL v3 metrology/authority:** result remains proposal/shadow, same-context expert roles earn zero independent-review credit, and no protected lesson/obstruction promotion follows from repository persistence or CI.

## Episode -> diagnosis -> reusable obstruction/lesson boundary

- **Episode:** R17 queried the same-domain rigorous lattice gauge RG source family after live-work memory rejected duplicate fixed-cutoff OS work.
- **Diagnosis:** the obvious Balaban route is mistyped if “large field” is read as “strong coupling”; the published 4D source surface proves UV stability/effective-action control, while the current 2026 claim family itself records nonperturbative UVR as still required.
- **Shadow obstruction:** `OBS-YM-S1a2f-RG-REGIME-AND-SPECTRAL-INTERTWINER-MISSING` — no inspected theorem yet binds controlled weak-to-strong regime crossing to the same-theory OS/transfer observable and physical mass normalization.
- **Reusable shadow lesson:** keep **field-amplitude sector**, **coupling regime**, **RG scale**, and **physical spectral normalization** as separate typed coordinates; a theorem controlling one must not be routed as controlling another without an explicit interface lemma.
- **Authority:** both obstruction and lesson are proposal/shadow evidence only. No protected memory admission or mathematical authority transition is requested.

## Local versus gluing failures

- Local mathematical failure: **none established**. No Balaban theorem was disproved.
- Representation failure: **present** if `large field` is equated with `strong coupling`.
- Source/applicability failure: **present** for treating the inspected Balaban statements as the complete #283 bridge.
- Local-to-global / same-theory gluing failure: **present**. The missing object is the explicit RG/observable/OS/physical-time intertwiner and regulator-uniform mass normalization along the actual continuum trajectory.
- Retrieval limitation: SSRN PDF direct fetch returned 403; author-indexed full text supplied the cited internal roadmap and theorem statements, but a line-by-line full-PDF verifier audit remains outstanding.

## Saturation and next discriminator

The fixed-cutoff OS-transfer family remains flattened for this cycle because #256/#258 already occupy it. `KNOWLEDGE`, `RELATION`, and `PATH` reopened when the current 2026 claim-family and its explicit UVR roadmap were retrieved. The next smallest discriminator is **UVR2/UVR3 exact source binding**: either exhibit a rigorous one-step coupling map with a uniform remainder plus a controlled trajectory reaching a theorem domain that carries the same gauge-invariant OS/transfer observable, or keep the bridge open. If a new RG map is proposed, it must additionally prove reflection-positive/spectral compatibility or an exact observable pushforward sufficient to recover the same continuum Hamiltonian gap.

## Novelty class

The solved subproblem “does the inspected `large field renormalization` source phrase certify strong-coupling entry?” is classified **compositional / RAKL_TRIVIAL**: the answer follows by combining the explicit primary-source scopes and the current manuscript’s own UVR roadmap. It is not a new Yang–Mills theorem and receives no protected novelty credit.
