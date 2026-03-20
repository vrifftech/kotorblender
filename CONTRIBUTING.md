# Contributing to KotorBlender

Thank you for your interest in contributing to KotorBlender. This document explains how to get started, run tests, and submit changes.

## Before you start

- **Small fixes** (typos, docs, single-operator tweaks) can go straight to a pull request.
- **Larger changes** (new features, refactors, format support) — please open an issue first to align with maintainers and the roadmap. This avoids duplicate work and ensures the approach fits the project.

## One topic per pull request

Keep each PR focused on a single logical change. Split refactors, new features, and bug fixes into separate PRs when possible. This makes review faster and history clearer.

## Tests and documentation

- **New behavior** should add or update tests where relevant, and update documentation (README, AGENTS.md, or in-code docstrings) as needed.
- **Existing tests** must continue to pass. Run the test suite before submitting (see below).

## How to run tests

KotorBlender is tightly coupled to the Blender Python API, so tests run inside Blender in background mode.

- **All background-mode tests (no game assets):**
  ```bash
  make test
  ```
  On Windows, if Blender is not on `PATH`, set the `BLENDER` environment variable to your Blender executable, or use `test/run_blender_tests.py` (see AGENTS.md).

- **Individual test modules** (for development):
  ```bash
  make test-registration   # Extension loading, operators
  make test-gff            # GFF binary format
  make test-pth            # PTH import/export
  make test-lyt            # LYT export
  make test-aabb           # AABB tree
  make test-constants       # Enums, utilities
  make test-mdl             # Minimal MDL roundtrip
  make test-community-mdl   # Community MDL load (if test_files present)
  ```

- **Test layout:** Tests live under `test/blender/test_*.py`. The runner is `test/run_blender_tests.sh` (Linux/macOS) or `test/run_blender_tests.py` (Windows). See [AGENTS.md](AGENTS.md) for the full test template and CI details.

- **E2E tests** (require extracted game assets) are not run in CI:
  ```bash
  DATA_DIR=/path/to/extracted/assets make test-e2e
  ```

## Code style

- **Lint:** We use `ruff` with a minimal rule set for CI. From the repo root:
  ```bash
  make lint
  ```
  This runs a syntax check and `ruff check --select E9,F821,F823` on `io_scene_kotor/`. Only errors that break the extension at load time are enforced; many pre-existing star-import warnings (F401/F403) are accepted. Match the style of the file you are editing and avoid introducing new blocking errors.

- **Reference:** [AGENTS.md](AGENTS.md) describes repository structure, Blender extension setup, and agent/CI conventions.

## Extension name (Blender 4.2+)

When enabling the extension from script or docs, use the full module name:

- **Blender 4.2+:** `bl_ext.user_default.io_scene_kotor`
- Not the bare name `io_scene_kotor` (that is the package directory name).

## Pull requests

Please use our [pull request template](.github/PULL_REQUEST_TEMPLATE.md) when opening a PR. It asks for a description of the problem, proposed solution, alternatives considered, limitations, and a short checklist (tests, lint, docs).
