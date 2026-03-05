# AGENTS.md

## Cursor Cloud specific instructions

### Overview

KotorBlender is a pure-Python Blender extension for importing/editing/exporting Star Wars: KotOR game assets (MDL models, LYT layouts, PTH paths). The only runtime dependency is **Blender** (4.2 LTS recommended, also compatible with 3.6 and 5.0).

### Blender installation

Blender 4.2 LTS is installed at `/opt/blender/blender` with a symlink at `/usr/local/bin/blender`. The `libegl1` package is also required for GUI mode.

### Extension setup

The add-on is symlinked into Blender's extensions directory:
```
~/.config/blender/4.2/extensions/user_default/io_scene_kotor -> /workspace/io_scene_kotor
```
It is enabled persistently in Blender user preferences (module name: `bl_ext.user_default.io_scene_kotor`).

### Key commands

- **Build extension package:** `make build` (outputs to `./build/`)
- **Run tests:** `DATA_DIR=/path/to/kotor/assets make test` (requires extracted KotOR game assets — not available in cloud)
- **Lint:** `python3 -m ruff check io_scene_kotor/` (no project-level ruff config exists; 400+ pre-existing warnings from star imports etc.)
- **Syntax check:** `python3 -c "import py_compile, os; [py_compile.compile(os.path.join(r,f), doraise=True) for r,_,fs in os.walk('io_scene_kotor') for f in fs if f.endswith('.py')]"`

### Gotchas

- The E2E test suite (`make test`) requires `DATA_DIR` pointing to extracted KotOR BIF archives (proprietary game data). Without these assets, the test script will fail immediately. You can still verify add-on loading and core I/O (PTH, LYT) via background-mode Python scripts.
- To enable the extension via Python in Blender 4.2+, use `bpy.ops.preferences.addon_enable(module='bl_ext.user_default.io_scene_kotor')` (not the bare module name `io_scene_kotor`).
- Blender GUI mode requires `libegl1` system package. Background mode (`blender --background`) works without it.
- The codebase has no `pyproject.toml`, `setup.cfg`, or formal linting config. All 80 `.py` files are validated via `py_compile`.
