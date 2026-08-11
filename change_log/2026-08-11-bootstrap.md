# 2026-08-11: application bootstrap and framework pin

- Added repository-specific agent, goal, architecture and development guidance
  after `bootstrap-ai-project` failed before writing files. The two attempts
  reported `command substitution: line 651: syntax error near unexpected token
  ')'` and `line 608: so: command not found`; the repository remained clean.
- Bound the authoritative RAKL framework gitlink to matching machine-readable
  config and made disagreement fail closed.
- Added a fail-closed runner and CI for the full migrated application suite.
- Corrected migrated test repository-root resolution only; no scientific claim,
  receipt or evaluator was changed.

## Framework pin sync after repository split

Updated the exact framework gitlink/config pin from `7853ec0` to current RAKL
`15f1c3a` after the application split and proposal-only feedback channel merged.
The complete application suite passed `166` tests before the receipt assertion
was added. See `receipts/framework-pin-sync-15f1c3a-20260811.json`.
