# Testing

KotorBlender uses two test layers:

- **Unit tests (no Blender)** — Live under `test/unit/`. They use **pytest** and run with system Python only (no `bpy`). They cover format parsers (GFF, TPC), constants, and option defaults. Use `make test-unit` or `pytest test/unit -v`. The VS Code/Cursor Python Test Adapter discovers only these tests, so you get a working Test Explorer without Blender.

- **Blender tests** — Live under `test/blender/test_*.py`. They run **inside Blender** in background mode (`blender --background --python ...`). They cover registration, operators, PTH/LYT/AABB, utils that need `bpy`, and minimal MDL roundtrip. Use `make test` to run all of them, or `make test-registration`, `make test-gff`, etc. On Windows, use `test/run_blender_tests.py` if Blender is not on `PATH`. See [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

- **E2E tests** — Full MDL roundtrip against extracted KotOR game assets. They require a path to extracted BIF data and are not run in CI.

## Running E2E tests

From a terminal (Linux or MSYS on Windows):

1. `DATA_DIR=/path/to/assets [TSL=?] [OFFSET=?] [LIMIT=?] make test-e2e`

where:

- `DATA_DIR` is path to a directory containing assets extracted from BIF archives (required for E2E)
- `TSL` is a flag indicating use of TSL model format (0 or 1, defaults to 0)
- `OFFSET` is an offset into the list of models in the data directory (defaults to 0)
- `LIMIT` is the maximum number of models to process (defaults to 50)

Note: `make test` runs only Blender asset-free tests. `make test-unit` runs pytest unit tests (no Blender). Use `make test-e2e` with `DATA_DIR` set for the full E2E suite.
