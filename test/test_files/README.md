# Test assets for KotorBlender

This directory holds binary assets used by Blender background-mode tests. Layout and sources:

## unfixed/

Originals from **BINS.zip** (unfixed community models that fail in current KotorBlender). Used for diagnosis and comparing with fixed versions.

- Each `.mdl` must have a sibling `.mdx` in the same directory for the MDL reader.

## fixed/

Fixed versions (converted to K2) from **converted.rar**. Tests assert that these load successfully.

- Extracts into `fixed/converted/`; MDL/MDX pairs live there (e.g. `KOQ200_01a.mdl`, `KOQ200_01a.mdx`).

## Re-extracting

If this directory is missing or you need to refresh assets:

1. Create `test/test_files/`, then `unfixed/` and `fixed/`.
2. Extract BINS.zip into `unfixed/`.
3. Extract converted.rar into `fixed/` (e.g. with WinRAR, 7-Zip, or Python `rarfile` + `unrar` on PATH).

Game/mod binaries may be proprietary. The test suite does **not** skip when assets are missing: if `fixed/` or `unfixed/` (or `pykotor_mdl/`) are empty or missing, the corresponding tests **fail** with a clear message so you can add or re-extract assets (see above).

## Diagnosing reader strictness (unfixed vs fixed)

`diff_unfixed_fixed.py` diffs the first N bytes of an unfixed vs fixed MDL pair to help find where the binary reader is too strict. From repo root:

```bash
python test/test_files/diff_unfixed_fixed.py              # list basenames
python test/test_files/diff_unfixed_fixed.py KOQ200_01a 64  # diff first 64 bytes
```
