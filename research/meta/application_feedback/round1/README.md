# Application-to-framework feedback round 1

This packet exports four lessons observed during the RAKL mathematical
application split without promoting any lesson into RAKL:

1. The migrated `O9d12a2a1a` source trace was byte-preserved, but six stored
   event hashes were not canonical hashes of their exact payloads. The exact
   source-side cause remains unresolved. The failed identity is preserved and a
   separately identified trace repairs only identity/hash-chain fields.
2. A migrated RH test retained `parents[1]` after moving one directory deeper,
   so it resolved application artifacts below `tests/research/` and failed
   before reaching a mathematical gate.
3. Framework commit `209a030` removed application artifacts while retaining
   application-owned regressions. One exact P/NP test produced two missing-file
   failures. The destination artifacts/tests were preserved in `RAKL_math`
   before 19 migrated regressions were removed from the framework suite.
4. The exact submodule/config/clean-authority runner passed the application
   suite at RAKL `15f1c3a`; this is a scoped tool candidate, not universal or
   scientific authority.

## Immutable transport

- Producer commit: `590b96278bb0bd4c89bc5db4bfe265061c52846a`
- Framework contract: `15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`
- Bundle SHA-256: `cbc37595c5cae92e81fdf32405f951e747d42e87c5633c7f834833ae96f12520`
- Import receipt: `rakl::application-feedback-import::7523595e8f7ff4fc55024b8fda1941443820e2db6b0ed0437007a7fdf422f5a4`
- Import verdict: `QUARANTINED_PROPOSAL`

Each item binds its source payload, result, trace and context to exact paths,
Git blobs and raw SHA-256 values at the producer commit. The bundle is
self-hashing and the builder reconstructs it in a detached producer checkout.
The builder also checks that every trace names the bound result and context,
that its strict-UTC observation time does not postdate the producer commit, and
that producer commit `590b962` remains an ancestor of the checked-out history.

The feedback importer is loaded only after a clean, correct-origin framework
object source has produced a separate detached checkout at exact historical
framework commit `15f1c3a`. The current application framework pin may advance
without changing this historical receipt; it is not used as the import
authority merely because it is the current submodule `HEAD`.

`QUARANTINED_PROPOSAL` means transport and chronology bindings passed. It does
not mean a diagnosis, tool, or framework change is correct, reusable, novel, or
promoted. The receipt records no tool-inventory mutation, no failure-lattice
mutation, no scientific authority and no method promotion.

## Candidate framework deltas remain unvalidated

The payloads propose, but do not adopt:

- byte-preservation plus canonical re-audit and immutable failed identities for
  migrated hash chains;
- explicit test-root rebinding assurance after layout changes;
- a bidirectional ownership manifest for repository splits;
- an exact-pin runner pattern with destination-specific authority-surface and
  test-discovery validation.

Each proposal still requires a frozen framework evaluator, known-answer PASS,
planted FAIL, structural `CANNOT_CHECK`, fresh assurance and protected RAKL
promotion. One application round is not cross-problem recurrence.

## Reproduction

```bash
python tools/build_application_feedback_round1.py \
  --producer-commit 590b96278bb0bd4c89bc5db4bfe265061c52846a \
  --check
python tools/run_application_tests.py --framework framework/RAKL
```

Full Git history is required because the transport artifacts are in the child
of producer commit `590b962`. PR #24 was merged with merge commit `96d52e1`, so
the producer remains reachable from `main`; squash or rebase integration would
not have preserved that exact chronology.
