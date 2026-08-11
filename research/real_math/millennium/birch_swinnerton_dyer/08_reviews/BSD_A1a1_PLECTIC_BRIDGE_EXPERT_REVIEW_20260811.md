# BSD-A1a1 plectic bridge — same-context expert review

**Subject:** `BSD_A1a1_PLECTIC_BRIDGE_AUDIT_20260811.md`  
**Active atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**Review type:** role-separated same-context AI review; **not independent peer review**.  
**Authority:** `INTERNAL_RESEARCH_CONTROL_ONLY / NO_ROOT_AUTHORITY`.

## Shared exact question

Does rotating from the scalar anticyclotomic theta-order representation to the richer plectic Heegner / mock-plectic representation produce a **proved**, non-circular bridge

```text
exact complex analytic rank two
  -> nonzero root-faithful plectic class/point or nondegenerate regulator
  -> arithmetic rank-two information,
```

under assumptions demonstrably weaker than the arithmetic conclusion sought?

## Role 1 — complex L-function / Rankin--Selberg lead

**Background:** complex analytic continuation, functional equations, Rankin--Selberg central derivatives, Gross--Zagier-type formulas.  
**Evidence inspected:** frozen A1a1 context; Fornea 2026 theorem/conjecture split; Hernández--Molina v2 abstract/result scope.  
**Strongest counter-hypothesis:** higher p-adic derivative formulas may already encode the exact complex second derivative needed for the rank-two root premise.  
**Falsifier:** require a source theorem whose input is the complex `s`-Taylor order/leading coefficient at the relevant central point and whose output is the plectic nonvanishing/determinant, with all auxiliary Euler/local factors explicit.  
**Finding:** the audited positive derivative theorem is Hida--Rankin p-adic; the complex-to-p-adic leading-direction comparison remains a separate obligation.  
**Vote:** `BLOCK_CANDIDATE_GENERATION`.

## Role 2 — plectic arithmetic-geometry lead

**Background:** Heegner constructions, Galois cohomology, localization, plectic points/classes, CM/Shimura-curve geometry.  
**Evidence inspected:** Fornea 2026 Theorems A--C and Section 1.2 conjectural significance.  
**Strongest counter-hypothesis:** the partially global class is sufficiently rich that nonvanishing follows formally from analytic-rank hypotheses once the class exists.  
**Falsifier:** inspect whether the analytic-rank/nonvanishing statement appears as theorem or conjecture and whether projection/localization is injective at the required root information.  
**Finding:** construction/comparison are theorems, while the higher-rank arithmetic significance is explicitly conjectural. Richness of representation is not a nonvanishing theorem.  
**Vote:** `REPRESENTATION_PROMISING / ROOT_BRIDGE_OPEN`.

## Role 3 — Iwasawa / Euler-system lead

**Background:** anticyclotomic Iwasawa theory, Heegner-point main conjectures, Euler systems, Selmer ranks.  
**Evidence inspected:** Fornea--Gehrmann arXiv:2311.03100v2.  
**Strongest counter-hypothesis:** the theorem can be read as analytic rank two forcing p-Selmer rank two.  
**Falsifier:** write the implication with every hypothesis as an arrow.  
**Finding:** nonvanishing of the mock plectic invariant is an explicit premise; the theorem proves `Q_K != 0 -> r_p(E/K)=2` under its setup. Reversing or deleting the nonvanishing premise is not licensed.  
**Vote:** `DOWNSTREAM_THEOREM_VALID / UPSTREAM_NONVANISHING_MISSING`.

## Role 4 — heights / regulators lead

