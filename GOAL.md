# Goal

Advance bounded atoms for the six unsolved Millennium Prize Problems while
building an auditable success/failure learning loop back into the RAKL
framework. This repository records mathematical application evidence; it does
not by itself certify that an open problem is solved.

## Product paths

- `research/`: exact contexts, candidates, evidence, falsifiers, negative
  history, reviews, traces and scoped lessons.
- `tests/`: application regression and governance tests.
- `tools/`: deterministic runners and receipt tooling.
- `schemas/`: machine-readable application and cross-repository handoff
  contracts.

## Acceptance boundary

1. The application suite passes against the exact framework SHA in
   `config/rakl-framework-pin.json` via `tools/run_application_tests.py`.
2. CI checks out that SHA rather than floating with RAKL `main`.
3. Every application artifact preserves chronology, evidence pointers and
   claim scope; missing evidence fails closed.
4. Every material success or failure lesson introduced is machine-readable,
   content-bound, scope-limited and checked by its lesson-ledger validator.
5. A proposed reusable RAKL delta is promoted only in a separate framework PR
   after frozen known-answer PASS, planted FAIL and structural CANNOT_CHECK
   evaluation.
6. No application test or infrastructure change alters a scientific result or
   upgrades computation, same-context reflection or proposal text into proof or
   independent review.

