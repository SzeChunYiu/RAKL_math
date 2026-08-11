# Development

## Exact application test suite

Initialize the RAKL framework submodule. Its gitlink must equal the SHA in
`config/rakl-framework-pin.json`, then run:

```bash
git submodule update --init framework/RAKL
python tools/run_application_tests.py --framework framework/RAKL
```

The runner rejects a different commit, a repository with a different origin,
or changes anywhere under `src`, `schemas`, or `pyproject.toml`. Checking the
whole injected `src/` search root prevents untracked startup modules such as
`sitecustomize.py` from bypassing the pin. The runner also disables user-site
imports and exposes only the verified framework `src/` directory.

To add pytest arguments, place them after `--`:

```bash
python tools/run_application_tests.py --framework /path/to/RAKL -- -x
```

## Framework pin updates

A pin update is a material dependency change. Review the RAKL diff, update both
the gitlink and machine-readable pin in its own PR, and rerun the complete
application suite. Do not float full CI at a branch name.
