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
