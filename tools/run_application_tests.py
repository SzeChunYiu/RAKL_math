#!/usr/bin/env python3
"""Run all RAKL_math application tests against one exact RAKL checkout."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import string
import subprocess
import sys
from typing import NoReturn


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = REPOSITORY_ROOT / "config" / "rakl-framework-pin.json"
# Every file reachable through the injected Python search root is authority
# bearing. Checking only ``src/rakl`` would let an untracked ``src/sitecustomize.py``
# execute before pytest while still presenting the pinned RAKL package commit.
AUTHORITY_PATHS = ("src", "schemas", "pyproject.toml")


def fail(message: str) -> NoReturn:
    print(f"framework pin check failed: {message}", file=sys.stderr)
    raise SystemExit(2)


def git(framework: Path, *arguments: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(framework), *arguments],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        fail(f"git {' '.join(arguments)} failed for {framework}: {detail}")
    return completed.stdout.strip()


def load_pin() -> dict[str, str]:
    try:
        pin = json.loads(PIN_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {PIN_PATH}: {exc}")

    required = {"repository", "commit"}
    if not isinstance(pin, dict) or not required.issubset(pin):
        fail(f"{PIN_PATH} lacks required fields: {sorted(required)}")
    if (
        not isinstance(pin["commit"], str)
        or len(pin["commit"]) != 40
        or any(character not in string.hexdigits.lower() for character in pin["commit"])
        or pin["commit"] != pin["commit"].lower()
    ):
        fail("configured commit is not a full 40-character SHA")
    return pin


def verify_application_gitlink(pin: dict[str, str]) -> None:
    completed = subprocess.run(
        [
            "git",
            "-C",
            str(REPOSITORY_ROOT),
            "rev-parse",
            "HEAD:framework/RAKL",
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        fail(f"cannot read committed framework/RAKL gitlink: {detail}")
    gitlink_commit = completed.stdout.strip()
    if gitlink_commit != pin["commit"]:
        fail(
            f"framework gitlink is {gitlink_commit}, expected configured "
            f"{pin['commit']}"
        )


def locate_framework(explicit: str | None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    elif os.environ.get("RAKL_FRAMEWORK_PATH"):
        candidates.append(Path(os.environ["RAKL_FRAMEWORK_PATH"]))
    else:
        candidates.extend(
            [
                REPOSITORY_ROOT / "framework" / "RAKL",
                REPOSITORY_ROOT.parent / "RAKL",
                REPOSITORY_ROOT.parent.parent / "RAKL",
            ]
        )

    for candidate in candidates:
        resolved = candidate.expanduser().resolve()
        if (resolved / ".git").exists() and (resolved / "src" / "rakl").is_dir():
            return resolved

    rendered = ", ".join(str(candidate) for candidate in candidates) or "none"
    fail(
        "no RAKL checkout found; pass --framework or set RAKL_FRAMEWORK_PATH "
        f"(checked: {rendered})"
    )


def normalized_repository(value: str) -> str:
    value = value.strip().removesuffix(".git").removesuffix("/")
    if value.startswith("git@github.com:"):
        value = "https://github.com/" + value.removeprefix("git@github.com:")
    return value


def verify_framework(framework: Path, pin: dict[str, str]) -> None:
    actual_commit = git(framework, "rev-parse", "HEAD")
    if actual_commit != pin["commit"]:
        fail(
            f"framework HEAD is {actual_commit}, expected pinned {pin['commit']}"
        )

    remote_urls = git(framework, "remote", "get-url", "--all", "origin").splitlines()
    expected_repository = normalized_repository(pin["repository"])
    if expected_repository not in {normalized_repository(url) for url in remote_urls}:
        fail(
            "framework origin does not match configured repository "
            f"{pin['repository']}"
        )

    dirty = git(
        framework,
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
        "--",
        *AUTHORITY_PATHS,
    )
    if dirty:
        fail(
            "framework authority paths are not clean; refusing an unpinned "
            f"effective implementation:\n{dirty}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--framework",
        help="path to a clean RAKL checkout at the configured exact commit",
    )
    parser.add_argument(
        "pytest_args",
        nargs=argparse.REMAINDER,
        help="additional pytest arguments after --",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pin = load_pin()
    verify_application_gitlink(pin)
    framework = locate_framework(args.framework)
    verify_framework(framework, pin)

    pytest_args = list(args.pytest_args)
    if pytest_args[:1] == ["--"]:
        pytest_args = pytest_args[1:]

    environment = os.environ.copy()
    environment.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONINTMAXSTRDIGITS": "0",
            "PYTHONNOUSERSITE": "1",
            "RAKL_FRAMEWORK_PATH": str(framework),
        }
    )
    verified_source = str(framework / "src")
    environment["PYTHONPATH"] = verified_source

    print(
        json.dumps(
            {
                "event": "rakl_framework_pin_verified",
                "repository": pin["repository"],
                "commit": pin["commit"],
                "framework_path": str(framework),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-q",
            str(REPOSITORY_ROOT / "tests" / "math_applications"),
            *pytest_args,
        ],
        cwd=REPOSITORY_ROOT,
        env=environment,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
