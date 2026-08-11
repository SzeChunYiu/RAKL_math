# RH-SPEC-002 negative history — PR #15 chronology and hash failure

Date: 2026-08-11. Authority: `NEGATIVE_HISTORY / ASSURANCE_REPAIR / NO_RH_EVIDENCE / ROOT_AUTHORITY_NONE`.

PR #15 first committed its calibration result as `c48f2df` and only later added `b22e345`, a continuation asserting that the exact calibration candidate had been proposed before execution. The earlier accepted `RH-SPEC-002-E07` selected a broad hostile limit-stability calibration, but no repository-visible exact five-case/evaluator identity predates the result commit. Later event timestamps do not repair that evidence gap.

The PR also failed exact local verification at head `7f45008d`: the Hurwitz tool stored hash `sha256:8ecd4553...`, while canonical recomputation gave `sha256:4a1a006c...`. Focused verification was `10 passed, 1 failed`; the full exact pin runner was `172 passed, 1 failed`.

## Bounded diagnosis

The independently checkable mathematical examples remain useful:

- Hurwitz/Rouché target-side zero transport under its exact hypotheses;
- disappearing spectrum under strong-resolvent convergence;
- Galerkin gap pollution;
- path-dependent two-parameter limits;
- exact finite real-zero prefix agreement without locally uniform target convergence.

What failed was assurance authority, not those standard constructions. They are assimilated only as `RETROSPECTIVE_KNOWN_ANSWER_CALIBRATION / SEARCH_CONTROL_ONLY`. The implication that the exact suite was demonstrably frozen before evaluation is superseded. No preregistration is backfilled.

The separate local 11-case calibration whose evaluator was committed at `bdbbd4c` before execution has a distinct calibration id and lineage. It is not imported, merged, or used to rescue PR #15.