**Background:** Néron--Tate and p-adic heights, derived heights, Bockstein regulators, leading terms.  
**Evidence inspected:** Hernández--Molina v2 and the existing A1a1 derived-height context; Howard-style derived-height interpretation retained as background.  
**Strongest counter-hypothesis:** plectic points already provide a proved rank-two p-adic regulator determinant.  
**Falsifier:** identify whether the regulator interpretation is theorem-level and whether its nondegeneracy follows from complex analytic rank.  
**Finding:** the plectic-regulator interpretation is described conjecturally in the source family. The proved p-adic Gross--Zagier formula is valuable but does not establish root-faithful regulator nondegeneracy from the complex premise.  
**Vote:** `NONDEGENERACY_NOT_SOURCE_CLOSED`.

## Role 5 — adversarial gluing / circularity lead

**Background:** proof-interface auditing, hidden equivalent-strength assumptions, countermodel construction.  
**Evidence inspected:** theorem/conjecture matrix and current A1a1 dual-memory warnings.  
**Strongest counter-hypothesis:** representation rotation itself constitutes progress enough to launch a new candidate theorem.  
**Falsifier:** demand a theorem-bearing first arrow before downstream machinery is counted as root progress.  
**Finding:** the new representation localizes the missing arrow more clearly but does not verify it. Launching a theorem candidate now would rename the obstruction.  
**Vote:** `NO_NEW_MATHEMATICAL_CANDIDATE`.

## Role 6 — formal assurance / RAKL provenance lead

**Background:** RAKL chronology, content identity, dual memory, authority boundaries, application/framework pinning.  
**Evidence inspected:** current RAKL `main@bd1a2768...`; current RAKL_math `main@6557b1b...`; final framework-pin integration receipt; RAKL issue #142 identity-collision evidence.  
**Strongest counter-hypothesis:** a fresh child atom can be assigned an intuitive human label immediately.  
**Falsifier:** test whether the current runtime supplies protected globally unique atom reservation before a concurrent branch can reuse the label.  
**Finding:** no such promotion-grade reservation is established here. Keep A1a1 canonical and describe the future child semantically without allocating a new primary ID. Current framework semantic authority and execution pin are prospectively synchronized, while historical artifact-local bindings remain unchanged.  
**Vote:** `PROVENANCE_CLEAN / CHILD_ID_WITHHELD`.

## Role 7 — novelty / research-value lead

**Background:** current number-theory frontier, rediscovery risk, information-gain assessment.  
**Evidence inspected:** Fornea 2026, Fornea--Gehrmann, Hernández--Molina v2, previous A1a1 current-frontier audit.  
**Strongest counter-hypothesis:** plectic work is merely another notation for the already-audited scalar theta-order path.  
**Falsifier:** identify genuinely different mathematical objects and proved maps absent from the previous scalar-order audit.  
**Finding:** plectic classes are genuinely richer partially global cohomological objects and the p-adic derivative-to-plectic theorem is a materially different near-solved context. The root-facing nonvanishing arrow is nevertheless still unproved in the audited chain.  
**Vote:** `RETAIN_SOURCE_AND_RELATION_NOVELTY / NO_THEOREM_NOVELTY_CLAIM`.

## Cell synthesis

**Consensus:** the representation rotation is informative and should be retained as a source-bound route refinement. It exposes a sharper interface:

```text
complex analytic rank two
  -> [MISSING / conjectural in audited plectic family]
plectic nonvanishing or root-faithful regulator
  -> [strong scoped downstream theorems exist]
p-primary rank information.
```

**Strongest objection:** the source family is special in field, prime, reduction and automorphic hypotheses, so even a future plectic nonvanishing theorem would need an additional scope-transfer audit before it could serve generic BSD over `Q`.

**Decision:** `PARTIAL_SUCCESS / REPRESENTATION_ROTATION_REFINES_RESIDUAL / CANDIDATE_GENERATION_BLOCKED`.

**Next discriminator:** source-bound search for an exact complex Gross--Zagier/higher Gross--Zagier or explicit-reciprocity theorem whose hypotheses start from the complex analytic rank-two datum and whose conclusion supplies nonzero plectic/global rank-two arithmetic information without importing the desired rank conclusion.