# Same-context pre-candidate review — BSD-S001c1

**Date:** 2026-08-11  
**Root control:** RAKL_math issue #7  
**Atom:** `BSD-S001c1-KURIHARA-TAYLOR-COMPARISON`  
**Authority:** `SAME_CONTEXT_PRE_CANDIDATE_REVIEW / NOT_INDEPENDENT / NO_THEOREM_AUTHORITY`

No mathematical comparison candidate is proposed in this review.

## Expert cell

### 1. Arithmetic-geometry / Selmer lead

**Background:** elliptic curves over `Q`, Mordell–Weil groups, Bloch–Kato and classical Selmer groups, Tate–Shafarevich groups, descent, regulators and the exact BSD arithmetic factors.

**Finding:** Kim–Pollack's discrete invariant can determine the `p`-primary Bloch–Kato Selmer corank and finite module structure under its hypotheses. This is materially stronger arithmetic information than a one-sided Euler-system bound. It still does not identify the Clay complex analytic order, and Selmer corank is not definitionally `rank E(Q)` if a divisible `p`-primary Sha contribution remains.

**Strongest objection:** treating an exact Selmer formula as the BSD rank theorem skips two distinct arrows: discrete order → complex analytic order, and Selmer corank → Mordell–Weil rank.

**Delegation:** keep these arrows separate in the implication graph and attach exact Sha/finiteness hypotheses to the second.

### 2. Cyclotomic Iwasawa / Kato lead

**Background:** Kato zeta elements, Kolyvagin systems, cyclotomic Iwasawa theory, characteristic ideals, localized main conjectures and explicit reciprocity.

**Finding:** Kim–Pollack Main Theorem II can obtain nonvanishing of the Kurihara collection from localized Iwasawa-main-conjecture input or good-ordinary hypotheses; Main Theorem I then recovers exact Selmer structure. This closes a substantial arithmetic branch without low analytic-rank assumptions.

**Strongest objection:** nonvanishing is only the gateway to the exact discrete order formula; it does not determine that order from the complex Taylor expansion. Importing the localized main conjecture therefore does not by itself close the complex rank edge.

**Delegation:** classify every use of IMC as `arithmetic reconstruction`, `nonvanishing`, or `complex comparison`; reject bundled `IMC => BSD` edges.

### 3. Complex↔discrete comparison lead

**Background:** complex and `p`-adic L-functions, modular symbols, special-value derivatives, explicit reciprocity, derived heights and leading-term formulas.

**Finding:** the 2026 Kim–Pollack manuscript explicitly motivates an analogy between the Kurihara collection and the Taylor expansion, while its abstract and introduction emphasize that its exact Selmer formula is insensitive to analytic rank. The source therefore exposes a clean comparison problem: identify the exact theorem, if any, that equates the discrete order invariant with `ord_{s=1}L(E,s)` in arbitrary rank.

**Strongest objection:** language such as “corresponds to the rank part of BSD” is explanatory positioning, not an equality between the two order invariants.

**Delegation:** search specifically for an order-preserving comparison theorem or two one-sided inequalities; do not search for another Selmer structure formula unless it supplies this cross-representation edge.

### 4. Adversarial circularity / local-global lead

**Background:** implication-audit, local/global arithmetic, counterexample design, circular definitions and hidden-assumption detection.

**Finding:** Burns–Kurihara–Sano already demonstrate the central circularity hazard: their `eta^BSD` leading-term object is defined using complex leading data. That interface is valuable but cannot be fed backwards as an independent reconstruction. Kim–Pollack avoids that definition-level circularity by using independently defined modular-symbol data, which makes it a better comparison target.

**Strongest objection:** a future proof can still be circular if it invokes `BSD_p`, analytic-rank equality, Selmer rank equality, or a main-conjecture specialization whose load-bearing input is equivalent to the desired bridge.

**Delegation:** annotate every implication edge with assumptions and mark the first edge containing root-strength information.

### 5. Formal-assurance lead

**Background:** formal statement binding, proof DAGs, quantifier/hypothesis audits, checker trust and dependency provenance.

**Finding:** the next formal object should be an implication graph with distinct typed nodes: `complex Taylor order`, `Kurihara order`, `Kato/Kolyvagin nonvanishing`, `Selmer corank`, `Mordell–Weil rank`, `Sha[p∞]`, and the refined global leading-term factors.

**Strongest objection:** a theorem proving equality between the last five arithmetic nodes but never mentioning complex Taylor order cannot close `BSD-RANK`.

**Delegation:** require any eventual candidate to state exact input/output types and an explicit complex-order conclusion. Until then, root authority remains none.

### 6. Novelty / frontier lead

**Background:** primary-source theorem search, notation normalization, recent Iwasawa/Euler-system literature and novelty boundaries.

**Finding:** determinant invention is prior art (Burns–Kurihara–Sano), and exact discrete Selmer reconstruction is now substantially stronger in Kim–Pollack. The research frontier has therefore moved from “find higher-rank arithmetic structure” to “compare an independently defined exact discrete order with the complex Taylor order.”

**Strongest objection:** this is a route refinement, not new mathematics. A comparison theorem may already exist under different ETNC, Mazur–Tate, derived-height or special-element language.

**Delegation:** run a notation-normalized primary-source search over those formulations before theorem invention.

## Discussion and consensus

The roles agree on four points:

1. **Do not invent another Selmer invariant first.** Kim–Pollack already provide an exact arbitrary-rank discrete arithmetic invariant under source hypotheses.
2. **Do not call the discrete formula BSD closure.** It is explicitly a discrete/refined BSD-type correspondence and is insensitive to analytic rank.
3. **Do not reuse `eta^BSD` backwards.** Its complex-leading-term definition preserves the BKS circularity warning.
4. **Move the active frontier to the compatibility edge.** The highest-information next action is a bounded primary-source implication audit for `ord(Kurihara) ↔ ord_{s=1} L(E,s)`.

## Proposal-only learning modes

- `REFLECTIVE_RESTRUCTURE`: replace “can Iwasawa theory prove BSD?” with the typed compatibility edge between two independently defined order coordinates.
- `CONTRASTIVE_DISCRIMINATION`: compare rank `0`, rank `1`, and arbitrary rank to locate exactly where proven complex input stops controlling the discrete order.
- `EFFECTUAL_PROBE`: build the implication graph and search for one-sided inequalities before generating a new theorem candidate.
- `FIXATION_RESET`: reject additional determinant/Selmer-package invention unless it changes the compatibility edge.

These modes create zero mathematical authority.

## Recommendation

Freeze the strict `BSD-S001c1` context/memory/trace packet and, only after its machine audit passes, execute a bounded source-level comparison search. Candidate generation should remain **unused** unless that search exposes a precise, non-circular missing identity or inequality not already present as a known conjecture/theorem.

Root state remains `OPEN_NO_SOLUTION_CERTIFICATE`.
