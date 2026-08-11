# NS-B1a3b1b1a-C001-R1 — finite terminal singular-point theorem does not close critical finite-center morphology

Status: `PARTIAL_SUCCESS / SCOPED_TRANSFER_ROUTE_PRUNING`  
Authority: `PROPOSAL_SHADOW_ONLY / ROOT_AUTHORITY_NONE`  
Novelty class: `transfer` (scoped RAKL classification; not a literature-novelty certificate)

## Exact scoped result

Under the exact hypotheses of Barker arXiv:2111.14776v2 Theorem 2, the terminal singular set at the first blow-up time contains at most `C_univ M^20` points. The proof establishes this by choosing a rescaling time from pairwise separation of a finite subset of terminal singular points, converting the backward-slice global `L^{3,infinity}` velocity bound into countably additive global spacetime velocity/pressure control, applying epsilon-regularity contrapositive at disjoint unit cylinders, and summing the resulting positive masses.

That theorem/proof does not establish the different quantitative statement required by the frozen target:

`A_lambda(t) subset union_{j=1}^{N0} B(x_j(t), R_lambda),  R_lambda <= C lambda^{-1/2}`

for preterminal vorticity super-level sets. The source scale `sqrt(-s_n)` is chosen from time and terminal-point separation, not from a vorticity level. No `lambda_vort -> distance` modulus is derived in the inspected proof.

Therefore the direct transfer

`finite terminal singular-set cardinality -> critical finite-center vorticity morphology`

is rejected at the source-interface gate. The finite-point theorem remains useful source knowledge; only this proposed bridge is pruned.

## Falsifier execution

Frozen falsifier: find in the source theorem/proof a quantitative estimate coupling a vorticity threshold to distance from the terminal singular set with the critical exponent `1/2`.

Outcome: `FALSIFIER_TRIGGERED_FOR_DIRECT_TRANSFER`. The inspected proof contains the terminal cardinality packing argument but no such vorticity-level radius estimate. The result is negative for the proposed transfer, not negative for the source theorem.

## Local failure versus gluing failures

Local/source-interface failure:
- `F-NS-B1a3b1b1a-CARDINALITY-NOT-CRITICAL-RADIUS` — terminal exceptional-set count lacks the target quantitative level-to-radius modulus.

Separate local-to-global/state-space gluing residuals:
- `G-NS-B1a3b1b1a-TERMINAL-TO-PRETERMINAL-MORPHOLOGY` — terminal singular points do not yet furnish controlled preterminal high-vorticity center trajectories/cover.
- `G-NS-B1a3b1b1a-FAR-FIELD-GLOBAL-SUPERLEVEL-COVER` — noncompact whole-space far field is not globally covered by local regularity away from terminal singular points without a uniform tail statement.
- `G-NS-B1a3b1b1a-VELOCITY-TO-VORTICITY-CONSUMER-STATE` — the source velocity-critical state does not itself produce weak-`L^{3/2}` vorticity amplitude or log-BMO direction.

No backward-uniqueness failure is asserted because the audited proof does not invoke backward uniqueness. No limit-passage failure is claimed inside the local theorem inspection; ancient-limit transport is simply outside this result and remains open.

## Episode -> diagnosis -> reusable obstruction/lesson separation

Episode: execute the prospectively frozen source-interface discriminator on Barker Theorem 2/proof.

Diagnosis: the proposed transfer confuses two distinct quantitative objects — finite terminal exceptional-set cardinality and a preterminal vorticity level-to-distance modulus.

Reusable obstruction: `O-NS-B1a3b1b1a-MISSING-LEVEL-RADIUS-MODULUS` — any route that imports a finite exceptional-set/count theorem into a scale-critical morphology consumer must separately prove the consumer's quantitative scale law and global support/quantifier interfaces.

Candidate lesson: `L-NS-B1a3b1b1a-R1-CARDINALITY-IS-NOT-MORPHOLOGY-MODULUS`, proposal/shadow only. Experience may guide routing but grants no theorem authority.

Motif: `M-NS-FINITE-EXCEPTIONAL-COUNT-VS-QUANTITATIVE-SCALE` — inspect whether an exceptional-set theorem controls only count/location or also the target level-dependent modulus before gluing it into a quantitative consumer.

## Routing consequence

Do not spend the next cycle attempting to plug Barker's point count directly into the Grujić finite-center consumer. The high-information residual is a genuinely quantitative NSE producer: derive/source a `lambda`-dependent finite-center radius law (with far-field and preterminal quantifiers), or rotate to a consumer whose source-family requirement is only terminal finite singularity/cardinality and whose remaining amplitude/direction assumptions can be produced independently.

Root #4 remains `OPEN_NO_SOLUTION_CERTIFICATE`; Type II remains untouched; independent mathematical reviews remain `0/3`.
