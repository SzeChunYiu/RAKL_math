# Same-context source-audit review — BSD-A1a1b

**Atom under preparation:** `BSD-A1a1b-HIGHER-EVEN-ORDER-EXCLUSION`  
**Review kind:** source/context review only; not independent mathematical review.  
**Candidate status:** none.  
**Root authority:** none.

The cell was convened after the parent parity route exposed the higher-even-order residual. Every role reviewed the same bounded primary-source packet but was assigned a distinct objection and falsifier.

## 1. Analytic / automorphic lead

**Background:** complex and p-adic L-functions, Rankin–Selberg families, functional equations, interpolation and leading terms.  
**Delegated question:** can exact complex analytic rank two itself constrain the anticyclotomic `J`-order beyond parity and positivity?  
**Evidence:** Castella–Hsieh interpolation and leading-term sections; distinction between the complex `s` variable and anticyclotomic character coordinate.  
**Finding:** the inspected interpolation formula supplies central values along the anticyclotomic family, not an identity of complex-`s` and character-direction derivatives. Functional equation controls parity, not the upper order.  
**Strongest counter-hypothesis:** a deeper automorphic comparison theorem may identify the two leading orders under special auxiliary choices.  
**Vote:** REVISE the representation toward an explicit derivative/height comparison; no candidate yet.

## 2. Iwasawa / derived-height lead

**Background:** `Z_p`-extensions, characteristic ideals, derived p-adic heights, augmentation filtrations and semisimplicity.  
**Delegated question:** what structural phenomenon would permit theta order `4,6,...`?  
**Evidence:** Howard's derived-height theory and Castella–Hsieh Theorem 4.1 / §5.3–5.4.  
**Finding:** deeper vanishing is naturally encoded by persistence of the derived-height filtration and by non-semisimple `J`-primary Iwasawa structure. In the rank-two Selmer analysis, even filtration depths appear explicitly.  
**Falsifier attempted:** search for a source statement making theta order depend only on the complex root sign/order. None was found in the inspected sources.  
**Vote:** ACCEPT the semisimplicity/nondegeneracy diagnosis as the best current structural coordinate; BLOCK any claim that it is the only possible diagnosis.

## 3. Arithmetic geometry / Selmer / Sha lead

**Background:** Mordell–Weil groups, Selmer groups, Tate–Shafarevich groups, Gross–Zagier/Kolyvagin and regulators.  
**Delegated question:** which apparent order-two routes are circular for the BSD analytic-to-arithmetic direction?  
**Finding:** assuming `dim Sel=2`, positive Mordell–Weil rank, Sha finiteness sufficient to identify Selmer with Mordell–Weil, or a maximal arithmetic regulator already supplies downstream arithmetic information not contained in bare analytic rank two. These hypotheses must remain visible rather than being used as harmless technical conditions.  
**Vote:** BLOCK all such routes as first bridges unless their arithmetic input is independently derived from the complex premise.

## 4. Analogy / method-transfer lead

**Background:** structural transfer across deformation theory, spectral multiplicity and degeneracy problems.  
**Delegated analogy:** distinguish a zero-order statement in one deformation coordinate from degeneracy of a transverse regulator/linearization.  
**Retained abstraction:** higher-order persistence often signals that the first expected transverse linear/regulator map is degenerate. This motivates testing derived-height nondegeneracy rather than guessing another theta identity.  
**Disanalogy:** the complex and p-adic objects are not a common smooth bivariate function, and no Euclidean transversality theorem transfers.  
**Vote:** ACCEPT as proposal-only re-representation with an explicit target-domain validation obligation.

## 5. Adversarial circularity / falsification lead

**Background:** proof auditing, hidden assumptions, converse failures, local/global mismatches.  
**Hostile checks:**
- replace complex analytic rank two by only root sign `+1`: parity survives but no upper bound appears;
- assume `dim Sel=2`: strong filtration restrictions appear, exposing the extra arithmetic coordinate;
- assume a p-adic BSD/main conjecture: order/leading information becomes available, exposing the increase in logical strength;
- transfer BDP p-adic order results literally to `Theta_{f/K}`: object/Selmer-condition mismatch blocks the transfer.

**Vote:** ACCEPT route pruning; REJECT any impossibility statement or silent object identification.

## 6. Formal assurance / dependency lead

**Background:** exact theorem statements, proof DAGs, dependency/axiom audits, RAKL chronology.  
**Delegated task:** classify the implication edges.

Current source graph:

`complex analytic rank 2`

`->? anticyclotomic derived-height nondegeneracy / semisimplicity`

`-> theta order <=2`

while existing strong routes instead look like

`Selmer filtration / main conjecture / p-adic BSD input -> order or leading-term control`.

The first arrow is the unclosed root-critical bridge. Parent exact-head CI is still required, and the child has not yet received a strict pre-candidate packet.  
**Vote:** BLOCK child candidate generation.

## 7. Novelty / frontier lead

**Background:** primary-source discovery, chronology and equivalence checking.  
**Sources checked:** Howard 1202.6343; Castella–Hsieh 2022; Castella–Hsu–Kundu–Lee–Liu 2308.10474; Sano 2308.08875.  
**Finding:** the bounded search found derived-height, semisimplicity, main-conjecture and p-adic-BSD routes to p-adic order/leading data, but no direct theorem from exact complex analytic rank two alone to the required higher-even-order exclusion.  
**Boundary:** absence in this bounded search is not a nonexistence result and does not support novelty authority.  
**Vote:** CONTINUE targeted source search after a fresh child context is frozen.

## Cell synthesis

The cell unanimously rejects “try another functional equation” as the immediate mode. The highest-information re-representation is:

> excess even theta vanishing is a candidate symptom of anticyclotomic derived-height degeneracy / Iwasawa non-semisimplicity, so the missing bridge should be searched for as `complex analytic rank two -> arithmetic nondegeneracy/semisimplicity`, with every Selmer/main-conjecture assumption strength-audited.

This conclusion is **research-control only**. It creates no theorem, no impossibility claim, no novelty claim and no BSD authority.
